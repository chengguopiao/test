#!/usr/bin/env python
import unittest
import string
import os
import commands
import random
import time

"""
@author:Cao Lina
@Note:Stability test cases for intel camera2.2
"""
PACKAGE_NAME = 'com.intel.camera22'
ACTIVITY_NAME = PACKAGE_NAME + '.Camera'
DCIM_PATH = '/mnt/sdcard/DCIM'
CAMERA_FOLDER = '100ANDRO'
CAMERA_ID = 'cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_camera_id_key'
Flash_STATE= 'cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_flashmode_key'
Exposure_STATE= 'cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_exposure_key'
Scene_STATE = 'cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_scenemode_key'
FDFR_STATE ='cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_fdfr_key'
PictureSize_STATE ='cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_picture_size_key'
Geolocation_STATE ='cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_camera_geo_location_key'
Hints_STATE ='cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_hints_key'
WhiteBalance_STATE='cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_whitebalance_key'
ISO_STATE='cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_iso_key'
SelfTimer_STATE='cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_delay_shooting_key'
Delete_CMD ='rm -r sdcard/DCIM/100ANDRO/' 
PICTURE_PATH = '' + os.sep + 'mnt'+os.sep+ DCIM_PATH+ '/'+CAMERA_FOLDER

CAMERA_ID_FRONT = '1'
CAMERA_ID_BACK = '0'
Camera=(366,1000)
Setting=(60,62)
Exposure=(404,172)
Scences=(288,172)
PictureSize=(170,172)
Geolocation=(60,166)
SwitchCamera=(658,50)

class BurstCameraTest(unittest.TestCase):

    def setUp(self):
        super(BurstCameraTest, self).setUp()

        #Set the name and component to start activity
        self.runComponent= PACKAGE_NAME + '/' + ACTIVITY_NAME
        # Runs the component
        self._launchBurst()
        
    def testCaptureWithExposure(self):
        """
        Summary:testCaptureWithExposurePlusOne: Take burst piture with exposure +1
        Steps:  1.Launch burst  activity
                2.Check exposure setting icon ,set to +1
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png', similarity=0.6)          
        #Step 2
	exposure = random.choice( ['3', '6', '0','-3','-6'] )
        self._setExposureStatus(exposure)
        #Step 3
        self._takeBurstCapture()



    def testCapturePictureWithScenes(self):
        """
        Summary:testCapturePictureWithScenesSport: Take picture with set scenes to Sports
        Steps:  1.Launch burst activity
                2.Check scence mode ,set mode to Sports
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png', similarity=0.6) 
        # Step 2
	scence = random.choice( ['sports', 'night', 'landscape','portrait','auto','night-portrait','barcode'] )
        self._setScenesStatus(scence)
        #Step 3
        self._takeBurstCapture()
        self._setScenesStatus('auto')


    def testCaptureWithPictureSize(self):
        """
        Summary:testCaptureWithPictureSizeStandard: Take picture with set the size 8M
        Steps:  1.Launch burst activity
                2.Check photo size ,set to 8M
                3.Touch shutter button to capture burst picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png', similarity=0.6) 
        #Step 2
	picturesize = random.choice( ['StandardScreen', 'WideScreen'] )
        self._setPictureSizeStatus(picturesize)
        #Step 3
        self._takeBurstCapture()
	time.sleep(1)
	self._setPictureSizeStatus('WideScreen')



    def testCapturepictureWithGeoLocation(self):
        """
        Summary:testCapturepictureWithGeoLocationOn: Take picture in geolocation on mode
        Steps:  1.Launch burst activity
                2.Check geo-tag ,set to ON
                3.Touch shutter button to capture burst picture
                4.Exit activity
        """ 
        self.expect('1_launch_checkpoint.png', similarity=0.6) 
        #Step 2
	location = random.choice( ['on', 'off'] )
        self._setGeoLocationStatus(location)
        #Step 3
        self._takeBurstCapture()


    def _takeBurstCapture(self):
        #Get the number of photo in sdcard
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            beforeNo = '0'
        #Get the number of photo in sdcard
        else:
            beforeNo = commands.getoutput('adb shell ls /mnt/sdcard/DCIM/*  | grep BST | wc -l')
        self.touch(Camera,waittime=20)
        afterNo = commands.getoutput('adb shell ls /mnt/sdcard/DCIM/*  | grep BST | wc -l')
        if string.atoi(beforeNo) != string.atoi(afterNo) - 10:
            self.fail('take picture fail!')  

    def _setExposureStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        # Enter exposuer setting
        self.touch(Setting)\
        .touch(Exposure)
        if status =='0':
            self.touch((288,292))
        elif status =='3':
            self.touch((408,290))
        elif status =='6':
            self.touch((520,294))
        elif status =='-3':
            self.touch((166,290))
        elif status =='-6':
            self.touch((60,294))
        state = self.adbCmd(Exposure_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera exposure'+status+'fail!')

    def _setScenesStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(Scences)
        if status =='sports':
            #commands.getoutput('adb shell input swipe 640 308 302 300')
            self.touch((640,300))
        elif status =='night':
            self.touch((530,300))
        elif status =='landscape':
            self.touch((400,300))
        elif status =='portrait':
            self.touch((300,300))
	elif status == 'night-portrait':
            self.touch((170,294))
        elif status == 'barcode':
            self.touch((50,294))
        #elif status == 'fireworks':
            #self.touch((50,294))
        elif status =='auto':
            commands.getoutput('adb shell input swipe 640 308 302 300')
            self.touch((640,270))
        state = self.adbCmd(Scene_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera scenes to'+status+'fail!')

    def _setPictureSizeStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(PictureSize)
        if status =='WideScreen':
            self.touch((56,292))
        elif status =='StandardScreen':
            self.touch((176,292))
        state = self.adbCmd(PictureSize_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera picture size to'+status+'fail!')

    def _setGeoLocationStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(Geolocation)
        if status =='on':
            self.touch((170,284))
        elif status =='off':
            self.touch((60,284))
        state = self.adbCmd(Geolocation_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera geoloaction'+status+'fail!')

    def _identifyCameraBack(self):
        #Check camera already set to back camera successfully
        self.logger.debug("Check the rear camera...")
        cameid2value = self.adbCmd(CAMERA_ID)
        self.logger.debug("Camera ID 2 value is: " + cameid2value)
        if cameid2value !='':
            mCameraID2Value = cameid2value.find(CAMERA_ID_BACK)
            if mCameraID2Value == -1:
                self.logger.debug("Switch the camera to back...")
                commands.getoutput('adb shell input swipe 530 6 523 22')
                self.touch(SwitchCamera,waittime=5)
                self.failIf(self.adbCmd(CAMERA_ID).find(CAMERA_ID_BACK) == -1,"Switch the camera to rear failed...")
            else:
                self.logger.debug("Current camera is rear...")
        else:
            self.logger.debug("Current camera is rear...")

    def _launchBurst(self):
        self.launch(self.runComponent)
        if self.exists('location.png'):
            self.touch('ok.png')
        self._identifyCameraBack()
        self.touch((650,1090),waittime=3)\
        .touch((358,1076),waittime=3)\
        .touch((360,922),waittime=3) 

    def tearDown(self):
        self.adbCmd('rm -r '+ PICTURE_PATH + '/*')
        self.press('back,back,back,home')
        super(BurstCameraTest,self).tearDown()
