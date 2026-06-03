with open('sample.txt') as file:
    content = file.read()
    
with open('user_file.txt', 'w') as file:
    file.write('User content')
    
print("File content: ")
print(content)
print("Done")
