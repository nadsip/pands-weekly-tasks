

import sys
import os

def count_es_in_file(filename):
    try:
        with open(filename, 'r') as file:
            e_count = 0
            for line in file:
                e_count += line.lower().count('e')
            return e_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
        sys.exit(1)
    except IOError:
        print(f"Error: Cannot read the file '{filename}'.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("usage: python es.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' is not a valid file.")
        sys.exit(1)

    e_count = count_es_in_file(filename)

    print(e_count)

if __name__ == '__main__':
    main()