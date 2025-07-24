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

def update_process_rooms_file(base_path: str, liquid_string: str) -> bool:
    """
    Update the _includes/process-rooms.html file with the new room list.
    """
    include_file_path = os.path.join(base_path, '_includes', 'process-rooms.html')
    
    if not os.path.exists(include_file_path):
        print(f"Error: {include_file_path} not found!")
        return False
    
    try:
        # Read the current file
        with open(include_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the rooms assignment line
        import re
        pattern = r'{% assign rooms = "[^"]*" \| split: "," %}'
        new_assignment = f'{{% assign rooms = "{liquid_string}" | split: "," %}}'
        
        if re.search(pattern, content):
            updated_content = re.sub(pattern, new_assignment, content)
            
            # Write the updated content back
            with open(include_file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"✅ Successfully updated {include_file_path}")
            return True
        else:
            print(f"❌ Could not find rooms assignment line in {include_file_path}")
            print("Expected pattern: {% assign rooms = \"...\" | split: \",\" %}")
            return False
            
    except Exception as e:
        print(f"❌ Error updating {include_file_path}: {e}")
        return False

def main():
    """
    Main function to extract rooms and automatically update the include file.
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
    print("UPDATING PROCESS-ROOMS.HTML:")
    print("=" * 60)
    
    # Update the include file automatically
    success = update_process_rooms_file(base_path, liquid_string)
    
    if success:
        print("\n" + "=" * 60)
        print("✅ ROOM PROCESSING UPDATE COMPLETE!")
        print("=" * 60)
        print("The _includes/process-rooms.html file has been automatically updated.")
        print("You can now commit and push the changes to deploy to GitHub Pages.")
        print("\nNext steps:")
        print("1. git add _includes/process-rooms.html")
        print("2. git commit -m 'Update room links processing'")
        print("3. git push")
    else:
        print("\n" + "=" * 60)
        print("❌ MANUAL UPDATE REQUIRED")
        print("=" * 60)
        print("Automatic update failed. Please manually update _includes/process-rooms.html")
        print("Replace the rooms assignment line with:")
        print('{% assign rooms = "' + liquid_string + '" | split: "," %}')
    
    print("=" * 60)

if __name__ == "__main__":
    main()
