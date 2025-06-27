# READING A FILE

f = open('EgFile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()

# a = open('xfile', 'w') Opening a file which does not exist in write mode will create a new file named upon what you entered in the file's space

# WRITTING A FILE

f = open('EgFile.txt', 'w')
f.write("Chasing Light\nIn morning's hush, the sun awakes,/nAnd dances on the silver lakes.\nA whisper in the drifting breeze,\nA secret told by swaying trees.\n\nWe chase the light, we dream, we grow,\nThrough highs and lows we come to know—\nThat even stars must fade to night,\nTo rise again with morning light.")
f.close()

f = open('EgFile.txt', 'a')
f.write('\nWow!, Hello Ayush.\nHow are you?')
f.close()

with open('EgFile.txt', 'r') as f: # With this command we can skip the close process
    f.read()