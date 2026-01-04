# Logo Update Documentation

## Summary
Replaced the text-based "Bank of Canada" site title with the consort-logo.png image in the header.

## Changes Made

### 1. Header Template Update
**File:** `test/themes/boc/layouts/_partials/header.html`

- Replaced the `<h1>` tag containing site title text with a `<div>` containing an image
- Changed from:
  ```html
  <h1 class="site-title">
      <a href="{{ site.BaseURL }}" style="color: inherit; text-decoration: none">
          {{ site.Title }}
      </a>
  </h1>
  ```
- Changed to:
  ```html
  <div class="site-title">
      <a href="{{ site.BaseURL }}">
          <img src="/images/consort-logo.png" alt="{{ site.Title }}" class="site-logo" />
      </a>
  </div>
  ```

### 2. CSS Styling Updates
**File:** `test/themes/boc/assets/css/main.css`

#### Desktop Styling
Added new CSS rules for the logo image:

```css
.site-title {
    margin: 0;
    padding: 0;
    display: flex;
    align-items: center;
}

.site-title a {
    display: block;
    line-height: 0;
}

.site-logo {
    height: 50px;
    width: auto;
    display: block;
    transition: opacity 0.3s ease;
}

.site-logo:hover {
    opacity: 0.9;
}
```

#### Mobile Responsive Styling
Updated mobile styles to adjust logo size:

```css
@media (max-width: 768px) {
    .site-logo {
        height: 40px;
    }
}
```

### 3. Logo File Location
**Path:** `/images/consort-logo.png`

The logo is located in:
- `test/static/images/consort-logo.png` (source)
- `test/public/images/consort-logo.png` (built)

## Accessibility Considerations

- The `alt` attribute uses `{{ site.Title }}` to provide meaningful alt text ("Bank of Canada")
- Logo is clickable and links to the home page
- Logo scales appropriately on mobile devices
- Hover effect provides visual feedback

## Logo Specifications

- **Desktop height:** 50px (width auto-scales)
- **Mobile height:** 40px (width auto-scales)
- **Format:** PNG with transparency
- **Hover effect:** 90% opacity on hover

## Testing Checklist

- [ ] Logo displays correctly on all pages
- [ ] Logo is clickable and links to home page
- [ ] Logo scales appropriately on mobile devices
- [ ] Hover effect works as expected
- [ ] Alt text is present for accessibility
- [ ] Logo looks good with the new color scheme (olive green header background)

## Notes

- The site title in `hugo.toml` remains "Bank of Canada" which is used for:
  - Page titles (browser tabs)
  - Alt text for the logo
  - Footer copyright text
  - SEO and metadata

- The logo replaces only the visual header title, not the site configuration