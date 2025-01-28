import os

# Define the size threshold in bytes (40 MB)
size_threshold = 50 * 1024 * 1024

# Get list of files in the current working directory and subdirectories
files_with_sizes = []
for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
        filesize = os.path.getsize(filepath)
        if filesize > size_threshold:
            files_with_sizes.append((filepath, filesize))

# Sort files by size
files_with_sizes.sort(key=lambda x: x[1], reverse=True)

# Print files with sizes
for file, size in files_with_sizes:
    # display in mb
    size = size / (1024 * 1024)
    print(f"{file}: {size} MB")