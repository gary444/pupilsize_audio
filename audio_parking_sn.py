from __future__ import absolute_import, division
import sys,os, math
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
import numpy as np
from numpy.random import random, randint, normal, shuffle
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy.tools.filetools import fromFile, toFile

from iViewXAPI import *
from modules.routine_helper import RoutineHelper


######################################################################################################
######################################################################################################

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Patrick_Exp_1'
expInfo = {u'participant': u'patrick'}
#    dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
#    if dlg.OK == False:
#        core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
output_path = _thisDir + os.sep + u'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    savePickle=True, saveWideText=True,
    dataFileName=output_path)
logFile = logging.LogFile(output_path+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

######################################################################################################
######################################################################################################

# Setup the Window
win = visual.Window(
    size=[1920, 1080],
    fullscr=True,
    screen=1,
    allowGUI=True,
    allowStencil=False,
    monitor='testMonitor',
    color=[-0.3,-0.3,-0.3],
    colorSpace='rgb',
    blendMode='avg',
    useFBO=True,
    units='pix')

# Store frame rate of monitor if we can measure it
frameDur = 0
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
######################################################################################################

# Settings / params

endExpNow = False  # flag for 'escape' or other condition => quit the exp
refresh_rate = 60 # refresh rate in Hz
if refresh_rate == 30:
    setting_screen_size = 900 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
    setting_step_limit = 0.19    # 30Hz: 0.19 | 60Hz: 0.09
else: # we assume it's 60Hz
    setting_screen_size = 1900 # ca. 900 bei 30Hz | ca. 1900 bei 60Hz
    setting_step_limit = 0.09    # 30Hz: 0.19 | 60Hz: 0.09
    
bsize_liste = [0]*setting_screen_size
psizeliste = [0]*setting_screen_size
bsize = 0
nend = 0
clbsloop = 0
prev_pup_mean = 0
cur_pup_mean = 0
maxsize = 0
minsize = 3000
psize = 0
conf_escape_keys = ["escape"]
conf_total_trials = 3

# in seconds
conf_bl_timer = 5
conf_trial_instr_timer = 2
conf_trial_timer = 30
    
######################################################################################################

# ---------------------------------------------
#---- connect to iViewX
# ---------------------------------------------
print "connecting to iview X..."
res = iViewXAPI.iV_Connect(c_char_p('141.54.159.23'), c_int(4444), c_char_p('141.54.159.21'), c_int(5555))
print "connected to iViewX"
res = iViewXAPI.iV_GetSystemInfo(byref(systemData))
print "iV_GetSystemInfo: " + str(res)
print "Samplerate: " + str(systemData.samplerate)
print "iViewX Verion: " + str(systemData.iV_MajorVersion) + "." + str(systemData.iV_MinorVersion) + "." + str(systemData.iV_Buildnumber)
print "iViewX API Verion: " + str(systemData.API_MajorVersion) + "." + str(systemData.API_MinorVersion) + "." + str(systemData.API_Buildnumber)

######################################################################################################
#mappings: set range conversion here
def mapToOutputRange(inputValue, targetValue):
    input_min = 3 #mm?
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

#import audio library here so iview X can connect
from pyo import *
s = Server(buffersize=1024,duplex=0, winhost="asio").boot()


######################################################################################################

# Initialize components for Routine "bl_instructions"
bl_instructions_stim = visual.TextStim(win=win, name='baseline_instructions',
    text=u'Press space',
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color="white", colorSpace='rgb', opacity=1,
    depth=0.0);

bl_stim = visual.TextStim(win=win, name='bl_stim',
    text=None,
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color="white", colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "tr_instructions"
trial_instructions_stim = visual.TextStim(win=win, name='trial_instructions_stim',
    text='Baseline registration has ended.\n\nExperiment will start shortly.',
    font='Arial',
    units='pix', pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color="white", colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "pause"
trial_stim = visual.TextStim(win=win, name='trial_stim',
    text='End of trial.\n\nEnd with space.\n',
    font='Arial',
    pos=[0, 0], height=30, wrapWidth=None, ori=0, 
    color="white", colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine
bl_instructionsClock = core.Clock()
pauseClock = core.Clock()

######################################################################################################

#####################  Routine "iViewX_Connect"

# routine_helper
comps = []
iview_connect_clock = core.Clock()
routine_helper = RoutineHelper(win, comps)
routine_helper.reset_components()

while routine_helper.get_status():
    if not routine_helper.get_status(): break
    routine_helper.set_status(False)
    if event.getKeys(keyList=conf_escape_keys):core.quit()
    if routine_helper.get_status(): win.flip()
    
routine_helper.end_components() # end components
routineTimer.reset() # reset the non-slip timer

######################################################################################################

#####################  Trials loop setup

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=conf_total_trials, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

######################################################################################################

#####################  Trials loop

for thisTrial in trials:
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    
    ######################################################################################################
    
    #####################  Routine "Baseline instructions"
    
    # routine_helper
    t = 0
    frameN = -1
    key_resp = event.BuilderKeyResponse()
    comps = [bl_instructions_stim, key_resp]
    routine_helper = RoutineHelper(win, comps)
    routine_helper.set_stim(bl_instructions_stim)
    routine_helper.reset_components()
    
    while routine_helper.get_status():
        
        t = bl_instructionsClock.getTime()
        frameN = frameN + 1
        if t >= 0.0:
            if bl_instructions_stim.status == NOT_STARTED:
                bl_instructions_stim.tStart = t
                bl_instructions_stim.frameNStart = frameN  # exact frame index
                bl_instructions_stim.setAutoDraw(True)
        
        if t >= 0.0 and key_resp.status == NOT_STARTED:
            key_resp.tStart = t
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        
        if key_resp.status == STARTED:
            keys = event.getKeys(keyList=['space'])
            if len(keys) > 0:  # at least one key was pressed
                key_resp.keys = keys[-1]
                key_resp.rt = key_resp.clock.getTime()
                routine_helper.set_status(False)
        
        # the next 4 lines can be used for all routines
        if not routine_helper.check_comps_status(): break
        if event.getKeys(keyList=conf_escape_keys): core.quit() # exit
        if routine_helper.get_status(): win.flip() # refresh screen
    routine_helper.end_components() # end components
    
    # check responses - generic key response code
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys=None
    trials.addData('bl_instructions_key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('bl_instructions_key_resp.rt', key_resp.rt)
    # the Routine "bl_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    ######################################################################################################
    
    #####################  Routine "Baseline"
    
    ########## Important, variables to reset on each trial loop
    bsize_liste = [0]*setting_screen_size
    state_no = 0
    lmarker = -1
    delay_size = 2
    # filter preferences
    step_limit = setting_step_limit 
    lower_th = 1
    
    # Helper
    comps = [bl_stim]
    routine_helper = RoutineHelper(win,comps)
    routine_helper.set_stim(bl_stim)
    routine_helper.set_timer(conf_bl_timer)
    routine_helper.reset_components()

    routineTimer.add(conf_bl_timer)
    while routine_helper.get_status() and routineTimer.getTime() > 0:
        routine_helper.update_beginning_while() # generic
        
        ########### Get Sample from iViewX
        res = iViewXAPI.iV_GetSample(byref(sampleData))
        bsize = (sampleData.leftEye.diam) # /32 fur highspeed eyetracker, ohne /32 fur RED

        #print(sampleData)
        #--------------------
        # State 0: starting
        
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
        # State 1: observation
        
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
                        lmarker = lmarker - 1
            
            else:
                lmarker = lmarker + 1
                bsize_liste[lmarker] = bsize
          
          
            state_next = 1
        
        #-------------------------------------------------------------
        # State 2: identification of next valid_value after the blink
        
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
        line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(1, 1, 1))
        line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(1, 1, 1))
        line1.draw()
        line2.draw()
        
        # generic
        if not routine_helper.check_comps_status(): break
        if event.getKeys(keyList=conf_escape_keys): core.quit()
        if routine_helper.get_status(): win.flip()
    routine_helper.end_components()
    
    ######################################################################################################
    
    #####################  Computing baseline stats
    
    bsize_liste = filter(None, bsize_liste)
    if len(bsize_liste) == 0:
        print("no data!!!!!")
    
    # Mean
    bl_mean = round((sum(bsize_liste)/(len(bsize_liste))),2)
    
    # Standard Deviation
    bl_std = abs(round(np.std(bsize_liste),8))
    
    # Percent-change: sd / mean
    bl_pr_change = round((bl_std/bl_mean),2)
    
    # Maximum Deviation 
    bl_max_deviation = (bl_mean+(bl_mean*bl_pr_change))*35
    
    # Minimum Deviation
    bl_min_deviation = (bl_mean-(bl_mean*bl_pr_change))*35
    
    # Save data
    thisExp.addData('Baseline_List', bsize_liste)
    thisExp.addData('Baseline_Mean', bl_mean)
    thisExp.addData('Baseline_Std', bl_std)
    thisExp.addData('Baseline_Percentage_Change', bl_pr_change)
    thisExp.addData('Baseline_Max_Deviation', bl_max_deviation)
    thisExp.addData('Baseline_Min_Deviation', bl_min_deviation)
    
    
    sd1_target = bl_mean + bl_std
    sd2_target = bl_mean + bl_std + bl_std;
#    print bl_mean
#    print bl_std
#    print sd1_target
    
    
    ######################################################################################################
    
    #####################  Routine "Trial Instructions"
    
    # Helper
    comps = [trial_instructions_stim]
    routine_helper = RoutineHelper(win,comps)
    routine_helper.set_stim(trial_instructions_stim)
    routine_helper.set_timer(conf_trial_instr_timer)
    routine_helper.reset_components()
    
    routineTimer.add(conf_trial_instr_timer)
    while routine_helper.get_status() and routineTimer.getTime() > 0:
        routine_helper.update_beginning_while() # generic
        
        # generic
        if not routine_helper.check_comps_status(): break
        if event.getKeys(keyList=conf_escape_keys): core.quit()
        if routine_helper.get_status(): win.flip()
    routine_helper.end_components()
    
    ######################################################################################################
    
    #####################  Routine "Trial"
    
    ########## Important, variables to reset on each trial loop
    psizeliste = [0]*setting_screen_size
    psize = 0
    
    # starting values
    state_no = 0
    lmarker = -1
    delay_size = 2
    
    # filter preferences
    step_limit = setting_step_limit
    lower_th = 1
    
    # plot settings
    minsize = 3000
    maxsize = 0
    plot_marker = 0
    mean_length = 3
    plot_buffer = 5
    
    #abc = 0
    
    # Draw
    line1 = visual.Line(win, start=(0, -20), end=(0, 20), lineColor=(-1, -1, -1))
    line2 = visual.Line(win, start=(-20, 0), end=(20, 0), lineColor=(-1, -1, -1))
    circle2 = visual.Circle(win, edges=96, radius=bl_max_deviation,lineWidth=1, lineColor=(0 , 0, 0), fillColor=(0 , 0, 0), interpolate=True)
    circle3 = visual.Circle(win, edges=96, radius=bl_min_deviation,lineWidth=1, lineColor=(-0.3 , -0.3, -0.3), fillColor=(-0.3 , -0.3, -0.3), interpolate=True)
    circle4 = visual.Circle(win, edges=96, radius=bl_mean*35,lineWidth=2, lineColor=(-1 , -1, -1), interpolate=True)
    circle5 = visual.Circle(win, edges=96, radius=1000,lineWidth=1, lineColor=(-1 , -1, -1), interpolate=True)
    circle6 = visual.Circle(win, edges=96, radius=1000,lineWidth=1, lineColor=(-1 , -1, -1), interpolate=True)
    target_circle = visual.Circle(win, edges=96, radius=sd2_target*35,lineWidth=1, lineColor=(-1 , -1, -1), interpolate=True)
    
    
    
   #DO SOUND SETUP HERE
    s.start()
    #create metronome for clicks - with envelope
    t1 = CosTable([(0,0), (100,1), (500,.3), (800,0)])
    clicks = Metro(time=1.0, poly=1)
    met_amp = TrigEnv(clicks, table=t1, dur=.25, mul=0.3)
    a = Sine(freq=1000, mul=met_amp).out()
    
    #create audio player for success noise
    sf = SfPlayer("sounds/bell1.wav")
    #ding = Trig(sf)

    # create envelope for continuous tone
    #tone = Adsr(attack=0.1, decay=0.4, sustain=0.5, release=0.1, dur=0, mul=0.5)
    #create wave generator for tone - takes env as it's multiplier
    #b = Sine(freq=1000, mul=tone).out()
    #avg last x values
    avg_length = 10
    recent_avg = 0.0
    holdCounter = 0
    holdLimit = refresh_rate / 2 #hold for half second before playing success noise
    holding = False

    #######################################    
    #######################################
    #######################################

    # Helper
    routineTimer.add(conf_trial_timer)
    
    comps = []
    routine_helper = RoutineHelper(win,comps)
    routine_helper.set_timer(conf_trial_timer)
    routine_helper.reset_components()
    
    while routine_helper.get_status() and routineTimer.getTime() > 0:
        routine_helper.update_beginning_while() # generic
        
        # Each Frame
        
        # Eye-tracker data
        
        res = iViewXAPI.iV_GetSample(byref(sampleData))
        
        psize = (sampleData.leftEye.diam) # /32 fur highspeed eyetracker, ohne /32 fur RED
        
        #--------------------
        # State 0: starting
        
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
        # State 1: observation
        
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
        # State 2: identification of next valid_value after the blink
        
        if state_no == 2:
            plot_marker = 1
            # collecting values following the blink
            
            if lmarker < puffer_size:
                lmarker = lmarker + 1
                psizeliste[lmarker] = psize
                
                state_next = 2
        
            else:
                # identification of next valid_value after the blink
                if psize > lower_th and abs(psize-psizeliste[lmarker]) <= step_limit and abs(psizeliste[lmarker]-psizeliste[lmarker-1]) <= step_limit:               
                    lmarker = lmarker + 1
                    psizeliste[lmarker] = psize
                    
                    state_next = 1
                else:
                   lmarker = lmarker + 1
                   psizeliste[lmarker] = psize
                   psizeliste[lmarker-2] = valid_value
                   
                   state_next = 2
                   
                   
        #-----------------------------------------------------------
        # update sound generation - average
        if lmarker == 0:
            recent_avg = psizeliste[0]
        elif lmarker < avg_length:
            recent_avg = ((recent_avg * lmarker) + psizeliste[lmarker]) / (lmarker+1)
        else:
            recent_avg = ((recent_avg * (avg_length-1)) + psizeliste[lmarker]) / avg_length 
            
        #if pupil size is less than target
        if recent_avg < sd2_target:
            holding = False
            if clicks.isPlaying() == False:
                sf.stop()#stop success noise
                clicks.play()#start clicks
            else:
                clicks.setTime(float(mapToOutputRange(recent_avg, sd2_target)))
        else:
        #if pupil is wider than target width
            if clicks.isPlaying():
                clicks.stop() 
                holding = True
            if holding == True: 
                holdCounter +=1
                if holdCounter == holdLimit:
                    sf.out()
                    print("triggered ding")
                    holdCounter = 0
                    holding = False
                    
        
        #- - - - - - - - - - - - - - - - - - - - - - - - - - -
        # smooth & plot data:
        
        if state_no == 0 or state_no == 1 or state_no == 2:

            if plot_marker == 1:
                # BASELINE RINGE (schwarz): MW +/-SD
                #- - - - - - - - - - - - - - - - - - - -
                #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -     
                # FEEDBACK RINGE (rot | grau): Pupillengroesse u. Extrema
                #- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                if lmarker >= mean_length + plot_buffer:
                    cur_pup_mean = 0
                    
                    for p in range(1, mean_length+1, 1):
                        cur_pup_mean = psizeliste[lmarker-p-plot_buffer] + cur_pup_mean
                        
                    cur_pup_mean = (cur_pup_mean/mean_length)*35
            
                if cur_pup_mean > maxsize and cur_pup_mean > bl_max_deviation:
                    maxsize = cur_pup_mean
                    circle5 = visual.Circle(win, edges=96, radius=maxsize,lineWidth=1, lineColor=(0.2 , 0.2, 0.2), interpolate=True)
                elif cur_pup_mean < minsize and cur_pup_mean < bl_min_deviation and cur_pup_mean != 0:
                    minsize = cur_pup_mean
                    circle6 = visual.Circle(win, edges=96, radius=minsize,lineWidth=1, lineColor=(0.2 , 0.2, 0.2), interpolate=True)
        
        # Red circle - Live eye pupil mean
        circle_cur_pup = visual.Circle(win, edges=96, radius=cur_pup_mean,lineWidth=4, lineColor=(0,-1,-1), interpolate=True)
        

      
        circle_cur_pup.draw()
        circle2.draw()
        circle3.draw()
        line1.draw()
        line2.draw()
        target_circle.draw()
        
        # Important
        state_no = state_next
        
        # generic
        if not routine_helper.check_comps_status(): break
        if event.getKeys(keyList=conf_escape_keys): core.quit()
        if routine_helper.get_status(): win.flip()
        
    routine_helper.end_components()
    
    #DO AUDIO CLEANUP HERE
    clicks.stop() 
    
    # Save Pupil stats
    psizeliste = filter(None, psizeliste)
    p_size_mean = round((sum(psizeliste)/(len(psizeliste))),2)
    
    thisExp.addData('Pupil_List', psizeliste)
    thisExp.addData('Pupil_Mean', p_size_mean)
    
    ######################################################################################################
    
    #####################  Routine "Pause"
    
    # routine_helper
    t = 0
    frameN = -1
    key_resp = event.BuilderKeyResponse()
    comps = [trial_stim, key_resp]
    routine_helper = RoutineHelper(win,comps)
    routine_helper.set_stim(trial_stim)
    routine_helper.reset_components()
    
    while routine_helper.get_status():
        
       
        
        t = pauseClock.getTime()
        frameN = frameN + 1
        if t >= 0.0:
            if trial_stim.status == NOT_STARTED:
                trial_stim.tStart = t
                trial_stim.frameNStart = frameN  # exact frame index
                trial_stim.setAutoDraw(True)
        
        if t >= 0.0 and key_resp.status == NOT_STARTED:
            key_resp.tStart = t
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        
        if key_resp.status == STARTED:
            keys = event.getKeys(keyList=['space'])
            
            if len(keys) > 0:  # at least one key was pressed
                key_resp.keys = keys[-1]
                key_resp.rt = key_resp.clock.getTime()
                routine_helper.set_status(False)
        
        # the next 4 lines can be used for all routines
        if not routine_helper.check_comps_status(): break
        if event.getKeys(keyList=conf_escape_keys): core.quit() # exit
        if routine_helper.get_status(): win.flip()
    routine_helper.end_components() # end components
    

    routineTimer.reset()
    
    # completed repeats of 'trials'
    thisExp.nextEntry()

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
    
# save data for this loop
trials.saveAsText(output_path + 'trials.csv', delim=',',
    stimOut = params,
    dataOut = ['n','all_mean','all_std', 'all_raw'])


# clean up
res = iViewXAPI.iV_Disconnect()
thisExp.saveAsWideText(output_path+'.csv')
thisExp.saveAsPickle(output_path)
logging.flush()
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
