
#The len() Function: Returns the length (number of items) of an object.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12] 
total_Lenght = len(my_list)
print(total_Lenght)


#The type() Function: Returns the type of an object.
print(type(42)) # Output: <class 'int’> 
print(type("Hello")) # Output: <class 'str'>
print(type(42.543)) # Output: <class 'float’> 

#The int() Function: Converts a value to an integer.
print(int("123")) # Output: 123 
print(int(4.56)) # Output: 4

#Function to Convert Binary to Decimal
convert_Binary_To_Decimal = int("1001", 2)
print("The Converted value is " + str(convert_Binary_To_Decimal))

#The float() Function: Converts a value to a floating-point number.
print(float("123.45")) # Output: 123.45 
print(float(4)) # Output: 4.0

#The str() Function: Converts a value to a string.
print(str(123)) # Output: '123’ 
print(str(4.56)) # Output: '4.56'

#The list() Function: Creates a list from an iterable.
my_tuple = (1, 2, 3) 
print(list(my_tuple))

#The dict() Function: Creates a dictionary. Dic comes with Key and Value
#Variable, List, Dictionary(Key,Value), Tupple
my_dict = dict(name="John", age=25) 
print(my_dict) # Output: {'name': 'John', 'age': 25}

#The sorted() Function: Returns a sorted list of the specified iterable..
my_list = [100, 3, 1, 4, 2, 54, 34, 33] 
print(sorted(my_list)) # Output: [1, 2, 3, 4]

#The sum() Function: Returns the sum of all items in an iterable.
my_list = [1, 2, 3, 4] 
print(sum(my_list)) # Output: 10

#The max() Function: Returns the largest item in an iterable or the largest of two or more arguments
my_list = [1, 2, 3, 4] 
print(max(my_list)) # Output: 4

#The min() Functions: Returns the smallest item in an iterable or the smallest of two or more arguments
my_list = [1, 2, 3, 4] 
print(min(my_list)) # Output: 1

#The abs() Functions: Returns the absolute value of a number
print(abs(-7))

#The round() Functions: Rounds a number to a specified number of decimal places.
print(round(3.14159, 2)) # Output: 3.14

#The filter() Function: Constructs an iterator from elements of an iterable for which a function returns true.
numbers = [1, 2, 3, 4, 5] 
even_numbers = filter(lambda x: x % 2 == 0, numbers) 
print(list(even_numbers)) # Output: [2, 4]

#The map() Function: Applies a function to all items in an iterable
numbers = [1, 2, 3, 4, 5] 
squared_numbers = map(lambda x: x ** 2, numbers) 
print(list(squared_numbers)) # Output: [1, 4, 9, 16, 25]









