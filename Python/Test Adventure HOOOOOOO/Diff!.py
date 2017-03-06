import difflib

diff = difflib.context_diff(open("Testdata1.las").readlines(), open("Testdata2.las").readlines())

try:
    while 1:
        print diff.next(),
except:
    print "NO DIFF"

