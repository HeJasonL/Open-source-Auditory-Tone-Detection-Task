#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on Wed Apr 15 09:31:08 2020
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
expName = 'BETA_003'  # from the Builder filename that created this script
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
    originPath='/Users/jasonhe/Dropbox/Documents/GitHub/Open-source Auditory Tone Detection (OSATD) Task/Auditory Tone Detection Task/BETA_003_lastrun.py',
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
instructionsText = visual.TextStim(win=win, name='instructionsText',
    text='In this task, you will be presented with trials.\nIn each of these trials, you will be presented with two listening intervals.\nA tone will be presented in only one of the two intervals. \n\nThe listening intervals will be visually indicated by the numbers "1" and "2", separated by a short delay.\nAfter the two listening intervals, you must decide in which interval you heard the tone.\n\nPress SPACE for to begin',
    font='Arial',
    pos=(0, 0), height=0.030, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Trial"
TrialClock = core.Clock()

#Initial color intensity of the feedback stimulus
intensity = .5

#Initial volume of the long tones (in psychopy units)
toneVolume = 0.5
probeTone1 = sound.Sound('1000', secs=-1, stereo=True)
probeTone1.setVolume(1.0)
delay = visual.TextStim(win=win, name='delay',
    text='\n+\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ISI = visual.TextStim(win=win, name='ISI',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
probeTone2 = sound.Sound('1000', secs=-1, stereo=True)
probeTone2.setVolume(1.0)
bandpassNoise1 = sound.Sound('Noise_BP_600_1400.wav', secs=.30, stereo=True)
bandpassNoise1.setVolume(1)
bandpassNoise2 = sound.Sound('Noise_BP_600_1400.wav', secs=0.3, stereo=True)
bandpassNoise2.setVolume(1)
interval1 = visual.TextStim(win=win, name='interval1',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.75, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
interval2 = visual.TextStim(win=win, name='interval2',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.75, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "Question"
QuestionClock = core.Clock()
questionText = visual.TextStim(win=win, name='questionText',
    text='In which interval ("1" or "2") do you think you heard the tone? \n\nRespond using the number pad. If you are unsure, just pick the interval you are most confident with.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
feedbackText = visual.TextStim(win=win, name='feedbackText',
    text='default text',
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
instructionsResponse = keyboard.Keyboard()
# keep track of which components have finished
InstructionsComponents = [instructionsText, instructionsResponse]
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
    
    # *instructionsText* updates
    if t >= 0.0 and instructionsText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructionsText.tStart = t  # not accounting for scr refresh
        instructionsText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instructionsText, 'tStartRefresh')  # time at next scr refresh
        instructionsText.setAutoDraw(True)
    
    # *instructionsResponse* updates
    if t >= 0.0 and instructionsResponse.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructionsResponse.tStart = t  # not accounting for scr refresh
        instructionsResponse.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instructionsResponse, 'tStartRefresh')  # time at next scr refresh
        instructionsResponse.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instructionsResponse.clock.reset)  # t=0 on next screen flip
        instructionsResponse.clearEvents(eventType='keyboard')
    if instructionsResponse.status == STARTED:
        theseKeys = instructionsResponse.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            instructionsResponse.keys = theseKeys.name  # just the last key pressed
            instructionsResponse.rt = theseKeys.rt
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
thisExp.addData('instructionsText.started', instructionsText.tStartRefresh)
thisExp.addData('instructionsText.stopped', instructionsText.tStopRefresh)
# check responses
if instructionsResponse.keys in ['', [], None]:  # No response was made
    instructionsResponse.keys = None
thisExp.addData('instructionsResponse.keys',instructionsResponse.keys)
if instructionsResponse.keys != None:  # we had a response
    thisExp.addData('instructionsResponse.rt', instructionsResponse.rt)
thisExp.addData('instructionsResponse.started', instructionsResponse.tStartRefresh)
thisExp.addData('instructionsResponse.stopped', instructionsResponse.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=4, method='random', 
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
    # update component parameters for each repeat
    probeTone1.setSound('1000', secs=startProbe1)
    probeTone1.setVolume(toneVolume, log=False)
    probeTone2.setSound('1000', secs=startProbe2)
    probeTone2.setVolume(toneVolume, log=False)
    bandpassNoise1.setSound('Noise_BP_600_1400.wav', secs=.30)
    bandpassNoise1.setVolume(1, log=False)
    bandpassNoise2.setSound('Noise_BP_600_1400.wav', secs=0.3)
    bandpassNoise2.setVolume(1, log=False)
    # keep track of which components have finished
    TrialComponents = [probeTone1, delay, ISI, probeTone2, bandpassNoise1, bandpassNoise2, interval1, interval2]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Trial"-------
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop probeTone1
        if t >= 1.05 and probeTone1.status == NOT_STARTED:
            # keep track of start time/frame for later
            probeTone1.tStart = t  # not accounting for scr refresh
            probeTone1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(probeTone1, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(probeTone1.play)  # screen flip
        frameRemains = 1.05 + startProbe1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if probeTone1.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            probeTone1.tStop = t  # not accounting for scr refresh
            probeTone1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(probeTone1, 'tStopRefresh')  # time at next scr refresh
            if startProbe1 > 0.5:  # don't force-stop brief sounds
                probeTone1.stop()
        
        # *delay* updates
        if t >= 0.0 and delay.status == NOT_STARTED:
            # keep track of start time/frame for later
            delay.tStart = t  # not accounting for scr refresh
            delay.frameNStart = frameN  # exact frame index
            win.timeOnFlip(delay, 'tStartRefresh')  # time at next scr refresh
            delay.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if delay.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            delay.tStop = t  # not accounting for scr refresh
            delay.frameNStop = frameN  # exact frame index
            win.timeOnFlip(delay, 'tStopRefresh')  # time at next scr refresh
            delay.setAutoDraw(False)
        
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
        # start/stop probeTone2
        if t >= 2.15 and probeTone2.status == NOT_STARTED:
            # keep track of start time/frame for later
            probeTone2.tStart = t  # not accounting for scr refresh
            probeTone2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(probeTone2, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(probeTone2.play)  # screen flip
        frameRemains = 2.15 + startProbe2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if probeTone2.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            probeTone2.tStop = t  # not accounting for scr refresh
            probeTone2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(probeTone2, 'tStopRefresh')  # time at next scr refresh
            if startProbe2 > 0.5:  # don't force-stop brief sounds
                probeTone2.stop()
        # start/stop bandpassNoise1
        if t >= 1 and bandpassNoise1.status == NOT_STARTED:
            # keep track of start time/frame for later
            bandpassNoise1.tStart = t  # not accounting for scr refresh
            bandpassNoise1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(bandpassNoise1, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(bandpassNoise1.play)  # screen flip
        frameRemains = 1 + .30- win.monitorFramePeriod * 0.75  # most of one frame period left
        if bandpassNoise1.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            bandpassNoise1.tStop = t  # not accounting for scr refresh
            bandpassNoise1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(bandpassNoise1, 'tStopRefresh')  # time at next scr refresh
            if .30 > 0.5:  # don't force-stop brief sounds
                bandpassNoise1.stop()
        # start/stop bandpassNoise2
        if t >= 2.1 and bandpassNoise2.status == NOT_STARTED:
            # keep track of start time/frame for later
            bandpassNoise2.tStart = t  # not accounting for scr refresh
            bandpassNoise2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(bandpassNoise2, 'tStartRefresh')  # time at next scr refresh
            win.callOnFlip(bandpassNoise2.play)  # screen flip
        frameRemains = 2.1 + 0.3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if bandpassNoise2.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            bandpassNoise2.tStop = t  # not accounting for scr refresh
            bandpassNoise2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(bandpassNoise2, 'tStopRefresh')  # time at next scr refresh
            if 0.3 > 0.5:  # don't force-stop brief sounds
                bandpassNoise2.stop()
        
        # *interval1* updates
        if t >= 1 and interval1.status == NOT_STARTED:
            # keep track of start time/frame for later
            interval1.tStart = t  # not accounting for scr refresh
            interval1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(interval1, 'tStartRefresh')  # time at next scr refresh
            interval1.setAutoDraw(True)
        frameRemains = 1 + .3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if interval1.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            interval1.tStop = t  # not accounting for scr refresh
            interval1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(interval1, 'tStopRefresh')  # time at next scr refresh
            interval1.setAutoDraw(False)
        
        # *interval2* updates
        if t >= 2.1 and interval2.status == NOT_STARTED:
            # keep track of start time/frame for later
            interval2.tStart = t  # not accounting for scr refresh
            interval2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(interval2, 'tStartRefresh')  # time at next scr refresh
            interval2.setAutoDraw(True)
        frameRemains = 2.1 + 0.3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if interval2.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            interval2.tStop = t  # not accounting for scr refresh
            interval2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(interval2, 'tStopRefresh')  # time at next scr refresh
            interval2.setAutoDraw(False)
        
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
    probeTone1.stop()  # ensure sound has stopped at end of routine
    trials.addData('probeTone1.started', probeTone1.tStartRefresh)
    trials.addData('probeTone1.stopped', probeTone1.tStopRefresh)
    trials.addData('delay.started', delay.tStartRefresh)
    trials.addData('delay.stopped', delay.tStopRefresh)
    trials.addData('ISI.started', ISI.tStartRefresh)
    trials.addData('ISI.stopped', ISI.tStopRefresh)
    probeTone2.stop()  # ensure sound has stopped at end of routine
    trials.addData('probeTone2.started', probeTone2.tStartRefresh)
    trials.addData('probeTone2.stopped', probeTone2.tStopRefresh)
    bandpassNoise1.stop()  # ensure sound has stopped at end of routine
    trials.addData('bandpassNoise1.started', bandpassNoise1.tStartRefresh)
    trials.addData('bandpassNoise1.stopped', bandpassNoise1.tStopRefresh)
    bandpassNoise2.stop()  # ensure sound has stopped at end of routine
    trials.addData('bandpassNoise2.started', bandpassNoise2.tStartRefresh)
    trials.addData('bandpassNoise2.stopped', bandpassNoise2.tStopRefresh)
    trials.addData('interval1.started', interval1.tStartRefresh)
    trials.addData('interval1.stopped', interval1.tStopRefresh)
    trials.addData('interval2.started', interval2.tStartRefresh)
    trials.addData('interval2.stopped', interval2.tStopRefresh)
    # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Question"-------
    t = 0
    QuestionClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    questionResponse = keyboard.Keyboard()
    # keep track of which components have finished
    QuestionComponents = [questionText, questionResponse]
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
        
        # *questionText* updates
        if t >= 0.0 and questionText.status == NOT_STARTED:
            # keep track of start time/frame for later
            questionText.tStart = t  # not accounting for scr refresh
            questionText.frameNStart = frameN  # exact frame index
            win.timeOnFlip(questionText, 'tStartRefresh')  # time at next scr refresh
            questionText.setAutoDraw(True)
        
        # *questionResponse* updates
        if t >= 0.0 and questionResponse.status == NOT_STARTED:
            # keep track of start time/frame for later
            questionResponse.tStart = t  # not accounting for scr refresh
            questionResponse.frameNStart = frameN  # exact frame index
            win.timeOnFlip(questionResponse, 'tStartRefresh')  # time at next scr refresh
            questionResponse.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(questionResponse.clock.reset)  # t=0 on next screen flip
            questionResponse.clearEvents(eventType='keyboard')
        if questionResponse.status == STARTED:
            theseKeys = questionResponse.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                questionResponse.keys = theseKeys.name  # just the last key pressed
                questionResponse.rt = theseKeys.rt
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
    trials.addData('questionText.started', questionText.tStartRefresh)
    trials.addData('questionText.stopped', questionText.tStopRefresh)
    # check responses
    if questionResponse.keys in ['', [], None]:  # No response was made
        questionResponse.keys = None
    trials.addData('questionResponse.keys',questionResponse.keys)
    if questionResponse.keys != None:  # we had a response
        trials.addData('questionResponse.rt', questionResponse.rt)
    trials.addData('questionResponse.started', questionResponse.tStartRefresh)
    trials.addData('questionResponse.stopped', questionResponse.tStopRefresh)
    # the Routine "Question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback"-------
    t = 0
    FeedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    feedbackText.setColor('white', colorSpace='rgb')
    feedbackText.setText(toneVolume)
    if questionResponse.keys[0] == str(interval):
       #Adjust tone volume
       toneVolume = toneVolume - 0.05 #tone volume goes down 2 dB for every correct response
       print('Tone Volume is now:', toneVolume)
       
       #Adjust feedback color and intensity
       intensity = intensity - 0.05
       feedbackText.setColor([0,intensity,0], colorSpace='rgb') #GREEN
    
    
    elif questionResponse.keys[0] != str(interval):
       #Adjust tone volume
       toneVolume = toneVolume + 0.05 #tone volume goes down by 2dB for every correct response
       print('Tone Volume is now:', toneVolume)
    
       #Adjust feedback color and intensity
       intensity = intensity + 0.05 
       feedbackText.setColor([intensity,0,0], colorSpace='rgb') #RED 
    # keep track of which components have finished
    FeedbackComponents = [feedbackText]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FeedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbackText* updates
        if t >= 0.0 and feedbackText.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedbackText.tStart = t  # not accounting for scr refresh
            feedbackText.frameNStart = frameN  # exact frame index
            win.timeOnFlip(feedbackText, 'tStartRefresh')  # time at next scr refresh
            feedbackText.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedbackText.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            feedbackText.tStop = t  # not accounting for scr refresh
            feedbackText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(feedbackText, 'tStopRefresh')  # time at next scr refresh
            feedbackText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('feedbackText.started', feedbackText.tStartRefresh)
    trials.addData('feedbackText.stopped', feedbackText.tStopRefresh)
    thisExp.nextEntry()
    
# completed 4 repeats of 'trials'


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
