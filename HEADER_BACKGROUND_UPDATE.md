# Header Background Update Documentation

## Summary
Updated the header section (above the navigation bar) to use the page background color instead of the colored background, creating a cleaner, more modern look.

## Changes Made

### File Modified
**File:** `test/themes/boc/assets/css/main.css`

### 1. Header Section Background
Changed the main header container to use page background variables:

**Before:**
```css
header {
    background-color: var(--boc-teal);
    color: var(--boc-white);
    /* ... */
}
```

**After:**
```css
header {
    background-color: var(--bg-primary);
    color: var(--text-primary);
    /* ... */
}
```

### 2. Header Top Border
Updated the border to use the standard border color variable:

**Before:**
```css
.header-top {
    /* ... */
    border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}
```

**After:**
```css
.header-top {
    /* ... */
    border-bottom: 1px solid var(--border-color);
}
```

### 3. Header Utility Buttons
Updated button styling to work with light background:

**Before:**
```css
.search-toggle,
.lang-toggle,
.mobile-menu-toggle,
.theme-toggle {
    background: transparent;
    border: 1px solid rgba(255, 255, 255, 0.3);
    color: var(--boc-white);
    /* ... */
}

/* Hover state */
.search-toggle:hover,
.lang-toggle:hover,
.mobile-menu-toggle:hover,
.theme-toggle:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: rgba(255, 255, 255, 0.5);
}
```

**After:**
```css
.search-toggle,
.lang-toggle,
.mobile-menu-toggle,
.theme-toggle {
    background: transparent;
    border: 1px solid var(--border-color);
    color: var(--text-primary);
    /* ... */
}

/* Hover state */
.search-toggle:hover,
.lang-toggle:hover,
.mobile-menu-toggle:hover,
.theme-toggle:hover {
    background: var(--bg-secondary);
    border-color: var(--boc-teal);
}
```

## Visual Changes

### Desktop View
- **Header top section**: Now uses white/light background (matches page)
- **Logo**: Consort logo displays on white background
- **Buttons**: Dark text and borders on light background
- **Navigation bar**: Still uses the olive green background (--boc-teal: #394333)

### Mobile View
- **Header**: Light background maintained
- **Mobile menu toggle**: Adapts to light background with proper contrast
- **Navigation drawer**: Remains olive green when opened

### Dark Mode
- **Header**: Uses dark background (--bg-primary: #1a1a1a)
- **Text and borders**: Automatically adjust via CSS variables
- **Buttons**: Light text on dark background
- **Navigation**: Uses dark theme colors

## Layout Structure

```
┌─────────────────────────────────────────┐
│  Header Top (WHITE/LIGHT BACKGROUND)   │
│  ┌──────────────┐  ┌──────────────┐    │
│  │ Consort Logo │  │   Buttons    │    │
│  └──────────────┘  └──────────────┘    │
├─────────────────────────────────────────┤
│  Navigation Bar (OLIVE GREEN #394333)  │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐      │
│  │Menu1│ │Menu2│ │Menu3│ │Menu4│      │
│  └─────┘ └─────┘ └─────┘ └─────┘      │
└─────────────────────────────────────────┘
```

## CSS Variables Used

### Light Mode
- `--bg-primary`: #ffffff (white)
- `--bg-secondary`: #f5f5f5 (light gray for button hover)
- `--text-primary`: #212121 (dark gray text)
- `--border-color`: #e0e0e0 (light border)
- `--boc-teal`: #394333 (olive green for nav and accents)

### Dark Mode
- `--bg-primary`: #1a1a1a (dark background)
- `--bg-secondary`: #2a2a2a (darker gray)
- `--text-primary`: #e0e0e0 (light text)
- `--border-color`: #3a3a3a (dark border)
- `--boc-teal`: #3a3a3a (adjusted for dark mode)

## Benefits

1. **Cleaner Design**: Separates branding area from navigation
2. **Better Logo Visibility**: Logo stands out better on neutral background
3. **Modern Look**: Follows current web design trends
4. **Improved Hierarchy**: Clear distinction between header utilities and navigation
5. **Dark Mode Support**: Automatically adapts via CSS variables
6. **Accessibility**: Better contrast for buttons and text

## Testing Checklist

- [x] Header displays with light background
- [x] Logo is visible and readable on new background
- [x] Buttons have proper contrast and are usable
- [x] Border between header and nav is visible
- [x] Navigation bar retains colored background
- [x] Mobile menu toggle works correctly
- [x] Dark mode switches properly
- [x] Sticky header behavior unchanged
- [x] Shadow effect still visible

## Browser Compatibility

All changes use standard CSS properties supported in:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Notes

- The navigation bar (menu items) retains the olive green background color
- Only the top section (logo and utility buttons) uses the page background
- The change maintains the sticky header functionality
- Box shadow is preserved for depth and visual separation
- All color changes respect the CSS variable system for theme consistency