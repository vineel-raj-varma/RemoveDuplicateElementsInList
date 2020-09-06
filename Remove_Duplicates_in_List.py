def remove(arr):
	lis = []
	for num in arr:
		if num not in lis:
	 		lis.append(num)
	return print(lis)	
			
arr = ['0', '2', '2','3', '4', '5', '5', '5', '6', '6', '8', '8', '9']					
remove(arr)

new_set = set(arr)
print(new_set)

# If input is ['0', '2', '2','3', '4', '5', '5', '5', '6', '6', '8', '8', '9']
# Output will be ['0', '2', '3', '4', '5', '6', '8', '9']