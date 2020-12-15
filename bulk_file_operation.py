import os


class OperationsOnFiles:
    def __init__(self, src_path):
        self.src_path = src_path

    try:
        # Prints the name of all the files with the extensions in the folder specified
        def src_files(self):
            i = 1
            file_dir = os.listdir(self.src_path)
            while True:
                if len(file_dir) == 0:
                    print("There are no files in this folder. Please try again or choose a different folder")
                    exit()
                else:
                    for file in file_dir:
                        print("All the files in the source folder are: ")
                        print()
                        file_names = str(i) + ". " + file
                        print(file_names)
                        i += 1
                return ""

        # Renames all the files or files with specific extension in the folder with a number attached to the end of
        # the file name
        def rename_bulk_files(self):
            i = 0
            path = self.src_path
            for file in os.listdir(path):
                dot_index = file.index('.')
                # file_path = os.path.join(path, file)
                if not files_extension or file.endswith(files_extension):  # !
                    file_src = os.path.join(path, file)  # !
                    file_des = os.path.join(path, file[0:dot_index] + "_" + str(i) + file[dot_index:])
                    os.rename(file_src, file_des)
                    i += 1

            print("All files have been renamed")

        # Move files or files with specific extension in one folder to another folder
        def move_bulk_files(self):
            destination_folder_path = input("Enter the destination folder in which you want to move the files: ")
            path = self.src_path
            for file in os.listdir(path):
                if not files_extension or file.endswith(files_extension):
                    src_path = os.path.join(path, file)  # !
                    des_path = os.path.join(destination_folder_path, file)
                    os.replace(src_path, des_path)
            print("All files have been moved to the destination folder")

        # Delete files or files with specific extensions in a folder
        def delete_bulk_files(self):
            path = self.src_path
            for i in os.listdir(self.src_path):
                file_path = os.path.join(path, i)
                if not files_extension or file_path.endswith(files_extension):
                    os.remove(file_path)
            print("All files have been deleted")

    except FileNotFoundError:
        print()
        print("The file you want to perform the action is not in the folder")
    except ValueError:
        print()
        print("Please enter a valid choice of operation")


try:
    source_folder_path = input("Enter the source of the folder on which you wish to perform the operation: ")
    my_operations = OperationsOnFiles(source_folder_path)
    print(my_operations.src_files())
    print("File Operations: \n1. Rename Bulk Files \n2. Move Bulk Files \n3. Delete Bulk Files")
    user_choice = int(input("Enter a number to perform the operations: "))
    files_extension = input(
        "Enter file extension of the file to be deleted or press 'ENTER' to delete all files: ").lower()

    if user_choice == 1:
        my_operations.rename_bulk_files()
    elif user_choice == 2:
        my_operations.move_bulk_files()
    elif user_choice == 3:
        my_operations.delete_bulk_files()
    else:
        print("Please enter a valid input")

except FileNotFoundError:
    print()
    print("The file you want to perform the action is not in the folder")
