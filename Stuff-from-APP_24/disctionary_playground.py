import itertools 
my_list = ["a", "A", "c", "C", "d", "D", "e", "E"]
print(type(my_list))

#convert list into iterator
my_list_iter = iter(my_list) 

print(type(my_list_iter))

my_list_dict_object = itertools.zip_longest(my_list_iter, my_list_iter, fillValue=None)

my_list_dict = dict(my_list_dict_object)

print(my_list_dict)