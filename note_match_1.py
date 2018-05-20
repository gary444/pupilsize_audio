
from pyo import *
import sys
import math
import numpy as np
from numpy import genfromtxt

#values from csv file
inValues = genfromtxt('set5.csv', delimiter=',')
targetValue = inValues[0]
values = np.delete(inValues,0)

print('target value  = ')
print(targetValue)
    
list_length = len(values)
min = min(values)
max = max(values)
s = 'list length: ' + repr(list_length)
print(s)
s = 'min ' + repr(min)
print(s)
s = 'max ' + repr(max)
print(s)

#get this automatically at some point:
baseline = 2.21207220367279

#create steps to quantise in put values to notes
#define number of steps to use between baseline and target (i.e. covering 1 SD)
SD_steps = 7
step_width = (targetValue - baseline) / SD_steps

def getStepsBelowTarget(inputValue):
    if inputValue > targetValue:
        return 0
    else:
        diff = targetValue - inputValue
        stepsBelow = diff/step_width
        #round up to get steps below
        return math.ceil(stepsBelow)

def noteToFreq(midiNote):
    return 2.0**((midiNote-69.0)/12.0)*440.0

majScaleDescending = [60,59,57,55,53,52,50,48,47,45,43,41,40,38,36]

def getFreq(inputValue):
    steps = getStepsBelowTarget(inputValue)
    if steps >= len(majScaleDescending):
        steps = len(majScaleDescending) - 1;
    print(majScaleDescending[steps])
    return noteToFreq(majScaleDescending[steps])
    

        
print('step width')
print(step_width)

# set sample rate
sampleRate = 60
sleeptime = 1.0/sampleRate

 #set up audio server
s = Server().boot()
s.start()

targetTone = 60 #60 is middle C
freq = noteToFreq(targetTone - 24)

env = Adsr(attack=.01, decay=.2, sustain=.5, release=.5, dur=1.5, mul=.5)

sig1 = RCOsc(freq, sharp=0.2, mul=env)
sig2 = RCOsc(noteToFreq(targetTone), sharp=0.0, mul=env*0.5)



p1 = Pan(sig1, outs=2, pan=0).out()
p2 = Pan(sig2, outs=2, pan=1).out()


#avg last x values
avg_length = 20
recent_avg = 0.0

current_step = -1;

note_change_pause = 60
since_note_change = 0

# cycle through samples in array
# adjust frequency of sine wave depending on average
for x in range(0,list_length):
    if x == 0:
        recent_avg = values[0]
    elif x < avg_length:
        recent_avg = ((recent_avg * x) + values[x]) / (x+1)
    else:
        recent_avg = ((recent_avg * (avg_length-1)) + values[x]) / avg_length 

        if since_note_change >= note_change_pause:
            since_note_change = 0
            #change note to
            step_change = getStepsBelowTarget(recent_avg)
            #if step_change != current_step:
                #current_step = step_change
                #change synth note
            sig1.setFreq(getFreq(recent_avg))

            env.play()
 #               sig.setSharp = 0.2;

        #elif since_note_change == note_change_pause/2:
#            sig.setFreq(getFreq(targetValue))
#            sig.setSharp = 0.0;
            
        since_note_change += 1
            
        
        
        #if pupil size is less than target
        #if recent_avg < targetValue:
        
        #if pupil is wider than target width
        #else:

                
    time.sleep(sleeptime)



s.stop()
