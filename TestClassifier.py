##tags = ('anger','anticipation','disgust','fear','joy','sadness','surprise','trust')
##documents = []
##fileName = "negin_abedzade/negin_abedzade.txt"
##fileName2 = "hrouhani/hrouhani.txt"
##fileName3 = "hrouhani2/hrouhani2.txt"
##fileName4 = "azarijahromi/azarijahromi.txt"
##f4 = open(fileName4,"r", encoding="utf8");
##f3 = open(fileName3,"r", encoding="utf8");
##f2 = open(fileName2,"r", encoding="utf8");
##f1 = open(fileName,"r", encoding="utf8");
##documents = posArr + negArr + f3.readlines() + f4.readlines();
##Classifiers = [];
##from engine import classifier
arr = []
for c in classifiers:
    arr.append(c.classify_many([doc[0] for doc in documents]))
##arr = cls.classify_many([doc[0] for doc in documents])
n = len(documents)
i=0;
for lis in arr:
    i=i+1
    k = 0;
    for j in arr:
        if j == 1:
            k+=1;
    print(tags[i-1],":  ",k/n)
