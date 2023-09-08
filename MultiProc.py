import CustomMNB
from multiprocessing import Pool
tags = ('anger','anticipation','disgust','fear','joy','sadness','surprise','trust')
def f(documents,k):
    return CustomMNB.CustomMNB(documents,k)
def g(documents,classifier):
    return classifier.classify_many(documents)
def testClasses(classifiers,documents):
    with Pool(4) as p:
        classifiers = p.starmap(g, [(documents,c) for c in classifiers]);
def createClasses(documents):
    with Pool(4) as p:
        classifiers = p.starmap(f, [(documents,k) for k in range(8)]);
    return classifiers;
