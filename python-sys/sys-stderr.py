import sys
def fun(*args):
    print(*args, file=sys.stderr)

fun("Hello World")