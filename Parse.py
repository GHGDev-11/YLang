from _strings import String

class Parse:
    def __init__(self, code):
        self.outcome = ""
        self.ln = 0
        self.wn = 0
        self.reserved = [
            "print",
            "input"
        ]

        for line in code.split("\n"):
            self.ln += 1
            for word in line.split(" "):
                self.wn += 1

                if word in self.reserved:
                    string = String(line).Value()
                    self.outcome += {
                        "print": f'print("""{string}""")\n',
                        "input": f'input("""{string}""")\n'
                    }.get(word, "")
    
    def Value(self):
        return self.outcome