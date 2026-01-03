# Mega Menu Quick Start Guide

## Block-Based Structure

The mega menu uses a flexible **block-based structure** where each column contains multiple blocks. Each block can be:

1. **Featured Card Block** - A clickable card with image, title, and description
2. **Link List Block** - A group of links with optional subheader

## Basic Structure

```yaml
megaMenus:
  menu-identifier:
    columns:
      - blocks:
          # Featured card block (with image)
          - url: "/destination-page"
            title: "Card Title"
            description: "Brief description"
            image: "/images/mega-menu/pic.jpg"
          
          # Link list block (with subheader)
          - subheader: "Section Name"
            links:
              - text: "Link Text"
                url: "/page"
          
          # Another featured card (without image)
          - url: "/another-page"
            title: "Another Card"
            description: "Another description"
          
          # Link list block (without subheader)
          - links:
              - text: "Link"
                url: "/page"
```

## Block Types

### Type 1: Featured Card Block
A clickable card that can include an image, title, and description.

**Required Fields:**
- `url` - Where clicking the card navigates to

**Optional Fields:**
- `title` - Card header
- `description` - Card subtitle
- `image` - Path to 360×180px image

**Example with everything:**
```yaml
- url: "/products/overview"
  title: "Our Products"
  description: "Explore our complete product line"
  image: "/images/mega-menu/products.jpg"
```

**Example without image:**
```yaml
- url: "/about"
  title: "About Us"
  description: "Learn about our company"
```

**Example with just title:**
```yaml
- url: "/contact"
  title: "Contact Us"
```

### Type 2: Link List Block
A group of links, optionally organized under a subheader.

**With subheader:**
```yaml
- subheader: "Popular Products"
  links:
    - text: "Product A"
      url: "/products/a"
    - text: "Product B"
      url: "/products/b"
```

**Without subheader:**
```yaml
- links:
    - text: "Quick Link"
      url: "/page"
    - text: "Another Link"
      url: "/other"
```

## Image Requirements

- **Dimensions**: 360px × 180px
- **Aspect Ratio**: 2:1
- **Format**: JPG, PNG, or WebP
- **Location**: `static/images/mega-menu/`
- **Reference**: `/images/mega-menu/filename.jpg`

## Complete Examples

### Example 1: Mixed Content in One Column

```yaml
megaMenus:
  products:
    columns:
      - blocks:
          # Featured card with image
          - url: "/products/featured"
            title: "Featured Products"
            description: "Check out our latest offerings"
            image: "/images/mega-menu/featured.jpg"
          
          # Link list with subheader
          - subheader: "By Category"
            links:
              - text: "Electronics"
                url: "/products/electronics"
              - text: "Furniture"
                url: "/products/furniture"
          
          # Another featured card without image
          - url: "/products/deals"
            title: "Special Deals"
            description: "Limited time offers"
          
          # Simple links
          - links:
              - text: "View All Products"
                url: "/products/all"
```

### Example 2: Three Columns with Different Content

```yaml
megaMenus:
  services:
    columns:
      # Column 1: Image-heavy
      - blocks:
          - url: "/services/consulting"
            title: "Consulting Services"
            description: "Expert guidance for your business"
            image: "/images/mega-menu/consulting.jpg"
          - url: "/services/training"
            title: "Training Programs"
            description: "Upskill your team"
            image: "/images/mega-menu/training.jpg"
      
      # Column 2: Mixed content
      - blocks:
          - url: "/services/support"
            title: "24/7 Support"
            description: "We're here to help"
          - subheader: "Support Channels"
            links:
              - text: "Live Chat"
                url: "/support/chat"
              - text: "Phone"
                url: "/support/phone"
              - text: "Email"
                url: "/support/email"
      
      # Column 3: Link-heavy
      - blocks:
          - subheader: "Resources"
            links:
              - text: "Documentation"
                url: "/docs"
              - text: "API Reference"
                url: "/api"
              - text: "Tutorials"
                url: "/tutorials"
          - subheader: "Community"
            links:
              - text: "Forums"
                url: "/community/forums"
              - text: "Events"
                url: "/community/events"
```

## Desktop vs Mobile

### Desktop (>768px)
- Columns side-by-side
- Featured cards have hover effects:
  - Lift up slightly
  - Drop shadow appears
  - Image zooms 5%
  - Title changes color

### Mobile (≤768px)
- Columns stack vertically
- Blocks stack within columns
- No hover effects (touch-optimized)
- Full-width layout

## How Blocks are Detected

The template automatically detects block type:

- **Has `url` field** → Featured card block
- **Has `subheader` field** → Link list with subheader
- **Has `links` field only** → Link list without subheader

## Quick Setup Checklist

1. ☐ Add `identifier` to parent menu in `themes/boc/hugo.toml`
2. ☐ Update child items to use `parent = 'identifier'`
3. ☐ Create entry in `data/menus.yaml` with same identifier
4. ☐ Add `columns` array
5. ☐ Add `blocks` array within each column
6. ☐ Add featured card blocks with `url`, `title`, `description`, `image`
7. ☐ Add link list blocks with `subheader` and `links`
8. ☐ Place 360×180px images in `static/images/mega-menu/`
9. ☐ Build with `hugo` and test

## Common Patterns

### Pattern 1: Featured + Links
```yaml
- blocks:
    - url: "/overview"
      title: "Overview"
      description: "Start here"
      image: "/images/mega-menu/overview.jpg"
    - subheader: "Quick Links"
      links:
        - text: "Link 1"
          url: "/link1"
```

### Pattern 2: Multiple Featured Cards
```yaml
- blocks:
    - url: "/option-1"
      title: "Option 1"
      description: "First choice"
      image: "/images/mega-menu/opt1.jpg"
    - url: "/option-2"
      title: "Option 2"
      description: "Second choice"
      image: "/images/mega-menu/opt2.jpg"
```

### Pattern 3: Multiple Link Groups
```yaml
- blocks:
    - subheader: "Category A"
      links:
        - text: "Item 1"
          url: "/a/1"
    - subheader: "Category B"
      links:
        - text: "Item 2"
          url: "/b/2"
```

## Common Mistakes

❌ **Wrong**: Featured card without `url`
```yaml
- title: "Card"
  description: "No URL"
```
✅ **Right**: Featured card with `url`
```yaml
- url: "/page"
  title: "Card"
  description: "Has URL"
```

❌ **Wrong**: Links not in a block
```yaml
- links:
    text: "Link"
    url: "/page"
```
✅ **Right**: Links in proper structure
```yaml
- links:
    - text: "Link"
      url: "/page"
```

❌ **Wrong**: Mixing old `featuredLink` structure
```yaml
- featuredLink:
    url: "/page"
```
✅ **Right**: Using blocks
```yaml
- blocks:
    - url: "/page"
```

## Need Help?

See full documentation:
- `MEGA_MENU_STRUCTURE.md` - Complete reference
- `MEGA_MENU_IMPLEMENTATION.md` - Technical details
- `data/menus.yaml` - Working examples