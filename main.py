string = input("Enter a string: ")
if len(string) <= 140:
    print(string)
else:
    print("Too long!")
string = new_string = string.title()
new_string = ""
for char in string:
    if char != " ":
        new_string += char
print(new_string)
new_string = new_string
print('#' + new_string)

#new_string = string.title()
#print(new_string)
#print('#' + string.title())
#print('#' + ''.join(filter(str.isalnum, input().title))[:140])