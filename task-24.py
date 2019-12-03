k = (input())
a = k.strip()
b = reversed(a)

f = ''.join(b)
if a == b:
    print('True')
else:
    print('False')