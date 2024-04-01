
import os
import heapq
from Part_I.frequencytable import create_frequency_table

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequency_table):
    priority_queue = [Node(char, freq) for char, freq in frequency_table.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def generate_huffman_codes(root, current_code, huffman_codes):
    if root is None:
        return
    if root.char is not None:
        huffman_codes[root.char] = current_code
        return
    generate_huffman_codes(root.left, current_code + '0', huffman_codes)
    generate_huffman_codes(root.right, current_code + '1', huffman_codes)

def create_huffman_code_table(huffman_tree):
    huffman_codes = {}
    generate_huffman_codes(huffman_tree, '', huffman_codes)
    return huffman_codes

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(current_dir, "test")
    file_path = os.path.join(test_dir, "freqfilespec.txt")
    
    frequency_table = create_frequency_table(file_path)
    huffman_tree = build_huffman_tree(frequency_table)
    huffman_codes = create_huffman_code_table(huffman_tree)
    print("\nHuffman Codes")
    for char, code in huffman_codes.items():
        print(char, code)

