def find_duplicates(items1, items2):
    a = set(items1).intersection(items2)
    b = list(a)
    return b
print(find_duplicates([1,2,3],[3,4,5]))
print(find_duplicates(["dog", "cat"], ["cat", "giraffe"]))
