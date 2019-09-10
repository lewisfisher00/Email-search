import re
import requests

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


def displayAll(key_values):
    key_values.sort(key=lambda x: -x[1])
    print(key_values)


# fileName = "sample.txt"
# with open(fileName) as file:
#     textData = file.read()

urlToRead = "https://www.bradonforest.org.uk/Contact-Us/"
textData = (requests.get(urlToRead)).text

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

matches = re.findall(r'\S+@(\w+[\.\w+]+)', textData)
domains = {}
for match in matches:
    domains[match] = domains.get(match, 0) + 1

key_values = []
for key_value_tup in domains.items():
    key_values.append(key_value_tup)

userChoice = input("1. Display all domains in file \n2. Display top 10 domains \n3. Set base frequency \n")
if userChoice == '1':
    displayAll(key_values)
if userChoice == '2':
    topTen(key_values)
if userChoice == '3':
    setFrequency(key_values)
