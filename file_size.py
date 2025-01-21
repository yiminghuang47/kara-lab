
import os

def list_files_by_size_recursive(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            size = os.path.getsize(filepath)//1000000  # Convert to MB
            if size > 50:
                files.append((filepath, size))

    # Sort files by size (descending)
    files.sort(key=lambda x: x[1], reverse=True)

    for filepath, size in files:
        print(f"{filepath}: {size} mb")

# Specify the directory
directory = "C:/Users/yh1024/Documents/Yiming Huang"
list_files_by_size_recursive(directory)