from Parse import Parse
from sys import argv
run = ""
run_is_Declared = False

for i in argv:
    if i == "-p":
        run = argv[argv.index(i) + 1]
        run_is_Declared = True
if not run_is_Declared:
    run = argv[1]

with open(run) as f:
    content = f.read()
    parser = Parse(content)
    exec(parser.Value())