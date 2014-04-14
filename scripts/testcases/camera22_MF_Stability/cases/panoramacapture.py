#!/usr/bin/env python
import unittest
import string
import os
import commands
import time
import random

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
PICTURE_PATH = '' + os.sep + 'mnt'+os.sep+ DCIM_PATH+ '/' +CAMERA_FOLDER
Camera=(366,1100)
Flash=(660,48)
Setting=(60,62)
Exposure=(170,180)
Geolocation=(50,168)
ISO_setting=(300,175)
Self_Timer=(679,163)



class PanoramaTest(unittest.TestCase):

    def setUp(self):
        super(PanoramaTest, self).setUp()
        #Set the name and component to start activity
        self.runComponent= PACKAGE_NAME + '/' + ACTIVITY_NAME
        # Runs the component
        self._launchpanorama()


    def testCaptureWithExposure(self):
        """
        Summary:testCaptureWithExposurePlusOne:capture Panorama picture with Exposure +1
        Steps  : 1.Launch Panorama activity
                 2.Touch Exposure Setting icon, set Exposure +1
                 3.Touch shutter button to capture picture
                 4.Exit  activity 
        """
        #step 1
        self.expect('1_launch_checkpoint.png', similarity=0.6) 
        #step 2
	exposure = random.choice( ['3', '6', '0','-3','-6'] )
        self._setExposureStatus(exposure)
        #step 3
        self._takePanoramaPicture()




    def testCapturepictureWithGeoLocation(self):
        """
        Summary:testCapturepictureWithGeoLocationOff: capture Panorama picture in geolocation off mode
        Steps:  1.Launch Panorama activity
                2.Check geo-tag ,set to Off
                3.Touch shutter button to capture picture
                4.Exit activity
        """ 
        self.expect('1_launch_checkpoint.png', similarity=0.6)  
        #Step 2
	location = random.choice( ['on', 'off'] )
        self._setGeoLocationStatus(location)
        #Step 3
        self._takePanoramaPicture()


    def testCapturepictureWithISOSetting(self):
        """
        Summary:testCapturepictureWithISOSettingAuto: Capture image with ISO Setting Auto
        Steps:  1.Launch Panorama activity
                2.Touch Geo-tag setting  icon,Set Geo-tag OFF
                3.Touch shutter button
                4.Touch shutter button to capture picture
		5.Exit  activity 
        """
	self.expect('1_launch_checkpoint.png', similarity=0.6)  
        #Step 2
        self._setGeoLocationStatus('off')
	time.sleep(1)
	iso = random.choice( ['iso-auto', 'iso-100','iso-200','iso-400','iso-800'] )
	self._setISOsettingstatus(iso)
        #Step 3
        self._takePanoramaPicture()
	
        


    def _takePanoramaPicture(self):
        #Get the number of photo in sdcard
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            beforeNo = '0'
        #Get the number of photo in sdcard
        else:
            beforeNo = commands.getoutput('adb shell ls /mnt/sdcard/DCIM/*  | grep PAN | wc -l')
        self.touch(Camera,waittime=5)
        self.touch(Camera,waittime=5)
        afterNo = commands.getoutput('adb shell ls /mnt/sdcard/DCIM/*  | grep PAN | wc -l')
	time.sleep(1)
        if string.atoi(beforeNo) != string.atoi(afterNo) - 1:
            self.fail('take picture fail!')


    def _setExposureStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        # Enter exposuer setting
	time.sleep(1)
        self.touch(Setting)
        self.touch(Exposure)
        if status =='0':
            self.touch((288,296))
        elif status =='3':
            self.touch((400,292))
        elif status =='6':
            self.touch((520,288))
        elif status =='-3':
            self.touch((170,290))
        elif status =='-6':
            self.touch((50,288))
        state = self.adbCmd(Exposure_STATE)
	time.sleep(1)
        statevalue = state.find(status)
	time.sleep(1)
        if statevalue == -1:
            self.fail('set camera exposure'+status+'fail!')

    def _setGeoLocationStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(Geolocation)
        if status =='on':
            self.touch((150,288))
        elif status =='off':
            self.touch((60,286))
        state = self.adbCmd(Geolocation_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera geoloaction'+status+'fail!')

    def _launchpanorama(self):
        self.launch(self.runComponent)
        if self.exists('location.png'):
            self.touch('ok.png')
        self.touch((650,1090))
	time.sleep(2)
        self.touch((80,1084)) 

    def _setISOsettingstatus(self, status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)
	commands.getoutput('adb shell input swipe 670 165 78 165')
        self.touch(ISO_setting)
        if status == 'iso-auto':
            self.touch((518,288))
        elif status == 'iso-100':
            self.touch((411,294))
        elif status == 'iso-200':
            self.touch((293,294))
        elif status == 'iso-400':
            self.touch((187,294))
        elif status == 'iso-800':
            self.touch((64,294))
	time.sleep(3)
        state = self.adbCmd(ISO_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera iso status'+ status + 'fail!')

    def tearDown(self):
        self.adbCmd('rm -r '+ PICTURE_PATH + '/*')
        self.press('back,back,back,home')
        super(PanoramaTest,self).tearDown()
