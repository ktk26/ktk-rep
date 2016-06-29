def get_repeated_numbers():
	list_of_repeated_numbers=[]
	i=1
	for num in list_of_numbers:
		if num in list_of_numbers[i:(len(list_of_numbers))]:
			list_of_repeated_numbers.append(num)
		i=i+1
	print(list_of_repeated_numbers)
list_of_numbers = input()
get_repeated_numbers()
