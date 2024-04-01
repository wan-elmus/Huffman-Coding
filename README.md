
# Huffman Coding Implementation

This project implements Huffman coding, a method for lossless data compression. Huffman coding assigns variable-length bit codes to characters based on their frequencies in the input text. Characters that occur more frequently are assigned shorter codes, resulting in more efficient encoding.

## Table of Contents

- [Huffman Coding Implementation](#huffman-coding-implementation)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Project Structure](#project-structure)
  - [How It Works](#how-it-works)
    - [Part I: Frequency Table Generation](#part-i-frequency-table-generation)
    - [Part II: Huffman Tree and Code Table Generation](#part-ii-huffman-tree-and-code-table-generation)
    - [Part III: Message Encoding](#part-iii-message-encoding)
  - [How to Run](#how-to-run)
  - [Output](#output)

## Overview

The project is divided into three parts:

    Part I: Read an input text file and create a frequency table.
    Part II: Build a Huffman tree based on the frequency table, then generate a Huffman code table.
    Part III: Use the Huffman code table to encode the input text file.

## Project Structure

The project directory contains the following components:

    Part_I/: Contains the implementation for Part I.
    Part_II/: Contains the implementation for Part II.
    Part_III/: Contains the implementation for Part III.
    test/: Contains sample input files for testing. It is in each folders ,i.e., Parts.

## How It Works

### Part I: Frequency Table Generation

In this part, the program reads an input text file and generates a frequency table, where each character is associated with its frequency of occurrence in the text.

### Part II: Huffman Tree and Code Table Generation

This part constructs a Huffman tree based on the frequency table generated in Part I. The Huffman tree is then used to generate a Huffman code table, where each character is mapped to its corresponding Huffman code.

### Part III: Message Encoding

Using the Huffman code table generated in Part II, this part encodes the input text file into binary format, using the Huffman codes assigned to each character.

## How to Run

Navigate to the project root directory - Huffman_coding.
Run each part separately by executing the corresponding Python file.

For Part I: **Execute**  *python3 Part_I/a.py*

For Part II: **Execute**  *PYTHONPATH="${PYTHONPATH}:$(pwd)" python3 Part_II/Huffman_tree_and_codetable.py*

For Part III: **Execute**  *PYTHONPATH="${PYTHONPATH}:$(pwd)" python3 Part_III/encode.py*

## Output

The output of each part will be displayed in the terminal/console, showing the frequency table, Huffman codes, and the encoded message.
