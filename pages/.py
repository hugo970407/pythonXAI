import os
folderPath = "markdown"
files = os.listdir(folderPath)
files_name = []
for f in files:
    if f.endswith(".md"):
        files_name.append(f)
print(files_name)