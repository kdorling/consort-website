# Mega Menu Animation Test Guide

## Quick Test Instructions

The mega menu should now slide downward smoothly when opened. Here's how to test it:

### Testing Steps

1. **Open the site in your browser**
   - Navigate to `http://localhost:1313` (or your Hugo server URL)
   - Or open `test/public/index.html` directly in a browser

2. **Test Desktop Animation**
   - Ensure browser window is wider than 768px
   - Click on any menu item with a dropdown (e.g., "Monetary Policy", "Markets", "Bank Notes")
   - **Expected**: Menu should smoothly slide down from above while fading in
   - Duration: ~0.35 seconds
   - Click again to close
   - **Expected**: Menu should slide up and fade out

3. **Test Multiple Clicks**
   - Click different menu items in succession
   - **Expected**: Previous menu closes, new menu opens smoothly
   - No jumping or flickering

### What You Should See

#### Opening Animation
```
Frame 1 (0ms):     Menu invisible, 20px above final position
Frame 2 (100ms):   Menu 60% visible, 12px above
Frame 3 (200ms):   Menu 90% visible, 4px above
Frame 4 (350ms):   Menu 100% visible, at final position
```

#### Visual Characteristics
- ✅ Smooth downward slide (not upward or sideways)
- ✅ Gradual fade-in from transparent to solid
- ✅ Ease-out timing (fast start, smooth end)
- ✅ No jank or stuttering
- ✅ Professional, polished appearance

### Troubleshooting

#### If You See NO Animation

**Problem**: Menu appears/disappears instantly

**Solutions**:
1. **Check Browser DevTools Console** (F12)
   - Look for JavaScript errors
   - Verify `dropdown-open` class is being toggled

2. **Verify CSS is loaded**
   - Open DevTools > Elements
   - Inspect the `<nav ul ul>` element
   - Check Computed styles for:
     ```
     transition: opacity 0.35s ease-out, transform 0.35s ease-out, ...
     visibility: hidden
     opacity: 0
     transform: matrix(1, 0, 0, 1, 0, -20)  <- translateY(-20px)
     ```

3. **Force refresh**
   - Hard reload: `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
   - Clear browser cache
   - Rebuild Hugo: `hugo --gc` in terminal

4. **Check browser compatibility**
   - Test in Chrome/Edge (best support)
   - Update browser to latest version

#### If Animation is Choppy

**Problem**: Animation stutters or drops frames

**Solutions**:
1. Check GPU acceleration is enabled in browser settings
2. Close other browser tabs/applications
3. Disable browser extensions temporarily
4. Check DevTools Performance tab for bottlenecks

#### If Menu Stays Visible

**Problem**: Menu doesn't close when clicking outside

**Check**: JavaScript is running
```javascript
// Open browser console and run:
document.getElementById('main-nav')
// Should return an element, not null
```

### Browser Testing Matrix

| Browser | Version | Expected Result |
|---------|---------|----------------|
| Chrome | 90+ | ✅ Full animation support |
| Firefox | 88+ | ✅ Full animation support |
| Safari | 14+ | ✅ Full animation support |
| Edge | 90+ | ✅ Full animation support |
| Mobile Safari | iOS 14+ | ⚡ No animation (by design) |
| Chrome Mobile | Android 10+ | ⚡ No animation (by design) |

### Mobile Behavior

**Important**: Animations are intentionally disabled on mobile (≤768px width) for performance.

**Test Mobile**:
1. Resize browser window to < 768px wide
2. Click hamburger menu
3. Click menu items with dropdowns
4. **Expected**: Instant display (no slide animation)

### DevTools Inspection

#### Check Animation Properties
```javascript
// Run in browser console
const dropdown = document.querySelector('nav ul ul');
const styles = getComputedStyle(dropdown);

console.log('Visibility:', styles.visibility);        // Should be 'hidden'
console.log('Opacity:', styles.opacity);              // Should be '0'
console.log('Transform:', styles.transform);          // Should be 'matrix(1, 0, 0, 1, 0, -20)'
console.log('Transition:', styles.transition);        // Should include 'opacity' and 'transform'
```

#### Watch Animation in Real-Time
1. Open DevTools (F12)
2. Go to **Elements** tab
3. Find `<nav ul ul>` element
4. Right-click > **Break on** > **Attribute modifications**
5. Click a menu item
6. Step through to see class changes

### Performance Check

#### Target Metrics
- **Frame Rate**: 60 FPS
- **Animation Duration**: 350ms
- **No Layout Shifts**: Check for CLS (Cumulative Layout Shift)

#### How to Measure
1. Open DevTools > **Performance** tab
2. Click **Record** button
3. Click menu to open dropdown
4. Stop recording
5. Look for:
   - Green bars (composited frames)
   - Consistent frame timing
   - No red/yellow warnings

### Visual Comparison

#### What Good Animation Looks Like
- Menu slides smoothly downward
- Opacity fades in gradually
- Motion slows down at the end (ease-out)
- No popping or jumping
- Consistent across all menu items

#### What Bad Animation Looks Like
- ❌ Menu jumps into place instantly
- ❌ Flickers or stutters
- ❌ Slides wrong direction (up or sideways)
- ❌ Inconsistent timing between opens/closes
- ❌ Overlapping menus

### Key Files to Check

If animation isn't working, verify these files:

1. **`themes/boc/assets/css/main.css`** (lines 285-321)
   - Should use `visibility: hidden` not `display: none`
   - Should have `transition` properties
   - Transform should be `translateY(-20px)`

2. **`themes/boc/assets/js/main.js`** (lines 6-50)
   - Should toggle `dropdown-open` class
   - No JavaScript errors in console

3. **`public/css/main.css`**
   - Should match source CSS
   - If different, rebuild with `hugo`

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| No animation | CSS not loaded | Hard refresh (Ctrl+Shift+R) |
| Menu jumps | `display: none` used | Verify CSS uses `visibility` |
| Choppy animation | Software rendering | Enable GPU acceleration |
| Wrong direction | Wrong transform value | Check `translateY(-20px)` |
| Too fast/slow | Wrong duration | Adjust `0.35s` value |

### Success Criteria

✅ Menu slides down 20px smoothly  
✅ Animation takes ~0.35 seconds  
✅ Fade-in is smooth and gradual  
✅ Ease-out timing feels natural  
✅ Multiple clicks work correctly  
✅ No console errors  
✅ Works across browsers  
✅ Mobile shows instant (no animation)  
✅ No performance issues  

### Next Steps

If animation is working correctly:
- ✅ Animation is live and functional
- Consider customizing duration/distance to taste
- Optional: Add `prefers-reduced-motion` support

If animation is NOT working:
1. Check browser console for errors
2. Verify CSS file is correct (see "Key Files to Check")
3. Hard refresh browser cache
4. Test in different browser
5. Rebuild Hugo site: `cd test && hugo --gc`

### Customization Options

Want to adjust the animation? Edit `themes/boc/assets/css/main.css`:

```css
nav ul ul {
    transform: translateY(-20px);  /* Change -20px for more/less distance */
    transition:
        opacity 0.35s ease-out,    /* Change 0.35s for speed */
        transform 0.35s ease-out,
        visibility 0s linear 0.35s;
}
```

**Suggestions**:
- **Faster**: Change to `0.25s`
- **Slower**: Change to `0.45s`
- **More dramatic**: Change to `translateY(-40px)`
- **Subtle**: Change to `translateY(-10px)`

### Support

If you're still not seeing animations:
1. Confirm Hugo version: `hugo version` (should be 0.80+)
2. Check if JavaScript is enabled in browser
3. Verify no browser extensions blocking CSS/JS
4. Try incognito/private browsing mode
5. Check `hugo.toml` for any minification settings

### Summary

The animation should provide a smooth, professional slide-down effect that enhances the user experience without being distracting. The key is the transition from `visibility: hidden` + `opacity: 0` + `translateY(-20px)` to `visibility: visible` + `opacity: 1` + `translateY(0)` over 0.35 seconds with ease-out timing.