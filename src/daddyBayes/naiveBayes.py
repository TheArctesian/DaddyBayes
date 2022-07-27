"""
I'm going to do this string by string. 

for training 

tokenize string add it to a dictionary with that graded thing

Word,Senti
"bitcoin sell spree",-1 >= set1 = { "bitcoin": 1,
                                      "sell" : 1,
                                      "spree" : 1
                                    }
thisdict.update({"year": 2020}) 
thisdict["year"] = 2018
x = thisdict.keys() 

nive bayes = oc of word / all words in trained cats
"""
from lib2to3.pgen2 import token
from this import d
from coalas import csvReader as c
import re

def clean(text):
    text = str(text)
    text = re.sub('[^A-Za-z]+', ' ', text).lower().strip()
    return text

def tokenize(text):
    text = clean(text)
    text = text.split(" ")
    return text


def lemma(text):
    text = tokenize(text)
    text = [word for word in text if not word in stop_words]
    lemma = " ".join(text)
    lemma = lemma.lower()
    return lemma

def setup(dictCount):
    for i in dictCount:
      globals()[f'dict{i}'] = {}

def train(x_train,y_test): # Input,Output
    for i in range(len(x_train)):  

        temp = tokenize(x_train[i])
        if y_test[i] == "-1":
            for value in temp:
                if value in Neg: 
                    Neg[value] += 1
                else:
                    Neg[value] = 1
        if y_test[i] == "0":
            for value in temp:
                if value in Neu: 
                    Neu[value] += 1
                else:
                    Neu[value] = 1
        if y_test[i] == "1":
            for value in temp:
                if value in Pos: 
                    Pos[value] += 1
                else:
                    Pos[value] = 1

def concatenate(array):
    if len(array) == len(set(array)):
        tempDict = dict()
        for value in array: 
            tempDict[value] = 1
        return tempDict
    else: 
        tempDict = dict()
        for value in array: 
            if value in tempDict: 
                tempDict[value] +=1
            else: 
                tempDict[value] = 1
        return tempDict
    

def classifer(text):
    temp = tokenize(text)
    td = concatenate(temp)
    ng = checkNeg(td)
    nu = checkNeu(td)
    ps = checkPos(td)
    print(f'Neg: {ng}, Neu: {nu}, Pos: {ps}') 


def getTotal(dic):
    temp = 0
    for i in dic:
        temp += dic.values()

def checkNeg(dic):
    prob = []
    total = getTotal(dic) + getTotal(Neg)
    for i in dic:
        if i in Neg:
            p = dic[i].values()+Neg[i].values()
            prob.append(p)
        else: 
            prob.append(1)
    x = 1
    for i in prob: 
        x = x*i/total

def checkNeu(dic):
    prob = []
    total = getTotal(dic) + getTotal(Neu)
    for i in dic:
        if i in Neu:
            p = dic[i].values()+Neu[i].values()
            prob.append(p)
        else: 
            prob.append(1)
    x = 1
    for i in prob: 
        x = x*i/total

def checkPos(dic):
    prob = []
    total = getTotal(dic) + getTotal(Pos)
    for i in dic:
        if i in Pos:
            p = dic[i].values()+Pos[i].values()
            prob.append(p)
        else: 
            prob.append(1)
    x = 1
    for i in prob: 
        x = x*i/total





if __name__ == "__main__":
    c.importCSV("../../tests/lemma.csv")
    c.printHeaders()
    Neg = dict()
    Neu = dict()
    Pos = dict()
    test = "pee pee poo poo in my bum bum"
    test =tokenize(test)
    test1 = "bitcoin pump slump"
    train(c.lemma, c.trained)
    classifer(test1)



    
    # train(c.lemma, c.trained)
