# Quick Start Guide

## View Your Bank of Canada-Themed Hugo Site

### Option 1: Development Server (Recommended)

Run the Hugo development server with live reload:

```bash
cd /Users/kevindorling/code/test
hugo server -D
```

Then open your browser to: **http://localhost:1313**

The site will automatically reload when you make changes to files.

### Option 2: Build and View Static Files

Build the site to the `public/` directory:

```bash
cd /Users/kevindorling/code/test
hugo --minify
```

Then open `public/index.html` in your browser, or serve it with:

```bash
cd public
python3 -m http.server 8000
```

Visit: **http://localhost:8000**

## What You'll See

### Homepage Features
- **Hero Section**: "More than a bank. We are the Central Bank of Canada."
- **Stats Cards**: Policy interest rate, CPI inflation, and other key metrics
- **Latest Updates**: Card-based layout of recent content
- **Alert Section**: Important notices and warnings
- **Information Sections**: About the Bank of Canada

### Navigation
- **Dropdown Menus**: Hover over menu items to see submenus:
  - Monetary Policy (Policy Rate, Inflation, Framework, Publications)
  - Financial System (Review, Infrastructure, Stability)
  - Markets (Exchange Rates, Interest Rates, Operations)
  - Bank Notes (Current Notes, Security Features, Commemorative)
  - Research (Working Papers, Discussion Papers, Economic Analysis)
  - About

### Mobile View
- Click the hamburger menu (☰) in the top right
- Navigation transforms for mobile devices
- Tap menu items with dropdowns to expand them

### Features to Try
1. **Responsive Design**: Resize your browser window to see mobile layout
2. **Keyboard Navigation**: Use Tab, Enter, Arrow keys to navigate menus
3. **Skip Link**: Press Tab on page load to see "Skip to content" link
4. **Search Button**: Placeholder for search functionality
5. **Language Toggle**: FR button to switch languages (placeholder)

## Making Changes

### Edit Content
```bash
# Edit homepage
nano content/_index.md

# Edit monetary policy section
nano content/monetary-policy/_index.md
```

### Customize Colors
Edit `themes/boc/assets/css/main.css` and change CSS variables:

```css
:root {
    --boc-teal: #004a5d;     /* Change to your color */
    --boc-red: #d32f2f;      /* Change accent color */
}
```

### Add New Menu Items
Edit `themes/boc/hugo.toml` or `hugo.toml`:

```toml
[[menus.main]]
  name = 'New Page'
  pageRef = '/new-page'
  weight = 80
```

### Create New Content
```bash
# Create a new page
hugo new my-new-page.md

# Create a new section
hugo new my-section/_index.md
```

## File Structure

```
test/
├── hugo.toml              # Main site configuration
├── content/               # Your content files
│   ├── _index.md         # Homepage content
│   └── monetary-policy/  # Section content
├── themes/
│   └── boc/              # Bank of Canada theme
│       ├── assets/
│       │   ├── css/      # Styles
│       │   └── js/       # JavaScript
│       ├── layouts/      # HTML templates
│       └── README.md     # Theme documentation
└── public/               # Generated site (after build)
```

## Tips

1. **Always run `hugo server -D`** during development for live preview
2. **Use `-D` flag** to include draft content
3. **Check the console** for any errors or warnings
4. **Read `themes/boc/README.md`** for detailed theme documentation
5. **See `THEME_UPDATES.md`** for complete list of changes made

## Need Help?

- **Hugo Documentation**: https://gohugo.io/documentation/
- **Theme README**: `themes/boc/README.md`
- **Hugo Command Reference**: `hugo help`

## Common Commands

```bash
# Start development server
hugo server -D

# Build for production
hugo --minify

# Create new content
hugo new content/page-name.md

# Check Hugo version
hugo version

# Clear cache
hugo mod clean
```

Enjoy your new Bank of Canada-themed Hugo site! 🍁