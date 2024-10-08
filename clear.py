list1 = []
us = int(input("reapeted times: "))

for i in range(us):
    use = input("names: ")
    list1.append(use)

print(list1)

user = input("Clear list? type clear is yes: ").lower()

if user == "clear":
    list1.clear()
    print(list1)