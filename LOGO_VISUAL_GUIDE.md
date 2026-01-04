# Logo Visual Guide - Dark Mode & Mobile Support

## Overview

Visual demonstration of how logos switch based on **screen size** and **theme mode**.

---

## Logo Switching Behavior

### Desktop Light Mode (Default)

```
┌──────────────────────────────────────┐
│  🌞 Light Mode - Desktop (>768px)   │
├──────────────────────────────────────┤
│                                      │
│  ┌────────────────────────┐         │
│  │  [LOGO-FULL-LIGHT.SVG] │  ← Shown│
│  │  Dark text/colors      │         │
│  │  Full brand name       │         │
│  └────────────────────────┘         │
│                                      │
│  [LOGO-FULL-DARK.SVG]     ← Hidden  │
│  [LOGO-MOBILE-LIGHT.SVG]  ← Hidden  │
│  [LOGO-MOBILE-DARK.SVG]   ← Hidden  │
│                                      │
└──────────────────────────────────────┘
```

**Active Logo:** Desktop Light  
**Height:** 150px  
**CSS:** `.site-logo-desktop.site-logo-light { display: block; }`

---

### Desktop Dark Mode

```
┌──────────────────────────────────────┐
│  🌙 Dark Mode - Desktop (>768px)     │
├──────────────────────────────────────┤
│                                      │
│  [LOGO-FULL-LIGHT.SVG]    ← Hidden  │
│                                      │
│  ┌────────────────────────┐         │
│  │  [LOGO-FULL-DARK.SVG]  │  ← Shown│
│  │  Light text/colors     │         │
│  │  Full brand name       │         │
│  └────────────────────────┘         │
│                                      │
│  [LOGO-MOBILE-LIGHT.SVG]  ← Hidden  │
│  [LOGO-MOBILE-DARK.SVG]   ← Hidden  │
│                                      │
└──────────────────────────────────────┘
```

**Active Logo:** Desktop Dark  
**Height:** 150px  
**CSS:** `.site-logo-desktop.site-logo-dark { display: block; }`  
**Selector:** `[data-theme="dark"]`

---

### Mobile Light Mode

```
┌───────────────────────┐
│  🌞 Light - Mobile    │
│     (≤768px)          │
├───────────────────────┤
│                       │
│  [LOGO-FULL-LIGHT]    │ ← Hidden
│  [LOGO-FULL-DARK]     │ ← Hidden
│                       │
│  ┌─────────────┐     │
│  │ [LOGO-ICON] │ ← Shown
│  │ Dark colors │     │
│  │ Compact     │     │
│  └─────────────┘     │
│                       │
│  [LOGO-MOBILE-DARK]   │ ← Hidden
│                       │
└───────────────────────┘
```

**Active Logo:** Mobile Light  
**Height:** 100px (tablet) / 80px (phone)  
**CSS:** `.site-logo-mobile.site-logo-light { display: block; }`  
**Media Query:** `@media (max-width: 768px)`

---

### Mobile Dark Mode

```
┌───────────────────────┐
│  🌙 Dark - Mobile     │
│     (≤768px)          │
├───────────────────────┤
│                       │
│  [LOGO-FULL-LIGHT]    │ ← Hidden
│  [LOGO-FULL-DARK]     │ ← Hidden
│  [LOGO-MOBILE-LIGHT]  │ ← Hidden
│                       │
│  ┌─────────────┐     │
│  │ [LOGO-ICON] │ ← Shown
│  │ Light colors│     │
│  │ Compact     │     │
│  └─────────────┘     │
│                       │
└───────────────────────┘
```

**Active Logo:** Mobile Dark  
**Height:** 100px (tablet) / 80px (phone)  
**CSS:** `.site-logo-mobile.site-logo-dark { display: block; }`  
**Selectors:** `@media (max-width: 768px)` + `[data-theme="dark"]`

---

## State Transition Diagrams

### Theme Toggle on Desktop

```
Desktop Light Mode            Toggle Dark Mode           Desktop Dark Mode
┌─────────────────┐          ───────────────→          ┌─────────────────┐
│ [Dark Logo]     │                                     │ [Light Logo]    │
│  Full width     │          ←───────────────          │  Full width     │
│  150px height   │          Toggle Light Mode         │  150px height   │
└─────────────────┘                                     └─────────────────┘

CSS Changes:
.site-logo-light: display: block → display: none
.site-logo-dark:  display: none  → display: block
```

### Theme Toggle on Mobile

```
Mobile Light Mode             Toggle Dark Mode           Mobile Dark Mode
┌─────────────┐              ───────────────→          ┌─────────────┐
│ [Dark Icon] │                                         │ [Light Icon]│
│  Compact    │              ←───────────────          │  Compact    │
│  100px      │              Toggle Light Mode         │  100px      │
└─────────────┘                                         └─────────────┘

CSS Changes:
.site-logo-light: display: block → display: none
.site-logo-dark:  display: none  → display: block
```

### Screen Resize (Light Mode)

```
Desktop Light                 Resize to Mobile           Mobile Light
┌─────────────────┐          ───────────────→          ┌─────────────┐
│ [Full Logo]     │                                     │ [Icon Logo] │
│  150px height   │          ←───────────────          │  100px      │
└─────────────────┘          Resize to Desktop         └─────────────┘

CSS Changes:
.site-logo-desktop: display: block → display: none
.site-logo-mobile:  display: none  → display: block
```

### Screen Resize (Dark Mode)

```
Desktop Dark                  Resize to Mobile           Mobile Dark
┌─────────────────┐          ───────────────→          ┌─────────────┐
│ [Full Logo]     │                                     │ [Icon Logo] │
│ Light colors    │          ←───────────────          │ Light colors│
│  150px height   │          Resize to Desktop         │  100px      │
└─────────────────┘                                     └─────────────┘

CSS Changes:
.site-logo-desktop: display: block → display: none
.site-logo-mobile:  display: none  → display: block
```

---

## All 4 Logo States

### Complete State Matrix

```
┌─────────────┬──────────────────┬──────────────────┐
│             │   Light Mode     │    Dark Mode     │
├─────────────┼──────────────────┼──────────────────┤
│ DESKTOP     │                  │                  │
│ (>768px)    │ ┌──────────────┐ │ ┌──────────────┐ │
│             │ │ Full Logo    │ │ │ Full Logo    │ │
│             │ │ Dark colors  │ │ │ Light colors │ │
│             │ │ 150px height │ │ │ 150px height │ │
│             │ └──────────────┘ │ └──────────────┘ │
│             │                  │                  │
├─────────────┼──────────────────┼──────────────────┤
│ MOBILE      │                  │                  │
│ (≤768px)    │ ┌──────────┐     │ ┌──────────┐     │
│             │ │ Icon     │     │ │ Icon     │     │
│             │ │ Dark     │     │ │ Light    │     │
│             │ │ 100px    │     │ │ 100px    │     │
│             │ └──────────┘     │ └──────────┘     │
└─────────────┴──────────────────┴──────────────────┘
```

---

## HTML Structure

```html
<div class="site-title">
  <a href="/">
    
    <!-- Logo 1: Desktop Light -->
    <img src="/images/logo-full-light.svg"
         class="site-logo site-logo-desktop site-logo-light"
         alt="Brand Name" />
    
    <!-- Logo 2: Desktop Dark -->
    <img src="/images/logo-full-dark.svg"
         class="site-logo site-logo-desktop site-logo-dark"
         alt="Brand Name" />
    
    <!-- Logo 3: Mobile Light -->
    <img src="/images/logo-mobile-light.svg"
         class="site-logo site-logo-mobile site-logo-light"
         alt="Brand Name" />
    
    <!-- Logo 4: Mobile Dark -->
    <img src="/images/logo-mobile-dark.svg"
         class="site-logo site-logo-mobile site-logo-dark"
         alt="Brand Name" />
    
  </a>
</div>
```

**Key Points:**
- All 4 images are in the DOM
- Only 1 is visible at any time
- CSS controls visibility
- No JavaScript needed

---

## CSS Visibility Rules

### Base Rules (Desktop Light Mode Default)

```css
/* Show desktop by default */
.site-logo-desktop { display: block; }
.site-logo-mobile  { display: none; }

/* Show light mode by default */
.site-logo-light { display: block; }
.site-logo-dark  { display: none; }
```

**Result:** Desktop Light logo visible

---

### Dark Mode Override

```css
[data-theme="dark"] .site-logo-light { display: none; }
[data-theme="dark"] .site-logo-dark  { display: block; }
```

**Result:** Swaps light → dark logos

---

### Mobile Override

```css
@media (max-width: 768px) {
  .site-logo-desktop { display: none; }
  .site-logo-mobile  { display: block; }
}
```

**Result:** Swaps desktop → mobile logos

---

### Combined (Mobile Dark Mode)

```css
/* Mobile media query */
@media (max-width: 768px) {
  .site-logo-desktop { display: none; }
  .site-logo-mobile  { display: block; }
}

/* Dark mode selector */
[data-theme="dark"] .site-logo-light { display: none; }
[data-theme="dark"] .site-logo-dark  { display: block; }
```

**Result:** Mobile Dark logo visible (both conditions met)

---

## Logo Size Progression

### Desktop to Mobile Transition

```
Desktop (>768px)         Tablet (768px)         Mobile (≤450px)
┌──────────────┐        ┌────────────┐         ┌─────────┐
│              │        │            │         │         │
│ LOGO         │   →    │  LOGO      │    →    │  LOGO   │
│ COMPANY      │        │  COMPANY   │         │         │
│              │        │            │         │         │
└──────────────┘        └────────────┘         └─────────┘
   150px height            100px height          80px height
   Full logo              Full/Compact           Icon only
```

---

## Fallback Behavior

### If Mobile Logos Not Specified

```
Configuration:
[params.logo]
  light = '/images/logo-light.svg'
  dark = '/images/logo-dark.svg'
  # No lightMobile or darkMobile specified

Visual Result on Mobile:
┌───────────────────┐
│  Mobile Screen    │
├───────────────────┤
│  ┌─────────────┐ │
│  │ Desktop     │ │ ← Desktop logo used
│  │ Logo        │ │   (scaled to 100px)
│  │ (scaled)    │ │
│  └─────────────┘ │
└───────────────────┘
```

**Hugo Template Fallback:**
```go
{{- $logoLightMobile := site.Params.logo.lightMobile | default $logoLight -}}
{{- $logoDarkMobile := site.Params.logo.darkMobile | default $logoDark -}}
```

---

## Example Logo Designs

### Desktop Full Logos (150px height)

```
Light Mode:
┌────────────────────────────────┐
│  ╔═══╗                         │
│  ║   ║  COMPANY NAME           │
│  ╚═══╝  Tagline here           │
└────────────────────────────────┘
Dark text, full width ~300px

Dark Mode:
┌────────────────────────────────┐
│  ╔═══╗                         │
│  ║   ║  COMPANY NAME           │
│  ╚═══╝  Tagline here           │
└────────────────────────────────┘
Light text, full width ~300px
```

### Mobile Compact Logos (100px height)

```
Light Mode:
┌──────────┐
│  ╔═══╗   │
│  ║   ║   │
│  ╚═══╝   │
└──────────┘
Icon only, ~90px wide

Dark Mode:
┌──────────┐
│  ╔═══╗   │
│  ║   ║   │
│  ╚═══╝   │
└──────────┘
Light icon, ~90px wide
```

---

## Browser DevTools Inspection

### Desktop Light Mode

```
Elements Panel:
<img src="/images/logo-full-light.svg"
     class="site-logo site-logo-desktop site-logo-light"
     style="display: block;">  ← VISIBLE

<img src="/images/logo-full-dark.svg"
     class="site-logo site-logo-desktop site-logo-dark"
     style="display: none;">   ← HIDDEN

<img src="/images/logo-mobile-light.svg"
     class="site-logo site-logo-mobile site-logo-light"
     style="display: none;">   ← HIDDEN

<img src="/images/logo-mobile-dark.svg"
     class="site-logo site-logo-mobile site-logo-dark"
     style="display: none;">   ← HIDDEN
```

### Mobile Dark Mode

```
Elements Panel:
<img src="/images/logo-full-light.svg"
     class="site-logo site-logo-desktop site-logo-light"
     style="display: none;">   ← HIDDEN

<img src="/images/logo-full-dark.svg"
     class="site-logo site-logo-desktop site-logo-dark"
     style="display: none;">   ← HIDDEN

<img src="/images/logo-mobile-light.svg"
     class="site-logo site-logo-mobile site-logo-light"
     style="display: none;">   ← HIDDEN

<img src="/images/logo-mobile-dark.svg"
     class="site-logo site-logo-mobile site-logo-dark"
     style="display: block;">  ← VISIBLE
```

---

## Quick Reference

### Logo Visibility Formula

```
Visible Logo = (Desktop OR Mobile) AND (Light OR Dark)

Examples:
• Desktop + Light  = Desktop Light logo
• Desktop + Dark   = Desktop Dark logo
• Mobile + Light   = Mobile Light logo
• Mobile + Dark    = Mobile Dark logo
```

### CSS Class Combinations

| Desktop/Mobile | Light/Dark | Result |
|----------------|------------|--------|
| `desktop` | `light` | Desktop Light ✓ |
| `desktop` | `dark` | Desktop Dark ✓ |
| `mobile` | `light` | Mobile Light ✓ |
| `mobile` | `dark` | Mobile Dark ✓ |

### Breakpoints

| Breakpoint | Logo Type | Height |
|------------|-----------|--------|
| >768px | Desktop | 150px |
| 451-768px | Mobile | 100px |
| ≤450px | Mobile | 80px |

---

## Summary

✅ **4 logos loaded** - All present in HTML  
✅ **1 logo visible** - CSS controls display  
✅ **Automatic switching** - Based on screen + theme  
✅ **No JavaScript** - Pure CSS implementation  
✅ **Smooth transitions** - No flash or flicker  
✅ **Fallback support** - Mobile optional  

---

**Last Updated:** January 2025  
**Implementation:** Pure CSS with Hugo templating  
**Browser Support:** All modern browsers