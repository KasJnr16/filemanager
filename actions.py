import os
import shutil

def get_cwd():
    cwd = os.getcwd()
    print("\nCurrent working directory: <<<{}>>>\n".format(cwd))
    return cwd

def data_selector(data_list):
    try:
        num = int(input("\nChoose the number corresponding to the directory you want to select: "))
        choosen_item = data_list[num - 1]
        print(f"\nYou have selected {choosen_item}")
        return choosen_item
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")
        return data_selector(data_list)

def confirm_action(action, item):
        confirmation = input(f'\nAre you sure you want to {action} <<<{item}>>>? [Y/n] ').lower()
        if confirmation == "y":
            return True
        else:
            print("Operation canceled.")
            return False

def show_files():
    """Display all files present in the current working directory."""
    cwd = get_cwd()
    try:
        files_in_dir = [file for file in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, file))]
        for i, file in enumerate(files_in_dir, start=1):
           print("{}. {}".format(i, file))
        return files_in_dir
    except Exception as e:
        print(f"\tError accessing {file}: {e}")
        return []

def show_directories():
    cwd = get_cwd()
    try:
        dir_list =[directory for directory in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, directory))]
        for i, directory in enumerate(dir_list, start=1):    
            print("{}. {}".format(i, directory))
        return dir_list
    except Exception as e:
        print(f"\tError accessing {directory}: {e}")
        return []
    
def show_files_and_directories():
    cwd = get_cwd()
    try:
        items = os.listdir(cwd)
        for i, item in enumerate(items, start=1):
            print("{}. {}".format(i, item))
        return items
    except Exception as e:
        print(f"\tError accessing items: {e}")
        return []
    
def make_file():
    """Create a new file within the current working directory."""
    cwd = get_cwd()
    filename = input("Enter the name of the file (with extension) <<<exp: myfile.txt>>>> : ")
    file_path = os.path.join(cwd, filename)
    # Check if file already exists
    if os.path.exists(file_path):
        print("File already exists. Operation canceled.")
    else:
        try:
            if confirm_action("create", filename) == True:
                with open(file_path, "w") as file:
                    print(f"{filename} has been created at {file_path}")
                    return True
        except Exception as e:
            print(f"Error creating {filename}: {e}")
            return False

def make_directory():
    """Create a directory for the output files if it doesn't exist"""
    # Get the current working directory
    cwd = os.getcwd()
    folder_name = str(input("Enter the name of the folder: "))
    try:
        if confirm_action("create", folder_name) == True:
            os.mkdir(os.path.join(cwd, folder_name))
            print(f"Directory <<<{folder_name}>>> created successfully.")
            return True
    except Exception as e:
        print(f"Error creating directory: {e}")
        return False
    
def remove_file(source):
    """Remove an existing file from the current working directory."""
    try:
        if confirm_action("delete", source) == True:
            os.remove(source)
            print(f"File <<<{source}>>> deleted successfully.")
            return True
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False
    
def remove_directory(source):
    """Remove an existing directory"""
    try:
        if confirm_action("delete", source) == True:
            os.rmdir(source)
            print(f"Directory <<<{source}>>> deleted successfully.")
            return True
    except Exception as e:
        print(f"Error deleting directory: {e}")
        return False
    
def rename_item(old_name, item_type):
    try:
        if confirm_action("rename", old_name) == True:
            new_name = str(input("\nEnter the name of the new name: "))
            os.rename(old_name, new_name)
            print(f"{item_type.capitalize()} <<<{old_name}>>> renamed to <<<{new_name}>>> successfully.")
            return True
    except Exception as e:
        print(f"Error renaming {item_type}: {e}")
        return False

def rename_file(old_name):
    """Rename an existing file."""
    return rename_item(old_name, "file")

def rename_directory(old_name):
    """Rename an existing directory."""
    return rename_item(old_name, "directory")

def copy_item(source, item_type):
    try:
        if confirm_action("copy", source) == True:
            destination = str(input("Where do you want to copy to? "))
            shutil.copytree(source, destination) if os.path.isdir(source) else shutil.copy2(source, destination)
            print(f"{item_type.capitalize()} <<<{source}>>> copied to <<<{destination}>>> successful.")
            return True
    except Exception as e:
        print(f"Error copying {item_type.capitalize()}: {e}")
        return False
    
def copy_file(source):
    """Copy an existing file."""
    return copy_item(source, "file")

def copy_directory(source):
    """Copy an existing directory."""
    return copy_item(source, "directory")
    
def move_item(source, item_type):
    """Move a file or directory from source to destination."""
    try:
        if confirm_action("move", source) == True:
            destination = str(input("Where do you want to move to? "))
            shutil.move(source, destination)
            print(f"{item_type.capitalize()} <<<{source}>>> moved to <<<{destination}>>> successfully.")
            return True
    except Exception as e:
        print(f"Error moving {item_type}: {e}")
        return False

def move_file(source):
    """Move an existing file."""
    return move_item(source, "file")

def move_directory(source):
    """Move an existing directory."""
    return move_item(source, "directory")

items = show_files_and_directories()
selected_item  = data_selector(items)
if os.path.isdir(selected_item):
    move_directory(selected_item)
elif os.path.isfile(selected_item):
    move_file(selected_item)
else:
    print("Error")


