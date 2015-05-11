import os

os.system("find . -name \"*.zip\" | while read filename; do unzip -o -d \"`dirname \"$filename\"`\" \"$filename\"; done;")
os.system("find . -name \"*.tar.gz\" | while read filename; do tar -xvzf \"$filename\" -C \"`dirname \"$filename\"`\"; done;")