#!/bin/bash

cat bsec2018.txt| awk -F '\t' '{print "<tr>\n\t<td>"$1"</td>\n\t<td><a href=\""$3"\" target=\"_blank\">"$2"</a></td>\n\t<td></td>\n\t<td></td>\n\t<td></td>\n</tr>"}'
