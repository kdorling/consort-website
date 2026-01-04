# Quick Theme Reference Guide

## Theme Toggle

### Location
The theme toggle button is in the header, next to the mobile menu button.

### Usage
- **Click the button** to switch between light and dark mode
- **Light mode:** Shows moon icon (🌙)
- **Dark mode:** Shows sun icon (☀️)
- **Preference is automatically saved** and persists across sessions

---

## Color Schemes

### Light Mode (Default)
```
Background:  White (#ffffff)
Text:        Dark gray (#212121)
Navigation:  Teal (#004a5d) with white text
Cards:       Light gray (#f5f5f5)
Links:       Teal (#006a85)
```

### Dark Mode
```
Background:  Dark gray (#1a1a1a)
Text:        Light gray (#e0e0e0)
Navigation:  Gray (#3a3a3a) with white text
Cards:       Dark gray (#2a2a2a)
Links:       Light blue (#4da6c7)
```

---

## Navigation

### Desktop
- **Teal bar (light mode)** or **gray bar (dark mode)**
- Click menu items to open dropdowns
- Click outside to close dropdowns
- Press Escape to close all dropdowns

### Mobile
- **Hamburger menu (☰)** to open
- **Close button (✕)** to close
- Full-screen sidebar below header
- Same color scheme as desktop
- Header always visible at top

---

## Mega Menu Links

### Behavior
- Links behave like standard HTML links
- Simple underline on hover
- No card effects or shadows
- Clean and straightforward

### Desktop vs Mobile
- Desktop: Multi-column layout
- Mobile: Single-column stacked layout
- Same link behavior on both

---

## Keyboard Navigation

- **Tab** - Navigate through menu items
- **Enter/Space** - Open dropdowns
- **Arrow Down** - Move to next item in dropdown
- **Arrow Up** - Move to previous item
- **Escape** - Close all dropdowns and return focus

---

## Responsive Breakpoints

- **Desktop:** > 768px
- **Mobile:** ≤ 768px
- **Small mobile:** ≤ 480px

---

## CSS Variables

### Light Mode
```css
--bg-primary: #ffffff
--text-primary: #212121
--boc-teal: #004a5d
--boc-white: #ffffff
```

### Dark Mode
```css
--bg-primary: #1a1a1a
--text-primary: #e0e0e0
--boc-teal: #3a3a3a (gray instead of teal)
--boc-white: #ffffff
```

---

## JavaScript Functions

### Theme Toggle
```javascript
initThemeToggle()
```
- Loads saved preference from localStorage
- Handles theme switching
- Updates button icon

### Mobile Menu
```javascript
initMobileMenu()
```
- Opens/closes mobile sidebar
- Manages body scroll
- Updates button state

### Dropdown Menus
```javascript
initDropdownMenus()
```
- Click-based dropdown toggle
- Closes other dropdowns
- Works on desktop and mobile

---

## localStorage Keys

```javascript
localStorage.getItem('theme')  // Returns 'light' or 'dark'
localStorage.setItem('theme', 'dark')  // Save preference
```

---

## Common Tasks

### Changing the Default Theme
Edit in CSS:
```css
:root {
  /* Change these default values */
}
```

### Adjusting Navigation Colors
Edit in CSS:
```css
[data-theme="dark"] {
  --boc-teal: #3a3a3a;  /* Navigation background */
  --boc-white: #ffffff;  /* Navigation text */
}
```

### Modifying Mobile Breakpoint
Edit in CSS:
```css
@media (max-width: 768px) {
  /* Change 768px to your preferred breakpoint */
}
```

---

## Browser Support

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers (iOS/Android)
- ⚠️ Requires CSS custom properties support

---

## Accessibility Features

- Proper ARIA labels on buttons
- Keyboard navigation support
- High contrast in both themes
- Focus indicators
- Screen reader friendly
- Skip to content link

---

## File Structure

```
test/themes/boc/
├── assets/
│   ├── css/
│   │   └── main.css          (All styles)
│   └── js/
│       └── main.js           (All JavaScript)
└── layouts/
    └── _partials/
        ├── header.html       (Theme toggle button)
        └── menu.html         (Navigation)
```

---

## Quick Troubleshooting

### Theme not switching?
- Check browser console for errors
- Verify localStorage is enabled
- Clear browser cache

### Mobile menu not working?
- Check JavaScript is loaded
- Verify button has correct ID: `mobile-menu-toggle`
- Check nav has ID: `main-nav`

### Colors not changing?
- Verify CSS variables are defined
- Check `data-theme` attribute on `<html>`
- Clear cached CSS files

---

## Performance Tips

- Theme switching is instant (uses CSS variables)
- localStorage is lightweight
- No HTTP requests for theme changes
- Smooth transitions are GPU-accelerated

---

## Customization Examples

### Add a new theme color
```css
:root {
  --my-custom-color: #ff0000;
}

[data-theme="dark"] {
  --my-custom-color: #ff6666;
}
```

### Use custom color
```css
.my-element {
  color: var(--my-custom-color);
}
```

### Disable transitions
```css
* {
  transition: none !important;
}
```

---

## Testing Checklist

- [ ] Theme toggle works on desktop
- [ ] Theme toggle works on mobile
- [ ] Mobile menu opens/closes
- [ ] Mobile menu fills screen
- [ ] Header visible on mobile when menu open
- [ ] Dropdowns work on desktop
- [ ] Links underline on hover
- [ ] Theme persists after refresh
- [ ] Keyboard navigation works
- [ ] All text is readable