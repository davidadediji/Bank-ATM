# iterate through a 2D list

grades = [[10,25,13,45], [205], [70, 76, 49, 100]]

grades[1].append(67)
print(grades)

for inner_list in grades:
	for grade in inner_list:
		print(grade, end=" ")
	print()


def print_2d(grades):
	for inner_list in grades:
		for grade in inner_list:
			print(grade, end=" ")
		print()

print_2d(grades)
