backpack = ['pizza slice', "button", "pizza slice", "fishing pole",
"pizza slice", "nunchicks", "sandwich from mcdonalds"]


while backpack.count("pizza slice")>0:
	backpack.remove('pizza slice')

print(backpack)

#note this isn't a scalable solution for a list since it is a loop and it checks the items repetitively
#there are better algorithmic technique to solving this.
