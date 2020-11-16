people = {
    'Matei': '0782622181',
    'Stefan': '0234534098',
    'Maria': '0567813970'
}

print(people)
buffer = {}
names = []
for x, y in people.items():
    names.append(x)
names.sort()
for i in range(len(names)):
    buffer[names[i]] = people[names[i]]
print (buffer)
