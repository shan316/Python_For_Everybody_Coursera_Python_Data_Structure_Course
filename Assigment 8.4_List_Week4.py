fname = input('Enter the file name: ')
fhand = open(fname)
words_list = []
for line in fhand:
    words = line.split()
    for word in words:
        if word in words_list: 
            continue
        words_list.append(word)
print(sorted(words_list))
