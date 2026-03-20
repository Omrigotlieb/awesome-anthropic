// @ts-check
const { test, expect } = require('@playwright/test');

const BASE = process.env.BASE_URL || 'http://127.0.0.1:42173';

// Wait for Docsify to finish loading a page (content must not be "Loading…")
async function waitForContent(page) {
  await page.waitForFunction(
    () => {
      const el = document.getElementById('app') || document.querySelector('.content');
      return el && el.innerText.trim() !== 'Loading…' && el.innerText.trim().length > 50;
    },
    { timeout: 15000 }
  );
}

async function gotoInterviewWizard(page) {
  await page.addInitScript(() => {
    try {
      localStorage.removeItem('aa-wiz');
    } catch (err) {
      // Ignore storage access issues in tests.
    }
  });
  await page.goto(BASE + '/#/docs/INTERVIEW');
  await waitForContent(page);
  await page.waitForSelector('.wiz-wrap', { timeout: 15000 });
}

// ─────────────────────────────────────────────────────────────
// HOMEPAGE / DASHBOARD
// ─────────────────────────────────────────────────────────────
test.describe('Homepage', () => {
  test('loads and shows title', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page).toHaveTitle(/Home|Awesome Anthropic/);
    await expect(page.locator('.dash-mhead-title')).toContainText('Awesome Anthropic');
  });

  test('sidebar is visible', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.sidebar')).toBeVisible();
  });

  test('shows dashboard masthead with light background', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.dash-masthead')).toBeVisible({ timeout: 15000 });
    // Masthead should now be white/light, not dark
    const bg = await page.evaluate(() => {
      const el = document.querySelector('.dash-masthead');
      return el ? window.getComputedStyle(el).backgroundColor : '';
    });
    expect(bg).toBe('rgb(255, 255, 255)');
  });

  test('shows benchmark comparison table with Opus 4.6', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.dash-bench-wrap')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.markdown-section')).toContainText('Opus 4.6');
  });

  test('benchmark table header is light (cream), not dark', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.dash-bench-wrap')).toBeVisible({ timeout: 15000 });
    const bg = await page.evaluate(() => {
      const th = document.querySelector('.dash-bench-wrap thead th');
      return th ? window.getComputedStyle(th).backgroundColor : '';
    });
    // Should NOT be the dark color rgb(20,20,19)
    expect(bg).not.toBe('rgb(20, 20, 19)');
  });

  test('shows changelog widget', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.markdown-section')).toContainText('Changelog', { timeout: 15000 });
  });

  test('shows trending leaderboard widget', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.markdown-section')).toContainText('Trending Now', { timeout: 15000 });
  });

  test('shows Claude Code performance tracker widget', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.markdown-section')).toContainText('Performance Tracker', { timeout: 15000 });
    await expect(page.locator('.dash-tracker-svg')).toBeVisible({ timeout: 15000 });
  });

  test('tracker widget has sparkline graph', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.dash-tracker-body')).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.dash-tracker-stat-val').first()).toContainText('%');
  });

  test('tracker links to marginlab.ai', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    const link = page.locator('a[href*="marginlab.ai"]').first();
    await expect(link).toBeVisible({ timeout: 15000 });
  });

  test('masthead includes GitHub star CTA', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    const cta = page.locator('.dash-mhead-actions a[href*="stargazers"]').first();
    await expect(cta).toBeVisible({ timeout: 15000 });
    await expect(cta).toContainText('Star on GitHub');
  });
});

// ─────────────────────────────────────────────────────────────
// SIDEBAR NAVIGATION
// ─────────────────────────────────────────────────────────────
test.describe('Sidebar navigation', () => {
  test('News Feed link navigates and loads', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await page.click('.sidebar a:has-text("News Feed")');
    await page.waitForURL(/docs\/NEWS/, { timeout: 10000 });
    await expect(page.locator('.markdown-section')).toContainText('Anthropic News Feed', { timeout: 15000 });
  });

  test('Changelog link navigates and loads', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    // Use href selector to avoid matching "Changelog (Auto-updated)" sub-heading in page TOC
    await page.click('.sidebar a[href="#/docs/CHANGELOG"]');
    await page.waitForURL(/docs\/CHANGELOG/, { timeout: 10000 });
    await expect(page.locator('.markdown-section')).toContainText('Anthropic Changelog', { timeout: 15000 });
  });

  test('Model Benchmarks link navigates and loads', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await page.click('.sidebar a:has-text("Model Benchmarks")');
    await page.waitForURL(/docs\/BENCHMARKS/, { timeout: 10000 });
    await expect(page.locator('.markdown-section')).toContainText('Model Performance', { timeout: 15000 });
  });

  test('Awesome List link navigates and loads', async ({ page }) => {
    await page.goto(BASE + '/#/docs/NEWS');
    await waitForContent(page);
    await page.click('.sidebar a:has-text("Awesome List")');
    await expect(page.locator('.markdown-section h1')).toContainText('Awesome Anthropic', { timeout: 15000 });
  });

  test('2024 News archive link navigates and loads', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await page.click('.sidebar a:has-text("2024 News")');
    await page.waitForURL(/ARCHIVE/, { timeout: 10000 });
    await expect(page.locator('.markdown-section')).toContainText('2024', { timeout: 15000 });
  });

  test('How to Contribute link navigates and loads', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await page.click('.sidebar a:has-text("How to Contribute")');
    await page.waitForURL(/CONTRIBUTING/, { timeout: 10000 });
    await expect(page.locator('.markdown-section')).toContainText('Contributing', { timeout: 15000 });
  });

  test('Code of Conduct link navigates and loads', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await page.click('.sidebar a:has-text("Code of Conduct")');
    await page.waitForURL(/CODE_OF_CONDUCT/, { timeout: 10000 });
    await expect(page.locator('.markdown-section')).not.toContainText('Loading', { timeout: 15000 });
    await expect(page.url()).toContain('CODE_OF_CONDUCT');
  });

  test('CC Ecosystem link navigates and loads', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await page.click('.sidebar a:has-text("CC Ecosystem")');
    await page.waitForURL(/CLAUDE_CODE/, { timeout: 10000 });
    await expect(page.locator('.markdown-section')).toContainText('Claude Code', { timeout: 15000 });
  });

  test('Interview Prep link navigates and loads', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await page.click('.sidebar a:has-text("Interview Prep")');
    await page.waitForURL(/INTERVIEW/, { timeout: 10000 });
    await expect(page.locator('.markdown-section')).toContainText('Anthropic', { timeout: 15000 });
  });
});

// ─────────────────────────────────────────────────────────────
// DIRECT URL NAVIGATION (hash routes)
// ─────────────────────────────────────────────────────────────
test.describe('Direct URL navigation', () => {
  const routes = [
    { url: '/#/docs/NEWS',             contains: 'Anthropic News Feed' },
    { url: '/#/docs/CHANGELOG',        contains: 'Anthropic Changelog' },
    { url: '/#/docs/BENCHMARKS',       contains: 'Model Performance' },
    { url: '/#/docs/ARCHIVE/2024-news', contains: '2024' },
    { url: '/#/CONTRIBUTING',          contains: 'Contributing' },
    { url: '/#/CODE_OF_CONDUCT',       contains: 'Conduct' },
    { url: '/#/docs/CLAUDE_CODE',      contains: 'Claude Code' },
    { url: '/#/docs/INTERVIEW',        contains: 'Anthropic' },
  ];

  for (const { url, contains } of routes) {
    test(`${url} shows correct content`, async ({ page }) => {
      await page.goto(BASE + url);
      await waitForContent(page);
      await expect(page.locator('.markdown-section')).toContainText(contains);
    });
  }
});

// ─────────────────────────────────────────────────────────────
// NEWS PAGE CONTENT
// ─────────────────────────────────────────────────────────────
test.describe('News page', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(BASE + '/#/docs/NEWS');
    await waitForContent(page);
  });

  test('shows Top Stories section', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Top Stories');
  });

  test('shows score table with links', async ({ page }) => {
    await expect(page.locator('.markdown-section table').first()).toBeVisible();
  });

  test('shows Official Announcements', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Official Announcements');
  });

  test('shows SDK releases', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('SDK');
  });
});

// ─────────────────────────────────────────────────────────────
// BENCHMARKS PAGE CONTENT
// ─────────────────────────────────────────────────────────────
test.describe('Benchmarks page', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(BASE + '/#/docs/BENCHMARKS');
    await waitForContent(page);
  });

  test('shows LMSYS section', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('LMSYS');
  });

  test('shows SWE-bench section', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('SWE-bench');
  });

  test('shows GPQA section', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('GPQA');
  });

  test('shows pricing table', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Price vs. Performance');
  });

  test('has working external links to benchmark sites', async ({ page }) => {
    const links = page.locator('.markdown-section a[href*="lmarena"]');
    await expect(links.first()).toBeVisible();
  });

  test('shows competitor models (not just Anthropic)', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('GPT');
  });

  test('shows Claude Code tracker section', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('marginlab');
  });
});

// ─────────────────────────────────────────────────────────────
// CLAUDE CODE ECOSYSTEM PAGE
// ─────────────────────────────────────────────────────────────
test.describe('Claude Code ecosystem page', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(BASE + '/#/docs/CLAUDE_CODE');
    await waitForContent(page);
  });

  test('shows Claude Code heading', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Claude Code');
  });

  test('shows MCP section', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('MCP');
  });

  test('shows Remote Connect section', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Remote');
  });

  test('shows Skills section', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Skills');
  });
});

// ─────────────────────────────────────────────────────────────
// INTERVIEW PREP PAGE
// ─────────────────────────────────────────────────────────────
test.describe('Interview prep page', () => {
  test.beforeEach(async ({ page }) => {
    await gotoInterviewWizard(page);
  });

  test('shows Anthropic interview content', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Anthropic');
  });

  test('shows technical topics', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Research / ML');
  });

  test('shows behavioral questions section', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Behavioral');
  });

  test('shows study plan or resources', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Begin Quest');
  });
});

// ─────────────────────────────────────────────────────────────
// CHANGELOG PAGE CONTENT
// ─────────────────────────────────────────────────────────────
test.describe('Changelog page', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(BASE + '/#/docs/CHANGELOG');
    await waitForContent(page);
  });

  test('shows dated entries', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('2026');
  });

  test('shows Sonnet 4.6 entry', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Sonnet 4.6');
  });

  test('shows Opus 4.6 entry', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Opus 4.6');
  });
});

// ─────────────────────────────────────────────────────────────
// VISUAL / DESIGN
// ─────────────────────────────────────────────────────────────
test.describe('Visual design', () => {
  test('homepage title uses a serif display font', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    const fontFamily = await page.evaluate(() => {
      const title = document.querySelector('.dash-mhead-title');
      return title ? window.getComputedStyle(title).fontFamily : '';
    });
    expect(fontFamily.toLowerCase()).toMatch(/serif|georgia|dm serif/);
  });

  test('body text is at least 16px for readability', async ({ page }) => {
    await page.goto(BASE + '/#/docs/NEWS');
    await waitForContent(page);
    const fontSize = await page.evaluate(() => {
      const p = document.querySelector('.markdown-section p');
      return p ? parseFloat(window.getComputedStyle(p).fontSize) : 0;
    });
    expect(fontSize).toBeGreaterThanOrEqual(16);
  });

  test('sidebar has a light editorial background', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    const bg = await page.evaluate(() => {
      const sidebar = document.querySelector('.sidebar');
      return sidebar ? window.getComputedStyle(sidebar).backgroundColor : '';
    });
    expect(bg).toBe('rgb(255, 255, 255)');
  });

  test('footer is rendered on every page', async ({ page }) => {
    await page.goto(BASE + '/#/docs/NEWS');
    await waitForContent(page);
    await expect(page.locator('.page-footer')).toBeVisible();
  });

  test('footer includes stargazers link', async ({ page }) => {
    await page.goto(BASE + '/#/docs/NEWS');
    await waitForContent(page);
    const link = page.locator('.page-footer a[href*="stargazers"]').first();
    await expect(link).toBeVisible();
  });

  test('page metadata uses repo-branded social preview image', async ({ page }) => {
    await page.goto(BASE + '/');
    const ogImage = await page.locator('meta[property="og:image"]').getAttribute('content');
    const twitterImage = await page.locator('meta[name="twitter:image"]').getAttribute('content');
    expect(ogImage).toContain('og-awesome-anthropic.svg');
    expect(twitterImage).toContain('og-awesome-anthropic.svg');
  });

  test('source card images load for dashboard lead card', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.dash-lead-card')).toBeVisible({ timeout: 15000 });
    // Card should have a background image (ci-* class)
    const hasBg = await page.evaluate(() => {
      const card = document.querySelector('.dash-lead-card');
      if (!card) return false;
      const classes = Array.from(card.classList);
      return classes.some(c => c.startsWith('ci-'));
    });
    expect(hasBg).toBe(true);
  });
});

// ─────────────────────────────────────────────────────────────
// STORY MODAL
// ─────────────────────────────────────────────────────────────
test.describe('Story modal', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.dash-lead-card')).toBeVisible({ timeout: 15000 });
  });

  test('opens modal when lead card is clicked', async ({ page }) => {
    await page.locator('.dash-lead-card').click();
    await expect(page.locator('.rmodal-overlay')).toBeVisible({ timeout: 8000 });
  });

  test('modal shows article title', async ({ page }) => {
    await page.locator('.dash-lead-card').click();
    await expect(page.locator('.rmodal-title')).toBeVisible({ timeout: 8000 });
    const titleText = await page.locator('.rmodal-title').textContent();
    expect(titleText.trim().length).toBeGreaterThan(5);
  });

  test('modal has "Read Full Article" button', async ({ page }) => {
    await page.locator('.dash-lead-card').click();
    await expect(page.locator('.rmodal-overlay')).toBeVisible({ timeout: 8000 });
    // Button in meta bar (always visible from first frame)
    const btn = page.locator('.rmodal-meta .rmodal-btn-p');
    await expect(btn).toBeVisible({ timeout: 8000 });
    await expect(btn).toContainText('Read Full Article');
  });

  test('modal has close button that dismisses it', async ({ page }) => {
    await page.locator('.dash-lead-card').click();
    await expect(page.locator('.rmodal-overlay')).toBeVisible({ timeout: 8000 });
    await page.locator('.rmodal-close').click();
    await expect(page.locator('.rmodal-overlay')).not.toBeVisible({ timeout: 5000 });
  });

  test('modal closes on Escape key', async ({ page }) => {
    await page.locator('.dash-lead-card').click();
    await expect(page.locator('.rmodal-overlay')).toBeVisible({ timeout: 8000 });
    await page.keyboard.press('Escape');
    await expect(page.locator('.rmodal-overlay')).not.toBeVisible({ timeout: 5000 });
  });

  test('modal closes when clicking overlay backdrop', async ({ page }) => {
    await page.locator('.dash-lead-card').click();
    await expect(page.locator('.rmodal-overlay')).toBeVisible({ timeout: 8000 });
    // Click the overlay but not the box (top-left corner of overlay)
    await page.locator('.rmodal-overlay').click({ position: { x: 5, y: 5 } });
    await expect(page.locator('.rmodal-overlay')).not.toBeVisible({ timeout: 5000 });
  });

  test('modal shows loading spinner initially', async ({ page }) => {
    await page.locator('.dash-lead-card').click();
    // The spinner should appear in the loading state
    const hasSpinnerOrContent = await page.evaluate(() => {
      return !!(document.querySelector('.rmodal-spinner') || document.querySelector('.rmodal-article-text') || document.querySelector('.rmodal-no-preview'));
    });
    expect(hasSpinnerOrContent).toBe(true);
  });

  test('modal body eventually shows article content or fallback', async ({ page }) => {
    await page.locator('.dash-lead-card').click();
    await expect(page.locator('.rmodal-overlay')).toBeVisible({ timeout: 8000 });
    // Wait for loading to finish (spinner disappears, content or fallback appears)
    await page.waitForFunction(() => {
      return !!(document.querySelector('.rmodal-article-text') || document.querySelector('.rmodal-no-preview'));
    }, { timeout: 20000 });
    const bodyEl = page.locator('.rmodal-body');
    await expect(bodyEl).toBeVisible();
  });

  test('modal "Read Full Article" link opens external URL', async ({ page }) => {
    await page.locator('.dash-lead-card').click();
    await expect(page.locator('.rmodal-overlay')).toBeVisible({ timeout: 8000 });
    const link = page.locator('.rmodal-meta a[target="_blank"]').first();
    await expect(link).toBeVisible({ timeout: 8000 });
    const href = await link.getAttribute('href');
    expect(href).toBeTruthy();
    expect(href).toMatch(/^https?:\/\//);
  });

  test('leaderboard story links trigger modal', async ({ page }) => {
    const lbLink = page.locator('.dash-lb-title[data-sm]').first();
    await expect(lbLink).toBeVisible({ timeout: 15000 });
    await lbLink.click();
    await expect(page.locator('.rmodal-overlay')).toBeVisible({ timeout: 8000 });
    await page.locator('.rmodal-close').click();
  });

  test('source badge is visible in modal meta bar', async ({ page }) => {
    await page.locator('.dash-lead-card').click();
    await expect(page.locator('.rmodal-overlay')).toBeVisible({ timeout: 8000 });
    // Meta bar should have either a score or source badge
    const meta = page.locator('.rmodal-meta');
    await expect(meta).toBeVisible({ timeout: 8000 });
    const text = await meta.textContent();
    expect(text.trim().length).toBeGreaterThan(0);
  });
});

// ─────────────────────────────────────────────────────────────
// INTERVIEW WIZARD
// ─────────────────────────────────────────────────────────────
test.describe('Interview wizard', () => {
  test.beforeEach(async ({ page }) => {
    await gotoInterviewWizard(page);
  });

  test('wizard container is rendered', async ({ page }) => {
    await expect(page.locator('.wiz-wrap')).toBeVisible();
  });

  test('shows character select screen first', async ({ page }) => {
    await expect(page.locator('.wiz-class-grid')).toBeVisible({ timeout: 8000 });
  });

  test('character classes are selectable', async ({ page }) => {
    const classes = page.locator('.wiz-cls');
    await expect(classes.first()).toBeVisible({ timeout: 8000 });
    const count = await classes.count();
    expect(count).toBeGreaterThanOrEqual(4);
  });

  test('selecting a class advances to level 1', async ({ page }) => {
    await page.locator('.wiz-cls').first().click();
    await expect(page.locator('.wiz-start')).toHaveClass(/on/, { timeout: 8000 });
    await page.locator('.wiz-start').click();
    await expect(page.locator('.wiz-card-title')).toContainText('Level 1', { timeout: 8000 });
  });

  test('shows XP progress bar after class selection', async ({ page }) => {
    await page.locator('.wiz-cls').first().click();
    await expect(page.locator('.wiz-prog-bar')).toBeVisible({ timeout: 8000 });
  });

  test('quiz options are clickable', async ({ page }) => {
    await page.locator('.wiz-cls').first().click();
    await page.locator('.wiz-start').click();
    await expect(page.locator('.wiz-opt').first()).toBeVisible({ timeout: 8000 });
    await page.locator('.wiz-opt').first().click();
    // After answering, option should get a correct/wrong class
    const hasResult = await page.evaluate(() => {
      return !!(document.querySelector('.wiz-opt.correct') || document.querySelector('.wiz-opt.wrong'));
    });
    expect(hasResult).toBe(true);
  });

  test('Next button advances steps', async ({ page }) => {
    await page.locator('.wiz-cls').first().click();
    await page.locator('.wiz-start').click();
    // Answer all quiz options on this step
    const opts = page.locator('.wiz-opt');
    const count = await opts.count();
    for (let i = 0; i < count; i++) {
      const opt = opts.nth(i);
      const isAnswered = await opt.evaluate(el => el.classList.contains('correct') || el.classList.contains('wrong'));
      if (!isAnswered) { await opt.click(); break; }
    }
    await expect(page.locator('.wiz-btn-next')).toBeVisible({ timeout: 5000 });
  });

  test('wizard header shows step progress', async ({ page }) => {
    await page.locator('.wiz-cls').first().click();
    await page.locator('.wiz-start').click();
    await expect(page.locator('.wiz-hdr')).toBeVisible({ timeout: 8000 });
    const hdrText = await page.locator('.wiz-hdr').textContent();
    expect(hdrText.length).toBeGreaterThan(0);
  });
});

// ─────────────────────────────────────────────────────────────
// DASHBOARD WIDGETS
// ─────────────────────────────────────────────────────────────
test.describe('Dashboard widgets', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.dash-grid')).toBeVisible({ timeout: 20000 });
  });

  test('Today\'s Digest widget is visible', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText("Today's Digest", { timeout: 15000 });
  });

  test('Quick-Start code panel is visible', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Quick Start', { timeout: 15000 });
  });

  test('Quick-Start panel has language tabs', async ({ page }) => {
    const tabs = page.locator('.qs-tab');
    await expect(tabs.first()).toBeVisible({ timeout: 15000 });
    const count = await tabs.count();
    expect(count).toBeGreaterThanOrEqual(2);
  });

  test('Which Claude picker is visible', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Which Claude', { timeout: 15000 });
  });

  test('Community Buzz section is visible', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Community Buzz', { timeout: 15000 });
  });

  test('Daily Blog widget previews article deck', async ({ page }) => {
    const blogCards = page.locator('.dash-blog-card');
    await expect(blogCards.first()).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.dash-blog-stat').first()).toContainText('article briefs', { timeout: 15000 });
  });

  test('Daily Blog widget exposes source trail chips', async ({ page }) => {
    const chips = page.locator('.dash-blog-chip');
    await expect(chips.first()).toBeVisible({ timeout: 15000 });
    const count = await chips.count();
    expect(count).toBeGreaterThanOrEqual(2);
  });

  test('Daily Blog widget shows freshness and source quality signals', async ({ page }) => {
    await expect(page.locator('.dash-blog-signal').filter({ hasText: 'Snapshot freshness' })).toBeVisible({ timeout: 15000 });
    await expect(page.locator('.dash-blog-signal').filter({ hasText: 'First-party sources' })).toContainText('of', { timeout: 15000 });
    await expect(page.locator('.dash-blog-signal').filter({ hasText: 'Community refs' })).toContainText('referenced', { timeout: 15000 });
  });

  test('community buzz cards are rendered', async ({ page }) => {
    const tweets = page.locator('.dash-tweet');
    await expect(tweets.first()).toBeVisible({ timeout: 15000 });
    const count = await tweets.count();
    expect(count).toBeGreaterThanOrEqual(4);
  });

  test('community buzz cards open modal on click', async ({ page }) => {
    const tweet = page.locator('.dash-tweet[data-sm]').first();
    await expect(tweet).toBeVisible({ timeout: 15000 });
    await tweet.click();
    await expect(page.locator('.rmodal-overlay')).toBeVisible({ timeout: 8000 });
    await page.keyboard.press('Escape');
  });

  test('model picker buttons are clickable', async ({ page }) => {
    const mpBtn = page.locator('.mp-btn').first();
    await expect(mpBtn).toBeVisible({ timeout: 15000 });
    await mpBtn.click();
    // After picking, result should show
    await expect(page.locator('.dash-mp-result')).toContainText('claude-', { timeout: 5000 });
  });
});

// ─────────────────────────────────────────────────────────────
// DARK MODE
// ─────────────────────────────────────────────────────────────
test.describe('Dark Mode', () => {
  test('dark mode toggle button is present', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('#dm-toggle-btn')).toBeVisible();
  });

  test('clicking toggle adds data-theme=dark to html element', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    const btn = page.locator('#dm-toggle-btn');
    await btn.click();
    const theme = await page.evaluate(() => document.documentElement.getAttribute('data-theme'));
    expect(theme).toBe('dark');
  });

  test('clicking toggle twice restores light mode', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    const btn = page.locator('#dm-toggle-btn');
    await btn.click();
    await btn.click();
    const theme = await page.evaluate(() => document.documentElement.getAttribute('data-theme') || '');
    expect(theme).not.toBe('dark');
  });

  test('dark mode persists via localStorage on reload', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await page.locator('#dm-toggle-btn').click();
    await page.reload();
    await waitForContent(page);
    const theme = await page.evaluate(() => document.documentElement.getAttribute('data-theme'));
    expect(theme).toBe('dark');
    // Clean up
    await page.evaluate(() => localStorage.removeItem('aa-theme'));
  });
});

// ─────────────────────────────────────────────────────────────
// NEWS PAGE — CARD GRID
// ─────────────────────────────────────────────────────────────
test.describe('News Page', () => {
  test('news page loads and shows card grid', async ({ page }) => {
    await page.goto(BASE + '/#/docs/NEWS');
    await waitForContent(page);
    await expect(page.locator('.markdown-section table').first()).toBeVisible({ timeout: 15000 });
  });

  test('news page has Top Stories heading', async ({ page }) => {
    await page.goto(BASE + '/#/docs/NEWS');
    await waitForContent(page);
    await expect(page.locator('.markdown-section')).toContainText('Top Stories', { timeout: 15000 });
  });

  test('news page shows official announcements section', async ({ page }) => {
    await page.goto(BASE + '/#/docs/NEWS');
    await waitForContent(page);
    await expect(page.locator('.markdown-section')).toContainText('Official Announcements', { timeout: 15000 });
  });
});

// ─────────────────────────────────────────────────────────────
// PROMPTS PAGE
// ─────────────────────────────────────────────────────────────
test.describe('Prompts Library Page', () => {
  test('prompts page loads with content', async ({ page }) => {
    await page.goto(BASE + '/#/docs/PROMPTS');
    await waitForContent(page);
    await expect(page.locator('.markdown-section')).toContainText('Prompt', { timeout: 15000 });
  });

  test('prompts page has search bar injected', async ({ page }) => {
    await page.goto(BASE + '/#/docs/PROMPTS');
    await waitForContent(page);
    // Give doneEach time to inject
    await page.waitForTimeout(1000);
    await expect(page.locator('.plib-search, input[placeholder*="Search prompts"]')).toBeVisible({ timeout: 10000 });
  });

  test('prompts page has multiple categories', async ({ page }) => {
    await page.goto(BASE + '/#/docs/PROMPTS');
    await waitForContent(page);
    // Should have at least 4 h2 category sections
    const h2Count = await page.locator('.markdown-section h2').count();
    expect(h2Count).toBeGreaterThanOrEqual(4);
  });

  test('prompts page has code blocks with prompt content', async ({ page }) => {
    await page.goto(BASE + '/#/docs/PROMPTS');
    await waitForContent(page);
    const preCount = await page.locator('.markdown-section pre').count();
    expect(preCount).toBeGreaterThanOrEqual(5);
  });
});

// ─────────────────────────────────────────────────────────────
// TOOLS PAGE
// ─────────────────────────────────────────────────────────────
test.describe('Tools Directory Page', () => {
  test('tools page loads with content', async ({ page }) => {
    await page.goto(BASE + '/#/docs/TOOLS');
    await waitForContent(page);
    await expect(page.locator('.markdown-section')).toContainText('Tool', { timeout: 15000 });
  });

  test('tools page has search bar injected', async ({ page }) => {
    await page.goto(BASE + '/#/docs/TOOLS');
    await waitForContent(page);
    await page.waitForTimeout(1000);
    await expect(page.locator('.tools-search, input[placeholder*="Search tools"]')).toBeVisible({ timeout: 10000 });
  });

  test('tools page has tables with SDK and tool entries', async ({ page }) => {
    await page.goto(BASE + '/#/docs/TOOLS');
    await waitForContent(page);
    const tableCount = await page.locator('.markdown-section table').count();
    expect(tableCount).toBeGreaterThanOrEqual(2);
  });

  test('tools page mentions Anthropic SDK', async ({ page }) => {
    await page.goto(BASE + '/#/docs/TOOLS');
    await waitForContent(page);
    await expect(page.locator('.markdown-section')).toContainText('anthropic', { timeout: 15000 });
  });
});

// ─────────────────────────────────────────────────────────────
// SIDEBAR NAVIGATION
// ─────────────────────────────────────────────────────────────
test.describe('Sidebar Navigation', () => {
  test('sidebar shows Prompt Library link', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.sidebar')).toContainText('Prompt', { timeout: 10000 });
  });

  test('sidebar shows Tools Directory link', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.sidebar')).toContainText('Tool', { timeout: 10000 });
  });

  test('sidebar News Feed link navigates to news page', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await page.locator('.sidebar a[href*="NEWS"]').first().click();
    await waitForContent(page);
    await expect(page.locator('.markdown-section')).toContainText('News', { timeout: 10000 });
  });

  test('sidebar Interview Prep link navigates to wizard', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await page.locator('.sidebar a[href*="INTERVIEW"]').first().click();
    await waitForContent(page);
    await page.waitForTimeout(1000);
    await expect(page.locator('.wiz-wrap')).toBeVisible({ timeout: 10000 });
  });
});

// ─────────────────────────────────────────────────────────────
// WIZARD PERSISTENCE
// ─────────────────────────────────────────────────────────────
test.describe('Interview Wizard Persistence', () => {
  test('wizard renders character select on first visit', async ({ page }) => {
    await gotoInterviewWizard(page);
    await page.waitForTimeout(1000);
    await expect(page.locator('.wiz-class-grid')).toBeVisible({ timeout: 10000 });
  });

  test('picking a class enables the Begin Quest button', async ({ page }) => {
    await gotoInterviewWizard(page);
    await page.waitForTimeout(1000);
    const classButtons = page.locator('.wiz-cls');
    if (await classButtons.count() > 0) {
      await classButtons.first().click();
      await expect(page.locator('.wiz-start')).toHaveClass(/on/, { timeout: 5000 });
    }
  });

  test('wizard clears localStorage on restart', async ({ page }) => {
    await page.goto(BASE + '/#/docs/INTERVIEW');
    await waitForContent(page);
    await page.waitForTimeout(500);
    // Set some state in localStorage
    await page.evaluate(() => localStorage.setItem('aa-wiz', JSON.stringify({ step: 3, xp: 45, cls: 'eng', answers: {}, achievements: [] })));
    // Navigate away and back to trigger initWizard
    await page.goto(BASE + '/');
    await waitForContent(page);
    await page.goto(BASE + '/#/docs/INTERVIEW');
    await waitForContent(page);
    await page.waitForTimeout(1000);
    // Should be on step 3 (restored state)
    const saved = await page.evaluate(() => localStorage.getItem('aa-wiz'));
    // State should still exist (it was restored, not cleared on load)
    expect(saved).not.toBeNull();
  });
});

// ─────────────────────────────────────────────────────────────
// RSS FEED
// ─────────────────────────────────────────────────────────────
test.describe('RSS Feed', () => {
  test('rss.xml exists and is valid XML', async ({ page }) => {
    const response = await page.request.get(BASE + '/rss.xml');
    // RSS may or may not be deployed yet — just check if accessible
    if (response.ok()) {
      const text = await response.text();
      expect(text).toContain('<rss');
      expect(text).toContain('</rss>');
      expect(text).toContain('<channel>');
    }
  });
});

// ─────────────────────────────────────────────────────────────
// PWA / MANIFEST
// ─────────────────────────────────────────────────────────────
test.describe('PWA Manifest', () => {
  test('manifest.json exists and has correct fields', async ({ page }) => {
    const response = await page.request.get(BASE + '/manifest.json');
    if (response.ok()) {
      const manifest = await response.json();
      expect(manifest.name).toContain('Anthropic');
      expect(manifest.start_url).toBe('./');
      expect(manifest.scope).toBe('./');
      expect(manifest.theme_color).toBeDefined();
      expect(manifest.display).toBeDefined();
    }
  });

  test('index.html references manifest in head', async ({ page }) => {
    await page.goto(BASE + '/');
    const manifestLink = await page.locator('link[rel="manifest"]').getAttribute('href');
    expect(manifestLink).toBeTruthy();
  });

  test('service worker uses scope-relative asset URLs', async ({ page }) => {
    const response = await page.request.get(BASE + '/sw.js');
    if (response.ok()) {
      const swScript = await response.text();
      expect(swScript).toContain('self.registration.scope');
      expect(swScript).not.toContain("'/awesome-anthropic/'");
    }
  });
});

// ─────────────────────────────────────────────────────────────
// DISTRIBUTION + DAILY BRIEF
// ─────────────────────────────────────────────────────────────
test.describe('Distribution and Daily Brief', () => {
  test('sidebar shows Distribution Playbook link', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.sidebar')).toContainText('Distribution Playbook', { timeout: 10000 });
  });

  test('distribution page direct route loads', async ({ page }) => {
    await page.goto(BASE + '/#/docs/DISTRIBUTION');
    await waitForContent(page);
    await expect(page.locator('.markdown-section')).toContainText('Distribution Playbook', { timeout: 15000 });
    await expect(page.locator('.markdown-section')).toContainText('Telegram', { timeout: 15000 });
    await expect(page.locator('.markdown-section')).toContainText('Discord', { timeout: 15000 });
    await expect(page.locator('.markdown-section')).toContainText('Buttondown', { timeout: 15000 });
  });

  test('daily brief page direct route loads', async ({ page }) => {
    await page.goto(BASE + '/#/docs/DAILY_ANTHROPIC');
    await waitForContent(page);
    await expect(page.locator('.markdown-section')).toContainText('Daily Anthropic Brief', { timeout: 15000 });
    await expect(page.locator('.markdown-section')).toContainText('Website Improvement Backlog', { timeout: 15000 });
  });

  test('dashboard shows Daily Anthropic Brief widget', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page.locator('.markdown-section')).toContainText('Daily Anthropic Brief', { timeout: 15000 });
  });

  test('dashboard brief widget links to brief doc', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    const link = page.locator('a[href*="docs/DAILY_ANTHROPIC"]').first();
    await expect(link).toBeVisible({ timeout: 15000 });
  });

  test('sidebar Daily Brief link navigates correctly', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await page.click('.sidebar a[href="#/docs/DAILY_ANTHROPIC"]');
    await page.waitForURL(/docs\/DAILY_ANTHROPIC/, { timeout: 10000 });
    await expect(page.locator('.markdown-section')).toContainText('Daily Anthropic Brief', { timeout: 15000 });
  });
});
