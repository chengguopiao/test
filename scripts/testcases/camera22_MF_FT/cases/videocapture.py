#!/usr/bin/env python
import unittest
import string
import time
import os
import commands

"""
@author:Cao Lina
@Note:Stability test cases for intel camera2.2
"""

PACKAGE_NAME = 'com.intel.camera22'
ACTIVITY_NAME = PACKAGE_NAME +'.Camera'


DCIM_PATH = '/sdcard/DCIM'
CAMERA_FOLDER = '100ANDRO'
VIDEO_NUMBERS = 'ls /mnt/sdcard/DCIM/100ANDRO/  | grep VID | wc -l'
CAMERA_ID = 'cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_camera_id_key'
Flash_STATE= 'cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_video_flashmode_key'
VideoSize_STATE= 'cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_video_quality_key'
Geolocation_STATE ='cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_camera_geo_location_key'
WhiteBalance_STATE='cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_whitebalance_key'
Exposure_STATE= 'cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_exposure_key' 
CAMERA_ID_FRONT = '1'
CAMERA_ID_BACK = '0'
PICTURE_PATH = '' + os.sep + 'mnt'+os.sep+ DCIM_PATH+ '/'+CAMERA_FOLDER
CameraIcon =(367,1085)
Flash =(370,75)
Setting =(52,60)
VideoSize =(288,175)
Geolocation =(172,175)
FrontGeolocation=(55,175)
SwitchCamera=(658,57)
Testcamera =(62,182)
WhiteBalance=(514,173)
Exposure = (407,175)


class VideoCameraTest(unittest.TestCase):
    def setUp(self):
        super(VideoCameraTest,self).setUp()
        #Set the name and component to start activity
        self.runComponent = PACKAGE_NAME +'/' + ACTIVITY_NAME 
        self._launchVideo()

    def testRecordVideoWithFlashOn(self):
        """
        Summary:testRecordVideoWithFlashOn:Record an video in flash on mode
        Steps  : 1.Launch video activity
                 2.Check flash state,set to ON
                 3.Touch shutter button to capture 30s video
                 4.Exit  activity
        """
        #Step 1
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setFlashStatus('torch')
        #Step 3
        self._takeVideo()

    def testRecordVideoWithFlashOff(self):
        """
        Summary:testRecordVideoWithFlashOff:Record an video in flash off mode
        Steps  : 1.Launch video activity
                 2.Check flash state,set to Off
                 3.Touch shutter button to capture 30s video
                 4.Exit  activity
        """
        #Step 1
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setFlashStatus('off')
        #Step 3
        self._takeVideo()

    def testRecordVideoWithVideoSizeFHD(self):
        """
        Summary:testRecordVideoWithVideoSizeFHD:Record an video in FHD video size mode
        Steps  : 1,Launch video activity
                 2.Check video size ,set to FHD
                 3.Touch shutter button to capture 30s video
                 4.Exit  activit
        """
        #Step 1
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setVideoSizeStatus('6')
        #Step 3
        self._takeVideo()

    def testRecordVideoWithVideoSizeHD(self):
        """
        Summary:testRecordVideoWithVideoSizeHD:Record an video in HD video size mode
        Steps  : 1,Launch video activity
                 2.Check video size ,set to HD
                 3.Touch shutter button to capture 30s video
                 4.Exit  activit
        """
        #Step 1
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setVideoSizeStatus('5')
        #Step 3
        self._takeVideo()

    def testRecordVideoWithVideoSizeSD(self):
        """
        Summary:testRecordVideoWithVideoSizeSD:Record an video in SD video size mode
        Steps  : 1.Launch video activity
                 2.Check video size ,set to SD
                 3.Touch shutter button to capture 30s video
                 4.Exit  activit
        """
        #Step 1
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setVideoSizeStatus('4')
        #Step 3
        self._takeVideo()
	time.sleep(1)
	self._setVideoSizeStatus('5')

    def testRecordVideoWithGeoLocationOn(self):
        """
        Summary:testRecordVideoWithGeoLocationOn:Record an video in GeoLocation On
        Steps  : 1.Launch video activity
                 2.Check geo-tag ,set to ON
                 3.Touch shutter button to capture 30s video
                 4.Exit  activity
        """
        #Step 1
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setGeoLocationStatus('on')
        #Step 3
        self._takeVideo()

    def testRecordVideoWithGeoLocationOff(self):
        """
        Summary:testRecordVideoWithGeoLocationOff:Record an video in GeoLocation Off
        Steps  : 1.Launch video activity
                 2.Check geo-tag ,set to Off
                 3.Touch shutter button to capture 30s video
                 4.Exit  activity
        """
        #Step 1
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setGeoLocationStatus('off')
        #Step 3
        self._takeVideo()

    def testRecordSwithToTestCamera(self):
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(Testcamera)\
        .expect('2_testcamera_checkpoint.png')

    def testRearFaceRecordVideoWithGeoLocationOn(self):
        """
        Summary:testRearFaceRecordVideoWithGeoLocationOn:Record an video with rear face camera and set GeoLocation On
        Steps  : 1.Launch video activity
                 2.Set to front face camera
                 3.Check geo-tag,set to ON
                 4.Touch shutter button to capture 30s video
                 5.Exit  activity
        """
        #Step 2
        self._identifyCameraFront()
        self.expect('1_launch_checkpoint.png')
        #Step 3
        self._setFrontGeoLocationStatus('on')
        #Step 4
        self._takeVideo()

    def testRearFaceRecordVideoWithGeoLocationOff(self):
        """
        Summary:testRearFaceRecordVideoWithGeoLocationOff:Record an video with rear face camera and set GeoLocation Off
        Steps  : 1.Launch video activity
                 2.Set to front face camera
                 3.Check geo-tag,set to ON
                 4.Touch shutter button to capture 30s video
                 5.Exit  activity
        """
        #Step 2
        self._identifyCameraFront()
        self.expect('1_launch_checkpoint.png')
        #Step 3
        self._setFrontGeoLocationStatus('off')
        #Step 4
        self._takeVideo()

    def testRecordVideoCaptureVideoWithBalanceAuto(self):
        """
        Summary:testRecordVideoCaptureVideoWithBalanceAuto: Capture video with White Balance Auto
        Steps:  1.Launch video activity
		2.Set White Balance Auto
		3.Touch shutter button to capture 30s video
		4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setWBstatus('auto')
        #Step 3
        self._takeVideo()
        
    def testRecordVideoCaptureVideoWithBalanceIncandescent(self):
        """
        Summary:testRecordVideoCaptureVideoWithBalanceIncandescent: Capture video with White Balance Incandescent
        Steps:  1.Launch video activity
		2.Set White Balance Incandescent
		3.Touch shutter button to capture 30s video
		4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setWBstatus('incandescent')
        #Step 3
        self._takeVideo()
        
    def testRecordVideoCaptureVideoWithBalanceDaylight(self):
        """
        Summary:testRecordVideoCaptureVideoWithBalanceDaylight: Capture video with White Balance Daylight
        Steps:  1.Launch video activity
		2.Set White Balance Daylight
		3.Touch shutter button to capture 30s video
		4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setWBstatus('daylight')
        #Step 3
        self._takeVideo()
        
    def testRecordVideoCaptureVideoWithBalanceFluorescent(self):
        """
        Summary:testRecordVideoCaptureVideoWithBalanceFluorescent: Capture video with White Balance Fluorescent
        Steps:  1.Launch video activity
		2.Set White Balance Fluorescent
		3.Touch shutter button to capture 30s video
		4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setWBstatus('fluorescent')
        #Step 3
        self._takeVideo()
        
    def testRecordVideoCaptureVideoWithBalanceCloudy(self):
        """
        Summary:testRecordVideoCaptureVideoWithBalanceCloudy: Capture video with White Balance Cloudy
        Steps:  1.Launch video activity
		2.Set White Balance Cloudy
		3.Touch shutter button to capture 30s video
		4.Exit  activity
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setWBstatus('cloudy-daylight')
        #Step 3
        self._takeVideo()
        
    def testRecordVideoCaptureVideoWithExposureAuto(self):
        """
        Summary:testRecordVideoCaptureVideoWithExposureAuto: Capture video with Exposure auto
        Steps:  1.Launch Video activity
		2.Touch Exposure Setting icon, set Exposure auto
		3.Touch shutter button
		4.Touch shutter button to capture picture
		5.Exit  activity 
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setExposureStatus('0')
        #Step 3
        self._takeVideo()
        
    def testRecordVideoCaptureVideoWithExposure1(self):
        """
        Summary:testRecordVideoCaptureVideoWithExposure1: Capture video with Exposure 1
        Steps:  1.Launch Video activity
		2.Touch Exposure Setting icon, set Exposure 1
		3.Touch shutter button 
		4.Touch shutter button to capture picture
		5.Exit  activity  
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setExposureStatus('3')
        #Step 3
        self._takeVideo()
        
    def testRecordVideoCaptureVideoWithExposure2(self):
        """
        Summary:testRecordVideoCaptureVideoWithExposure2: Capture video with Exposure 2
        Steps:  1.Launch Video activity
				2.Touch Exposure Setting icon, set Exposure 2
				3.Touch shutter button 
				4.Touch shutter button to capture picture
				5.Exit  activity   
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setExposureStatus('6')
        #Step 3
        self._takeVideo()
        
    def testRecordVideoCaptureVideoWithExposureRed1(self):
        """
        Summary:testRecordVideoCaptureVideoWithExposureRed1: Capture video with Exposure -1
        Steps:  1.Launch Video activity
		2.Touch Exposure Setting icon, set Exposure -1
		3.Touch shutter button
		4.Touch shutter button to capture picture
		5.Exit  activity   
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setExposureStatus('-3')
        #Step 3
        self._takeVideo()
        
    def testRecordVideoCaptureVideoWithExposureRed2(self):
        """
        Summary:testRecordVideoCaptureVideoWithExposureRed2: Capture video with Exposure -2
        Steps:  1.Launch Video activity
		2.Touch Exposure Setting icon, set Exposure -2
		3.Touch shutter button
		4.Touch shutter button to capture picture
		5.Exit  activity    
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
        #Step 2
        self._setExposureStatus('-6')
        #Step 3
        self._takeVideo()
        
    def testRecordVideoCaptureVideoWithHSSize(self):
        """
        Summary:testRecordVideoCaptureVideoWithHSSize: Capture video with HS size
        Steps:  1.Launch video activity
		2.Check video size ,set to HS
		3.Touch shutter button to capture 30s video
		4.Exit  activity   
        """
        
    def testRecordVideoWithCaptureImage(self):
        """
        Summary:testRecordVideoWithCaptureImage: Capture image when record video
        Steps:  1.Launch video activity
                2.Touch shutter button to capture 30s video
		3.Touch screen to capture a picture during recording video
		4.Exit  activity   
        """
        self._identifyCameraBack()
        self.expect('1_launch_checkpoint.png')
	#step 2
	#Get the number of video in sdcard
	result1 = self.adbCmd('ls '+DCIM_PATH)
        if result1.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            self.beforevideoNO = '0'
        else:
            self.beforevideoNO = commands.getoutput('adb shell '+ VIDEO_NUMBERS)

        result2 = self.adbCmd('ls '+DCIM_PATH)
        if result2.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            beforepictureNO = '0'

        #Get the number of photo in sdcard
        else:
            beforepictureNO = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
            self.sleep(3)
        
        #step 3
        self.touch(CameraIcon,waittime=10)\
	.touch((365,576),waittime=3)
	time.sleep(20)
        self.touch(CameraIcon,waittime=3)
        
        #Identify add video successfully
        addVideo = commands.getoutput('adb shell '+ VIDEO_NUMBERS)
        if string.atoi(addVideo) != string.atoi(self.beforevideoNO)+1:
            self.fail('take video fail!')

	#Identify add picture successfully
        afterpictureNO = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        self.sleep(3)
        if string.atoi(beforepictureNO) == string.atoi(afterpictureNO) - 1 or string.atoi(beforepictureNO) == string.atoi(afterpictureNO) - 2:
            self.logger.debug('take picture success!')
        else:
            self.fail('take picture fail!')

    def _takeVideo(self):
        result = self.adbCmd('ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            self.beforeNO = '0'
        else:
            self.beforeNO = commands.getoutput('adb shell '+ VIDEO_NUMBERS)
        
        #Record video(30 seconds)
        self.touch(CameraIcon,waittime=30)\
        .touch(CameraIcon,waittime=3)
        
        #Identify add video successfully
        addVideo = commands.getoutput('adb shell '+ VIDEO_NUMBERS)
        if string.atoi(addVideo) != string.atoi(self.beforeNO)+1:
            self.fail('take video fail!')

    def _setFlashStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        # Touch flash setting
        self.touch(Flash)
        if status =='torch':
            self.touch((170,180),waittime=3)
        elif status =='off':
            self.touch((60,180),waittime=3)
        state = self.adbCmd(Flash_STATE)
        statevalue = state.find(status)
	time.sleep(3)
        if statevalue == -1:
            self.fail('set video with flash' +status+ 'fail!')

    def _setVideoSizeStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(VideoSize)
        if status =='6':
            self.touch((405,288))
        elif status =='5':
            self.touch((170,290))    
        elif status =='4':
            self.touch((56,288))      
        state = self.adbCmd(VideoSize_STATE)
        if state != "":
            statevalue = state.find(status)
            if statevalue == -1:
                self.fail('set video size with' +status+ 'fail!')

    def _setGeoLocationStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(Geolocation)
        if status =='on':
            self.touch((174,288))
        elif status =='off':
            self.touch((60,284)) 
        state = self.adbCmd(Geolocation_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set video with geolocation' +status+ 'fail!')

    def _setFrontGeoLocationStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)\
        .touch(FrontGeolocation)
        if status =='on':
            self.touch((174,288))
        elif status =='off':
            self.touch((60,284)) 
        state = self.adbCmd(Geolocation_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set video with geolocation' +status+ 'fail!')

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

    def _setExposureStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        # Enter exposuer setting
        self.touch(Setting)
        #.drag(start=(620,178),end=(366,214),time=4,steps=6)\
        self.touch(Exposure)
        if status == '0':
            self.touch((293,294))
        elif status == '3':
            self.touch((411,300))
        elif status == '6':
            self.touch((519,290))
        elif status == '-3':
            self.touch((182,290))
        elif status == '-6':
            self.touch((60,288))
        state = self.adbCmd(Exposure_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera exposure status' +status+ 'fail!')

    def _setWBstatus(self,status):
	commands.getoutput('adb shell input swipe 530 6 523 22')
        self.touch(Setting)
        self.touch(WhiteBalance)
        if status == 'auto':
            self.touch((528,288))
        elif status == 'incandescent':
            self.touch((408,294))
        elif status == 'daylight':
            self.touch((304,294))
        elif status == 'fluorescent':
            self.touch((172,294))
        elif status == 'cloudy-daylight':
            self.touch((67,294))
	time.sleep(3)
        state = self.adbCmd(WhiteBalance_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera WhitBalance status'+ status + 'fail!')




    def _launchVideo(self):
        self.launch(self.runComponent)
        if self.exists('location.png'):
            self.touch('ok.png')
        self.touch((650,1090))
	time.sleep(3)
        self.touch((492,1101))
	time.sleep(5)

    def tearDown(self):
        self.adbCmd('rm -r '+ PICTURE_PATH + '/*')
        self.press('back,back,back,home')
        super(VideoCameraTest,self).tearDown()
