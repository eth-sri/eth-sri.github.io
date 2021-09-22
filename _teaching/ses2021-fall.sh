#!/bin/bash

cat ses2021-fall.txt | awk -F '\t' '{print "<tr>\n\t<td>"$1"</td>\n\t<td><a href=\""$3"\" target=\"_blank\">"$2"</a></td>\n\t<td>"$4"</td>\n\t<td></td>\n\t<td></td>\n\t<td><a href=\"mailto:"$6"\">"$5"</a></td>\n</tr>"}'
