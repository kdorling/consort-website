# Bank of Canada Hugo Theme

A Hugo theme inspired by the Bank of Canada website design, featuring a professional, accessible, and responsive layout.

## Features

- **Responsive Design**: Mobile-first approach that works seamlessly on all devices
- **Bank of Canada Color Scheme**: Teal, red, and gray colors matching the official website
- **Dropdown Navigation**: Multi-level navigation menus with hover and keyboard support
- **Accessibility**: WCAG 2.1 compliant with skip links, proper ARIA labels, and keyboard navigation
- **Modern Typography**: Clean, professional font stack using system fonts
- **Hero Section**: Eye-catching hero area for homepage
- **Stats Cards**: Highlight key metrics and data points
- **Card-Based Layouts**: Modern card designs for content listings
- **Sticky Header**: Header stays visible while scrolling
- **Mobile Menu**: Hamburger menu with smooth toggle animation

## Installation

1. Clone or copy this theme into your Hugo project's `themes` directory:

```bash
cd your-hugo-project
cp -r path/to/boc themes/boc
```

2. Update your `hugo.toml` (or `config.toml`) to use the theme:

```toml
theme = 'boc'
```

## Configuration

### Basic Configuration

```toml
baseURL = 'https://example.org/'
languageCode = 'en-US'
title = 'Bank of Canada'
theme = 'boc'

[params]
  description = 'More than a bank. We are the Central Bank of Canada.'
```

### Menu Configuration

The theme supports multi-level dropdown menus. Define your menus in `hugo.toml`:

```toml
[menus]
  [[menus.main]]
    name = 'Home'
    pageRef = '/'
    weight = 10

  # Parent menu item
  [[menus.main]]
    name = 'Monetary Policy'
    pageRef = '/monetary-policy'
    weight = 20

  # Child menu items (dropdown)
  [[menus.main]]
    name = 'Policy Interest Rate'
    parent = 'Monetary Policy'
    pageRef = '/monetary-policy/policy-rate'
    weight = 1

  [[menus.main]]
    name = 'Inflation'
    parent = 'Monetary Policy'
    pageRef = '/monetary-policy/inflation'
    weight = 2
```

## Layouts

### Home Layout

The home layout (`layouts/home.html`) includes:
- Hero section with tagline
- Stats/highlights cards
- Latest updates section
- Alert/notice section
- Additional content areas

### Page Layout

Standard single page layout with:
- Page header with title and description
- Content area with proper typography
- Tags footer (if tags are defined)
- Metadata display

### Section Layout

List pages that display child pages as cards:
- Section header
- Intro content
- Card grid of child pages

## Styling

### Color Variables

The theme uses CSS custom properties for easy customization:

```css
--boc-teal: #004a5d;          /* Primary brand color */
--boc-dark-teal: #003744;     /* Darker teal for hover states */
--boc-light-teal: #006a85;    /* Lighter teal for links */
--boc-red: #d32f2f;           /* Accent color */
--boc-gray: #f5f5f5;          /* Light background */
--boc-dark-gray: #333333;     /* Footer and dark text */
```

### Custom Styling

To customize colors, add a custom CSS file in your project:

```css
/* assets/css/custom.css */
:root {
  --boc-teal: #your-color;
  --boc-red: #your-accent;
}
```

Then load it in your templates or via Hugo's asset pipeline.

## Components

### Hero Section

Add a hero section to your homepage:

```html
<div class="hero">
  <h1>Your Headline</h1>
  <p>Your tagline or description</p>
</div>
```

### Stats Cards

Display key metrics:

```html
<div class="stats">
  <div class="stat-card">
    <div class="stat-label">Label</div>
    <div class="stat-value">2.25%</div>
    <div class="stat-date">Dec 10, 2025</div>
  </div>
</div>
```

### Alerts

Show important notices:

```html
<div class="alert alert-warning">
  <h3>Important Notice</h3>
  <p>Your message here...</p>
</div>
```

Available alert types:
- `alert-info` - Blue information alert
- `alert-warning` - Orange warning alert
- `alert-danger` - Red danger/error alert

### Buttons

```html
<a href="/link" class="btn btn-primary">Primary Button</a>
<a href="/link" class="btn btn-secondary">Secondary Button</a>
```

## JavaScript Features

The theme includes JavaScript for:
- Mobile menu toggle
- Dropdown menu functionality
- Keyboard navigation (arrow keys, escape, etc.)
- Smooth scrolling for skip links
- Sticky header with scroll effects
- Responsive behavior

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Accessibility Features

- WCAG 2.1 Level AA compliant
- Skip to content link
- Keyboard navigation support
- ARIA labels and roles
- Focus indicators
- Semantic HTML5
- Screen reader friendly

## Responsive Breakpoints

- Desktop: > 768px
- Tablet/Mobile: ≤ 768px
- Small Mobile: ≤ 480px

## Development

### Prerequisites

- Hugo v0.146.0 or higher
- No extended version required
- No external dependencies

### Local Development

```bash
hugo server -D
```

### Building for Production

```bash
hugo --minify
```

## Customization Tips

1. **Override Layouts**: Copy any layout file to your project's `layouts` directory to customize
2. **Add Custom CSS**: Create `assets/css/custom.css` in your project
3. **Modify Colors**: Update CSS variables in your custom stylesheet
4. **Extend JavaScript**: Add additional JS files in `assets/js/`

## Content Structure

Recommended content structure:

```
content/
├── _index.md                 # Homepage
├── about/
│   └── _index.md
├── monetary-policy/
│   ├── _index.md
│   ├── policy-rate.md
│   └── inflation.md
├── financial-system/
│   └── _index.md
└── markets/
    └── _index.md
```

## Front Matter Example

```yaml
---
title: "Page Title"
date: 2025-01-01T00:00:00Z
draft: false
description: "Brief description of the page"
tags: ["tag1", "tag2"]
---
```

## License

This theme is provided as-is for use in Hugo projects. The design is inspired by the Bank of Canada website but is not affiliated with or endorsed by the Bank of Canada.

## Support

For issues or questions about this theme, please refer to the Hugo documentation at https://gohugo.io/documentation/

## Credits

- Design inspiration: Bank of Canada (bankofcanada.ca)
- Built with: Hugo Static Site Generator
- Icons: Unicode characters