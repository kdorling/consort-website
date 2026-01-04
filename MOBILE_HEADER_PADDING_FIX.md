# Mobile Header Padding Fix

## Issue
On mobile views (768px and below), page content was being hidden behind the fixed header. Users had to scroll down to see content that should have been visible at the top of the page.

## Root Cause
The header is set to `position: fixed` on mobile devices to keep it visible while scrolling. However, the body's `padding-top` was hardcoded to `80px`, which was insufficient to account for the actual header height of `140px`.

This caused a 60px gap where content was hidden behind the header.

## Files Changed

### `themes/boc/assets/css/responsive.css`

**Before:**
```css
@media (max-width: 768px) {
    body {
        padding-top: 80px;
    }
```

**After:**
```css
@media (max-width: 768px) {
    body {
        padding-top: var(--header-height-mobile);
    }
```

## How It Works

The fix uses the CSS variable `--header-height-mobile` (defined as `140px` in `variables.css`) instead of a hardcoded value. This ensures:

1. **Consistency**: The body padding matches the actual header height
2. **Maintainability**: If the header height changes in the future, only the CSS variable needs to be updated
3. **Alignment**: The padding is now consistent with other mobile calculations that use the same variable

## Related CSS Variables

From `themes/boc/assets/css/variables.css`:
- `--header-height-mobile: 140px` - Used for tablets and phones (max-width: 768px)
- `--header-height-small: 130px` - Used for small phones (max-width: 450px)

## Testing

To verify the fix works correctly:

1. Open the site on a mobile device or use browser DevTools mobile emulation
2. Check that page content is not hidden behind the header
3. Verify the top of the content is properly visible when the page loads
4. Test on different screen sizes (768px, 450px, etc.)

## Impact

- ✅ Page content is now fully visible on mobile views
- ✅ No content is hidden behind the fixed header
- ✅ Proper spacing between header and main content
- ✅ Better user experience on mobile devices