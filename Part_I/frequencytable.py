
def create_frequency_table(file_path):
    frequency_table = {}
    with open(file_path, 'r') as file:
        for line in file:
            char, freq = line.split()
            frequency_table[char] = int(freq)
    return frequency_table

if __name__ == "__main__":
    frequency_table = create_frequency_table("./test/freqfilespec.txt")
    print("Frequency table")
    for char, freq in frequency_table.items():
        print(char, freq)
