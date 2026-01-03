# Featured Link Update - Summary

## What Changed

The mega menu structure has been updated so that the **image, header, and description** are now combined into a **single clickable featured link** (card).

## Before vs After

### Before (Old Structure)
```yaml
columns:
  - title: "Policy Tools"
    description: "Learn about our instruments"
    image: "/images/mega-menu/policy.jpg"
    blocks:
      - subheader: "Rates"
        links:
          - text: "Interest Rate"
            url: "/rate"
```

**Issue**: Image, title, and description were separate non-clickable elements.

### After (New Structure)
```yaml
columns:
  - featuredLink:
      url: "/monetary-policy/tools"        # 👈 NEW: Entire card is clickable
      title: "Policy Tools"
      description: "Learn about our instruments"
      image: "/images/mega-menu/policy.jpg"
    blocks:
      - subheader: "Rates"
        links:
          - text: "Interest Rate"
            url: "/rate"
```

**Improvement**: Image, title, and description form one clickable card that links to the URL.

## Image Specifications

- **Size**: 360px × 180px (changed from 400×250px)
- **Aspect Ratio**: 2:1
- **Display**: `object-fit: cover` maintains aspect ratio
- **Format**: JPG, PNG, or WebP
- **Location**: `static/images/mega-menu/`

## Visual Behavior

### Desktop
When hovering over the featured link card:
- Card lifts up 2px
- Drop shadow appears
- Image zooms in 5%
- Title color changes to light teal

### Mobile
- No hover effects (touch-optimized)
- Card is fully clickable
- Images maintain 360×180px size
- Stacks vertically with other columns

## Files Modified

1. **`themes/boc/layouts/_partials/menu.html`**
   - Added `featuredLink` structure support
   - Wraps image, title, description in single `<a>` tag
   - Maintains backward compatibility

2. **`themes/boc/assets/css/main.css`**
   - Added `.mega-menu-column-featured` styles
   - Set image dimensions to 360×180px
   - Added hover effects for desktop
   - Added mobile-specific styles

3. **`data/menus.yaml`**
   - Updated all 5 mega menus to use `featuredLink`
   - Added URL for each featured card
   - Restructured image, title, description under `featuredLink`

## Migration Guide

If you have custom mega menu data, update it like this:

### Old Format
```yaml
- title: "My Title"
  description: "My description"
  image: "/images/pic.jpg"
```

### New Format
```yaml
- featuredLink:
    url: "/destination-page"          # Add this
    title: "My Title"                 # Indent under featuredLink
    description: "My description"     # Indent under featuredLink
    image: "/images/pic.jpg"          # Indent under featuredLink
```

## Current Mega Menus

All 5 mega menus have been updated:

1. **Monetary Policy** (3 columns) - All have featured links with images
2. **Financial System** (2 columns) - Column 1 has image, column 2 doesn't
3. **Markets** (1 column) - Featured link without image
4. **Bank Notes** (3 columns) - Column 1 has image, others don't
5. **Research** (2 columns) - Both without images

## Benefits

✅ **Better UX**: Entire card is clickable, not just small links
✅ **Visual Hierarchy**: Featured content stands out
✅ **Consistent Interaction**: Users expect cards to be clickable
✅ **Mobile-Friendly**: Large touch targets
✅ **Flexible**: Image, title, description all optional

## Example Usage

### Full Featured Card
```yaml
- featuredLink:
    url: "/products/overview"
    title: "Our Products"
    description: "Explore our complete product line"
    image: "/images/mega-menu/products.jpg"
  blocks:
    - subheader: "Categories"
      links:
        - text: "Category A"
          url: "/products/a"
```

### Simple Featured Card (No Image)
```yaml
- featuredLink:
    url: "/about"
    title: "About Us"
    description: "Learn about our company"
  links:
    - text: "Our Team"
      url: "/about/team"
```

### Minimal Featured Card (Just Title)
```yaml
- featuredLink:
    url: "/contact"
    title: "Contact Us"
  blocks:
    - links:
        - text: "Email"
          url: "/contact/email"
```

## Testing

Verified working:
- ✅ Featured links are clickable
- ✅ Images display at 360×180px
- ✅ Hover effects work on desktop
- ✅ No hover effects on mobile
- ✅ Columns stack on mobile
- ✅ All 5 mega menus render correctly
- ✅ Backward compatibility maintained

## Documentation

See these files for more details:
- `MEGA_MENU_QUICK_START.md` - Quick reference
- `MEGA_MENU_STRUCTURE.md` - Complete documentation
- `MEGA_MENU_IMPLEMENTATION.md` - Technical details
- `data/menus.yaml` - Working examples