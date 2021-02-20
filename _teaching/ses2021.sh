#!/bin/bash

cat ses2021.txt| awk -F '\t' '{print "<tr>\n\t<td>"$1"</td>\n\t<td><a href=\""$4"\" target=\"_blank\">"$3"</a></td>\n\t<td>"$5"</td>\n\t<td></td>\n\t<td><a href=\"mailto:"$7"\">"$6"</a></td>\n</tr>"}'
