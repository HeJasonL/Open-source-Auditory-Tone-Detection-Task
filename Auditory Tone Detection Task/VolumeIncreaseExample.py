from __future__ import division
from psychopy import sound, event, visual, core

#set the sound
Noise=sound.SoundPyo('Noise_BP_600_1400.wav')#change this path to your sound/wav file

#What volume do you want to start at in dB.
thisVol =  50
#how much do you want the volume to increase by following a response?
increase=1
#how many trials you want 
trials=10

for i in range(trials):
    Vol=((0.34/0.1)/(10**(111.8/20)))*(10**(thisVol/20))#Changes the volume of the sound in line with current intensity
    Noise.setVolume(Vol)
    print ('sound playing at',thisVol, 'db' )
    Noise.play()
    event.waitKeys()
    Noise.stop()
    thisVol=thisVol+increase

core.quit()