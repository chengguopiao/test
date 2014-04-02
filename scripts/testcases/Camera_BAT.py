#/usr/bin/python 

from devicewrapper.android import device as d
from uiautomator import device as d
import unittest
import time
import os
import sys
import commands
import string

CAMERA_ACTIVITY = 'adb shell am start -n com.intel.camera22/.Camera'
CAMERA_ID = 'adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_camera_id_key'
PictureSize_STATE ='adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_picture_size_key'
DCIM_PATH = '/sdcard/DCIM'
CAMERA_FOLDER = '100ANDRO'
VideoSize_STATE= 'adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_video_quality_key'
VIDEO_NUMBERS = 'ls /mnt/sdcard/DCIM/100ANDRO/  | grep VID | wc -l'
Flash_STATE= 'adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0_0.xml | grep pref_camera_flashmode_key'
Geolocation_STATE ='adb shell cat /data/data/com.intel.camera22/shared_prefs/com.intel.camera22_preferences_0.xml | grep pref_camera_geo_location_key'

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


#####################################################3

class MyTest(unittest.TestCase):


    def setUp(self):
        d.press.home()
        self._launchcamera()
        super(MyTest,self).setUp()

    def tearDown(self):
        d.press.back()
        super(MyTest,self).tearDown()


# Test case 1
    def testCaptureWithBackAndFrontCamera(self):
        # set camera status to back
        self._confirmcamerastatus('back')
        # take 10 picture
        for i in range (0,1):
            self._takePicture()
        self._confirmcamerastatus('front')
        for i in range (0,1):
            self._takePicture()
        self._confirmcamerastatus('back')    

# Test case 2
    def testCaptureWith6MPPortraitFlashOn(self):
        # Set picture size
        self._setPictureSizeStatus('WideScreen')
        # Set flash status
        self._setFlashStatus('on')
        time.sleep(1)
        self._takePicture()

# Test case 3
    def testCaptureWithFrontCamera(self):
        self._confirmcamerastatus('front')
        time.sleep(1)
        self._takePicture()
        self._confirmcamerastatus('back') 

# Test case 4
    def testCaptureWith8MPPortraitFlashAuto(self):
        # Set picture size
        self._setPictureSizeStatus('StandardScreen')
        # Set flash status
        self._setFlashStatus('auto')
        time.sleep(1)
        self._takePicture()
        time.sleep(1)
        self._setPictureSizeStatus('WideScreen')

# Test case 5
    def testCapturevideo720portraitposition(self):
        # Select Video Mode mode
        self._VideoMode()
        time.sleep(1)
        self._setVideoSizeStatus('5')
        time.sleep(1)
        self._takeVideo()


# Test case 6
    def testCaptureburstimagesportraitmode(self):
        self._launchBurst()
        time.sleep(1)
        self._takePicture()

# Test case 7 
    def testCapturePicturePanoramaWithGeolocation(self):
        self._launchpanorama()
        time.sleep(1)
        self._setGeoLocationStatus('on')
        time.sleep(1)
        self._PtakePicture()

# Test case 8
    def testCaptureVideoRecordingPressShutter(self):
        self._VideoMode()
        time.sleep(1)
        self._CtakeVideo()

# Test case 9
    def testCaptureSmilingFaceDefaultsettingPortraitBacFacingCamera(self):
        self._launchSmail()
        time.sleep(1)
        self._stakePicture()

# Test case 10
    def testCapturePerfectShotmodewithFacesPortrait(self):
        self._launchperfectshot()
        time.sleep(1)
        self._setGeoLocationStatus('off')
        time.sleep(1)
        self._btakePicture()

# Test case 11
    def testCaptureCaptureImagewithZoom(self):
        d(resourceId = "com.intel.camera22:id/face_view").pinch.Out(percent=80, steps=200)		 
        d(resourceId = "com.intel.camera22:id/face_view").pinch.Out(percent=80, steps=200)	
        d(resourceId = "com.intel.camera22:id/face_view").pinch.Out(percent=80, steps=200)
        time.sleep(1)
        self._takePicture()

# Test case 12
    def testCaptureCaptureVideowithZoominbetween(self):
        self._VideoMode()
        time.sleep(2)
        d(resourceId = "com.intel.camera22:id/camera_preview").pinch.Out(percent=80, steps=200)		 
        d(resourceId = "com.intel.camera22:id/camera_preview").pinch.Out(percent=80, steps=200)	
        d(resourceId = "com.intel.camera22:id/camera_preview").pinch.Out(percent=80, steps=200)
        self._takeVideo() 	

# Test case 13
    def testCaptureCameraLaunchSocialCameraCapturcontinuousPhotoFrontBack(self):
        self._confirmcamerastatus('back')
        time.sleep(1)	
        self._DtakePicture()
        time.sleep(1)
        self._confirmcamerastatus('front')
        time.sleep(1)
        self._DtakePicture()
        self._confirmcamerastatus('back')
#        





##############################################################       

    def _launchcamera(self):

        commands.getoutput(CAMERA_ACTIVITY)
        try:
            d(text = 'OK').wait.exists(timeout=3000)
            d(text = 'OK').click.wait()
        except:
            pass
        finally:
            pass

    def _confirmcamerastatus(self,status):
        #check back/front camera
        if status == 'front':
            camera = commands.getoutput(CAMERA_ID)
            cameravalue = camera.find('1')
            if cameravalue == -1:
                commands.getoutput('adb shell input swipe 530 6 523 22')
                d(description = 'Front and back camera switch').click.wait()
            time.sleep(2)
            camera = commands.getoutput(CAMERA_ID)
            cameravalue = camera.find('1')
            assert cameravalue != -1
        if status == 'back':
            camera = commands.getoutput(CAMERA_ID)
            cameravalue = camera.find('0')
            if cameravalue == -1:
                commands.getoutput('adb shell input swipe 530 6 523 22')
                d(description = 'Front and back camera switch').click.wait()
            time.sleep(2)
            camera = commands.getoutput(CAMERA_ID)
            cameravalue = camera.find('0')
            assert cameravalue != -1

    def _takePicture(self):
        result = commands.getoutput('adb shell ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            before = '0'
        #Get the number of photo in sdcard
        else:
            before = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep jpg | wc -l')
            time.sleep(3)
        d.click(356,1100)
        time.sleep(3)
        after = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep jpg  | wc -l')
        time.sleep(2)
        if string.atoi(before) < string.atoi(after):
            print('take picture success!')
        else:
            self.fail('take picture fail!') 

    def _btakePicture(self):
        result = commands.getoutput('adb shell ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            before = '0'
        #Get the number of photo in sdcard
        else:
            before = commands.getoutput('adb shell ls /sdcard/DCIM/100ANDRO/* | grep BST | wc -l')
            time.sleep(3)
        d.click(356,1100)
        time.sleep(2)
        after = commands.getoutput('adb shell ls /sdcard/DCIM/100ANDRO/* | grep BST | wc -l')
        time.sleep(2)
        if string.atoi(before) < string.atoi(after) - 2 :
            print('take picture success!')
        else:
            self.fail('take picture fail!')          


    def _stakePicture(self):
        result = commands.getoutput('adb shell ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            before = '0'
        #Get the number of photo in sdcard
        else:
            before = commands.getoutput('adb shell ls /sdcard/DCIM/100ANDRO/* | grep jpg | wc -l')
            time.sleep(3)
        d.click(356,1100)
        time.sleep(2)
        d.click(356,1100)
        after = commands.getoutput('adb shell ls /sdcard/DCIM/100ANDRO/* | grep jpg | wc -l')
        time.sleep(2)
        if string.atoi(before) == string.atoi(after) - 1 or string.atoi(before) == string.atoi(after) - 2:
            print('take picture success!')
        else:
            self.fail('take picture fail!')            

    def _PtakePicture(self):
        result = commands.getoutput('adb shell ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            before = '0'
        #Get the number of photo in sdcard
        else:
            before = commands.getoutput('adb shell ls /sdcard/DCIM/100ANDRO/* | grep jpg | wc -l')
            time.sleep(3)
        d.click(356,1100)
        time.sleep(2)
        d.click(356,1100)
        time.sleep(3)
        after = commands.getoutput('adb shell ls /sdcard/DCIM/100ANDRO/* | grep jpg | wc -l')
        time.sleep(3)
        if string.atoi(before) == string.atoi(after) - 1 or string.atoi(before) == string.atoi(after) - 2:
            print('take picture success!')
        else:
            self.fail('take picture fail!')
        

    def _DtakePicture(self):
        self._ClearData()
        d.swipe(363, 1145, 359, 1045, steps=600)
        time.sleep(2)
        after = commands.getoutput('adb shell ls /sdcard/DCIM/100ANDRO/* | grep jpg | wc -l')
        time.sleep(3)
        if string.atoi(after) > 10:
            print('take picture success!')
        else:
            self.fail('take picture fail!')


    def _setPictureSizeStatus(self,status):
        #commands.getoutput('adb shell input swipe 530 6 523 22')
        d.swipe(530,6,523,22)
        time.sleep(1)
        d.click(65,85)
        time.sleep(1)
        d.click(412,185)
        time.sleep(1)
        if status == 'WideScreen':
            d.click(60,292)
        elif status == 'StandardScreen':
            d.click(180,292)
        time.sleep(2)
        state = commands.getoutput(PictureSize_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera picture size to' + status +'fail!')

    def _setFlashStatus(self,status):
        #commands.getoutput('adb shell input swipe 530 6 523 22')
        # Touch flash setting
        d.swipe(530,6,523,22)
        time.sleep(1)
        d.click(270,85)
        time.sleep(2)	
        if status == 'on':
            d.click(176,176)
        elif status == 'off':
            d.click(59,178)
        elif status  == 'auto':
            d.click(300,180)
        else:
            d.click(296,176)
        time.sleep(2)
        state = commands.getoutput(Flash_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera flash status to' + status + 'fail!') 



    def _VideoMode(self):
        d.click(645,1100)
        time.sleep(1)
        d.click(515,1100)
        time.sleep(1)

    def _setVideoSizeStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        time.sleep(1)
        d.click(52,60)
        time.sleep(1)
        d.click(295,180)
        time.sleep(1)
        if status =='6':
            d.click(405,288)
        elif status =='5':
            d.click(170,290)    
        elif status =='4':
            d.click(56,288)      
        state = commands.getoutput(VideoSize_STATE)
        if state != "":
            statevalue = state.find(status)
            if statevalue == -1:
                self.fail('set video size with' +status+ 'fail!')
    def _takeVideo(self):
        result = commands.getoutput('adb shell ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            self.beforeNO = '0'
        else:
            self.beforeNO = commands.getoutput('adb shell '+ VIDEO_NUMBERS)
        
        #Record video(30 seconds)
        d(description = 'Shutter button').click.wait()
        time.sleep(5)
        d(description = 'Shutter button').click.wait()

        #Identify add video successfully
        addVideo = commands.getoutput('adb shell '+ VIDEO_NUMBERS)
        if string.atoi(addVideo) != string.atoi(self.beforeNO)+1:
            self.fail('take video fail!')
    def _launchBurst(self):
        try:
            d(text = 'OK').wait.exists(timeout=3000)
            d(text = 'OK').click.wait()
        except:
            pass
        finally:
            self._confirmcamerastatus('back')
            d.click(650,1090)
            d.click(358,1076)
            d.click(360,922) 
    def _launchpanorama(self):
        try:
            d(text = 'OK').wait.exists(timeout=3000)
            d(text = 'OK').click.wait()
        except:
            pass
        finally:    
            d.click(650,1090)
            time.sleep(2)
            d.click(80,1084) 
 
    def _setGeoLocationStatus(self,status):
        commands.getoutput('adb shell input swipe 530 6 523 22')
        d.click(52,60)
        d.click(50,168)
        if status == 'on':
            d.click(170,284)
        elif status == 'off':
            d.click(60,276)
        state = commands.getoutput(Geolocation_STATE)
        statevalue = state.find(status)
        if statevalue == -1:
            self.fail('set camera geoloaction to' + status + 'fail!')

    def _VideoMode(self):
        try:
            d(text = 'OK').wait.exists(timeout=3000)
            d(text = 'OK').click.wait()
        except:
            pass
        finally:
            d.click(650,1090)
            time.sleep(3)
            d.click(492,1101)
            time.sleep(5)

    def _CtakeVideo(self):
        result = commands.getoutput('adb shell ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            self.beforeNO = '0'
        else:
            self.beforeNO = commands.getoutput('adb shell '+ VIDEO_NUMBERS)
        
        #Record video(30 seconds)
        d.swipe(363, 1145, 359, 1045, steps=100)
        #Identify add video successfully
        addVideo = commands.getoutput('adb shell '+ VIDEO_NUMBERS)
        if string.atoi(addVideo) != string.atoi(self.beforeNO)+1:
            self.fail('take video fail!')

    def _launchSmail(self):
        try:
            d(text = 'OK').wait.exists(timeout=3000)
            d(text = 'OK').click.wait()
        except:
            pass
        finally:    
            d.click(650,1090)
            d.click(650,930)
    
    def _StakePicture(self):
        result = commands.getoutput('adb shell ls '+DCIM_PATH)
        if result.find(CAMERA_FOLDER) == -1:
            self.logger.info("no 100ANDRO folder.")
            before = '0'
        #Get the number of photo in sdcard
        else:
            before = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
            time.sleep(3)
        d(description = 'Shutter button').click.wait()
        time.sleep(1)
        d(description = 'Shutter button').click.wait()
        after = commands.getoutput('adb shell ls /sdcard/DCIM/* | grep IMG | wc -l')
        time.sleep(3)
        if string.atoi(before) == string.atoi(after) - 1 or string.atoi(before) == string.atoi(after) - 2:
            print('take picture success!')
        else:
            self.fail('take picture fail!')

    def _launchperfectshot(self):
        try:
            d(text = 'OK').wait.exists(timeout=3000)
            d(text = 'OK').click.wait()
        except:
            pass
        finally: 
            d.click(650,1090)
            time.sleep(3)
            d.click(230,1097) 

    def _ClearData(self):
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///mnt/sdcard/')
        time.sleep(5)
        commands.getoutput('adb shell rm /mnt/sdcard/DCIM/100ANDRO/*')
        time.sleep(2)
        commands.getoutput('adb shell am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///mnt/sdcard/')



if __name__ =='__main__':  
    unittest.main()  

    


