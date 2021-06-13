# program to rreplace the char in the string
str = input("enter the string")
index, char = input("enter the index and character to be change").split()
string_list = list(str)
string_list[int(index)] = char
new_string = "".join(string_list)
print(new_string)
