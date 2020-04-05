wordfile = open("words.txt")
wordset = {word.strip() for word in wordfile.readlines()}


def isListOfWords(s):
    #write a O(N^2) algorithm to determine whether the string can be broken into a list of words
    #You can start by writing an exponential algorithm and then using dynamic programming to 
    #  improve the runtime complexity
    if len(s) == 0:
        return True
    pos_words = []
    for i in range(len(s)):
        to_look = ""
        to_look = s[i]
        if to_look in wordset:
            pos_words.append(to_look)
        for j in range(len(s) - (i + 1)):
            to_look += s[j + i + 1]
            if to_look in wordset:
                pos_words.append(to_look)
            print("scanneded:", to_look)
    print("words in string:" , pos_words)

           
        
assert(isListOfWords("alistofwords"))
assert(isListOfWords("anotherlistofwords"))
assert(isListOfWords("stableapathydropon"))
assert(not isListOfWords("retouchesreissueshockshopbedrollsunspotassailsinstilledintersectionpipitreappointx"))
assert(not isListOfWords("xretouchesreissueshockshopbedrollsunspotassailsinstilledintersectionpipitreappoint"))


