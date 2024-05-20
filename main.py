string = input("Enter a string: ")
list = list(string)
if len(list) <= 140:
    print(list)
else:
    print("Too long!")
string = new_string = string.title()
new_string = ""
for char in string:
    if char != " ":
        new_string += char
print(new_string)
new_string = new_string.title()
print('#' + new_string.title())

#new_string = string.title()
#print(new_string)
#print('#' + string.title())
#print('#' + ''.join(filter(str.isalnum, input().title))[:140])