a = input("Enter your message: ")
choice = int(input("Enter 1 to code or 0 to decode: "))
words = a.split(" ")            
coding = True if (choice == 1) else False
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            prefix = "dawg"
            suffix = "bait"
            anew = prefix + word[1:] + word[0] + suffix
            nwords.append(anew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            anew = word[3:-3]
            anew = anew[-1] + anew[:-1]
            nwords.append(anew)
        else:
            nwords.append(word[:-1])
    print(" ".join(nwords))