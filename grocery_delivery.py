import grocery_functions as gf
Groceries = []
Clothes = []
Electronics = []
Books = []

print("Welcome to your Shopping List!")
print("Enter and item and its category to add it to the list, say done to finish adding items")
finish = True

while finish:
    item = input("Add an item to the shopping list: ")
    category = input("What category do you want to put that in? (Groceries, Clothes, Electronics, Books): ")
    if category == "groceries" or category == "Groceries":
        gf.addItem(Groceries, item)
    if category == "clothes" or category == "Clothes":
        gf.addItem(Clothes,item)
    if category == "electronics" or category == "Electronics":
        gf.addItem(Electronics, item)
    if category == "Books" or category == "books":
        gf.addItem(Books, item)
    if item == "done":
        finish = False
    
    
gf.printAll(Groceries, Clothes, Electronics, Books)
 
removei = input("Enter an item you want to remove from the shopping list: ")
removecategory = input("Enter the category: ")

if removecategory == "groceries" or removecategory == "Groceries":
    gf.removeItem(Groceries, removei)
if removecategory == "clothes" or removecategory == "Clothes":
    gf.removeItem(Clothes,removei)
if removecategory == "electronics" or removecategory == "Electronics":
    gf.removeItem(Electronics, removei)
if removecategory == "Books" or removecategory == "books":
    gf.removeItem(Books, removei)
else:
    print("Error, this category or item doesn't exist")
print()
gf.printAll(Groceries, Clothes, Electronics, Books)
print()


searchitem = input("Enter an item you want to search for in the shopping list: ")
searchcategory = input("Enter the category: ")
print("*Note the list starts at 0")
print()
#print out index if the item and category exists, and error if it doesn't 
if searchcategory == "groceries" or searchcategory == "Groceries":
    index = gf.search(Groceries, searchitem)
    i = print("The item number is #" + str(gf.search(Groceries, searchitem)) + " in the list Groceries")
    if index < 0:
        print("Error, this item does not exist")
if searchcategory == "clothes" or searchcategory == "Clothes":
    index = gf.search(Clothes, searchitem)
    i = print("The item number is #" + str(gf.search(Clothes, searchitem)) + " in the list Clothes")
    if index < 0:
        print("Error, this item does not exist")
if searchcategory == "electronics" or searchcategory == "Electronics":
    index = gf.search(Electronics, searchitem)
    i = print("The item number is #" + str(gf.search(Electronics, searchitem)) + " in the list Electronics")
    if index < 0:
        print("Error, this item does not exist")
if searchcategory == "Books" or searchcategory == "books":
    index = gf.search(Books, searchitem)
    i = print("The item number is #" + str(gf.search(Books, searchitem)) + " in the list Books")
    if index < 0:
        print("Error, this item does not exist")


print()
print("Now sorting your list")
print()
gf.sortCategories(Groceries, Clothes, Electronics, Books)
gf.printAll(Groceries, Clothes, Electronics, Books)


