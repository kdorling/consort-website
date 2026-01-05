# Accessibility Guide

This document outlines the accessibility features implemented in the Bank of Canada inspired theme and provides guidelines for maintaining and testing accessibility.

## Overview

This theme follows WCAG 2.1 Level AA standards and implements best practices for web accessibility.

## ✅ Implemented Accessibility Features

### 1. Keyboard Navigation

#### Navigation Menus
- **Tab Navigation**: All navigation items are keyboard accessible
- **Dropdown Menus**: 
  - Press `Enter` or `Space` to open dropdowns
  - Use `Arrow Up/Down` to navigate within dropdowns
  - Press `Escape` to close dropdowns
  - `aria-expanded` attributes indicate dropdown state
- **Mobile Menu**:
  - Press `Escape` to close the mobile sidebar
  - Focus returns to menu toggle button when closed
  - Tab order is maintained throughout

#### Skip Links
- "Skip to content" link at the top of each page
- Appears on keyboard focus
- Allows users to bypass navigation

### 2. Screen Reader Support

#### ARIA Attributes
- **Navigation Landmarks**:
  - `aria-label="Main navigation"` on main nav
  - `aria-label="Utility navigation"` on utility nav
  - `aria-label="[Menu] submenu"` on dropdown menus
- **Button States**:
  - `aria-expanded` on dropdown toggles (true/false)
  - `aria-expanded` on mobile menu toggle
  - `aria-current="page"` on active menu items
- **Hidden Elements**:
  - `aria-hidden="true"` on decorative icons and separators
- **Interactive Elements**:
  - `aria-label` on all icon-only buttons (search, language, theme, menu)

#### Semantic HTML
- Proper heading hierarchy (h1 → h2 → h3)
- `<nav>` elements for navigation regions
- `<main>` for main content
- `<header>` and `<footer>` landmarks
- `<button>` elements for interactive controls

### 3. Visual Accessibility

#### Color Contrast
- **Light Mode**:
  - Text on background: #212121 on #ffffff (AAA)
  - Links: #657b4f on #ffffff (AA)
  - Navigation: White text on #394333 (AAA)
- **Dark Mode**:
  - Text on background: #e0e0e0 on #1a1a1a (AAA)
  - Links: #d9b646 on #1a1a1a (AAA)
  - Headers: #657b4f on #1a1a1a (AA)

#### Focus Indicators
- **Visible Focus States**:
  - 3px outline on all focusable elements
  - Light mode: Gold outline (#d9b646)
  - Dark mode: Light gold outline (#e5c869)
  - 2px offset for better visibility
- **Focus-Visible**:
  - Uses `:focus-visible` to show focus only for keyboard users
  - Mouse clicks don't show focus ring
  - Keyboard navigation always shows focus

### 4. Motion and Animation

#### Reduced Motion Support
```css
@media (prefers-reduced-motion: reduce) {
    /* All animations reduced to near-instant */
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
}
```

Users with vestibular disorders or motion sensitivity can disable animations via their OS settings.

### 5. Touch Target Sizes

#### Mobile Optimization
- All interactive elements have minimum 44x44px touch targets
- Adequate spacing between clickable elements (8px minimum)
- Navigation links: 44px minimum height
- Buttons: Properly sized with padding

### 6. Text and Typography

#### Readable Text
- Base font size: 16px (1rem)
- Line height: 1.6 for body text
- Line height: 1.3 for headings
- Responsive font scaling on mobile

#### Content Structure
- Proper heading hierarchy maintained
- Lists use semantic `<ul>` and `<ol>` tags
- Paragraphs properly marked up
- Links have descriptive text (no "click here")

### 7. Images and Media

#### Alternative Text
- All images have `alt` attributes
- Decorative images: `alt=""`
- Meaningful images: Descriptive alt text
- Logo images: Alt text with site name
- Loading: `loading="lazy"` for performance

### 8. Forms (If Implemented)

When implementing forms, ensure:
- All inputs have associated `<label>` elements
- Required fields marked with `aria-required="true"`
- Error messages associated with inputs via `aria-describedby`
- Fieldsets for grouped controls
- Clear instructions and help text

## 🧪 Accessibility Testing Checklist

### Keyboard Testing
- [ ] Tab through entire page without getting trapped
- [ ] All interactive elements receive visible focus
- [ ] Dropdown menus open and close with keyboard
- [ ] Mobile menu opens/closes with Enter/Space and Escape
- [ ] Skip link appears on focus and works
- [ ] Can navigate without using a mouse

### Screen Reader Testing
Test with:
- **NVDA** (Windows, free)
- **JAWS** (Windows, commercial)
- **VoiceOver** (macOS/iOS, built-in)

Check:
- [ ] All content is announced properly
- [ ] Navigation landmarks are identified
- [ ] Button states are announced (expanded/collapsed)
- [ ] Images have appropriate alt text
- [ ] Heading hierarchy is logical
- [ ] Links are descriptive

### Visual Testing
- [ ] Test with browser zoom at 200%
- [ ] Check color contrast with browser dev tools
- [ ] Test with dark mode enabled
- [ ] Verify focus indicators are visible
- [ ] Check text is readable at all sizes

### Automated Testing Tools

#### Browser Extensions
1. **axe DevTools** (Chrome/Firefox)
   - Comprehensive accessibility scanner
   - Reports WCAG violations
   - Provides remediation guidance

2. **WAVE** (Chrome/Firefox)
   - Visual accessibility evaluation
   - Highlights issues on page
   - Color contrast checker

3. **Lighthouse** (Chrome DevTools)
   - Built into Chrome
   - Accessibility audit score
   - Performance metrics

#### Command Line Tools
```bash
# Pa11y - Automated testing
npm install -g pa11y
pa11y https://your-site.com

# axe-core CLI
npm install -g @axe-core/cli
axe https://your-site.com
```

### Manual Testing Scenarios

#### Test Case 1: Keyboard-Only Navigation
1. Disconnect mouse (or don't use it)
2. Use only Tab, Shift+Tab, Enter, Space, Arrow keys, Escape
3. Navigate entire site
4. Open and close all menus
5. Verify focus is always visible

#### Test Case 2: Screen Reader Navigation
1. Enable screen reader (NVDA/VoiceOver)
2. Navigate by headings (H key in NVDA)
3. Navigate by landmarks (D key in NVDA)
4. Navigate by links (NVDA: Insert+F7)
5. Verify all content is accessible

#### Test Case 3: Mobile Touch Testing
1. Test on actual mobile device
2. Verify all buttons are easy to tap
3. Check spacing between elements
4. Test with one hand
5. Test landscape and portrait

#### Test Case 4: Visual Accessibility
1. Enable dark mode
2. Check contrast in DevTools
3. Zoom to 200% and 400%
4. Enable Windows High Contrast mode
5. Test with different color blindness simulations

## 🔧 Common Issues and Solutions

### Issue: Focus Not Visible
**Solution**: Ensure custom CSS doesn't remove outlines
```css
/* BAD */
*:focus { outline: none; }

/* GOOD */
:focus-visible {
    outline: 3px solid var(--boc-red);
    outline-offset: 2px;
}
```

### Issue: Click-Only Navigation
**Solution**: Always support keyboard events
```javascript
// BAD
element.addEventListener('click', handler);

// GOOD
element.addEventListener('click', handler);
element.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
        handler(e);
    }
});
```

### Issue: Missing ARIA Labels
**Solution**: Add descriptive labels to icon buttons
```html
<!-- BAD -->
<button>🔍</button>

<!-- GOOD -->
<button aria-label="Search">
    <span aria-hidden="true">🔍</span>
</button>
```

### Issue: Keyboard Trap
**Solution**: Always allow Escape to exit, ensure Tab can leave
```javascript
// Always provide exit mechanism
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeMenu();
    }
});
```

## 📋 WCAG 2.1 Level AA Compliance

### Perceivable
- ✅ Text alternatives for images
- ✅ Captions and alternatives for media (if used)
- ✅ Content structured with proper markup
- ✅ Sufficient color contrast (4.5:1 for text)
- ✅ Text can be resized up to 200%

### Operable
- ✅ All functionality available via keyboard
- ✅ No keyboard traps
- ✅ Sufficient time to read content
- ✅ No content that flashes more than 3 times/second
- ✅ Multiple ways to navigate (nav menu, skip links)
- ✅ Clear focus indicators
- ✅ Descriptive link text

### Understandable
- ✅ Language of page identified (lang attribute)
- ✅ Consistent navigation
- ✅ Consistent identification of components
- ✅ Clear labels and instructions (forms)
- ✅ Error identification and suggestions (forms)

### Robust
- ✅ Valid HTML (parseable)
- ✅ Proper use of ARIA attributes
- ✅ Name, role, value provided for UI components
- ✅ Status messages announced (if applicable)

## 🚀 Future Improvements

### Priority 1 (High Impact)
1. **Live Region Announcements**
   - Add `aria-live` regions for dynamic content
   - Announce search results
   - Announce theme changes

2. **Enhanced Error Handling**
   - Add proper error messages for forms
   - Use `aria-invalid` and `aria-describedby`
   - Provide clear recovery instructions

3. **Language Support**
   - Implement bilingual navigation (EN/FR)
   - Add `lang` attributes to content sections
   - Support RTL languages if needed

### Priority 2 (Nice to Have)
1. **High Contrast Mode**
   - Add Windows High Contrast mode support
   - Ensure all UI elements remain visible
   - Test with different contrast themes

2. **Voice Control**
   - Ensure all interactive elements have accessible names
   - Add visible labels where possible
   - Test with Dragon NaturallySpeaking

3. **Cognitive Accessibility**
   - Add breadcrumb navigation
   - Provide site map
   - Add search functionality with suggestions
   - Simplify complex interactions

## 📚 Resources

### Standards and Guidelines
- [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)

### Testing Tools
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [WAVE Browser Extension](https://wave.webaim.org/extension/)
- [Color Contrast Analyzer](https://www.tpgi.com/color-contrast-checker/)
- [Screen Reader Testing](https://www.nvaccess.org/)
- Lighthouse (Built into Chrome DevTools)

### Learning Resources
- [WebAIM](https://webaim.org/)
- [A11y Project](https://www.a11yproject.com/)
- [Inclusive Components](https://inclusive-components.design/)
- [Accessible Components](https://www.scottohara.me/blog/)

## 🤝 Contributing

When adding new features:
1. Test with keyboard navigation
2. Test with screen reader
3. Check color contrast
4. Add appropriate ARIA attributes
5. Ensure focus management
6. Test on mobile devices
7. Run automated tools

Remember: **Accessibility is not a feature, it's a requirement.**

---

Last Updated: 2024
Theme: Bank of Canada Inspired Theme
Accessibility Standard: WCAG 2.1 Level AA
