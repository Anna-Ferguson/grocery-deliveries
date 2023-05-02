

def printAll(list1, list2, list3, list4):
    print("Groceries")
    print(list1)
    print()
    print("Clothes")
    print(list2)
    print()
    print("Electronics")
    print(list3)
    print()
    print("Books")
    print(list4)
    print()

def addItem (list, item):
    list.append(item)

def sortCategories(list1, list2, list3, list4):
    list1.sort()
    list2.sort()
    list3.sort()
    list4.sort()

def removeItem(list, item):
    list.remove(item)

def search(list, item):
    for index in range(0,len(list)):
        if item == list[index]:
            return index
    return -1



     
        


