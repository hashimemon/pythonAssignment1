L=[]
def shoppingCart(*items):
    for i in items:
        L.append(i)
        print("You bought:",i)
    print('\nYour Shopping List are/is:',L)
shoppingCart("Shirt","Touser","Shoes","Toys","Sweater")
