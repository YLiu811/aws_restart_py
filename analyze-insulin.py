import re
import os

save_file = "binsulin-seq-clean.txt"

def extract_chars(text):
    """Extracts the xxx alphabetic characters from a string.

    Args:
        text: The input string.
    Returns:
        The extracted string, or None if no match is found.
    """
    # match = re.match(r"[a-zA-Z]{1,24}", text) #Improved regex that considers both upper and lower case
    match = re.search(r"{24,54}", text)
    if match:
        return match.group(0)
    return None

def read_file_content(filename):
    """Reads the content of a file.

    Args:
        filename: The name of the file.

    Returns:
        The content of the file as a string, or None if an error occurs.
    """
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def save_to_file(text_to_save, save_file):
    """Saves text to a file.
    Args:
        text_to_save: The text to save.
        filename: The name of the file.
    """
    try:
        with open(save_file, "w") as f:
            f.write(text_to_save)
        print(f"Text saved to {save_file}")
    except Exception as e:
        print(f"An error occurred while saving to file: {e}")

def count_characters_in_file(filename, exclude_spaces=True, exclude_non_alphanumeric=True):
    """Counts characters in a file, optionally excluding spaces or non-alphanumeric characters.
    Args:
        filename: The path to the file.
        exclude_spaces: If True, spaces are not counted.
        exclude_non_alphanumeric: If True, non-alphanumeric characters are not counted.

    Returns:
        The character count, or None if an error occurs.
    """
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)
        with open(file_path, "r") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None
    # 2. Counting Characters with Regex
    if exclude_spaces and exclude_non_alphanumeric:
        characters = re.findall(r"[a-zA-Z0-9]", text) # Count only alphanumeric characters
    elif exclude_spaces:
      characters = re.findall(r"[^\s]", text) # Count everything that is not a space
    elif exclude_non_alphanumeric:
        characters = re.findall(r"[a-zA-Z0-9\s]", text) # Count alphanumeric and spaces
    else:
        characters = list(text) # Count everything
    return len(characters)
count = count_characters_in_file(save_file)
# Get the directory of the current script
# Example to show the current working directory
# print(f"Current working directory: {os.getcwd()}") #For debugging purposes only
read_file= "preproinsulin-seq-clean.txt"
script_dir = os.path.dirname(os.path.abspath(__file__)) #This is the most robust way to get current directory
file_path = os.path.join(script_dir, read_file) #Construct the path to the file
print(f"Attempting to open file at path: {file_path}")
file_content = read_file_content(file_path)
if file_content:
    print(file_content)
    extracted_text = extract_chars(file_content)
    if extracted_text:
        print("Extracted text:", extracted_text)
        save_to_file(extracted_text, save_file)
        print(f'count of save_file is {count}')
    else:
        print("No matching text found in the file.")
else:
    print("Could not read the file. Please check if it exists and is readable.")


