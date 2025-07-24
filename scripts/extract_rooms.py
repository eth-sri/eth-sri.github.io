#!/usr/bin/env python3
"""
Extract room mentions from Jekyll site files and generate Liquid-compatible room list.
This script scans HTML and Markdown files for ETH room mentions and outputs a string
that can be used in the process-rooms.html include file.
"""

import os
import re
import glob
from typing import Set, List

def find_room_mentions(content: str) -> Set[str]:
    """
    Extract room mentions from content using the same regex as the original plugin.
    Matches formats like: CAB G 56, CAB G56, HG F 81.1, HG F81.1
    """
    # Same regex pattern as the original Ruby plugin
    room_pattern = r'(?:^|\s+|\(\s*|,\s*|>)([A-Z]+)\s([A-Z])\s?(\d+(?:\.\d+)?)(?=\s|$|\)|,|<)'
    
    matches = re.findall(room_pattern, content, re.MULTILINE)
    rooms = set()
    
    for building, floor, room_num in matches:
        # Create standardized room format (with space)
        room_code = f"{building} {floor} {room_num}"
        rooms.add(room_code)
    
    return rooms

def scan_files(base_path: str) -> Set[str]:
    """
    Scan all relevant files in the Jekyll site for room mentions.
    """
    all_rooms = set()
    
    # File patterns to scan
    patterns = [
        '**/*.html',
        '**/*.md'
    ]
    
    files_processed = 0
    
    for pattern in patterns:
        full_pattern = os.path.join(base_path, pattern)
        for filepath in glob.glob(full_pattern):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    rooms = find_room_mentions(content)
                    if rooms:
                        print(f"Found {len(rooms)} room(s) in {filepath}: {', '.join(sorted(rooms))}")
                        all_rooms.update(rooms)
                    files_processed += 1
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
    
    print(f"\nProcessed {files_processed} files")
    return all_rooms

def generate_liquid_string(rooms: Set[str]) -> str:
    """
    Generate a Liquid-compatible string for the rooms variable.
    """
    sorted_rooms = sorted(list(rooms))
    # Escape any quotes and join with commas
    escaped_rooms = [room.replace('"', '\\"') for room in sorted_rooms]
    return ','.join(escaped_rooms)

def main():
    """
    Main function to extract rooms and generate output.
    """
    # Get the repository root (assuming script is run from repo root or scripts/ dir)
    if os.path.basename(os.getcwd()) == 'scripts':
        base_path = os.path.dirname(os.getcwd())
    else:
        base_path = os.getcwd()
    
    print(f"Scanning for room mentions in: {base_path}")
    print("=" * 60)
    
    # Extract all room mentions
    all_rooms = scan_files(base_path)
    
    print("=" * 60)
    print(f"Total unique rooms found: {len(all_rooms)}")
    print("\nAll rooms:")
    for room in sorted(all_rooms):
        print(f"  - {room}")
    
    # Generate Liquid string
    liquid_string = generate_liquid_string(all_rooms)
    
    print("\n" + "=" * 60)
    print("LIQUID STRING FOR process-rooms.html:")
    print("=" * 60)
    print('{% assign rooms = "' + liquid_string + '" | split: "," %}')
    
    print("\n" + "=" * 60)
    print("INSTRUCTIONS:")
    print("1. Copy the line above starting with '{% assign rooms ='")
    print("2. Replace the rooms assignment line in _includes/process-rooms.html")
    print("3. Commit and push to update your GitHub Pages site")
    print("=" * 60)

if __name__ == "__main__":
    main()
