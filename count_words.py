path = './music.txt'
f =  open(path, 'r')
data = f.read()
data = data.split()

result = {}
for word in data:
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

for key in result:
    print(key, result[key])