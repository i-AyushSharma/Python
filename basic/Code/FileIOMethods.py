f = open('EgFile', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# f = open('EgFile', 'w')
# lines = ['line1\n, line2\netc.']
# f.writelines(lines)
# f.close()