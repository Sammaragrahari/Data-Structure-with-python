# l1 = ["great", "power", "comes","with","great","responsibilites"]
# ["Great","Power", "Comes","With","Great","Responsibilites"]
def upper(l1):
    res =[]
    if len(l1)==0:
        return res
    res.append(l1[0].title())
    return res+upper(l1[1:])
l1 = ["great", "power", "comes","with","great","responsibilites"]
print(l1)
print(upper(l1))
