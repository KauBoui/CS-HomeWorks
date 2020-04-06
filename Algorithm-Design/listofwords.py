wordfile = open("words.txt")
wordset = {word.strip() for word in wordfile.readlines()}

def isListOfWords(s):
    #write a O(N^2) algorithm to determine whether the string can be broken into a list of words
    #You can start by writing an exponential algorithm and then using dynamic programming to 
    #  improve the runtime complexity
    results = {}
    def memoization(s):
        if s in results: return results[s]
        if s in wordset:
            results[s] = True
            return True
        for i in range(len(s[1:])):
            if s[:i] in wordset and memoization(s[i:]):
                results[s[:i]] = True
                return True
        results[s] = False 
        return False 
    return memoization(s)
   

           
        
assert(isListOfWords("alistofwords"))
assert(isListOfWords("anotherlistofwords"))
assert(isListOfWords("stableapathydropon"))
assert(not isListOfWords("retouchesreissueshockshopbedrollsunspotassailsinstilledintersectionpipitreappointx"))
assert(not isListOfWords("xretouchesreissueshockshopbedrollsunspotassailsinstilledintersectionpipitreappoint"))

