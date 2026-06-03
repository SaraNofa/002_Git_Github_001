with open('sample.txt') as file:
    content = file.read()
    
content_capitalized = content.upper()
print(content_capitalized)