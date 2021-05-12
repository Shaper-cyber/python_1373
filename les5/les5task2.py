example_1 = open("C:/Users/Damir/Desktop/Example.txt", 'r', encoding="UTF-8")
i = 0
for j in example_1.readlines():
    i += 1
print(i)
example_1.seek(0, 0)
a1 = 0
a2 = 0
a3 = 0

for s1 in example_1.readline():
    if s1 == " ":
        a1 += 1
a1 += 1
print(a1)
for s2 in example_1.readline():
    if s2 == " ":
        a2 += 1
a2 += 1
print(a2)

for s3 in example_1.readline():
    if s3 == " ":
        a3 += 1
a3 += 1 
print(a3)

example_1.close()
