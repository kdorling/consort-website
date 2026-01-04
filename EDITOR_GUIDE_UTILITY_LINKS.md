# Quick Reference Guide for Editors: Utility Links

## What are Utility Links?

Utility links are the small text links that appear in the top-right corner of the website header, just below the Search, Language, and Dark Mode buttons. They are separated by pipe characters (`|`).

**Example:** `Online Services | Careers | Contact Us`

## Where to Edit Utility Links

Edit the file: `hugo.toml` (in the root of your website)

## How to Edit

### Current Default Links

```toml
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

### Change Link Text

Simply change the `text` value:

```toml
[[params.utilityLinks]]
  text = "Job Opportunities"  # Changed from "Careers"
  url = "/careers"
```

### Change Link Destination

Simply change the `url` value:

```toml
[[params.utilityLinks]]
  text = "Online Services"
  url = "/banking/online"  # Changed destination
```

### Add a New Link

Add a new block at the end:

```toml
[[params.utilityLinks]]
  text = "Help Center"
  url = "/help"
```

### Remove a Link

Delete the entire block or comment it out:

```toml
# [[params.utilityLinks]]
#   text = "Careers"
#   url = "/careers"
```

### Reorder Links

Cut and paste the blocks in the order you want them to appear:

```toml
# This will appear FIRST
[[params.utilityLinks]]
  text = "Contact Us"
  url = "/contact"

# This will appear SECOND
[[params.utilityLinks]]
  text = "Online Services"
  url = "/services"

# This will appear THIRD
[[params.utilityLinks]]
  text = "Careers"
  url = "/careers"
```

**Result:** `Contact Us | Online Services | Careers`

## Examples

### Example 1: Banking Site
```toml
[[params.utilityLinks]]
  text = "Log In"
  url = "/login"

[[params.utilityLinks]]
  text = "Open Account"
  url = "/open-account"

[[params.utilityLinks]]
  text = "Support"
  url = "/support"

[[params.utilityLinks]]
  text = "Branch Locator"
  url = "/branches"
```

### Example 2: Government Site
```toml
[[params.utilityLinks]]
  text = "Media Centre"
  url = "/media"

[[params.utilityLinks]]
  text = "Careers"
  url = "/careers"

[[params.utilityLinks]]
  text = "Contact"
  url = "/contact"
```

### Example 3: External Links
```toml
[[params.utilityLinks]]
  text = "Partner Portal"
  url = "https://partners.example.com"

[[params.utilityLinks]]
  text = "Investor Relations"
  url = "https://investors.example.com"
```

## Important Notes

- ⚠️ **Always use double brackets**: `[[params.utilityLinks]]`
- ⚠️ **Each link needs both `text` and `url`**
- ⚠️ **Order matters**: Links appear in the order you list them
- 📱 **Mobile**: Links are visible on all devices (smaller font on mobile for better fit)
- 🔄 **After editing**: Save the file and rebuild your Hugo site to see changes

## Common Mistakes to Avoid

### ❌ Wrong - Missing Brackets
```toml
[params.utilityLinks]  # Wrong! Needs double brackets
  text = "Link"
  url = "/page"
```

### ✅ Correct - Double Brackets
```toml
[[params.utilityLinks]]  # Correct!
  text = "Link"
  url = "/page"
```

### ❌ Wrong - Missing Quotes
```toml
[[params.utilityLinks]]
  text = Contact Us  # Wrong! Needs quotes
  url = /contact     # Wrong! Needs quotes
```

### ✅ Correct - With Quotes
```toml
[[params.utilityLinks]]
  text = "Contact Us"  # Correct!
  url = "/contact"     # Correct!
```

## Recommended Number of Links

- **Minimum**: 2 links
- **Recommended**: 3-5 links
- **Maximum**: 6 links (for visual balance)

## Need Help?

1. **Syntax Error?** Check that all quotes match and brackets are correct
2. **Link Not Working?** Verify the URL is correct (include the leading `/`)
3. **Not Showing?** Make sure you've rebuilt the site after editing
4. **Still Stuck?** Contact your web developer

## Testing Your Changes

After editing `hugo.toml`:

1. Save the file
2. Rebuild your Hugo site
3. Check the top-right corner of your header
4. Verify links work by clicking them
5. Test on different page sizes (links appear smaller on mobile)

## Quick Reference Card

| Action | Code |
|--------|------|
| Add Link | Add new `[[params.utilityLinks]]` block |
| Remove Link | Delete or comment out block |
| Change Text | Edit `text = "..."` |
| Change URL | Edit `url = "..."` |
| Reorder | Cut and paste blocks |
| External Link | Use full URL: `url = "https://..."` |
| Internal Link | Use path: `url = "/page"` |