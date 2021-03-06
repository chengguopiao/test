#!/usr/bin/env python
import unittest
import string
import os
import time
import commands
import random

"""
@author:Cao Lina
@Note:Feature test for intel camera2.2
"""
PACKAGE_NAME = 'com.intel.camera22'
ACTIVITY_NAME = PACKAGE_NAME + '.Camera'
DCIM_PATH = '/sdcard/DCIM'
CAMERA_FOLDER = '100ANDRO'

FDFR_STATE ='cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_fdfr_key'
PictureSize_STATE ='cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_picture_size_key'
Geolocation_STATE ='cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_camera_geo_location_key' 
Exposure_STATE= 'cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_exposure_key'
SelfTimer_STATE='cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_delay_shooting_key'

PICTURE_PATH = '' + os.sep + 'mnt'+os.sep+ DCIM_PATH+ '/'+CAMERA_FOLDER
Camera=(356,1076)
Setting=(60,64)
Picturesize=(176,176)
Geolocation=(59,170)
Exposure=(288,170)
FDFR=(661,64)
Self_Timer=(273,181)

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        self._launchHdr()

    # Test case 1
    def testCapturePictureWithFD(self):
        """
        Summary:testCapturePictureWithFDOn: Take a picture with FD/FR on
        Steps:  1.Launch HDR capture activity
                2.Set FD/FR
                3.Touch shutter button to capture picture
                4.Exit activity
        """
        self.expect('1_launch_checkpoint.png', similarity=0.6) 
        # Step 2
        self._setFDFRStatus()
        # Step 3
        self._takepicture()


    # Test case 3
    def testCapturePictureWithPictureSize(self):
        """
        Summary:testCapturePictureWithPictureSizeStandard: Take a picture with picture size is standard
        Steps:  1,Launch HDR capture activity
                2.Set photo size
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png', similarity=0.6) 
        # Step 2
	picturesize = random.choice( ['StandardScreen', 'WideScreen'] )
        self._setPictureSizeStatus(picturesize)
        #Step 3
        self._takepicture()
	time.sleep(2)
	self._setPictureSizeStatus('WideScreen')
	

    # Test case 5
    def testCapturepictureWithGeoLocation(self):
        """
        Summary:testCapturepictureWithGeoLocationOn:Take a picture with  geolocation is on
        Steps:  1,Launch HDR capture activity
                2.Set photo Geo-tag
                3.Touch shutter button to capture picture
                4.Exit  activity
        """ 
        self.expect('1_launch_checkpoint.png', similarity=0.6) 
        #Step 2
	location = random.choice( ['on', 'off'] )
        self._setGeoLocationStatus(location)
        #Step 3
        self._takepicture()  


    # Test case 7
    def testCapturePictureWithSelfTimer(self):
        """
        Summary:testCapturePictureWithSelfTimerOff: Capture image with Self-timer off
        Steps:  1.Launch HDR capture activity
                2.Set Self-timer
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png', similarity=0.6) 
        #Step 2
	selftimer = random.choice( ['0', '3','5','10'] )
        self._setSelftTimerstatus(selftimer)
        #Step 3
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            beforeNo = '0'
        #Get the number of photo in sdcard
        else:
            beforeNo = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
            self.sleep(3)
        self.touch(Camera,waittime=5)
	time.sleep(12)
        afterNo = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        if string.atoi(beforeNo) != string.atoi(afterNo) - 1:
            self.fail('take picture fail!')
        self._setSelftTimerstatus('0')



    def _takepicture(self):
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            beforeNo = '0'
        #Get the number of photo in sdcard
        else:
            beforeNo = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
            self.sleep(3)
        self.touch(Camera,waittime=5)
        afterNo = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        if string.atoi(beforeNo) != string.atoi(afterNo) - 1:
            self.fail('take picture fail!')

    def _setFDFRStatus(self):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        a = random.choice(['on','off'])
        if a == 'on':
            state = self.adbCmd(FDFR_STATE)
            if state !='':
                statevalue = state.find('on')
                if statevalue == -1:
                    self.touch(FDFR)
                    state = self.adbCmd(FDFR_STATE)
                    statevalue = state.find('on')
                    if statevalue == -1:
                        self.fail('set camera FD/FR on fail !')
        elif a =='off':
            state = self.adbCmd(FDFR_STATE)
            statevalue = state.find('off')
            if statevalue == -1:
                self.touch(FDFR)
                state = self.adbCmd(FDFR_STATE)
                statevalue = state.find('off')
                if statevalue == -1:
                    self.fail('set camera FD/FR off fail !') 



    def _setPictureSizeStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(Picturesize)
        if status =='WideScreen':
            self.touch((60,294))
        elif status =='StandardScreen':
            self.touch((172,292))
        state = self.adbCmd(PictureSize_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera picture size to'+ status+ 'fail!')

    def _setGeoLocationStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(Geolocation)
        if status =='on':
            self.touch((170,292))
        elif status =='off':
            self.touch((56,286))
        state = self.adbCmd(Geolocation_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera geoloaction'+status+'fail!')

    def _setSelftTimerstatus(self,status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)
        self.touch(Self_Timer)
        if status == '10':
            self.touch((395,288))
        elif status == '5':
            self.touch((288,294))
        elif status == '3':
            self.touch((176,294))
        elif status == '0':
            self.touch((58,294))
	time.sleep(3)
        state = self.adbCmd(SelfTimer_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera self-timer status'+ status + 'fail!')
    	


    def _launchHdr(self):
        self.launch(self.runComponent)
        if self.exists('location.png'):
            self.touch('ok.png')
        self.touch((655,1110))
	time.sleep(3)
        self.touch((650,780))
	time.sleep(7)

    def tearDown(self):
        self.adbCmd('rm -r '+ PICTURE_PATH + '/*')
        self.press('back,back,back,home')
        super(CameraTest,self).tearDown()
