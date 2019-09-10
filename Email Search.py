import re


def setFrequency(key_values):
    freq = int(input("Enter base frequency:"))
    listToPrint = []
    for elem in key_values:
        if int(elem[1]) >= freq:
            listToPrint.append(elem)
    print(listToPrint)


def topTen(key_values):
    key_values.sort(key=lambda x: -x[1])
    print(key_values[0:10])


fileName = "sample.txt"
with open(fileName) as file:
    textData = file.read()

# counter = 0
# for i in range(len(textData)):
#     if textData[i: i + 13] == '@softwire.com':
#         counter = counter + 1
# print(counter)

# matches = re.findall(r'\S*@softwire.com$', textData)
# counter = 0
# for match in matches:
#     counter = counter + 1
# print(counter)

matches = re.findall(r'\S+@(\w+\.\S+)', textData)
domains = {}
for match in matches:
    domains[match] = domains.get(match, 0) + 1

key_values = []
for key_value_tup in domains.items():
    key_values.append(key_value_tup)

userChoice = input("1. Display top 10 domains \n2. Set base frequency \n")
if userChoice == '1':
    topTen(key_values)
if userChoice == '2':
    setFrequency(key_values)
