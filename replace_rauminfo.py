"""
Wrap all mentions of a room in a link to the room's location page.

common formats for rooms:
CAB G 56
CAB G56
HG F 81.1
HG F81.1
note: can be any ALLCAPS SINGLE LETTER DIGITS combination

Link format:
https://ethz.ch/en/utils/location.html?building=LFW&floor=C&room=5&lang=en
"""

import re
import os

# match mentions of rooms, skip if they are in a link
room_regex = re.compile(r"(?<!\>)(?P<space>\s+|\(\s*|,\s*)(?P<building>[A-Z]+)\s(?P<floor>[A-Z])\s?(?P<room>\d+(\.\d+)?)")

# walk the tree and find all files
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            with open(os.path.join(root, file), "r") as f:
                content = f.read()

            printed = False
            # find all mentions of a room
            # propose to user to replace each match with the link
            for match in room_regex.finditer(content):
                if not printed:
                    print(file)
                    printed = True
                print(match.groupdict())
                # replace the match with the link
                content = content.replace(match.group(0), f"{match.group('space')}<a href=\"https://ethz.ch/en/utils/location.html?building={match.group('building')}&floor={match.group('floor')}&room={match.group('room')}&lang=en\">{match.group('building')} {match.group('floor')} {match.group('room')}</a>")

            # write the content back to the file
            with open(os.path.join(root, file), "w") as f:
                f.write(content)
