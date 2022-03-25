msg = "Pay attention to everything I say"

words = msg.split()
print(words)

#split by a newline
msg = """\
Pay attention
to everything
I say"""

words = msg.split("\n")
print(words)