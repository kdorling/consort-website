# Logo Visibility Fix

## Issue

Multiple logos were displaying at the same time (stacked vertically) instead of only showing one logo.

## Root Cause

The CSS rules were conflicting. The original implementation had:

```css
/* All logos set to display: block by default */
.site-logo {
    display: block;
}

/* Then tried to hide specific types */
.site-logo-mobile {
    display: none;
}

.site-logo-dark {
    display: none;
}
```

This caused logos with multiple classes (e.g., `.site-logo-desktop.site-logo-light`) to still display because the `.site-logo` rule was too general.

---

## Solution

Changed the approach to **hide all logos by default** and only show specific combinations:

```css
/* Hide all logos by default */
.site-logo {
    display: none;
}

/* Show only specific combinations */
.site-logo-desktop.site-logo-light {
    display: block;  /* Desktop Light Mode */
}

[data-theme="dark"] .site-logo-desktop.site-logo-dark {
    display: block;  /* Desktop Dark Mode */
}

@media (max-width: 768px) {
    .site-logo-mobile.site-logo-light {
        display: block;  /* Mobile Light Mode */
    }
    
    [data-theme="dark"] .site-logo-mobile.site-logo-dark {
        display: block;  /* Mobile Dark Mode */
    }
}
```

---

## Changes Made

### File: `themes/boc/assets/css/header.css`

**Before:**
```css
.site-logo {
    display: block;  /* ❌ Too general */
}

.site-logo-desktop {
    display: block;  /* ❌ Conflicts */
}

.site-logo-light {
    display: block;  /* ❌ Conflicts */
}

.site-logo-mobile {
    display: none;
}

.site-logo-dark {
    display: none;
}
```

**After:**
```css
.site-logo {
    display: none;  /* ✅ Hidden by default */
}

/* ✅ Only show specific combinations */
.site-logo-desktop.site-logo-light {
    display: block;
}

/* Desktop Dark Mode - explicitly hide light and show dark */
[data-theme="dark"] .site-logo-desktop.site-logo-light {
    display: none;
}

[data-theme="dark"] .site-logo-desktop.site-logo-dark {
    display: block;
}

@media (max-width: 768px) {
    .site-logo-desktop {
        display: none !important;
    }
    
    .site-logo-mobile.site-logo-light {
        display: block;
    }
    
    [data-theme="dark"] .site-logo-mobile.site-logo-light {
        display: none;
    }
    
    [data-theme="dark"] .site-logo-mobile.site-logo-dark {
        display: block;
    }
}
```

### File: `themes/boc/assets/css/responsive.css`

**Removed redundant mobile logo switching** (now handled in `header.css`):

```css
/* REMOVED - was causing conflicts */
.site-logo-desktop {
    display: none;
}

.site-logo-mobile {
    display: block;
}
```

---

## How It Works Now

### Desktop Light Mode (Default)
- All logos: `display: none`
- Only `.site-logo-desktop.site-logo-light`: `display: block`
- **Result**: 1 logo visible ✓

### Desktop Dark Mode
- All logos: `display: none`
- Desktop light: `display: none` (explicit override)
- Only `[data-theme="dark"] .site-logo-desktop.site-logo-dark`: `display: block`
- **Result**: 1 logo visible ✓

### Mobile Light Mode
- All logos: `display: none`
- Desktop logos: `display: none !important`
- Only `.site-logo-mobile.site-logo-light`: `display: block`
- **Result**: 1 logo visible ✓

### Mobile Dark Mode
- All logos: `display: none`
- Desktop logos: `display: none !important`
- Mobile light: `display: none`
- Only `[data-theme="dark"] .site-logo-mobile.site-logo-dark`: `display: block`
- **Result**: 1 logo visible ✓

---

## Testing Results

### ✅ Fixed Issues
- [x] Only 1 logo displays at a time
- [x] Correct logo shows in light mode
- [x] Correct logo shows in dark mode
- [x] Correct logo shows on desktop
- [x] Correct logo shows on mobile
- [x] No stacking of multiple logos

### ✅ All Scenarios Work
- [x] Desktop + Light = Desktop Light logo only
- [x] Desktop + Dark = Desktop Dark logo only
- [x] Mobile + Light = Mobile Light logo only
- [x] Mobile + Dark = Mobile Dark logo only

---

## CSS Specificity Explanation

### Why This Works

The new approach uses **class combination selectors** with explicit overrides:

```css
/* Base: Hide all */
/* Specificity: 0,1,0 */
.site-logo {
    display: none;
}

/* Desktop Light Mode */
/* Specificity: 0,2,0 (two classes) */
.site-logo-desktop.site-logo-light {
    display: block;
}

/* Dark Mode: Explicitly hide light, show dark */
/* Specificity: 0,3,0 (attribute + two classes) */
[data-theme="dark"] .site-logo-desktop.site-logo-light {
    display: none;  /* Override the light mode rule */
}

[data-theme="dark"] .site-logo-desktop.site-logo-dark {
    display: block;
}
```

### Key Principle

**Start hidden, show only what's needed** instead of **start visible, hide what's not needed**.

---

## Browser Compatibility

✅ Works in all modern browsers
- Chrome
- Firefox
- Safari
- Edge
- Mobile browsers

**CSS Features Used:**
- Class combination selectors (`.class1.class2`)
- Attribute selectors (`[data-theme="dark"]`)
- Media queries (`@media (max-width: 768px)`)
- `!important` flag (for desktop override on mobile)

All widely supported.

---

## Troubleshooting

### If you still see multiple logos:

1. **Clear browser cache**
   ```bash
   # Hard refresh
   # Mac: Cmd + Shift + R
   # Windows: Ctrl + Shift + R
   ```

2. **Rebuild Hugo**
   ```bash
   hugo --quiet
   ```

3. **Verify CSS compiled**
   ```bash
   grep "display: none" public/css/bundle.css | grep site-logo
   ```
   Should show: `.site-logo { ... display: none; ...}`

4. **Check browser DevTools**
   - Only 1 `<img>` should have `display: block`
   - Other 3 should have `display: none`

---

## Summary

**Problem**: Multiple logos showing due to conflicting CSS rules  
**Solution**: Hide all by default, show only specific combinations  
**Result**: Only 1 logo visible at any time  
**Status**: ✅ Fixed and tested  

---

**Fix Date**: January 2025  
**Files Modified**: `header.css`, `responsive.css`  
**Build Required**: Yes (`hugo --quiet`)