# Mobile Sidebar Testing Guide

## Quick Test Instructions

### 1. Open the Site on Mobile
- Use a real mobile device, OR
- Use Chrome DevTools mobile emulation (F12 → Toggle device toolbar)

### 2. Test the Animation
1. **Open the menu**: Tap the hamburger icon (☰) in the header
   - ✅ Sidebar should slide in from the left at full width
   - ✅ Page content should not scroll
   - ✅ Icon changes to X (✕)

2. **Close the menu**: Try each method
   - Tap the X icon → Menu slides out
   - Press Escape key → Menu slides out

3. **Check smoothness**
   - Animation should be smooth (60fps)
   - No jerky movements
   - No horizontal scrollbar

### 3. Test Different Screen Sizes
Use Chrome DevTools to test:
- iPhone SE (375px) → 280px sidebar
- iPhone 12 Pro (390px) → 280px sidebar
- iPad Mini (768px) → 320px sidebar
- Tablet landscape (800px) → Should switch to desktop view

## Visual Checklist

### Opening Animation
```
Before:                    During:                   After:
┌──────────────┐          ┌──────────────┐         ┌──────────────┐
│              │          │████░░░░░░░░░░│         │██████████████│
│   Content    │    →     │████ Sliding  │    →    │██ Full Menu ██│
│              │          │████ from left│         │██ 100% width██│
└──────────────┘          └──────────────┘         └──────────────┘
  No overlay              Sliding in                Fully open
```

### What to Look For
- [ ] Sidebar enters from LEFT side (not right)
- [ ] Sidebar takes FULL WIDTH (100% of screen)
- [ ] Menu content fades in smoothly
- [ ] No white flash or content jump
- [ ] Shadow visible on right edge of sidebar

## Detailed Test Cases

### Test Case 1: Basic Open/Close
**Steps:**
1. Load any page on mobile view
2. Tap hamburger icon
3. Wait for animation to complete
4. Tap X to close

**Expected Result:**
- Opens in ~300ms with smooth slide
- Closes in ~300ms with smooth slide
- No errors in console

---

### Test Case 2: Navigation While Open
**Steps:**
1. Open the mobile menu
2. Try to scroll the page content behind the menu

**Expected Result:**
- Page content does not scroll (locked)
- Only sidebar content is scrollable

---

### Test Case 3: Dropdown Menus Inside Sidebar
**Steps:**
1. Open the mobile menu
2. Tap "Government" or "Departments"
3. Observe dropdown behavior

**Expected Result:**
- Dropdowns expand vertically inside sidebar
- Mega menu content appears
- Sidebar scrolls if content is long
- No horizontal overflow

---

### Test Case 4: Rapid Toggle
**Steps:**
1. Quickly tap hamburger icon 5 times in a row
2. Observe animation behavior

**Expected Result:**
- Animation handles rapid taps gracefully
- No animation queue buildup
- Menu ends in correct state
- No visual glitches

---

### Test Case 5: Screen Rotation
**Steps:**
1. Open menu on portrait mode
2. Rotate device to landscape
3. Rotate back to portrait

**Expected Result:**
- Menu adapts to new orientation
- No layout breaks
- Sidebar width adjusts appropriately

---

### Test Case 6: Resize from Desktop to Mobile
**Steps:**
1. View site in desktop mode (> 768px)
2. Resize browser to mobile width (< 768px)
3. Open mobile menu

**Expected Result:**
- Desktop nav disappears
- Mobile hamburger icon appears
- Mobile menu functions correctly

---

### Test Case 7: Content Height
**Steps:**
1. Open mobile menu
2. Scroll through all navigation items
3. Expand dropdowns to see full content

**Expected Result:**
- Sidebar is scrollable
- All content accessible
- Smooth touch scrolling
- No content cut off

---

## Browser-Specific Tests

### iOS Safari
- [ ] Smooth slide animation
- [ ] Touch scrolling works (momentum scrolling)
- [ ] No address bar jumping
- [ ] Orientation change handled

### Chrome Mobile
- [ ] 60fps animation
- [ ] No horizontal scroll
- [ ] Fast tap response

### Firefox Mobile
- [ ] Animation smooth
- [ ] Transitions work correctly
- [ ] Z-index layering correct

## Performance Checks

### FPS Monitor (Chrome DevTools)
1. Open DevTools → Performance
2. Start recording
3. Open/close menu several times
4. Stop recording
5. Check FPS graph

**Expected:**
- Consistent 60 FPS during animation
- No dropped frames
- No layout thrashing

### Network Throttling
1. Set network to "Slow 3G"
2. Test menu open/close

**Expected:**
- Animation still smooth (CSS only)
- No delay in menu interaction
- Not dependent on network

## Accessibility Tests

### Keyboard Navigation
1. Use Tab key to focus hamburger icon
2. Press Enter to open menu
3. Tab through menu items
4. Press Escape to close

**Expected:**
- Focus visible on all elements
- Menu opens/closes via keyboard
- Focus trapped in menu when open
- Escape key closes menu

### Screen Reader (VoiceOver/TalkBack)
1. Enable screen reader
2. Navigate to menu button
3. Open menu

**Expected:**
- "Menu button, collapsed" announced
- After opening: "Menu button, expanded"
- Menu items announced correctly

### ARIA Attributes
Inspect the hamburger button:
```html
<button 
  id="mobile-menu-toggle"
  aria-expanded="false"  <!-- or "true" when open -->
  aria-label="Toggle navigation menu"
>
```

## Common Issues & Solutions

### Issue: Horizontal Scrollbar Appears
**Cause:** Content wider than viewport or overflow not hidden
**Fix:** Ensure `overflow-x: hidden` on nav-container

### Issue: Animation Stutters
**Cause:** Too many repaints
**Fix:** Already optimized with CSS transitions



### Issue: Menu Opens Behind Content
**Cause:** Z-index too low
**Fix:** Sidebar is z-index 9998, should be above content

### Issue: Can Scroll Behind Menu
**Cause:** Body overflow not set
**Fix:** `body.mobile-menu-open { overflow: hidden; }` should be present

## Success Criteria

All these should be true:

✅ Sidebar slides in from left in ~300ms
✅ Sidebar takes full screen width (100%)
✅ Content fades in with slight delay
✅ Animation is smooth (60fps)
✅ X button closes menu
✅ Escape key closes menu
✅ Body scroll is locked when menu is open
✅ No horizontal scrollbar at any point
✅ Works on all mobile screen sizes (100% width on all)
✅ Dropdown menus inside sidebar still function
✅ Keyboard navigation works
✅ ARIA attributes update correctly
✅ No console errors
✅ Menu state resets when resizing to desktop

## Test Matrix

| Device/Browser | Open Animation | Close Animation | Scroll Lock | Dropdowns |
|----------------|----------------|-----------------|-------------|-----------|
| iPhone Safari  | ⬜             | ⬜              | ⬜          | ⬜        |
| Android Chrome | ⬜             | ⬜              | ⬜          | ⬜        |
| iPad Safari    | ⬜             | ⬜              | ⬜          | ⬜        |
| Firefox Mobile | ⬜             | ⬜              | ⬜          | ⬜        |
| Chrome DevTools| ⬜             | ⬜              | ⬜          | ⬜        |

## Quick Debug Commands

### Check CSS Compiled
```bash
grep -n "nav-container" public/css/bundle.css
```



### Rebuild Hugo
```bash
hugo --quiet
```

### Check for Errors
Open browser console (F12) and look for:
- Red error messages
- CSS warnings
- JavaScript errors

## Contact/Notes

If issues persist:
1. Clear browser cache
2. Hard refresh (Cmd+Shift+R / Ctrl+Shift+F5)
3. Check console for errors
4. Verify Hugo rebuilt successfully

---

**Last Updated:** January 2025
**Related Docs:**
- `MOBILE_SIDEBAR_SLIDE_ANIMATION.md` - Technical details
- `MOBILE_SIDEBAR_VISUAL_GUIDE.md` - Visual reference
- `MOBILE_SIDEBAR_QUICK_SUMMARY.md` - Quick overview