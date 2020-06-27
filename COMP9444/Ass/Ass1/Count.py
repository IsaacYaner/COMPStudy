string = 'The quick brown fox jumped over the lazy dog'
count = 1
for i in string:
    if i == ' ':
        count += 1
print(count)