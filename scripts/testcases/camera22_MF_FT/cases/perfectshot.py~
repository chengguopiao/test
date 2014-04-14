#!/usr/bin/env python
import unittest
import string
import os
import time
import commands


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
Camera =(366,1100)
Setting =(60,62)
Geolocation=(60,172)
Exposure=(280,176)
Scences=(170,180)

class PerfectShotTest(unittest.TestCase):

    def setUp(self):
        super(PerfectShotTest, self).setUp()
        #Set the name and component to start activity
        self.runComponent= PACKAGE_NAME + '/' + ACTIVITY_NAME
        # Runs the component
        self._launchperfectshot()

    def testCapturepictureWithGeoLocationOn(self):
        """
        Summary:testCapturepictureWithGeoLocationOn: capture PerfectShot picture in geolocation on mode
        Steps:  1.Launch perfect shot activity
                2.Check geo-tag ,set to ON
                3.Touch shutter button to capture picture
                4.Exit activity
        """ 
        self.expect('1_launch_checkpoint.png') 
        #Step 2
        self._setGeoLocationStatus('on')
        #Step 3
	time.sleep(2)
	if self.exists('1_location.png'):
	    time.sleep(1)
	    self.touch('cancel.png')
	time.sleep(1)
        self._takePerfectshotPicture()

    def testCapturepictureWithGeoLocationOff(self):
        """
        Summary:testCapturepictureWithGeoLocationOff: capture PerfectShot picture in geolocation off mode
        Steps:  1.Launch perfect shot activity
                2.Check geo-tag ,set to Off
                3.Touch shutter button to capture  picture
                4.Exit activity
        """ 
        self.expect('1_launch_checkpoint.png') 
        #Step 2
        self._setGeoLocationStatus('off')
        #Step 3
        self._takePerfectshotPicture()

    def testCaptureWithExposurePlusOne(self):
        """
        Summary:testCaptureWithExposurePlusOne: Take burst piture with exposure +1
        Steps:  1.Launch perfect shot activity
                2.Check exposure setting icon ,set to +1
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png')           
        #Step 2
        self._setExposureStatus('3')
        #Step 3
        self._takePerfectshotPicture()

    def testCaptureWithExposurePlusTwo(self):
        """
        Summary:testCapturePictureWithExposurePlusOne: Take burst piture with exposure +2
        Steps:  1.Launch perfect shot activity
                2.Check exposure setting icon ,set to +2
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png')           
        #Step 2
        self._setExposureStatus('6')
        #Step 3
        self._takePerfectshotPicture()

    def testCaptureWithExposureRedOne(self):
        """
        Summary:testCaptureWithExposureRedOne: Take burst piture with exposure -1
        Steps:  1.Launch perfect shot activity
                2.Check exposure setting icon ,set to -1
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png')           
        #Step 2
        self._setExposureStatus('-3')
        #Step 3
        self._takePerfectshotPicture()

    def testCaptureWithExposureRedTwo(self):
        """
        Summary:testCaptureWithExposureRedTwo: Take burst piture with exposure -2
        Steps:  1.Launch perfect shot activity
                2.Check exposure setting icon ,set to -2
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png')           
        #Step 2
        self._setExposureStatus('-6')
        #Step 3
        self._takePerfectshotPicture()

    def testCaptureWithExposureZero(self):
        """
        Summary:testCaptureWithExposureZero: Take burst piture with exposure 0
        Steps:  1.Launch perfect shot activity
                2.Check exposure setting icon ,set to 0
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png')           
        #Step 2
        self._setExposureStatus('0')
        #Step 3
        self._takePerfectshotPicture()

    def testCapturePictureWithScenesSport(self):
        """
        Summary:testCapturePictureWithScenesSport: Take picture with set scenes to Sports
        Steps:  1Launch perfect shot activity
                2.Check scence mode ,set mode to Sports
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png') 
        # Step 2
        self._setScenesStatus('sports')
        #Step 3
        self._takePerfectshotPicture()

    def testCapturePictureWithScenesNight(self):
        """
        Summary:testCapturePictureWithScenesNight: Take picture with set scenes to night
        Steps:  1.Launch perfect shot activity
                2.Check scence mode ,set mode to night
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png') 
        # Step 2
        self._setScenesStatus('night')
        #Step 3
	time.sleep(3)
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            beforeNo = '0'
        #Get the number of photo in sdcard
        else:
            beforeNo = commands.getoutput('adb shell ls /mnt/sdcard/DCIM/*  | grep BST | wc -l')
        self.touch(Camera,waittime=60)
        afterNo = commands.getoutput('adb shell ls /mnt/sdcard/DCIM/*  | grep BST | wc -l')
	time.sleep(3)
        if string.atoi(beforeNo) != string.atoi(afterNo) - 9:
            self.fail('take picture fail!')

    def testCapturePictureWithScenesLandscape(self):
        """
        Summary:testCapturePictureWithScenesLandscape: Take picture with set scenes to landscape
        Steps:  1.Launch perfect shot activity
                2.Check scence mode ,set mode to landscape
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png') 
        # Step 2
        self._setScenesStatus('landscape')
        #Step 3
        self._takePerfectshotPicture()

    def testCapturePictureWithScenesPortrait(self):
        """
        Summary:testCapturePictureWithScenesSport: Take picture with set scenes to portrait
        Steps:  1.Launch perfect shot activity
                2.Check scence mode ,set mode to portrait
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png') 
        # Step 2
        self._setScenesStatus('portrait')
        #Step 3
        self._takePerfectshotPicture()

    def testCapturePictureWithScenesAuto(self):
        """
        Summary:testCapturePictureWithScenesAuto: Take picture with set scenes to auto
        Steps:  1.Launch perfect shot activity
                2.Check scence mode ,set mode to auto
                3.Touch shutter button to capture picture
                4.Exit  activity
        """
        self.expect('1_launch_checkpoint.png') 
        # Step 2
        self._setScenesStatus('auto')
        #Step 3
        self._takePerfectshotPicture()

    def testCapturePictureWithScenesNightPortrait(self):
        """
        Summary:testCapturePictureWithScenes NightPortrait: Capture image with Scene modeNightPortrait
        Steps:  1.Launch perfect shot activity
		2.Set Scene mode Night-portrait
		3.Touch shutter button to capture picture
		4.Exit  activity 
        """	
        self.expect('1_launch_checkpoint.png') 
        # Step 2
	time.sleep(1)
        self._setScenesStatus('night-portrait')
	time.sleep(1)
        #Step 3
        self._takePerfectshotPicture()
	time.sleep(1)
	self._setScenesStatus('auto')
        
    def testCapturePictureWithScenesBarcode(self):
        """
        Summary:testCapturePictureWithScenesBarcode: Capture image with Scene mode Barcode
        Steps:  1.Launch perfect shot activity
		2.Set Scene mode Barcode
		3.Touch shutter button to capture picture
		4.Exit  activity 
        """
        self.expect('1_launch_checkpoint.png') 
        # Step 2
	time.sleep(1)
        self._setScenesStatus('barcode')
	time.sleep(1)
        #Step 3
        self._takePerfectshotPicture()
	time.sleep(1)
	self._setScenesStatus('auto')
        
    def testCapturePictureWithScenesFireworks(self):
        """
        Summary:testCapturePictureWithScenesFireworks: Capture image with Scene mode Fireworks
        Steps:  1.Launch perfect shot activity
		2.Set Scene mode Fireworks
		3.Touch shutter button to capture picture
		4.Exit  activity 
        """
        self.expect('1_launch_checkpoint.png') 
        # Step 2
	time.sleep(1)
        self._setScenesStatus('fireworks')
	time.sleep(1)
        #Step 3
        self._takePerfectshotPicture()
	time.sleep(1)
	self._setScenesStatus('auto')

    def _takePerfectshotPicture(self):
        #Get the number of photo in sdcard
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            beforeNo = '0'
        #Get the number of photo in sdcard
        else:
            beforeNo = commands.getoutput('adb shell ls /mnt/sdcard/DCIM/*  | grep BST | wc -l')
        self.touch(Camera,waittime=25)
        afterNo = commands.getoutput('adb shell ls /mnt/sdcard/DCIM/*  | grep BST | wc -l')
	time.sleep(3)
        if string.atoi(beforeNo) != string.atoi(afterNo) - 9:
            self.fail('take picture fail!')

    def _setGeoLocationStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(Geolocation)
        if status =='on':
            self.touch((170,288))
        elif status =='off':
            self.touch((50,286))
        state = self.adbCmd(Geolocation_STATE)
	time.sleep(1)
        statevalue = state.find(status)
        if statevalue == -1:
	    time.sleep(1)
            self.fail('set camera geoloaction'+status+ 'fail!')

    def _setExposureStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        # Enter exposuer setting
        self.touch(Setting)\
        .touch(Exposure)
        if status =='0':
            self.touch((290,288))
        elif status =='3':
            self.touch((400,294))
        elif status =='6':
            self.touch((520,290))
        elif status =='-3':
            self.touch((170,292))
        elif status =='-6':
            self.touch((56,292))
        state = self.adbCmd(Exposure_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera exposure'+status+ 'fail!')

    def _setScenesStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(Scences)
        if status =='sports':
            commands.getoutput('adb shell input swipe 640 308 302 300')
            self.touch((551,282))
        elif status == 'night':
            self.touch((523,294))
        elif status == 'landscape':
            self.touch((402,294))
        elif status == 'portrait':
            self.touch((285,294))
        elif status == 'night-portrait':
            self.touch((175,294))
        elif status == 'barcode':
            self.touch((65,294))
        #elif status == 'fireworks':
            #self.touch((50,294))
        elif status == 'auto':
            commands.getoutput('adb shell input swipe 648 288 59 288')
            self.touch((657,294))
        state = self.adbCmd(Scene_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera scenes to'+status+'fail!')

    def _launchperfectshot(self):
        self.launch(self.runComponent)
        if self.exists('location.png'):
            self.touch('ok.png')
        self.touch((650,1090))
	time.sleep(3)
        self.touch((215,1097)) 

    def tearDown(self):
        self.adbCmd('rm -r '+ PICTURE_PATH + '/*')
        self.press('back,back,back,home')
        super(PerfectShotTest,self).tearDown()
