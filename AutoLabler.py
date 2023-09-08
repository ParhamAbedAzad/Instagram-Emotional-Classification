import preProc

count = [0,0,0,0,0,0,0,0]
tags = ('anger','anticipation','disgust','fear','joy','sadness','surprise','trust')
emojies = {
    "✌" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':1},
    "🤞" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':1},
    "👌" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':1},
    "👍" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':1},
    "💪" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':1},
    "✋" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':1},
    "🤝" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':1},
    "😧" : {'anger':0,'anticipation':0,'disgust':0,'fear':1,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😦" : {'anger':0,'anticipation':0,'disgust':0,'fear':1,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😟" : {'anger':0,'anticipation':0,'disgust':0,'fear':1,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😬" : {'anger':0,'anticipation':0,'disgust':0,'fear':1,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "🤐" : {'anger':0,'anticipation':0,'disgust':0,'fear':1,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😲" : {'anger':0,'anticipation':0,'disgust':0,'fear':1,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😧" : {'anger':0,'anticipation':0,'disgust':0,'fear':1,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😳" : {'anger':0,'anticipation':0,'disgust':0,'fear':1,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😱" : {'anger':0,'anticipation':0,'disgust':0,'fear':1,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😰" : {'anger':0,'anticipation':0,'disgust':0,'fear':1,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😅" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':1,'trust':0},
    "😮" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':1,'trust':0},
    "🙊" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':1,'trust':0},
    "🙈" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':1,'trust':0},
    "😲" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':1,'trust':0},
    "😯" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':1,'trust':0},
    "🤯" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':1,'trust':0},
    "🤦‍♀️" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':1,'surprise':1,'trust':0},
    "🤦‍♂️" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':1,'surprise':1,'trust':0},
    "😟" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':1,'surprise':1,'trust':0},
    "😒" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':1,'surprise':1,'trust':0},
    "☹" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':1,'surprise':0,'trust':0},
    "🙁" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':1,'surprise':0,'trust':0},
    "😞" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':1,'surprise':0,'trust':0},
    "😟" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':1,'surprise':0,'trust':0},
    "😢" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':1,'surprise':0,'trust':0},
    "😭" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':1,'surprise':0,'trust':0},
    "😔" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':1,'surprise':0,'trust':0},
    "💔" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':1,'surprise':0,'trust':0},
    "😫" : {'anger':0,'anticipation':0,'disgust':1,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😪" : {'anger':0,'anticipation':0,'disgust':1,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "🤐" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😣" : {'anger':0,'anticipation':0,'disgust':1,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "🤢" : {'anger':0,'anticipation':0,'disgust':1,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "🤮" : {'anger':0,'anticipation':0,'disgust':1,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😷" : {'anger':0,'anticipation':0,'disgust':1,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "🤧" : {'anger':0,'anticipation':0,'disgust':1,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😐" : {'anger':0,'anticipation':0,'disgust':1,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😖" : {'anger':0,'anticipation':0,'disgust':1,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😡" : {'anger':1,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😤" : {'anger':1,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "🤬" : {'anger':1,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😠" : {'anger':1,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "😑" : {'anger':0,'anticipation':0,'disgust':1,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "👊" : {'anger':1,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "🤛" : {'anger':1,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "🤜" : {'anger':1,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "👎" : {'anger':1,'anticipation':0,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "🖐" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    #"✊" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "🤚" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    #"🤟" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    #"🙏" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    #"🤤" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    #"😛" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    #"😜" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0}, 
    "😎" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    #"🤓" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    #"🧐" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    #"🤑" : {'anger':0,'anticipation':1,'disgust':0,'fear':0,'joy':0,'sadness':0,'surprise':0,'trust':0},
    "🤩" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    "❤" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    #"💕" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    #"💖" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    #"💞" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    #"❣" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    #"💘" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    #"💝" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    "😍" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    #"🥰" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    "😘" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},#+?
    "😃" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    "😄" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    "😅" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    #"😆" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    #"😉" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    "😊" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    "😋" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    "😗" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    "😙" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    #"😚" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    #"☺" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    #"🙂" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0},
    #"🤗" : {'anger':0,'anticipation':0,'disgust':0,'fear':0,'joy':1,'sadness':0,'surprise':0,'trust':0}

    }
class NRCReader:
    def __init__(self, NRCAddress="NRC-emotion-lexicon-wordlevel-persian-v0.92.txt"):
        self.nrc_address = NRCAddress
        self.data = {}

    def load(self):
        with open(self.nrc_address, "r", encoding="utf-8") as nrc_file:
            for line in nrc_file.readlines():
                splited = line.replace("\n", "").split("\t")
                word, emotion, value = splited[0], splited[1], splited[2]
                if word in self.data.keys():
                    self.data[word].append((emotion, int(value)))
                else:
                    self.data[word] = [(emotion, int(value))]

    def vectorize(self, sentence:list):
        out = {}
        for word in sentence:
            if word in self.data.keys():
                for item in self.data[word]:
                    if word in out.keys():
                        out[word] += (item[0], item[1])
                    else:
                        out[word] = (item[0], item[1])
        return out

    def getEmotions(self, sentence:list):
        global count;
        out = [0 for tag in tags]
        for word in sentence:
            if word in emojies:
                i=0;
                for tag in tags:
                    if emojies[word][tag] == 1:
                        out[i] = 3;
                    i = i+1;
            #elif word not in self.data.keys():
            #    continue;
            #else:
            #    emotions = self.data[word]
            #    for i in range(len(tags)):
            #        if emotions[i][1] == 1:
            #            out[i] += 1
        count = [count[i] + 1 if out[i]>1 else count[i] for i in range(len(out))];
        return [1 if o>1 else 0 for o in out];

        
    def get_emotion(self, word, emotion):
        emotions = self.data[word]
        for emot in emotions:
            if emot[0] == emotion:
                return emot[1]
    
nrc = NRCReader();
#nrc.load();

AccName = input("please enter Acc Name:  ");
fileName1 = "{0}/{0}.txt".format(AccName);
fileName2 = "{0}/{1}.txt".format(AccName,AccName + "_em");
fileName3 = "{0}/{1}.txt".format(AccName,AccName + "_lc");
f1 = open(fileName1,"r", encoding="utf8");
f2 = open(fileName2,"w", encoding="utf8");
f3 = open(fileName3,"w", encoding="utf8");
comments = f1.readlines()
k = 0;
for comment in comments:
    p_comment = preProc.proc(comment)
    res = str(nrc.getEmotions(p_comment))
    if '\n' in comment:
        comment.replace("\n", "")
    if 1==1:
        f2.write(res);
        f3.write(comment)
        f2.write("\n")
f2.close()
f3.close()

print(count);
