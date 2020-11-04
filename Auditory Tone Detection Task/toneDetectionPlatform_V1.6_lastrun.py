#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on November 02, 2020, at 16:59
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
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
psychopyVersion = '2020.2.4'
expName = 'toneDetectionPlatform_V1.6'  # from the Builder filename that created this script
expInfo = {'participant': '', 'Session': '1', 'Tone Length': ['Short', 'Long'], 'Condition': ['Quiet', 'Simultaneous', 'Backward'], 'calibration': '0.8912509381337447'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
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
    originPath='C:\\Users\\W2032175\\Documents\\GitHub\\Open-source-Auditory-Tone-Detection-Task\\Auditory Tone Detection Task\\toneDetectionPlatform_V1.6_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
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

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
welcomeText = visual.TextStim(win=win, name='welcomeText',
    text='Welcome to the Tone Detection task\n\nPress SPACE to begin',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome_resp = keyboard.Keyboard()
calibration = expInfo['calibration']

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instructionsLightBulb1 = visual.ImageStim(
    win=win,
    name='instructionsLightBulb1', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
instructionsLightBulb2 = visual.ImageStim(
    win=win,
    name='instructionsLightBulb2', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
instructionsText = visual.TextStim(win=win, name='instructionsText',
    text='When you begin  the task, you will be presented with two light bulbs on each side of the screen. \n',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
pressSpace = visual.TextStim(win=win, name='pressSpace',
    text='PRESS SPACE to continue',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "instructions_2"
instructions_2Clock = core.Clock()
instructionsLightBulb1_2 = visual.ImageStim(
    win=win,
    name='instructionsLightBulb1_2', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
instructionsLightBulb2_2 = visual.ImageStim(
    win=win,
    name='instructionsLightBulb2_2', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
instructionsText_2 = visual.TextStim(win=win, name='instructionsText_2',
    text='In each trial, the light bulbs will blink',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
pressSpace_2 = visual.TextStim(win=win, name='pressSpace_2',
    text='PRESS SPACE to continue',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "instructions_3"
instructions_3Clock = core.Clock()
instructionsLightBulb1_3 = visual.ImageStim(
    win=win,
    name='instructionsLightBulb1_3', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
instructionsLightBulb2_3 = visual.ImageStim(
    win=win,
    name='instructionsLightBulb2_3', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text="The left light bulb or 'light bulb 1' will always blink first",
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
pressSpace_3 = visual.TextStim(win=win, name='pressSpace_3',
    text='Press SPACE to see light bulb 1 blink',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "instructions_4"
instructions_4Clock = core.Clock()
instructionsLightBulb1_4 = visual.ImageStim(
    win=win,
    name='instructionsLightBulb1_4', 
    image='lightBulb_ON.png', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
instructionsLightBulb2_4 = visual.ImageStim(
    win=win,
    name='instructionsLightBulb2_4', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "instructions_5"
instructions_5Clock = core.Clock()
instructionsLightBulb1_5 = visual.ImageStim(
    win=win,
    name='instructionsLightBulb1_5', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
instructionsLightBulb2_5 = visual.ImageStim(
    win=win,
    name='instructionsLightBulb2_5', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
instructionsLightBulb2_6 = visual.ImageStim(
    win=win,
    name='instructionsLightBulb2_6', 
    image='lightBulb_ON.png', mask=None,
    ori=0, pos=(0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text="After a brief pause, the second light bulb 'light bulb 2' will also blink",
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
pressSpace_4 = visual.TextStim(win=win, name='pressSpace_4',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "instructions_6"
instructions_6Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='In each trial, ONE of the light bulbs will also make a noise\n',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='press SPACEBAR to hear this sound',
    font='Arial',
    pos=(0, -0.3), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "instructions_7"
instructions_7Clock = core.Clock()
lightBulbOFF = visual.ImageStim(
    win=win,
    name='lightBulbOFF', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
lightBulbON = visual.ImageStim(
    win=win,
    name='lightBulbON', 
    image='lightBulb_ON.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sound_1 = sound.Sound('1000', secs=1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)

# Initialize components for Routine "instructions_8"
instructions_8Clock = core.Clock()
instructions_8_firstLine = visual.TextStim(win=win, name='instructions_8_firstLine',
    text='Remember, although BOTH light bulbs will blink, only ONE light bulb will make a noise! \n\n',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='It is your job to decide which light bulb made the noise by responding your the number pad.\n',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text="\nIF you think that 'light bulb 1' made the noise, press '1'\nOR IF you think 'light bulb 2' made the noise, press '2'\n\n",
    font='Arial',
    pos=(0, -0.02), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instructions_8_pressP = visual.TextStim(win=win, name='instructions_8_pressP',
    text="press 'p' to begin the practice trials!",
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "practice_ITI"
practice_ITIClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "practice_firstChoiceSpace"
practice_firstChoiceSpaceClock = core.Clock()
firstVisualStimulus_2 = visual.TextStim(win=win, name='firstVisualStimulus_2',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
firstChoiceProbeTone_2 = sound.Sound('1000', secs=-1, stereo=True, hamming=True,
    name='firstChoiceProbeTone_2')
firstChoiceProbeTone_2.setVolume(1.0)
firstChoiceLeftStimulus_2 = visual.ImageStim(
    win=win,
    name='firstChoiceLeftStimulus_2', 
    image='lightBulb_ON.png', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
firstChoiceRightStimulus_2 = visual.ImageStim(
    win=win,
    name='firstChoiceRightStimulus_2', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "practice_ISI"
practice_ISIClock = core.Clock()
ISIVisualStimulus_3 = visual.TextStim(win=win, name='ISIVisualStimulus_3',
    text='ISI',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rightStimulus_3 = visual.ImageStim(
    win=win,
    name='rightStimulus_3', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
leftStimulus_3 = visual.ImageStim(
    win=win,
    name='leftStimulus_3', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "practice_secondChoiceSpace_2"
practice_secondChoiceSpace_2Clock = core.Clock()
secondVisualStimulus_2 = visual.TextStim(win=win, name='secondVisualStimulus_2',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
secondChoiceTone_2 = sound.Sound('1000', secs=-1, stereo=True, hamming=True,
    name='secondChoiceTone_2')
secondChoiceTone_2.setVolume(1.0)
secondChoiceLeftStimulus_2 = visual.ImageStim(
    win=win,
    name='secondChoiceLeftStimulus_2', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
secondChoiceRightStimulus_2 = visual.ImageStim(
    win=win,
    name='secondChoiceRightStimulus_2', 
    image='lightBulb_ON.png', mask=None,
    ori=0, pos=(0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "practice_decisionSpace"
practice_decisionSpaceClock = core.Clock()
decisionTextProbe_2 = visual.TextStim(win=win, name='decisionTextProbe_2',
    text='In which interval did you hear the tone?\n1 OR 2?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
decisionKey_2 = keyboard.Keyboard()

# Initialize components for Routine "practice_feedbackSpace"
practice_feedbackSpaceClock = core.Clock()
feedback = "defaultFeedback"
feedbackText_2 = visual.TextStim(win=win, name='feedbackText_2',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "practiceComplete"
practiceCompleteClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text="You have now completed the practice trials!\n\nIf you understand the task, press 'c' to continue. \n\nIf you do not understand the task, please ask for some help!\n",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "beginTest"
beginTestClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text="Upon pressing 'b', you will begin the testing session. \n\nRemember, in the testing session trials, the sound the light bulb makes will be shorter than the sounds made in the practice trials. \n\nThe trials will also be a little faster, so stay alert!\n\nPress 'b' to begin",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "setUp"
setUpClock = core.Clock()
#Preset Tone Durations 
if expInfo['Tone Length'] == 'Long':
    presetToneDuration = 0.2 #200ms
if expInfo['Tone Length'] == 'Short':
        presetToneDuration = 0.02 #20ms




    
    
    
    
    
if expInfo['Condition'] == 'Simultaneous': #if Condition is 'Simultaneous', make onset 200ms into the trial 
    toneOnset = 0.22 #.22 rather than .20 to account account for the 20ms gap that exists before the noise (starting at 20ms into the trial) at the start of the trial
elif expInfo['Condition'] == 'Backward':  #else if Condition is 'Backward' : make Onset start at 0 (20ms before noise) 
    toneOnset = 0 
else: #else, just start the tone in sync with the start of the noise (as per the 'Quiet' Condition)
    toneOnset = 0.02 
    
firstITI = visual.TextStim(win=win, name='firstITI',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trialNumber = 0



# Initialize components for Routine "firstChoiceSpace"
firstChoiceSpaceClock = core.Clock()
firstVisualStimulus = visual.TextStim(win=win, name='firstVisualStimulus',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
firstChoiceNoise = sound.Sound('Noise_BP_600_1400.wav', secs=0.32, stereo=True, hamming=True,
    name='firstChoiceNoise')
firstChoiceNoise.setVolume(1.0)
firstChoiceProbeTone = sound.Sound('1000', secs=-1, stereo=True, hamming=True,
    name='firstChoiceProbeTone')
firstChoiceProbeTone.setVolume(1.0)
firstChoiceLeftStimulus = visual.ImageStim(
    win=win,
    name='firstChoiceLeftStimulus', 
    image='lightBulb_ON.png', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
firstChoiceRightStimulus = visual.ImageStim(
    win=win,
    name='firstChoiceRightStimulus', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISIVisualStimulus = visual.TextStim(win=win, name='ISIVisualStimulus',
    text='ISI',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rightStimulus = visual.ImageStim(
    win=win,
    name='rightStimulus', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
leftStimulus = visual.ImageStim(
    win=win,
    name='leftStimulus', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "secondChoiceSpace"
secondChoiceSpaceClock = core.Clock()
secondVisualStimulus = visual.TextStim(win=win, name='secondVisualStimulus',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
secondChoiceNoise = sound.Sound('Noise_BP_600_1400.wav', secs=0.32, stereo=True, hamming=True,
    name='secondChoiceNoise')
secondChoiceNoise.setVolume(1.0)
secondChoiceTone = sound.Sound('1000', secs=-1, stereo=True, hamming=True,
    name='secondChoiceTone')
secondChoiceTone.setVolume(1.0)
secondChoiceLeftStimulus = visual.ImageStim(
    win=win,
    name='secondChoiceLeftStimulus', 
    image='lightBulb_OFF.png', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
secondChoiceRightStimulus = visual.ImageStim(
    win=win,
    name='secondChoiceRightStimulus', 
    image='lightBulb_ON.png', mask=None,
    ori=0, pos=(0.5, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "decisionSpace"
decisionSpaceClock = core.Clock()
decisionTextProbe = visual.TextStim(win=win, name='decisionTextProbe',
    text='In which interval did you hear the tone?\n1 OR 2?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
decisionKey = keyboard.Keyboard()

# Initialize components for Routine "feedbackSpace"
feedbackSpaceClock = core.Clock()
feedback = "defaultFeedback"
feedbackText = visual.TextStim(win=win, name='feedbackText',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
welcome_resp.keys = []
welcome_resp.rt = []
_welcome_resp_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcomeText, welcome_resp]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeText* updates
    if welcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeText.frameNStart = frameN  # exact frame index
        welcomeText.tStart = t  # local t and not account for scr refresh
        welcomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeText, 'tStartRefresh')  # time at next scr refresh
        welcomeText.setAutoDraw(True)
    
    # *welcome_resp* updates
    waitOnFlip = False
    if welcome_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcome_resp.frameNStart = frameN  # exact frame index
        welcome_resp.tStart = t  # local t and not account for scr refresh
        welcome_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome_resp, 'tStartRefresh')  # time at next scr refresh
        welcome_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcome_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcome_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcome_resp.status == STARTED and not waitOnFlip:
        theseKeys = welcome_resp.getKeys(keyList=['space'], waitRelease=False)
        _welcome_resp_allKeys.extend(theseKeys)
        if len(_welcome_resp_allKeys):
            welcome_resp.keys = _welcome_resp_allKeys[-1].name  # just the last key pressed
            welcome_resp.rt = _welcome_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('welcomeText.started', welcomeText.tStartRefresh)
thisExp.addData('welcomeText.stopped', welcomeText.tStopRefresh)
# check responses
if welcome_resp.keys in ['', [], None]:  # No response was made
    welcome_resp.keys = None
thisExp.addData('welcome_resp.keys',welcome_resp.keys)
if welcome_resp.keys != None:  # we had a response
    thisExp.addData('welcome_resp.rt', welcome_resp.rt)
thisExp.addData('welcome_resp.started', welcome_resp.tStartRefresh)
thisExp.addData('welcome_resp.stopped', welcome_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
instructions_loop = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='instructions_loop')
thisExp.addLoop(instructions_loop)  # add the loop to the experiment
thisInstructions_loop = instructions_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstructions_loop.rgb)
if thisInstructions_loop != None:
    for paramName in thisInstructions_loop:
        exec('{} = thisInstructions_loop[paramName]'.format(paramName))

for thisInstructions_loop in instructions_loop:
    currentLoop = instructions_loop
    # abbreviate parameter names if possible (e.g. rgb = thisInstructions_loop.rgb)
    if thisInstructions_loop != None:
        for paramName in thisInstructions_loop:
            exec('{} = thisInstructions_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    instructionsComponents = [instructionsLightBulb1, instructionsLightBulb2, instructionsText, pressSpace, key_resp]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsLightBulb1* updates
        if instructionsLightBulb1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsLightBulb1.frameNStart = frameN  # exact frame index
            instructionsLightBulb1.tStart = t  # local t and not account for scr refresh
            instructionsLightBulb1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsLightBulb1, 'tStartRefresh')  # time at next scr refresh
            instructionsLightBulb1.setAutoDraw(True)
        
        # *instructionsLightBulb2* updates
        if instructionsLightBulb2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsLightBulb2.frameNStart = frameN  # exact frame index
            instructionsLightBulb2.tStart = t  # local t and not account for scr refresh
            instructionsLightBulb2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsLightBulb2, 'tStartRefresh')  # time at next scr refresh
            instructionsLightBulb2.setAutoDraw(True)
        
        # *instructionsText* updates
        if instructionsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsText.frameNStart = frameN  # exact frame index
            instructionsText.tStart = t  # local t and not account for scr refresh
            instructionsText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsText, 'tStartRefresh')  # time at next scr refresh
            instructionsText.setAutoDraw(True)
        
        # *pressSpace* updates
        if pressSpace.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace.frameNStart = frameN  # exact frame index
            pressSpace.tStart = t  # local t and not account for scr refresh
            pressSpace.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace, 'tStartRefresh')  # time at next scr refresh
            pressSpace.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_loop.addData('instructionsLightBulb1.started', instructionsLightBulb1.tStartRefresh)
    instructions_loop.addData('instructionsLightBulb1.stopped', instructionsLightBulb1.tStopRefresh)
    instructions_loop.addData('instructionsLightBulb2.started', instructionsLightBulb2.tStartRefresh)
    instructions_loop.addData('instructionsLightBulb2.stopped', instructionsLightBulb2.tStopRefresh)
    instructions_loop.addData('instructionsText.started', instructionsText.tStartRefresh)
    instructions_loop.addData('instructionsText.stopped', instructionsText.tStopRefresh)
    instructions_loop.addData('pressSpace.started', pressSpace.tStartRefresh)
    instructions_loop.addData('pressSpace.stopped', pressSpace.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    instructions_loop.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        instructions_loop.addData('key_resp.rt', key_resp.rt)
    instructions_loop.addData('key_resp.started', key_resp.tStartRefresh)
    instructions_loop.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instructions_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    instructions_2Components = [instructionsLightBulb1_2, instructionsLightBulb2_2, instructionsText_2, pressSpace_2, key_resp_2]
    for thisComponent in instructions_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions_2"-------
    while continueRoutine:
        # get current time
        t = instructions_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsLightBulb1_2* updates
        if instructionsLightBulb1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsLightBulb1_2.frameNStart = frameN  # exact frame index
            instructionsLightBulb1_2.tStart = t  # local t and not account for scr refresh
            instructionsLightBulb1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsLightBulb1_2, 'tStartRefresh')  # time at next scr refresh
            instructionsLightBulb1_2.setAutoDraw(True)
        
        # *instructionsLightBulb2_2* updates
        if instructionsLightBulb2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsLightBulb2_2.frameNStart = frameN  # exact frame index
            instructionsLightBulb2_2.tStart = t  # local t and not account for scr refresh
            instructionsLightBulb2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsLightBulb2_2, 'tStartRefresh')  # time at next scr refresh
            instructionsLightBulb2_2.setAutoDraw(True)
        
        # *instructionsText_2* updates
        if instructionsText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsText_2.frameNStart = frameN  # exact frame index
            instructionsText_2.tStart = t  # local t and not account for scr refresh
            instructionsText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsText_2, 'tStartRefresh')  # time at next scr refresh
            instructionsText_2.setAutoDraw(True)
        
        # *pressSpace_2* updates
        if pressSpace_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_2.frameNStart = frameN  # exact frame index
            pressSpace_2.tStart = t  # local t and not account for scr refresh
            pressSpace_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_2, 'tStartRefresh')  # time at next scr refresh
            pressSpace_2.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_2"-------
    for thisComponent in instructions_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_loop.addData('instructionsLightBulb1_2.started', instructionsLightBulb1_2.tStartRefresh)
    instructions_loop.addData('instructionsLightBulb1_2.stopped', instructionsLightBulb1_2.tStopRefresh)
    instructions_loop.addData('instructionsLightBulb2_2.started', instructionsLightBulb2_2.tStartRefresh)
    instructions_loop.addData('instructionsLightBulb2_2.stopped', instructionsLightBulb2_2.tStopRefresh)
    instructions_loop.addData('instructionsText_2.started', instructionsText_2.tStartRefresh)
    instructions_loop.addData('instructionsText_2.stopped', instructionsText_2.tStopRefresh)
    instructions_loop.addData('pressSpace_2.started', pressSpace_2.tStartRefresh)
    instructions_loop.addData('pressSpace_2.stopped', pressSpace_2.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    instructions_loop.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        instructions_loop.addData('key_resp_2.rt', key_resp_2.rt)
    instructions_loop.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    instructions_loop.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "instructions_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instructions_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    instructions_3Components = [instructionsLightBulb1_3, instructionsLightBulb2_3, text_3, pressSpace_3, key_resp_3]
    for thisComponent in instructions_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions_3"-------
    while continueRoutine:
        # get current time
        t = instructions_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsLightBulb1_3* updates
        if instructionsLightBulb1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsLightBulb1_3.frameNStart = frameN  # exact frame index
            instructionsLightBulb1_3.tStart = t  # local t and not account for scr refresh
            instructionsLightBulb1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsLightBulb1_3, 'tStartRefresh')  # time at next scr refresh
            instructionsLightBulb1_3.setAutoDraw(True)
        
        # *instructionsLightBulb2_3* updates
        if instructionsLightBulb2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsLightBulb2_3.frameNStart = frameN  # exact frame index
            instructionsLightBulb2_3.tStart = t  # local t and not account for scr refresh
            instructionsLightBulb2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsLightBulb2_3, 'tStartRefresh')  # time at next scr refresh
            instructionsLightBulb2_3.setAutoDraw(True)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *pressSpace_3* updates
        if pressSpace_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_3.frameNStart = frameN  # exact frame index
            pressSpace_3.tStart = t  # local t and not account for scr refresh
            pressSpace_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_3, 'tStartRefresh')  # time at next scr refresh
            pressSpace_3.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_3"-------
    for thisComponent in instructions_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_loop.addData('instructionsLightBulb1_3.started', instructionsLightBulb1_3.tStartRefresh)
    instructions_loop.addData('instructionsLightBulb1_3.stopped', instructionsLightBulb1_3.tStopRefresh)
    instructions_loop.addData('instructionsLightBulb2_3.started', instructionsLightBulb2_3.tStartRefresh)
    instructions_loop.addData('instructionsLightBulb2_3.stopped', instructionsLightBulb2_3.tStopRefresh)
    instructions_loop.addData('text_3.started', text_3.tStartRefresh)
    instructions_loop.addData('text_3.stopped', text_3.tStopRefresh)
    instructions_loop.addData('pressSpace_3.started', pressSpace_3.tStartRefresh)
    instructions_loop.addData('pressSpace_3.stopped', pressSpace_3.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    instructions_loop.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        instructions_loop.addData('key_resp_3.rt', key_resp_3.rt)
    instructions_loop.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    instructions_loop.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "instructions_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instructions_4"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    instructions_4Components = [instructionsLightBulb1_4, instructionsLightBulb2_4]
    for thisComponent in instructions_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions_4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = instructions_4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsLightBulb1_4* updates
        if instructionsLightBulb1_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsLightBulb1_4.frameNStart = frameN  # exact frame index
            instructionsLightBulb1_4.tStart = t  # local t and not account for scr refresh
            instructionsLightBulb1_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsLightBulb1_4, 'tStartRefresh')  # time at next scr refresh
            instructionsLightBulb1_4.setAutoDraw(True)
        if instructionsLightBulb1_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instructionsLightBulb1_4.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                instructionsLightBulb1_4.tStop = t  # not accounting for scr refresh
                instructionsLightBulb1_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instructionsLightBulb1_4, 'tStopRefresh')  # time at next scr refresh
                instructionsLightBulb1_4.setAutoDraw(False)
        
        # *instructionsLightBulb2_4* updates
        if instructionsLightBulb2_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsLightBulb2_4.frameNStart = frameN  # exact frame index
            instructionsLightBulb2_4.tStart = t  # local t and not account for scr refresh
            instructionsLightBulb2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsLightBulb2_4, 'tStartRefresh')  # time at next scr refresh
            instructionsLightBulb2_4.setAutoDraw(True)
        if instructionsLightBulb2_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instructionsLightBulb2_4.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                instructionsLightBulb2_4.tStop = t  # not accounting for scr refresh
                instructionsLightBulb2_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instructionsLightBulb2_4, 'tStopRefresh')  # time at next scr refresh
                instructionsLightBulb2_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_4"-------
    for thisComponent in instructions_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_loop.addData('instructionsLightBulb1_4.started', instructionsLightBulb1_4.tStartRefresh)
    instructions_loop.addData('instructionsLightBulb1_4.stopped', instructionsLightBulb1_4.tStopRefresh)
    instructions_loop.addData('instructionsLightBulb2_4.started', instructionsLightBulb2_4.tStartRefresh)
    instructions_loop.addData('instructionsLightBulb2_4.stopped', instructionsLightBulb2_4.tStopRefresh)
    
    # ------Prepare to start Routine "instructions_5"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    instructions_5Components = [instructionsLightBulb1_5, instructionsLightBulb2_5, instructionsLightBulb2_6, text_4, pressSpace_4, key_resp_4]
    for thisComponent in instructions_5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions_5"-------
    while continueRoutine:
        # get current time
        t = instructions_5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsLightBulb1_5* updates
        if instructionsLightBulb1_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsLightBulb1_5.frameNStart = frameN  # exact frame index
            instructionsLightBulb1_5.tStart = t  # local t and not account for scr refresh
            instructionsLightBulb1_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsLightBulb1_5, 'tStartRefresh')  # time at next scr refresh
            instructionsLightBulb1_5.setAutoDraw(True)
        
        # *instructionsLightBulb2_5* updates
        if instructionsLightBulb2_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsLightBulb2_5.frameNStart = frameN  # exact frame index
            instructionsLightBulb2_5.tStart = t  # local t and not account for scr refresh
            instructionsLightBulb2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsLightBulb2_5, 'tStartRefresh')  # time at next scr refresh
            instructionsLightBulb2_5.setAutoDraw(True)
        if instructionsLightBulb2_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instructionsLightBulb2_5.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                instructionsLightBulb2_5.tStop = t  # not accounting for scr refresh
                instructionsLightBulb2_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instructionsLightBulb2_5, 'tStopRefresh')  # time at next scr refresh
                instructionsLightBulb2_5.setAutoDraw(False)
        
        # *instructionsLightBulb2_6* updates
        if instructionsLightBulb2_6.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            instructionsLightBulb2_6.frameNStart = frameN  # exact frame index
            instructionsLightBulb2_6.tStart = t  # local t and not account for scr refresh
            instructionsLightBulb2_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsLightBulb2_6, 'tStartRefresh')  # time at next scr refresh
            instructionsLightBulb2_6.setAutoDraw(True)
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        
        # *pressSpace_4* updates
        if pressSpace_4.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            pressSpace_4.frameNStart = frameN  # exact frame index
            pressSpace_4.tStart = t  # local t and not account for scr refresh
            pressSpace_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pressSpace_4, 'tStartRefresh')  # time at next scr refresh
            pressSpace_4.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_5"-------
    for thisComponent in instructions_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_loop.addData('instructionsLightBulb1_5.started', instructionsLightBulb1_5.tStartRefresh)
    instructions_loop.addData('instructionsLightBulb1_5.stopped', instructionsLightBulb1_5.tStopRefresh)
    instructions_loop.addData('instructionsLightBulb2_5.started', instructionsLightBulb2_5.tStartRefresh)
    instructions_loop.addData('instructionsLightBulb2_5.stopped', instructionsLightBulb2_5.tStopRefresh)
    instructions_loop.addData('instructionsLightBulb2_6.started', instructionsLightBulb2_6.tStartRefresh)
    instructions_loop.addData('instructionsLightBulb2_6.stopped', instructionsLightBulb2_6.tStopRefresh)
    instructions_loop.addData('text_4.started', text_4.tStartRefresh)
    instructions_loop.addData('text_4.stopped', text_4.tStopRefresh)
    instructions_loop.addData('pressSpace_4.started', pressSpace_4.tStartRefresh)
    instructions_loop.addData('pressSpace_4.stopped', pressSpace_4.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    instructions_loop.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        instructions_loop.addData('key_resp_4.rt', key_resp_4.rt)
    instructions_loop.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    instructions_loop.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "instructions_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instructions_6"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    instructions_6Components = [text_2, text_5, key_resp_5]
    for thisComponent in instructions_6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions_6"-------
    while continueRoutine:
        # get current time
        t = instructions_6Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_6Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_6"-------
    for thisComponent in instructions_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_loop.addData('text_2.started', text_2.tStartRefresh)
    instructions_loop.addData('text_2.stopped', text_2.tStopRefresh)
    instructions_loop.addData('text_5.started', text_5.tStartRefresh)
    instructions_loop.addData('text_5.stopped', text_5.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    instructions_loop.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        instructions_loop.addData('key_resp_5.rt', key_resp_5.rt)
    instructions_loop.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    instructions_loop.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "instructions_6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instructions_7"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    #set desired dB of the practice trials to 40
    desired_db = 50
    
    #convert variable types to integer
    calibration = float(calibration)
    desired_db = int(desired_db)
    
    
    psychopy_input_value = ((calibration)/(10**(117/20))*(10**(desired_db/20)))
    
    sound_1.setSound('1000', secs=1, hamming=True)
    sound_1.setVolume(psychopy_input_value, log=False)
    # keep track of which components have finished
    instructions_7Components = [lightBulbOFF, lightBulbON, sound_1]
    for thisComponent in instructions_7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions_7"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = instructions_7Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_7Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lightBulbOFF* updates
        if lightBulbOFF.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lightBulbOFF.frameNStart = frameN  # exact frame index
            lightBulbOFF.tStart = t  # local t and not account for scr refresh
            lightBulbOFF.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lightBulbOFF, 'tStartRefresh')  # time at next scr refresh
            lightBulbOFF.setAutoDraw(True)
        if lightBulbOFF.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lightBulbOFF.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                lightBulbOFF.tStop = t  # not accounting for scr refresh
                lightBulbOFF.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lightBulbOFF, 'tStopRefresh')  # time at next scr refresh
                lightBulbOFF.setAutoDraw(False)
        
        # *lightBulbON* updates
        if lightBulbON.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            lightBulbON.frameNStart = frameN  # exact frame index
            lightBulbON.tStart = t  # local t and not account for scr refresh
            lightBulbON.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lightBulbON, 'tStartRefresh')  # time at next scr refresh
            lightBulbON.setAutoDraw(True)
        if lightBulbON.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lightBulbON.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                lightBulbON.tStop = t  # not accounting for scr refresh
                lightBulbON.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lightBulbON, 'tStopRefresh')  # time at next scr refresh
                lightBulbON.setAutoDraw(False)
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_7"-------
    for thisComponent in instructions_7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_loop.addData('lightBulbOFF.started', lightBulbOFF.tStartRefresh)
    instructions_loop.addData('lightBulbOFF.stopped', lightBulbOFF.tStopRefresh)
    instructions_loop.addData('lightBulbON.started', lightBulbON.tStartRefresh)
    instructions_loop.addData('lightBulbON.stopped', lightBulbON.tStopRefresh)
    sound_1.stop()  # ensure sound has stopped at end of routine
    instructions_loop.addData('sound_1.started', sound_1.tStartRefresh)
    instructions_loop.addData('sound_1.stopped', sound_1.tStopRefresh)
    
    # ------Prepare to start Routine "instructions_8"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    instructions_8Components = [instructions_8_firstLine, text_8, text_9, instructions_8_pressP, key_resp_6]
    for thisComponent in instructions_8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions_8"-------
    while continueRoutine:
        # get current time
        t = instructions_8Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_8Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_8_firstLine* updates
        if instructions_8_firstLine.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_8_firstLine.frameNStart = frameN  # exact frame index
            instructions_8_firstLine.tStart = t  # local t and not account for scr refresh
            instructions_8_firstLine.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_8_firstLine, 'tStartRefresh')  # time at next scr refresh
            instructions_8_firstLine.setAutoDraw(True)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        
        # *instructions_8_pressP* updates
        if instructions_8_pressP.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            instructions_8_pressP.frameNStart = frameN  # exact frame index
            instructions_8_pressP.tStart = t  # local t and not account for scr refresh
            instructions_8_pressP.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_8_pressP, 'tStartRefresh')  # time at next scr refresh
            instructions_8_pressP.setAutoDraw(True)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['p'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_8"-------
    for thisComponent in instructions_8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_loop.addData('instructions_8_firstLine.started', instructions_8_firstLine.tStartRefresh)
    instructions_loop.addData('instructions_8_firstLine.stopped', instructions_8_firstLine.tStopRefresh)
    instructions_loop.addData('text_8.started', text_8.tStartRefresh)
    instructions_loop.addData('text_8.stopped', text_8.tStopRefresh)
    instructions_loop.addData('text_9.started', text_9.tStartRefresh)
    instructions_loop.addData('text_9.stopped', text_9.tStopRefresh)
    instructions_loop.addData('instructions_8_pressP.started', instructions_8_pressP.tStartRefresh)
    instructions_loop.addData('instructions_8_pressP.stopped', instructions_8_pressP.tStopRefresh)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    instructions_loop.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        instructions_loop.addData('key_resp_6.rt', key_resp_6.rt)
    instructions_loop.addData('key_resp_6.started', key_resp_6.tStartRefresh)
    instructions_loop.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
    # the Routine "instructions_8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'instructions_loop'


# set up handler to look after randomisation of conditions etc
practiceTrials = data.TrialHandler(nReps=0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practiceTrials')
thisExp.addLoop(practiceTrials)  # add the loop to the experiment
thisPracticeTrial = practiceTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
if thisPracticeTrial != None:
    for paramName in thisPracticeTrial:
        exec('{} = thisPracticeTrial[paramName]'.format(paramName))

for thisPracticeTrial in practiceTrials:
    currentLoop = practiceTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            exec('{} = thisPracticeTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_ITI"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    #set desired dB of the practice trials to 40
    desired_db = 50
    
    #convert variable types to integer
    calibration = float(calibration)
    desired_db = int(desired_db)
    
    psychopy_input_value = ((calibration)/(10**(117/20))*(10**(desired_db/20)))
    
    
    print('psychopy_input_value for practice:', psychopy_input_value)
    
    # keep track of which components have finished
    practice_ITIComponents = [text_6]
    for thisComponent in practice_ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice_ITI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_ITI"-------
    for thisComponent in practice_ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceTrials.addData('text_6.started', text_6.tStartRefresh)
    practiceTrials.addData('text_6.stopped', text_6.tStopRefresh)
    
    # ------Prepare to start Routine "practice_firstChoiceSpace"-------
    continueRoutine = True
    # update component parameters for each repeat
    if condition == 1:
        toneDuration = 0.2
    
    elif condition == 2:
        toneDuration = 0
    firstChoiceProbeTone_2.setSound('1000', secs=toneDuration, hamming=True)
    firstChoiceProbeTone_2.setVolume(psychopy_input_value, log=False)
    # keep track of which components have finished
    practice_firstChoiceSpaceComponents = [firstVisualStimulus_2, firstChoiceProbeTone_2, firstChoiceLeftStimulus_2, firstChoiceRightStimulus_2]
    for thisComponent in practice_firstChoiceSpaceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_firstChoiceSpaceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice_firstChoiceSpace"-------
    while continueRoutine:
        # get current time
        t = practice_firstChoiceSpaceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_firstChoiceSpaceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *firstVisualStimulus_2* updates
        if firstVisualStimulus_2.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
            # keep track of start time/frame for later
            firstVisualStimulus_2.frameNStart = frameN  # exact frame index
            firstVisualStimulus_2.tStart = t  # local t and not account for scr refresh
            firstVisualStimulus_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firstVisualStimulus_2, 'tStartRefresh')  # time at next scr refresh
            firstVisualStimulus_2.setAutoDraw(True)
        if firstVisualStimulus_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > firstVisualStimulus_2.tStartRefresh + 0.32-frameTolerance:
                # keep track of stop time/frame for later
                firstVisualStimulus_2.tStop = t  # not accounting for scr refresh
                firstVisualStimulus_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(firstVisualStimulus_2, 'tStopRefresh')  # time at next scr refresh
                firstVisualStimulus_2.setAutoDraw(False)
        # start/stop firstChoiceProbeTone_2
        if firstChoiceProbeTone_2.status == NOT_STARTED and tThisFlip >= toneOnset-frameTolerance:
            # keep track of start time/frame for later
            firstChoiceProbeTone_2.frameNStart = frameN  # exact frame index
            firstChoiceProbeTone_2.tStart = t  # local t and not account for scr refresh
            firstChoiceProbeTone_2.tStartRefresh = tThisFlipGlobal  # on global time
            firstChoiceProbeTone_2.play(when=win)  # sync with win flip
        if firstChoiceProbeTone_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > firstChoiceProbeTone_2.tStartRefresh + toneDuration-frameTolerance:
                # keep track of stop time/frame for later
                firstChoiceProbeTone_2.tStop = t  # not accounting for scr refresh
                firstChoiceProbeTone_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(firstChoiceProbeTone_2, 'tStopRefresh')  # time at next scr refresh
                firstChoiceProbeTone_2.stop()
        
        # *firstChoiceLeftStimulus_2* updates
        if firstChoiceLeftStimulus_2.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
            # keep track of start time/frame for later
            firstChoiceLeftStimulus_2.frameNStart = frameN  # exact frame index
            firstChoiceLeftStimulus_2.tStart = t  # local t and not account for scr refresh
            firstChoiceLeftStimulus_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firstChoiceLeftStimulus_2, 'tStartRefresh')  # time at next scr refresh
            firstChoiceLeftStimulus_2.setAutoDraw(True)
        if firstChoiceLeftStimulus_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > firstChoiceLeftStimulus_2.tStartRefresh + 0.32-frameTolerance:
                # keep track of stop time/frame for later
                firstChoiceLeftStimulus_2.tStop = t  # not accounting for scr refresh
                firstChoiceLeftStimulus_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(firstChoiceLeftStimulus_2, 'tStopRefresh')  # time at next scr refresh
                firstChoiceLeftStimulus_2.setAutoDraw(False)
        
        # *firstChoiceRightStimulus_2* updates
        if firstChoiceRightStimulus_2.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
            # keep track of start time/frame for later
            firstChoiceRightStimulus_2.frameNStart = frameN  # exact frame index
            firstChoiceRightStimulus_2.tStart = t  # local t and not account for scr refresh
            firstChoiceRightStimulus_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firstChoiceRightStimulus_2, 'tStartRefresh')  # time at next scr refresh
            firstChoiceRightStimulus_2.setAutoDraw(True)
        if firstChoiceRightStimulus_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > firstChoiceRightStimulus_2.tStartRefresh + 0.32-frameTolerance:
                # keep track of stop time/frame for later
                firstChoiceRightStimulus_2.tStop = t  # not accounting for scr refresh
                firstChoiceRightStimulus_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(firstChoiceRightStimulus_2, 'tStopRefresh')  # time at next scr refresh
                firstChoiceRightStimulus_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_firstChoiceSpaceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_firstChoiceSpace"-------
    for thisComponent in practice_firstChoiceSpaceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceTrials.addData('firstVisualStimulus_2.started', firstVisualStimulus_2.tStartRefresh)
    practiceTrials.addData('firstVisualStimulus_2.stopped', firstVisualStimulus_2.tStopRefresh)
    firstChoiceProbeTone_2.stop()  # ensure sound has stopped at end of routine
    practiceTrials.addData('firstChoiceProbeTone_2.started', firstChoiceProbeTone_2.tStartRefresh)
    practiceTrials.addData('firstChoiceProbeTone_2.stopped', firstChoiceProbeTone_2.tStopRefresh)
    practiceTrials.addData('firstChoiceLeftStimulus_2.started', firstChoiceLeftStimulus_2.tStartRefresh)
    practiceTrials.addData('firstChoiceLeftStimulus_2.stopped', firstChoiceLeftStimulus_2.tStopRefresh)
    practiceTrials.addData('firstChoiceRightStimulus_2.started', firstChoiceRightStimulus_2.tStartRefresh)
    practiceTrials.addData('firstChoiceRightStimulus_2.stopped', firstChoiceRightStimulus_2.tStopRefresh)
    # the Routine "practice_firstChoiceSpace" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practice_ISI"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    practice_ISIComponents = [ISIVisualStimulus_3, rightStimulus_3, leftStimulus_3]
    for thisComponent in practice_ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice_ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISIVisualStimulus_3* updates
        if ISIVisualStimulus_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISIVisualStimulus_3.frameNStart = frameN  # exact frame index
            ISIVisualStimulus_3.tStart = t  # local t and not account for scr refresh
            ISIVisualStimulus_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISIVisualStimulus_3, 'tStartRefresh')  # time at next scr refresh
            ISIVisualStimulus_3.setAutoDraw(True)
        if ISIVisualStimulus_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISIVisualStimulus_3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                ISIVisualStimulus_3.tStop = t  # not accounting for scr refresh
                ISIVisualStimulus_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ISIVisualStimulus_3, 'tStopRefresh')  # time at next scr refresh
                ISIVisualStimulus_3.setAutoDraw(False)
        
        # *rightStimulus_3* updates
        if rightStimulus_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightStimulus_3.frameNStart = frameN  # exact frame index
            rightStimulus_3.tStart = t  # local t and not account for scr refresh
            rightStimulus_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightStimulus_3, 'tStartRefresh')  # time at next scr refresh
            rightStimulus_3.setAutoDraw(True)
        if rightStimulus_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rightStimulus_3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                rightStimulus_3.tStop = t  # not accounting for scr refresh
                rightStimulus_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rightStimulus_3, 'tStopRefresh')  # time at next scr refresh
                rightStimulus_3.setAutoDraw(False)
        
        # *leftStimulus_3* updates
        if leftStimulus_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            leftStimulus_3.frameNStart = frameN  # exact frame index
            leftStimulus_3.tStart = t  # local t and not account for scr refresh
            leftStimulus_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftStimulus_3, 'tStartRefresh')  # time at next scr refresh
            leftStimulus_3.setAutoDraw(True)
        if leftStimulus_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > leftStimulus_3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                leftStimulus_3.tStop = t  # not accounting for scr refresh
                leftStimulus_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(leftStimulus_3, 'tStopRefresh')  # time at next scr refresh
                leftStimulus_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_ISI"-------
    for thisComponent in practice_ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceTrials.addData('ISIVisualStimulus_3.started', ISIVisualStimulus_3.tStartRefresh)
    practiceTrials.addData('ISIVisualStimulus_3.stopped', ISIVisualStimulus_3.tStopRefresh)
    practiceTrials.addData('rightStimulus_3.started', rightStimulus_3.tStartRefresh)
    practiceTrials.addData('rightStimulus_3.stopped', rightStimulus_3.tStopRefresh)
    practiceTrials.addData('leftStimulus_3.started', leftStimulus_3.tStartRefresh)
    practiceTrials.addData('leftStimulus_3.stopped', leftStimulus_3.tStopRefresh)
    
    # ------Prepare to start Routine "practice_secondChoiceSpace_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    if condition == 1:
        toneDuration = 0 
    
    elif condition == 2:
        toneDuration = 0.2
    secondChoiceTone_2.setSound('1000', secs=toneDuration, hamming=True)
    secondChoiceTone_2.setVolume(psychopy_input_value, log=False)
    # keep track of which components have finished
    practice_secondChoiceSpace_2Components = [secondVisualStimulus_2, secondChoiceTone_2, secondChoiceLeftStimulus_2, secondChoiceRightStimulus_2]
    for thisComponent in practice_secondChoiceSpace_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_secondChoiceSpace_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice_secondChoiceSpace_2"-------
    while continueRoutine:
        # get current time
        t = practice_secondChoiceSpace_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_secondChoiceSpace_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *secondVisualStimulus_2* updates
        if secondVisualStimulus_2.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
            # keep track of start time/frame for later
            secondVisualStimulus_2.frameNStart = frameN  # exact frame index
            secondVisualStimulus_2.tStart = t  # local t and not account for scr refresh
            secondVisualStimulus_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(secondVisualStimulus_2, 'tStartRefresh')  # time at next scr refresh
            secondVisualStimulus_2.setAutoDraw(True)
        if secondVisualStimulus_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > secondVisualStimulus_2.tStartRefresh + 0.32-frameTolerance:
                # keep track of stop time/frame for later
                secondVisualStimulus_2.tStop = t  # not accounting for scr refresh
                secondVisualStimulus_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(secondVisualStimulus_2, 'tStopRefresh')  # time at next scr refresh
                secondVisualStimulus_2.setAutoDraw(False)
        # start/stop secondChoiceTone_2
        if secondChoiceTone_2.status == NOT_STARTED and tThisFlip >= toneOnset-frameTolerance:
            # keep track of start time/frame for later
            secondChoiceTone_2.frameNStart = frameN  # exact frame index
            secondChoiceTone_2.tStart = t  # local t and not account for scr refresh
            secondChoiceTone_2.tStartRefresh = tThisFlipGlobal  # on global time
            secondChoiceTone_2.play(when=win)  # sync with win flip
        if secondChoiceTone_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > secondChoiceTone_2.tStartRefresh + toneDuration-frameTolerance:
                # keep track of stop time/frame for later
                secondChoiceTone_2.tStop = t  # not accounting for scr refresh
                secondChoiceTone_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(secondChoiceTone_2, 'tStopRefresh')  # time at next scr refresh
                secondChoiceTone_2.stop()
        
        # *secondChoiceLeftStimulus_2* updates
        if secondChoiceLeftStimulus_2.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
            # keep track of start time/frame for later
            secondChoiceLeftStimulus_2.frameNStart = frameN  # exact frame index
            secondChoiceLeftStimulus_2.tStart = t  # local t and not account for scr refresh
            secondChoiceLeftStimulus_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(secondChoiceLeftStimulus_2, 'tStartRefresh')  # time at next scr refresh
            secondChoiceLeftStimulus_2.setAutoDraw(True)
        if secondChoiceLeftStimulus_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > secondChoiceLeftStimulus_2.tStartRefresh + 0.32-frameTolerance:
                # keep track of stop time/frame for later
                secondChoiceLeftStimulus_2.tStop = t  # not accounting for scr refresh
                secondChoiceLeftStimulus_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(secondChoiceLeftStimulus_2, 'tStopRefresh')  # time at next scr refresh
                secondChoiceLeftStimulus_2.setAutoDraw(False)
        
        # *secondChoiceRightStimulus_2* updates
        if secondChoiceRightStimulus_2.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
            # keep track of start time/frame for later
            secondChoiceRightStimulus_2.frameNStart = frameN  # exact frame index
            secondChoiceRightStimulus_2.tStart = t  # local t and not account for scr refresh
            secondChoiceRightStimulus_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(secondChoiceRightStimulus_2, 'tStartRefresh')  # time at next scr refresh
            secondChoiceRightStimulus_2.setAutoDraw(True)
        if secondChoiceRightStimulus_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > secondChoiceRightStimulus_2.tStartRefresh + 0.32-frameTolerance:
                # keep track of stop time/frame for later
                secondChoiceRightStimulus_2.tStop = t  # not accounting for scr refresh
                secondChoiceRightStimulus_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(secondChoiceRightStimulus_2, 'tStopRefresh')  # time at next scr refresh
                secondChoiceRightStimulus_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_secondChoiceSpace_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_secondChoiceSpace_2"-------
    for thisComponent in practice_secondChoiceSpace_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceTrials.addData('secondVisualStimulus_2.started', secondVisualStimulus_2.tStartRefresh)
    practiceTrials.addData('secondVisualStimulus_2.stopped', secondVisualStimulus_2.tStopRefresh)
    secondChoiceTone_2.stop()  # ensure sound has stopped at end of routine
    practiceTrials.addData('secondChoiceTone_2.started', secondChoiceTone_2.tStartRefresh)
    practiceTrials.addData('secondChoiceTone_2.stopped', secondChoiceTone_2.tStopRefresh)
    practiceTrials.addData('secondChoiceLeftStimulus_2.started', secondChoiceLeftStimulus_2.tStartRefresh)
    practiceTrials.addData('secondChoiceLeftStimulus_2.stopped', secondChoiceLeftStimulus_2.tStopRefresh)
    practiceTrials.addData('secondChoiceRightStimulus_2.started', secondChoiceRightStimulus_2.tStartRefresh)
    practiceTrials.addData('secondChoiceRightStimulus_2.stopped', secondChoiceRightStimulus_2.tStopRefresh)
    # the Routine "practice_secondChoiceSpace_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practice_decisionSpace"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    corrAns = condition
    decisionKey_2.keys = []
    decisionKey_2.rt = []
    _decisionKey_2_allKeys = []
    # keep track of which components have finished
    practice_decisionSpaceComponents = [decisionTextProbe_2, decisionKey_2]
    for thisComponent in practice_decisionSpaceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_decisionSpaceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice_decisionSpace"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_decisionSpaceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_decisionSpaceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *decisionTextProbe_2* updates
        if decisionTextProbe_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            decisionTextProbe_2.frameNStart = frameN  # exact frame index
            decisionTextProbe_2.tStart = t  # local t and not account for scr refresh
            decisionTextProbe_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(decisionTextProbe_2, 'tStartRefresh')  # time at next scr refresh
            decisionTextProbe_2.setAutoDraw(True)
        if decisionTextProbe_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > decisionTextProbe_2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                decisionTextProbe_2.tStop = t  # not accounting for scr refresh
                decisionTextProbe_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(decisionTextProbe_2, 'tStopRefresh')  # time at next scr refresh
                decisionTextProbe_2.setAutoDraw(False)
        
        # *decisionKey_2* updates
        waitOnFlip = False
        if decisionKey_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            decisionKey_2.frameNStart = frameN  # exact frame index
            decisionKey_2.tStart = t  # local t and not account for scr refresh
            decisionKey_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(decisionKey_2, 'tStartRefresh')  # time at next scr refresh
            decisionKey_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(decisionKey_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(decisionKey_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if decisionKey_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > decisionKey_2.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                decisionKey_2.tStop = t  # not accounting for scr refresh
                decisionKey_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(decisionKey_2, 'tStopRefresh')  # time at next scr refresh
                decisionKey_2.status = FINISHED
        if decisionKey_2.status == STARTED and not waitOnFlip:
            theseKeys = decisionKey_2.getKeys(keyList=['1', '2'], waitRelease=False)
            _decisionKey_2_allKeys.extend(theseKeys)
            if len(_decisionKey_2_allKeys):
                decisionKey_2.keys = _decisionKey_2_allKeys[-1].name  # just the last key pressed
                decisionKey_2.rt = _decisionKey_2_allKeys[-1].rt
                # was this correct?
                if (decisionKey_2.keys == str(corrAns)) or (decisionKey_2.keys == corrAns):
                    decisionKey_2.corr = 1
                else:
                    decisionKey_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_decisionSpaceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_decisionSpace"-------
    for thisComponent in practice_decisionSpaceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceTrials.addData('decisionTextProbe_2.started', decisionTextProbe_2.tStartRefresh)
    practiceTrials.addData('decisionTextProbe_2.stopped', decisionTextProbe_2.tStopRefresh)
    # check responses
    if decisionKey_2.keys in ['', [], None]:  # No response was made
        decisionKey_2.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           decisionKey_2.corr = 1;  # correct non-response
        else:
           decisionKey_2.corr = 0;  # failed to respond (incorrectly)
    # store data for practiceTrials (TrialHandler)
    practiceTrials.addData('decisionKey_2.keys',decisionKey_2.keys)
    practiceTrials.addData('decisionKey_2.corr', decisionKey_2.corr)
    if decisionKey_2.keys != None:  # we had a response
        practiceTrials.addData('decisionKey_2.rt', decisionKey_2.rt)
    practiceTrials.addData('decisionKey_2.started', decisionKey_2.tStartRefresh)
    practiceTrials.addData('decisionKey_2.stopped', decisionKey_2.tStopRefresh)
    
    # ------Prepare to start Routine "practice_feedbackSpace"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if decisionKey_2.keys[0] == str(corrAns):
       feedback = "Correct" 
    
    if decisionKey_2.keys[0] != str(corrAns):
       feedback = "Incorrect" 
    
    
    feedbackText_2.setText(feedback)
    # keep track of which components have finished
    practice_feedbackSpaceComponents = [feedbackText_2]
    for thisComponent in practice_feedbackSpaceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_feedbackSpaceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice_feedbackSpace"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_feedbackSpaceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_feedbackSpaceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbackText_2* updates
        if feedbackText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackText_2.frameNStart = frameN  # exact frame index
            feedbackText_2.tStart = t  # local t and not account for scr refresh
            feedbackText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackText_2, 'tStartRefresh')  # time at next scr refresh
            feedbackText_2.setAutoDraw(True)
        if feedbackText_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackText_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedbackText_2.tStop = t  # not accounting for scr refresh
                feedbackText_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackText_2, 'tStopRefresh')  # time at next scr refresh
                feedbackText_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_feedbackSpaceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_feedbackSpace"-------
    for thisComponent in practice_feedbackSpaceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceTrials.addData('feedbackText_2.started', feedbackText_2.tStartRefresh)
    practiceTrials.addData('feedbackText_2.stopped', feedbackText_2.tStopRefresh)
    
    # ------Prepare to start Routine "practiceComplete"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    practiceCompleteComponents = [text_7, key_resp_7]
    for thisComponent in practiceCompleteComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceCompleteClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practiceComplete"-------
    while continueRoutine:
        # get current time
        t = practiceCompleteClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceCompleteClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['c'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceCompleteComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practiceComplete"-------
    for thisComponent in practiceCompleteComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practiceTrials.addData('text_7.started', text_7.tStartRefresh)
    practiceTrials.addData('text_7.stopped', text_7.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    practiceTrials.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        practiceTrials.addData('key_resp_7.rt', key_resp_7.rt)
    practiceTrials.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    practiceTrials.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    # the Routine "practiceComplete" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'practiceTrials'


# ------Prepare to start Routine "beginTest"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
beginTestComponents = [text_10, key_resp_8]
for thisComponent in beginTestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
beginTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "beginTest"-------
while continueRoutine:
    # get current time
    t = beginTestClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=beginTestClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['b'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginTestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "beginTest"-------
for thisComponent in beginTestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "beginTest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "setUp"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
setUpComponents = [firstITI]
for thisComponent in setUpComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setUpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setUp"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = setUpClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setUpClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *firstITI* updates
    if firstITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        firstITI.frameNStart = frameN  # exact frame index
        firstITI.tStart = t  # local t and not account for scr refresh
        firstITI.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(firstITI, 'tStartRefresh')  # time at next scr refresh
        firstITI.setAutoDraw(True)
    if firstITI.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > firstITI.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            firstITI.tStop = t  # not accounting for scr refresh
            firstITI.frameNStop = frameN  # exact frame index
            win.timeOnFlip(firstITI, 'tStopRefresh')  # time at next scr refresh
            firstITI.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setUpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setUp"-------
for thisComponent in setUpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('firstITI.started', firstITI.tStartRefresh)
thisExp.addData('firstITI.stopped', firstITI.tStopRefresh)

# set up handler to look after randomisation of trials etc
conditions = data.importConditions('questConditionsFile.xlsx')
trials = data.MultiStairHandler(stairType='quest', name='trials',
    nTrials=30,
    conditions=conditions,
    method='random',
    originPath=-1)
thisExp.addLoop(trials)  # add the loop to the experiment
# initialise values for first condition
level = trials._nextIntensity  # initialise some vals
condition = trials.currentStaircase.condition

for level, condition in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
    for paramName in condition:
        exec(paramName + '= condition[paramName]')
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    #tone
    #randomly assign which interval the tone appears in 
    if trialNumber == 0:
        halfNTrials = int(trials.nTrials/2)
        trialList = ['1']*halfNTrials + ['2']*halfNTrials
        np.random.shuffle(trialList)
        print(trialList)
    
    #convert variable types to integer
    calibration = float(calibration)
    desired_db = float(level)
    psychopy_input_value = ((calibration)/(10**(117/20))*(10**(desired_db/20)))
    
    #Noise
    if expInfo['Condition'] == 'Quiet': #if the Condition is Quiet, turn off background noise 
        print('Quiet condition selected')
        psychopy_input_value_for_noise = 0
    else:
        noise_db = int(40)
        calibration = float(calibration)
        psychopy_input_value_for_noise = ((calibration)/(10**(117/20))*(10**(noise_db/20)))
    
    #print
    print('desired dB on this loop was:', desired_db)
    print('psychopy input value', psychopy_input_value)
    print('calibration:', calibration)
    print('psychopyvalue for noise:', psychopy_input_value_for_noise)
    
    # keep track of which components have finished
    ITIComponents = [text]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addOtherData('text.started', text.tStartRefresh)
    trials.addOtherData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "firstChoiceSpace"-------
    continueRoutine = True
    # update component parameters for each repeat
    condition = trialList[trialNumber]
    if condition == '1':
        toneDuration = presetToneDuration
    
    elif condition == '2':
        toneDuration = 0
    firstChoiceNoise.setSound('Noise_BP_600_1400.wav', secs=0.32, hamming=True)
    firstChoiceNoise.setVolume(psychopy_input_value_for_noise, log=False)
    firstChoiceProbeTone.setSound('1000', secs=toneDuration, hamming=True)
    firstChoiceProbeTone.setVolume(psychopy_input_value, log=False)
    # keep track of which components have finished
    firstChoiceSpaceComponents = [firstVisualStimulus, firstChoiceNoise, firstChoiceProbeTone, firstChoiceLeftStimulus, firstChoiceRightStimulus]
    for thisComponent in firstChoiceSpaceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    firstChoiceSpaceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "firstChoiceSpace"-------
    while continueRoutine:
        # get current time
        t = firstChoiceSpaceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=firstChoiceSpaceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *firstVisualStimulus* updates
        if firstVisualStimulus.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
            # keep track of start time/frame for later
            firstVisualStimulus.frameNStart = frameN  # exact frame index
            firstVisualStimulus.tStart = t  # local t and not account for scr refresh
            firstVisualStimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firstVisualStimulus, 'tStartRefresh')  # time at next scr refresh
            firstVisualStimulus.setAutoDraw(True)
        if firstVisualStimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > firstVisualStimulus.tStartRefresh + 0.32-frameTolerance:
                # keep track of stop time/frame for later
                firstVisualStimulus.tStop = t  # not accounting for scr refresh
                firstVisualStimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(firstVisualStimulus, 'tStopRefresh')  # time at next scr refresh
                firstVisualStimulus.setAutoDraw(False)
        # start/stop firstChoiceNoise
        if firstChoiceNoise.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
            # keep track of start time/frame for later
            firstChoiceNoise.frameNStart = frameN  # exact frame index
            firstChoiceNoise.tStart = t  # local t and not account for scr refresh
            firstChoiceNoise.tStartRefresh = tThisFlipGlobal  # on global time
            firstChoiceNoise.play(when=win)  # sync with win flip
        if firstChoiceNoise.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > firstChoiceNoise.tStartRefresh + 0.32-frameTolerance:
                # keep track of stop time/frame for later
                firstChoiceNoise.tStop = t  # not accounting for scr refresh
                firstChoiceNoise.frameNStop = frameN  # exact frame index
                win.timeOnFlip(firstChoiceNoise, 'tStopRefresh')  # time at next scr refresh
                firstChoiceNoise.stop()
        # start/stop firstChoiceProbeTone
        if firstChoiceProbeTone.status == NOT_STARTED and tThisFlip >= toneOnset-frameTolerance:
            # keep track of start time/frame for later
            firstChoiceProbeTone.frameNStart = frameN  # exact frame index
            firstChoiceProbeTone.tStart = t  # local t and not account for scr refresh
            firstChoiceProbeTone.tStartRefresh = tThisFlipGlobal  # on global time
            firstChoiceProbeTone.play(when=win)  # sync with win flip
        if firstChoiceProbeTone.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > firstChoiceProbeTone.tStartRefresh + toneDuration-frameTolerance:
                # keep track of stop time/frame for later
                firstChoiceProbeTone.tStop = t  # not accounting for scr refresh
                firstChoiceProbeTone.frameNStop = frameN  # exact frame index
                win.timeOnFlip(firstChoiceProbeTone, 'tStopRefresh')  # time at next scr refresh
                firstChoiceProbeTone.stop()
        
        # *firstChoiceLeftStimulus* updates
        if firstChoiceLeftStimulus.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
            # keep track of start time/frame for later
            firstChoiceLeftStimulus.frameNStart = frameN  # exact frame index
            firstChoiceLeftStimulus.tStart = t  # local t and not account for scr refresh
            firstChoiceLeftStimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firstChoiceLeftStimulus, 'tStartRefresh')  # time at next scr refresh
            firstChoiceLeftStimulus.setAutoDraw(True)
        if firstChoiceLeftStimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > firstChoiceLeftStimulus.tStartRefresh + 0.32-frameTolerance:
                # keep track of stop time/frame for later
                firstChoiceLeftStimulus.tStop = t  # not accounting for scr refresh
                firstChoiceLeftStimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(firstChoiceLeftStimulus, 'tStopRefresh')  # time at next scr refresh
                firstChoiceLeftStimulus.setAutoDraw(False)
        
        # *firstChoiceRightStimulus* updates
        if firstChoiceRightStimulus.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
            # keep track of start time/frame for later
            firstChoiceRightStimulus.frameNStart = frameN  # exact frame index
            firstChoiceRightStimulus.tStart = t  # local t and not account for scr refresh
            firstChoiceRightStimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(firstChoiceRightStimulus, 'tStartRefresh')  # time at next scr refresh
            firstChoiceRightStimulus.setAutoDraw(True)
        if firstChoiceRightStimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > firstChoiceRightStimulus.tStartRefresh + 0.32-frameTolerance:
                # keep track of stop time/frame for later
                firstChoiceRightStimulus.tStop = t  # not accounting for scr refresh
                firstChoiceRightStimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(firstChoiceRightStimulus, 'tStopRefresh')  # time at next scr refresh
                firstChoiceRightStimulus.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in firstChoiceSpaceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "firstChoiceSpace"-------
    for thisComponent in firstChoiceSpaceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addOtherData('firstVisualStimulus.started', firstVisualStimulus.tStartRefresh)
    trials.addOtherData('firstVisualStimulus.stopped', firstVisualStimulus.tStopRefresh)
    firstChoiceNoise.stop()  # ensure sound has stopped at end of routine
    trials.addOtherData('firstChoiceNoise.started', firstChoiceNoise.tStartRefresh)
    trials.addOtherData('firstChoiceNoise.stopped', firstChoiceNoise.tStopRefresh)
    firstChoiceProbeTone.stop()  # ensure sound has stopped at end of routine
    trials.addOtherData('firstChoiceProbeTone.started', firstChoiceProbeTone.tStartRefresh)
    trials.addOtherData('firstChoiceProbeTone.stopped', firstChoiceProbeTone.tStopRefresh)
    trials.addOtherData('firstChoiceLeftStimulus.started', firstChoiceLeftStimulus.tStartRefresh)
    trials.addOtherData('firstChoiceLeftStimulus.stopped', firstChoiceLeftStimulus.tStopRefresh)
    trials.addOtherData('firstChoiceRightStimulus.started', firstChoiceRightStimulus.tStartRefresh)
    trials.addOtherData('firstChoiceRightStimulus.stopped', firstChoiceRightStimulus.tStopRefresh)
    # the Routine "firstChoiceSpace" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ISI"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [ISIVisualStimulus, rightStimulus, leftStimulus]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISIVisualStimulus* updates
        if ISIVisualStimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISIVisualStimulus.frameNStart = frameN  # exact frame index
            ISIVisualStimulus.tStart = t  # local t and not account for scr refresh
            ISIVisualStimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISIVisualStimulus, 'tStartRefresh')  # time at next scr refresh
            ISIVisualStimulus.setAutoDraw(True)
        if ISIVisualStimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISIVisualStimulus.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                ISIVisualStimulus.tStop = t  # not accounting for scr refresh
                ISIVisualStimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ISIVisualStimulus, 'tStopRefresh')  # time at next scr refresh
                ISIVisualStimulus.setAutoDraw(False)
        
        # *rightStimulus* updates
        if rightStimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightStimulus.frameNStart = frameN  # exact frame index
            rightStimulus.tStart = t  # local t and not account for scr refresh
            rightStimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightStimulus, 'tStartRefresh')  # time at next scr refresh
            rightStimulus.setAutoDraw(True)
        if rightStimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rightStimulus.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                rightStimulus.tStop = t  # not accounting for scr refresh
                rightStimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rightStimulus, 'tStopRefresh')  # time at next scr refresh
                rightStimulus.setAutoDraw(False)
        
        # *leftStimulus* updates
        if leftStimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            leftStimulus.frameNStart = frameN  # exact frame index
            leftStimulus.tStart = t  # local t and not account for scr refresh
            leftStimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftStimulus, 'tStartRefresh')  # time at next scr refresh
            leftStimulus.setAutoDraw(True)
        if leftStimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > leftStimulus.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                leftStimulus.tStop = t  # not accounting for scr refresh
                leftStimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(leftStimulus, 'tStopRefresh')  # time at next scr refresh
                leftStimulus.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addOtherData('ISIVisualStimulus.started', ISIVisualStimulus.tStartRefresh)
    trials.addOtherData('ISIVisualStimulus.stopped', ISIVisualStimulus.tStopRefresh)
    trials.addOtherData('rightStimulus.started', rightStimulus.tStartRefresh)
    trials.addOtherData('rightStimulus.stopped', rightStimulus.tStopRefresh)
    trials.addOtherData('leftStimulus.started', leftStimulus.tStartRefresh)
    trials.addOtherData('leftStimulus.stopped', leftStimulus.tStopRefresh)
    
    # ------Prepare to start Routine "secondChoiceSpace"-------
    continueRoutine = True
    # update component parameters for each repeat
    if condition == '1':
        toneDuration = 0 
    
    elif condition == '2':
        toneDuration = presetToneDuration
    
    secondChoiceNoise.setSound('Noise_BP_600_1400.wav', secs=0.32, hamming=True)
    secondChoiceNoise.setVolume(psychopy_input_value_for_noise, log=False)
    secondChoiceTone.setSound('1000', secs=toneDuration, hamming=True)
    secondChoiceTone.setVolume(psychopy_input_value, log=False)
    # keep track of which components have finished
    secondChoiceSpaceComponents = [secondVisualStimulus, secondChoiceNoise, secondChoiceTone, secondChoiceLeftStimulus, secondChoiceRightStimulus]
    for thisComponent in secondChoiceSpaceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    secondChoiceSpaceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "secondChoiceSpace"-------
    while continueRoutine:
        # get current time
        t = secondChoiceSpaceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=secondChoiceSpaceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *secondVisualStimulus* updates
        if secondVisualStimulus.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
            # keep track of start time/frame for later
            secondVisualStimulus.frameNStart = frameN  # exact frame index
            secondVisualStimulus.tStart = t  # local t and not account for scr refresh
            secondVisualStimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(secondVisualStimulus, 'tStartRefresh')  # time at next scr refresh
            secondVisualStimulus.setAutoDraw(True)
        if secondVisualStimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > secondVisualStimulus.tStartRefresh + 0.32-frameTolerance:
                # keep track of stop time/frame for later
                secondVisualStimulus.tStop = t  # not accounting for scr refresh
                secondVisualStimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(secondVisualStimulus, 'tStopRefresh')  # time at next scr refresh
                secondVisualStimulus.setAutoDraw(False)
        # start/stop secondChoiceNoise
        if secondChoiceNoise.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
            # keep track of start time/frame for later
            secondChoiceNoise.frameNStart = frameN  # exact frame index
            secondChoiceNoise.tStart = t  # local t and not account for scr refresh
            secondChoiceNoise.tStartRefresh = tThisFlipGlobal  # on global time
            secondChoiceNoise.play(when=win)  # sync with win flip
        if secondChoiceNoise.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > secondChoiceNoise.tStartRefresh + 0.32-frameTolerance:
                # keep track of stop time/frame for later
                secondChoiceNoise.tStop = t  # not accounting for scr refresh
                secondChoiceNoise.frameNStop = frameN  # exact frame index
                win.timeOnFlip(secondChoiceNoise, 'tStopRefresh')  # time at next scr refresh
                secondChoiceNoise.stop()
        # start/stop secondChoiceTone
        if secondChoiceTone.status == NOT_STARTED and tThisFlip >= toneOnset-frameTolerance:
            # keep track of start time/frame for later
            secondChoiceTone.frameNStart = frameN  # exact frame index
            secondChoiceTone.tStart = t  # local t and not account for scr refresh
            secondChoiceTone.tStartRefresh = tThisFlipGlobal  # on global time
            secondChoiceTone.play(when=win)  # sync with win flip
        if secondChoiceTone.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > secondChoiceTone.tStartRefresh + toneDuration-frameTolerance:
                # keep track of stop time/frame for later
                secondChoiceTone.tStop = t  # not accounting for scr refresh
                secondChoiceTone.frameNStop = frameN  # exact frame index
                win.timeOnFlip(secondChoiceTone, 'tStopRefresh')  # time at next scr refresh
                secondChoiceTone.stop()
        
        # *secondChoiceLeftStimulus* updates
        if secondChoiceLeftStimulus.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
            # keep track of start time/frame for later
            secondChoiceLeftStimulus.frameNStart = frameN  # exact frame index
            secondChoiceLeftStimulus.tStart = t  # local t and not account for scr refresh
            secondChoiceLeftStimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(secondChoiceLeftStimulus, 'tStartRefresh')  # time at next scr refresh
            secondChoiceLeftStimulus.setAutoDraw(True)
        if secondChoiceLeftStimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > secondChoiceLeftStimulus.tStartRefresh + 0.32-frameTolerance:
                # keep track of stop time/frame for later
                secondChoiceLeftStimulus.tStop = t  # not accounting for scr refresh
                secondChoiceLeftStimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(secondChoiceLeftStimulus, 'tStopRefresh')  # time at next scr refresh
                secondChoiceLeftStimulus.setAutoDraw(False)
        
        # *secondChoiceRightStimulus* updates
        if secondChoiceRightStimulus.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
            # keep track of start time/frame for later
            secondChoiceRightStimulus.frameNStart = frameN  # exact frame index
            secondChoiceRightStimulus.tStart = t  # local t and not account for scr refresh
            secondChoiceRightStimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(secondChoiceRightStimulus, 'tStartRefresh')  # time at next scr refresh
            secondChoiceRightStimulus.setAutoDraw(True)
        if secondChoiceRightStimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > secondChoiceRightStimulus.tStartRefresh + 0.32-frameTolerance:
                # keep track of stop time/frame for later
                secondChoiceRightStimulus.tStop = t  # not accounting for scr refresh
                secondChoiceRightStimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(secondChoiceRightStimulus, 'tStopRefresh')  # time at next scr refresh
                secondChoiceRightStimulus.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in secondChoiceSpaceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "secondChoiceSpace"-------
    for thisComponent in secondChoiceSpaceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addOtherData('secondVisualStimulus.started', secondVisualStimulus.tStartRefresh)
    trials.addOtherData('secondVisualStimulus.stopped', secondVisualStimulus.tStopRefresh)
    secondChoiceNoise.stop()  # ensure sound has stopped at end of routine
    trials.addOtherData('secondChoiceNoise.started', secondChoiceNoise.tStartRefresh)
    trials.addOtherData('secondChoiceNoise.stopped', secondChoiceNoise.tStopRefresh)
    secondChoiceTone.stop()  # ensure sound has stopped at end of routine
    trials.addOtherData('secondChoiceTone.started', secondChoiceTone.tStartRefresh)
    trials.addOtherData('secondChoiceTone.stopped', secondChoiceTone.tStopRefresh)
    trials.addOtherData('secondChoiceLeftStimulus.started', secondChoiceLeftStimulus.tStartRefresh)
    trials.addOtherData('secondChoiceLeftStimulus.stopped', secondChoiceLeftStimulus.tStopRefresh)
    trials.addOtherData('secondChoiceRightStimulus.started', secondChoiceRightStimulus.tStartRefresh)
    trials.addOtherData('secondChoiceRightStimulus.stopped', secondChoiceRightStimulus.tStopRefresh)
    # the Routine "secondChoiceSpace" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "decisionSpace"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    corrAns = condition
    decisionKey.keys = []
    decisionKey.rt = []
    _decisionKey_allKeys = []
    # keep track of which components have finished
    decisionSpaceComponents = [decisionTextProbe, decisionKey]
    for thisComponent in decisionSpaceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    decisionSpaceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "decisionSpace"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = decisionSpaceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=decisionSpaceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *decisionTextProbe* updates
        if decisionTextProbe.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            decisionTextProbe.frameNStart = frameN  # exact frame index
            decisionTextProbe.tStart = t  # local t and not account for scr refresh
            decisionTextProbe.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(decisionTextProbe, 'tStartRefresh')  # time at next scr refresh
            decisionTextProbe.setAutoDraw(True)
        if decisionTextProbe.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > decisionTextProbe.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                decisionTextProbe.tStop = t  # not accounting for scr refresh
                decisionTextProbe.frameNStop = frameN  # exact frame index
                win.timeOnFlip(decisionTextProbe, 'tStopRefresh')  # time at next scr refresh
                decisionTextProbe.setAutoDraw(False)
        
        # *decisionKey* updates
        waitOnFlip = False
        if decisionKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            decisionKey.frameNStart = frameN  # exact frame index
            decisionKey.tStart = t  # local t and not account for scr refresh
            decisionKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(decisionKey, 'tStartRefresh')  # time at next scr refresh
            decisionKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(decisionKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(decisionKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if decisionKey.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > decisionKey.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                decisionKey.tStop = t  # not accounting for scr refresh
                decisionKey.frameNStop = frameN  # exact frame index
                win.timeOnFlip(decisionKey, 'tStopRefresh')  # time at next scr refresh
                decisionKey.status = FINISHED
        if decisionKey.status == STARTED and not waitOnFlip:
            theseKeys = decisionKey.getKeys(keyList=['1', '2'], waitRelease=False)
            _decisionKey_allKeys.extend(theseKeys)
            if len(_decisionKey_allKeys):
                decisionKey.keys = _decisionKey_allKeys[-1].name  # just the last key pressed
                decisionKey.rt = _decisionKey_allKeys[-1].rt
                # was this correct?
                if (decisionKey.keys == str(corrAns)) or (decisionKey.keys == corrAns):
                    decisionKey.corr = 1
                else:
                    decisionKey.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in decisionSpaceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "decisionSpace"-------
    for thisComponent in decisionSpaceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addOtherData('decisionTextProbe.started', decisionTextProbe.tStartRefresh)
    trials.addOtherData('decisionTextProbe.stopped', decisionTextProbe.tStopRefresh)
    # check responses
    if decisionKey.keys in ['', [], None]:  # No response was made
        decisionKey.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           decisionKey.corr = 1;  # correct non-response
        else:
           decisionKey.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (MultiStairHandler)
    trials.addResponse(decisionKey.corr)
    trials.addOtherData('decisionKey.rt', decisionKey.rt)
    trials.addOtherData('decisionKey.started', decisionKey.tStartRefresh)
    trials.addOtherData('decisionKey.stopped', decisionKey.tStopRefresh)
    
    # ------Prepare to start Routine "feedbackSpace"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if decisionKey.keys[0] == str(corrAns):
       feedback = "Correct" 
    
    if decisionKey.keys[0] != str(corrAns):
       feedback = "Incorrect" 
    
    
    feedbackText.setText(feedback)
    # keep track of which components have finished
    feedbackSpaceComponents = [feedbackText]
    for thisComponent in feedbackSpaceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackSpaceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackSpace"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackSpaceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackSpaceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbackText* updates
        if feedbackText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackText.frameNStart = frameN  # exact frame index
            feedbackText.tStart = t  # local t and not account for scr refresh
            feedbackText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackText, 'tStartRefresh')  # time at next scr refresh
            feedbackText.setAutoDraw(True)
        if feedbackText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackText.tStartRefresh + 1.0-frameTolerance:
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
        for thisComponent in feedbackSpaceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackSpace"-------
    for thisComponent in feedbackSpaceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    print('trialNumber:', trialNumber, 'tone was presented in interval: ', condition, 'toneVolume was:', desired_db, 'participant was: ', feedback)
    trialNumber = trialNumber + 1
    trials.addOtherData('feedbackText.started', feedbackText.tStartRefresh)
    trials.addOtherData('feedbackText.stopped', feedbackText.tStopRefresh)
    thisExp.nextEntry()
    
# all staircases completed


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
