old_word = input("Enter word to search: ")
new_word = input("Enter new word: ")

f = open("input.txt", "r")
data = f.read()
f.close()

data = data.replace(old_word, new_word)

f2 = open("output.txt", "w")
f2.write(data)
f2.close()

print("word Replaced")
