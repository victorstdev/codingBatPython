def front_back(str):
  newStr = str[-1] + str[1:-1] + str[0]
  return newStr

print(front_back('teste'))