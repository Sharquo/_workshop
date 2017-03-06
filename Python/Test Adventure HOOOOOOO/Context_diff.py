import difflib

diff = difflib.context_diff(open("Testdata1.las").readlines(), open("Testdata2.las").readlines())

with open("Results.txt", 'w') as file:
    count_lines = 0
    for line in diff:
        file.write(line)
        count_lines += 1
    if count_lines == 0:
        file.write("\n ----- NO DIFF ----- \n")
    else:
        pass