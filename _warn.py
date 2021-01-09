def Error(name, details, line_number, word_number, file): print(f"Error called (Most recent showed last):\n  File {file}:\n    Line {line_number}, word {word_number}:\n{name}: {details}")

def Warn(name, details, line_number="", word_number="", file=""): print(f"Warning (Most recent showed last):\n  File {file}:\n    Line {line_number}, word {word_number}:\n{name}: {details}\n\n")