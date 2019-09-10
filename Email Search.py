import re
fileName = "sample.txt"
with open(fileName) as file:
    textData = file.read()

# counter = 0
# for i in range(len(textData)):
#     if textData[i: i + 13] == '@softwire.com':
#         counter = counter + 1
# print(counter)

# matches = re.findall('\S*@softwire.com$', textData)
# counter = 0
# for match in matches:
#     counter = counter + 1
# print(counter)

matches = re.findall(r'\S+@(\w+\.\S+)', textData)
domains = {}
for match in matches:
    domains[match] = domains.get(match, 0) + 1

print(domains)
