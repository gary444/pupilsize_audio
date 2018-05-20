

from pyo import *
import sys
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

#mappings: set range conversion here============================
def mapToOutputRange(inputValue, targetValue):
    input_min = 1.9 #mm
    #input_max = 7.0 #mm
    input_target = targetValue #from baseline measurements
    input_range = input_target - input_min
    output_min = 0.05
    output_max = 1.0
    shouldInvert = True;
    if shouldInvert == True:
        output_min, output_max = output_max, output_min#swap
    output_range = output_max - output_min 
    if inputValue > input_target:
        return output_max

    scaled_val = (inputValue - input_min) / input_range
    output_val = output_min + (scaled_val * output_range)
    return output_val

#end mapping ===================================================


# set sample rate
sampleRate = 60
sleeptime = 1.0/sampleRate

 #set up audio server
s = Server().boot()
s.start()

#create metronome for clicks - with envelope
t1 = CosTable([(0,0), (100,1), (500,.3), (800,0)])
clicks = Metro(time=1.0, poly=1)
met_amp = TrigEnv(clicks, table=t1, dur=.25, mul=0.3)
a = Sine(freq=1000, mul=met_amp).out()

# create envelope for continuous tone
tone = Adsr(attack=0.1, decay=0.4, sustain=0.5, release=0.1, dur=0, mul=0.5)
#create wave generator for tone - takes env as it's multiplier
b = Sine(freq=1000, mul=tone).out()

#avg last x values
avg_length = 20
recent_avg = 0.0

# cycle through samples in array
# adjust frequency of sine wave depending on average
for x in range(0,list_length):
    if x == 0:
        recent_avg = values[0]
    elif x < avg_length:
        recent_avg = ((recent_avg * x) + values[x]) / (x+1)
    else:
        recent_avg = ((recent_avg * (avg_length-1)) + values[x]) / avg_length 

        #if pupil size is less than target
        if recent_avg < targetValue:
            if clicks.isPlaying() == False:
                tone.stop()
                clicks.play()
            else:
                clicks.setTime(float(mapToOutputRange(recent_avg, targetValue)))
        else:
        #if pupil is wider than target width
            if clicks.isPlaying():
                clicks.stop() 
                tone.play()
                
    time.sleep(sleeptime)

#kill sine wave
tone.stop()
time.sleep(2)

s.stop()
