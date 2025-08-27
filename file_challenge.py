print(" Welcome to File Processor!")
print("=" * 40)

with open('input.txt', 'w') as file:
    file.write("Hello! This is a text file.\n")
    file.write("Python makes file handling easy.\n")
    file.write("We are learning to read and write files.\n")
    file.write("This is the fourth line of text.\n")
    file.write("And this is the fifth line.\n")

print(" input.txt created successfully!")

with open('input.txt', 'r') as file:
    text = file.read()

print("File read successfully!")

words = text.split()
word_count = len(words)
print(f" Found {word_count} words in the file")

uppercase_text = text.upper()

with open('output.txt', 'w') as file:
    file.write("UPPERCASE TEXT:\n")
    file.write("=" * 30 + "\n")
    file.write(uppercase_text)
    file.write("=" * 30 + "\n")
    file.write(f"\nTotal words: {word_count}\n")

print("output.txt created successfully!")
print(" All done! Check your files:")
print("   - input.txt (original text)")
print("   - output.txt (uppercase text + word count)")
