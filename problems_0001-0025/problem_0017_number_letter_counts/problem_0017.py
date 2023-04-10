ones_mappings = {"0": "", "1": "one", "2": "two", "3": "three", "4": "four",
                 "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}

tens_mappings = {"0": "", "2": "twenty", "3": "thirty", "4": "forty",
                 "5": "fifty", "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety"}

teens_mappings = {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen",
                  "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}


class CountLetters():
    def __init__(self, number: int):
        self.number = str(number)
        self.digits = len(self.number)
        self.lookup()
        self.build()

    def build(self):
        self.new = []

        if self.number == "1000":
            self.new = ["one thousand"]
        else:
            for digit_place in range(self.digits, 0, -1):
                self.new += [self.lookup_functions[digit_place]()]

        self.new = " ".join([x for x in self.new if x])

    def lookup(self):
        self.lookup_functions = {1: self.ones,
                                 2: self.tens,
                                 3: self.hundreds}

    def ones(self):
        try:
            if self.number[-2] == "1":
                return ""
            else:
                return f"{ones_mappings[self.number[-1]]}"
        except IndexError:
            return f"{ones_mappings[self.number[-1]]}"

    def tens(self):
        if self.number[-2] == "1":
            return f"{teens_mappings[self.number[-2:]]}"
        else:
            return f"{tens_mappings[self.number[-2]]}"

    def hundreds(self):
        if int(self.number[-2:]):
            return f"{ones_mappings[self.number[-3]]} hundred and"
        else:
            return f"{ones_mappings[self.number[-3]]} hundred"

    def thousand():
        pass


total = 0
for i in range(1, 1001):
    print(str(i), CountLetters(i).new)
    total += len("".join(CountLetters(i).new.split()))

print(total)
