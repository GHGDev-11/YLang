from _warn import Warn

class String:
    def __init__(self, line):
        self.string = ""
        in_string = False
        quote = ""
        unquote = ""

        for char in line:
            if char in ["'", '"', "`"] and not in_string: # "`" is optional, i just added it so there's 3 types of quotes.
                in_string = True
                quote = char
            elif char != quote and in_string:
                self.string += char
            elif char == quote and in_string:
                unquote = char
                break

        if quote and not unquote:
            Warn("UnquoteWarning", "Did not find unquote character, cut off string at end of line.", 1, 0, '"<string>"')
    
    def Value(self):
        return self.string