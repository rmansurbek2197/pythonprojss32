class PalindromDetector:
    def __init__(self, text):
        self.text = text
        self.words = text.split()
        self.palindroms = []

    def find_palindroms(self):
        for word in self.words:
            if self.is_palindrom(word):
                self.palindroms.append(word)

    def is_palindrom(self, word):
        word = word.lower()
        return word == word[::-1]

    def print_palindroms(self):
        print("Palindrom so'zlar:")
        for palindrom in self.palindroms:
            print(palindrom)

def main():
    text = "Madam, Arora, refer, level, radar, madam"
    detector = PalindromDetector(text)
    detector.find_palindroms()
    detector.print_palindroms()

    text = "Kamil, anna, bob, dad, mom, radar"
    detector = PalindromDetector(text)
    detector.find_palindroms()
    detector.print_palindroms()

    text = "Aibek, Javokhir, Bekzod, level, refer"
    detector = PalindromDetector(text)
    detector.find_palindroms()
    detector.print_palindroms()

    text = "Ona, ota, inson, it, level, madam"
    detector = PalindromDetector(text)
    detector.find_palindroms()
    detector.print_palindroms()

    text = "Refer, level, madam, anna, bob, dad"
    detector = PalindromDetector(text)
    detector.find_palindroms()
    detector.print_palindroms()

if __name__ == "__main__":
    main()