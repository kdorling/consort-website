# Mega Menu Animation - Quick Test Card

## ⚡ 60-Second Test

### 1. Open Your Site
```bash
# If using Hugo server:
cd test
hugo server

# Then open: http://localhost:1313
```

### 2. Click a Menu Item
- Click "Monetary Policy" or "Markets" or "Bank Notes"
- **Expected**: Menu should **grow/expand** downward smoothly (takes ~0.35 seconds)
- **Expected**: Menu should fade in while growing from the navigation bar
- Click again or click outside to close
- **Expected**: Menu should shrink back up and fade out

### 3. Did You See Animation?

#### ✅ YES - Animation Working!
You should see:
- Smooth growing/scaling effect from top
- Menu expands downward from navigation bar
- Gradual fade-in effect
- Natural deceleration at the end (ease-out)
- No jumping or flickering

**Success!** The animation is working correctly.

#### ❌ NO - Animation Not Working

Run this quick fix:

```bash
# 1. Hard refresh browser
# Windows/Linux: Ctrl + Shift + R
# Mac: Cmd + Shift + R

# 2. Or rebuild Hugo
cd test
hugo --gc
```

Still not working? Continue to "Debug Steps" below.

---

## 🔍 Debug Steps

### Step 1: Check Browser Console
1. Press `F12` to open DevTools
2. Go to **Console** tab
3. Look for any red error messages
4. If you see errors, note them down

### Step 2: Run Debug Script
Copy this into the console:

```javascript
const dropdown = document.querySelector('nav ul ul');
if (dropdown) {
    const s = getComputedStyle(dropdown);
    console.log('Visibility:', s.visibility);
    console.log('Opacity:', s.opacity);
    console.log('Transform:', s.transform);
    console.log('Transition:', s.transition);
    console.log(s.transition.includes('opacity') ? '✅ OK' : '❌ Problem');
} else {
    console.log('❌ Dropdown not found');
}
```

**Good output:**
```
Visibility: hidden
Opacity: 0
Transform: matrix(1, 0, 0, 0, 0, 0)
Transition: opacity 0.35s ease-out, transform 0.35s ease-out, ...
✅ OK
```

**Bad output:**
```
❌ Problem
```

### Step 3: Test Animation Manually
Run this in console:

```javascript
const menu = document.querySelector('.has-dropdown');
menu.classList.add('dropdown-open');
setTimeout(() => menu.classList.remove('dropdown-open'), 2000);
```

Watch for smooth growing/expanding animation from the navigation bar.

### Step 4: Check Window Width
```javascript
console.log('Width:', window.innerWidth, 'px');
```

**Important:** Animations only work on desktop (width > 768px)
- If width ≤ 768px, animations are disabled (by design)
- Resize window wider and test again

---

## 🛠️ Common Fixes

### Fix 1: Clear Cache
```bash
# Hard refresh (most common fix)
Ctrl + Shift + R   # Windows/Linux
Cmd + Shift + R    # Mac
```

### Fix 2: Rebuild Hugo
```bash
cd test
hugo --gc
# Restart browser after rebuild
```

### Fix 3: Check CSS File
Look for this in `themes/boc/assets/css/main.css` around line 286:

```css
nav ul ul {
    visibility: hidden;  /* ← Should be visibility, NOT display */
    opacity: 0;
    transform: scaleY(0);  /* ← Should be scaleY(0) for growing effect */
    transform-origin: top;
    transition: opacity 0.35s ease-out, transform 0.35s ease-out, ...;
}
```

If it says `display: none;`, that's the problem!

### Fix 4: Browser Compatibility
Test in different browser:
- ✅ Chrome/Edge (best)
- ✅ Firefox
- ✅ Safari
- ⚠️ Update to latest version

---

## 📱 Mobile Note

**Animations are intentionally disabled on mobile (<768px width)**

Test on mobile:
1. Resize browser to < 768px
2. Click hamburger menu
3. Click menu items
4. **Expected**: Instant display (no animation) ← This is correct!

---

## ✅ Success Checklist

- [ ] Window width > 768px (desktop mode)
- [ ] Menu grows/expands downward when clicked
- [ ] Menu appears anchored to navigation bar
- [ ] Animation takes ~0.35 seconds
- [ ] Smooth fade-in effect
- [ ] Menu shrinks back when closed
- [ ] No console errors
- [ ] Works on multiple menu items
- [ ] Clicking outside closes menu

All checked? **Animation is working!** 🎉

---

## 🎨 Customization

Want to adjust the animation? Edit `themes/boc/assets/css/main.css`:

```css
nav ul ul {
    transform: scaleY(0);          /* Growing effect: 0 = collapsed */
    transform-origin: top;         /* Grows from: top, center, or bottom */
    transition: 
        opacity 0.35s ease-out,    /* Speed: try 0.25s or 0.5s */
        transform 0.35s ease-out,  /* Try cubic-bezier for bouncy effect */
        visibility 0s linear 0.35s;
}
```

Then rebuild:
```bash
cd test
hugo
```

---

## 📞 Still Not Working?

1. **Check these files exist:**
   - `themes/boc/assets/css/main.css`
   - `themes/boc/assets/js/main.js`
   - `public/css/main.css`

2. **Verify Hugo version:**
   ```bash
   hugo version
   # Should be 0.80 or higher
   ```

3. **Try incognito/private mode:**
   - Rules out extension conflicts
   - Fresh browser state

4. **Check for JavaScript errors:**
   - Open console (F12)
   - Look for red error messages
   - Fix any errors shown

5. **Last resort - full clean rebuild:**
   ```bash
   cd test
   rm -rf public
   hugo --gc
   ```

---

## 📚 Documentation

For detailed information:
- `ANIMATION_FIX_EXPLANATION.md` - Technical details
- `ANIMATION_TEST_GUIDE.md` - Comprehensive testing
- `debug-animation.js` - Full debug script

---

## Summary

**Expected Behavior:**
- Desktop: Smooth growing/expanding animation (0.35s)
- Mobile: Instant display (no animation)

**Key Changes:**
- Replaced `display: none` with `visibility: hidden`
- Changed from `translateY()` to `scaleY()` for growing effect
- Added `transform-origin: top` to anchor growth to nav bar

**Quick Test:**
1. Click menu item
2. Watch for smooth growing/expanding effect
3. Menu should appear to grow from the navigation bar downward
4. Success? You're done! 🎉

**Not Working?**
1. Hard refresh (Ctrl+Shift+R)
2. Check width > 768px
3. Run debug script
4. Rebuild Hugo