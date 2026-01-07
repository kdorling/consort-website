# Mobile Sidebar Bottom Cutoff Fix

## Problem

On actual mobile devices (especially iOS Safari and Android Chrome), the bottom portion of the sidebar navigation menu was getting cut off, even though it appeared fine in desktop browser device emulators.

## Root Cause

The issue occurred due to how mobile browsers handle viewport units:

1. **Dynamic Address Bars**: Mobile browsers have address bars that show/hide as users scroll, causing the viewport height to change dynamically.

2. **`100vh` Unit Issue**: The traditional `100vh` unit represents the largest possible viewport (when the address bar is hidden), but the browser doesn't always adjust elements when the address bar appears.

3. **Missing Safe Area Support**: Modern phones (especially iPhones with notches/home indicators) have "safe areas" at the bottom that need to be accounted for.

## Solution Implemented

### 1. Dynamic Viewport Height (`100dvh`)

Changed from `100vh` to `100dvh` (dynamic viewport height) with a fallback:

```css
.nav-container {
    height: calc(100vh - var(--header-height-mobile)); /* Fallback */
    height: calc(100dvh - var(--header-height-mobile)); /* Modern browsers */
}
```

**What `100dvh` does:**
- Adjusts dynamically as the address bar shows/hides
- Ensures the sidebar always fits the *current* viewport
- Falls back to `100vh` for older browsers

### 2. Safe Area Insets

Added padding to account for iOS safe areas (home indicator, notches):

```css
.nav-container {
    padding-bottom: max(20px, env(safe-area-inset-bottom));
}
```

**What this does:**
- `env(safe-area-inset-bottom)`: System-provided safe area size
- `max(20px, ...)`: Ensures at least 20px padding even on non-notched phones
- Prevents content from being hidden behind the home indicator

### 3. Additional Bottom Padding

Added extra padding to the nav element to ensure the last menu item is always accessible:

```css
.nav-container nav {
    padding: 0 0 20px 0;
}
```

### 4. Updated Viewport Meta Tag

Changed the viewport meta tag to support safe areas:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
```

**Key additions:**
- `initial-scale=1.0`: Prevents zoom issues
- `viewport-fit=cover`: Extends content into safe areas (which we then pad appropriately)

## Browser Support

### `100dvh` Support
- ✅ iOS Safari 15.4+
- ✅ Chrome 108+
- ✅ Firefox 110+
- ✅ Samsung Internet 20+
- ⚠️ Older browsers: Falls back to `100vh`

### `env(safe-area-inset-bottom)` Support
- ✅ iOS Safari 11.0+
- ✅ All modern browsers
- ⚠️ Non-supporting browsers: Uses 20px fallback

## Testing Checklist

Test on actual devices (emulators don't always show the issue):

### iOS (Safari)
- [ ] iPhone with notch (X, 11, 12, 13, 14, 15)
- [ ] iPhone with Dynamic Island (14 Pro, 15 Pro)
- [ ] iPhone with home button (SE, 8)
- [ ] iPad (various sizes)

### Android
- [ ] Chrome on Pixel/Samsung
- [ ] Samsung Internet Browser
- [ ] Various screen sizes

### Test Scenarios
1. **Open sidebar**: Ensure it opens fully
2. **Scroll to bottom**: Verify last menu item is visible and clickable
3. **Rotate device**: Check landscape and portrait
4. **Expand mega menus**: Ensure all content is accessible
5. **Scroll the sidebar**: Verify smooth scrolling
6. **Address bar behavior**: Scroll up/down in sidebar and check no cutoff occurs

## Before vs After

### Before
```css
.nav-container {
    height: calc(100vh - var(--header-height-mobile));
    /* No safe area support */
    /* No bottom padding */
}
```

**Issue**: Bottom 50-100px could be cut off depending on address bar state

### After
```css
.nav-container {
    height: calc(100vh - var(--header-height-mobile)); /* Fallback */
    height: calc(100dvh - var(--header-height-mobile)); /* Dynamic */
    padding-bottom: max(20px, env(safe-area-inset-bottom));
}
```

**Result**: Always fits viewport and respects safe areas

## Additional Notes

### Why Emulators Don't Show the Issue
- Desktop browser emulators don't simulate the dynamic address bar behavior
- They don't account for safe areas properly
- Real devices have different rendering behaviors

### Performance Impact
- Minimal: Only affects mobile navigation
- Uses CSS-only solutions (no JavaScript)
- Hardware-accelerated properties

### Future Improvements
- Consider using `100svh` (small viewport height) for guaranteed minimum space
- Add smooth resize transitions if needed
- Test with screen readers on mobile

## References

- [CSS Values and Units Module Level 4 - Viewport Units](https://www.w3.org/TR/css-values-4/#viewport-relative-lengths)
- [WebKit - Designing Websites for iPhone X](https://webkit.org/blog/7929/designing-websites-for-iphone-x/)
- [MDN: env()](https://developer.mozilla.org/en-US/docs/Web/CSS/env)
- [Can I Use: dvh viewport unit](https://caniuse.com/viewport-unit-variants)

---

**Fixed Date**: 2024
**Files Modified**:
- `themes/boc/assets/css/responsive.css`
- `themes/boc/layouts/_partials/head.html`
