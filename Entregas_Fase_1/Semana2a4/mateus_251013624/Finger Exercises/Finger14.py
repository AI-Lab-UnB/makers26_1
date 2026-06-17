#Questão 1

print("Questão 1:\n")
def keys_with_value(d,target):
    return sorted([k for k, i in d.items() if i == target])

aDict = {1:2, 2:4, 5:2}
target = 2
print(keys_with_value(aDict, target)) # prints the list [1,5]

#Questão 2

def all_positive(d):
    return sorted([k for k, i in d.items() if sum(i) > 0])

print("\nQuestão 2:\n")
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]