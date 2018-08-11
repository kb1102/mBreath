##Apnea
from xmlr import xmlparse
import pandas as pd
doc =xmlparse("./apnea/mesa-sleep-0001-profusion.xml")#it gives us the file in the form of Dictonaries
final=doc["CMPStudyConfig"]["ScoredEvents"]["ScoredEvent"]

df=pd.DataFrame.from_dict(final)
data=df[df["Name"]=='Hypopnea']
Apnea=data[["Duration","Input","Name","Start"]]
Apnea.to_csv("Apnea.csv")

##Flow

import pyedflib
import numpy as np 
f = pyedflib.EdfReader("./flow/mesa-sleep-0001.edf")
signal_labels = f.getSignalLabels()

#to get the description about labels:

for channel in range(len(signal_labels)):

    print("\nsignal parameters for the %d.channel:\n\n" % channel)

    print("label: %s" % f.getLabel(channel))
    print("samples in file: %i" % f.getNSamples()[channel])

channel =8 ## this is our required column
sampel_rate =f.getNSamples()[channel] 
read_signal=f.readSignal(channel)
n =f.getNSamples()[channel]
Flow=[]
Epoch=[]
epoch=0
for i in np.arange(n):
    flow=read_signal[i]
    Flow.append(flow)
      
    epoch=epoch
    Epoch.append(epoch)
       
    epoch=epoch+ (1/32)
data={'Flow':Flow,'Epoch':Epoch}
Flow=pd.DataFrame(data)
Flow.to_csv("Flow.csv")

##Stage
document =xmlparse("./stage/mesa-sleep-0001-nsrr.xml")
stage=document['PSGAnnotation']["ScoredEvents"]["ScoredEvent"]
stage=pd.DataFrame.from_dict(stage)

stage=stage[stage["EventType"]=="Stages|Stages"]
stage=stage[["Duration","EventConcept","EventType","Start"]]

stage.to_csv("stage.csv")















