# Home Page Guide

This guide explains the structure and configuration options for the home page (`home.html`) in the Bank of Canada inspired theme.

## Overview

The home page template is designed to be flexible and configurable through Hugo's configuration file. It consists of several sections that can be customized or disabled based on your needs.

## Page Structure

The home page includes the following sections in order:

1. **Hero Section** - Eye-catching banner with site title and description
2. **Main Content** - Content from `content/_index.md`
3. **Quick Stats** - Configurable statistics cards (optional)
4. **Featured Departments/Services** - Showcase up to 6 departments
5. **Latest News & Updates** - Display recent news and events
6. **Call to Action** - Encourage user engagement (optional)

## Configuration

### 1. Hero Section

The hero section automatically displays your site title and description.

**In `hugo.toml`:**
```toml
title = 'Village of Consort'

[params]
  description = 'Welcome to the Village of Consort, Alberta - a vibrant community where rural living meets modern opportunity.'
```

### 2. Main Content

Edit `content/_index.md` to add your main homepage content:

```markdown
---
title: "Home"
date: 2025-01-01T00:00:00Z
draft: false
---

## Discover Consort

Welcome to our community! Here you'll find information about...

### Our Services
- Service 1
- Service 2
- Service 3
```

### 3. Quick Stats (Optional)

Add statistics to highlight key information.

**In `hugo.toml`:**
```toml
[[params.stats]]
  label = "Population"
  value = "900+"
  date = "2024 Census"

[[params.stats]]
  label = "Established"
  value = "1912"

[[params.stats]]
  label = "Area"
  value = "2.5 km²"

[[params.stats]]
  label = "Elevation"
  value = "755m"
```

If no stats are configured, this section won't display.

### 4. Departments & Services

Automatically displays up to 6 pages from the `content/departments/` directory.

Create department pages:
```
content/
  departments/
    _index.md
    administration.md
    recreation.md
    public-works.md
    etc.
```

Each department file should have frontmatter:
```markdown
---
title: "Recreation Services"
date: 2025-01-01
summary: "Programs, facilities, and activities for all ages."
---

Content goes here...
```

### 5. Latest News & Updates

Displays the 3 most recent items from `content/news/` or `content/events/`.

Create news items:
```
content/
  news/
    _index.md
    2025-01-15-town-hall.md
    2025-01-10-new-park.md
```

Example news item:
```markdown
---
title: "New Community Park Opening"
date: 2025-01-10
summary: "Join us for the grand opening of Riverside Park on February 1st."
---

We're excited to announce the opening of our newest community space...
```

### 6. Call to Action (Optional)

Add a call-to-action section with buttons.

**In `hugo.toml`:**
```toml
[params.callToAction]
  title = "Get Involved"
  text = "There are many ways to connect with our community. Attend council meetings, volunteer for events, or explore our programs."
  
  [[params.callToAction.buttons]]
    text = "View Events"
    url = "/events"
    class = "btn-primary"
  
  [[params.callToAction.buttons]]
    text = "Contact Us"
    url = "/contact"
    class = "btn-secondary"
```

If not configured, this section won't display.

## Complete Configuration Example

Here's a full example of homepage configuration in `hugo.toml`:

```toml
baseURL = 'https://example.org/'
languageCode = 'en-US'
title = 'Village of Consort'
theme = 'boc'

[params]
  description = 'Welcome to the Village of Consort, Alberta - a vibrant community where rural living meets modern opportunity.'

  # Quick Stats
  [[params.stats]]
    label = "Population"
    value = "900+"
    date = "2024 Census"

  [[params.stats]]
    label = "Established"
    value = "1912"

  [[params.stats]]
    label = "Area"
    value = "2.5 km²"

  [[params.stats]]
    label = "Departments"
    value = "8"

  # Call to Action
  [params.callToAction]
    title = "Get Involved"
    text = "There are many ways to connect with our community. Attend council meetings, volunteer for events, or explore our programs."
    
    [[params.callToAction.buttons]]
      text = "View Events Calendar"
      url = "/events"
      class = "btn-primary"
    
    [[params.callToAction.buttons]]
      text = "Contact Us"
      url = "/contact"
      class = "btn-secondary"
```

## Content Organization

For best results, organize your content as follows:

```
content/
├── _index.md              # Homepage main content
├── departments/
│   ├── _index.md
│   ├── administration.md
│   ├── recreation.md
│   ├── public-works.md
│   └── ...
├── news/
│   ├── _index.md
│   └── (news articles)
├── events/
│   ├── _index.md
│   └── (event pages)
├── government/
│   └── ...
└── ...
```

## Styling & Customization

### Stats Cards

Stats are styled with the `.stat-card` class. Each stat includes:
- `.stat-label` - The category label (e.g., "Population")
- `.stat-value` - The main value (e.g., "900+")
- `.stat-date` - Optional date/context (e.g., "2024 Census")

### Card Grid

Departments and news use the `.card-grid` layout, which automatically adjusts columns based on screen size:
- Desktop: 3 columns
- Tablet: 2 columns
- Mobile: 1 column

### Buttons

Use button classes for call-to-action links:
- `.btn-primary` - Main action (teal background)
- `.btn-secondary` - Secondary action (red background)

## Disabling Sections

To disable optional sections, simply don't configure them:

- **No Stats**: Don't add `[[params.stats]]` entries
- **No Call to Action**: Don't add `[params.callToAction]`
- **No Departments**: Delete or move the `content/departments/` folder
- **No News**: Don't create `content/news/` or `content/events/`

## Accessibility

The home page template follows accessibility best practices:
- Semantic HTML5 elements (`<section>`, `<article>`)
- Proper heading hierarchy (h1 → h2 → h3)
- Descriptive link text
- ARIA labels where appropriate
- Keyboard navigable

## SEO Considerations

For better SEO on the homepage:

1. **Title and Description**: Set in `hugo.toml` - used for meta tags
2. **Structured Content**: Use proper headings in `_index.md`
3. **Fresh Content**: Keep news/events up to date
4. **Internal Links**: Link to important pages from main content

## Troubleshooting

### Stats Not Showing
- Check that `[[params.stats]]` entries are in `hugo.toml`
- Ensure proper TOML syntax (double brackets)
- Verify Hugo server has been restarted after config changes

### No Departments Displayed
- Verify files exist in `content/departments/`
- Check that pages have `draft: false` in frontmatter
- Ensure summary is provided (either explicit or auto-generated)

### News Section Empty
- Create `content/news/` or `content/events/` directory
- Add markdown files with proper frontmatter
- Set `draft: false` on published items

### Hero Not Showing
- If commented out, uncomment the hero section in `home.html`
- Check that `params.description` is set in `hugo.toml`

## Best Practices

1. **Keep Content Fresh**: Regularly update news and events
2. **Optimize Images**: Use appropriate sizes and formats
3. **Write Clear Summaries**: First 70-100 words become the summary
4. **Use Dates Properly**: Date format: `2025-01-01T00:00:00Z`
5. **Test Responsively**: View on mobile, tablet, and desktop

## Advanced Customization

To modify the home page template:

1. Copy `themes/boc/layouts/home.html` to `layouts/home.html`
2. Make your changes
3. Your version will override the theme's version

Or edit the theme file directly if you're maintaining your own fork.

---

**File Location**: `themes/boc/layouts/home.html`  
**Last Updated**: 2024  
**Hugo Version**: 0.146.0+