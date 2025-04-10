def modify_and_write_file(input_filename, output_filename):
    """
    Reads a file, modifies each line, and writes the modified lines to a new file.

    Args:
        input_filename (str): The name of the input file.
        output_filename (str): The name of the output file to be created.
    """
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                # Simple modification: Add "Processed: " to the beginning of each line
                modified_line = "Processed: " + line.strip() + "\n"
                outfile.write(modified_line)
        print(f"Successfully processed '{input_filename}' and wrote to '{output_filename}'")
    except FileNotFoundError:
        print(f"Error: The input file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}' or write to '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    while True:
        input_file = input("Enter the name of the file to read: ")
        try:
            with open(input_file, 'r') as f:
                # Successfully opened the file, break out of the loop
                break
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied to read '{input_file}'. Please check file permissions.")
        except Exception as e:
            print(f"An unexpected error occurred while trying to open '{input_file}': {e}. Please try again.")

    output_file = input("Enter the name for the new output file: ")
    modify_and_write_file(input_file, output_file)

    print("\nProgram finished.")