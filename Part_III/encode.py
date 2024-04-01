
import os
from Part_I.frequencytable import create_frequency_table
from Part_II.Huffman_tree_and_codetable import build_huffman_tree, create_huffman_code_table

def encode_message(file_path, huffman_codes):
    encoded_message = ""
    with open(file_path, 'r') as file:
        for line in file:
            for char in line.strip():
                encoded_message += huffman_codes.get(char, '')
    
    return encoded_message

def write_binary_file(encoded_message, output_file_path):
    with open(output_file_path, 'wb') as binary_file:
        binary_file.write(encoded_message.encode())

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(current_dir, "test")
    file_path = os.path.join(test_dir, "freqfilespec.txt")
    encodefile_path = os.path.join(test_dir, "filetoencode.txt")
    output_file_path = os.path.join(current_dir, "encoded_message.bin")
    
    frequency_table = create_frequency_table(file_path)
    huffman_tree = build_huffman_tree(frequency_table)
    huffman_codes = create_huffman_code_table(huffman_tree)
    
    # Add space character to huffman_codes if it's missing
    if ' ' not in huffman_codes:
        huffman_codes[' '] = ' ' 
    
    encoded_message = encode_message(encodefile_path, huffman_codes)
    with open(encodefile_path, 'r') as file:
        for line in file:
            print(line.strip())
    
    print("encoded message")
    print(encoded_message)
    
    write_binary_file(encoded_message, output_file_path)
    print(f"Encoded message has been written to {output_file_path}")
