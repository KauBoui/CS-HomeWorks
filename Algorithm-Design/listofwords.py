wordfile = open("words.txt")
wordset = {word.strip() for word in wordfile.readlines()}

def isListOfWords(s):
    #write a O(N^2) algorithm to determine whether the string can be broken into a list of words
    #You can start by writing an exponential algorithm and then using dynamic programming to 
    #  improve the runtime complexity
    #global temp
    #global temp2 
    #i = len(s) - 1
    #while i >= 0:
    #    if len(s) == 0:
    #        print("It do be 0")
    #        return True
    #    print("i is:", i)
    #    temp = s[i] + temp
    #    i = i - 1 
    #    print(temp)
    #    if temp in wordset:
    #        s = s[:i + 1]
    #        for j in reversed(range(len(s))):
    #            temp2 = s[j] + temp2
    #            print("temp2 do be", temp2)
    #            if temp2 + temp in wordset:
    #                temp = temp2 + temp
    #                print("temp2 do be", temp2)
    #                s = s[:j]
    #                i = j
    #                break
    #        temp2 = ""
    #        temp = ""
    #        print(s)
    #        isListOfWords(s)
    if len(s) == 0:
            print("if statement")
            return True
    temp = ""
    i = len(s) - 1
    while i >= 0:
        temp = s[i] + temp
        print("temp: " , temp)
        if temp in wordset:
            s = s[:i]
            temp2 = s
            print("first s: ", s)
            for j in range(len(temp2)):
                print("temp2: ", temp2)
                if temp2 + temp in wordset:
                    print("temp2+temp: ", temp2 + temp)
                    cut_point = len(temp2)
                    print("cut_point: ", cut_point)
                    s = s[:-cut_point]
                    print("slen: ", len(s))
                    print("s: ", s)
                    print("temp2 sliced: ", temp2)
                    i = j
                    break
                temp2 = temp2[1:]
            isListOfWords(s)
        i = i - 1
    return False

#assert(isListOfWords("alistofwords"))
#assert(isListOfWords("anotherlistofwords"))
assert(isListOfWords("stableapathydropon"))
assert(not isListOfWords("retouchesreissueshockshopbedrollsunspotassailsinstilledintersectionpipitreappointx"))
assert(not isListOfWords("xretouchesreissueshockshopbedrollsunspotassailsinstilledintersectionpipitreappoint"))

