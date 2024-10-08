list1 = []
us = int(input("Repeated times: "))

for i in range(us):
    use = input("Number: ")
    list1.append(use)

print("Initial list:", list1)

wow = input("WOW: ")

if wow in list1:
    list1.remove(wow)
else:
    print("{wow} is not in the list.")

print("Updated list:", list1)
