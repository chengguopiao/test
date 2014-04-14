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
VideoSize_STATE= 'cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_video_quality_key'
VIDEO_NUMBERS = 'ls /mnt/sdcard/DCIM/100ANDRO/  | grep VID | wc -l'
CAMERA_ID_FRONT = '1'
CAMERA_ID_BACK = '0'
PICTURE_PATH = '' + os.sep + 'mnt'+os.sep+ DCIM_PATH+'/'+CAMERA_FOLDER
CAMERAKEY=(360,1095)
Setting = (61,60)
Flash = (268,80)
Exposure = (645,190)
Scences =(525,180)
FDFR = (474,60)
FrontFDFR = (351,60)
PictureSize = (398,176)
Geolocation = (280,178)
FrontGeolocation =(57,168)
Hint =(155,170)
SwitchFrontbackCamera =(657,75)
TestCamera =(66,177)
WhiteBalance=(432,173)
ISO_setting=(545,175)
Self_Timer=(679,163)
VideoSize=(290,180)
CameraIcon =(367,1095)
Camera=(366,1095)




class CameraTest(unittest.TestCase):
    def setUp(self):
        super(CameraTest,self).setUp()
        self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
        self.launch(self.runComponent)
        if self.exists('location.png'):
            self.touch('ok.png')

	# Test case 1
    def testswitchmode50times(self):
        """
        Summary:testswitchmode50times: test switch mode 50 times
        Steps:  1.Launch single capture activity
		2.Switch camera mode 50 times
                3.Exit  activity
        """
	#step 1
	self.expect('1_launch_checkpoint.png')
	for i in range (50):
		time.sleep(1)
		self._Videomode()
		time.sleep(2)
		self.expect('Video.png')
		self._Cameramode()
		time.sleep(2)
		self.touch((651,1092))
		time.sleep(1)	
		self.expect('1_launch_checkpoint.png')

	# Test case 2
    def testlaunchcamera50times(self):
        """
        Summary:testlaunchcamera50times: Launch camera 50 times
        Steps:  1.Launch single capture activity
		2.Repeat 50 times
                3.Exit  activity
        """
	self.expect('1_launch_checkpoint.png')
	time.sleep(1)
	for i in range (50):
		time.sleep(1)
		self.press('back,back,back,home')
		time.sleep(1)
		self.runComponent = PACKAGE_NAME + '/' + ACTIVITY_NAME
		self.launch(self.runComponent)
		time.sleep(1)
		self.expect('1_launch_checkpoint.png')

	# Test case 3
    def testswitchbackfrontcameraineachmode30times(self):
        """
        Summary:SwitchBack/Frontcameraineachmode30times: Switch Back/Front camera in each mode 30 times
        Steps:  1.Launch single capture activity
		2.Switch Back/Front camera in each mode 30 times
                3.Exit  activity
        """
	self.expect('1_launch_checkpoint.png')
	time.sleep(1)
	for i in range (30):
		self._CameraFront()
		time.sleep(1)
		self._CameraBack()
		time.sleep(1)
	time.sleep(1)
	self._identifyCameraBack()
	time.sleep(1)
	self._ClearData()
	time.sleep(1)
	
	# Test case 4
    def testChangeflashmode100times(self):
        """
        Summary:testChangeflashmode100times: Change flash mode 100 times
        Steps:  1.Launch single capture activity
		2.Change flash mode 100 times
                3.Exit  activity
        """
	self.expect('1_launch_checkpoint.png')
	time.sleep(1)
	for i in range (100):
		time.sleep(1)
	        self._setFlashStatus('off')
	        time.sleep(1)
                self._setFlashStatus('on')
	        time.sleep(1)

	# Test case 5
    def testChangescenemode100times(self):
        """
        Summary:testChangescenemode100times: Change scene mode 100 times
        Steps:  1.Launch single capture activity
		2.Change scene mode 100 times
                3.Exit  activity
        """
	self.expect('1_launch_checkpoint.png')
	time.sleep(1)
	for i in range (100):
		SCE = random.choice(['sports','night','landscape','portrait','night-portrait','barcode','auto'])
		self._setScenesStatus(SCE)
		time.sleep(1)
	time.sleep(1)
	self._setScenesStatus('auto')

	# Test case 6
    def testChangeexposuremode100times(self):
        """
        Summary:testChangeexposuremode100times: Change exposure mode 100 times
        Steps:  1.Launch single capture activity
		2.Change exposure mode 100 times
                3.Exit  activity
        """
	self.expect('1_launch_checkpoint.png')
	time.sleep(1)
	for i in range (100):
		SCE = random.choice(['0','6','-6','-3','3'])
		self._setExposureStatus(SCE)
		time.sleep(1)



	# Test case 7
    def testChangepicturesizemode100times(self):
        """
        Summary:testChangepicturesizemode100times: Change picture size mode 100 times
        Steps:  1.Launch single capture activity
		2.Change picture size 100 times
                3.Exit  activity
        """
	self.expect('1_launch_checkpoint.png')
	time.sleep(1)
	for i in range (100):
		SCE = random.choice(['WideScreen','StandardScreen'])
		self._setPictureSizeStatus(SCE)
		time.sleep(1)
	time.sleep(2)
	self._setPictureSizeStatus('WideScreen')

	# Test case 8
    def testChangevideosizemode100times(self):
        """
        Summary:testChangevideosizemode100times: Change video size mode 100 times
        Steps:  1.Launch single capture activity
		2.Change video size 100 times
                3.Exit  activity
        """
	self.expect('1_launch_checkpoint.png')
	time.sleep(1)
	self._launchVideo()
	for i in range (100):
		SCE = random.choice(['4','5','6'])
		self._setVideoSizeStatus(SCE)
		time.sleep(1)

	# Test case 9
    def testentergalleryfromgallerypreviewthumbnail100times(self):
        """
        Summary:testentergalleryfromgallerypreviewthumbnail100times: enter gallery from gallery preview thumbnail 100times
        Steps:  1.Launch single capture activity
		2.enter gallery from gallery preview thumbnail 100times
                3.Exit  activity
        """
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2
	self._takePicture()
	time.sleep(2)
	for i in range (100):
		self.touch((68,1095))
		time.sleep(5)
		commands.getoutput('adb shell input tap 300 300')
		time.sleep(5)
		self.expect('gallery.png')
		time.sleep(1)
		self.press('back')
		time.sleep(3)
	
	# Test case 10
    def testCapturesingleimage500timesbackcamera(self):
        """
        Summary:testCapturesingleimage500times: Capture single image 500 times
        Steps:  1.Launch single capture activity
		2.Capture single image 500 times
                3.Exit  activity
        """
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2	
	for i in range (500):
		self._takePicture()
		time.sleep(1)
	time.sleep(1)
	self._ClearData()
	time.sleep(1)

	# Test case 11
    def testCapturesingleimage500timesfrontcamera(self):
        """
        Summary:testCapturesingleimage500times: Capture single image 500 times
        Steps:  1.Launch single capture activity
		2.change to front camera
		3.Capture single image 500 times
                4.Exit  activity
        """
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2	
	self._identifyCameraFront()
	time.sleep(2)
	for i in range (500):
		self._takePicture()
		time.sleep(1)
	time.sleep(1)
	self._identifyCameraBack()
	time.sleep(1)
	self._ClearData()
	time.sleep(1)

	# Test case 12
    def testCapturehdrimage500timesbackcamera(self):
        """
        Summary:testCapturehdrimage500times: Capture hdr image 500 times
        Steps:  1.Launch hdr capture activity
		2.Capture hdr image 500 times
                3.Exit  activity
        """
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2	
	self._launchHdr()
	time.sleep(1)
	for i in range (500):
		self._takePicture()
		time.sleep(1)
	time.sleep(1)
	self._ClearData()
	time.sleep(1)

	# Test case 13
    def testCapturesmileimage500timesbackcamera(self):
        """
        Summary:testCapturesmileimage500times: Capture smile image 500 times
        Steps:  1.Launch smile capture activity
		2.Capture smile image 500 times
                3.Exit  activity
        """
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2	
	self._smile()
	time.sleep(1)
	self.expect('smile.png')
	time.sleep(1)
	for i in range (500):
		self._StakePicture()
		time.sleep(1)
	time.sleep(1)
	self._ClearData()
	time.sleep(1)


	# Test case 14
    def testRecord1080Pvideo500times(self):
        """
        Summary:testRecord1080Pvideo500times: test Record 1080P video 500 times
        Steps:  1.Launch video capture activity
		2.Record 1080P video 500 times
                3.Exit  activity
        """
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2	
	self._launchVideo()
	time.sleep(1)
	self._setVideoSizeStatus('6')
	time.sleep(1)
	for i in range (500):
		self._takeVideo()
		time.sleep(1)
	time.sleep(1)
	self._ClearData()
	time.sleep(1)	
	

	# Test case 15
    def testRecordvideo500timesfrontcamera(self):
        """
        Summary:testRecordvideo500times: test Record video 500 times
        Steps:  1.Launch video capture activity
		2.Change to front camera
		3.Record video 500 times
                4.Exit  activity
        """
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2	
	self._identifyCameraFront()
	time.sleep(1)
	self._launchVideo()
	time.sleep(1)
	for i in range (500):
		self._takeVideo()
		time.sleep(1)
	time.sleep(1)
	self._identifyCameraBack()
	time.sleep(1)
	self._ClearData()
	time.sleep(1)	

	# Test case 16
    def testCaptureburstimage200timesbackcamera(self):
        """
        Summary:testCaptureburstimage200times: Capture burst image 200 times
        Steps:  1.Launch burst capture activity
		2.Capture burst image 200 times
                3.Exit  activity
        """
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2	
	self.touch((652,1102))
	time.sleep(1)
	self.touch((366,1102))
	time.sleep(1)
	self.touch((366,938))
	self.expect('Burst.png')
	for i in range (200):
		self._takeBurstCapture()
		time.sleep(1)
	time.sleep(1)
	self._ClearData()
	time.sleep(1)

	# Test case 17
    def testCapturecontinueimage200timesbackcamera(self):
        """
        Summary:testCapturecontinueimage200times: Capture continue image 200 times
        Steps:  1.Launch continue capture activity
		2.Capture continue image 200 times
                3.Exit  activity
        """
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2	
	time.sleep(1)
	for i in range (200):
		self._CtakePicture()
		time.sleep(1)
	time.sleep(1)
	self._ClearData()
	time.sleep(1)

	# Test case 18
    def testCaptureperfectshotimage200timesbackcamera(self):
        """
        Summary:testCaptureperfectshotimage200times: Capture perfect shot image 200 times
        Steps:  1.Launch perfectshot capture activity
		2.Capture perfectshot image 200 times
                3.Exit  activity
        """
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2	
	self._launchperfectshot()
	time.sleep(1)
	for i in range (200):
		self._takePerfectshotPicture()
		time.sleep(1)
	time.sleep(1)
	self._ClearData()
	time.sleep(1)


	# Test case 19
    def testCapturepanoramaimage200timesbackcamera(self):
        """
        Summary:testCapturepanoramaimage200times: Capture panorama image 200 times
        Steps:  1.Launch panorama capture activity
		2.Capture panorama image 200 times
                3.Exit  activity
        """
	#step 1
        self._launchpanorama()
	time.sleep(2)
	self.expect('1_panorama.png')
	time.sleep(1)
	for i in range (200):
		self._takePanoramaPicture()
		time.sleep(1)
	time.sleep(1)
	self._ClearData()



	# Test case 20
    def testCaptureSingleImage8M500timesbackcamera(self):
	"""
	capture single image 500 times
	8M pixels, back camera
	
	"""

	#step 1
	self.expect('1_launch_checkpoint.png')
	time.sleep(1)
	self._setPictureSizeStatus('StandardScreen')
	self.expect('1_standardscreen mode.png')
	time.sleep(1)
	for i in range (500):
		self._takePicture()
		time.sleep(1)
	time.sleep(2)
	self._setPictureSizeStatus('WideScreen')
	time.sleep(1)
	self.expect('1_launch_checkpoint.png')	
	time.sleep(1)
	self._ClearData()
	time.sleep(1)

	# Test case 21
    def testcaseCaptureSmileImage8M500timesbackcamera(self):
	"""
	Capture Smile Image 8M 500 times back camera
	8M pixels, back camera
	"""
	#step 1
	self.expect('1_launch_checkpoint.png')
	time.sleep(1)
	self._setPictureSizeStatus('StandardScreen')
	time.sleep(1)
	self.expect('1_standardscreen mode.png')
	time.sleep(1)
	self._smile()
	time.sleep(1)
	self.expect('smile_standardscreen mode.png')
	for i in range (500):
		self._StakePicture()
		time.sleep(1)
	time.sleep(2)
	self._setSmilePictureSizeStatus('WideScreen')
	time.sleep(1)
	self._ClearData()
	time.sleep(1)

	# Test Case 22
    def testcaseRecord720PVideo500times(self):
	"""
	Record 720P Video 500times
	Video size 720P
	"""
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2	
	self._launchVideo()
	time.sleep(1)
	self.expect('1_launch_video.png')
	time.sleep(1)
	self._setVideoSizeStatus('5')
	time.sleep(1)
	for i in range (500):
		self._takeVideo()
		time.sleep(1)
	time.sleep(1)
	self._ClearData()
	time.sleep(1)	
	

	# Test Case 23
    def testcaseRecord480Pvideo500times(self):
	"""
	test case Record 480 Pvideo 500 times
	Video size 480P

	"""
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2	
	self._launchVideo()
	time.sleep(1)
	self.expect('1_launch_video.png')
	time.sleep(1)
	self._setVideoSizeStatus('4')
	time.sleep(1)
	for i in range (500):
		self._takeVideo()
		time.sleep(1)
	time.sleep(1)
	self._setVideoSizeStatus('5')
	time.sleep(1)
	self._ClearData()
	time.sleep(1)	
	

	# Test Case 24
    def testcaseBurstImage8M200times(self):
	"""
	test case Burst Image 200 times
	8M pixels, back camera
	"""
	#step 1
	self.expect('1_launch_checkpoint.png')
	#step 2	
	self.touch((652,1102))
	time.sleep(1)
	self.touch((366,1102))
	time.sleep(1)
	self.touch((366,938))
	time.sleep(2)
	self.expect('Burst.png')
	time.sleep(1)
	self._setSmilePictureSizeStatus('StandardScreen')
	time.sleep(1)
	self.expect('1_burst_8m.png')
	for i in range (200):
		self._takeBurstCapture()
		time.sleep(1)
	self._setSmilePictureSizeStatus('WideScreen')
	time.sleep(1)
	self._ClearData()
	time.sleep(1)


    ############################################################################################################
    ############################################################################################################
    def _setFlashStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        # Touch flash setting
        self.touch(Flash)
        if status == 'on':
            self.touch((185,180))
        elif status == 'off':
            self.touch((65,180))
        else:
            self.touch((290,185))
        state = self.adbCmd(Flash_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera flash status to' + status + 'fail!') 

    def _Cameramode(self):
	self.touch((651,1092))
	time.sleep(2)
	self.touch((651,1092))
    def _Videomode(self):
	self.touch((651,1092))
	time.sleep(2)
	self.touch((512,1087))

    def _setScenesStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)
        self.touch(Scences)
	commands.getoutput('adb shell input swipe 59 288 640 288')
	time.sleep(1)
        if status == 'sports':
	    commands.getoutput('adb shell input swipe 648 288 59 288')
            self.touch((536,289))
        elif status == 'night':
            self.touch((530,290))
        elif status == 'landscape':
            self.touch((409,290))
        elif status == 'portrait':
            self.touch((290,290))
        elif status == 'night-portrait':
            self.touch((175,294))
        elif status == 'barcode':
            self.touch((60,294))
        elif status == 'auto':
	    commands.getoutput('adb shell input swipe 648 288 59 288')
            self.touch((653,294))
	time.sleep(3)
        state = self.adbCmd(Scene_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera scenes status'+ status + 'fail!')

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


    def _setSmilePictureSizeStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)
        self.touch((175,185))             # smile PictureSize
        if status == 'WideScreen':
            self.touch((66,292))
        elif status == 'StandardScreen':
            self.touch((175,292))
        state = self.adbCmd(PictureSize_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera picture size to' + status +'fail!')


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


    def _setVideoSizeStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)
        self.touch(VideoSize)
        if status =='6':
            self.touch((403,290)) 
        elif status =='5':
            self.touch((170,290))  # 720  
        elif status =='4':
            self.touch((65,288))  # 480    
        state = self.adbCmd(VideoSize_STATE)
        if state != "":
            statevalue = state.find(status)
            if statevalue == -1:
                self.fail('set video size with' +status+ 'fail!')



    def _CtakePicture(self):
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            before = '0'
        #Get the number of photo in sdcard
        else:
            before = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
            self.sleep(3)
        self.longtouch(CAMERAKEY,waittime=3)
	time.sleep(2)
        after = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        self.sleep(10)
        if string.atoi(after) > 2:
            self.logger.debug('take picture success!')
        else:
            self.fail('Ctake picture fail!')


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
	time.sleep(2)
        after = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        self.sleep(3)
        if string.atoi(before) < string.atoi(after):
            self.logger.debug('take picture success!')
        else:
            self.fail('take picture fail!')

    def _StakePicture(self):
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            before = '0'
        #Get the number of photo in sdcard
        else:
            before = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
            self.sleep(3)
        self.touch(CAMERAKEY,waittime=3)
	time.sleep(2)
	self.touch(CAMERAKEY,waittime=3)
	time.sleep(2)
        after = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        self.sleep(3)
        if string.atoi(before) < string.atoi(after):
            self.logger.debug('take picture success!')
        else:
            self.fail('Stake picture fail!')


    def _identifyCameraFront(self):
        #Check camera already set to front camera
        cameidvalue = self.adbCmd(CAMERA_ID)
        self.logger.debug("Camera ID value is: " + cameidvalue)
        if cameidvalue !='':
            mCameraIDValue = cameidvalue.find(CAMERA_ID_FRONT)
            if mCameraIDValue == -1:
                commands.getoutput('adb shell input swipe 530 6 523 22')
                self.touch(SwitchFrontbackCamera,waittime=3)
		time.sleep(3)
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



    def _launchHdr(self):
        self.launch(self.runComponent)
        if self.exists('location.png'):
            self.touch('ok.png')
        self.touch((655,1210))
	time.sleep(3)
        self.touch((650,899))
	time.sleep(7)

    def _smile(self):
	self.touch((655,1089))
	time.sleep(1)
	self.touch((645,935))
	time.sleep(1)
	self.expect('smile.png')

    def _takeVideo(self):
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            self.beforeNO = '0'
        else:
            self.beforeNO = commands.getoutput('adb shell '+ VIDEO_NUMBERS)
        
        #Record video(10 seconds)
        self.touch(CameraIcon,waittime=10)\
        .touch(CameraIcon,waittime=3)
        
        #Identify add video successfully
        addVideo = commands.getoutput('adb shell '+ VIDEO_NUMBERS)
        if string.atoi(addVideo) != string.atoi(self.beforeNO)+1:
            self.fail('take video fail!')

    def _launchVideo(self):
        self.launch(self.runComponent)
        if self.exists('location.png'):
            self.touch('ok.png')
        self.touch((650,1100))
	time.sleep(3)
        self.touch((503,1089))
	time.sleep(5)

    def _launchperfectshot(self):
        self.launch(self.runComponent)
        if self.exists('location.png'):
            self.touch('ok.png')
        self.touch((656,1100))
	time.sleep(3)
        self.touch((225,1100)) 

    def _launchpanorama(self):
        if self.exists('location.png'):
            self.touch('ok.png')
        self.touch((656,1100))
	time.sleep(2)
        self.touch((78,1095))


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

    def _takePerfectshotPicture(self):
        #Get the number of photo in sdcard
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            beforeNo = '0'
        #Get the number of photo in sdcard
        else:
            beforeNo = commands.getoutput('adb shell ls /mnt/sdcard/DCIM/*  | grep BST | wc -l')
        self.touch(Camera,waittime=10)
        afterNo = commands.getoutput('adb shell ls /mnt/sdcard/DCIM/*  | grep BST | wc -l')
	time.sleep(6)
        if string.atoi(beforeNo) != string.atoi(afterNo) - 9:
            self.fail('take picture fail!')
                

    def _CameraFront(self):
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



    def _CameraBack(self):
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

    def _ClearData(self):
	commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///mnt/sdcard/')
	time.sleep(5)
	commands.getoutput('adb shell rm /mnt/sdcard/DCIM/100ANDRO/*')
	time.sleep(2)
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///mnt/sdcard/')


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


    def _setSmileISOsettingstatus(self, status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)
	commands.getoutput('adb shell input swipe 670 165 78 165')
        self.touch((633,179))             # Smile ISO setting
        if status == 'iso-auto':
            self.touch((525,288))
        elif status == 'iso-100':
            self.touch((405,294))
        elif status == 'iso-200':
            self.touch((285,294))
        elif status == 'iso-400':
            self.touch((170,294))
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
        super(CameraTest,self).tearDown()
	

