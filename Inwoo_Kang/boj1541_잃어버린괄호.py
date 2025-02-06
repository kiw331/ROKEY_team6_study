import re
text = '+' + input()

number = list(map(int, re.findall(r"\d+", text)))
sign = re.findall(r"\D", text)

i = 0
while i<len(sign) and sign[i] == '+':
    i += 1

print(sum(number[:i]) - sum(number[i:]))