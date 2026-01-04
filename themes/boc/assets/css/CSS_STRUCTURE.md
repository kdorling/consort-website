# CSS Structure Documentation

This document explains the modular CSS architecture for the Bank of Canada themed website.

## File Organization

The CSS has been split into multiple files for better maintainability, organization, and performance. Each file has a specific purpose and contains related styles.

```
css/
├── main.css           # Main entry point - imports all other CSS files
├── variables.css      # CSS custom properties and theme colors
├── base.css          # Reset, typography, and accessibility
├── header.css        # Header, navigation, and mega menu
├── layout.css        # Main content, sections, hero, and stats
├── components.css    # Reusable components (buttons, cards, alerts, etc.)
├── footer.css        # Footer styles
└── responsive.css    # Media queries for mobile/tablet/print
```

## File Descriptions

### 1. `main.css`
**Purpose:** Main entry point that imports all other stylesheets.

**Contains:**
- Import statements for all CSS modules
- Brief documentation comments

**Edit when:** You need to add or remove a CSS module.

---

### 2. `variables.css`
**Purpose:** Centralized CSS custom properties for consistency and easy theming.

**Contains:**
- Brand colors (teal, red, gray variants)
- Light/dark mode color schemes
- Spacing scale (xs, sm, md, lg, xl, 2xl)
- Layout variables (max-width, border-radius, transition-speed)
- Typography settings (font sizes, line heights)
- Responsive breakpoint heights

**Edit when:** 
- Adding new colors to the theme
- Adjusting spacing scale
- Modifying transitions or animations
- Changing typography settings

**Example usage:**
```css
padding: var(--spacing-md);
color: var(--boc-teal);
transition: all var(--transition-speed) ease;
```

---

### 3. `base.css`
**Purpose:** Foundation styles that apply globally.

**Contains:**
- CSS reset (`* { margin: 0; padding: 0; }`)
- Body styles
- Typography (h1-h6, p, a, ul, ol, li)
- Accessibility features (skip-link, focus states, sr-only)

**Edit when:**
- Changing default fonts or sizes
- Modifying link behavior
- Updating accessibility features
- Adjusting global box model

---

### 4. `header.css`
**Purpose:** All header, navigation, and mega menu styles.

**Contains:**
- Header container and layout
- Site branding (logo, title)
- Utility navigation
- Header buttons (search, language, theme toggle, mobile menu)
- Main navigation bar
- Dropdown indicators
- Mega menu (columns, featured links, images, link blocks)
- Scrolled header state (hide/show on scroll)
- Simple dropdown fallback styles

**Edit when:**
- Modifying navigation appearance
- Adjusting mega menu layouts
- Changing dropdown behavior
- Updating header scroll behavior

**Key sections:**
- Header structure (lines 1-144)
- Navigation (lines 146-209)
- Mega menu (lines 211-418)

---

### 5. `layout.css`
**Purpose:** Main content area layouts and sections.

**Contains:**
- Main content container
- Page headers and metadata
- Page content styles
- Hero section (gradient banner)
- Stats section (grid of stat cards)
- Generic sections
- Section intro boxes

**Edit when:**
- Adjusting page layouts
- Modifying hero appearance
- Changing stats grid
- Updating section styles

**Key sections:**
- Main content (lines 1-72)
- Hero section (lines 74-102)
- Stats section (lines 104-145)
- Sections (lines 147-170)

---

### 6. `components.css`
**Purpose:** Reusable UI components used throughout the site.

**Contains:**
- Buttons (primary, secondary)
- Cards (grid, header, body, footer)
- Tags
- Alerts (info, warning, danger)
- Tables
- Read-more links

**Edit when:**
- Creating new button styles
- Modifying card appearance
- Adding new alert types
- Updating table styles

**Key sections:**
- Buttons (lines 1-34)
- Cards (lines 36-89)
- Tags (lines 91-109)
- Alerts (lines 111-137)
- Tables (lines 139-163)

---

### 7. `footer.css`
**Purpose:** Footer styles only.

**Contains:**
- Footer container
- Footer grid layout
- Footer sections and links
- Footer bottom (copyright area)

**Edit when:**
- Changing footer layout
- Modifying footer colors
- Adjusting footer spacing

---

### 8. `responsive.css`
**Purpose:** All media queries for responsive design.

**Contains:**
- Tablet/mobile breakpoint (768px and below)
- Small mobile breakpoint (450px and below)
- Print styles

**Edit when:**
- Adding new breakpoints
- Adjusting mobile layouts
- Modifying mobile menu behavior
- Updating print styles

**Breakpoints:**
- `@media (max-width: 768px)` - Tablet and mobile
- `@media (max-width: 450px)` - Small mobile phones
- `@media (min-width: 769px)` - Desktop-only styles
- `@media print` - Print styles

---

## Development Workflow

### Making Changes

1. **Identify the right file:** Use the descriptions above to find where your changes belong
2. **Use variables:** Always use CSS variables instead of hard-coded values when possible
3. **Test responsively:** Check changes at multiple screen sizes
4. **Maintain organization:** Keep related styles together

### Adding New Styles

1. Determine which file the styles belong in
2. Use existing patterns and variables
3. Add comments for complex sections
4. Follow the established naming conventions

### Variable Usage

Instead of:
```css
.element {
    padding: 20px;
    color: #394333;
    border-radius: 4px;
}
```

Use:
```css
.element {
    padding: var(--spacing-md);
    color: var(--boc-teal);
    border-radius: var(--border-radius);
}
```

### Benefits of This Structure

✅ **Maintainability:** Easy to find and edit specific styles
✅ **Performance:** Can load only needed CSS files
✅ **Collaboration:** Multiple developers can work on different files
✅ **Organization:** Logical grouping of related styles
✅ **Scalability:** Easy to add new modules
✅ **Variables:** Consistent design tokens throughout

## Common Tasks

### Change Brand Colors
Edit `variables.css` - update color variables in `:root` and `[data-theme="dark"]`

### Modify Navigation
Edit `header.css` - find the Navigation or Mega Menu sections

### Adjust Mobile Layout
Edit `responsive.css` - find the appropriate media query

### Add New Component
Edit `components.css` - add your component with proper comments

### Update Spacing
Edit `variables.css` - modify spacing scale variables

### Change Typography
Edit `base.css` for global styles, or `variables.css` for font size variables

## Import Order

The import order in `main.css` is important:

1. **variables.css** - Must be first (defines all CSS custom properties)
2. **base.css** - Base styles and resets
3. **header.css** - Header and navigation
4. **layout.css** - Main content layouts
5. **components.css** - Reusable components
6. **footer.css** - Footer styles
7. **responsive.css** - Must be last (overrides for responsive design)

## Browser Support

All CSS uses modern features with fallbacks:
- CSS Custom Properties (CSS Variables)
- CSS Grid
- Flexbox
- CSS Transitions
- Media Queries

Supports: All modern browsers (Chrome, Firefox, Safari, Edge)