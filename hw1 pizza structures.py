#a family of four is getting pizza. Each whole pizza has eight slices.
#Calculate how many whole pizzas needed and remaining slices left 
fam1 = int(input("enter how many slices eaten: "))
fam2 = int(input("enter how many slices eaten: "))
fam3 = int(input("enter how many slices eaten: "))
fam4 = int(input("enter how many slices eaten: "))
#whole pizzas needed. Each pizza equals 8
whole_pizza = 8 + 8
#remaining slices after pizza is eaten
remaining_slices = whole_pizza % (fam1 + fam2 + fam3 + fam4) 
#print how many how many slices from whole sliced remain
print ("After buying", whole_pizza,"slices of pizza" ,remaining_slices, "slices remained")
