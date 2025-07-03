import sys

args = sys.argv
n = len(args)

add = []
lst = []  # avoid using 'list' as a variable name, it shadows built-in

i = 1
while i < n:
    if args[i] == "add":
        i += 1
        s = ""
        while i < n and args[i] != "add" and args[i] != "list":
            s += " " + args[i]
            i += 1
        add.append(s.strip())
    elif args[i] == "list":
        i += 1
        s = ""
        while i < n and args[i] != "add" and args[i] != "list":
            s += " " + args[i]
            i += 1
        lst.append(s.strip())
    else:
        i += 1

print("Add:", add)
print("List:", lst)
