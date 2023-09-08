import nltk
import hazm
import random
import preProc
import pickle
import CustomMNB
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify.scikitlearn import SklearnClassifier
import xgboost as xgb
import numpy as np
from sklearn.metrics import accuracy_score
from multiprocessing import Pool
import MultiProc
def creatClassifier(k):
    return CustomMNB.CustomMNB(documents,k)

def toArr(line):
    result = []
    for c in line:
        if c=='0' or c=='1':
            result = result + [int(c)]
    return result
##test = open("C:\\Users\\FarazParham\\Desktop\\model.pickle","rb")
##test = open("model.pickle","rb")
##model = pickle.load(test)
##test.close()

tags = ('anger','anticipation','disgust','fear','joy','sadness','surprise','trust')
documents = []
fileName = "negin_abedzade/negin_abedzade.txt"
fileName2 = "hrouhani/hrouhani.txt"
fileName3 = "hrouhani2/hrouhani2.txt"
fileName4 = "azarijahromi/azarijahromi.txt"
fileName_em = "negin_abedzade/negin_abedzade_em.txt"
fileName2_em = "hrouhani/hrouhani_em.txt"
fileName3_em = "hrouhani2/hrouhani2_em.txt"
fileName4_em = "azarijahromi/azarijahromi_em.txt"
f4 = open(fileName4,"r", encoding="utf8");
f3 = open(fileName3,"r", encoding="utf8");
f2 = open(fileName2,"r", encoding="utf8");
f1 = open(fileName,"r", encoding="utf8");
f4_em = open(fileName4_em,"r", encoding="utf8");
f3_em = open(fileName3_em,"r", encoding="utf8");
f2_em = open(fileName2_em,"r", encoding="utf8");
f1_em = open(fileName_em,"r", encoding="utf8");
EmotionDocs = [];
posArr = f1.readlines() # first person
negArr = f2.readlines() # second person
allComments = posArr + negArr + f3.readlines() + f4.readlines();
emArr = f1_em.readlines() + f2_em.readlines() + f3_em.readlines() + f4_em.readlines();
f1.close();
f2.close();
f3.close();
f4.close();
f1_em.close();
f2_em.close();
f3_em.close();
f4_em.close();
emArr = [toArr(line) for line in emArr]
tagsArr = [[emArr[k][i] for k in range(len(emArr))] for i in range(len(tags))]
#documents = [(preProc.proc(c),'pos') for c in posArr] + [(preProc.proc(c),'neg') for c in negArr]
documents = [(preProc.proc(allComments[i]),emArr[i]) for i in range(len(allComments))]
random.shuffle(documents)
print("     |    Acc   |    Per   |    Rec   |  ")
print("------------------------------------------")
classifiers = [CustomMNB.CustomMNB(documents,i) for i in range(len(tags))]
##classifiers = MultiProc.createClasses(documents);
##for i in range(len(tags):
##classifiers = [CustomMNB.CustomMNB(documents,i) for i in range(len(tags))]
##cls = CustomMNB.CustomMNB(documents,0)
##with Pool(4) as p:
##    classifiers = p.map(CustomMNB.CustomMNB(), [documents,k for k in range(len(tags))]);
##i = 0
##while i <len(tags):
##    if classifiers[i].returnAccuracy() > cls[i].returnAccuracy():
##        cls[i] = classifiers[i]
##    classifiers[i].showAccuracy();
##    i = i+1;

##test = open("C:\\Users\\FarazParham\\Desktop\\naivebayes.pickle","wb")
##pickle.dump(cls,test)
##test.close()
##classifiers[0].train(training_set)
##print("MultinomialNB accuracy percent:",nltk.classify.accuracy(classifiers[i], testing_set))

### XGBOOST Code START
##in_train = [np.array(list(x[0].values())) for x in training_set]
##in_test = [np.array(list(x[0].values())) for x in testing_set]
##out_train = [1 if (x[1]=='pos') else 0 for x in training_set]
##out_test = [1 if (x[1]=='pos') else 0 for x in testing_set]
##in_train = np.array(in_train)
##in_test = np.array(in_test)
##out_train = np.array(out_train)
##out_test = np.array(out_test)
##dtrain = xgb.DMatrix(in_train,label=out_train)
##dtest = xgb.DMatrix(in_test,label=out_test)
##param = {'max_depth':10, 'eta':0.2, 'objective':'multi:softmax','num_class':3 }
##num_round = 10
##bst = xgb.train(param, dtrain, num_round)
##preds = bst.predict(dtest)
##print(accuracy_score(out_test,preds))
### XGBOOST Code End


####### uncomment
##classifier = SklearnClassifier(MultinomialNB())
##classifier.train(training_set)
##print("MultinomialNB accuracy percent:",nltk.classify.accuracy(classifier, testing_set))
###### uncomment

##BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
##BernoulliNB_classifier.train(training_set)
##print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)
##
##SVC_classifier = SklearnClassifier(SVC())
##SVC_classifier.train(training_set)
##print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)
##
##LinearSVC_classifier = SklearnClassifier(LinearSVC())
##LinearSVC_classifier.train(training_set)
##print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)
##
##NuSVC_classifier = SklearnClassifier(NuSVC())
##NuSVC_classifier.train(training_set)
##print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)


##save_classifier = open("C:\\Users\\FarazParham\\Desktop\\naivebayes.pickle","wb")
##pickle.dump(classifier,save_classifier)
##save_classifier.close()
