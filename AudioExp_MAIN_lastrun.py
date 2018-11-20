#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.1),
    on August 21, 2018, at 15:42
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'BCI_Exp_v10'  # from the Builder filename that created this script
expInfo = {u'session': u'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.path.sep + '%s_%s' %(expInfo['session'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'F:\\Users\\Administrator\\Documents\\pupil_project\\psychopy\\audio\\AudioExp\\AudioExp_MAIN.psyexp',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=1,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-0.3,-0.3,-0.3], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "iViewX_Connect"
iViewX_ConnectClock = core.Clock()
from iViewXAPI import  *            #iViewX library
# ---------------------------------------------
#---- connect to iViewX
# ---------------------------------------------
res = iViewXAPI.iV_Connect(c_char_p('141.54.159.23'), c_int(4444), c_char_p('141.54.159.21'), c_int(5555))

res = iViewXAPI.iV_GetSystemInfo(byref(systemData))
print "iV_GetSystemInfo: " + str(res)
print "Samplerate: " + str(systemData.samplerate)
print "iViewX Verion: " + str(systemData.iV_MajorVersion) + "." + str(systemData.iV_MinorVersion) + "." + str(systemData.iV_Buildnumber)
print "iViewX API Verion: " + str(systemData.API_MajorVersion) + "." + str(systemData.API_MinorVersion) + "." + str(systemData.API_Buildnumber)


#import audio library here so iview X can connect
#from pyo import *
#s = Server(buffersize=1024,duplex=0, winhost="asio").boot()
#s.start()

'''
# ---------------------------------------------
#---- configure and start calibration
# ---------------------------------------------
#calibrationData = CCalibration(13, 1, 1, 0, 0, 180, 150, 2, 20, b"")

calibrationData = CCalibration(9, 1, 1, 0, 2, 250, 180, 2, 20, b"")
#(method, visualization, display, speed, auto, fg, bg, shape, size, filename)

res = iViewXAPI.iV_SetupCalibration(byref(calibrationData))
print "iV_SetupCalibration " + str(res)
res = iViewXAPI.iV_Calibrate()
print "iV_Calibrate " + str(res)
res = iViewXAPI.iV_Validate()
print "iV_Validate " + str(res)

print "iV_GetAccuracy " + str(res)
print "deviationXLeft " + str(accuracyData.deviationLX) + " deviationYLeft " + str(accuracyData.deviationLY)
print "deviationXRight " + str(accuracyData.deviationRX) + " deviationYRight " + str(accuracyData.deviationRY)
'''

# Initialize components for Routine "Audio_Setup"
Audio_SetupClock = core.Clock()


# Initialize components for Routine "bl_instructions"
bl_instructionsClock = core.Clock()
import random
nend=0
clbsloop=0
current_mean = 0

custom_routine_text = "test1"
routine_end_text = "test2"
baseline_instructions = visual.TextStim(win=win, name='baseline_instructions',
    text='default text',
    font='Arial',
    units='pix', pos=(-10, 0), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "baseline_b4try"
baseline_b4tryClock = core.Clock()
b_zeitpuffer1_2_ = visual.TextStim(win=win, name='b_zeitpuffer1_2_',
    text=None,
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=0.0);
#-----------------------------------
# Begin Experiment
#-----------------------------------
import numpy

labels = ["PS", "FR", "none"]

# set method order for whole experiment
# 0 - parking sensor, 1 - freq/note, 2 - none
trial_method = int(expInfo["session"]) % 6
trial_method_order = [0,1,2]#default

if trial_method == 0:
    trial_method_order = [0,1,2]
elif trial_method == 1:
    trial_method_order = [1,2,0]
elif trial_method == 2:
    trial_method_order = [2,0,1]
elif trial_method == 3:
    trial_method_order = [1,0,2]
elif trial_method == 4:
    trial_method_order = [2,1,0]
elif trial_method == 5:
    trial_method_order = [0,2,1]

# Initialize components for Routine "trying"
tryingClock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text=None,
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=0.0);
from numpy import (log)
maxsize=0
minsize=3000
timer = 0

#min input size for pupil
min_input_bound = 2 #mm

#mapping for parking sensor: set range conversion here
def mapToTimeOutputRange(inputValue, targetValue):
    input_min = min_input_bound 
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

#mapping from pupil size to freqency
def mapToOutputRange(inputValue, targetValue):
    input_min = min_input_bound #mm
    input_target = targetValue #from baseline measurements
    input_range = input_target - input_min
    output_min = 400 #hz
    output_max = 800 #hz
    output_range = output_max - output_min 
    if inputValue > input_target:
        return output_max
    if inputValue < input_min:
        return output_min
    scaled_val = (inputValue - input_min) / input_range
    output_val = output_min + (scaled_val * output_range)
    return output_val




# Initialize components for Routine "pause"
pauseClock = core.Clock()
Puffer = visual.TextStim(win=win, name='Puffer',
    text="End of 'trying' period\n\nPress space to continue",
    font='Arial',
    pos=[0, 0], height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "activ"
activClock = core.Clock()
#set text for activation labels
actlabels = ["_act_", "_deact_"]
activation_out_text = "test_"
activation_end_text = "test"

text_15 = visual.TextStim(win=win, name='text_15',
    text='default text',
    font='Arial',
    pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "baseline"
baselineClock = core.Clock()
zeitpuffer1 = visual.TextStim(win=win, name='zeitpuffer1',
    text=None,
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "trial_gap"
trial_gapClock = core.Clock()
zeitpuffer1_2 = visual.TextStim(win=win, name='zeitpuffer1_2',
    text=None,
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "trial"
trialClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text=None,
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color=[-0.5, -0.5, -0.5], colorSpace='rgb', opacity=1,
    depth=0.0);
from numpy import (log)
maxsize=0
minsize=3000
timer = 0



# Initialize components for Routine "trial_pause"
trial_pauseClock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "pause1b"
pause1bClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='default text',
    font='Arial',
    pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "pause2"
pause2Clock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='default text',
    font='Arial',
    pos=(0, 0), height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "Audio_Cleanup"
Audio_CleanupClock = core.Clock()


# Initialize components for Routine "end_text"
end_textClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text='    End of experiment  \n\nThank you for participating\n',
    font='Arial',
    pos=[0, 0], height=20, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "iViewX_Connect"-------
t = 0
iViewX_ConnectClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
iViewX_ConnectComponents = []
for thisComponent in iViewX_ConnectComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "iViewX_Connect"-------
while continueRoutine:
    # get current time
    t = iViewX_ConnectClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in iViewX_ConnectComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "iViewX_Connect"-------
for thisComponent in iViewX_ConnectComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "iViewX_Connect" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Audio_Setup"-------
t = 0
Audio_SetupClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
from pyo import *
server = Server(buffersize=1024,duplex=0, winhost="asio").boot()
server.start()

refresh_rate = 60 # sampling rate 

#create new file

data_filename = 'data/exp_text_data/audioexp_' + expInfo['session'] +'.txt'
f = open(data_filename,'w')
f.write('\nDate and Time\n')
f.write(data.getDateStr())
f.close()
# keep track of which components have finished
Audio_SetupComponents = []
for thisComponent in Audio_SetupComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Audio_Setup"-------
while continueRoutine:
    # get current time
    t = Audio_SetupClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Audio_SetupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Audio_Setup"-------
for thisComponent in Audio_SetupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Audio_Setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "bl_instructions"-------
    t = 0
    bl_instructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    
    
    if trial_method_order[trials.thisN] == 0:
        print("test")
        method_name = "Parking Sensor Beeps\n"
        method_desc = "Shorter gaps between beeps means a larger pupil size\n"
    
    elif trial_method_order[trials.thisN] == 1:
        method_name = "Pitch Feedback\n"
        method_desc = "Higher frequency means larger pupil size\n"
    
    elif trial_method_order[trials.thisN] == 2:
        method_name = "No Audio Feedback\n"
        method_desc = "\n"
    
    custom_routine_text = "Trying section\n\n" + method_name + method_desc + "\n\nPress space to continue"
    #routine_text = "Trying section\n Press space to continue"
    
    print(custom_routine_text)
    key_resp_4 = event.BuilderKeyResponse()
    baseline_instructions.setText(custom_routine_text)
    # keep track of which components have finished
    bl_instructionsComponents = [key_resp_4, baseline_instructions]
    for thisComponent in bl_instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "bl_instructions"-------
    while continueRoutine:
        # get current time
        t = bl_instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *key_resp_4* updates
        if t >= 0.0 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_4.keys = theseKeys[-1]  # just the last key pressed
                key_resp_4.rt = key_resp_4.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *baseline_instructions* updates
        if t >= 0.0 and baseline_instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            baseline_instructions.tStart = t
            baseline_instructions.frameNStart = frameN  # exact frame index
            baseline_instructions.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bl_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "bl_instructions"-------
    for thisComponent in bl_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys=None
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    # the Routine "bl_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "baseline_b4try"-------
    t = 0
    baseline_b4tryClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    #-----------------------------------
    # Begin Routine
    #-----------------------------------
    bsize_liste = [0]*900 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
    # starting values
    bsize = 0
    state_no = 0
    lmarker = -1 
    delay_size = 2
    #---------------------
    # filter preferences
    step_limit = 0.19    # 30Hz: 0.19 | 60Hz: 0.09
    lower_th = 1
    
    # keep track of which components have finished
    baseline_b4tryComponents = [b_zeitpuffer1_2_]
    for thisComponent in baseline_b4tryComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "baseline_b4try"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = baseline_b4tryClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *b_zeitpuffer1_2_* updates
        if t >= 0.0 and b_zeitpuffer1_2_.status == NOT_STARTED:
            # keep track of start time/frame for later
            b_zeitpuffer1_2_.tStart = t
            b_zeitpuffer1_2_.frameNStart = frameN  # exact frame index
            b_zeitpuffer1_2_.setAutoDraw(True)
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if b_zeitpuffer1_2_.status == STARTED and t >= frameRemains:
            b_zeitpuffer1_2_.setAutoDraw(False)
        res = iViewXAPI.iV_GetSample(byref(sampleData))
        bsize =(sampleData.leftEye.diam) # /32 für highspeed eyetracker, ohne /32 für RED
        
        #--------------------
        # state 0: starting
        #--------------------
        if state_no == 0:
         if lmarker < 1:
          lmarker = lmarker + 1
          bsize_liste[lmarker] = bsize
          state_next = 0
         
         else:  
          if bsize > lower_th and bsize_liste[lmarker] > lower_th and bsize_liste[lmarker-1] > lower_th and (abs(bsize-bsize_liste[lmarker]) <= step_limit) and (abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit):
           lmarker = lmarker + 1
           bsize_liste[lmarker] = bsize
           state_next = 1
          else:
           bsize_liste[lmarker-1] = bsize_liste[lmarker]
           bsize_liste[lmarker] = bsize
        
           state_next = 0
        
        
        #----------------------
        # state 1: observation
        #----------------------
        
        if state_no == 1:
         
         # Filter Activation
         #- - - - - - - - - - -
         if bsize <= lower_th:
          on = 1
          jump_marker = lmarker + 1 # marks values to be replaced 
          
                # Identification of last valid_value before the blink
                #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
          while on == 1:
           if bsize_liste[lmarker] >= lower_th and bsize_liste[lmarker-1] >= lower_th and bsize_liste[lmarker-2] >= lower_th and abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit and abs(bsize_liste[lmarker-1]-bsize_liste[lmarker-2]) <= step_limit:
            valid_value = bsize_liste[lmarker]
            lmarker = lmarker + 1
            for i in range(lmarker, jump_marker, 1):
             bsize_liste[i] = valid_value
        
            bsize_liste[jump_marker] = valid_value
        
            lmarker = jump_marker
            puffer_size = jump_marker + delay_size
        
            on = 0
            state_next = 2
        
           else:
            lmarker = lmarker-1
            
         else:
          lmarker = lmarker + 1
          bsize_liste[lmarker] = bsize
          
          state_next = 1
        
        #-------------------------------------------------------------
        # state 2: identification of next valid_value after the blink
        #-------------------------------------------------------------
        
        if state_no == 2:
         # collecting values following the blink
         #- - - - - - - - - - - - - - - - - - - - - -
         if lmarker < puffer_size:
          lmarker = lmarker + 1
          bsize_liste[lmarker] = bsize
        
          state_next = 2
        
         else:
        # identification of next valid_value after the blink
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - 
          if bsize > lower_th and abs(bsize-bsize_liste[lmarker]) <= step_limit and abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit:               
           lmarker = lmarker + 1
           bsize_liste[lmarker] = bsize
           
           state_next = 1
        
          else:
           lmarker = lmarker + 1
           bsize_liste[lmarker] = bsize
           bsize_liste[lmarker-2] = valid_value
           
           state_next = 2
        
        state_no = state_next
        
        #baseline_liste.append(sampleData.leftEye.diam/32)
        #
        line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
        line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
        line1.draw()
        line2.draw()
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baseline_b4tryComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "baseline_b4try"-------
    for thisComponent in baseline_b4tryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #-----------------------------------
    # End Routine
    #-----------------------------------  
    
    # computing baseline mean
    bsize_liste = filter(None, bsize_liste)
    if len(bsize_liste) != 0:
        baselinemean = round((sum(bsize_liste)/(len(bsize_liste))),2)
        # computing baseline sd
        baselinesd = abs(round(numpy.std(bsize_liste),8))
    else :
        f = open(data_filename,'a')
        f.write('\nERROR: no data for trying baseline ' + labels[trial_method_order[trials.thisN]] + '\n')
        f.close
        baselinemean = 5.0
        baselinesd = 0
    
    
    #target values for pupil size
    sd1_target = baselinemean + baselinesd
    sd2_target = baselinemean + baselinesd + baselinesd;
    
    #--------------------------------------------------------------------------
    # savings:
    
    trials.addData('Trying_Baseline_Liste_' + labels[trials.thisN], bsize_liste)
    trials.addData('Trying_Baseline_Mean_'+  labels[trials.thisN], baselinemean)
    trials.addData('Trying_Baseline_SD_'+  labels[trials.thisN], baselinesd)
    trials.addData('Trying_SD1_Target_'+  labels[trials.thisN], sd1_target)
    trials.addData('Trying_SD2_Target_'+  labels[trials.thisN], sd2_target)
    
    #save data to file
    f = open(data_filename,'a')
    
    f.write('\nTryingBaselineList_' +  labels[trial_method_order[trials.thisN]] + '\n')
    f.write(str(bsize_liste))
    
    f.write('\nTryingBaselineMean_' +  labels[trial_method_order[trials.thisN]] + '\n')
    f.write(str(baselinemean))
    
    f.write('\nTryingBaselineSD_' +  labels[trial_method_order[trials.thisN]] + '\n')
    f.write(str(baselinesd))
    
    f.write('\nTryingBaselineSD1target_' +  labels[trial_method_order[trials.thisN]] + '\n')
    f.write(str(sd1_target))
    
    f.write('\nTryingBaselineSD2target_' +  labels[trial_method_order[trials.thisN]] + '\n')
    f.write(str(sd2_target))
    
    f.close()
    
    
    
    
    # ------Prepare to start Routine "trying"-------
    t = 0
    tryingClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    startTime = time.time()
    
    psizeliste = [0]*36000 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
    #psizeliste_displayed = [0]*36000
    psize = 0
    
    #SOUND SETUP
    #mean calculation parameters:
    avg_length = 20
    recent_avg = 0.0
    recent_total = 0.0
    
    testCount = 0
    
    #setup parking sensor
    if trial_method_order[trials.thisN] == 0:
        #create metronome for clicks - with envelope
        t1 = CosTable([(0,0), (100,1), (500,.3), (800,0)])
        clicks = Metro(time=1.0, poly=1)
        met_amp = TrigEnv(clicks, table=t1, dur=.25, mul=0.3)
        a = Sine(freq=1000, mul=met_amp).out()
    
        # create envelope for continuous tone
        tone = Adsr(attack=0.1, decay=0.4, sustain=0.5, release=0.1, dur=0, mul=0.5)
        b = Sine(freq=1000, mul=tone).out()
    
    elif trial_method_order[trials.thisN] == 1:
        synth = Sine(mul=0.5)   
        synth.setFreq(float(mapToOutputRange(baselinemean,sd2_target)))
        synth.out()
    
    #panning - no longer needed
    #elif trial_method_order[trials.thisN] == 2:
        #angle1 = 1
        #angle2 = 0
        #threshold1 = baselinemean-2*baselinesd
        #threshold2 = baselinemean+2*baselinesd
        #sig1 = Sine(mul=.5)
        #p = Pan(sig1, outs=2, pan=1).out()
    
    #---------------------
    # starting values
    state_no = 0
    lmarker = -1 
    delay_size = 2
    #---------------------
    # filter preferences
    step_limit = 0.09    # 30Hz: 0.19 | 60Hz: 0.09
    lower_th = 1
    timer = 0
    
    
    key_resp_6 = event.BuilderKeyResponse()
    # keep track of which components have finished
    tryingComponents = [text_12, key_resp_6]
    for thisComponent in tryingComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trying"-------
    while continueRoutine:
        # get current time
        t = tryingClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_12* updates
        if t >= 0.0 and text_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_12.tStart = t
            text_12.frameNStart = frameN  # exact frame index
            text_12.setAutoDraw(True)
        frameRemains = 0.0 + 600- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_12.status == STARTED and t >= frameRemains:
            text_12.setAutoDraw(False)
        
        #-----------------------------------
        # Each Frame
        #-----------------------------------
        # eye-tracker data
        res = iViewXAPI.iV_GetSample(byref(sampleData))
        psize =(sampleData.leftEye.diam) # /32 für highspeed eyetracker, ohne /32 für RED
        
        #--------------------
        # state 0: starting
        #--------------------
        if state_no == 0:
         if lmarker < 1:
          lmarker = lmarker + 1
          psizeliste[lmarker] = psize
          state_next = 0
         
         else:
          if psize > lower_th and psizeliste[lmarker] > lower_th and psizeliste[lmarker-1] > lower_th and (abs(psize-psizeliste[lmarker]) <= step_limit) and (abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit):
           lmarker = lmarker + 1
           psizeliste[lmarker] = psize
           state_next = 1
          else:
           psizeliste[lmarker-1] = psizeliste[lmarker]
           psizeliste[lmarker] = psize
           state_next = 0
        
        
        #----------------------
        # state 1: observation
        #----------------------
        
        if state_no == 1:
         plot_marker = 1 
         # Filter Activation
         #- - - - - - - - - - -
         if psize <= lower_th:
          on = 1
          jump_marker = lmarker + 1 # marks values to be replaced 
          # Identification of last valid_value before the blink
          #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
          while on == 1:
           if psizeliste[lmarker] >= lower_th and psizeliste[lmarker-1] >= lower_th and psizeliste[lmarker-2] >= lower_th and abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit and abs(psizeliste[lmarker-1]-psizeliste[lmarker-2]) <= step_limit:
            valid_value = psizeliste[lmarker]
            lmarker = lmarker + 1
            # replacing values
            for i in range(lmarker, jump_marker, 1):
             psizeliste[i] = valid_value
            psizeliste[jump_marker] = valid_value
            lmarker = jump_marker
            puffer_size = jump_marker + delay_size
            on = 0
            state_next = 2
           else:
            lmarker = lmarker-1
         else:
          lmarker = lmarker + 1
          psizeliste[lmarker] = psize
          state_next = 1
        #-------------------------------------------------------------
        # state 2: identification of next valid_value after the blink
        #-------------------------------------------------------------
        if state_no == 2:
         plot_marker = 1
         # collecting values following the blink
         #- - - - - - - - - - - - - - - - - - - - - -
         if lmarker < puffer_size:
          lmarker = lmarker + 1
          psizeliste[lmarker] = psize
          state_next = 2
        
         else:
         # identification of next valid_value after the blink
         #- - - - - - - - - - - - - - - - - - - - - - - - - - - - 
          if psize > lower_th and abs(psize-psizeliste[lmarker]) <= step_limit and abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit:               
           lmarker = lmarker + 1
           psizeliste[lmarker] = psize
           state_next = 1
          else:
           lmarker = lmarker + 1
           psizeliste[lmarker] = psize
           psizeliste[lmarker-2] = valid_value
           state_next = 2
        
        timer = timer + 1
        
        
        
        #make some noise--------------------------------------------------------
        # update sound generation - average
        if lmarker == 0:
            recent_avg = psizeliste[0]
        elif lmarker < avg_length:
            recent_avg = ((recent_avg * lmarker) + psizeliste[lmarker]) / (lmarker+1)
        
        else:
            recent_total = 0.0
            for x in range(0, avg_length):
                recent_total += psizeliste[lmarker - x]
            recent_avg = recent_total / avg_length
        
        #parking sensor
        if trial_method_order[trials.thisN] == 0:
                #if pupil size is less than target
                if recent_avg < sd2_target:
                    if clicks.isPlaying() == False:
                        tone.stop()
                        clicks.play()
                    else:
                        clicks.setTime(float(mapToTimeOutputRange(recent_avg, sd2_target)))
                else:
                #if pupil is wider than target width
                    if clicks.isPlaying():
                        clicks.stop() 
                    if tone.isPlaying() == False:
                        tone.play()
        
        #frequency
        elif trial_method_order[trials.thisN] == 1:
            # adjust frequency of sine wave depending on average
            if lmarker > avg_length:
                synth.setFreq(float(mapToOutputRange(recent_avg, sd2_target)))
                #synth.out()
        
        #panning
        #elif trial_method_order[trials.thisN] == 2:
        #    b = (angle1*threshold2 - angle2/threshold1) / (threshold2-threshold1)
        #    a = (angle1 - b)/threshold1
        #    newLocation = (float) (a*recent_avg + b)
        #    if newLocation >= 1: 
        #        newLocation = 1
        #    elif newLocation <= 0: 
        #        newLocation = 0
        #    p.setPan(newLocation)
        
        #draw cross
        line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
        line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
        line1.draw()
        line2.draw()
        #- - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        state_no = state_next
        
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_6.keys = theseKeys[-1]  # just the last key pressed
                key_resp_6.rt = key_resp_6.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tryingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trying"-------
    for thisComponent in tryingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #synth.stop()
    
    #parking sensor
    if trial_method_order[trials.thisN] == 0:
        clicks.stop()
        tone.stop()
    elif trial_method_order[trials.thisN] == 1:
        synth.stop()
    #elif trial_method_order[trials.thisN] == 2:
    #    p.stop()
    
    
    psizeliste = filter(None, psizeliste)
    
    if len(psizeliste) != 0:
        psizemean = round((sum(psizeliste)/(len(psizeliste))),2)
    else :
        psizemean = 0
        f = open(data_filename,'a')
        f.write('\nERROR: no data for trying ' + labels[trial_method_order[trials.thisN]] + '\n')
        f.close
    
    
    f = open(data_filename,'a')
    f.write('\nTrying_Pupil_Data_' +  labels[trial_method_order[trials.thisN]] + '\n')
    f.write(str(psizeliste))
    
    f.write('\nTrying_Pupil_Mean_' +  labels[trial_method_order[trials.thisN]] + '\n')
    f.write(str(psizemean))
    
    f.write('\nTrying_Time_' +  labels[trial_method_order[trials.thisN]] + '\n')
    endtime = time.time() - startTime
    f.write(str(endtime))
    
    f.close()
    
    
    
    
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys=None
    trials.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        trials.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "trying" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "pause"-------
    t = 0
    pauseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5 = event.BuilderKeyResponse()
    # keep track of which components have finished
    pauseComponents = [Puffer, key_resp_5]
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pause"-------
    while continueRoutine:
        # get current time
        t = pauseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Puffer* updates
        if t >= 0.0 and Puffer.status == NOT_STARTED:
            # keep track of start time/frame for later
            Puffer.tStart = t
            Puffer.frameNStart = frameN  # exact frame index
            Puffer.setAutoDraw(True)
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    activ_loop = data.TrialHandler(nReps=2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='activ_loop')
    thisExp.addLoop(activ_loop)  # add the loop to the experiment
    thisActiv_loop = activ_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisActiv_loop.rgb)
    if thisActiv_loop != None:
        for paramName in thisActiv_loop:
            exec('{} = thisActiv_loop[paramName]'.format(paramName))
    
    for thisActiv_loop in activ_loop:
        currentLoop = activ_loop
        # abbreviate parameter names if possible (e.g. rgb = thisActiv_loop.rgb)
        if thisActiv_loop != None:
            for paramName in thisActiv_loop:
                exec('{} = thisActiv_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "activ"-------
        t = 0
        activClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # update component parameters for each repeat
        #determine activation
        #if int(expInfo["session"]) % 12 > 5:
        #    start_w_activation = True
        #else :
        #    start_w_activation = False
        
        start_w_activation = int(expInfo["session"]) % 12 < 6
        
        #set current activation
        current_activation = start_w_activation
        
        if activ_loop.thisN == 0:
            #record to file
            #thisExp.addData('Start_with_activation', start_w_activation)
            f = open(data_filename,'a')
            f.write('\nStart with activation\n' + str(start_w_activation))
            f.close()
        else:
            current_activation = not current_activation
        
        
        #create text
        if current_activation == True:
            activation_out_text = "Activation section\n\n\nTry to increase your pupil size \nwhen the cross turns red"
            activation_end_text = "End of activation section"
        else :
            activation_out_text = "Deactivation section\n\n\nTry to decrease your pupil size \nwhen the cross turns green"
            activation_end_text = "End of deactivation section"
        key_resp_9 = event.BuilderKeyResponse()
        text_15.setText(activation_out_text)
        # keep track of which components have finished
        activComponents = [key_resp_9, text_15]
        for thisComponent in activComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "activ"-------
        while continueRoutine:
            # get current time
            t = activClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *key_resp_9* updates
            if t >= 0.0 and key_resp_9.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_9.tStart = t
                key_resp_9.frameNStart = frameN  # exact frame index
                key_resp_9.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if key_resp_9.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_9.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_9.rt = key_resp_9.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_15* updates
            if t >= 0.0 and text_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_15.tStart = t
                text_15.frameNStart = frameN  # exact frame index
                text_15.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in activComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "activ"-------
        for thisComponent in activComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # check responses
        if key_resp_9.keys in ['', [], None]:  # No response was made
            key_resp_9.keys=None
        activ_loop.addData('key_resp_9.keys',key_resp_9.keys)
        if key_resp_9.keys != None:  # we had a response
            activ_loop.addData('key_resp_9.rt', key_resp_9.rt)
        # the Routine "activ" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        train = data.TrialHandler(nReps=5, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='train')
        thisExp.addLoop(train)  # add the loop to the experiment
        thisTrain = train.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrain.rgb)
        if thisTrain != None:
            for paramName in thisTrain:
                exec('{} = thisTrain[paramName]'.format(paramName))
        
        for thisTrain in train:
            currentLoop = train
            # abbreviate parameter names if possible (e.g. rgb = thisTrain.rgb)
            if thisTrain != None:
                for paramName in thisTrain:
                    exec('{} = thisTrain[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "baseline"-------
            t = 0
            baselineClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(5.000000)
            # update component parameters for each repeat
            #-----------------------------------
            # Begin Routine
            #-----------------------------------
            bsize_liste = [0]*36000 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
            bsize = 0
            # starting values
            state_no = 0
            lmarker = -1 
            delay_size = 2
            
            #---------------------
            # filter preferences
            step_limit = 0.19    # 30Hz: 0.19 | 60Hz: 0.09
            lower_th = 1
            
            #SOUND SETUP
            #mean calculation parameters:
            avg_length = 10
            recent_avg = 0.0
            
            sd2_target = 6.0
            
            #setup parking sensor
            #if trial_method_order[trials.thisN] == 0:
                #create metronome for clicks - with envelope
            #    t1 = CosTable([(0,0), (100,1), (500,.3), (800,0)])
            #    clicks = Metro(time=1.0, poly=1)
            #    met_amp = TrigEnv(clicks, table=t1, dur=.25, mul=0.3)
            #    a = Sine(freq=1000, mul=met_amp).out()
            
                # create envelope for continuous tone
            #    tone = Adsr(attack=0.1, decay=0.4, sustain=0.5, release=0.1, dur=0, mul=0.5)
            #    b = Sine(freq=1000, mul=tone).out()
            
            #freq setup
            #elif trial_method_order[trials.thisN] == 1:
            #    synth = Sine(mul=0.5)
            #    synth.setFreq(float(mapToOutputRange(baselinemean, sd2_target)))
            #    synth.out()
            # keep track of which components have finished
            baselineComponents = [zeitpuffer1]
            for thisComponent in baselineComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "baseline"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = baselineClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *zeitpuffer1* updates
                if t >= 0.0 and zeitpuffer1.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    zeitpuffer1.tStart = t
                    zeitpuffer1.frameNStart = frameN  # exact frame index
                    zeitpuffer1.setAutoDraw(True)
                frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if zeitpuffer1.status == STARTED and t >= frameRemains:
                    zeitpuffer1.setAutoDraw(False)
                res = iViewXAPI.iV_GetSample(byref(sampleData))
                bsize =(sampleData.leftEye.diam) # /32 für highspeed eyetracker, ohne /32 für RED
                
                #--------------------
                # state 0: starting
                #--------------------
                if state_no == 0:
                 if lmarker < 1:
                  lmarker = lmarker + 1
                  bsize_liste[lmarker] = bsize
                  state_next = 0
                 
                 else:  
                  if bsize > lower_th and bsize_liste[lmarker] > lower_th and bsize_liste[lmarker-1] > lower_th and (abs(bsize-bsize_liste[lmarker]) <= step_limit) and (abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit):
                   lmarker = lmarker + 1
                   bsize_liste[lmarker] = bsize
                   state_next = 1
                  else:
                   bsize_liste[lmarker-1] = bsize_liste[lmarker]
                   bsize_liste[lmarker] = bsize
                
                   state_next = 0
                
                
                #----------------------
                # state 1: observation
                #----------------------
                
                if state_no == 1:
                 
                 # Filter Activation
                 #- - - - - - - - - - -
                 if bsize <= lower_th:
                  on = 1
                  jump_marker = lmarker + 1 # marks values to be replaced 
                  
                        # Identification of last valid_value before the blink
                        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                  while on == 1:
                   if bsize_liste[lmarker] >= lower_th and bsize_liste[lmarker-1] >= lower_th and bsize_liste[lmarker-2] >= lower_th and abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit and abs(bsize_liste[lmarker-1]-bsize_liste[lmarker-2]) <= step_limit:
                    valid_value = bsize_liste[lmarker]
                    lmarker = lmarker + 1
                    for i in range(lmarker, jump_marker, 1):
                     bsize_liste[i] = valid_value
                
                    bsize_liste[jump_marker] = valid_value
                
                    lmarker = jump_marker
                    puffer_size = jump_marker + delay_size
                
                    on = 0
                    state_next = 2
                
                   else:
                    lmarker = lmarker-1
                    
                 else:
                  lmarker = lmarker + 1
                  bsize_liste[lmarker] = bsize
                  
                  state_next = 1
                
                #-------------------------------------------------------------
                # state 2: identification of next valid_value after the blink
                #-------------------------------------------------------------
                
                if state_no == 2:
                 # collecting values following the blink
                 #- - - - - - - - - - - - - - - - - - - - - -
                 if lmarker < puffer_size:
                  lmarker = lmarker + 1
                  bsize_liste[lmarker] = bsize
                
                  state_next = 2
                
                 else:
                # identification of next valid_value after the blink
                #- - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                  if bsize > lower_th and abs(bsize-bsize_liste[lmarker]) <= step_limit and abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit:               
                   lmarker = lmarker + 1
                   bsize_liste[lmarker] = bsize
                   
                   state_next = 1
                
                  else:
                   lmarker = lmarker + 1
                   bsize_liste[lmarker] = bsize
                   bsize_liste[lmarker-2] = valid_value
                   
                   state_next = 2
                
                #make some noise--------------------------------------------------------
                # update sound generation - average
                #if lmarker <= 0:
                #    recent_avg = bsize_liste[0]
                #elif lmarker <= avg_length:
                #    recent_avg = ((recent_avg * lmarker) + bsize_liste[lmarker]) / (lmarker+1)
                #else:
                #    #print(str(lmarker))
                #    #recent_avg = ((recent_avg * (avg_length-1)) + bsize_liste[lmarker]) / avg_length 
                #    recent_avg = ((recent_avg * avg_length) - bsize_liste[lmarker-avg_length] + bsize_liste[lmarker]) / avg_length
                
                #parking sensor
                #if trial_method_order[trials.thisN] == 0:
                #        #if pupil size is less than target
                #        if recent_avg < sd2_target:
                #            if clicks.isPlaying() == False:
                #                tone.stop()
                #                clicks.play()
                #            else:
                #                clicks.setTime(float(mapToTimeOutputRange(recent_avg, sd2_target)))
                #        else:
                #        #if pupil is wider than target width
                #            if clicks.isPlaying():
                #                clicks.stop() 
                #                tone.play()
                
                #freq output
                #elif trial_method_order[trials.thisN] == 1:
                #    if lmarker > avg_length:
                #        synth.setFreq(float(mapToOutputRange(recent_avg, sd2_target)))
                
                state_no = state_next
                
                #baseline_liste.append(sampleData.leftEye.diam/32)
                #
                line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
                line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
                line1.draw()
                line2.draw()
                
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in baselineComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "baseline"-------
            for thisComponent in baselineComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            #-----------------------------------
            # End Routine
            #-----------------------------------  
            
            # computing baseline mean
            bsize_liste = filter(None, bsize_liste)
            if len(bsize_liste) != 0:
                baselinemean = round((sum(bsize_liste)/(len(bsize_liste))),2)
                # computing baseline sd
                baselinesd = abs(round(numpy.std(bsize_liste),8))
            else :
                baselinesd = 0
                baselinemean = 5.0
                f = open(data_filename,'a')
                f.write('\nERROR: no data for ' + labels[trial_method_order[trials.thisN]] +labelstr +str(train.thisN) + '\n')
                f.close()
            
            
            #--------------------------------------------------------------------------
            # saving:
            #thisExp.addData('Baseline_Data_' + labels[trials.thisN] +actlabels[activ_loop.thisN] +str(train.thisN), bsize_liste)
            #thisExp.addData('Baseline_Mean_' +  labels[trials.thisN]+actlabels[activ_loop.thisN] +str(train.thisN), baselinemean)
            #thisExp.addData('Baseline_SD_' + labels[trials.thisN]+actlabels[activ_loop.thisN] +str(train.thisN), baselinesd)
            
            train.addData('Baseline_Data_' + labels[trials.thisN] +actlabels[activ_loop.thisN] +str(train.thisN), bsize_liste)
            train.addData('Baseline_Mean_' +  labels[trials.thisN]+actlabels[activ_loop.thisN] +str(train.thisN), baselinemean)
            train.addData('Baseline_SD_' + labels[trials.thisN]+actlabels[activ_loop.thisN] +str(train.thisN), baselinesd)
            
            #target values for pupil size
            sd1_target = baselinemean + baselinesd
            sd2_target = baselinemean + baselinesd + baselinesd;
            sd2_lower_target = baselinemean - baselinesd - baselinesd;
            
            if current_activation:
                current_target = sd2_target
            else:
                current_target = sd2_lower_target
            
            f = open(data_filename,'a')
            if current_activation:
                labelstr = '_act_'
            else:
                labelstr = '_deact_'
            
            f.write('\nBaseline_Data_' + labels[trial_method_order[trials.thisN]] +labelstr +str(train.thisN) + '\n')
            f.write(str(bsize_liste))
            
            f.write('\nBaseline_Mean_' + labels[trial_method_order[trials.thisN]] +labelstr +str(train.thisN) + '\n')
            f.write(str(baselinemean))
            
            f.write('\nBaseline_SD_' + labels[trial_method_order[trials.thisN]] +labelstr +str(train.thisN) + '\n')
            f.write(str(baselinesd))
            
            
            f.write('\nTarget_' + labels[trial_method_order[trials.thisN]] +labelstr +str(train.thisN) + '\n')
            f.write(str(current_target))
            
            #f.write('\nTarget_sd2_lower' + labels[trial_method_order[trials.thisN]] +labelstr +str(train.thisN) + '\n')
            #f.write(str(sd2_lower_target))
            
            f.close()
            
            # ------Prepare to start Routine "trial_gap"-------
            t = 0
            trial_gapClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            #-----------------------------------
            # Begin Routine
            #-----------------------------------
            bsize_liste = [0]*9000 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
            bsize = 0
            # starting values
            state_no = 0
            lmarker = -1 
            delay_size = 2
            
            #---------------------
            # filter preferences
            step_limit = 0.19    # 30Hz: 0.19 | 60Hz: 0.09
            lower_th = 1
            
            #SOUND SETUP
            #mean calculation parameters:
            avg_length = 10
            recent_avg = 0.0
            
            #setup parking sensor
            if trial_method_order[trials.thisN] == 0:
                #create metronome for clicks - with envelope
                t1 = CosTable([(0,0), (100,1), (500,.3), (800,0)])
                clicks = Metro(time=1.0, poly=1)
                met_amp = TrigEnv(clicks, table=t1, dur=.25, mul=0.3)
                a = Sine(freq=1000, mul=met_amp).out()
            
                # create envelope for continuous tone
                tone = Adsr(attack=0.1, decay=0.4, sustain=0.5, release=0.1, dur=0, mul=0.5)
                b = Sine(freq=1000, mul=tone).out()
            
            #freq setup
            elif trial_method_order[trials.thisN] == 1:
                synth = Sine(mul=0.5)
                synth.setFreq(float(mapToOutputRange(baselinemean, sd2_target)))
                synth.out()
            # keep track of which components have finished
            trial_gapComponents = [zeitpuffer1_2]
            for thisComponent in trial_gapComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "trial_gap"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trial_gapClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *zeitpuffer1_2* updates
                if t >= 0.0 and zeitpuffer1_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    zeitpuffer1_2.tStart = t
                    zeitpuffer1_2.frameNStart = frameN  # exact frame index
                    zeitpuffer1_2.setAutoDraw(True)
                frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
                if zeitpuffer1_2.status == STARTED and t >= frameRemains:
                    zeitpuffer1_2.setAutoDraw(False)
                res = iViewXAPI.iV_GetSample(byref(sampleData))
                bsize =(sampleData.leftEye.diam) # /32 für highspeed eyetracker, ohne /32 für RED
                
                #--------------------
                # state 0: starting
                #--------------------
                if state_no == 0:
                 if lmarker < 1:
                  lmarker = lmarker + 1
                  bsize_liste[lmarker] = bsize
                  state_next = 0
                 
                 else:  
                  if bsize > lower_th and bsize_liste[lmarker] > lower_th and bsize_liste[lmarker-1] > lower_th and (abs(bsize-bsize_liste[lmarker]) <= step_limit) and (abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit):
                   lmarker = lmarker + 1
                   bsize_liste[lmarker] = bsize
                   state_next = 1
                  else:
                   bsize_liste[lmarker-1] = bsize_liste[lmarker]
                   bsize_liste[lmarker] = bsize
                
                   state_next = 0
                
                
                #----------------------
                # state 1: observation
                #----------------------
                
                if state_no == 1:
                 
                 # Filter Activation
                 #- - - - - - - - - - -
                 if bsize <= lower_th:
                  on = 1
                  jump_marker = lmarker + 1 # marks values to be replaced 
                  
                        # Identification of last valid_value before the blink
                        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                  while on == 1:
                   if bsize_liste[lmarker] >= lower_th and bsize_liste[lmarker-1] >= lower_th and bsize_liste[lmarker-2] >= lower_th and abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit and abs(bsize_liste[lmarker-1]-bsize_liste[lmarker-2]) <= step_limit:
                    valid_value = bsize_liste[lmarker]
                    lmarker = lmarker + 1
                    for i in range(lmarker, jump_marker, 1):
                     bsize_liste[i] = valid_value
                
                    bsize_liste[jump_marker] = valid_value
                
                    lmarker = jump_marker
                    puffer_size = jump_marker + delay_size
                
                    on = 0
                    state_next = 2
                
                   else:
                    lmarker = lmarker-1
                    
                 else:
                  lmarker = lmarker + 1
                  bsize_liste[lmarker] = bsize
                  
                  state_next = 1
                
                #-------------------------------------------------------------
                # state 2: identification of next valid_value after the blink
                #-------------------------------------------------------------
                
                if state_no == 2:
                 # collecting values following the blink
                 #- - - - - - - - - - - - - - - - - - - - - -
                 if lmarker < puffer_size:
                  lmarker = lmarker + 1
                  bsize_liste[lmarker] = bsize
                
                  state_next = 2
                
                 else:
                # identification of next valid_value after the blink
                #- - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                  if bsize > lower_th and abs(bsize-bsize_liste[lmarker]) <= step_limit and abs(bsize_liste[lmarker]-bsize_liste[lmarker-1]) <= step_limit:               
                   lmarker = lmarker + 1
                   bsize_liste[lmarker] = bsize
                   
                   state_next = 1
                
                  else:
                   lmarker = lmarker + 1
                   bsize_liste[lmarker] = bsize
                   bsize_liste[lmarker-2] = valid_value
                   
                   state_next = 2
                
                #make some noise--------------------------------------------------------
                if trial_method_order[trials.thisN] == 0 or trial_method_order[trials.thisN] == 1:
                
                    # update sound generation - average
                    if lmarker <= 0:
                        recent_avg = bsize_liste[0]
                    elif lmarker <= avg_length:
                        recent_avg = ((recent_avg * lmarker) + bsize_liste[lmarker]) / (lmarker+1)
                    else:
                        recent_total = 0.0
                        for x in range(0, avg_length):
                            recent_total += bsize_liste[lmarker - x]
                        recent_avg = recent_total / avg_length
                
                    #parking sensor
                    if trial_method_order[trials.thisN] == 0:
                            #if pupil size is less than target
                            if recent_avg < sd2_target:
                                if clicks.isPlaying() == False:
                                    tone.stop()
                                    clicks.play()
                                else:
                                    clicks.setTime(float(mapToTimeOutputRange(recent_avg, sd2_target)))
                            else:
                            #if pupil is wider than target width
                                if clicks.isPlaying():
                                    clicks.stop() 
                                    tone.play()
                
                    #freq output
                    elif trial_method_order[trials.thisN] == 1:
                        if lmarker > avg_length:
                            synth.setFreq(float(mapToOutputRange(recent_avg, sd2_target)))
                
                state_no = state_next
                
                #baseline_liste.append(sampleData.leftEye.diam/32)
                #
                line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
                line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
                line1.draw()
                line2.draw()
                
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_gapComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trial_gap"-------
            for thisComponent in trial_gapComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            #-----------------------------------
            # End Routine
            #-----------------------------------  
            
            
            bsize_liste = filter(None, bsize_liste)
            
            f = open(data_filename,'a')
            if current_activation:
                labelstr = '_act_'
            else:
                labelstr = '_deact_'
            
            f.write('\nTrialGap_Data_' + labels[trial_method_order[trials.thisN]] +labelstr +str(train.thisN) + '\n')
            f.write(str(bsize_liste))
            
            
            f.close()
            
            # ------Prepare to start Routine "trial"-------
            t = 0
            trialClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(10.000000)
            # update component parameters for each repeat
            psizeliste = [0]*36000
            psize = 0
            
            #elif trial_method_order[trials.thisN] == 2:
            #    angle1 = 1
            #    angle2 = 0
            #    threshold1 = baselinemean-2*baselinesd
            #    threshold2 = baselinemean+2*baselinesd
            #    sig1 = Sine(mul=.5)
            #    p = Pan(sig1, outs=2, pan=1).out()
            
            #---------------------
            # starting values
            state_no = 0
            lmarker = -1 
            delay_size = 2
            
            #---------------------
            # filter preferences
            step_limit = 0.09    # 30Hz: 0.19 | 60Hz: 0.09
            lower_th = 1
            timer = 0
            
            #success tracker variables
            threshold_reached = False
            threshold_target_frames = 30
            frames_at_target = 0
            trial_start_time = time.time()
            success_time = -1
            key_resp_12 = event.BuilderKeyResponse()
            # keep track of which components have finished
            trialComponents = [text_6, key_resp_12]
            for thisComponent in trialComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "trial"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trialClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_6* updates
                if t >= 0.0 and text_6.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_6.tStart = t
                    text_6.frameNStart = frameN  # exact frame index
                    text_6.setAutoDraw(True)
                frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_6.status == STARTED and t >= frameRemains:
                    text_6.setAutoDraw(False)
                
                #-----------------------------------
                # Each Frame
                #-----------------------------------
                # eye-tracker data
                res = iViewXAPI.iV_GetSample(byref(sampleData))
                psize =(sampleData.leftEye.diam) # /32 für highspeed eyetracker, ohne /32 für RED
                
                #--------------------
                # state 0: starting
                #--------------------
                if state_no == 0:
                 if lmarker < 1:
                  lmarker = lmarker + 1
                  psizeliste[lmarker] = psize
                  state_next = 0
                 
                 else:
                  if psize > lower_th and psizeliste[lmarker] > lower_th and psizeliste[lmarker-1] > lower_th and (abs(psize-psizeliste[lmarker]) <= step_limit) and (abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit):
                   lmarker = lmarker + 1
                   psizeliste[lmarker] = psize
                   state_next = 1
                  else:
                   psizeliste[lmarker-1] = psizeliste[lmarker]
                   psizeliste[lmarker] = psize
                   state_next = 0
                
                
                #----------------------
                # state 1: observation
                #----------------------
                
                if state_no == 1:
                 plot_marker = 1 
                 # Filter Activation
                 #- - - - - - - - - - -
                 if psize <= lower_th:
                  on = 1
                  jump_marker = lmarker + 1 # marks values to be replaced 
                  # Identification of last valid_value before the blink
                  #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                  while on == 1:
                   if psizeliste[lmarker] >= lower_th and psizeliste[lmarker-1] >= lower_th and psizeliste[lmarker-2] >= lower_th and abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit and abs(psizeliste[lmarker-1]-psizeliste[lmarker-2]) <= step_limit:
                    valid_value = psizeliste[lmarker]
                    lmarker = lmarker + 1
                    # replacing values
                    for i in range(lmarker, jump_marker, 1):
                     psizeliste[i] = valid_value
                    psizeliste[jump_marker] = valid_value
                    lmarker = jump_marker
                    puffer_size = jump_marker + delay_size
                    on = 0
                    state_next = 2
                   else:
                    lmarker = lmarker-1
                 else:
                  lmarker = lmarker + 1
                  psizeliste[lmarker] = psize
                  state_next = 1
                #-------------------------------------------------------------
                # state 2: identification of next valid_value after the blink
                #-------------------------------------------------------------
                if state_no == 2:
                 plot_marker = 1
                 # collecting values following the blink
                 #- - - - - - - - - - - - - - - - - - - - - -
                 if lmarker < puffer_size:
                  lmarker = lmarker + 1
                  psizeliste[lmarker] = psize
                  state_next = 2
                
                 else:
                 # identification of next valid_value after the blink
                 #- - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                  if psize > lower_th and abs(psize-psizeliste[lmarker]) <= step_limit and abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit:               
                   lmarker = lmarker + 1
                   psizeliste[lmarker] = psize
                   state_next = 1
                  else:
                   lmarker = lmarker + 1
                   psizeliste[lmarker] = psize
                   psizeliste[lmarker-2] = valid_value
                   state_next = 2
                
                timer = timer + 1
                
                #make some noise--------------------------------------------------------
                # update sound generation - average
                
                #if average is needed for sound
                
                if trial_method_order[trials.thisN] == 0 or trial_method_order[trials.thisN] == 1:
                
                    if lmarker <= 0:
                        recent_avg = psizeliste[0]
                    elif lmarker <= avg_length:
                        recent_avg = ((recent_avg * lmarker) + psizeliste[lmarker]) / (lmarker+1)
                    else:
                        recent_total = 0.0
                        for x in range(0, avg_length):
                            recent_total += psizeliste[lmarker - x]
                        recent_avg = recent_total / avg_length
                
                    #parking sensor
                    if trial_method_order[trials.thisN] == 0:
                            #if pupil size is less than target
                            if recent_avg < sd2_target:
                                if clicks.isPlaying() == False:
                                    tone.stop()
                                    clicks.play()
                                else:
                                    clicks.setTime(float(mapToTimeOutputRange(recent_avg, sd2_target)))
                            else:
                            #if pupil is wider than target width
                                if clicks.isPlaying():
                                    clicks.stop() 
                                    tone.play()
                
                    #freq output
                    elif trial_method_order[trials.thisN] == 1:
                        synth.setFreq(float(mapToOutputRange(recent_avg, sd2_target)))
                        if lmarker == avg_length:
                            synth.out()
                
                #work out time above threshold
                if threshold_reached == False:
                    if current_activation:
                        #search for values above threshold
                        if psizeliste[lmarker] > current_target:
                            frames_at_target +=1
                            if frames_at_target == threshold_target_frames:
                                success_time = time.time() - trial_start_time
                                threshold_reached = True
                                print(str(psizeliste[lmarker-1]) + str(psizeliste[lmarker]))
                        else:
                            frames_at_target = 0
                    else:
                        #search for values below threshold
                        if psizeliste[lmarker] < current_target:
                            frames_at_target +=1
                            if frames_at_target == threshold_target_frames:
                                success_time = time.time() - trial_start_time
                                threshold_reached = True
                                print(str(psizeliste[lmarker-1]) + str(psizeliste[lmarker]))
                        else:
                            frames_at_target = 0
                
                #draw cross
                if current_activation:
                    color = (1,-1,-1)
                else:
                    color = (-1,1,-1)
                
                line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=color)
                line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=color)
                line1.draw()
                line2.draw()
                #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                
                state_no = state_next
                
                
                # *key_resp_12* updates
                if t >= 0.0 and key_resp_12.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_12.tStart = t
                    key_resp_12.frameNStart = frameN  # exact frame index
                    key_resp_12.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
                if key_resp_12.status == STARTED and t >= frameRemains:
                    key_resp_12.status = STOPPED
                if key_resp_12.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        key_resp_12.keys = theseKeys[-1]  # just the last key pressed
                        key_resp_12.rt = key_resp_12.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trial"-------
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            #parking sensor
            if trial_method_order[trials.thisN] == 0:
                clicks.stop()
                tone.stop()
            elif trial_method_order[trials.thisN] == 1:
                synth.stop()
            
            psizeliste = filter(None, psizeliste)
            
            if len(psizeliste) != 0:
                psizemean = round((sum(psizeliste)/(len(psizeliste))),2)
            else :
                psizemean = 0
            
            
            f = open(data_filename,'a')#open a  file in 'append' mode
            if current_activation:
                labelstr = '_act_'
            else:
                labelstr = '_deact_'
            
            f.write('\nPupil_Data_' + labels[trial_method_order[trials.thisN]] +labelstr +str(train.thisN) + '\n')
            f.write(str(psizeliste))
            
            f.write('\nPupil_Mean_' + labels[trial_method_order[trials.thisN]] +labelstr +str(train.thisN) + '\n')
            f.write(str(psizemean))
            
            f.write('\nPupil_Time_to_Target_' + labels[trial_method_order[trials.thisN]] +labelstr +str(train.thisN) + '\n')
            f.write(str(success_time))
            
            f.close()
            # check responses
            if key_resp_12.keys in ['', [], None]:  # No response was made
                key_resp_12.keys=None
            train.addData('key_resp_12.keys',key_resp_12.keys)
            if key_resp_12.keys != None:  # we had a response
                train.addData('key_resp_12.rt', key_resp_12.rt)
            
            # ------Prepare to start Routine "trial_pause"-------
            t = 0
            trial_pauseClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(5.000000)
            # update component parameters for each repeat
            
            # keep track of which components have finished
            trial_pauseComponents = [text_16]
            for thisComponent in trial_pauseComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "trial_pause"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trial_pauseClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_16* updates
                if t >= 0.0 and text_16.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_16.tStart = t
                    text_16.frameNStart = frameN  # exact frame index
                    text_16.setAutoDraw(True)
                frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
                if text_16.status == STARTED and t >= frameRemains:
                    text_16.setAutoDraw(False)
                line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
                line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
                line1.draw()
                line2.draw()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_pauseComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trial_pause"-------
            for thisComponent in trial_pauseComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            thisExp.nextEntry()
            
        # completed 5 repeats of 'train'
        
        
        # ------Prepare to start Routine "pause1b"-------
        t = 0
        pause1bClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text_13.setText(activation_end_text
)
        key_resp_10 = event.BuilderKeyResponse()
        # keep track of which components have finished
        pause1bComponents = [text_13, key_resp_10]
        for thisComponent in pause1bComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "pause1b"-------
        while continueRoutine:
            # get current time
            t = pause1bClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_13* updates
            if t >= 0.0 and text_13.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_13.tStart = t
                text_13.frameNStart = frameN  # exact frame index
                text_13.setAutoDraw(True)
            
            # *key_resp_10* updates
            if t >= 0.0 and key_resp_10.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_10.tStart = t
                key_resp_10.frameNStart = frameN  # exact frame index
                key_resp_10.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if key_resp_10.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_10.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_10.rt = key_resp_10.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pause1bComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "pause1b"-------
        for thisComponent in pause1bComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_10.keys in ['', [], None]:  # No response was made
            key_resp_10.keys=None
        activ_loop.addData('key_resp_10.keys',key_resp_10.keys)
        if key_resp_10.keys != None:  # we had a response
            activ_loop.addData('key_resp_10.rt', key_resp_10.rt)
        # the Routine "pause1b" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2 repeats of 'activ_loop'
    
    
    # ------Prepare to start Routine "pause2"-------
    t = 0
    pause2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_14.setText('End of stimulus section\n\nPress space to continue\n')
    key_resp_11 = event.BuilderKeyResponse()
    routine_end_text = "End of " + method_name + " section"
    
    # keep track of which components have finished
    pause2Components = [text_14, key_resp_11]
    for thisComponent in pause2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pause2"-------
    while continueRoutine:
        # get current time
        t = pause2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_14* updates
        if t >= 0.0 and text_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_14.tStart = t
            text_14.frameNStart = frameN  # exact frame index
            text_14.setAutoDraw(True)
        
        # *key_resp_11* updates
        if t >= 0.0 and key_resp_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_11.tStart = t
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_11.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_11.keys = theseKeys[-1]  # just the last key pressed
                key_resp_11.rt = key_resp_11.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pause2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause2"-------
    for thisComponent in pause2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys=None
    trials.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        trials.addData('key_resp_11.rt', key_resp_11.rt)
    
    # the Routine "pause2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'trials'


# ------Prepare to start Routine "Audio_Cleanup"-------
t = 0
Audio_CleanupClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
server.stop()

# keep track of which components have finished
Audio_CleanupComponents = []
for thisComponent in Audio_CleanupComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Audio_Cleanup"-------
while continueRoutine:
    # get current time
    t = Audio_CleanupClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Audio_CleanupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Audio_Cleanup"-------
for thisComponent in Audio_CleanupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Audio_Cleanup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "end_text"-------
t = 0
end_textClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
end_textComponents = [text_end, key_resp_3]
for thisComponent in end_textComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end_text"-------
while continueRoutine:
    # get current time
    t = end_textClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if t >= 0.0 and text_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_end.tStart = t
        text_end.frameNStart = frameN  # exact frame index
        text_end.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_textComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_text"-------
for thisComponent in end_textComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "end_text" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()











res = iViewXAPI.iV_Disconnect()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
