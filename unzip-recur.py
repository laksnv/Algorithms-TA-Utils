import os

os.system("find . -name \"*.zip\" | while read filename; do unzip -o -d \"`dirname \"$filename\"`\" \"$filename\"; done;")