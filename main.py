user_input = input('Enter some text: ')

with open('sample.txt') as file:
    content = file.read()
    
with open('user_file.txt', 'w') as file:
    file.write(user_input)
    
print("File content: ")
print(content)
print("Done")
