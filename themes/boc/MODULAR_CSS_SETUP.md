# Modular CSS Setup for Hugo

This document explains how the modular CSS architecture is implemented in this Hugo theme.

## Overview

The CSS has been split into **7 modular files** that are automatically bundled together by Hugo Pipes at build time. This provides better organization and maintainability while still delivering a single optimized CSS file to browsers.

## How It Works

### 1. Modular CSS Files

Located in `themes/boc/assets/css/`:

```
css/
├── variables.css      # CSS custom properties (82 lines)
├── base.css          # Reset & typography (122 lines)
├── header.css        # Header & navigation (418 lines)
├── layout.css        # Content layouts (170 lines)
├── components.css    # UI components (177 lines)
├── footer.css        # Footer styles (57 lines)
└── responsive.css    # Media queries (502 lines)
```

**Total:** ~1,528 lines of organized, maintainable CSS

### 2. Hugo Pipes Bundling

The bundling happens in `themes/boc/layouts/_partials/head/css.html`:

```go
{{- $variables := resources.Get "css/variables.css" -}}
{{- $base := resources.Get "css/base.css" -}}
{{- $header := resources.Get "css/header.css" -}}
{{- $layout := resources.Get "css/layout.css" -}}
{{- $components := resources.Get "css/components.css" -}}
{{- $footer := resources.Get "css/footer.css" -}}
{{- $responsive := resources.Get "css/responsive.css" -}}

{{- $css := slice $variables $base $header $layout $components $footer $responsive | resources.Concat "css/bundle.css" -}}
```

### 3. Build Process

**Development mode:**
```bash
hugo server
```
- Generates unminified `bundle.css`
- Fast rebuilds on file changes
- Easy to debug in browser DevTools

**Production build:**
```bash
hugo
```
- Concatenates all CSS files
- Minifies the bundle
- Adds fingerprint hash for cache busting
- Generates integrity hash for security

## Benefits

### ✅ Organization
- Each file has a single, clear purpose
- Easy to find and edit specific styles
- No more giant monolithic CSS files

### ✅ Performance
- Single HTTP request (one bundled file)
- Minified in production
- Fingerprinted for optimal caching
- Gzipped by web servers

### ✅ Maintainability
- Logical separation of concerns
- Multiple developers can work simultaneously
- Changes are isolated to specific files
- Clear file structure

### ✅ Hugo Integration
- No build tools required (no npm, webpack, etc.)
- Hugo Pipes handles everything
- Hot reload in development
- Automatic cache invalidation

## File Order Matters

The files are concatenated in this specific order:

1. **variables.css** - Must be first (defines CSS custom properties)
2. **base.css** - Base styles and resets
3. **header.css** - Header and navigation
4. **layout.css** - Main content layouts
5. **components.css** - Reusable components
6. **footer.css** - Footer styles
7. **responsive.css** - Must be last (media query overrides)

**Important:** The order is defined in `themes/boc/layouts/_partials/head/css.html`

## Making Changes

### To edit existing styles:

1. Find the appropriate CSS file (see `CSS_STRUCTURE.md`)
2. Make your changes
3. Save the file
4. Hugo automatically rebuilds the bundle

### To add a new CSS module:

1. Create new file in `themes/boc/assets/css/`
2. Add it to the bundle in `themes/boc/layouts/_partials/head/css.html`:
   ```go
   {{- $newmodule := resources.Get "css/newmodule.css" -}}
   {{- $css := slice $variables $base $header $layout $components $newmodule $footer $responsive | resources.Concat "css/bundle.css" -}}
   ```
3. Update `CSS_STRUCTURE.md` documentation

### To remove a module:

1. Delete the CSS file
2. Remove it from the slice in `themes/boc/layouts/_partials/head/css.html`

## Generated Files

Hugo generates these files in `public/css/`:

**Development:**
```
public/css/bundle.css          # Unminified, readable
```

**Production:**
```
public/css/bundle.min.[hash].css   # Minified with integrity hash
```

**Example HTML output:**
```html
<link 
  rel="stylesheet" 
  href="/css/bundle.min.6b09e5ce37b73ce2e03b8c08dad75f02e25bc85a8b2d6571cabd0e4e30904fac.css"
  integrity="sha256-awnlzje3POLgO4wI2tdfAuJbyFqLLWVxyr0OTjCQT6w="
  crossorigin="anonymous">
```

## Why Not @import?

We don't use CSS `@import` statements because:

- ❌ Multiple HTTP requests (slower)
- ❌ Blocking rendering
- ❌ Not optimized by Hugo Pipes
- ❌ Can't minify across imports

Hugo Pipes concatenation is better:

- ✅ Single HTTP request
- ✅ Optimized and minified
- ✅ Cache-friendly with fingerprinting
- ✅ Integrity hashes for security

## Troubleshooting

### CSS changes not appearing?

1. Stop Hugo server (`Ctrl+C`)
2. Clear Hugo's cache: `hugo --gc`
3. Restart: `hugo server`

### Bundle not generating?

Check that all CSS files exist:
```bash
ls -la themes/boc/assets/css/*.css
```

### Syntax errors?

Hugo will show errors in the console. Check:
- Missing closing braces
- Invalid CSS syntax
- Typos in file names

## Performance Metrics

**Before modularization:**
- Single file: 1,517 lines
- Hard to maintain
- Difficult to navigate

**After modularization:**
- 7 organized files: 1,528 lines total
- Generated bundle: Same size (no overhead)
- Minified production: ~20KB
- Gzipped: ~5KB

## Development Workflow

1. **Start Hugo server:**
   ```bash
   hugo server -D
   ```

2. **Edit CSS files:**
   - Open any `.css` file in `themes/boc/assets/css/`
   - Make changes
   - Save

3. **See changes instantly:**
   - Hugo watches for changes
   - Automatically rebuilds bundle
   - Browser live-reloads

4. **Deploy:**
   ```bash
   hugo
   ```
   - Builds optimized production bundle
   - Ready to deploy `public/` directory

## Documentation

For detailed information about each CSS file:
- **CSS_STRUCTURE.md** - Complete guide to the CSS architecture
- **main.css** - Overview and instructions
- This file - Hugo Pipes implementation details

## Credits

Built with Hugo Pipes - no external build tools required!
- https://gohugo.io/hugo-pipes/
- https://gohugo.io/hugo-pipes/bundling/