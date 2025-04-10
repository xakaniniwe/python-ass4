# python-ass4
# File Read & Write with Error Handling

This Python script demonstrates how to read the contents of a file, modify each line, and write the modified lines to a new file. It also includes robust error handling to gracefully manage scenarios where the input file does not exist or cannot be read.

## How to Use

1.  **Save the script:** Save the Python code (provided in the previous response) as a `.py` file (e.g., `file_processor.py`).

2.  **Prepare an input file (optional):** Create a text file (e.g., `input.txt`) in the same directory as the script. You can populate this file with the text you want to process. If you don't have an input file ready, the script will prompt you for one, and you can create it then.

3.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the file, and execute the script using the Python interpreter:

    ```bash
    python file_processor.py
    ```

4.  **Enter the input filename:** The script will prompt you to enter the name of the file you want to read. Type the filename (e.g., `input.txt`) and press Enter.

    * **Error Handling:** If the file you enter does not exist or if the script doesn't have permission to read it, an informative error message will be displayed, and you will be asked to enter the filename again.

5.  **Enter the output filename:** Once a valid input file is provided, the script will ask you to enter the name for the new file where the modified content will be written (e.g., `output.txt`).

6.  **View the output:** After successful processing, a new file with the name you specified will be created in the same directory. This file will contain the modified content from the input file. In this script, each line from the input file will be prefixed with "Processed: ".

## Functionality

The script consists of the following main components:

* **`modify_and_write_file(input_filename, output_filename)` function:**
    * Takes the names of the input and output files as arguments.
    * Uses a `try-except` block to handle potential `FileNotFoundError`, `PermissionError`, and other general `Exception` during file operations.
    * Opens the input file in read mode (`'r'`) and the output file in write mode (`'w'`) using the `with` statement (ensuring automatic file closing).
    * Iterates through each line in the input file.
    * Modifies each line by adding the prefix "Processed: " and a newline character.
    * Writes the modified line to the output file.
    * Prints a success message upon completion or an error message if any issue occurs.

* **Main execution block (`if __name__ == "__main__":`)**
    * Uses a `while True` loop with a `try-except` block to repeatedly prompt the user for the input filename until a valid, readable file is provided.
    * Prompts the user for the desired name of the output file.
    * Calls the `modify_and_write_file()` function to perform the file reading, modification, and writing.
    * Prints a "Program finished." message at the end.

## Error Handling

The script implements error handling for the following common scenarios:

* **File Not Found:** If the user enters the name of a file that does not exist in the specified location, a `FileNotFoundError` is caught, and an informative message is displayed, prompting the user to try again.
* **Permission Denied:** If the script does not have the necessary permissions to read the input file or write to the output file, a `PermissionError` is caught, and a message advising the user to check file permissions is shown.
* **Other Unexpected Errors:** A general `Exception` is caught to handle any other unforeseen issues that might arise during file operations, providing a more robust user experience.

## Example Usage

1.  Create a file named `my_input.txt` with the following content:
    ```
    Line one
    Second line
    Third line of text
    ```

2.  Run the `file_processor.py` script.

3.  When prompted, enter `my_input.txt` as the input filename.

4.  When prompted, enter `my_output.txt` as the output filename.

5.  After the script finishes, a new file named `my_output.txt` will be created with the following content:
    ```
    Processed: Line one
    Processed: Second