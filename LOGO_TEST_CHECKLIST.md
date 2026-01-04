# Logo Visibility Test Checklist

## Complete Testing Guide

Use this checklist to verify that only ONE logo displays in each scenario.

---

## Desktop Testing (>768px)

### Light Mode
- [ ] Open site on desktop browser (>768px width)
- [ ] Ensure light mode is active (check theme toggle)
- [ ] **Expected**: Desktop light logo visible
- [ ] **Expected**: Desktop dark logo hidden
- [ ] **Expected**: Mobile logos hidden
- [ ] **Count**: Only 1 logo visible

### Dark Mode
- [ ] Stay on desktop (>768px width)
- [ ] Toggle to dark mode
- [ ] **Expected**: Desktop dark logo visible
- [ ] **Expected**: Desktop light logo hidden
- [ ] **Expected**: Mobile logos hidden
- [ ] **Count**: Only 1 logo visible

### Toggle Test
- [ ] Toggle dark mode on/off repeatedly
- [ ] Logo should switch smoothly
- [ ] No flash of multiple logos
- [ ] No stacking or duplication

---

## Mobile Testing (≤768px)

### Light Mode
- [ ] Resize browser to ≤768px OR use mobile device
- [ ] Ensure light mode is active
- [ ] **Expected**: Mobile light logo visible
- [ ] **Expected**: Mobile dark logo hidden
- [ ] **Expected**: Desktop logos hidden
- [ ] **Count**: Only 1 logo visible

### Dark Mode
- [ ] Stay on mobile width (≤768px)
- [ ] Toggle to dark mode
- [ ] **Expected**: Mobile dark logo visible
- [ ] **Expected**: Mobile light logo hidden
- [ ] **Expected**: Desktop logos hidden
- [ ] **Count**: Only 1 logo visible

### Toggle Test
- [ ] Toggle dark mode on/off repeatedly
- [ ] Logo should switch smoothly
- [ ] No multiple logos visible
- [ ] No layout shift

---

## Responsive Testing

### Resize: Desktop → Mobile (Light Mode)
- [ ] Start at desktop width (>768px) in light mode
- [ ] Desktop light logo visible
- [ ] Slowly resize window smaller
- [ ] At 768px breakpoint, should switch to mobile light logo
- [ ] No overlap or flash of multiple logos
- [ ] **Count**: Only 1 logo visible at all times

### Resize: Desktop → Mobile (Dark Mode)
- [ ] Start at desktop width (>768px) in dark mode
- [ ] Desktop dark logo visible
- [ ] Slowly resize window smaller
- [ ] At 768px breakpoint, should switch to mobile dark logo
- [ ] No overlap or flash of multiple logos
- [ ] **Count**: Only 1 logo visible at all times

### Resize: Mobile → Desktop (Light Mode)
- [ ] Start at mobile width (≤768px) in light mode
- [ ] Mobile light logo visible
- [ ] Slowly resize window larger
- [ ] At 769px, should switch to desktop light logo
- [ ] Smooth transition
- [ ] **Count**: Only 1 logo visible at all times

### Resize: Mobile → Desktop (Dark Mode)
- [ ] Start at mobile width (≤768px) in dark mode
- [ ] Mobile dark logo visible
- [ ] Slowly resize window larger
- [ ] At 769px, should switch to desktop dark logo
- [ ] Smooth transition
- [ ] **Count**: Only 1 logo visible at all times

---

## Cross-Browser Testing

### Chrome Desktop
- [ ] Light mode: 1 logo only
- [ ] Dark mode: 1 logo only
- [ ] Resize: smooth transitions

### Firefox Desktop
- [ ] Light mode: 1 logo only
- [ ] Dark mode: 1 logo only
- [ ] Resize: smooth transitions

### Safari Desktop
- [ ] Light mode: 1 logo only
- [ ] Dark mode: 1 logo only
- [ ] Resize: smooth transitions

### Safari iOS (Mobile)
- [ ] Light mode: 1 logo only
- [ ] Dark mode: 1 logo only
- [ ] Portrait/landscape: works correctly

### Chrome Android (Mobile)
- [ ] Light mode: 1 logo only
- [ ] Dark mode: 1 logo only
- [ ] Portrait/landscape: works correctly

---

## Browser DevTools Inspection

### Desktop Light Mode
1. Open DevTools (F12)
2. Inspect header
3. Find all 4 `<img class="site-logo ...">` elements
4. Check computed styles:

**Expected:**
```
✓ .site-logo-desktop.site-logo-light { display: block; }
✗ .site-logo-desktop.site-logo-dark { display: none; }
✗ .site-logo-mobile.site-logo-light { display: none; }
✗ .site-logo-mobile.site-logo-dark { display: none; }
```

### Desktop Dark Mode
1. Toggle dark mode
2. Inspect all 4 logo elements
3. Check computed styles:

**Expected:**
```
✗ .site-logo-desktop.site-logo-light { display: none; }
✓ .site-logo-desktop.site-logo-dark { display: block; }
✗ .site-logo-mobile.site-logo-light { display: none; }
✗ .site-logo-mobile.site-logo-dark { display: none; }
```

### Mobile Light Mode
1. Switch to mobile width (≤768px)
2. Ensure light mode
3. Check computed styles:

**Expected:**
```
✗ .site-logo-desktop.site-logo-light { display: none !important; }
✗ .site-logo-desktop.site-logo-dark { display: none !important; }
✓ .site-logo-mobile.site-logo-light { display: block; }
✗ .site-logo-mobile.site-logo-dark { display: none; }
```

### Mobile Dark Mode
1. Stay at mobile width
2. Toggle dark mode
3. Check computed styles:

**Expected:**
```
✗ .site-logo-desktop.site-logo-light { display: none !important; }
✗ .site-logo-desktop.site-logo-dark { display: none !important; }
✗ .site-logo-mobile.site-logo-light { display: none; }
✓ .site-logo-mobile.site-logo-dark { display: block; }
```

---

## Common Issues to Check

### Issue: Two logos visible on desktop dark mode
**Fix Applied**: Added explicit hide rule for desktop light logo in dark mode
```css
[data-theme="dark"] .site-logo-desktop.site-logo-light {
    display: none;
}
```

### Issue: Multiple logos visible
**Cause**: CSS not compiled or browser cache
**Solution**:
1. Rebuild: `hugo --quiet`
2. Hard refresh browser (Cmd+Shift+R / Ctrl+Shift+F5)
3. Clear browser cache

### Issue: Wrong logo showing
**Check**:
- Correct logo paths in `hugo.toml`
- Files exist in `static/images/`
- Hugo rebuilt after config changes

### Issue: Logo not switching on theme toggle
**Check**:
- Theme toggle JavaScript working
- `[data-theme="dark"]` applied to `<html>` element
- CSS dark mode rules present

---

## Visual Verification

At any given moment, you should see:

```
┌─────────────────────────┐
│  ☰  [SINGLE LOGO]   🔍  │  ← Only ONE logo
├─────────────────────────┤
│                         │
│  Content...             │
│                         │
└─────────────────────────┘
```

**NOT:**
```
┌─────────────────────────┐
│  ☰  [LOGO 1]        🔍  │  ← ❌ Wrong!
│      [LOGO 2]           │  ← Multiple logos
├─────────────────────────┤
```

---

## Quick Test Commands

### Verify CSS Compiled
```bash
grep "display: none" public/css/bundle.css | grep site-logo
```

Should show:
- `.site-logo { display: none; }`
- Dark mode overrides
- Mobile overrides

### Check HTML Structure
```bash
grep "site-logo" public/index.html | wc -l
```

Should show: **4** (4 logo img tags)

### Verify Logo Files Exist
```bash
ls -l static/images/*logo*.svg
```

Should list your logo files.

---

## Success Criteria

✅ Only 1 logo visible at any time  
✅ Correct logo for desktop light mode  
✅ Correct logo for desktop dark mode  
✅ Correct logo for mobile light mode  
✅ Correct logo for mobile dark mode  
✅ Smooth transitions when resizing  
✅ Smooth transitions when toggling theme  
✅ No flashing or duplication  
✅ Works in all major browsers  
✅ DevTools shows correct display values  

---

## Testing Summary

| Scenario | Expected Logo | Status |
|----------|---------------|--------|
| Desktop + Light | Desktop Light | ⬜ |
| Desktop + Dark | Desktop Dark | ⬜ |
| Mobile + Light | Mobile Light | ⬜ |
| Mobile + Dark | Mobile Dark | ⬜ |
| Resize transitions | Smooth | ⬜ |
| Theme toggle | Smooth | ⬜ |

---

## Report Issues

If any test fails:

1. Note the specific scenario
2. Check DevTools computed styles
3. Verify CSS compiled correctly
4. Clear browser cache
5. Check console for errors
6. Compare with expected behavior above

---

**Last Updated**: January 2025  
**Status**: All tests should pass ✅