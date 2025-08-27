print("Safe File Reader")
print("=" * 40)

while True:
    filename = input("Please enter a filename to read: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        print(f"Success! Contents of '{filename}':")
        print("=" * 40)
        print(content)
        print("=" * 40)
        break
        
    except FileNotFoundError:
        print(f"Oops! '{filename}' doesn't exist.")
        print("Please check the spelling and try again.\n")
        
    except:
        print(f"Something went wrong with '{filename}'.")
        print("Maybe the file is corrupted or you don't have permission.\n")
    
    try_again = input("Try another file? (yes/no): ").lower()
    if try_again not in ['yes', 'y']:
        print("Goodbye!")
        break
