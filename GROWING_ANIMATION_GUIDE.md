# Mega Menu Growing Animation Guide

## Overview

The mega menu now features a **growing animation** that makes the dropdown appear to expand/scale downward from the navigation bar, creating a smooth, professional reveal effect.

## What Changed

### From: Sliding Animation
- Menu slid down from 20px above
- Used `translateY(-20px)` → `translateY(0)`
- Gave impression of menu dropping down

### To: Growing Animation
- Menu scales from 0% to 100% height
- Uses `scaleY(0)` → `scaleY(1)`
- Gives impression of menu growing/expanding outward
- Grows from the navigation bar downward

## Technical Implementation

### CSS Changes

**File:** `themes/boc/assets/css/main.css` (Lines 285-321)

```css
/* Hidden State */
nav ul ul {
    visibility: hidden;
    opacity: 0;
    transform: scaleY(0);           /* ← Scaled to 0% height */
    transform-origin: top;          /* ← Grows from top edge */
    transition:
        opacity 0.35s ease-out,
        transform 0.35s ease-out,
        visibility 0s linear 0.35s;
    pointer-events: none;
}

/* Open State */
nav ul li.dropdown-open > ul {
    visibility: visible;
    opacity: 1;
    transform: scaleY(1);           /* ← Scaled to 100% height */
    transition:
        opacity 0.35s ease-out,
        transform 0.35s ease-out,
        visibility 0s linear 0s;
    pointer-events: auto;
}
```

### Key Properties

| Property | Closed State | Open State | Purpose |
|----------|--------------|------------|---------|
| `transform` | `scaleY(0)` | `scaleY(1)` | Scales height 0% → 100% |
| `transform-origin` | `top` | `top` | Sets pivot point at top edge |
| `opacity` | `0` | `1` | Fades in while growing |
| `visibility` | `hidden` | `visible` | Controls actual visibility |

## How It Works

### Transform Origin

```css
transform-origin: top;
```

This is crucial! It sets the **pivot point** at the top of the menu:
- Menu grows **downward** from the navigation bar
- Top edge stays fixed (attached to nav bar)
- Bottom edge expands downward
- Creates natural "curtain opening" effect

### Scale Transform

```css
/* Closed */
transform: scaleY(0);   /* 0% of original height = invisible */

/* Open */
transform: scaleY(1);   /* 100% of original height = full size */
```

**scaleY(0.5)** would be 50% height, **scaleY(2)** would be 200% height, etc.

## Visual Effect

### Animation Timeline (0.35 seconds)

```
Time 0ms (Closed):
┌─────────────────────┐
│  Navigation Bar     │
└─────────────────────┘
(Menu invisible, scaleY(0))


Time 100ms:
┌─────────────────────┐
│  Navigation Bar     │
├─────────────────────┤
│  ▓▓▓ Growing...     │  ← 30% height
│                     │
└─────────────────────┘


Time 200ms:
┌─────────────────────┐
│  Navigation Bar     │
├─────────────────────┤
│  ▓▓▓▓▓▓▓            │  ← 60% height
│  Menu Content       │
│  Becoming visible   │
└─────────────────────┘


Time 350ms (Open):
┌─────────────────────┐
│  Navigation Bar     │
├─────────────────────┤
│  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │  ← 100% height
│  Fully Visible      │
│  All Content        │
│  Interactive        │
└─────────────────────┘
```

### What Users See

1. **Click menu item**
2. Menu appears to **grow** from the navigation bar
3. Content **expands** downward smoothly
4. Simultaneously **fades in** (opacity)
5. Reaches full size in 0.35 seconds
6. Clean, professional reveal

## Comparison: Slide vs Grow

### Slide Animation (Previous)
- ✓ Menu moved downward
- ✓ Content visible throughout
- ✓ Simple vertical motion
- ○ Less dramatic reveal

### Grow Animation (Current)
- ✓ Menu scales from top
- ✓ Content reveals progressively
- ✓ More dynamic appearance
- ✓ Feels more "attached" to nav bar
- ✓ Modern, polished effect

## Testing

### Quick Visual Test

1. Open site (desktop, width > 768px)
2. Click "Monetary Policy" or "Markets"
3. **Look for:**
   - Menu appears to **expand/grow** from nav bar
   - Top edge stays **fixed** to navigation
   - Bottom edge **extends** downward
   - Content **scales** into view
   - Smooth **fade-in** effect

### Browser Console Test

```javascript
// Test the animation
const menu = document.querySelector('.has-dropdown');
menu.classList.add('dropdown-open');
setTimeout(() => menu.classList.remove('dropdown-open'), 2000);
```

Watch the menu grow from 0 to full height.

### Inspect Animation

```javascript
// Check computed styles
const dropdown = document.querySelector('nav ul ul');
const styles = getComputedStyle(dropdown);

console.log('Transform:', styles.transform);
// Closed: matrix(1, 0, 0, 0, 0, 0) ← scaleY(0)
// Open: matrix(1, 0, 0, 1, 0, 0) ← scaleY(1)

console.log('Transform Origin:', styles.transformOrigin);
// Should be: "50% 0px" or similar (top center)
```

## Performance

### GPU Acceleration

Both `transform` and `opacity` are GPU-accelerated:
- ✅ Smooth 60 FPS animation
- ✅ No layout recalculation
- ✅ No paint operations (except for opacity)
- ✅ Composite layer handled by GPU

### Why ScaleY Performs Well

- Browser creates separate composite layer
- GPU handles scaling calculations
- Main thread remains responsive
- Same performance as translateY

## Browser Support

| Browser | ScaleY | Transform-Origin | Support |
|---------|--------|------------------|---------|
| Chrome 90+ | ✅ | ✅ | Full support |
| Firefox 88+ | ✅ | ✅ | Full support |
| Safari 14+ | ✅ | ✅ | Full support |
| Edge 90+ | ✅ | ✅ | Full support |
| IE 11 | ✅ | ✅ | Full support |

**Result:** Works in all modern browsers + IE11.

## Mobile Behavior

Animations remain **disabled on mobile** (width ≤ 768px):

```css
@media (max-width: 768px) {
    nav ul ul {
        display: none;  /* Takes no space when closed */
        transform: none !important;
        opacity: 1 !important;
        transition: none !important;
    }
    
    nav ul li.mobile-open > ul,
    nav ul li.dropdown-open > ul {
        display: block !important;  /* Instant reveal when opened */
    }
}
```

**Key Mobile Differences:**
- Uses `display: none/block` instead of `visibility: hidden/visible`
- Takes **zero space** when closed (no gaps in navigation)
- **Instant toggle** (no animation delay)
- Better performance for mobile devices

## Customization Options

### Adjust Speed

```css
nav ul ul {
    transition:
        opacity 0.25s ease-out,    /* ← Faster: 0.25s */
        transform 0.25s ease-out,
        visibility 0s linear 0.25s;
}
```

### Change Easing

```css
/* Bouncy effect */
transition: transform 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);

/* Sharp snap */
transition: transform 0.2s ease-in;

/* Linear growth */
transition: transform 0.35s linear;
```

### Different Origin Points

```css
/* Grow from center */
transform-origin: center;

/* Grow from bottom (unusual) */
transform-origin: bottom;

/* Grow from specific point */
transform-origin: 50% 20px;
```

### Combined Effects

```css
/* Grow AND slide */
transform: scaleY(0) translateY(-10px);
/* to */
transform: scaleY(1) translateY(0);

/* Grow AND rotate (wild!) */
transform: scaleY(0) rotateX(90deg);
/* to */
transform: scaleY(1) rotateX(0deg);
```

## Accessibility

### Screen Readers

- Animation is purely visual
- Screen readers ignore transforms
- Content remains accessible
- `aria-expanded` should be used (already implemented)

### Motion Sensitivity

Consider adding for users with motion sensitivity:

```css
@media (prefers-reduced-motion: reduce) {
    nav ul ul {
        transition-duration: 0.01ms !important;
        transform: scaleY(1) !important;
    }
}
```

## Troubleshooting

### Menu Appears Squished

**Problem:** Content looks compressed during animation

**Cause:** `scaleY` actually scales the content

**Solution:** This is normal behavior. Content scales with container.

### Menu Grows from Wrong Point

**Problem:** Menu grows from center or bottom

**Solution:** Ensure `transform-origin: top` is set

```css
nav ul ul {
    transform-origin: top;  /* ← Must be "top" */
}
```

### Animation Too Slow/Fast

Adjust duration:

```css
transition: opacity 0.35s ease-out, transform 0.35s ease-out, ...;
/*                   ↑ Change this value                      */
```

### Content Blurry During Animation

**Cause:** GPU sub-pixel rendering during scale

**Solutions:**
1. Usually resolves at end of animation
2. Can add: `backface-visibility: hidden;`
3. Or: `will-change: transform;`

## Advanced: Staggered Column Animation

Make columns grow sequentially:

```css
.mega-menu-column:nth-child(1) {
    transition-delay: 0s;
}

.mega-menu-column:nth-child(2) {
    transition-delay: 0.05s;
}

.mega-menu-column:nth-child(3) {
    transition-delay: 0.1s;
}
```

## Summary

**Effect:** Menu grows from 0 to 100% height, anchored at top

**Technical:**
- `transform: scaleY(0)` → `scaleY(1)`
- `transform-origin: top`
- Duration: 0.35s
- Easing: ease-out

**Benefits:**
- ✅ Smooth, modern appearance
- ✅ Professional "expanding" effect
- ✅ GPU-accelerated performance
- ✅ Works across all browsers
- ✅ Feels anchored to navigation bar

**User Experience:**
- More dramatic than sliding
- Clear connection to nav bar
- Progressive content reveal
- Polished, contemporary feel

The growing animation creates a sleek, modern dropdown effect that feels both smooth and intentional!