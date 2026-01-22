import re

def search_pattern(filename, pattern_type):
    results = []
    if pattern_type == 'ip':
        pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    elif pattern_type == 'url':
        pattern = r'https?://[^\s]+'
    else:
        print("Invalid pattern type. Choose 'ip' or 'url'.")
        return results

    with open(filename, 'r') as file:
        for line in file:
            if re.search(pattern, line):
                results.append(line.strip())
    return results

def main():
    filename = input("Enter the filename to search: ")
    pattern_type = input("Enter pattern type to search (ip/url): ").lower()

    matched_lines = search_pattern(filename, pattern_type)

    if matched_lines:
        print(f"\nLines matching {pattern_type} pattern:")
        for line in matched_lines:
            print(line)
    else:
        print(f"No lines matching {pattern_type} pattern found.")

if __name__ == "__main__":
    main()
