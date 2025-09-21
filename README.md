muffin = 10
cupcake = 10
buying = input("Do you want a muffin or cupcake?: ")

while buying != "0":
    if buying == "muffin" and muffin > 0:
        muffin = muffin - 1
        if buying == 'muffin' and muffin == 0:
            print('Muffin out of stock')


    if buying =="cupcake" and cupcake > 0:
        cupcake = cupcake - 1
    if buying == 'cupcake' and cupcake == 0:
             print("cupcake is out of stock")
    buying = input(' Do you want a muffin or cupcake: ')
print("muffin", muffin, "cupcake", cupcake)
#You want 9 muffins reamining and 3 cupcakes left
