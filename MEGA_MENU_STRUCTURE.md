# Mega Menu Structure Documentation

This document explains how to configure and use the three-column mega menu structure.

## Overview

The mega menu system supports flexible, structured dropdown menus with up to three columns. Each column contains **blocks** that can be:

- **Featured Card Block** - A clickable card with optional image, title, and description
- **Link List Block** - Organized groups of links with optional subheaders

You can have multiple blocks of any type within a single column. Columns stack vertically on mobile devices for responsive design.

## Configuration

### Data File Location

Mega menu content is defined in: `data/menus.yaml`

### Structure

```yaml
megaMenus:
  menu-identifier:
    columns:
      - blocks:                             # Array of blocks
          # Featured card block (requires url)
          - url: "/path/to/page"            # Required for featured card
            title: "Card Title"             # Optional
            description: "Brief description" # Optional
            image: "/images/mega-menu/pic.jpg" # Optional (360x180px)
          
          # Link list block with subheader
          - subheader: "Section Title"      # Optional
            links:
              - text: "Link Text"
                url: "/path/to/page"
          
          # Link list block without subheader
          - links:
              - text: "Link Text"
                url: "/path/to/page"
```

### Menu Identifier Matching

The menu identifier in `data/menus.yaml` must match the `identifier` field in `themes/boc/hugo.toml`:

```toml
[[menus.main]]
  name = 'Monetary Policy'
  pageRef = '/monetary-policy'
  identifier = 'monetary-policy'  # This matches the data file key
  weight = 20
```

## Column Layouts

### One Column
Set `cols-1` class automatically when only one column is defined. Max width: 400px.

### Two Columns
Set `cols-2` class automatically when two columns are defined. Max width: 800px.

### Three Columns
Set `cols-3` class automatically when three columns are defined. Max width: 1200px.

## Examples

### Example 1: Three Columns with Mixed Content

```yaml
megaMenus:
  monetary-policy:
    columns:
      # Column 1: Featured card with image + link blocks
      - blocks:
          - url: "/monetary-policy/tools"
            title: "Policy Tools"
            description: "Learn about our monetary policy instruments."
            image: "/images/mega-menu/monetary-policy.jpg"
          - subheader: "Interest Rates"
            links:
              - text: "Policy Interest Rate"
                url: "/monetary-policy/policy-rate"
      
      # Column 2: Featured card without image + link blocks
      - blocks:
          - url: "/monetary-policy/publications"
            title: "Publications"
            description: "Research and policy documents."
          - subheader: "Reports"
            links:
              - text: "Monetary Policy Report"
                url: "/monetary-policy/report"
      
      # Column 3: Featured card + simple links
      - blocks:
          - url: "/monetary-policy/resources"
            title: "Resources"
            description: "Tools and educational materials."
          - links:
              - text: "Inflation Calculator"
                url: "/tools/calculator"
```

### Example 2: Single Column with Multiple Featured Cards

```yaml
megaMenus:
  markets:
    columns:
      - blocks:
          # First featured card with image
          - url: "/markets/overview"
            title: "Market Operations"
            description: "Market activities and data"
            image: "/images/mega-menu/markets.jpg"
          
          # Link list block
          - subheader: "Rates"
            links:
              - text: "Exchange Rates"
                url: "/markets/exchange-rates"
              - text: "Interest Rates"
                url: "/markets/interest-rates"
          
          # Second featured card without image
          - url: "/markets/liquidity"
            title: "Liquidity Management"
            description: "Tools and facilities"
          
          # Another link list
          - subheader: "Operations"
            links:
              - text: "Market Operations"
                url: "/markets/operations"
```

### Example 3: Multiple Featured Cards in One Column

```yaml
megaMenus:
  about:
    columns:
      - blocks:
          # First featured card
          - url: "/about/overview"
            title: "About Us"
            description: "Learn more about the Bank of Canada."
            image: "/images/mega-menu/about.jpg"
          
          # Second featured card
          - url: "/about/history"
            title: "Our History"
            description: "Decades of service to Canada"
            image: "/images/mega-menu/history.jpg"
          
          # Simple links
          - links:
              - text: "Leadership"
                url: "/about/leadership"
              - text: "Careers"
                url: "/about/careers"
```

## Images

### Image Location

Place images in: `static/images/mega-menu/`

They will be accessible at: `/images/mega-menu/filename.jpg`

### Image Specifications

- **Format**: JPG, PNG, or WebP
- **Size**: 360px × 180px (2:1 aspect ratio)
- **Max File Size**: 200KB
- **Loading**: Images use lazy loading automatically
- **Display**: Images use `object-fit: cover` to maintain aspect ratio
- **Hover Effect**: Slight zoom effect on desktop when hovering the featured link

### Image Placeholders

If you don't have images yet, you can:
1. Omit the `image` field entirely
2. Use a placeholder service: `https://via.placeholder.com/360x180`
3. Create simple colored rectangles with text overlays

## Block Detection

The template automatically detects block type:

- **Has `url` field** → Featured card block (clickable card)
- **Has `subheader` field** → Link list with subheader
- **Has `links` field only** → Link list without subheader

## Backward Compatibility

Menus without mega menu data defined in `data/menus.yaml` will render as simple dropdowns using the legacy structure from `hugo.toml`:

```toml
[[menus.main]]
  name = 'Submenu Item'
  parent = 'Parent Menu'
  pageRef = '/path/to/page'
  weight = 1
```

## Mobile Behavior

On mobile devices (≤768px):
- Columns stack vertically
- Background color is slightly lighter than sidebar
- Images maintain aspect ratio
- Touch-friendly link sizes (minimum 44px height)

## CSS Classes

### Main Container
- `.mega-menu-columns` - Grid container for columns
- `.mega-menu-columns.cols-1` - One column layout
- `.mega-menu-columns.cols-2` - Two column layout
- `.mega-menu-columns.cols-3` - Three column layout

### Column Elements
- `.mega-menu-column` - Individual column container

### Block Elements
- `.mega-menu-column-featured` - Featured card block (clickable)
- `.mega-menu-column-image` - Image container (360px × 180px)
- `.mega-menu-column-header` - Featured card title
- `.mega-menu-column-description` - Featured card description
- `.mega-menu-link-block` - Link list block container
- `.mega-menu-link-block-header` - Link list subheader

## Customization

### Colors

Desktop colors (defined in CSS):
- Background: White gradient (#ffffff to #f9f9f9)
- Text: Dark gray (#333333)
- Links: Dark gray, hover to teal
- Border accent: Red (#d32f2f)

Mobile colors:
- Background: Light teal (#005570)
- Text: White
- Hover: Lighter teal (#006a85)

### Spacing

- Column gap: 40px (desktop), 20px (mobile)
- Internal padding: 40px vertical (desktop), 15px (mobile)
- Link spacing: 8px padding, 2px margin
- Featured link: 15px margin-bottom

### Interactions

- **Desktop featured link hover**: Slight upward translation, shadow, and image zoom
- **Mobile featured link**: No hover effects (touch-optimized)

## Accessibility

- All links are keyboard navigable
- ARIA labels on navigation elements
- Focus indicators on all interactive elements
- Semantic HTML structure (h3, h4 for headings)
- Alt text on images (uses column title)

## Testing Checklist

- [ ] Desktop view displays correct number of columns
- [ ] Mobile view stacks columns vertically
- [ ] Images load and display properly
- [ ] All links are clickable and navigate correctly
- [ ] Hover states work on desktop
- [ ] Touch interactions work on mobile
- [ ] Keyboard navigation works (Tab, Enter, Escape)
- [ ] Dropdown opens on click (not hover)
- [ ] Dropdown closes when clicking outside
- [ ] Only one dropdown open at a time