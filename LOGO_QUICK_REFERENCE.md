# Logo Configuration - Quick Reference

## 🎯 Overview

Configure different logos for **light/dark modes** and **desktop/mobile screens**.

---

## ⚡ Quick Config

### hugo.toml

```toml
[params.logo]
  # Desktop logos (required)
  light = '/images/logo-light.svg'
  dark = '/images/logo-dark.svg'

  # Mobile logos (optional - falls back to desktop)
  lightMobile = '/images/logo-mobile-light.svg'
  darkMobile = '/images/logo-mobile-dark.svg'
```

---

## 📁 File Structure

```
static/
└── images/
    ├── logo-light.svg          (Desktop light mode)
    ├── logo-dark.svg           (Desktop dark mode)
    ├── logo-mobile-light.svg   (Mobile light mode - optional)
    └── logo-mobile-dark.svg    (Mobile dark mode - optional)
```

---

## 📊 Logo Visibility Matrix

| Screen Size | Theme | Visible Logo |
|-------------|-------|--------------|
| Desktop (>768px) | Light | `logo.light` |
| Desktop (>768px) | Dark | `logo.dark` |
| Mobile (≤768px) | Light | `logo.lightMobile` (or `logo.light`) |
| Mobile (≤768px) | Dark | `logo.darkMobile` (or `logo.dark`) |

---

## 📐 Recommended Sizes

### Desktop
- **Height**: 150px
- **Format**: SVG preferred
- **Style**: Full logo with text

### Mobile (≤768px)
- **Height**: 100px
- **Format**: SVG preferred
- **Style**: Compact/icon version

### Small Mobile (≤450px)
- **Height**: 80px
- **Format**: SVG preferred
- **Style**: Minimal/icon only

---

## 🎨 Design Guidelines

### Light Mode Logos
- Dark colors on transparent background
- High contrast for light backgrounds
- Full brand visibility

### Dark Mode Logos
- Light/white colors on transparent background
- High contrast for dark backgrounds
- Consider glow or outline

### Mobile Logos
- Simplified version of desktop
- Clear at small sizes
- Icon-only or abbreviated text works well

---

## 🔧 Setup Steps

1. **Create logo files** (2 minimum, 4 recommended)
2. **Place in** `static/images/`
3. **Configure** `hugo.toml` with paths
4. **Rebuild**: `hugo --quiet`
5. **Test** on desktop and mobile in both themes

---

## ✅ Testing Checklist

- [ ] Desktop light mode logo appears
- [ ] Desktop dark mode logo appears
- [ ] Mobile light mode logo appears
- [ ] Mobile dark mode logo appears
- [ ] Toggle dark mode - logo switches
- [ ] Resize window - logo switches
- [ ] No multiple logos visible at once
- [ ] Logos are sharp and clear
- [ ] Proper sizing on all screens

---

## 🔄 Fallback Behavior

### Minimal Config (2 logos)
```toml
[params.logo]
  light = '/images/logo-light.svg'
  dark = '/images/logo-dark.svg'
  # Mobile logos not specified → uses desktop logos
```

### Light Mode Only (1 logo)
```toml
[params.logo]
  light = '/images/logo.svg'
  # Dark mode → uses light logo (not recommended)
```

---

## 🐛 Troubleshooting

### Logo not changing in dark mode?
- Check theme toggle working
- Verify dark logo path in config
- Rebuild Hugo
- Clear browser cache

### Mobile logo not showing?
- Confirm screen width ≤768px
- Check mobile logo paths
- Verify fallback to desktop logos

### Multiple logos visible?
- Rebuild Hugo
- Clear browser cache
- Check CSS compiled correctly

---

## 💡 Common Configurations

### Option 1: Full Suite (Recommended)
```toml
[params.logo]
  light = '/images/brand-full-light.svg'
  dark = '/images/brand-full-dark.svg'
  lightMobile = '/images/brand-icon-light.svg'
  darkMobile = '/images/brand-icon-dark.svg'
```
**Best for**: Complex logos with text

### Option 2: Simple Setup
```toml
[params.logo]
  light = '/images/logo-light.svg'
  dark = '/images/logo-dark.svg'
```
**Best for**: Simple logos that scale well

### Option 3: Same Logo, Different Colors
```toml
[params.logo]
  light = '/images/logo-dark.svg'    # Dark on light bg
  dark = '/images/logo-light.svg'    # Light on dark bg
  lightMobile = '/images/icon-dark.svg'
  darkMobile = '/images/icon-light.svg'
```
**Best for**: Icon-based logos

---

## 📝 CSS Classes Reference

| Class | Purpose |
|-------|---------|
| `.site-logo` | Base logo styles |
| `.site-logo-desktop` | Shows on desktop (>768px) |
| `.site-logo-mobile` | Shows on mobile (≤768px) |
| `.site-logo-light` | Shows in light mode |
| `.site-logo-dark` | Shows in dark mode |

---

## 🎯 Key Points

✅ 4 logo images supported (desktop/mobile × light/dark)  
✅ Mobile logos optional (falls back to desktop)  
✅ Pure CSS switching (no JavaScript)  
✅ Smooth transitions between modes  
✅ Only 1 logo visible at any time  
✅ SVG format recommended  

---

## 📚 Full Documentation

See `LOGO_DARK_MODE_MOBILE_GUIDE.md` for complete details.

---

**Status**: ✅ Production Ready  
**Last Updated**: January 2025