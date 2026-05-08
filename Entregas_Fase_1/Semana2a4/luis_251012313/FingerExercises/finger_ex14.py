print("Question 1:\n");
def keys_with_value(aDict, target):
    return sorted([k for k, v in aDict.items() if v == target]);

aDict = {1:2, 2:4, 5:2};
target = 2;
print(keys_with_value(aDict, target));

print("\nQuestion 2:\n");
def all_positive(d):
    return sorted([k for k, v in d.items() if sum(v) > 0]);

d = {5:[2, -4], 2:[1, 2, 3], 1:[2]};
print(all_positive(d));