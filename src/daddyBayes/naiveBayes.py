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

nive bayes = oc of word / all words

"""
from coalas import importCSV as c

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

def train(x,y): # Input,Output,Outputs or how many dict are to be made
    for i in range(len(y)):  
        if y[i] == "-1":
            Neg[x[i]] +=1
        if y[i] == "0":
            Neu[x[i]] +=1
        if y[i] == "1":
            Pos[x[i]] +=1



if __name__ == "__main__":
    c.importCSV("../../tests/trained.csv")
    Neg = {}
    Neu = {}
    Pos = {}
    train(c.lemma, c.trained)
