# Create a Function
def reverse_string(s):
    string = ""
    for i in s:
        string = i + string
    return string


s = "Arun"
print("The original string is: ", end="")
print(s)
print("The reversed string(using loops) is: ", end="")
print(reverse_string(s))

# def reverse_string(string):
#     string = "Arun"
#     result = ""
#     for i in range(len(string)-1):
#         result += result[i]
#     return result
#     reversed_str = reverse_string(string)
#     print("Reversed string is: ", reversed_str)

# def reverse_string(input_string):
#     reversed_string = ""
#     for i in range(len(input_string) - 1, -1, -1):
#         reversed_string += input_string[i]
#     return reversed_string
#
#
# # Example usage:
# input_str = "Arun"
# reversed_str = reverse_string(input_str)
# print("Original string:", input_str)
# print("Reversed string:", reversed_str)
