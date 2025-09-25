
def caesar_cipher(text, step):
    result = ''
    for char in text:
        if char.isalpha():
            shift = step % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def process_file(input_filename, output_filename, step):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()
        
        encrypted_content = caesar_cipher(content, step)
        
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(encrypted_content)
        
        print(f"File processed successfully. Output saved to '{output_filename}'")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")
    try:
        step = int(input("Enter the distance value: "))
    except ValueError:
        print("Error: Distance value must be an integer.")
        return

    process_file(input_file, output_file, step)


if __name__ == '__main__':
    main()