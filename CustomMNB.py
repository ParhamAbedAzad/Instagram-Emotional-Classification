import random;
import nltk;
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, recall_score, precision_score
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
import xgboost as xgb
import numpy as np
from VoteClassifier import VoteClassifier
from sklearn.linear_model import LogisticRegression,SGDClassifier
import emoji
def removeEmojies(testing_set):
    for test in testing_set:
        for emo in emoji.UNICODE_EMOJI:
            if emo in test[0]:
                test[0][emo]=False;
    return testing_set;
def removeEmojies2(EmotionDocs):
    for doc in EmotionDocs:
        j=0
        for i in range(len(doc[0])):
            if doc[0][i-j] in emoji.UNICODE_EMOJI:
                doc[0].remove(doc[0][i-j]);
                j+= 1
        if doc[0] ==[]:
            EmotionDocs.remove(doc);
    return EmotionDocs;  
tags = ('Ang','Ant','Dis','Fea','Joy','Sad','Sur','Tru')
class CustomMNB:
    def __find_features(self,document):
##        d = {}
##        res = self.model.infer_vector(document)
##        for i in range(len(res)):
##            d[i] = (res[i] + 2)/4;
##            if d[i] < 0:
##                print(res)
##                print(i)
##        return d
        words = set(document)
        features = {}
        for w in self.word_features:
            features[w] = (w in words)
        return features
    def __init__(self, documents, i):
        st = tags[i] + "  |  "
        self.classifier = SklearnClassifier(MultinomialNB());
        EmotionDocs = [];
        docLen = len(documents)
        for j in range(docLen):
            if documents[j][1][i]==1:
                EmotionDocs.append(documents[j])
                for howManyZero in range(1):
                    randNum = random.randrange(docLen)
                    while documents[randNum][1][i]==1:
                        randNum = random.randrange(docLen)
                    EmotionDocs.append(documents[randNum])
        EmotionDocs[0:int(len(EmotionDocs)/3)] = removeEmojies2(EmotionDocs[0:int(len(EmotionDocs)/3)])
        random.shuffle(EmotionDocs)
        if i==4:
            EmotionDocs = EmotionDocs[0:int(len(EmotionDocs)/2)]
        all_words = [j for sub in EmotionDocs
                 for j in sub[0]]
        all_words = nltk.FreqDist(all_words)
        if i==4:
            self.word_features = list(all_words.keys())[:int(len(all_words)/8)]
        else:
            self.word_features = list(all_words.keys())[:int(len(all_words)/3)]
        border = int(len(EmotionDocs)*0.9)
        self.featuresets = [(self.__find_features(rev), scores[i]) for (rev, scores) in EmotionDocs]
##        self.featuresets[0:int(len(self.featuresets)/2)] = removeEmojies(self.featuresets[0:int(len(self.featuresets)/2)])
##        random.shuffle(self.featuresets)
        self.training_set = self.featuresets[:border]
        self.testing_set = self.featuresets[border:]
##        self.testing_set[0:int(len(self.testing_set)/2)] = removeEmojies(self.testing_set[0:int(len(self.testing_set)/2)])
##        random.shuffle(self.testing_set)
        self.classifier.train(self.training_set);
        self.showAccuracy()
        self.SVC_classifier = SklearnClassifier(SVC())
        self.SVC_classifier.train(self.training_set)
        print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(self.SVC_classifier, self.testing_set))*100)

##        self.LinearSVC_classifier = SklearnClassifier(LinearSVC())
##        self.LinearSVC_classifier.train(self.training_set)
##        print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(self.LinearSVC_classifier, self.testing_set))*100)

        self.LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
        self.LogisticRegression_classifier.train(self.training_set)
        print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(self.LogisticRegression_classifier, self.testing_set))*100)

##        self.SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
##        self.SGDClassifier_classifier.train(self.training_set)
##        print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(self.SGDClassifier_classifier, self.testing_set))*100)
##
##        self.NuSVC_classifier = SklearnClassifier(NuSVC())
##        self.NuSVC_classifier.train(self.training_set)
##        print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(self.NuSVC_classifier, self.testing_set))*100)

        self.voted_classifier = VoteClassifier(self.classifier,
                                  self.SVC_classifier,
                                  self.LogisticRegression_classifier)

        st += format(nltk.classify.accuracy(self.voted_classifier, self.testing_set)*100,'.3f')
        st += "  |  ";
        (x,y) = self.returnPerRec()
        st += str(format(x,'.3f')) + "  |  " + str(format(y,'.3f')) + "  |"
        print(st)
##        in_train = [np.array(list(x[0].values())) for x in self.training_set]
##        in_test = [np.array(list(x[0].values())) for x in self.testing_set]
##        out_train = [x[1] for x in self.training_set]
##        out_test = [x[1] for x in self.testing_set]
##        in_train = np.array(in_train)
##        in_test = np.array(in_test)
##        out_train = np.array(out_train)
##        out_test = np.array(out_test)
##        dtrain = xgb.DMatrix(in_train,label=out_train)
##        dtest = xgb.DMatrix(in_test,label=out_test)
##        param = {'max_depth':10, 'eta':0.2, 'objective':'multi:softmax','num_class':3 }
##        num_round = 10
##        bst = xgb.train(param, dtrain, num_round)
##        preds = bst.predict(dtest)
##        print(accuracy_score(out_test,preds))

        
    def train(self):
        self.classifier.train(self.training_set)
    def showAccuracy(self):
        print("MultinomialNB accuracy percent:",format(nltk.classify.accuracy(self.classifier, self.testing_set),'.3f'))
    def returnAccuracy(self):
        return nltk.classify.accuracy(self.classifier, self.testing_set)
    def classify(self,document):
        return self.voted_classifier.classify(self.__find_features(document))
    def classify_many(self,documents):
        return [self.classify(document) for document in documents]
    def returnPerRec(self):
        self.fillTestRes()
        return (precision_score(self.testResults,self.testAns), recall_score(self.testResults,self.testAns))
    def fillTestRes(self):
        self.testCases = [k[0] for k in self.testing_set];
        self.testResults = self.voted_classifier.classify_many(self.testCases);
        self.testAns = [k[1] for k in self.testing_set]
