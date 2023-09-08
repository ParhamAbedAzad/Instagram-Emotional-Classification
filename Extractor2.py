import re;
import csv
import emoji;
AccName = input("please enter Acc Name:  ");
fileName = "{0}/{0}.csv".format(AccName);
fileName2 = "{0}/{0}.txt".format(AccName);
f2 = open(fileName2,"w", encoding="utf8");
with open(fileName, 'r', encoding="utf8") as csvfile: 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader:
        s = re.sub(r'_',r' ',re.sub(r'(@(\w)* ?)',r'',row[1]));
        s = re.sub(r'#',r'',s)
        s = re.sub(r'\n',r'',s)
        if s != "":
            f2.write(s + "\n")
        
