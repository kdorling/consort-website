# Utility Links Feature Documentation

## Summary
Added a row of configurable utility links below the header buttons (Search, Language, Theme toggle). These links are pipe-separated and can be easily customized by editors through the Hugo configuration file.

## Changes Made

### 1. Header Template Update
**File:** `test/themes/boc/layouts/_partials/header.html`

#### Structure Changes
- Wrapped header utilities and new utility links in a `.header-right` container
- Added a new `<nav class="utility-links">` section below the buttons
- Links are dynamically generated from site configuration
- Pipe separators (`|`) automatically added between links

#### Template Code
```html
<div class="header-right">
    <div class="header-utils">
        <!-- Search, Language, Theme, Mobile Menu buttons -->
    </div>

    <nav class="utility-nav" aria-label="Utility navigation">
        {{- $utilityLinks := site.Params.utilityLinks | default (slice
            (dict "text" "Online Services" "url" "/services")
            (dict "text" "Careers" "url" "/careers")
            (dict "text" "Contact Us" "url" "/contact")
        ) -}}
        {{- range $index, $link := $utilityLinks -}}
            {{- if gt $index 0 }}
                <span class="utility-nav-separator" aria-hidden="true">|</span>
            {{ end -}}
            <a href="{{ $link.url }}" class="utility-nav-link">{{ $link.text }}</a>
        {{- end -}}
    </nav>
</div>
```

### 2. CSS Styling
**File:** `test/themes/boc/assets/css/main.css`

#### Desktop Styles
```css
.header-right {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 10px;
}

.utility-nav {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.875rem;
}

.utility-nav-link {
    color: var(--text-primary);
    text-decoration: none;
    transition: color 0.3s ease;
    white-space: nowrap;
}

.utility-nav-link:hover {
    color: var(--boc-teal);
    text-decoration: underline;
}

.utility-nav-separator {
    color: var(--text-secondary);
    user-select: none;
    padding: 0 4px;
}
```

#### Mobile Styles
```css
@media (max-width: 768px) {
    .utility-nav {
        display: flex;
        font-size: 0.8rem;
        margin-top: 8px;
    }
}
```

### 3. Configuration File
**File:** `test/hugo.toml`

Added configurable utility links in the `[params]` section:

```toml
[params]
  description = 'More than a bank. We are the Central Bank of Canada.'

  # Utility links displayed in the header (above navigation)
  [[params.utilityLinks]]
    text = "Online Services"
    url = "/services"

  [[params.utilityLinks]]
    text = "Careers"
    url = "/careers"

  [[params.utilityLinks]]
    text = "Contact Us"
    url = "/contact"
```

## Visual Layout

### Desktop View
```
┌──────────────────────────────────────────────────────┐
│  [Logo]              [🔍 Search] [FR] [🌙] [☰]       │
│                      Online Services | Careers | Contact Us │
└──────────────────────────────────────────────────────┘
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃         [Home]  [About]  [Services]  [Contact]       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

### Mobile View
```
┌────────────────────────────────┐
│  [Logo]              [☰]       │
│         Services | Careers | Contact │
└────────────────────────────────┘
```

## How to Customize Links

Editors can modify the utility links by editing the `hugo.toml` file:

### Adding a New Link
```toml
[[params.utilityLinks]]
  text = "New Link"
  url = "/new-page"
```

### Changing Link Text
```toml
[[params.utilityLinks]]
  text = "Updated Text"
  url = "/services"
```

### Changing Link URL
```toml
[[params.utilityLinks]]
  text = "Online Services"
  url = "/new-services-page"
```

### Reordering Links
Simply change the order of the `[[params.utilityLinks]]` blocks in the config file.

### Removing Links
Delete or comment out the `[[params.utilityLinks]]` block:
```toml
# [[params.utilityLinks]]
#   text = "Careers"
#   url = "/careers"
```

## Default Links

If no links are configured in `hugo.toml`, the system defaults to:
1. **Online Services** → `/services`
2. **Careers** → `/careers`
3. **Contact Us** → `/contact`

## Features

### Accessibility
- Uses semantic `<nav>` element with `aria-label="Utility navigation"`
- Pipe separators marked with `aria-hidden="true"` (decorative only)
- Proper link structure for screen readers
- Keyboard navigable

### Responsive Design
- Desktop: Links displayed with pipe separators (14px font)
- Tablet: Links visible (14px font)
- Mobile (≤768px): Links visible with smaller font (12.8px)

### Styling
- **Font size**: 0.875rem (14px) - slightly smaller than body text
- **Text color**: Matches body text (`var(--text-primary)`)
- **Hover color**: Olive green accent (`var(--boc-teal)`)
- **Separator color**: Secondary text color (`var(--text-secondary)`)
- **Spacing**: 8px gap between elements, 4px padding around separators
- **Mobile Font**: 0.8rem (12.8px) - smaller for space efficiency

### Dark Mode Support
- Colors automatically adjust via CSS variables
- Works seamlessly in both light and dark themes

## Examples

### Minimal Configuration (2 links)
```toml
[[params.utilityLinks]]
  text = "Login"
  url = "/login"

[[params.utilityLinks]]
  text = "Help"
  url = "/help"
```
**Result:** `Login | Help`

### Extended Configuration (5 links)
```toml
[[params.utilityLinks]]
  text = "Online Banking"
  url = "/banking"

[[params.utilityLinks]]
  text = "Services"
  url = "/services"

[[params.utilityLinks]]
  text = "Careers"
  url = "/careers"

[[params.utilityLinks]]
  text = "Media"
  url = "/media"

[[params.utilityLinks]]
  text = "Contact"
  url = "/contact"
```
**Result:** `Online Banking | Services | Careers | Media | Contact`

### External Links
```toml
[[params.utilityLinks]]
  text = "Partner Portal"
  url = "https://partners.example.com"

[[params.utilityLinks]]
  text = "Customer Login"
  url = "https://login.example.com"
```

## Technical Details

### Template Logic
- Uses Hugo's `site.Params.utilityLinks` to fetch configuration
- Unique class names prevent conflicts with main navigation:
  - `.utility-nav` for the container (vs `.nav-container` for main nav)
  - `.utility-nav-link` for links (vs regular `nav a` selectors)
  - `.utility-nav-separator` for pipe characters
- Falls back to default links if none configured
- Uses `range $index` to conditionally add separators (skips first item)
- Pipe separator only appears between links, not at start/end

### CSS Positioning
- Links right-aligned to match button row above
- Flexbox layout for easy spacing
- `white-space: nowrap` prevents text wrapping
- `gap` property for consistent spacing

### Performance
- No JavaScript required
- Static HTML generated at build time
- Minimal CSS (< 30 lines)
- No impact on page load performance

## Browser Support

Fully supported in:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- iOS Safari 14+
- Chrome Mobile

## Migration from Old Structure

If you had custom header utility code, you may need to:
1. Move utility buttons into `.header-right > .header-utils`
2. Add utility links in `hugo.toml`
3. Update any custom CSS targeting `.header-utils` parent

## Future Enhancements

Possible improvements:
- Option to show/hide on mobile
- Icon support before link text
- External link indicators
- Active state for current section
- Dropdown submenus for utility links
- Custom separator character (not just `|`)

## Class Names Reference

All utility navigation elements use unique class names to prevent conflicts with the main navigation:

| Element | Class Name | Purpose |
|---------|------------|---------|
| Container | `.utility-nav` | Wrapper for utility links |
| Link | `.utility-nav-link` | Individual utility link |
| Separator | `.utility-nav-separator` | Pipe character between links |

This ensures styles applied to utility links do not affect the main navigation bar and vice versa.

## Testing Checklist

- [x] Links display with pipe separators
- [x] Hover states work correctly
- [x] Links are right-aligned
- [x] Mobile view displays links with smaller font
- [x] Dark mode compatibility
- [x] Configuration in hugo.toml works
- [x] Default links appear if not configured
- [x] Accessibility: semantic HTML and ARIA labels
- [x] Keyboard navigation works
- [x] No layout shift on hover
- [x] Unique class names prevent nav conflicts

## Support

For questions or issues with utility links:
1. Check `hugo.toml` syntax is correct
2. Verify link URLs are valid
3. Test in multiple browsers
4. Check mobile responsiveness
5. Validate HTML structure in browser dev tools