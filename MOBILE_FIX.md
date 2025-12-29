# Mobile Dropdown Fix - Complete Guide

## Issue
Dropdown menu content is not visible on mobile devices.

## Root Cause Analysis

The mobile dropdowns may have visibility issues due to:
1. CSS specificity conflicts between desktop and mobile styles
2. JavaScript not properly toggling the `mobile-open` class
3. CSS animations/transforms interfering with display
4. Z-index stacking issues on mobile

## Solutions Implemented

### 1. CSS Fixes (themes/boc/assets/css/main.css)

#### Ensured Mobile Dropdown Visibility
```css
@media (max-width: 768px) {
    /* Mobile dropdown container */
    nav ul ul {
        position: static;
        display: none;
        background-color: var(--boc-dark-teal);
        width: 100%;
        padding: 0;
        border-top: none;
        flex-direction: column;
        opacity: 1 !important;              /* Override desktop animation */
        transform: none !important;          /* Remove slide animation */
        pointer-events: auto !important;     /* Ensure clickable */
    }

    /* Show dropdown when open */
    nav ul li.mobile-open > ul,
    nav ul li.dropdown-open > ul {
        display: flex !important;
        visibility: visible !important;
    }

    /* Dropdown link styling */
    nav ul ul a {
        margin: 0;
        padding: 12px 20px 12px 40px;
        color: #ffffff !important;           /* White text */
        background-color: rgba(0, 0, 0, 0.2); /* Slightly darker background */
        border-left: 3px solid transparent;
        font-size: 0.95rem;
        line-height: 1.5;
        display: block;
        text-decoration: none;
    }

    /* Hover/Focus state */
    nav ul ul a:hover,
    nav ul ul a:focus {
        background-color: rgba(255, 255, 255, 0.2);
        color: #ffffff !important;
        border-left-color: var(--boc-red);
        text-decoration: none;
    }

    /* Ensure list items are visible */
    nav ul ul li {
        display: block !important;
        opacity: 1 !important;
        width: 100%;
    }
}
```

### 2. JavaScript Toggle (themes/boc/assets/js/main.js)

The JavaScript properly handles mobile toggling:

```javascript
link.addEventListener("click", function (e) {
    if (window.innerWidth > 768) {
        // Desktop: toggle dropdown-open
        e.preventDefault();
        parent.classList.toggle("dropdown-open");
    } else {
        // Mobile: toggle mobile-open
        e.preventDefault();
        parent.classList.toggle("mobile-open");
        console.log("Mobile dropdown toggled:", 
                    parent.classList.contains("mobile-open"));
    }
});
```

## Testing Steps

### On Mobile Device or Browser Dev Tools

1. **Open the site and resize to mobile (<768px)**
   ```
   http://localhost:1313
   ```

2. **Click the hamburger menu (☰)**
   - Navigation should slide down
   - Menu items visible in teal background

3. **Click "Monetary Policy"** (or any menu with ▼)
   - Dropdown should expand below
   - Should see white text on darker teal background
   - Items should be:
     - Policy Interest Rate
     - Inflation
     - Monetary Policy Framework
     - Publications

4. **Check visibility:**
   - Text should be bright white (#ffffff)
   - Background should be dark teal with slight transparency
   - Items should be indented (40px from left)

5. **Click another dropdown**
   - Previous dropdown should stay open
   - New dropdown should open

6. **Tap outside or close hamburger menu**
   - All dropdowns should close
   - Menu should collapse

### Using Browser Developer Tools

1. **Open DevTools (F12)**
2. **Toggle Device Toolbar (Ctrl+Shift+M or Cmd+Shift+M)**
3. **Select a mobile device** (e.g., iPhone 12, Pixel 5)
4. **Open Console** to see debug messages
5. **Click menu items** and watch console:
   ```
   Mobile dropdown toggled: true
   Mobile dropdown toggled: false
   ```

### Manual Verification Checklist

- [ ] Hamburger menu (☰) visible on mobile
- [ ] Clicking hamburger opens navigation
- [ ] Menu items with ▼ are clickable
- [ ] Clicking menu item toggles dropdown
- [ ] Dropdown text is white and clearly visible
- [ ] Dropdown background is dark teal
- [ ] Items are indented from left
- [ ] Multiple dropdowns can be open
- [ ] Clicking hamburger again closes menu
- [ ] Console shows toggle messages

## Debug Commands

### Check if JavaScript is loaded:
Open browser console and type:
```javascript
document.getElementById("main-nav")
```
Should return the nav element, not null.

### Check for mobile-open class:
```javascript
document.querySelectorAll(".mobile-open")
```
Should show elements when dropdowns are open.

### Force open a dropdown:
```javascript
document.querySelector(".has-dropdown").classList.add("mobile-open")
```

### Check computed styles:
```javascript
window.getComputedStyle(document.querySelector("nav ul ul")).display
```
Should be "flex" when open, "none" when closed.

## Common Issues and Fixes

### Issue: Dropdown opens but no text visible

**Cause**: Text color matches background
**Fix**: Ensure CSS has:
```css
nav ul ul a {
    color: #ffffff !important;
}
```

### Issue: Dropdown doesn't open at all

**Cause**: JavaScript not firing or CSS display override
**Fix**: 
1. Check console for errors
2. Verify `.mobile-open` class is added (inspect element)
3. Check CSS specificity with `!important`

### Issue: Dropdown opens on desktop instead of mobile

**Cause**: Window width check incorrect
**Fix**: Verify `window.innerWidth <= 768` in JavaScript

### Issue: Multiple clicks needed

**Cause**: Event bubbling or preventDefault missing
**Fix**: Ensure `e.preventDefault()` is present in click handler

### Issue: Text is too dark or invisible

**Cause**: Color inheritance or specificity issues
**Fix**: Use `!important` on mobile text color:
```css
color: #ffffff !important;
```

## Visual Reference

### What You Should See on Mobile:

```
┌─────────────────────┐
│ Bank of Canada  ☰  │  <- Header (teal)
├─────────────────────┤
│ Home                │  <- Menu items
│ Monetary Policy ▼   │
│   Policy Rate       │  <- Dropdown (darker teal)
│   Inflation         │  <- White text
│   Framework         │
│ Financial System ▼  │
│ Markets ▼           │
└─────────────────────┘
```

### Color Scheme:
- Header: Teal (#004a5d)
- Menu items: Teal (#004a5d)
- Dropdown background: Dark teal (#003744) with rgba(0,0,0,0.2) overlay
- Dropdown text: Pure white (#ffffff)
- Hover: rgba(255,255,255,0.2) overlay
- Active border: Red (#d32f2f)

## Rebuild and Test

```bash
cd /Users/kevindorling/code/test
hugo --minify
hugo server -D
```

1. Open http://localhost:1313
2. Open DevTools (F12)
3. Toggle device toolbar
4. Select mobile device
5. Test dropdown functionality

## Success Criteria

✅ Hamburger menu opens/closes navigation
✅ Menu items with ▼ are clickable
✅ Dropdowns expand below parent item
✅ White text clearly visible on dark teal background
✅ Items indented 40px from left
✅ Hover states work (lighter background)
✅ Console shows "Mobile dropdown toggled: true/false"
✅ No JavaScript errors in console
✅ Multiple dropdowns can be open simultaneously
✅ Smooth user experience

## If Still Not Working

1. **Clear browser cache**: Ctrl+Shift+Delete or Cmd+Shift+Delete
2. **Hard refresh**: Ctrl+F5 or Cmd+Shift+R
3. **Restart Hugo server**: Kill and restart `hugo server -D`
4. **Check CSS is loaded**: View source, verify CSS file is included
5. **Check JS is loaded**: View source, verify JS file is included
6. **Inspect element**: Right-click dropdown, inspect to see actual styles

## Contact/Support

If issues persist:
1. Check browser console for errors
2. Verify Hugo version: `hugo version`
3. Ensure build completed: Check for errors in `hugo --minify`
4. Review CSS specificity: Mobile styles should override desktop

## Files Modified

- `themes/boc/assets/css/main.css` - Mobile dropdown styles
- `themes/boc/assets/js/main.js` - Mobile toggle logic

## Summary

The mobile dropdown issue has been fixed with:
1. **Explicit visibility** using `!important` flags
2. **White text** on dark teal background
3. **Proper JavaScript** toggle logic
4. **Debug logging** in console
5. **CSS overrides** for mobile-specific behavior

Build the site and test on a mobile device or using browser DevTools in mobile emulation mode. The dropdowns should now be clearly visible with white text on a dark teal background.