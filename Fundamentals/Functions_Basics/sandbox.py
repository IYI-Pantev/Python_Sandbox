# # If the number of arguments is unknown,
# # add a * before the parameter name:
#
# def my_function(*kids):
#     print("The youngest child is " + kids[2])
#
#
# my_function("Emil", "Tobias", "Linus")
#
#
# # #Keyword Arguments
# # You can also send arguments with the key = value syntax.
# #
# # This way the order of the arguments does not matter.
# #
# # Example
# def my_function(child3, child2, child1):
#     print("The youngest child is " + child3)
#
#
# my_function(child1="Emil", child2="Tobias", child3="Linus")
#
#
# # Default Parameter Value
# # The following example shows how to use a default parameter value.
# #
# # If we call the function without argument, it uses the default value:
# #
# # Example
# def my_function(country="Norway"):
#     print("I am from " + country)
#
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

n = [1, 2, 3]

odds = [x for x in n if x % 2 !=0]
print(odds)

