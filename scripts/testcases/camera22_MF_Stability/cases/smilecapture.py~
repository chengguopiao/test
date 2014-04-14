#!/usr/bin/env python
import unittest
import string
import os
import commands
import time
import random

"""
@author:Cao Lina
@Note:Feature test for intel camera2.2
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
CAMERA_ID_FRONT = '1'
CAMERA_ID_BACK = '0'
PICTURE_PATH = '' + os.sep + 'mnt'+os.sep+ DCIM_PATH +'/'+ CAMERA_FOLDER
CAMERAKEY=(364,1100)
Flash =(660,75)
Setting =(60,62)
Exposure =(400,174)
Scences=(290,176)
Picturesize=(178,176)
Geolocation=(58,168)
SwitchCamera=(660,46)
ISO=(630,170)
WhiteBalance=(516,183)

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        self._launchSmail()

    # Test case 1
    def testCapturePictureWithFlash(self):
        """
        Summary:testCapturePictureWithFlashOn: Take a picture with flash on
        Steps: 1.Launch SmileCam activity
               2.Check flash state
               3.Touch shutter button to capture picture
               4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png', similarity=0.6) 
        # Step 2
	flash = random.choice( ['auto', 'off', 'on'] )
        self._setFlashStatus(flash)
        # Step 3
        self._takePictures()


    # Test case 4
    def testCaptureWithExposure(self):
        """
        Summary:testCaptureWithExposurePlusOne: Take a picture with Exposure +1
        Steps: 1.Launch SmileCam activity
               2.Check exposure setting icon ,set to 1
               3.Touch shutter button to capture picture
               4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png', similarity=0.6)           
        #Step 2
	exposure = random.choice( ['3', '6', '0','-3','-6'] )
        self._setExposureStatus(exposure)
        #Step 3
        self._takePictures()


    # Test case 9
    def testCapturePictureWithScenes(self):
        """
        Summary:testCapturePictureWithScenesSport: Take a picture with set scenes to Sports
        Steps:  1.Launch SmileCam activity
                2.Check scence mode
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png', similarity=0.6) 
        #Step 2
	scence = random.choice( ['sports', 'night', 'landscape','portrait','auto','night-portrait','barcode'] )
        self._setScenesStatus('sports')
        #Step 3
        self._takePictures()
        self._setScenesStatus('auto')
   

    # Test case 14
    def testCapturePictureWithPictureSize(self):
        """
        Summary:testCapturePictureWithPictureSizeStandard: Take a picture with picture size is standard
        Steps:  1.Launch SmileCam activity
                2.Check photo size
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png', similarity=0.6) 
        # Step 2
	picturesize = random.choice( ['StandardScreen', 'WideScreen'] )
        self._setPictureSizeStatus(picturesize)
        #Step 3
        self._takePictures()



    # Test case 16
    def testCapturepictureWithGeoLocation(self):
        """
        Summary:testCapturepictureWithGeoLocationOn:Take a picture with  geolocation is on
        Steps:  1.Launch SmileCam activity
                2.Check geo-tag 
                3.Touch shutter button to capture picture
                4.Exit  activity
        """ 
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png', similarity=0.6) 
        #Step 2
	location = random.choice( ['on', 'off'] )
        self._setGeoLocationStatus(location)
        #Step 3
        self._takePictures()  



    # Test case 18
    def testRearFaceCapturepictureWithGeoLocation(self):
        """
        Summary:testRearFaceCapturepictureWithGeoLocationOn: Take a picture using fear face camera and set geolocation on 
        Steps:  1.Launch SmileCam activity
                2.Set to front face camera
                3.Check geo-tag ,set to ON
                4.Touch shutter button to capture 30s video
                5.Exit  activity
        """ 
        #Step 2
        self._identifyCameraFront()
        #self.expect('1_launch_checkpoint.png', similarity=0.6) 
        #Step 3
	location = random.choice( ['on', 'off'] )
        self._setGeoLocationStatus(location)
        #Step 4
        self._takePictures()
	time.sleep(1)
	self._identifyCameraBack()   



    # Test case 23
    def testCapturepictureWithISO(self):
        """
        Summary:testCapturepictureWithISOAuto: Capture image with ISO Setting Auto
        Steps:  1.Launch SmileCam capture activity
                2.Set ISO Setting Auto
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png', similarity=0.6) 
        #Step 2
	iso = random.choice( ['iso-auto', 'iso-100','iso-200','iso-400','iso-800'] )
        self._setISOstatus(iso)
        #Step 3
        self._takePictures()


    # Test case 27
    def testCapturepictureWithWhiteBalance(self):
        """
        Summary:testCapturepictureWithWhiteBalanceAuto: Capture image with White Balance Auto
        Steps:  1.Launch SmileCam capture activity
                2.Set White Balance Auto
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png', similarity=0.6) 
        #Step 2
	wb = random.choice( ['auto', 'incandescent','daylight','fluorescent','cloudy-daylight'] )
        self._setWhiteBalancestatus(wb)
        #Step 3
        self._takePictures()



    def _takePictures(self):
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            beforeNo = '0'
        #Get the number of photo in sdcard
        else:
            beforeNo = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
            self.sleep(3)
        self.touch(CAMERAKEY,waittime=3)
        self.touch(CAMERAKEY,waittime=5)
        afterNo = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        if string.atoi(beforeNo) != string.atoi(afterNo) - 1:
            self.fail('take picture fail!')

    def _setFlashStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        # Touch flash setting
        self.touch(Flash)
        if status =='on':
            self.touch((170,176),waittime=3)
        elif status =='off':
            self.touch((56,180),waittime=3)
        elif status =='auto':
            self.touch((288,174),waittime=3)
        state = self.adbCmd(Flash_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera flash'+status+ 'fail!')

    def _setExposureStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        # Enter exposuer setting
        self.touch(Setting)\
        .touch(Exposure)
        if status =='0':
            self.touch((270,292))
        elif status =='3':
            self.touch((410,292))
        elif status =='6':
            self.touch((520,290))
        elif status =='-3':
            self.touch((170,290))
        elif status =='-6':
            self.touch((60,290))
        state = self.adbCmd(Exposure_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera exposure'+status+ 'fail!')

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
        .touch(Picturesize)
        if status == 'WideScreen':
            self.touch((56,292))
        elif status =='StandardScreen':
            self.touch((170,294))
        state = self.adbCmd(PictureSize_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera picture size to'+status+ 'fail!')

    def _setGeoLocationStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(Geolocation)
        if status == 'on':
            self.touch((170,286))
        elif status =='off':
            self.touch((56,288))
        state = self.adbCmd(Geolocation_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera geoloaction'+status+ 'fail!')

    def _identifyCameraFront(self):
        #Check camera already set to front camera
        cameidvalue = self.adbCmd(CAMERA_ID)
        self.logger.debug("Camera ID value is: " + cameidvalue)
        if cameidvalue !='':
            mCameraIDValue = cameidvalue.find(CAMERA_ID_FRONT)
            if mCameraIDValue == -1:
                commands.getoutput('adb shell input swipe 530 6 523 22')
                self.touch(SwitchCamera,waittime=5)
                self.failIf(self.adbCmd(CAMERA_ID).find(CAMERA_ID_FRONT) == -1,"Switch the camera to front failed...")
            else:
                self.logger.debug("Current camera is front...")
        else:
            self.logger.debug("Switch the camera to front...")
            commands.getoutput('adb shell input swipe 530 6 523 22')
            self.touch(SwitchCamera,waittime=5)
            self.failIf(self.adbCmd(CAMERA_ID).find(CAMERA_ID_FRONT) == -1,"Switch the camera to front failed...")

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

    def _setISOstatus(self, status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(ISO)
        if status == 'iso-auto':
            self.touch((517,290))
        elif status == 'iso-100':
            self.touch((415,293))
        elif status == 'iso-200':
            self.touch((313,276))
        elif status == 'iso-400':
            self.touch((183,290))
        elif status == 'iso-800':
            self.touch((75,286))
        time.sleep(3)
        state = self.adbCmd(ISO_STATE)
        statevalue = state.find(status)
        if  statevalue == -1:
            self.fail('set camera iso status'+ status + 'fail!')

    def _setWhiteBalancestatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(WhiteBalance)
        if status == 'auto':
            self.touch((520,285))
        elif status == 'incandescent':
            self.touch((414,305))
        elif status == 'daylight':
            self.touch((302,303))
        elif status == 'fluorescent':
            self.touch((179,284))
        elif status == 'cloudy-daylight':
            self.touch((62,302))
        time.sleep(3)
        state = self.adbCmd(WhiteBalance_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera WhitBalance status'+ status + 'fail!')

    def _launchSmail(self):
        self.launch(self.runComponent)
        if self.exists('location.png'):
            self.touch('ok.png')
        self.touch((650,1090),waittime=3)\
        .touch((650,930),waittime=3)

    def tearDown(self):
        self.adbCmd('rm -r '+ PICTURE_PATH + '/*')
        self.press('back,back,back,home')
        super(CameraTest,self).tearDown()
