# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583

# programing task --

def substr(str, keyword):
  index = str.find(keyword)
  return index

# #  Example
# # should print: `17`
print(substr("this is what I'm searching in", "searching"))

# # should print: `-1`
print(substr("this is what I'm searching in", "not"))