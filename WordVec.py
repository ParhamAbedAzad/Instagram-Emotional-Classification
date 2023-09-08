from gensim.models import Word2Vec
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from preProc import proc
import pickle
fileName = "negin_abedzade/negin_abedzade.txt"
fileName2 = "hrouhani/hrouhani.txt"
fileName3 = "hrouhani2/hrouhani2.txt"
fileName4 = "azarijahromi/azarijahromi.txt"
f4 = open(fileName4,"r", encoding="utf8");
f3 = open(fileName3,"r", encoding="utf8");
f2 = open(fileName2,"r", encoding="utf8");
f1 = open(fileName,"r", encoding="utf8");
allComments = f1.readlines() + f2.readlines() + f3.readlines() + f4.readlines();
docs = [proc(allComments[i]) for i in range(len(allComments))]
model = Doc2Vec([TaggedDocument(doc,[i]) for i,doc in enumerate(docs)],min_count=2)
save_model = open("model.pickle","wb")
pickle.dump(model,save_model)
save_model.close()
