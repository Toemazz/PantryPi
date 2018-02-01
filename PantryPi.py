import time
import json
import picamera
import argparse
import Dropbox as db
from pubnub import Pubnub
from shutil import copyfile


# Method: Used to send a message to PubNub
def send_message_to_pubnub():
    msg = 'New Image on Dropbox'

    json_msg = json.dumps(msg)
    channel = 'PiToPantryPal'
    pubnub.publish(channel=channel, message=json_msg)
    print('[INFO]: Published message to {}'.format(channel))


# Method: Used to capture the image for classification
def capture_image(img_path, capture=False):
    save_path = './images/capture.jpg'

    # Capture image from Raspberry Pi
    if capture:
        camera = picamera.PiCamera()
        camera.resolution = (1024, 768)
        time.sleep(1)
        camera.capture(save_path)
    # Load test image
    else:
        copyfile(img_path, save_path)
 

# Method: Used when message is received from PubNub
def callback(message, channel):
    # Capture the image
    capture_image(img_path=image_path, capture=capture)

    # Upload image to DropBox
    db.delete_single_file_from_dropbox(dbox_dir='/', file_name='capture.jpg')
    db.upload_single_file_to_dropbox(local_file_path='./images/capture.jpg', dbox_dir='/')

    # Send ack to PubNub
    send_message_to_pubnub()


# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-p', '--path', required=False, type=str, default='./test_images/01.jpg',
                help='Path to test image file')
ap.add_argument('-c', '--capture', required=False, type=bool, default=False,
                help='True: Capture image from Pi, False: Load a test image')
args = vars(ap.parse_args())

# Connect to PubNub
pubnub = Pubnub(publish_key="pub-c-935c97ba-71d6-4dd1-b500-e1ea1f85e0a5",
                subscribe_key="sub-c-7ce45822-aff9-11e7-8f6d-3a18aff742a6")

# Optional arguments
capture = args['capture']
image_path = args['path']

# Subscribe to PubNub
channel = "PhoneToPi"
pubnub.subscribe(channels=channel, callback=callback)
print("[INFO]: Subscribed to PubNub on channel '{}'".format(channel))
