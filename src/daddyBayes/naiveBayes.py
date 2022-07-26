from coalas import csvReader as c # This is the csv parser I made but its pretty shit 
import math
import re


"""
This code is pretty much just specilised for 3 variable projects
I will adapt this to be multi var
"""
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
    if ng > nu and ng > ps:
        return -1
    if nu > ng and nu > ps:
        return 0
    if ps > nu and ps > ng:
        return 1


def getTotal(dic):
    temp = 0
    for i in dic:
        temp += dic[i]
    return temp

def checkNeg(dic):
    prob = []
    total = getTotal(dic) + getTotal(Neg)
    for i in dic:
        if i in Neg:
            p = dic[i]+Neg[i]
            prob.append(p)
        else: 
            prob.append(1)
    temp = []
    for i in prob: 
        x = i/total
        temp.append(x)
    if len(temp) == 1:
        return(temp[0])
    else: 
        return math.prod(temp)
def checkNeu(dic):
    prob = []
    total = getTotal(dic) + getTotal(Neu)
    for i in dic:
        if i in Neu:
            p = dic[i]+Neu[i]
            prob.append(p)
        else: 
            prob.append(1)
    temp = []
    
    for i in prob: 
        x = i/total
        temp.append(x)
    if len(temp) == 1:
        return(temp[0])
    else: 
        return math.prod(temp)

def checkPos(dic):
    prob = []
    total = getTotal(dic) + getTotal(Pos)
    for i in dic:
        if i in Pos:
            p = dic[i]+Pos[i]
            prob.append(p)
        else: 
            prob.append(1)
    temp = []
    for i in prob: 
        x = i/total
        temp.append(x)
    if len(temp) == 1:
        return(temp[0])
    else: 
        return math.prod(temp)

def test():
    test1 = "bitcoin pump slump"
    print(classifer(test1))

def checkAc(train, perdicted):
    leng = len(train) 
    total = 0
    for i in range(leng):
        print(f'{i}: train{train[i]}, pred{perdicted[i]}')
        if int(train[i]) == int(perdicted[i]):
            print("foo")
            total += 1
    per = total/leng 
    return per

    return per

def dictionaryComprehension(keys, values, dicitonary):
    dicitonary = { k:v for (k,v) in zip(keys, values)}

if __name__ == "__main__":
    c.importCSV("../../tests/lemma.csv")
    c.printHeaders()
    c.addCol('naiveB')
    Neg = dict()
    Neu = dict()
    Pos = dict()
    train(c.lemma, c.trained)
    for i in range(len(c.lemma)):
        v = classifer(c.lemma[i])
        c.naiveB.append(v)
    checkAc(c.trained,c.naiveB)
    c.writeCSV("s.csv")

    import pandas as pd
    df = pd.read_csv("../../../../School/EE/Algos/Qual/bayes/out.csv")
    print([col for col in df])
    # lemma is iloc[2]
    da = []
    for i in df['Lemma']:
        print(i)
        da.append(i)
    time = []
    for i in df['date']:
        time.append(i)
    price = []
    for i in df['price']:
        price.append(i)
    o = []
    for i in range(len(da)):
        cl = classifer(da[i])
        print(cl)
        o.append(cl)


    with open('test.csv', "w") as file: 
        file.write('date,price,headline,action')
        for i in range(len(da)):
            print("WRITING")
            file.write(f'{time[i]},{price[i]},{da[i]},{o[i]}\n')


    
