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
Delete_CMD ='rm -r sdcard/DCIM/100ANDRO/'

CAMERA_ID_FRONT = '1'
CAMERA_ID_BACK = '0'
PICTURE_PATH = '' + os.sep + 'mnt'+os.sep+ DCIM_PATH+'/'+CAMERA_FOLDER
CAMERAKEY=(366,1100)
Setting = (89,81)
Flash = (260,60)
Exposure = (640,170)
Scences =(520,174)
FDFR = (460,56)
FrontFDFR = (360,56)
PictureSize = (408,176)
Geolocation = (290,178)
FrontGeolocation =(56,168)
Hint =(160,170)
SwitchFrontbackCamera =(658,50)
TestCamera =(60,180)

class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        self.launch(self.runComponent)
        if self.exists('location.png'):
            self.touch('ok.png')

    # Test case 1
    def testQuickSwitchtoSinglemode(self):
        """
        Summary:testQuickSwitchtoSinglemode: Quick Switch to Single mode
        Steps:  1.Launch single capture activity
                2.press change mode and then press Video icon to enter video
                3.press change mode icon then choose camera group 
        """
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2
	self._Cameramode()
	time.sleep(2)
	self._Videomode()
	time.sleep(2)
	self._Cameramode()
	time.sleep(1)
	self.touch((663,1100))
	time.sleep(3)
	self.expect('1_launch_checkpoint.png')	
	
    # Test case 2
    def testQuickSwitchtoHDRmode(self):
        """
        Summary:testQuickSwitchtoHDRmode: Quick Switch to HDR mode
        Steps:  1.Launch HDR capture activity
                2.press change mode and then press Video icon to enter video
                3.press change mode icon then choose camera group  
        """
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2
        if self.exists('location.png'):
            self.touch('ok.png')
        self.touch((655,1110))
	time.sleep(3)
        self.touch((650,790))
	time.sleep(2)
	self._Videomode()
	time.sleep(2)
	self._Cameramode()
	self.touch((655,1100))
	time.sleep(1)
	self.expect('1_launch_checkpoint.png')	


    # Test case 3
    def testQuickSwitchtoBurstmode(self):
        """
        Summary:testQuickSwitchtoBurstmode: Quick Switch to Burst mode
        Steps:  1.Launch Burst capture activity
                2.press change mode and then press panorama icon to enter panorama
                3.press change mode icon then choose Multi group  
        """  
	#step 1
	time.sleep(1)
	self.expect('1_launch_checkpoint.png')
	#step 2
        if self.exists('location.png'):
            self.touch('ok.png')
        self.touch((655,1110))
	time.sleep(3)
        self.touch((360,1093))
	time.sleep(3)
	self.touch((360.1029))
	time.sleep(3)
	self.touch((655,1110))
	time.sleep(1)
	self.touch((655,1110))
	time.sleep(1)
	self.touch((655,1110))
	time.sleep(1)
	self._Videomode()
	time.sleep(1)
	self._Cameramode()
	self.touch((655,1100))
	time.sleep(1)
	self.expect('1_launch_checkpoint.png')
    
    # Test case 4
    def testQuickSwitchtoPerfectShotmode(self):
        """
        Summary:testQuickSwitchtoPerfectShotmode: Quick Switch to Perfect Shot mode 
        Steps:  1.Launch Perfect capture activity
                2.press change mode and then press panorama icon to enter panorama
                3.press change mode icon then choose Multi group  
        """ 
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2
	if self.exists('location.png'):
            self.touch('ok.png')
        self.touch((655,1110))
	time.sleep(3)
        self.touch((230,1093))
	time.sleep(3)
	self.touch((655,1110))
	time.sleep(1)
	self.touch((655,1110))
	time.sleep(1)
	self.touch((655,1110))
	time.sleep(1)
	self._Videomode()
	time.sleep(1)
	self._Cameramode()
	self.touch((655,1100))
	time.sleep(1)
	self.expect('1_launch_checkpoint.png') 

    # Test case 5
    def testQuickSwitchtoGallery(self):
        """
        Summary:testQuickSwitchtoGallery: Quick Switch to gallery 
        Steps:  1. Launch camera 
                2. Touch shutter button to capture a picture
                3. Touch the thubnail icon to view it in gallery 
        """ 
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2
	self._takePicture()
	time.sleep(2)
	self.touch((80,1082))
	time.sleep(5)
	commands.getoutput('adb shell input tap 300 300')
	time.sleep(3)
	self.expect('gallery.png')
    # Test case 6
    def testQuickSwitchtoSmileCammode(self):
        """
        Summary:testQuickSwitchtoSmileCammode: Quick Switch to SmileCam mode
        Steps:  1.Launch SmileCam capture activity
                2.press change mode and then press Video icon to enter video
                3.press change mode icon then choose camera group  
        """  
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2
	self.touch((655,1110))
	time.sleep(1)
	self.touch((646,923))
	time.sleep(1)
	self.expect('smile.png')
	time.sleep(2)
	self._Videomode()
	time.sleep(2)
	self._Cameramode()
	time.sleep(2)
	self.touch((655,1110))
	self.expect('1_launch_checkpoint.png')
		
    def _takePicture(self):
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            before = '0'
        #Get the number of photo in sdcard
        else:
            before = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
            self.sleep(3)
        self.touch(CAMERAKEY,waittime=3)
        after = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
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
            self.touch((180,172))
        elif status == 'off':
            self.touch((60,178))
        else:
            self.touch((290,176))
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
            self.touch((288,288))
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
            self.touch((400,290))
        elif status == 'night':
            self.touch((280,294))
        elif status == 'landscape':
            self.touch((170,294))
        elif status == 'portrait':
            self.touch((60,294))
        elif status == 'auto':
            self.touch((520,294))
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

    def tearDown(self):
        self.adbCmd('rm -r '+ PICTURE_PATH + '/*')
        self.press('back,back,back,home')
        super(CameraTest,self).tearDown()
    def _launchpanorama(self):
        self.launch(self.runComponent)
        if self.exists('location.png'):
            self.touch('ok.png')
        self.touch((650,1090))
	time.sleep(2)
        self.touch((80,1084))
    def _Cameramode(self):
	self.touch((652,1100))
	time.sleep(2)
	self.touch((652,1100))
    def _Videomode(self):
	self.touch((652,1100))
	time.sleep(2)
	self.touch((500,1100))
