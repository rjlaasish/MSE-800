class TestAnalyzer:
    def __init__(self, data):
        if not isinstance(data, (str, list)):
            raise TypeError("Input must be a string or list of strings.")
        self.data = data

    def get_length(self):
        if isinstance(self.data, str):
            return len(self.data)
        return sum(len(item) for item in self.data)

    def count_uppercase(self):
        text = self.data if isinstance(self.data, str) else "".join(self.data)
        count = 0
        for char in text:
            if char.isupper():
                count += 1
        return count
    def count_digits(self):
        text = self.data if isinstance(self.data, str) else "".join(self.data)
        count = 0
        for char in text:
            if char.isdigit():
                count += 1
        return count

    def count_special_characters(self):
        text = self.data if isinstance(self.data, str) else "".join(self.data)
        count = 0
        for char in text:
            if not char.isalnum():
                count += 1
        return count

    def analyze(self):
        print(f"Word is: {self.data}")
        print(f"Total length is {self.get_length()}")
        print(f"Total uppercases are {self.count_uppercase()}")
        print(f"Total digit are {self.count_digits()}")
        print(f"Total special chars(not a letter or digit) {self.count_special_characters()}\n")


if __name__ == "__main__":
    analyzer1 = TestAnalyzer('Hello World')
    analyzer1.analyze()
    analyzer2 = TestAnalyzer(["Professional", "Software", "Engineering"])
    analyzer2.analyze()
