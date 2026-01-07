# Footer Configuration Guide

This guide explains how to customize the footer content in the Bank of Canada inspired theme using the data-driven footer system.

## Overview

The footer can be completely customized through a YAML data file (`data/footer.yaml`), allowing you to control:
- Footer sections and their titles
- Links within each section
- Content blocks (text, contact information, etc.)
- External links (with target="_blank")
- Copyright text
- Additional legal/policy links in the footer bottom

## Quick Start

1. Create or edit `data/footer.yaml` in your Hugo site
2. Define your footer sections and links
3. Hugo will automatically use your configuration
4. If no configuration exists, a default footer is displayed

## Configuration Structure

### Basic Structure

```yaml
sections:
  - title: "Section Title"
    links:
      - text: "Link Text"
        url: "/url"
      - text: "External Link"
        url: "https://example.com"
        external: true

  - title: "Contact Section"
    content:
      - type: "text"
        label: "Address:"
        text: "123 Main St"

bottom:
  copyright: "Copyright {year} {site}. All rights reserved."
  links:
    - text: "Privacy"
      url: "/privacy"
```

## Sections Configuration

### Adding Footer Sections

Each section represents a column in the footer grid.

```yaml
sections:
  - title: "About"
    links:
      - text: "About Us"
        url: "/about"
      - text: "Our Team"
        url: "/team"
      - text: "Contact"
        url: "/contact"

  - title: "Services"
    links:
      - text: "Service 1"
        url: "/services/1"
      - text: "Service 2"
        url: "/services/2"
```

### Section Properties

- **title** (optional): The heading for the footer section
- **links** (optional): Array of links in this section
- **content** (optional): Array of content blocks (text, contact info, etc.)

**Note**: A section can have either `links` or `content`, or both.

### Link Properties

- **text** (required): The link text displayed to users
- **url** (required): The link destination (relative or absolute)
- **external** (optional): Set to `true` for external links (adds `rel="external"` and `target="_blank"`)

### External Links Example

```yaml
sections:
  - title: "Connect"
    links:
      - text: "Facebook"
        url: "https://facebook.com/yourpage"
        external: true
      - text: "Twitter"
        url: "https://twitter.com/yourhandle"
        external: true
      - text: "Email Newsletter"
        url: "/newsletter"
```

## Content Blocks

Content blocks allow you to display formatted text, contact information, or other non-link content in footer sections.

### Text Content Block

```yaml
sections:
  - title: "Quick Contact"
    content:
      - type: "text"
        label: "Village Office Address:"
        text: |
          Box 490 4901 50 Avenue
          Consort, Alberta T0C 1B0
      - type: "text"
        label: "Village Office Phone:"
        text: "+1 (403) 577-3623"
```

### Content Block Properties

- **type** (required): Currently supports `"text"`
- **label** (optional): Bold heading for the content block
- **text** (required): The content to display (supports multi-line with `|`)

### Multi-line Text

Use the pipe character (`|`) for multi-line text:

```yaml
content:
  - type: "text"
    label: "Office Hours:"
    text: |
      Monday - Friday: 8:30 AM - 4:30 PM
      Saturday - Sunday: Closed
```

### Mixing Links and Content

You can combine both links and content in the same section:

```yaml
sections:
  - title: "Contact"
    content:
      - type: "text"
        label: "Phone:"
        text: "+1 (403) 577-3623"
      - type: "text"
        label: "Email:"
        text: "info@example.com"
    links:
      - text: "Contact Form"
        url: "/contact"
      - text: "Directions"
        url: "/directions"
```

## Bottom Footer Configuration

### Copyright Text

Customize the copyright text with dynamic placeholders:

```yaml
bottom:
  copyright: "Copyright {year} {site}. All rights reserved."
```

**Available Placeholders:**
- `{year}` - Replaced with current year (e.g., "2025")
- `{site}` - Replaced with your site title from `hugo.toml`

**Examples:**

```yaml
# Simple copyright
copyright: "© {year} {site}"

# With additional text
copyright: "Copyright {year} {site}. Licensed under CC BY 4.0."

# Custom format
copyright: "{site} | {year} | All Rights Reserved"
```

### Bottom Links

Add legal, privacy, or policy links in the footer bottom:

```yaml
bottom:
  links:
    - text: "Privacy Policy"
      url: "/privacy"
    - text: "Terms of Use"
      url: "/terms"
    - text: "Accessibility"
      url: "/accessibility"
```

These links appear below the copyright text, separated by pipe characters (|).

## Complete Example

Here's a full example configuration:

```yaml
# Footer Configuration for Village of Consort

sections:
  # First Column - About
  - title: "About"
    links:
      - text: "About the Village"
        url: "/about"
      - text: "Mayor and Council"
        url: "/government/mayor-council"
      - text: "Careers"
        url: "/careers"
      - text: "Contact Us"
        url: "/contact"

  # Second Column - Services
  - title: "Services"
    links:
      - text: "Departments"
        url: "/departments"
      - text: "Online Services"
        url: "/online-services"
      - text: "Recreation Programs"
        url: "/departments/recreation"
      - text: "Economic Development"
        url: "/departments/economic-development"

  # Third Column - Resources
  - title: "Resources"
    links:
      - text: "Bylaws & Policies"
        url: "/government/bylaws-policies"
      - text: "Meeting Agendas"
        url: "/government/agendas-minutes"
      - text: "News & Alerts"
        url: "/news"
      - text: "Events Calendar"
        url: "/events"

  # Fourth Column - Quick Contact (with content blocks)
  - title: "Quick Contact"
    content:
      - type: "text"
        label: "Village Office Address:"
        text: |
          Box 490 4901 50 Avenue
          Consort, Alberta T0C 1B0
      - type: "text"
        label: "Village Office Phone:"
        text: "+1 (403) 577-3623"
    links:
      - text: "Contact Form"
        url: "/contact"
      - text: "Directions"
        url: "/directions"

# Bottom Footer
bottom:
  copyright: "Copyright {year} {site}. All rights reserved."
  links:
    - text: "Privacy Policy"
      url: "/privacy"
    - text: "Accessibility"
      url: "/accessibility"
    - text: "Terms of Use"
      url: "/terms"
```

### Contact Information Blocks

Perfect for office hours, addresses, phone numbers:

```yaml
sections:
  - title: "Visit Us"
    content:
      - type: "text"
        label: "Main Office:"
        text: |
          123 Main Street
          Suite 100
          City, State 12345
      - type: "text"
        label: "Hours:"
        text: |
          Mon-Fri: 9:00 AM - 5:00 PM
          Sat-Sun: Closed
      - type: "text"
        label: "Phone:"
        text: "+1 (555) 123-4567"
      - type: "text"
        label: "Email:"
        text: "info@example.com"
```

## Responsive Behavior

The footer automatically adjusts for different screen sizes:

- **Desktop**: 4 columns (or as many sections as you define)
- **Tablet**: 2 columns
- **Mobile**: 1 column (stacked)

This is handled automatically by the CSS grid layout.

## Styling

### Footer Sections

Footer sections use the following CSS classes:
- `.footer-container` - Main container
- `.footer-grid` - Grid layout for sections
- `.footer-section` - Individual section
- `.footer-section h3` - Section headings
- `.footer-section ul` - Link lists
- `.footer-section a` - Links
- `.footer-content` - Content block container
- `.footer-content-block` - Individual content block

### Footer Bottom

- `.footer-bottom` - Bottom copyright area
- Inline navigation for bottom links

All styling supports both light and dark modes automatically.

## Advanced Customization

### Varying Number of Columns

You can have any number of sections (columns):

```yaml
sections:
  - title: "Column 1"
    links: [...]
  - title: "Column 2"
    links: [...]
  # Add as many as needed
```

### Sections Without Titles

Omit the `title` property for a section without a heading:

```yaml
sections:
  - links:
      - text: "Link 1"
        url: "/link1"
      - text: "Link 2"
        url: "/link2"
  - content:
      - type: "text"
        text: "Some information without a title"
```

### Mixed Internal and External Links

```yaml
sections:
  - title: "Resources"
    links:
      - text: "Documentation"
        url: "/docs"
      - text: "GitHub Repository"
        url: "https://github.com/yourrepo"
        external: true
      - text: "Support Forum"
        url: "https://forum.example.com"
        external: true
      - text: "Contact Support"
        url: "/support"
```

## Fallback Behavior

If `data/footer.yaml` doesn't exist or is empty, the theme displays a default footer with:
- About section
- Services section
- Resources section
- Connect section
- Basic copyright text

This ensures your site always has a functional footer.

## Migration from Hardcoded Footer

If you're upgrading from a hardcoded footer:

1. Copy your existing footer links
2. Create `data/footer.yaml`
3. Structure your links in the YAML format
4. Test the site
5. The new footer will replace the hardcoded version

## Tips and Best Practices

### Organization
- Group related links in the same section
- Keep section titles short (1-2 words)
- Aim for 3-5 links per section
- Use 3-4 sections for best layout

### Link Text
- Use clear, descriptive text
- Keep link text short
- Match your site's navigation terminology
- Avoid generic terms like "Click here"

### Content Blocks
- Use labels to identify what each content block represents
- Keep text concise and readable
- Use multi-line formatting for addresses
- Include only essential contact information

### External Links
- Always mark social media links as external
- Use external for third-party services
- Consider security for external links

### Accessibility
- Ensure link text is descriptive
- External links automatically get appropriate attributes
- Footer bottom links include proper ARIA labels

### SEO Considerations
- Link to important pages
- Use descriptive anchor text
- Include sitemap links if applicable
- Keep footer links relevant

## Troubleshooting

### Footer Not Updating
- Ensure `data/footer.yaml` is in the correct location
- Check YAML syntax (use a YAML validator)
- Restart Hugo development server
- Clear browser cache

### Links Not Working
- Verify URLs are correct
- Check for leading slashes on internal links
- Ensure external URLs include `https://`
- Test external links in browser

### Layout Issues
- Check that sections array is properly formatted
- Ensure each section has valid YAML structure
- Verify indentation (use spaces, not tabs)
- Test with minimal configuration first

### Copyright Not Showing
- Check `bottom.copyright` is defined
- Verify placeholders use correct format: `{year}` and `{site}`
- Ensure site title is set in `hugo.toml`

### Content Blocks Not Displaying
- Verify `content` array is properly formatted
- Check that `type: "text"` is specified
- Ensure proper YAML indentation
- Use `|` for multi-line text
- Verify template supports content blocks

## Testing Checklist

- [ ] Footer displays correctly on desktop
- [ ] Footer is responsive on mobile
- [ ] All internal links work
- [ ] External links open in new tab
- [ ] Copyright shows current year
- [ ] Site title appears correctly
- [ ] Bottom links display properly
- [ ] Dark mode styling works
- [ ] No YAML syntax errors
- [ ] All sections have content

## File Location

- **Configuration File**: `data/footer.yaml`
- **Template File**: `themes/boc/layouts/_partials/footer.html`
- **CSS File**: `themes/boc/assets/css/footer.css`

## Related Documentation

- [Mega Menu Configuration](MEGA_MENU_GUIDE.md)
- [Theme Configuration](hugo.toml)
- [Hugo Data Files](https://gohugo.io/templates/data-templates/)

---

**Last Updated**: 2024  
**Hugo Version**: 0.146.0+  
**Theme**: Bank of Canada Inspired Theme