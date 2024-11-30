# week-4-python-Assignment-PLP-S-Hook
File Reading and Writing
# File Read & Write Challenge: File Modification with Error Handling

This Python program reads a file, modifies its contents, and writes the modified content to a new file. It includes error handling to manage situations where the input file doesn't exist, cannot be read, or the program encounters other unexpected issues.

## Features
- Reads content from an input file.
- Modifies the content (in this case, converts text to uppercase).
- Writes the modified content to a new output file.
- Handles errors such as file not found, input/output errors, and other exceptions.

## How It Works

1. **User Input**: The user is prompted to provide the names of the input file (to read) and the output file (to write the modified content).
2. **File Reading**: The program attempts to open and read the input file.
3. **Content Modification**: The content of the file is modified (e.g., all text is converted to uppercase).
4. **Writing to a New File**: The modified content is written to a new file.
5. **Error Handling**: The program catches and handles the following types of errors:
   - **FileNotFoundError**: If the input file doesn’t exist.
   - **IOError**: If there are issues reading or writing the files.
   - **Generic Exception**: For unexpected errors.

## Usage

1. Clone or download the script.
2. Run the script in a Python environment:
   
