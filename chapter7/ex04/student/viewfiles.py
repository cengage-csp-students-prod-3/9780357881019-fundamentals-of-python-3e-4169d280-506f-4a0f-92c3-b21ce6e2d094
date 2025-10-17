import os

def displayFiles(pathname):
    """Recursively displays file names and contents within directories."""
    if os.path.isfile(pathname):
        print(f"File name: {pathname}")
        with open(pathname, 'r') as file:
            print(file.read())
    elif os.path.isdir(pathname):
        print(f"Directory name: {pathname}")
        for name in os.listdir(pathname):
            full_path = os.path.join(pathname, name)
            displayFiles(full_path)