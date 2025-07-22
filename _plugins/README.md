# Jekyll Plugins

## Room Links Plugin (`room_links.rb`)

This plugin automatically converts room mentions in your Jekyll site to clickable links that point to ETH Zurich's location pages.

### How it works

The plugin runs during Jekyll's `post_render` hook and processes all HTML pages and documents from collections. It uses a regular expression to find room mentions in the following formats:

- `CAB G 56`
- `CAB G56` 
- `HG F 81.1`
- `HG F81.1`

And converts them to links like:
```html
<a href="https://ethz.ch/en/utils/location.html?building=CAB&floor=G&room=56&lang=en">CAB G 56</a>
```

### Usage

The plugin runs automatically during `jekyll build` or `jekyll serve`. No manual intervention is required.
