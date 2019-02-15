#!/bin/bash

cat bsec2019.txt| awk -F '\t' '{print "<tr>\n\t<td>"$1"</td>\n\t<td>"$2"</td>\n\t<td><a href=\""$4"\" target=\"_blank\">"$3"</a></td>\n\t<td>"$5"</td>\n\t<td></td>\n\t<td><a href=\"mailto:"$7"\">"$6"</a></td>\n</tr>"}'
