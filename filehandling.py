#  File Read & Write Challenge with Error Handling

def modify_content(content):
    """
    Modify the content in any way you'd like.
    Here — convert text to uppercase.
    """
    return content.upper()

def main():
    #  Ask the user for the filename to read
    filename = input("Enter the name of the file to read: ")

    try:
        #  Try opening and reading the file
        with open(filename, 'r') as file:
            content = file.read()

        #  Modify the content
        modified_content = modify_content(content)

        #  Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f" Modified content written to '{new_filename}' successfully.")

    except FileNotFoundError:
        print(" Error: File not found. Please check the filename and try again.")
    except IOError:
        print(" Error: Could not read the file. Please check permissions or file status.")

if __name__ == "__main__":
    main()
