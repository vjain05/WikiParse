import wikipedia
from collections import deque
import sys
import pprint
from sets import Set
import numpy as np
import json
import random

def prints(obj):
    pprint.pprint(obj)

def pickRandNums(low,high,nums):
    #assume nums<range(low,high)
    arr=[]
    for i in range(low,high+1):
        arr.append(i)
    indicator=0
    for i in range(0,nums):
        idx=np.random.random_integers(indicator,len(arr)-1)
        temp=arr[idx]
        arr[idx]=arr[indicator]
        arr[indicator]=temp
        indicator+=1
    return arr[0:nums]

a=[]
#fil = open("/Users/vmac/PycharmProjects/WikiParse/sampleInput.txt","r+")
fil=wikipedia.random(pages=5)
outz = open("/Users/vmac/PycharmProjects/WikiParse/sampleOutput.json","w+")
dictOfWords={}
for iz in fil:
    stuff = iz

    theQueue=deque([])
    theQueue.append((stuff,"-1"))
    numAtLevel=1
    levelCounter=0
    nextLevel=0
    counter=0

    az = Set([])
    while len(theQueue)>0:
        counter+=1
        item=theQueue.popleft()
        if item[0] not in az:
            print item[0]
            az.add(item[0])
            if not dictOfWords.has_key(item[1]):
                dictOfWords[item[1]]=[]

            dictOfWords[item[1]].append(item[0])

            levelCounter+=1
            try:
                nb=wikipedia.page(item[0])
            except wikipedia.exceptions.PageError,e:
                print e
                break
            except wikipedia.exceptions.DisambiguationError, e:
                errOpts=e.options
                nb=wikipedia.page(random.choice(errOpts))

            nb2=nb.links
            #cou=0
            #for i in nb:
            #    if i not in az and cou<=0:
            #        nextLevel+=1
            #        theQueue.append((i,item[0]))
            #        cou+=1
            theNum=np.random.random_integers(len(nb2))-1
            counterz=0
            while nb2[theNum] in az:
                theNum=np.random.random_integers(len(nb2))-1
                counterz+=1
                if counterz==len(nb2)*2:
                    break
            nextLevel+=1
            theQueue.append((nb2[theNum],item[0]))
            if levelCounter==numAtLevel:
                print "-"
                levelCounter=0
                numAtLevel=nextLevel
                nextLevel=0
            if counter>=100:
                break

json.dump(dictOfWords,outz)
#fil.close()
outz.close()