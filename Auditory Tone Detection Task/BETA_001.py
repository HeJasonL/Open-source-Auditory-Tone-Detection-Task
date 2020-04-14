#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on Mon Apr 13 11:33:38 2020
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

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = 'BETA_001'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jasonhe/Dropbox/Documents/Projects/Auditory detection tasks AIMS Project/Auditory Tone Detection Task/BETA_001.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
Welcome_Text = visual.TextStim(win=win, name='Welcome_Text',
    text='Welcome to the Auditory Tone Detection Task\n\nPress SPACE to continue',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instructions_Text = visual.TextStim(win=win, name='Instructions_Text',
    text='In this task, you will be presented with trials. \nIn each of these trials, you will be presented with two listening intervals.\nA tone will be presented in only one of the two intervals. \n\nThe listening intervals are indicated by the numbers "1" and "2", presented on your screen.\nThe listening intervals are separated by less than a second (800ms), so make sure you are being attentive!\nAfter the two listening intervals, you must decide in which interval you heard the tone.\n\nPress SPACE for further instructions',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
Long_Tone1 = sound.Sound('1000', secs=0.20, stereo=True)
Long_Tone1.setVolume(1.0)
Delay = visual.TextStim(win=win, name='Delay',
    text='\n+\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ISI = visual.TextStim(win=win, name='ISI',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Long_Tone2 = sound.Sound('1000', secs=0.2, stereo=True)
Long_Tone2.setVolume(1.0)
Bandpass_Noise1 = sound.Sound('Noise_BP_600_1400.wav', secs=.30, stereo=True)
Bandpass_Noise1.setVolume(1)
Bandpass_Noise2 = sound.Sound('Noise_BP_600_1400.wav', secs=0.3, stereo=True)
Bandpass_Noise2.setVolume(1)
Interval1 = visual.TextStim(win=win, name='Interval1',
    text='1',
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
Interval2 = visual.TextStim(win=win, name='Interval2',
    text='2',
    font='Arial',
    pos=(0, 0), height=1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "Question"
QuestionClock = core.Clock()
Question_Text = visual.TextStim(win=win, name='Question_Text',
    text='In which interval ("1" or "2") do you think you heard the tone? \nPress "z" for "m" or press "?" for 2.\n\nIf you are unsure, just pick the interval you are most confident with.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Next"
NextClock = core.Clock()
Next_Text = visual.TextStim(win=win, name='Next_Text',
    text='Press SPACE to start the next trial',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
t = 0
WelcomeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Welcome_Response = keyboard.Keyboard()
# keep track of which components have finished
WelcomeComponents = [Welcome_Text, Welcome_Response]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome_Text* updates
    if t >= 0.0 and Welcome_Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Welcome_Text.tStart = t  # not accounting for scr refresh
        Welcome_Text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Welcome_Text, 'tStartRefresh')  # time at next scr refresh
        Welcome_Text.setAutoDraw(True)
    
    # *Welcome_Response* updates
    if t >= 0.0 and Welcome_Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        Welcome_Response.tStart = t  # not accounting for scr refresh
        Welcome_Response.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Welcome_Response, 'tStartRefresh')  # time at next scr refresh
        Welcome_Response.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(Welcome_Response.clock.reset)  # t=0 on next screen flip
        Welcome_Response.clearEvents(eventType='keyboard')
    if Welcome_Response.status == STARTED:
        theseKeys = Welcome_Response.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            Welcome_Response.keys = theseKeys.name  # just the last key pressed
            Welcome_Response.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Welcome_Text.started', Welcome_Text.tStartRefresh)
thisExp.addData('Welcome_Text.stopped', Welcome_Text.tStopRefresh)
# check responses
if Welcome_Response.keys in ['', [], None]:  # No response was made
    Welcome_Response.keys = None
thisExp.addData('Welcome_Response.keys',Welcome_Response.keys)
if Welcome_Response.keys != None:  # we had a response
    thisExp.addData('Welcome_Response.rt', Welcome_Response.rt)
thisExp.addData('Welcome_Response.started', Welcome_Response.tStartRefresh)
thisExp.addData('Welcome_Response.stopped', Welcome_Response.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Instructions_Response = keyboard.Keyboard()
# keep track of which components have finished
InstructionsComponents = [Instructions_Text, Instructions_Response]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions_Text* updates
    if t >= 0.0 and Instructions_Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions_Text.tStart = t  # not accounting for scr refresh
        Instructions_Text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Instructions_Text, 'tStartRefresh')  # time at next scr refresh
        Instructions_Text.setAutoDraw(True)
    
    # *Instructions_Response* updates
    if t >= 0.0 and Instructions_Response.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instructions_Response.tStart = t  # not accounting for scr refresh
        Instructions_Response.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Instructions_Response, 'tStartRefresh')  # time at next scr refresh
        Instructions_Response.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(Instructions_Response.clock.reset)  # t=0 on next screen flip
        Instructions_Response.clearEvents(eventType='keyboard')
    if Instructions_Response.status == STARTED:
        theseKeys = Instructions_Response.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            Instructions_Response.keys = theseKeys.name  # just the last key pressed
            Instructions_Response.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions_Text.started', Instructions_Text.tStartRefresh)
thisExp.addData('Instructions_Text.stopped', Instructions_Text.tStopRefresh)
# check responses
if Instructions_Response.keys in ['', [], None]:  # No response was made
    Instructions_Response.keys = None
thisExp.addData('Instructions_Response.keys',Instructions_Response.keys)
if Instructions_Response.keys != None:  # we had a response
    thisExp.addData('Instructions_Response.rt', Instructions_Response.rt)
thisExp.addData('Instructions_Response.started', Instructions_Response.tStartRefresh)
thisExp.addData('Instructions_Response.stopped', Instructions_Response.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
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
    
    # ------Prepare to start Routine "Trial"-------
    t = 0
    TrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.400000)
    # update component parameters for each repeat
    Long_Tone1.setSound('1000', secs=0.20)
    Long_Tone1.setVolume(probe1, log=False)
    Long_Tone2.setSound('1000', secs=0.2)
    Long_Tone2.setVolume(probe2, log=False)
    Bandpass_Noise1.setSound('Noise_BP_600_1400.wav', secs=.30)
    Bandpass_Noise1.setVolume(1, log=False)
    Bandpass_Noise2.setSound('Noise_BP_600_1400.wav', secs=0.3)
    Bandpass_Noise2.setVolume(1, log=False)
    # keep track of which components have finished
    TrialComponents = [Long_Tone1, Delay, ISI, Long_Tone2, Bandpass_Noise1, Bandpass_Noise2, Interval1, Interval2]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop Long_Tone1
        if t >= 1.05 and Long_Tone1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Long_Tone1.tStart = t  # not accounting for scr refresh
            Long_Tone1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Long_Tone1, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(Long_Tone1.play)  # screen flip
        frameRemains = 1.05 + 0.20- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Long_Tone1.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Long_Tone1.tStop = t  # not accounting for scr refresh
            Long_Tone1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Long_Tone1, 'tStopRefresh')  # time at next scr refresh
            if 0.20 > 0.5:  # don't force-stop brief sounds
                Long_Tone1.stop()
        
        # *Delay* updates
        if t >= 0.0 and Delay.status == NOT_STARTED:
            # keep track of start time/frame for later
            Delay.tStart = t  # not accounting for scr refresh
            Delay.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Delay, 'tStartRefresh')  # time at next scr refresh
            Delay.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Delay.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Delay.tStop = t  # not accounting for scr refresh
            Delay.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Delay, 'tStopRefresh')  # time at next scr refresh
            Delay.setAutoDraw(False)
        
        # *ISI* updates
        if t >= 1.3 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # not accounting for scr refresh
            ISI.frameNStart = frameN  # exact frame index
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.setAutoDraw(True)
        frameRemains = 1.3 + 0.8- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ISI.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            ISI.tStop = t  # not accounting for scr refresh
            ISI.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISI, 'tStopRefresh')  # time at next scr refresh
            ISI.setAutoDraw(False)
        # start/stop Long_Tone2
        if t >= 2.15 and Long_Tone2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Long_Tone2.tStart = t  # not accounting for scr refresh
            Long_Tone2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Long_Tone2, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(Long_Tone2.play)  # screen flip
        frameRemains = 2.15 + 0.2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Long_Tone2.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Long_Tone2.tStop = t  # not accounting for scr refresh
            Long_Tone2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Long_Tone2, 'tStopRefresh')  # time at next scr refresh
            if 0.2 > 0.5:  # don't force-stop brief sounds
                Long_Tone2.stop()
        # start/stop Bandpass_Noise1
        if t >= 1 and Bandpass_Noise1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Bandpass_Noise1.tStart = t  # not accounting for scr refresh
            Bandpass_Noise1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Bandpass_Noise1, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(Bandpass_Noise1.play)  # screen flip
        frameRemains = 1 + .30- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Bandpass_Noise1.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Bandpass_Noise1.tStop = t  # not accounting for scr refresh
            Bandpass_Noise1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Bandpass_Noise1, 'tStopRefresh')  # time at next scr refresh
            if .30 > 0.5:  # don't force-stop brief sounds
                Bandpass_Noise1.stop()
        # start/stop Bandpass_Noise2
        if t >= 2.1 and Bandpass_Noise2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Bandpass_Noise2.tStart = t  # not accounting for scr refresh
            Bandpass_Noise2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Bandpass_Noise2, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(Bandpass_Noise2.play)  # screen flip
        frameRemains = 2.1 + 0.3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Bandpass_Noise2.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Bandpass_Noise2.tStop = t  # not accounting for scr refresh
            Bandpass_Noise2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Bandpass_Noise2, 'tStopRefresh')  # time at next scr refresh
            if 0.3 > 0.5:  # don't force-stop brief sounds
                Bandpass_Noise2.stop()
        
        # *Interval1* updates
        if t >= 1 and Interval1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Interval1.tStart = t  # not accounting for scr refresh
            Interval1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Interval1, 'tStartRefresh')  # time at next scr refresh
            Interval1.setAutoDraw(True)
        frameRemains = 1 + .3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Interval1.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Interval1.tStop = t  # not accounting for scr refresh
            Interval1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Interval1, 'tStopRefresh')  # time at next scr refresh
            Interval1.setAutoDraw(False)
        
        # *Interval2* updates
        if t >= 2.1 and Interval2.status == NOT_STARTED:
            # keep track of start time/frame for later
            Interval2.tStart = t  # not accounting for scr refresh
            Interval2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Interval2, 'tStartRefresh')  # time at next scr refresh
            Interval2.setAutoDraw(True)
        frameRemains = 2.1 + 0.3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Interval2.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Interval2.tStop = t  # not accounting for scr refresh
            Interval2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Interval2, 'tStopRefresh')  # time at next scr refresh
            Interval2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Long_Tone1.stop()  # ensure sound has stopped at end of routine
    trials.addData('Long_Tone1.started', Long_Tone1.tStartRefresh)
    trials.addData('Long_Tone1.stopped', Long_Tone1.tStopRefresh)
    trials.addData('Delay.started', Delay.tStartRefresh)
    trials.addData('Delay.stopped', Delay.tStopRefresh)
    trials.addData('ISI.started', ISI.tStartRefresh)
    trials.addData('ISI.stopped', ISI.tStopRefresh)
    Long_Tone2.stop()  # ensure sound has stopped at end of routine
    trials.addData('Long_Tone2.started', Long_Tone2.tStartRefresh)
    trials.addData('Long_Tone2.stopped', Long_Tone2.tStopRefresh)
    Bandpass_Noise1.stop()  # ensure sound has stopped at end of routine
    trials.addData('Bandpass_Noise1.started', Bandpass_Noise1.tStartRefresh)
    trials.addData('Bandpass_Noise1.stopped', Bandpass_Noise1.tStopRefresh)
    Bandpass_Noise2.stop()  # ensure sound has stopped at end of routine
    trials.addData('Bandpass_Noise2.started', Bandpass_Noise2.tStartRefresh)
    trials.addData('Bandpass_Noise2.stopped', Bandpass_Noise2.tStopRefresh)
    trials.addData('Interval1.started', Interval1.tStartRefresh)
    trials.addData('Interval1.stopped', Interval1.tStopRefresh)
    trials.addData('Interval2.started', Interval2.tStartRefresh)
    trials.addData('Interval2.stopped', Interval2.tStopRefresh)
    
    # ------Prepare to start Routine "Question"-------
    t = 0
    QuestionClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Question_Response = keyboard.Keyboard()
    # keep track of which components have finished
    QuestionComponents = [Question_Text, Question_Response]
    for thisComponent in QuestionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Question"-------
    while continueRoutine:
        # get current time
        t = QuestionClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question_Text* updates
        if t >= 0.0 and Question_Text.status == NOT_STARTED:
            # keep track of start time/frame for later
            Question_Text.tStart = t  # not accounting for scr refresh
            Question_Text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Question_Text, 'tStartRefresh')  # time at next scr refresh
            Question_Text.setAutoDraw(True)
        
        # *Question_Response* updates
        if t >= 0.0 and Question_Response.status == NOT_STARTED:
            # keep track of start time/frame for later
            Question_Response.tStart = t  # not accounting for scr refresh
            Question_Response.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Question_Response, 'tStartRefresh')  # time at next scr refresh
            Question_Response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Question_Response.clock.reset)  # t=0 on next screen flip
            Question_Response.clearEvents(eventType='keyboard')
        if Question_Response.status == STARTED:
            theseKeys = Question_Response.getKeys(keyList=['z', 'm'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                Question_Response.keys = theseKeys.name  # just the last key pressed
                Question_Response.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in QuestionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Question"-------
    for thisComponent in QuestionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Question_Text.started', Question_Text.tStartRefresh)
    trials.addData('Question_Text.stopped', Question_Text.tStopRefresh)
    # check responses
    if Question_Response.keys in ['', [], None]:  # No response was made
        Question_Response.keys = None
    trials.addData('Question_Response.keys',Question_Response.keys)
    if Question_Response.keys != None:  # we had a response
        trials.addData('Question_Response.rt', Question_Response.rt)
    trials.addData('Question_Response.started', Question_Response.tStartRefresh)
    trials.addData('Question_Response.stopped', Question_Response.tStopRefresh)
    # the Routine "Question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Next"-------
    t = 0
    NextClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    Next_Response = keyboard.Keyboard()
    # keep track of which components have finished
    NextComponents = [Next_Text, Next_Response]
    for thisComponent in NextComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Next"-------
    while continueRoutine:
        # get current time
        t = NextClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_Text* updates
        if t >= 0.0 and Next_Text.status == NOT_STARTED:
            # keep track of start time/frame for later
            Next_Text.tStart = t  # not accounting for scr refresh
            Next_Text.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Next_Text, 'tStartRefresh')  # time at next scr refresh
            Next_Text.setAutoDraw(True)
        
        # *Next_Response* updates
        if t >= 0.0 and Next_Response.status == NOT_STARTED:
            # keep track of start time/frame for later
            Next_Response.tStart = t  # not accounting for scr refresh
            Next_Response.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Next_Response, 'tStartRefresh')  # time at next scr refresh
            Next_Response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Next_Response.clock.reset)  # t=0 on next screen flip
            Next_Response.clearEvents(eventType='keyboard')
        if Next_Response.status == STARTED:
            theseKeys = Next_Response.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                Next_Response.keys = theseKeys.name  # just the last key pressed
                Next_Response.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Next"-------
    for thisComponent in NextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Next_Text.started', Next_Text.tStartRefresh)
    trials.addData('Next_Text.stopped', Next_Text.tStopRefresh)
    # check responses
    if Next_Response.keys in ['', [], None]:  # No response was made
        Next_Response.keys = None
    trials.addData('Next_Response.keys',Next_Response.keys)
    if Next_Response.keys != None:  # we had a response
        trials.addData('Next_Response.rt', Next_Response.rt)
    trials.addData('Next_Response.started', Next_Response.tStartRefresh)
    trials.addData('Next_Response.stopped', Next_Response.tStopRefresh)
    # the Routine "Next" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
