import os
# Get the current working directory
print("Current Directory -->", os.getcwd())

# List files and folders
print(os.listdir())

# Create a directory
os.mkdir("my_folder")

# Create nested directories
os.makedirs("parent/child")

# Rename a file or folder
os.rename("parent/child", "parent/childcreation")


# Delete an empty directory
os.rmdir("my_folder")
os.rmdir("parent/childcreation")
os.rmdir("parent")

# Check whether something exists
print(os.path.exists("file.txt"))

# Whatever i had done, its just creating folders and deleting at last