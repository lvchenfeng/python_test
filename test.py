def g(n):
    for i in range(n):
        yield i **2
for i in g(5):
    print(str(i)+":")