#/usr/bin/python 

from devicewrapper.android import device as d
from uiautomator import device as dd
import unittest
import time
import os
import sys
import commands
import string    




######################################################################
CPTUREBUTTON_RESOURCEID ='com.intel.camera22:id/shutter_button'
FRONTBACKBUTTON_DESCR = 'Front and back camera switch'
CPTUREPOINT='adb shell input swipe 363 1145 359 1045 '
DRAWUP_CAPTUREBUTTON='adb shell input swipe 363 1145 359 1045 '
DRAWDOWN_MENU='adb shell input swipe 530 6 523 22'

CAMERA_ID = 'adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_camera_id_key'



class Util:
    def __init__(self):
        pass


    def _takePicture(self,status):
        # capture single image
        def singlecapture():
            d(resourceId = CPTUREBUTTON_RESOURCEID).click.wait()
        # capture smile image
        def smilecapture():
            d(resourceId = CPTUREBUTTON_RESOURCEID).click.wait()
            time.sleep(2)
            d(resourceId = CPTUREBUTTON_RESOURCEID).click.wait()
        # capture single image by press 2s
        def longclickcapture():
            commands.getoutput(DRAWUP_CAPTUREBUTTON + '2000')
            time.sleep(2) 
        #Dictionary
        takemode={'single':singlecapture,'smile':smilecapture,'longclick':longclickcapture}    
        takemode[status]()
     
    def _takePictureCustomTime(self,status): 
        # capture image by press Custom Time
        commands.getoutput(DRAWUP_CAPTUREBUTTON+ (status+'000'))


    def _takeVideo(self,status):
        # Start record video
        d(resourceId = CPTUREBUTTON_RESOURCEID).click.wait() 
        # Set recording time
        time.sleep(string.atoi(status) - string.atoi('2'))
        #Stop record video
        d(resourceId = CPTUREBUTTON_RESOURCEID).click.wait() 
        return True

    def _switchBackOrFrontCamera(self,status):
        #Dictionary
        camerastatus = {'back': '0','front':'1'}  
        # Get the current camera status
        currentstatus = commands.getoutput(CAMERA_ID)
        # Confirm the current status of the user is required
        if currentstatus.find(camerastatus.get(status)) == -1:
            # draw down the menu
            commands.getoutput(DRAWDOWN_MENU)
            time.sleep(1)
            # set the camera status
            d(description = FRONTBACKBUTTON_DESCR).click.wait()
            time.sleep(3)
            # Get the current camera status
            currentstatus = commands.getoutput(CAMERA_ID)
            # check the result
            if currentstatus.find(camerastatus.get(status)) != -1:
                print ('set camear is '+status)
                return True
            else:
                print ('set camear is '+status+' fail')
                return False
        else:
            print('Current camera is ' + status)


if __name__ == '__main__':
    Util.()
