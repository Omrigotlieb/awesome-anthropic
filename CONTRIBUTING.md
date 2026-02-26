# Contributing to awesome-anthropic

Thank you for helping keep this list awesome!

## What to Add

A resource is a good fit if it:

- Is directly related to Anthropic, Claude, or the Anthropic ecosystem.
- Is high quality and actively maintained (not abandoned).
- For GitHub repos: has a clear README and is publicly accessible.
- Provides genuine value to developers, researchers, or users.

## What NOT to Add

- General AI/LLM resources not specific to Anthropic or Claude.
- Resources behind paywalls (unless notably exceptional).
- Duplicate entries already in the list.
- Broken, dead, or placeholder links.
- Self-promotional submissions without disclosure.

## Format

Each entry must follow this exact format:

```
- [Resource Name](url) - Brief, objective description.
```

Rules:
- Description starts with a capital letter and ends with a period.
- Descriptions should be under 100 characters.
- Entries within a section should be in roughly alphabetical or logical order.
- No promotional language ("best", "amazing", "revolutionary").

## How to Submit

1. **Fork** the repository.
2. **Add** your resource to the correct section in `README.md`.
3. **Verify** the URL works and the description is accurate.
4. **Submit** a pull request using the PR template.

## PR Checklist

Before submitting, confirm:

- [ ] My addition is in the correct section.
- [ ] The URL is live and returns a 200 status.
- [ ] The description follows the format rules above.
- [ ] The entry is not a duplicate of an existing item.
- [ ] I have not edited any auto-updated sections (between `<!-- X_START -->` and `<!-- X_END -->` tags).

## Automated Sections

The following sections are maintained by automated workflows and **must not** be edited manually:

- `## Changelog (Auto-updated)` — synced from `docs.anthropic.com/en/release-notes`.
- `## News Digest (Auto-updated)` — aggregated daily from blogs, HN, Reddit, arXiv, and GitHub.

To report an error in auto-generated content, open an issue with the `automated-content` label.

## Reporting Issues

| Issue Type | Template |
|------------|----------|
| Broken link | Use the **Broken Link** issue template |
| Suggest addition | Use the **Add Resource** issue template |
| Other | Open a general issue |

## Running Scripts Locally

```bash
pip install -r requirements.txt

# Fetch today's news
python scripts/fetch_news.py

# Check Anthropic changelog
python scripts/check_changelog.py

# Validate all links
python scripts/link_checker.py
```

## Code of Conduct

Be respectful and constructive. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
