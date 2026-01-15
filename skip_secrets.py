import sys
import os

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    
    filename = sys.argv[1]
    if not os.path.isfile(filename) or not os.access(filename, os.R_OK):
        sys.exit(1)
    
    try:
        with open(filename, 'r') as infile:
            lines = infile.readlines()
    except Exception:
        sys.exit(1)
    
    filtered_lines = []
    for line in lines:
        if 'pineapple' not in line:
            filtered_lines.append(line)

    try:
        with open('out.txt', 'w') as outfile:
            outfile.writelines(filtered_lines)
    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    main()