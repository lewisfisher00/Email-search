import re
fileName = "sample.txt"
with open(fileName) as file:
    textData = file.read()

# counter = 0
# for i in range(len(textData)):
#     if textData[i: i + 13] == '@softwire.com':
#         counter = counter + 1
# print(counter)

# matches = re.findall('\S*@softwire.com', textData)
# for match in matches:
#     print(match)

