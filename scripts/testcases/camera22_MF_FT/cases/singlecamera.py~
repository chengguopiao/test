#!/usr/bin/env python
import unittest
import string
import os
import commands
import time

"""
@author:Cao Lina
@Note:Feature test for intel camera2.2
"""
PACKAGE_NAME = 'com.intel.camera22'
ACTIVITY_NAME = PACKAGE_NAME + '.Camera'
DCIM_PATH = '/sdcard/DCIM'
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
CAMERA_ID_FRONT = '1'
CAMERA_ID_BACK = '0'
PICTURE_PATH = '' + os.sep + 'mnt'+os.sep+ DCIM_PATH+'/'+CAMERA_FOLDER
CAMERAKEY=(369,1164)
Setting = (61,60)
Flash = (256,60)
Exposure = (645,190)
Scences =(513,190)
FDFR = (474,60)
FrontFDFR = (475,75)
PictureSize = (398,176)
Geolocation = (280,178)
FrontGeolocation =(57,168)
Hint =(155,170)
SwitchFrontbackCamera =(657,60)
TestCamera =(66,177)
WhiteBalance=(432,173)
ISO_setting=(551,163)
Self_Timer=(679,163)

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        self.launch(self.runComponent)
        if self.exists('location.png'):
            self.touch('ok.png')

    # Test case 1
    def testCapturePictureWithFlashOn(self):
        """
        Summary:testCapturePictureWithFlashOn: Take a picture with flash on
        Steps:  1.Launch single capture activity
                2.Set flash ON
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        state = self.adbCmd(Scene_STATE)
        statevalue = state.find('auto')
	if statevalue == -1:
            self._setScenesStatus('auto')
        self._setFlashStatus('on')
        # Step 3
        self._takePicture()

    # Test case 2
    def testCapturePictureWithFlashOff(self):
        """
        Summary:testCapturePictureWithFlashOff: Take a picture with flash off
        Steps:  1.Launch single capture activity
                2.Set flash Off
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        state = self.adbCmd(Scene_STATE)
        statevalue = state.find('auto')
	if statevalue == -1:
            self._setScenesStatus('auto')
        self._setFlashStatus('off')
        # Step 3
        self._takePicture()

    # Test case 3
    def testCapturePictureWithFlashAuto(self):
        """
        Summary:testCapturePictureWithFlashAuto: Take a picture with flash auto
        Steps:  1.Launch single capture activity
                2.Set flash auto
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        state = self.adbCmd(Scene_STATE)
        statevalue = state.find('auto')
	if statevalue == -1:
            self._setScenesStatus('auto')
        self._setFlashStatus('auto')
        # Step 3
        self._takePicture()

    # Test case 4
    def testCaptureWithExposurePlusOne(self):
        """
        Summary:testCaptureWithExposurePlusOne: Take a picture with Exposure +1
        Steps: 1.Launch single capture activity
               2.Set exposure +1
               3.Touch shutter button to capture picture
               4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')          
        #Step 2
        self._setExposureStatus('3')
        #Step 3
        self._takePicture()

    # Test case 5
    def testCaptureWithExposurePlusTwo(self):
        """
        Summary:testCaptureWithExposurePlusTwo: Take a picture with Exposure +2
        Steps: 1.Launch single capture activity
               2.Set exposure +2
               3.Touch shutter button to capture picture
               4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')          
        #Step 2
        self._setExposureStatus('6')
        #Step 3
        self._takePicture()


    # Test case 6
    def testCaptureWithExposureRedOne(self):
        """
        Summary:testCaptureWithExposureRedOne: Take a picture with Exposure -1
        Steps: 1.Launch single capture activity
               2.Set exposure -1
               3.Touch shutter button to capture picture
               4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')          
        #Step 2
        self._setExposureStatus('-3')
        #Step 3
        self._takePicture()


    # Test case 7
    def testCaptureWithExposureRedTwo(self):
        """
        Summary:testCaptureWithExposureRedOne: Take a picture with Exposure -2
        Steps: 1.Launch single capture activity
               2.Set exposure -2
               3.Touch shutter button to capture picture
               4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')          
        #Step 2
        self._setExposureStatus('-6')
        #Step 3
        self._takePicture()


    # Test case 8
    def testCaptureWithExposureZero(self):
        """
        Summary:testCaptureWithExposureZero: Take a picture with Exposure 0
        Steps: 1.Launch single capture activity
               2.Set exposure 0
               3.Touch shutter button to capture picture
               4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')          
        #Step 2
        self._setExposureStatus('0')
        #Step 3
        self._takePicture()

    # Test case 9
    def testCapturePictureWithScenesSport(self):
        """
        Summary:testCapturePictureWithScenesSport: Take a picture with set scenes to Sports
        Steps:  1.Launch single capture activity
                2.Set scene mode Sports
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setScenesStatus('sports')
        #Step 3
        self._takePicture()
        self._setScenesStatus('auto')
   
    # Test case 10
    def testCapturePictureWithScenesNight(self):
        """
        Summary:testCapturePictureWithScenesNight: Take a picture with set scenes to Night
        Steps:  1.Launch single capture activity
                2.Set scene mode Night
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setScenesStatus('night')
        #Step 3
        self._takePicture()
        self._setScenesStatus('auto')

    # Test case 11
    def testCapturePictureWithScenesLandscape(self):
        """
        Summary:testCapturePictureWithScenesLandscape: Take a picture with set scenes to Landscape
        Steps:  1.Launch single capture activity
                2.Set scene mode Landscape
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2 
        self._setScenesStatus('landscape')
        #Step 3
        self._takePicture()
        self._setScenesStatus('auto')

    # Test case 12
    def testCapturePictureWithScenesPortrait(self):
        """
        Summary:testCapturePictureWithScenesPortrait: Take a picture with set scenes to Portrait
        Steps:  1.Launch single capture activity
                2.Set scene mode Portrait
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setScenesStatus('portrait')
        #Step 3
        self._takePicture()
        self._setScenesStatus('auto')

    # Test case 13
    def testCapturePictureWithScenesAuto(self):
        """
        Summary:testCapturePictureWithScenesAuto: Take a picture with set scenes to Auto
        Steps:  1.Launch single capture activity
                2.Set scene mode Auto
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setScenesStatus('auto')
        #Step 3
        self._takePicture()


    # Test case 14
    def testCapturePictureWithFDON(self):
        """
        Summary:testCapturePictureWithFDON: Take a picture with set FD/FR on
        Steps:  1.Launch single capture activity
                2.Set FD/FR ON
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        state = self.adbCmd(Scene_STATE)
        statevalue = state.find('auto')
	if statevalue == -1:
            self._setScenesStatus('auto')
        self._setFDFROn()
        #Step 3
        self._takePicture()


    # Test case 15
    def testCapturePictureWithFDOff(self):
        """
        Summary:testCapturePictureWithFDOff: Take a picture with set FD/FR off
        Steps:  1.Launch single capture activity
                2.Set FD/FR Off
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        state = self.adbCmd(Scene_STATE)
        statevalue = state.find('auto')
	if statevalue == -1:
            self._setScenesStatus('auto')
        self._setFDFROff()
        #Step 3
        self._takePicture()

    # Test case 16
    def testCapturePictureWithPictureSizeStandard(self):
        """
        Summary:testCapturePictureWithPictureSizeStandard: Take a picture with picture size is standard
        Steps:  1.Launch single capture activity
                2.Set picture size is standard
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setPictureSizeStatus('StandardScreen')
        #Step 3
        self._takePicture()
	time.sleep(2)
	self._setPictureSizeStatus('WideScreen')

    # Test case 17
    def testCaptureWithPictureSizeWidesreen(self):
        """
        Summary:testCaptureWithSize6M: Take a picture with  picture size is Widesreen
        Steps:  1.Launch single capture activity
                2.Set picture size is Widesreen
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setPictureSizeStatus('WideScreen')
        #Step 3
        self._takePicture()

    # Test case 18
    def testCapturepictureWithGeoLocationOn(self):
        """
        Summary:testCapturepictureWithGeoLocationOn:Take a picture with  geolocation is on
        Steps:  1.Launch camera app
                2.Set geo location on 
                3.Touch shutter button to capture picture
                4.Exit  activity
        """ 
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setGeoLocationStatus('on')
        #Step 3
        self._takePicture() 

    # Test case 19
    def testCapturepictureWithGeoLocationOff(self):
        """
        Summary:testCapturepictureWithGeoLocationOff: Take a picture with  geolocation is off
        Steps:  1.Launch camera app
                2.Set geo location off 
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setGeoLocationStatus('off')
        #Step 3
        self._takePicture()


    # Test case 20
    def testCapturepictureWithHintsOn(self):
        """
        Summary:testCapturepictureWithHintsOn: Take a picture with  hints is on
        Steps:  1.Launch camera app
                2.Set hints on
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setHintsStatus('on')
        #Step 3
        self._takePicture()

    # Test case 21
    def testCapturepictureWithHintsOff(self):
        """
        Summary:testCapturepictureWithHintsOff: Take a picture with  hints is off
        Steps:  1.Launch camera app
                2.Set hints off
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        #self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setHintsStatus('off')
        #Step 3
        self._takePicture()

    # Test case 22
    def testRearFaceCapturePictureWithFDON(self):
        """
        Summary:testRearFaceCapturePictureWithFDON: Take a picture using fear face camera and set FD/FR on
        Steps:  1.Launch single capture activity
                2.Set FD/FR ON
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        #self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setFrontFDFROn()
        #Step 3
        self._takePicture()

    # Test case 23
    def testRearFaceCapturePictureWithFDOff(self):
        """
        Summary:testRearFaceCapturePictureWithFDOff: Take a picture using fear face camera and set FD/FR off
        Steps:  1.Launch single capture activity
                2.Set FD/FR Off
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        #self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setFrontFDFROff()
        #Step 3
        self._takePicture()

    # Test case 24
    def testRearFaceCapturepictureWithGeoLocationOn(self):
        """
        Summary:testRearFaceCapturepictureWithGeoLocationOn: Take a picture using fear face camera and set geolocation on 
        Steps:  1.Launch camera app
                2.Set geolocation on 
                3.Touch shutter button to capture picture
                4.Exit  activity
        """ 
        self._identifyCameraBack()
        #self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setGeoLocationStatus('on')
        #Step 3
	if self.exists('1_location.png'):
	    time.sleep(1)
	    self.touch('cancel.png')
	time.sleep(1)
        self._takePicture()


    # Test case 25
    def testRearFaceCapturepictureWithGeoLocationOff(self):
        """
        Summary:testRearFaceCapturepictureWithGeoLocationOff: Take a picture using fear face camera and set geolocation off
        Steps:  1.Launch camera app
                2.Set geo location off 
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        #self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setGeoLocationStatus('off')
        #Step 3
        self._takePicture()

    # Test case 26
    def testCapturePictureWithScenesNightportrait(self):
        """
        Summary:testCapturePictureWithScenesNightportrait: Capture image with Scene mode Night-portrait
        Steps:  1.Launch single capture activity
                2.Set scene mode night-portrait
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setScenesStatus('night-portrait')
        #Step 3
        self._takePicture()
        self._setScenesStatus('auto')

    # Test case 27
    def testCapturePictureWithScenesBarcode(self):
        """
        Summary:testCapturePictureWithScenesBarcode: Capture image with Scene mode barcode
        Steps:  1.Launch single capture activity
                2.Set scene mode barcode
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setScenesStatus('barcode')
        #Step 3
        self._takePicture()
        self._setScenesStatus('auto')


    # Test case 28
    def testCapturePictureWithScenesFireworks(self):
        """
        Summary:testCapturePictureWithScenesFireworks: Capture image with Scene mode fireworks
        Steps:  1.Launch single capture activity
                2.Set scene mode fireworks
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setScenesStatus('fireworks')
        #Step 3
        self._takePicture()
        self._setScenesStatus('auto')



    # Test case 29
    def testCapturepictureWithSelfTimerOff(self):
        """
        Summary:testCapturepictureWithSelfTimerOff: Capture image with Self-timer off
        Steps:  1.Launch single capture activity
                2.Set Self-timer off
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setSelftTimerstatus('0')
        #Step 3
        self._takePicture()


    # Test case 30
    def testCapturepictureWithSelfTimerThreeSec(self):
        """
        Summary:testCapturepictureWithSelfTimerThreeSec: Capture image with Self-timer 3s
        Steps:  1.Launch single capture activity
                2.Set Self-timer 3s
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setSelftTimerstatus('3')
        #Step 3
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            before = '0'
        #Get the number of photo in sdcard
        else:
            before = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
            self.sleep(3)
        self.touch(CAMERAKEY,waittime=3)
	time.sleep(5)
        after = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        self.sleep(3)
        if string.atoi(before) == string.atoi(after) - 1 or string.atoi(before) == string.atoi(after) - 2:
            self.logger.debug('take picture success!')
        else:
            self.fail('take picture fail!')
        self._setSelftTimerstatus('0')


    # Test case 31
    def testCapturepictureWithSelfTimerFiveSec(self):
        """
        Summary:testCapturepictureWithSelfTimerFiveSec: Capture image with Self-timer 5s
        Steps:  1.Launch single capture activity
                2.Set Self-timer 5s
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setSelftTimerstatus('5')
        #Step 3
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            before = '0'
        #Get the number of photo in sdcard
        else:
            before = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
            self.sleep(3)
        self.touch(CAMERAKEY,waittime=3)
	time.sleep(7)
        after = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        self.sleep(3)
        if string.atoi(before) == string.atoi(after) - 1 or string.atoi(before) == string.atoi(after) - 2:
            self.logger.debug('take picture success!')
        else:
            self.fail('take picture fail!')
        self._setSelftTimerstatus('0')


    # Test case 32
    def testCapturepictureWithSelfTimerTenSec(self):
        """
        Summary:testCapturepictureWithSelfTimerTenSec: Capture image with Self-timer 10s
        Steps:  1.Launch single capture activity
                2.Set Self-timer 10s
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setSelftTimerstatus('10')
        #Step 3
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            before = '0'
        #Get the number of photo in sdcard
        else:
            before = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
            self.sleep(3)
        self.touch(CAMERAKEY,waittime=3)
	time.sleep(12)
        after = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        self.sleep(3)
        if string.atoi(before) == string.atoi(after) - 1 or string.atoi(before) == string.atoi(after) - 2:
            self.logger.debug('take picture success!')
        else:
            self.fail('take picture fail!')
        self._setSelftTimerstatus('0')



    # Test case 33
    def testCapturepictureWithISOAuto(self):
        """
        Summary:testCapturepictureWithISOAuto: Capture image with ISO Setting Auto
        Steps:  1.Launch single capture activity
                2.Set ISO Setting Auto
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setISOsettingstatus('iso-auto')
        #Step 3
        self._takePicture()


    # Test case 34
    def testCapturepictureWithISOHundred(self):
        """
        Summary:testCapturepictureWithISOHundred: Capture image with ISO Setting 100
        Steps:  1.Launch single capture activity
                2.Set ISO Setting 100
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setISOsettingstatus('iso-100')
        #Step 3
        self._takePicture()


    # Test case 35
    def testCapturepictureWithISOTwoHundred(self):
        """
        Summary:testCapturepictureWithISOTwoHundred: Capture image with ISO Setting 200
        Steps:  1.Launch single capture activity
                2.Set ISO Setting 200
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setISOsettingstatus('iso-200')
        #Step 3
        self._takePicture()

    # Test case 36
    def testCapturepictureWithISOFourHundred(self):
        """
        Summary:testCapturepictureWithISOFourHundred: Capture image with ISO Setting 400
        Steps:  1.Launch single capture activity
                2.Set ISO Setting 400
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setISOsettingstatus('iso-400')
        #Step 3
        self._takePicture()

    # Test case 37
    def testCapturepictureWithISOEightHundred(self):
        """
        Summary:testCapturepictureWithISOEightHundred: Capture image with ISO Setting 800
        Steps:  1.Launch single capture activity
                2.Set ISO Setting 800
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setISOsettingstatus('iso-800')
        #Step 3
        self._takePicture()

    # Test case 38
    def testCapturepictureWithWhiteBalanceAuto(self):
        """
        Summary:testCapturepictureWithWhiteBalanceAuto: Capture image with White Balance Auto
        Steps:  1.Launch single capture activity
                2.Set White Balance Auto
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setWBstatus('auto')
        #Step 3
        self._takePicture()

    # Test case 39
    def testCapturepictureWithWhiteBalanceIncandescent(self):
        """
        Summary:testCapturepictureWithWhiteBalanceIncandescent: Capture image with White Balance Incandescent
        Steps:  1.Launch single capture activity
                2.Set White Balance Incandescent
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setWBstatus('incandescent')
        #Step 3
        self._takePicture()

    # Test case 40
    def testCapturepictureWithWhiteBalanceDaylight(self):
        """
        Summary:testCapturepictureWithWhiteBalanceDaylight: Capture image with White Balance Daylight
        Steps:  1.Launch single capture activity
                2.Set White Balance Daylight
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setWBstatus('daylight')
        #Step 3
        self._takePicture()

    # Test case 41
    def testCapturepictureWithWhiteBalanceFluorescent(self):
        """
        Summary:testCapturepictureWithWhiteBalanceFluorescent: Capture image with White Balance Fluorescent
        Steps:  1.Launch single capture activity
                2.Set White Balance Fluorescent
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setWBstatus('fluorescent')
        #Step 3
        self._takePicture()

    # Test case 42
    def testCapturepictureWithWhiteBalanceCloudy(self):
        """
        Summary:testCapturepictureWithWhiteBalanceCloudy: Capture image with White Balance Cloudy
        Steps:  1.Launch single capture activity
                2.Set White Balance Cloudy
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        # Step 2
        self._setWBstatus('cloudy-daylight')
        #Step 3
        self._takePicture()



    # Test case 43    
    def testSwitchToCamera(self):
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting,waittime=3)\
        .touch(TestCamera)\
        .expect('2_testcamera_checkpoint.png')

    def _takePicture(self):
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            before = '0'
        #Get the number of photo in sdcard
        else:
            before = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep jpg | wc -l')
            self.sleep(3)
        self.touch(CAMERAKEY,waittime=3)
	time.sleep(3)
        after = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep jpg | wc -l')
        self.sleep(3)
        if string.atoi(before) == string.atoi(after) - 1 or string.atoi(before) == string.atoi(after) - 2:
            self.logger.debug('take picture success!')
        else:
            self.fail('take picture fail!')

    def _setFlashStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        # Touch flash setting
        self.touch(Flash)
        if status == 'on':
            self.touch((176,176))
        elif status == 'off':
            self.touch((59,178))
        else:
            self.touch((296,176))
        state = self.adbCmd(Flash_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera flash status to' + status + 'fail!') 

    def _setExposureStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        # Enter exposuer setting
        self.touch(Setting)
        #.drag(start=(620,178),end=(366,214),time=4,steps=6)\
        self.touch(Exposure)
        if status == '0':
            self.touch((285,294))
        elif status == '3':
            self.touch((400,300))
        elif status == '6':
            self.touch((520,290))
        elif status == '-3':
            self.touch((170,290))
        elif status == '-6':
            self.touch((60,288))
        state = self.adbCmd(Exposure_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera exposure status' +status+ 'fail!')

    def _setScenesStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(Scences)
        if status == 'sports':
	    #commands.getoutput('adb shell input swipe 648 288 59 288')
            self.touch((640,294))
        elif status == 'night':
            self.touch((520,294))
        elif status == 'landscape':
            self.touch((400,294))
        elif status == 'portrait':
            self.touch((300,294))
        elif status == 'night-portrait':
            self.touch((170,294))
        elif status == 'barcode':
            self.touch((60,294))
        #elif status == 'fireworks':
            #self.touch((50,294))
        elif status == 'auto':
	    commands.getoutput('adb shell input swipe 648 288 59 288')
            self.touch((640,294))
	time.sleep(3)
        state = self.adbCmd(Scene_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera scenes status'+ status + 'fail!')

    def _setPictureSizeStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(PictureSize)
        if status == 'WideScreen':
            self.touch((60,292))
        elif status == 'StandardScreen':
            self.touch((180,292))
        state = self.adbCmd(PictureSize_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera picture size to' + status +'fail!')

    def _setGeoLocationStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(Geolocation)
        if status == 'on':
            self.touch((170,284))
        elif status == 'off':
            self.touch((60,276))
	time.sleep(2)
        state = self.adbCmd(Geolocation_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera geoloaction to' + status + 'fail!')

    def _setFrontGeoLocationStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(FrontGeolocation)
        if status == 'on':
            self.touch((170,288))
        elif status =='off':
            self.touch((50,286)) 
        state = self.adbCmd(Geolocation_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera geoloaction' +status+ 'fail!')

    def _setHintsStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(Hint)
        if status =='on':
            self.touch((172,298))
        elif status == 'off':
            self.touch((60,292))
        state = self.adbCmd(Hints_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera Hints' +status+ 'fail!')

    def _setFDFROn(self):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        state = self.adbCmd(FDFR_STATE)
        if state !='':
            statevalue = state.find('on')
            if statevalue == -1:
                self.touch(FDFR)
                state = self.adbCmd(FDFR_STATE)
                statevalue = state.find('on')
                if statevalue == -1:
                    self.fail('set camera FD/FR on fail !')

    def _setFDFROff(self):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        state = self.adbCmd(FDFR_STATE)
        statevalue = state.find('off')
        if statevalue == -1:
            self.touch(FDFR)
            state = self.adbCmd(FDFR_STATE)
            statevalue = state.find('off')
            if statevalue == -1:
                self.fail('set camera FD/FR off fail !')

    def _setFrontFDFROn(self):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        state = self.adbCmd(FDFR_STATE)
        if state !='':
            statevalue = state.find('on')
            if statevalue == -1:
                self.touch(FrontFDFR)
                state = self.adbCmd(FDFR_STATE)
                statevalue = state.find('on')
                if statevalue == -1:
                    self.fail('set camera FD/FR on fail !')

    def _setFrontFDFROff(self):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        state = self.adbCmd(FDFR_STATE)
        statevalue = state.find('off')
        if statevalue == -1:
            self.touch(FrontFDFR)
            state = self.adbCmd(FDFR_STATE)
            statevalue = state.find('off')
            if statevalue == -1:
                self.fail('set camera FD/FR off fail !')

    def _identifyCameraFront(self):
        #Check camera already set to front camera
        cameidvalue = self.adbCmd(CAMERA_ID)
        self.logger.debug("Camera ID value is: " + cameidvalue)
        if cameidvalue !='':
            mCameraIDValue = cameidvalue.find(CAMERA_ID_FRONT)
            if mCameraIDValue == -1:
                commands.getoutput('adb shell input swipe 530 6 523 22')
                self.touch(SwitchFrontbackCamera,waittime=3)
                self.failIf(self.adbCmd(CAMERA_ID).find(CAMERA_ID_FRONT) == -1,"Switch the camera to front failed...")
            else:
                self.logger.debug("Current camera is front...")
        else:
            self.logger.debug("Switch the camera to front...")
            commands.getoutput('adb shell input swipe 530 6 523 22')
            self.touch(SwitchFrontbackCamera,waittime=3)
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
                self.touch(SwitchFrontbackCamera,waittime=3)
                self.failIf(self.adbCmd(CAMERA_ID).find(CAMERA_ID_BACK) == -1,"Switch the camera to rear failed...")
            else:
                self.logger.debug("Current camera is rear...")
        else:
            self.logger.debug("Current camera is rear...")

    def _setWBstatus(self,status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)
	commands.getoutput('adb shell input swipe 670 165 78 165')
        self.touch(WhiteBalance)
        if status == 'auto':
            self.touch((518,288))
        elif status == 'incandescent':
            self.touch((411,294))
        elif status == 'daylight':
            self.touch((293,294))
        elif status == 'fluorescent':
            self.touch((187,294))
        elif status == 'cloudy-daylight':
            self.touch((64,294))
	time.sleep(3)
        state = self.adbCmd(WhiteBalance_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera WhitBalance status'+ status + 'fail!')

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
    
    def _setSelftTimerstatus(self,status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)
	commands.getoutput('adb shell input swipe 670 165 78 165')
        self.touch(Self_Timer)
        if status == '10':
            self.touch((414,288))
        elif status == '5':
            self.touch((295,294))
        elif status == '3':
            self.touch((181,294))
        elif status == '0':
            self.touch((54,294))
	time.sleep(3)
        state = self.adbCmd(SelfTimer_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera self-timer status'+ status + 'fail!')
    	
	

	

    def tearDown(self):
        self.adbCmd('rm -r '+ PICTURE_PATH + '/*')
        self.press('back,back,back,home')
        super(CameraTest,self).tearDown()
