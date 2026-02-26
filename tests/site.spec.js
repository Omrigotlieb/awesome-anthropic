// @ts-check
const { test, expect } = require('@playwright/test');

const BASE = 'https://omrigotlieb.github.io/awesome-anthropic';

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

// ─────────────────────────────────────────────────────────────
// HOMEPAGE / DASHBOARD
// ─────────────────────────────────────────────────────────────
test.describe('Homepage', () => {
  test('loads and shows title', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    await expect(page).toHaveTitle(/Awesome Anthropic/);
    await expect(page.locator('.markdown-section h1')).toContainText('Awesome Anthropic');
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
    await page.goto(BASE + '/#/docs/INTERVIEW');
    await waitForContent(page);
  });

  test('shows Anthropic interview content', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Anthropic');
  });

  test('shows technical topics', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('LLM');
  });

  test('shows behavioral questions section', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Behavioral');
  });

  test('shows study plan or resources', async ({ page }) => {
    await expect(page.locator('.markdown-section')).toContainText('Study');
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
  test('uses Anthropic brand font (Lora or DM Serif)', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    const fontFamily = await page.evaluate(() => {
      const body = document.querySelector('.markdown-section p');
      return body ? window.getComputedStyle(body).fontFamily : '';
    });
    expect(fontFamily.toLowerCase()).toMatch(/lora|serif|georgia/);
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

  test('sidebar has warm dark background', async ({ page }) => {
    await page.goto(BASE + '/');
    await waitForContent(page);
    const bg = await page.evaluate(() => {
      const sidebar = document.querySelector('.sidebar');
      return sidebar ? window.getComputedStyle(sidebar).backgroundColor : '';
    });
    // Should be a dark color (not white/light)
    expect(bg).not.toBe('rgb(255, 255, 255)');
  });

  test('footer is rendered on every page', async ({ page }) => {
    await page.goto(BASE + '/#/docs/NEWS');
    await waitForContent(page);
    await expect(page.locator('.page-footer')).toBeVisible();
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
