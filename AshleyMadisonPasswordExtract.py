#Jonathan Poch
#CS 3923
testFile = open("Password Hashes/AshleyMadison.txt", 'r+')
for line in testFile.readlines():
    list = line.split(",")
    print(line.rstrip() + " " + list[3])
