age = 5
stuff = [True, False, 0, -1, "0", "1", "10", age<30, "20", "2", "5", "9001", "5.5"]
stuff.sort(key=float)
print(stuff)