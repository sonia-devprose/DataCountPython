# Define square function to square numbers
def square(x):
	return x * x
# Define lambda function multiply to multiply two numbers
multiply = lambda a,b : a*b
# Define a list
list = [1,2,3,4,5]
# Create a new list of squares of previous list
new_list = [square(num)for num in list]
print(new_list)
# Define tuple
my_tuple = (10,20,30)
print(my_tuple)
# Define new integers to count the number of times they appear in the list
integer_list = [23, 45, 44, 56, 45, 23, 56, 44, 23]
# import statement to refer libraries, classes, modules, etc.
from  collections import Counter
# Apply Counter  class
final_count = Counter(integer_list)
print(final_count)
