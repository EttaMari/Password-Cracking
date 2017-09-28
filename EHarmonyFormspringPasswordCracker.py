#Jonathan Poch
#CS 3923
import hashlib
import itertools
import time

def cartesianProduct(length, validCharacters, flag=0):
    for attempt in itertools.product(validCharacters, repeat=length):
        if (flag == 1):
            md5Crack(''.join(attempt))
        else:
            sha256Crack(''.join(attempt))

def sha256Crack(guess):
    #5
    for x in range(0,100):
        saltedGuess = str(x).zfill(2) + guess
#        print(saltedGuess)
        hash = hashlib.sha256(saltedGuess.encode('utf-8')).hexdigest()
#        print(hash)
        if hash in formspringPasswords:
            print("PASSWORD CRACKED!\n" + hash + " : " + guess)

def md5Crack(guess):
    #8-14
#    print(guess)
    hash = hashlib.md5(guess.encode('utf-8')).hexdigest()
#    print(hash)
    if hash in eHarmonyPasswords:
        print("PASSWORD CRACKED!\n" + hash + " : " + guess)

def tryBruteForce(length, flag=0):
    print("Trying brute force...")

    numbers = "0123456789"
    upperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lettersAndNumbers = upperCaseLetters + numbers
    lowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"
    symbols = ",./<>?;':\"[]\{}|`~!@#$%^&*()_+"
    all = lowerCaseLetters + upperCaseLetters + numbers + symbols
    
    start = time.clock()
    cartesianProduct(length, numbers, flag)
    end = time.clock()
    print(str(end - start) + " seconds")

    start = time.clock()
    cartesianProduct(length, upperCaseLetters, flag)
    end = time.clock()
    print(str(end - start) + " seconds")

    start = time.clock()
    cartesianProduct(length, lettersAndNumbers, flag)
    end = time.clock()
    print(str(end - start) + " seconds")

    if (flag==0):
        start = time.clock()
        cartesianProduct(length, lowerCaseLetters, flag)
        end = time.clock()
        print(str(end - start) + " seconds")

        start = time.clock()
        cartesianProduct(length, all, flag)
        end = time.clock()
        print(str(end - start) + " seconds")

def tryWordList(wordList, flag=0):
    print("Trying word list...")
#    words = [line.strip() for line in wordList]
    words = (line.rstrip('\n') for line in open(wordList))

#    print(words)
    start = time.clock()
    for word in words:
        if (flag == 1):
            md5Crack(word.upper())
        else:
            sha256Crack(word)
            sha256Crack(word.upper())
    end = time.clock()
    print(str(end - start) + " seconds")

def tryWordListWithColors(wordList, flag=0):
    print("Trying word list with colors...")
    colors = ["red","orange","yellow","green","blue","purple","violent","gold","silver","magenta","white","black","grey","gray","brown", "maroon","pink"]
#    words = [line.strip() for line in wordList]
    words = (line.rstrip('\n') for line in open(wordList))

    #    print(words)
    start = time.clock()
    for word in words:
        if (flag == 1):
            for color in colors:
                md5Crack(color.upper() + word.upper())
        else:
            for color in colors:
                sha256Crack(color + word)
                sha256Crack(color.upper() + word.upper())

    end = time.clock()
    print(str(end - start) + " seconds")

def tryEHarmonyPasswordsForFormspring():
    eHarmonyPasswordCracks = ["419INTERNET419","ZOMBIE247","BLACKVAN","JADA8140","MADELYN091","7600BLOCK","NORTH0101","BUFFALO9541","ELISE2103","JESSE2359","MARISA0212"]
    
    start = time.clock()
    for password in eHarmonyPasswordCracks:
        sha256Crack(password.lower())
        sha256Crack(password.upper())
    end = time.clock()
    print(str(end - start) + " seconds")

def tryWordListWithNumbers(wordList, flag=0):
    print("Trying word list with numbers...")
#    words = [line.strip() for line in wordList]
    words = (line.rstrip('\n') for line in open(wordList))


#    print("There are " + str(len(words)) + " words.")

    start = time.clock()
    for word in words:
        for x in range(0,1000):
            if (flag==1):
                md5Crack(word.upper())
                md5Crack(str(x) + word.upper())
                md5Crack("0" + str(x) + word.upper())
                md5Crack(str(x) + word.upper() + str(x))
                md5Crack("0" + str(x) + word.upper() + str(x))
                md5Crack("0" + str(x) + word.upper() + "0" + str(x))
                md5Crack(word.upper() + str(x))
                md5Crack(word.upper() + "0" + str(x))
            else:
                sha256Crack(word)
                sha256Crack(str(x) + word)
                sha256Crack("0" + str(x) + word)
                sha256Crack(str(x) + word + str(x))
                sha256Crack("0" + str(x) + word + str(x))
                sha256Crack("0" + str(x) + word + "0" + str(x))
                sha256Crack(word + str(x))
                sha256Crack(word + "0" + str(x))
                sha256Crack(word)
                sha256Crack(str(x) + word.upper())
                sha256Crack("0" + str(x) + word.upper())
                sha256Crack(str(x) + word.upper() + str(x))
                sha256Crack("0" + str(x) + word.upper() + str(x))
                sha256Crack("0" + str(x) + word.upper() + "0" + str(x))
                sha256Crack(word.upper() + str(x))
                sha256Crack(word.upper() + "0" + str(x))
#            for y in range(0,1000):
#                md5Crack(str(x) + word.upper() + str(y))
    end = time.clock()
    print(str(end - start) + " seconds")

def tryWordListWithColorsAndNumbers(wordList, flag=0):
    colors = ["red","orange","yellow","green","blue","purple","violent","gold","silver","magenta","white","black","grey","gray","brown", "maroon","pink"]
    print("Trying word list with colors and numbers...")
    #    words = [line.strip() for line in wordList]
    words = (line.rstrip('\n') for line in open(wordList))
    
    
    #    print("There are " + str(len(words)) + " words.")
    
    start = time.clock()
    for word in words:
        for x in range(0,10000):
            for color in colors:
                if (flag==1):
                    md5Crack(color.upper() + word.upper())
                    md5Crack(color.upper() + str(x) + word.upper())
                    md5Crack(color.upper() + "0" + str(x) + word.upper())
                    md5Crack(color.upper() + str(x) + word.upper() + str(x))
                    md5Crack(color.upper() + "0" + str(x) + word.upper() + str(x))
                    md5Crack(color.upper() + "0" + str(x) + word.upper() + "0" + str(x))
                    md5Crack(color.upper() + word.upper() + str(x))
                    md5Crack(color.upper() + word.upper() + "0" + str(x))
                else:
                    sha256Crack(color + word)
                    sha256Crack(color + str(x) + word)
                    sha256Crack(color + "0" + str(x) + word)
                    sha256Crack(color + str(x) + word + str(x))
                    sha256Crack(color + "0" + str(x) + word + str(x))
                    sha256Crack(color + "0" + str(x) + word + "0" + str(x))
                    sha256Crack(color + word + str(x))
                    sha256Crack(color + word + "0" + str(x))
                
                    sha256Crack(color.upper() + word)
                    sha256Crack(color.upper() + str(x) + word.upper())
                    sha256Crack(color.upper() + "0" + str(x) + word.upper())
                    sha256Crack(color.upper() + str(x) + word.upper() + str(x))
                    sha256Crack(color.upper() + "0" + str(x) + word.upper() + str(x))
                    sha256Crack(color.upper() + "0" + str(x) + word.upper() + "0" + str(x))
                    sha256Crack(color.upper() + word.upper() + str(x))
                    sha256Crack(color.upper() + word.upper() + "0" + str(x))
    #            for y in range(0,1000):
#                md5Crack(str(x) + word.upper() + str(y))
    end = time.clock()
    print(str(end - start) + " seconds")

def tryWordListWithCartesianProduct(wordList, flag=0):
    print("Trying word list with cartesian product...")
    
#    words = [line.strip() for line in wordList]
    words = (line.rstrip('\n') for line in open(wordList))

    
    #    print("There are " + str(len(words)) + " words.")
    
    start = time.clock()
    for combination in itertools.product(words,words):
        if (flag == 1):
            md5Crack(''.join(combination).upper())
        else:
            sha256Crack(''.join(combination))
            sha256Crack(''.join(combination).upper())
    end = time.clock()
    print(str(end - start) + " seconds")


eHarmonyFile = open("Password Hashes/eHarmony.txt", 'r')
eHarmonyPasswords = [line.strip() for line in eHarmonyFile]

formspringFile = open("Password Hashes/formspring.txt", 'r')
formspringPasswords = [line.strip() for line in formspringFile]


#tryBruteForce(8)
#tryBruteForce(9)
#tryBruteForce(10)
#tryBruteForce(11)
#tryBruteForce(12)
#tryBruteForce(13)
#tryBruteForce(14)

wordListJohn = "Word Lists/john.txt"
wordListNames = "Word Lists/NAMES.DIC"
wordListLarge = "Word Lists/LARGE.DIC"
wordListPassword = "Word Lists/common-passwords.txt"


#tryBruteForce(6)

#########################
# MD5 Attempts          #
#########################
tryWordList(wordListJohn,1)
tryWordList(wordListNames,1)
tryWordList(wordListLarge,1)
tryWordList(wordListPassword,1)

tryWordListWithColors(wordListJohn,1)
tryWordListWithColors(wordListNames,1)
tryWordListWithColors(wordListLarge,1)
tryWordListWithColors(wordListPassword,1)

tryWordListWithNumbers(wordListJohn,1)
tryWordListWithNumbers(wordListNames, 1)
tryWordListWithNumbers(wordListLarge, 1)
tryWordListWithNumbers(wordListPassword, 1)

tryWordListWithColorsAndNumbers(wordListJohn,1)
tryWordListWithColorsAndNumbers(wordListNames, 1)
tryWordListWithColorsAndNumbers(wordListLarge, 1)
tryWordListWithColorsAndNumbers(wordListPassword, 1)
#
#tryWordListWithCartesianProduct(wordListJohn, 1)
#tryWordListWithCartesianProduct(wordListNames, 1)
#tryWordListWithCartesianProduct(wordListLarge, 1)
#tryWordListWithCartesianProduct(wordListPassword, 1)

#########################
# SHA256 Attempts       #  #rather slow...uncomment if needed
#########################
tryEHarmonyPasswordsForFormspring()

tryWordList(wordListJohn)
tryWordList(wordListNames)
tryWordList(wordListLarge)
tryWordList(wordListPassword)
#
#tryWordListWithColors(wordListJohn)
#tryWordListWithColors(wordListNames)
#tryWordListWithColors(wordListLarge)
#tryWordListWithColors(wordListPassword)
#
#tryWordListWithNumbers(wordListJohn)
#tryWordListWithNumbers(wordListNames)
#tryWordListWithNumbers(wordListLarge)
#tryWordListWithNumbers(wordListPassword)
#
#tryWordListWithColorsAndNumbers(wordListJohn)
#tryWordListWithColorsAndNumbers(wordListNames)
#tryWordListWithColorsAndNumbers(wordListLarge)
#tryWordListWithColorsAndNumbers(wordListPassword)
#
#tryWordListWithCartesianProduct(wordListJohn)
#tryWordListWithCartesianProduct(wordListNames)
#tryWordListWithCartesianProduct(wordListLarge)
#tryWordListWithCartesianProduct(wordListPassword)

eHarmonyFile.close()


