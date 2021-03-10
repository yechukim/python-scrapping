import re

p = re.compile("^appl")

def print_match(m):
  if m:
    print("m.group():", m.group())
    print("m.string:", m.string)
    print("m.start():", m.start())
    print("m.end():", m.end())
    print("m.span()", m.span())
  else :
    print("not matched! :'(")

# m = p.match("eee")
# print_match(m)

li = p.findall("apple")
print(li)
