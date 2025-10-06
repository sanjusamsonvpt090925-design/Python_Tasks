# Task 2: Write and Append Data to a File

file_name = "output.txt"

## 1. Takes user input and writes it to a file named output.txt (Overwrites the file)
try:
    # Get the first input from the user
    first_input = input("Enter text to write to the file: ")
    
    # Open the file in 'write' mode ('w') and use 'with' for safe handling
    with open(file_name, 'w') as file:
        file.write(first_input + '\n') # Write the input and a newline character
    
    print(f"Data successfully written to {file_name}.")
    
except Exception as e:
    print(f"An error occurred during writing: {e}")

# -------------------------------------------------------------

## 2. Appends additional data to the same file.
try:
    # Get the second input from the user
    additional_input = input("Enter additional text to append: ")
    
    # Open the file in 'append' mode ('a')
    with open(file_name, 'a') as file:
        file.write(additional_input + '\n') # Append the input and a newline character
        
    print(f"Data successfully appended.")
    
except Exception as e:
    print(f"An error occurred during appending: {e}")

# -------------------------------------------------------------

## 3. Reads and displays the final content of the file.
print(f"\nFinal content of {file_name}:")
try:
    # Open the file in 'read' mode ('r')
    with open(file_name, 'r') as file:
        # Read the entire content of the file
        final_content = file.read()
        print(final_content)
        
except FileNotFoundError:
    print(f"Error: The file {file_name} was not found.")
except Exception as e:
    print(f"An error occurred during reading: {e}")
