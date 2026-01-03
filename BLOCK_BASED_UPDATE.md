# Block-Based Mega Menu Update

## Summary

The mega menu structure has been updated to use a flexible **block-based system** where each column can contain multiple blocks of different types.

## What Changed

### Before: Single Featured Link Per Column
```yaml
columns:
  - featuredLink:
      url: "/page"
      title: "Title"
      description: "Description"
      image: "/image.jpg"
    blocks:
      - subheader: "Links"
        links:
          - text: "Link"
            url: "/link"
```

**Limitation**: Only one featured card allowed per column at the top.

### After: Multiple Blocks Per Column
```yaml
columns:
  - blocks:
      # Block 1: Featured card with image
      - url: "/page"
        title: "Title"
        description: "Description"
        image: "/image.jpg"
      
      # Block 2: Link list
      - subheader: "Links"
        links:
          - text: "Link"
            url: "/link"
      
      # Block 3: Another featured card
      - url: "/page2"
        title: "Title 2"
        description: "Description 2"
      
      # Block 4: Simple links
      - links:
          - text: "Quick Link"
            url: "/quick"
```

**Improvement**: Unlimited blocks of any type in any order.

## Block Types

### 1. Featured Card Block
A clickable card with optional image, title, and description.

**Detection**: Has `url` field

**Structure**:
```yaml
- url: "/destination"           # Required
  title: "Card Title"           # Optional
  description: "Card subtitle"  # Optional
  image: "/images/pic.jpg"      # Optional (360x180px)
```

**Example with image**:
```yaml
- url: "/products/overview"
  title: "Our Products"
  description: "Explore our complete line"
  image: "/images/mega-menu/products.jpg"
```

**Example without image**:
```yaml
- url: "/about"
  title: "About Us"
  description: "Learn about our company"
```

**Example minimal**:
```yaml
- url: "/contact"
  title: "Contact Us"
```

### 2. Link List Block (with subheader)
A group of links organized under a subheader.

**Detection**: Has `subheader` field

**Structure**:
```yaml
- subheader: "Category Name"
  links:
    - text: "Link Text"
      url: "/path"
```

**Example**:
```yaml
- subheader: "Popular Products"
  links:
    - text: "Product A"
      url: "/products/a"
    - text: "Product B"
      url: "/products/b"
```

### 3. Link List Block (without subheader)
A simple list of links without a header.

**Detection**: Has `links` field only

**Structure**:
```yaml
- links:
    - text: "Link Text"
      url: "/path"
```

**Example**:
```yaml
- links:
    - text: "View All"
      url: "/all"
    - text: "Contact Us"
      url: "/contact"
```

## Real-World Examples

### Example 1: Markets Menu (1 Column, Multiple Featured Cards)

```yaml
markets:
  columns:
    - blocks:
        # Featured card 1 with image
        - url: "/markets/overview"
          title: "Market Operations"
          description: "Market activities and data"
          image: "/images/mega-menu/markets.jpg"
        
        # Link list
        - subheader: "Rates & Data"
          links:
            - text: "Exchange Rates"
              url: "/markets/exchange-rates"
            - text: "Interest Rates"
              url: "/markets/interest-rates"
        
        # Featured card 2 without image
        - url: "/markets/liquidity"
          title: "Liquidity Management"
          description: "Tools and facilities"
        
        # Another link list
        - subheader: "Operations"
          links:
            - text: "Market Operations"
              url: "/markets/operations"
```

**Result**: One column with 2 featured cards and 2 link lists.

### Example 2: Bank Notes Menu (3 Columns, Mixed Content)

```yaml
bank-notes:
  columns:
    # Column 1: Featured card + simple links
    - blocks:
        - url: "/bank-notes/current"
          title: "Current Notes"
          image: "/images/mega-menu/bank-notes.jpg"
          description: "Explore Canada's bank notes"
        - links:
            - text: "Polymer Series"
              url: "/bank-notes/polymer"
            - text: "Commemorative Notes"
              url: "/bank-notes/commemorative"
    
    # Column 2: Featured card + link blocks
    - blocks:
        - url: "/bank-notes/security"
          title: "Security & Authentication"
          description: "Verify genuine notes"
        - subheader: "Security Features"
          links:
            - text: "How to Check Notes"
              url: "/bank-notes/security-check"
    
    # Column 3: Two featured cards + links
    - blocks:
        - url: "/bank-notes/history"
          title: "History & Design"
          description: "Stories behind our currency"
        - url: "/bank-notes/museum"
          title: "Currency Museum"
          description: "Historical collection"
          image: "/images/mega-menu/museum.jpg"
        - links:
            - text: "Design Process"
              url: "/bank-notes/design"
```

**Result**: Three columns with various combinations of featured cards and link lists.

## Benefits

✅ **Unlimited Featured Cards** - Add as many clickable cards as needed per column
✅ **Flexible Ordering** - Mix featured cards and link lists in any order
✅ **Cleaner Structure** - Everything is a block, consistent pattern
✅ **Better UX** - Multiple prominent calls-to-action per column
✅ **Easier Maintenance** - Simple, predictable structure

## Migration Guide

### Old Structure → New Structure

**Old**:
```yaml
- featuredLink:
    url: "/page"
    title: "Title"
  blocks:
    - subheader: "Links"
      links:
        - text: "Link"
          url: "/link"
```

**New**:
```yaml
- blocks:
    - url: "/page"        # Featured card (no wrapper needed)
      title: "Title"
    - subheader: "Links"  # Link block (same as before)
      links:
        - text: "Link"
          url: "/link"
```

### Key Changes:
1. Remove `featuredLink:` wrapper
2. Move featured content into `blocks:` array
3. Keep link blocks as-is (they're already blocks)

## Use Cases

### Use Case 1: Service Overview
Show multiple service cards with images:
```yaml
- blocks:
    - url: "/services/consulting"
      title: "Consulting"
      image: "/images/consulting.jpg"
    - url: "/services/training"
      title: "Training"
      image: "/images/training.jpg"
    - url: "/services/support"
      title: "Support"
      image: "/images/support.jpg"
```

### Use Case 2: Alternating Content
Mix featured content with organized links:
```yaml
- blocks:
    - url: "/products/featured"
      title: "Featured Product"
      image: "/images/featured.jpg"
    - subheader: "By Category"
      links:
        - text: "Electronics"
          url: "/cat/electronics"
    - url: "/products/deals"
      title: "Special Deals"
    - subheader: "Quick Links"
      links:
        - text: "View All"
          url: "/all"
```

### Use Case 3: Content-Rich Column
Provide multiple entry points:
```yaml
- blocks:
    - url: "/overview"
      title: "Overview"
      description: "Start here"
      image: "/images/overview.jpg"
    - subheader: "Getting Started"
      links:
        - text: "Tutorial"
          url: "/tutorial"
    - url: "/advanced"
      title: "Advanced Topics"
      description: "For experienced users"
    - subheader: "Resources"
      links:
        - text: "Documentation"
          url: "/docs"
```

## Files Modified

1. **`themes/boc/layouts/_partials/menu.html`**
   - Removed `featuredLink` wrapper logic
   - Added block type detection (url vs subheader vs links)
   - Simplified template to iterate through blocks only

2. **`data/menus.yaml`**
   - Updated all 5 mega menus
   - Converted `featuredLink` to block entries
   - Added examples of multiple featured cards

3. **Documentation**
   - `MEGA_MENU_QUICK_START.md` - Updated with block examples
   - `MEGA_MENU_STRUCTURE.md` - Updated structure documentation
   - `BLOCK_BASED_UPDATE.md` - This file

## Current Status

All 5 mega menus now use block-based structure:

1. **Monetary Policy** (3 columns) - Each with featured card + link blocks
2. **Financial System** (2 columns) - Featured cards + organized links
3. **Markets** (1 column) - **2 featured cards** + 2 link blocks
4. **Bank Notes** (3 columns) - Column 3 has **2 featured cards**
5. **Research** (2 columns) - Column 2 has **2 featured cards**

Total featured card blocks: **14** (up from 11)

## Testing

Verified working:
- ✅ Multiple featured cards in single column
- ✅ Featured cards with and without images
- ✅ Link blocks with and without subheaders
- ✅ Mixed ordering of block types
- ✅ All 5 mega menus render correctly
- ✅ Desktop hover effects work
- ✅ Mobile stacking works
- ✅ Block type detection works

## Next Steps

1. Add more featured cards where appropriate
2. Create 360×180px images for new featured cards
3. Test various combinations of block types
4. Consider adding more block types in future (e.g., video, embed)

## Documentation

See these files for details:
- `MEGA_MENU_QUICK_START.md` - Quick reference with examples
- `MEGA_MENU_STRUCTURE.md` - Complete documentation
- `data/menus.yaml` - Working examples of all patterns