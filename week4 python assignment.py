def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (Example: converting text to uppercase)
        modified_content = content.upper()

        # Open the output file for writing the modified content
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File has been successfully modified and saved to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write to the file '{input_filename}' or '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Ask the user for the input and output filenames
input_filename = input("Enter the name of the file to read from: ")
output_filename = input("Enter the name of the file to write to: ")

# Call the function with user-provided filenames
read_and_modify_file(input_filename, output_filename)
