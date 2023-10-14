# Topic 11
# Task 1

with open('myfile.txt', 'w') as file:
    file.write("Hello file world")
print("File 'myfile.txt' created successfully")

try:
    with open('myfile.txt', 'r') as file:
        content = file.read()
        print(f"File content: {content}")
except FileNotFoundError:
    print(f"File 'myfile.txt' not found.")
except Exception as e:
    print(f"En error occurred: {e}")

# python .\second\homework_011.py
# python .\second\myfile.txt


