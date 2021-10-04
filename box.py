def boxprint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception('Width and height should be greater than 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

a = input('Enter Symbol')
b = int(input('Enter width'))
c = int(input('Enter height'))
boxprint(a, b, c)

