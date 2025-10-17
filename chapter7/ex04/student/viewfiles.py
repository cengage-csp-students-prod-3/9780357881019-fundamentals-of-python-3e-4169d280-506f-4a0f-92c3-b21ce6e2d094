# Write your code here
import os

def view_files(pathname):
    """Recursively displays file names and contents within directories."""
    if os.path.isfile(pathname):
        print(f"File name: {pathname}")
        with open(pathname, 'r') as file:
            print(file.read())
    elif os.path.isdir(pathname):
        print(f"Directory name: {pathname}")
        for name in os.listdir(pathname):
            full_path = os.path.join(pathname, name)
            view_files(full_path)
    else:
        print(f"Invalid path: {pathname}")

# Test the function
if __name__ == "__main__":
    path = input("Enter a directory or file path: ")
    view_files(path)