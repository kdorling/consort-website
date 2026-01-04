# Mega Menu Nested List Visibility Fix

## Problem

Links inside the mega menu (such as "Mayor Biography", "Council Biographies", etc.) were not visible even when the mega menu dropdown was open.

## Root Cause

The issue was caused by CSS selector specificity conflict:

1. **Hiding Rule**: `nav ul ul` was used to hide dropdown menus with:
   - `max-height: 0`
   - `overflow: hidden`
   - `pointer-events: none`

2. **Nested Structure**: The mega menu contains nested `<ul>` elements for link lists:
   ```
   nav > ul > li > ul (dropdown container)
     └── li.mega-menu-columns
         └── div.mega-menu-column
             └── div.mega-menu-link-block
                 └── ul (this was being hidden!)
                     └── li > a (links were invisible)
   ```

3. **Conflict**: The inner `<ul>` inside `.mega-menu-link-block` was also being targeted by `nav ul ul`, causing it to be hidden even when the parent dropdown was open.

## Solution

Added explicit CSS overrides to ensure lists inside `.mega-menu-link-block` are always visible and accessible, regardless of the parent dropdown state.

## Changes Made

### File Modified
**File**: `test/themes/boc/assets/css/main.css`

### CSS Addition (Lines ~425-428)

Added important overrides to `.mega-menu-link-block ul`:

```css
.mega-menu-link-block ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: block;
    max-height: none !important;      /* Override nav ul ul hiding */
    overflow: visible !important;      /* Override nav ul ul hiding */
    position: static !important;       /* Override nav ul ul positioning */
    pointer-events: auto !important;   /* Override nav ul ul interactivity */
}
```

### Why !important Was Necessary

The `!important` flag was required because:
1. The hiding rules from `nav ul ul` have higher specificity
2. The nested structure means multiple selectors could apply
3. We need to guarantee these lists are always visible inside the mega menu
4. It's a controlled override for a specific component

## Technical Details

### Selector Specificity Before Fix
- `nav ul ul` = 0,0,0,3 (3 elements)
- `.mega-menu-link-block ul` = 0,0,1,1 (1 class, 1 element)
- Result: `nav ul ul` would win in some contexts

### With !important Override
- `.mega-menu-link-block ul` rules now always apply
- Ensures mega menu internal lists are never hidden
- Maintains proper positioning and interactivity

## Result

✅ **Links Now Visible**: All links inside mega menu blocks are now visible  
✅ **Proper Hierarchy**: Dropdown containers can still hide/show correctly  
✅ **Click Targets**: Links are interactive with proper pointer events  
✅ **No Side Effects**: Override only affects mega-menu-link-block lists

## Testing Checklist

- [x] "Mayor Biography" link is visible in Government & Council mega menu
- [x] "Council Biographies" link is visible
- [x] All other mega menu links are visible in their respective sections
- [x] Dropdown opening/closing still works correctly
- [x] Hover states work on all links
- [x] Links are clickable and navigate correctly
- [x] Mobile menu functionality not affected

## Files Modified

1. `test/themes/boc/assets/css/main.css` - Added visibility overrides for mega-menu-link-block ul elements

## Build Status

✅ Site rebuilt successfully with `hugo` command  
✅ Changes verified in `public/css/main.css`  
✅ All mega menu links now visible and interactive

## Related Issues

This fix complements the earlier mega-menu link styling improvements (padding, hover states) and ensures those styled links are actually visible to users.