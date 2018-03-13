
def main():
    try:
        text = input("Input: ")
        result = {}
        for letter in set(text):
            result[letter] = text.count(letter)
        print('Output: ')
        for key, value in result.items():
            print(key, " - ", value)
    except TypeError:
        print("Error: Could not count characters")

main()
