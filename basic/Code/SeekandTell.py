#Seek

with open('EgFile.txt', 'r') as f:
    print(type(f))
    f.seek(10) #Move to the 10th byte in the file

    data = f.read(5) #Read the next 5 Bytes
    print(data)

#Tell

    current_position = f.tell()
    print(current_position)
    
#Trunkate

    # with open('EgFile.txt', 'w') as f:
#     f.write('Hello World!')
#     f.truncate(5) 