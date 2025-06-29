#DAY 50

f = open('EgFile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# f = open('EgFile', 'w')
# lines = ['line1\n, line2\netc.']
# f.writelines(lines)
# f.close()

#DAY 51
with open('EgFile.txt', 'r') as f:
    print(type(f))
    f.seek(10)
    data = f.read(5)
    print(data)
    print(f.tell())

# with open('EgFile.txt', 'r') as f:
#     f.write('Hello World!')
#     f.truncate(5)

# with open('EgFile.txt', 'r') as f:
#     print(f.read())