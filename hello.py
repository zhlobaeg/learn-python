import random

f = [ '🤣haha', '😢:-( sad', '😍love', '😎cool', '😒boring' ]

for i in range(1000):
    result = f[random.randrange(0, 4)]
    print(result)