import pandas as pd
import numpy

"""
Parsed a file through however you want so that you get numpy arrays for each condition

Par example:

Say I have a csv or a 2d matrix structured like so

Text,Condition

Your text can by whatever you want as long as it is in string format 

The conditions however you should know how many there are and what they are

Unless you don't then you can use the function `identifyConditions`

After which send those conditions into the initParama function

This will initilise dicts for each of your conditions

Then the train function will:
    A. Clean each text so it's only the relevent words
    B. Seprate the text into a list
    C. Put each word in the last into a condition (dictionary)

now using the classify function you can ran any string through there and classify it as such

"""
# now I have to built this

def initPram(arrayOfParamaters):
    # initlises dictionaries for each array
    for param in arrayOfParamaters:
        globals()[param] = dict()


def initCSV(fileName):
    df = pd.read_csv('myfile.csv', sep=',', header=None)
    # parse these
def identifyConditions(array):
    return numpy.unique(array);

    print("not done")
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
    lemma = " ".join(text).lower()
    return lemma

if __name__ == "__main__":
    print("hello world")

