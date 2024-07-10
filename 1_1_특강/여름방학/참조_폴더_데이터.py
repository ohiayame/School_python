import os

# Relative reference
f_handler = open("foo/test.txt", "r")

# Absolute reference
# f_handler = open(r"c:/foo/test.txt", "r")

msg = f_handler.read()

print(msg)

f_handler.close()