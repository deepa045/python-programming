char=raw_input()
def reverse(char):
  str = ""
  for i in char:
    str = i + str
  print str
reverse(char)
