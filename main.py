try:
    with open('sample.txt') as file:
        content = file.read()
        
    print("File content: ")
    print(content)
    print("Done")
    
    user_input = input('Enter some text: ')

    with open('user_file.txt', 'w') as file:
        file.write(user_input)


except FileNotFoundError:
    print("Error: file is not found")    
