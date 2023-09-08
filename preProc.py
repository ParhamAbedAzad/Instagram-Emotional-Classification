import hazm
import emoji
stemmer = hazm.Stemmer()
fileName = "Stop_Words.txt"
f = open(fileName, "r", encoding="utf8")
stopWords = f.read().split("\n");
def proc(s):
    for c in emoji.UNICODE_EMOJI:
        s = s.replace(c," {} ".format(c))
    s = s.replace(" ","  ")
    arr = hazm.word_tokenize(s)
    for w in stopWords:
        arr = list(filter(w.__ne__, arr))
    
    return [stemmer.stem(w) for w in arr]
def removeEmojies(testing_set):
    for test in testing_set:
        for emo in emoji.UNICODE_EMOJI:
            if emo in test[0]:
                test[0][emo]=0
    return testing_set;                
            
