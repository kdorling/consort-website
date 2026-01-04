# Dark/Light Mode Implementation

## Overview

A comprehensive dark/light mode system has been added to the theme with consistent color schemes across both desktop and mobile views. The theme preference is saved to localStorage and persists across sessions.

## Features

### 1. **Theme Toggle Button**
- Located in the header next to other utility buttons
- Shows moon icon (🌙) in light mode
- Shows sun icon (☀️) in dark mode
- Visible on both desktop and mobile devices
- Accessible via keyboard with proper ARIA labels

### 2. **Color Scheme System**

#### CSS Variables
The theme uses CSS custom properties (variables) for easy theme switching:

**Light Mode (Default):**
```css
--bg-primary: #ffffff
--bg-secondary: #f5f5f5
--bg-tertiary: #fafafa
--text-primary: #212121
--text-secondary: #666666
--border-color: #e0e0e0
--shadow-color: rgba(0, 0, 0, 0.1)
--dropdown-bg: #ffffff
```

**Dark Mode:**
```css
--bg-primary: #1a1a1a
--bg-secondary: #2a2a2a
--bg-tertiary: #222222
--text-primary: #e0e0e0
--text-secondary: #b0b0b0
--border-color: #3a3a3a
--shadow-color: rgba(0, 0, 0, 0.3)
--dropdown-bg: #2a2a2a
```

### 3. **Consistent Color Application**

The following elements adapt to the selected theme:

- **Background colors:** Body, sections, cards, stat cards, tables
- **Text colors:** Headings, body text, links, secondary text
- **Border colors:** All borders adapt to theme
- **Shadow colors:** Box shadows adjust for visibility
- **Dropdown menus:** Both desktop and mobile dropdowns use theme colors
- **Navigation:** Top-level navigation maintains teal brand color, dropdowns adapt

### 4. **Theme-Specific Adjustments**

**Light Mode:**
- Navigation bar: Teal (`#004a5d`) with white text
- Mobile dropdown: Teal (`#005570`)

**Dark Mode:**
- Navigation bar: Gray (`#3a3a3a`) with white text
- Mobile dropdown: Gray (`#3a3a3a`)
- Hover states: Darker gray (`#2a2a2a`)

**Consistent Across Both Themes:**
- Red accent: `#d32f2f`

### 5. **Mobile Consistency**

Mobile menu styling is now consistent with the color scheme system:
- Mobile dropdown backgrounds adapt to theme (teal in light mode, gray in dark mode)
- Text colors are consistent (white text)
- Hover states provide subtle feedback with darker backgrounds
- Theme toggle is visible and functional on mobile devices
- Navigation bar and mobile menu share the same background color in each theme

## Technical Implementation

### HTML (header.html)
```html
<button
    class="theme-toggle"
    aria-label="Toggle dark mode"
    id="theme-toggle"
>
    <span class="theme-icon">🌙</span>
</button>
```

### Dark Mode Navigation Colors
In dark mode, the navigation system uses gray tones instead of teal:
- `--boc-teal: #3a3a3a` (main gray)
- `--boc-dark-teal: #2a2a2a` (darker gray for hover states)
- `--boc-light-teal: #4a4a4a` (lighter gray)
- `--boc-white: #ffffff` (white text)
- `--mobile-dropdown-bg: #3a3a3a` (consistent gray)

### JavaScript (main.js)
The theme toggle functionality includes:
1. **Initialization:** Checks localStorage for saved theme preference
2. **Toggle Logic:** Switches between light and dark themes
3. **Persistence:** Saves preference to localStorage
4. **Icon Update:** Changes icon based on current theme
5. **Default:** Defaults to light mode if no preference is saved

Key function:
```javascript
function initThemeToggle() {
  const currentTheme = localStorage.getItem("theme") || "light";
  document.documentElement.setAttribute("data-theme", currentTheme);
  
  // Toggle logic and localStorage save
}
```

### CSS (main.css)
Theme switching is controlled by the `data-theme` attribute:
```css
:root {
  /* Default light mode variables */
}

[data-theme="dark"] {
  /* Dark mode variable overrides */
}
```

## User Experience

### First Visit
- Theme defaults to light mode
- User can click the theme toggle to switch to dark mode
- Preference is saved immediately

### Returning Visits
- Theme preference is loaded from localStorage
- Site displays in the user's preferred theme instantly
- No flash of wrong theme on page load

### Smooth Transitions
All color changes include smooth CSS transitions:
```css
transition: background-color 0.3s ease, color 0.3s ease;
```

## Accessibility

- Theme toggle button has proper `aria-label`
- Keyboard accessible
- High contrast maintained in both modes
- Text remains readable with proper color contrast ratios
- Focus indicators work in both themes

## Browser Support

- Works in all modern browsers that support CSS custom properties
- localStorage is widely supported
- Graceful fallback to light mode if localStorage is unavailable

## Future Enhancements

Potential improvements:
1. System preference detection (`prefers-color-scheme` media query)
2. Automatic theme switching based on time of day
3. Additional theme variants (e.g., high contrast mode)
4. Theme sync across tabs using storage events

## Testing Checklist

- [x] Theme toggle works on desktop
- [x] Theme toggle works on mobile
- [x] Theme persists across page reloads
- [x] Theme persists across browser sessions
- [x] Desktop dropdown menus adapt to theme
- [x] Mobile dropdown menus maintain consistency
- [x] All text is readable in both themes
- [x] Cards and sections adapt properly
- [x] Tables adapt to theme
- [x] Footer adapts to theme
- [x] Forms and buttons adapt to theme
- [x] Brand colors remain consistent
- [x] Smooth transitions between themes
- [x] No flash of unstyled content

## Files Modified

1. **test/themes/boc/assets/css/main.css**
   - Added dark mode CSS variables
   - Updated color references to use variables
   - Ensured mobile consistency

2. **test/themes/boc/layouts/_partials/header.html**
   - Added theme toggle button

3. **test/themes/boc/assets/js/main.js**
   - Added `initThemeToggle()` function
   - Integrated theme toggle into initialization

## Summary

The dark/light mode implementation provides:
- ✅ Seamless theme switching
- ✅ Persistent user preferences
- ✅ Consistent design across all views
- ✅ Maintained brand identity
- ✅ Excellent user experience
- ✅ Full accessibility support
- ✅ Mobile-desktop consistency