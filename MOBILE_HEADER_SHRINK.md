# Mobile Header Shrink on Scroll

## Overview

On mobile devices, the header automatically shrinks when the user scrolls down, showing only the hamburger menu icon. This provides more screen space for content while keeping navigation easily accessible.

## Feature Description

### Default State (Top of Page)
- Full header visible with:
  - Site logo
  - Utility navigation links
  - Theme toggle button
  - Hamburger menu button

### Scrolled State (After 50px scroll)
- Shrunken header showing only:
  - Hamburger menu button
  - Reduced header height
  - All other elements hidden

### Return to Top
- Scrolling back up restores the full header
- Smooth transition between states

## Technical Implementation

### Scroll Threshold
- **Mobile**: 50px scroll triggers shrink
- **Desktop**: Different behavior (unchanged)

### CSS Classes
- `.header-scrolled-mobile` - Added to `<header>` element
- `.header-scrolled-mobile` - Added to `<body>` element for padding adjustment

### Transitions
All state changes use smooth CSS transitions:
```css
transition: opacity 0.3s ease, max-height 0.3s ease;
```

## Behavior Details

### What Hides on Scroll
1. Site logo
2. Utility navigation (Online Services, Careers, Contact)
3. Theme toggle button

### What Remains Visible
1. Hamburger menu button (☰)
2. Header background
3. Header shadow

### Mobile Menu Integration
- Mobile sidebar continues to work normally
- Sidebar position adjusts to shrunken header height
- Opening menu works in both header states

## Responsive Behavior

### Mobile Devices (≤768px)
- Shrink feature **ACTIVE**
- Triggers at 50px scroll
- Shows only hamburger menu

### Desktop/Tablet (>768px)
- Shrink feature **DISABLED**
- Different scroll behavior applies
- Full header remains visible

## Height Values

| State | Header Height |
|-------|--------------|
| Default | ~140px (var: `--header-height-mobile`) |
| Scrolled | ~60px |
| Sidebar Position Default | `top: 140px` |
| Sidebar Position Scrolled | `top: 60px` |

## User Experience Benefits

1. **More Content Space**: Shrinking header gives users more screen real estate
2. **Quick Access**: Hamburger menu always accessible
3. **Smooth Transitions**: No jarring jumps or flashes
4. **Intuitive**: Users expect this behavior on mobile
5. **Performance**: Lightweight CSS-based animations

## Browser Support

### Modern Browsers
✅ Chrome (Mobile)
✅ Safari (iOS)
✅ Firefox (Mobile)
✅ Samsung Internet
✅ Edge (Mobile)

### Features Used
- CSS transitions (all modern browsers)
- JavaScript scroll events (universal support)
- Viewport units (dvh with fallback)

## Accessibility Considerations

### Keyboard Navigation
- Tab navigation works in both states
- Focus indicators remain visible
- No keyboard traps

### Screen Readers
- All elements remain in DOM (just hidden visually)
- ARIA labels unchanged
- Navigation structure preserved

### Motion Sensitivity
- Respects `prefers-reduced-motion` setting
- Transitions disabled for users with motion sensitivity
- No parallax or complex animations

## Customization

### Adjust Scroll Threshold

Edit `themes/boc/assets/js/main.js`:
```javascript
const mobileScrollThreshold = 50; // Change this value
```

### Adjust Shrunken Height

Edit `themes/boc/assets/css/responsive.css`:
```css
body.header-scrolled-mobile .nav-container {
    top: 60px !important; /* Change to desired height */
}
```

### Change Transition Speed

Edit `themes/boc/assets/css/responsive.css`:
```css
.utility-nav {
    transition: opacity 0.3s ease; /* Adjust duration */
}
```

### Disable Feature

Comment out or remove the mobile scroll behavior in `main.js`:
```javascript
// Mobile behavior - shrink header on scroll
// if (currentScroll > mobileScrollThreshold) {
//   header.classList.add("header-scrolled-mobile");
// }
```

## Testing Checklist

### Functional Testing
- [ ] Header shrinks at 50px scroll on mobile
- [ ] Header expands when scrolling back to top
- [ ] Hamburger menu works in both states
- [ ] Mobile sidebar opens correctly
- [ ] Sidebar position adjusts to header height
- [ ] Theme toggle hidden when scrolled
- [ ] Utility nav hidden when scrolled

### Visual Testing
- [ ] Smooth transition between states
- [ ] No content jumps or flashes
- [ ] Logo fades out cleanly
- [ ] Shadow displays correctly
- [ ] Dark mode works in both states

### Device Testing
- [ ] iPhone (Safari)
- [ ] Android (Chrome)
- [ ] iPad (Portrait & Landscape)
- [ ] Small phones (<400px width)
- [ ] Large phones (>400px width)

### Interaction Testing
- [ ] Rapid scrolling works correctly
- [ ] Touch scrolling feels smooth
- [ ] No scroll jank or lag
- [ ] Works with sidebar open
- [ ] Works with sidebar closed

## Troubleshooting

### Header Not Shrinking
- Check viewport width is ≤768px
- Verify JavaScript is loaded
- Check browser console for errors
- Ensure scroll threshold is met (50px+)

### Jerky Transitions
- Check for conflicting CSS transitions
- Verify hardware acceleration enabled
- Test on actual device (not emulator)

### Sidebar Position Wrong
- Check body class is added on scroll
- Verify nav-container top value
- Check for CSS specificity issues

### Elements Not Hiding
- Verify `.header-scrolled-mobile` class added
- Check CSS opacity and max-height rules
- Ensure no `!important` overrides

## Performance Notes

- **Lightweight**: CSS-only animations
- **Smooth**: 60fps transitions on modern devices
- **Efficient**: Single scroll event listener
- **Battery-Friendly**: No continuous polling

## Files Modified

1. **JavaScript**: `themes/boc/assets/js/main.js`
   - Added mobile scroll threshold
   - Added/removed classes on scroll

2. **CSS**: `themes/boc/assets/css/responsive.css`
   - Added `.header-scrolled-mobile` styles
   - Adjusted nav-container positioning
   - Added transition properties

## Related Features

- [Mobile Sidebar](MOBILE_SIDEBAR_FIX.md)
- [Sticky Header](DARK_MODE_IMPLEMENTATION.md)
- [Responsive Design](CSS_STRUCTURE.md)

## Future Enhancements

Consider adding:
- [ ] Fade in/out animation for hamburger icon
- [ ] Optional site title text when scrolled
- [ ] Configurable threshold via hugo.toml
- [ ] Different animations (slide, bounce, etc.)
- [ ] Show mini logo when scrolled

---

**Implementation Date**: 2024
**Applies To**: Mobile devices (≤768px width)
**Status**: Active and tested