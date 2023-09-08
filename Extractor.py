import json;
import re;
import emoji;
AccName = input("please enter Acc Name:  ");
isTag="";
while(isTag!="user" and isTag != "tag"):
    isTag = input("user or tag:  ");
isTag = True if (isTag=="tag") else False;
fileName = "{0}/{0}.json".format(AccName);
fileName2 = "{0}/{0}.txt".format(AccName);
f1 = open(fileName,"r", encoding="utf8");
datas = json.loads(f1.read())
f2 = open(fileName2,"w", encoding="utf8");
comment = "";
if(isTag):
    comment = 'edge_media_to_comment';
else:
    comment = 'comments';
for data in datas['GraphImages']:
    if not data[comment]['data']:
        continue;
    f2.write("<--NEW POST-->" + "\n");
    for s in data[comment]['data']:
        s2 = s['text'];
        #s2 = re.sub(r'^@(w|.)* ',r'',s2)
        #for c in emoji.UNICODE_EMOJI:
        #    s2 = s2.replace(c," {} ".format(c))
        #s2 = s2.replace("  "," ")
        f2.write(s2 + "\n");
f2.close()
f1.close()
#print(datas['GraphImages'][1]['comments']['data'][1]['text']);
