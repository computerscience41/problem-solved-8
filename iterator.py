string = "Hello"
iterator = iter(string)

while True:
    try:
        char = next(iterator)
        print(char)
    except StopIteration:
        break
