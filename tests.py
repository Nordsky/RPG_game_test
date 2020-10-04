path_first = 'loc/location/test_loc.txt'
a = []          # main mas
f = open(path_first)
m = len(f.readlines())      # len file
f.seek(0)
for li in f:
    a.append(li)
x = int(a[m-5])
y = int(a[m-4])

print(a[3+y*2 + 2][3])
