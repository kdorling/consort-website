# Logo Dark Mode & Mobile Support Guide

## Overview

The theme now supports **different logo images** for:
1. **Light mode** vs **Dark mode**
2. **Desktop** vs **Mobile** screens

This allows you to optimize logo visibility and branding across different contexts.

---

## Features

✅ **Dark Mode Logos** - Separate logos for light and dark themes  
✅ **Mobile Logos** - Different logos for phone screens  
✅ **Automatic Switching** - CSS handles all visibility logic  
✅ **Fallback Support** - Mobile logos optional (falls back to desktop)  
✅ **No JavaScript** - Pure CSS implementation  

---

## Configuration

### Hugo Config (`hugo.toml`)

```toml
[params.logo]
  # Desktop logos (required)
  light = '/images/consort-full-light.svg'
  dark = '/images/consort-full-dark.svg'

  # Mobile logos (optional - falls back to desktop if not specified)
  lightMobile = '/images/consort-mobile-light.svg'
  darkMobile = '/images/consort-mobile-dark.svg'
```

---

## Logo Types Explained

### 1. Desktop Light Mode (`logo.light`)
- **Used on**: Desktop/tablet screens (> 768px) in light mode
- **Recommended**: Dark logo on transparent background
- **Example**: Black text logo with brand colors

### 2. Desktop Dark Mode (`logo.dark`)
- **Used on**: Desktop/tablet screens (> 768px) in dark mode
- **Recommended**: Light logo on transparent background
- **Example**: White/light text logo with brand colors

### 3. Mobile Light Mode (`logo.lightMobile`)
- **Used on**: Mobile screens (≤ 768px) in light mode
- **Recommended**: Compact version of desktop light logo
- **Falls back to**: `logo.light` if not specified
- **Example**: Icon-only logo or abbreviated version

### 4. Mobile Dark Mode (`logo.darkMobile`)
- **Used on**: Mobile screens (≤ 768px) in dark mode
- **Recommended**: Compact version of desktop dark logo
- **Falls back to**: `logo.dark` if not specified
- **Example**: Light icon-only logo or abbreviated version

---

## Logo Sizes

### Desktop
- **Height**: 150px (default)
- **Width**: Auto (maintains aspect ratio)
- **Recommended**: Full logo with text

### Mobile (768px and below)
- **Height**: 100px
- **Width**: Auto (maintains aspect ratio)
- **Recommended**: Compact logo or icon only

### Small Mobile (450px and below)
- **Height**: 80px
- **Width**: Auto (maintains aspect ratio)
- **Recommended**: Minimal logo or icon

---

## How It Works

### HTML Structure

The header template now renders **4 logo images**:

```html
<a href="/">
  <!-- Desktop logos -->
  <img src="/images/consort-full-light.svg" 
       class="site-logo site-logo-desktop site-logo-light" />
  <img src="/images/consort-full-dark.svg" 
       class="site-logo site-logo-desktop site-logo-dark" />

  <!-- Mobile logos -->
  <img src="/images/consort-mobile-light.svg" 
       class="site-logo site-logo-mobile site-logo-light" />
  <img src="/images/consort-mobile-dark.svg" 
       class="site-logo site-logo-mobile site-logo-dark" />
</a>
```

### CSS Classes

| Class | Purpose |
|-------|---------|
| `.site-logo` | Base styles (size, transition) |
| `.site-logo-desktop` | Shows on screens > 768px |
| `.site-logo-mobile` | Shows on screens ≤ 768px |
| `.site-logo-light` | Shows in light mode |
| `.site-logo-dark` | Shows in dark mode |

### Visibility Logic

```css
/* Default: Desktop Light Mode */
.site-logo-desktop.site-logo-light {
  display: block;  /* Visible */
}

/* Other combinations hidden by default */
.site-logo-desktop.site-logo-dark,
.site-logo-mobile { 
  display: none;
}

/* Dark mode: Show dark logos */
[data-theme="dark"] .site-logo-light {
  display: none;
}
[data-theme="dark"] .site-logo-dark {
  display: block;
}

/* Mobile: Show mobile logos */
@media (max-width: 768px) {
  .site-logo-desktop {
    display: none;
  }
  .site-logo-mobile {
    display: block;
  }
}
```

---

## Logo Combinations

At any given time, only **ONE** logo is visible:

| Screen Size | Theme Mode | Visible Logo |
|-------------|------------|--------------|
| Desktop (>768px) | Light | Desktop Light |
| Desktop (>768px) | Dark | Desktop Dark |
| Mobile (≤768px) | Light | Mobile Light |
| Mobile (≤768px) | Dark | Mobile Dark |

---

## Setup Steps

### Step 1: Prepare Your Logo Images

Create 4 logo variations (or minimum 2 if not using mobile-specific logos):

1. **Desktop Light**: `consort-full-light.svg`
2. **Desktop Dark**: `consort-full-dark.svg`
3. **Mobile Light**: `consort-mobile-light.svg` (optional)
4. **Mobile Dark**: `consort-mobile-dark.svg` (optional)

### Step 2: Add Images to Project

Place logo files in `static/images/`:

```
static/
└── images/
    ├── consort-full-light.svg
    ├── consort-full-dark.svg
    ├── consort-mobile-light.svg
    └── consort-mobile-dark.svg
```

### Step 3: Configure Hugo

Edit `hugo.toml`:

```toml
[params.logo]
  light = '/images/consort-full-light.svg'
  dark = '/images/consort-full-dark.svg'
  lightMobile = '/images/consort-mobile-light.svg'
  darkMobile = '/images/consort-mobile-dark.svg'
```

### Step 4: Rebuild Site

```bash
hugo --quiet
```

---

## Logo Design Recommendations

### Desktop Logos

**Light Mode (Desktop):**
- Dark text on transparent background
- Full company name and tagline
- Rich colors that work on white/light backgrounds
- Optimal width: 200-400px

**Dark Mode (Desktop):**
- Light/white text on transparent background
- Same layout as light mode
- Adjust colors for dark background visibility
- Consider adding glow or outline for contrast

### Mobile Logos

**Light Mode (Mobile):**
- Simplified icon or abbreviated text
- Dark on transparent
- Clear at small sizes (80-100px height)
- Optimal width: 80-150px

**Dark Mode (Mobile):**
- Simplified icon or abbreviated text
- Light on transparent
- Maintains brand recognition
- Same dimensions as light mobile

---

## File Format Recommendations

### SVG (Recommended)
✅ Scales perfectly at any size  
✅ Small file size  
✅ Sharp on retina displays  
✅ Easy to modify colors  

### PNG (Alternative)
- Use 2x or 3x resolution for retina
- Export at 300-450px height for desktop
- Export at 150-300px height for mobile
- Transparent background

### Avoid
❌ JPEG (no transparency)  
❌ Low-resolution images  
❌ Raster formats for logos if possible  

---

## Testing Checklist

### Desktop Testing
- [ ] Light mode logo appears correctly (>768px)
- [ ] Dark mode logo appears correctly (>768px)
- [ ] Toggle dark mode - logo switches
- [ ] Logo height is 150px
- [ ] Logo is sharp and clear
- [ ] No flash when switching themes

### Mobile Testing
- [ ] Mobile light logo appears (≤768px)
- [ ] Mobile dark logo appears (≤768px)
- [ ] Toggle dark mode - logo switches
- [ ] Logo height is 100px (tablet) / 80px (phone)
- [ ] Logo fits in header properly
- [ ] No overlap with buttons

### Responsive Testing
- [ ] Resize from desktop to mobile - logo switches
- [ ] Resize from mobile to desktop - logo switches
- [ ] No layout breaks during transition
- [ ] All 4 logo combinations render correctly

---

## Fallback Behavior

### If Mobile Logos Not Specified

The system gracefully falls back:

```toml
[params.logo]
  light = '/images/logo-light.svg'
  dark = '/images/logo-dark.svg'
  # lightMobile not specified - uses light
  # darkMobile not specified - uses dark
```

Result:
- Mobile light mode → Uses `logo.light`
- Mobile dark mode → Uses `logo.dark`

### If Dark Logo Not Specified

```toml
[params.logo]
  light = '/images/logo.svg'
  # dark not specified - uses light
```

Result:
- Dark mode will show light logo
- Not ideal, but functional

---

## Common Use Cases

### Case 1: Simple Setup (2 Logos)

Just light and dark desktop logos:

```toml
[params.logo]
  light = '/images/logo-light.svg'
  dark = '/images/logo-dark.svg'
```

- Mobile screens use same logos (scaled down)
- Minimal configuration
- Good for simple logos

### Case 2: Mobile-Optimized (4 Logos)

Full logo suite:

```toml
[params.logo]
  light = '/images/logo-full-light.svg'
  dark = '/images/logo-full-dark.svg'
  lightMobile = '/images/logo-icon-light.svg'
  darkMobile = '/images/logo-icon-dark.svg'
```

- Desktop shows full logo with text
- Mobile shows icon only
- Optimal branding across all devices
- Recommended for complex logos

### Case 3: Light Mode Only (1 Logo)

No dark mode support:

```toml
[params.logo]
  light = '/images/logo.svg'
```

- Uses same logo everywhere
- Dark mode shows light logo (may be hard to see)
- Not recommended if dark mode is enabled

---

## Troubleshooting

### Issue: Logo not changing in dark mode
**Check:**
- Theme toggle is working (`[data-theme="dark"]` applied to `<html>`)
- Dark logo path is correct in `hugo.toml`
- CSS for `.site-logo-dark` is present
- Hugo has been rebuilt

### Issue: Mobile logo not appearing
**Check:**
- Screen width is ≤768px
- Mobile logo path is specified or falls back correctly
- CSS media query is active
- Browser cache cleared

### Issue: Multiple logos visible at once
**Check:**
- CSS is compiled correctly
- No conflicting custom CSS
- Logo classes are correct in HTML
- Rebuild Hugo and clear cache

### Issue: Logo too large/small
**Adjust in CSS:**
```css
/* Desktop */
.site-logo {
  height: 150px;  /* Adjust this */
}

/* Mobile */
@media (max-width: 768px) {
  .site-logo {
    height: 100px;  /* Adjust this */
  }
}
```

### Issue: Logo appears blurry on retina screens
**Solution:**
- Use SVG format (recommended)
- Or export PNG at 2-3x the display size

---

## Advanced Customization

### Different Heights for Each Logo Type

```css
/* Desktop light - tallest */
.site-logo-desktop.site-logo-light {
  height: 160px;
}

/* Desktop dark - slightly shorter */
.site-logo-desktop.site-logo-dark {
  height: 150px;
}

/* Mobile - compact */
.site-logo-mobile {
  height: 90px;
}
```

### Add Logo Fade Transition

Already included in base CSS:

```css
.site-logo {
  transition: opacity 0.3s ease;
}
```

### Logo Hover Effect

```css
.site-logo:hover {
  opacity: 0.9;
  transform: scale(1.05);
  transition: all 0.3s ease;
}
```

---

## Files Modified

### Configuration
- `hugo.toml` - Added `[params.logo]` section

### Templates
- `themes/boc/layouts/_partials/header.html` - Updated logo rendering

### Styles
- `themes/boc/assets/css/header.css` - Added logo visibility CSS
- `themes/boc/assets/css/responsive.css` - Added mobile logo switching

---

## Browser Support

| Browser | Support |
|---------|---------|
| Chrome | ✅ Full |
| Firefox | ✅ Full |
| Safari | ✅ Full |
| Edge | ✅ Full |
| Mobile Safari | ✅ Full |
| Mobile Chrome | ✅ Full |

CSS features used:
- `display: none/block`
- Media queries
- Attribute selectors
- Multiple class selectors

All widely supported.

---

## Performance Notes

- **4 images loaded**: All 4 logos load on page load
- **CSS handles visibility**: Only 1 shown at a time
- **Minimal overhead**: Logos are cached by browser
- **Recommendation**: Use SVG for smallest file size
- **Optimization**: Logos load in parallel with other assets

---

## Example Logo Filenames

### Descriptive Naming
```
logo-full-light.svg       (Desktop light mode)
logo-full-dark.svg        (Desktop dark mode)
logo-icon-light.svg       (Mobile light mode)
logo-icon-dark.svg        (Mobile dark mode)
```

### Company-Specific Naming
```
consort-full-light.svg
consort-full-dark.svg
consort-mobile-light.svg
consort-mobile-dark.svg
```

### Alternative Naming
```
brand-desktop-light.svg
brand-desktop-dark.svg
brand-mobile-light.svg
brand-mobile-dark.svg
```

Choose a naming convention and stick with it!

---

## Summary

The logo system now supports:

1. ✅ **4 logo variations** (desktop/mobile × light/dark)
2. ✅ **Automatic switching** based on screen size and theme
3. ✅ **Fallback support** if mobile logos not provided
4. ✅ **Easy configuration** via `hugo.toml`
5. ✅ **No JavaScript required**
6. ✅ **Smooth transitions** between states

**Next Steps:**
1. Create your logo variations
2. Add to `static/images/`
3. Configure in `hugo.toml`
4. Rebuild with `hugo`
5. Test on desktop and mobile in both light/dark modes

---

**Last Updated:** January 2025  
**Status:** ✅ Production Ready  
**Implementation:** Pure CSS with Hugo templating