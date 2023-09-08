import pickle
import CustomMNB
import preProc
test = open("C:\\Users\\FarazParham\\Desktop\\naivebayes.pickle","rb")
cls = pickle.load(test)
test.close()
fileName = "Ex1.txt"
fileName2 = "Ex2.txt"
f2 = open(fileName2,"r", encoding="utf8");
f1 = open(fileName,"r", encoding="utf8");
posArr = f1.readlines() # first person
negArr = f2.readlines() # second person
documents = [(preProc.proc(posArr[i])) for i in range(len(posArr))]
documents2 = [(preProc.proc(negArr[i])) for i in range(len(negArr))]
tags = ('anger','anticipation','disgust','fear','joy','sadness','surprise','trust')
arr1 = []
for c in cls:
    arr1.append(c.classify_many([doc for doc in documents]))
arr2 = []
for c in cls:
    arr2.append(c.classify_many([doc for doc in documents2]))
i=0;
for lis in arr1:
    i=i+1
    k = 0;
    for j in lis:
        if j == 1:
            k+=1;
    print(tags[i-1],":  ",k)
i=0;
for lis in arr2:
    i=i+1
    k = 0;
    for j in lis:
        if j == 1:
            k+=1;
    print(tags[i-1],":  ",k)
