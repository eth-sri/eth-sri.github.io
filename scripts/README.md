# Room Links Processing System

This directory contains scripts and documentation for the GitHub Pages-compatible room links processing system that replaces the custom Jekyll plugin.

## Overview

The system automatically converts ETH room mentions (like "CAB G 56", "HG F 3", etc.) into clickable links that point to ETH Zurich's location pages. This replaces the functionality of the `_plugins/room_links.rb` plugin which is not supported on GitHub Pages.

## Components

### 1. Room Extraction Script (`extract_rooms.py`)

This Python script scans your Jekyll site for room mentions and generates a Liquid-compatible room list.

**Usage:**
```bash
cd scripts
python3 extract_rooms.py
```

**What it does:**
- Scans all HTML and Markdown files in your repository
- Uses regex to find room mentions in formats like: `CAB G 56`, `CAB G56`, `HG F 81.1`, `HG F81.1`
- Extracts unique room codes and sorts them alphabetically
- Generates a Liquid string that can be copied into `_includes/process-rooms.html`

### 2. Liquid Include (`_includes/process-rooms.html`)

This Liquid template processes content and converts room mentions to clickable links.

**Usage in layouts:**
```liquid
{% include process-rooms.html content=content %}
```

**Features:**
- Processes all known room codes from the extracted list
- Handles different spacing variations (`CAB G 56` and `CAB G56`)
- Supports rooms in parentheses and after commas
- Generates proper ETH location URLs

### 3. Integration

The room processing is integrated into:
- `_layouts/course.html` - Processes room mentions in course information and content
- `contact.html` - Processes the office location

## Maintenance Workflow

When you add new content with room mentions:

1. **Run the extraction script:**
   ```bash
   cd scripts
   python3 extract_rooms.py
   ```

2. **Copy the generated Liquid string:**
   The script will output a line like:
   ```liquid
   {% assign rooms = "CAB G 51,CAB G 52,..." | split: "," %}
   ```

3. **Update the include file:**
   Replace the `{% assign rooms = ... %}` line in `_includes/process-rooms.html` with the new one.

4. **Commit and push:**
   The changes will be automatically processed by GitHub Pages.

## Supported Room Formats

The system recognizes these room formats:
- `CAB G 56` (building, floor with space, room number)
- `CAB G56` (building, floor without space, room number)  
- `HG F 81.1` (rooms with decimal numbers)
- `HG F81.1` (decimal rooms without space)

## Current Room List

As of the last extraction, the system processes these rooms:
- CAB G 51, CAB G 52, CAB G 56, CAB G 57, CAB G 59, CAB G 61
- CAB H 53, CAB H 69.1
- CHN D 42, CHN D 46, CHN D 48, CHN E 42, CHN E 46, CHN G 22, CHN G 46
- ETZ F 91, ETZ G 91, ETZ H 91, ETZ J 91
- HG D 7.2, HG E 22, HG E 3, HG F 3, HG F 5, HG F 7, HG G 26.5, HG G 3
- IFW A 36
- LFW B 3, LFW C 4, LFW C 5, LFW E 13
- ML D 28, ML E 12, ML F 34, ML F 38, ML H 41.1, ML J 34.1, ML J 34.3
- NO D 11, NO E 11

## Benefits

- ✅ **GitHub Pages Compatible**: No custom plugins required
- ✅ **Automated Detection**: Python script finds all room mentions automatically
- ✅ **No Content Changes**: Existing content works without modification
- ✅ **Easy Maintenance**: Simple workflow to update when new rooms are added
- ✅ **Same Functionality**: Provides identical linking behavior as the original plugin

## Troubleshooting

**If room links aren't working:**
1. Check that the room code is in the list in `_includes/process-rooms.html`
2. Run `extract_rooms.py` to see if new rooms were detected
3. Ensure the layout using the content includes the `process-rooms.html` include

**If new rooms aren't detected:**
1. Verify the room format matches the supported patterns
2. Check that the file containing the room is in one of the scanned directories
3. Run the extraction script with verbose output to debug
