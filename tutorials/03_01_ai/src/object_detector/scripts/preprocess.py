#!/usr/bin/env python
# coding: UTF-8

import rospy
import sys
import numpy as np
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge


def process_image(msg):
    try:
        bridge = CvBridge()
        # Image convert to rgb8 numpy array.
        # Expect encode "rgb8" or "bgr8"
        orig = bridge.imgmsg_to_cv2(msg, "rgb8")

        #
        # If need more preprocess, write here.
        #

        newImgMsg = bridge.cv2_to_imgmsg(orig, encoding="rgb8")
        pub.publish(newImgMsg)
    except Exception as err:
        print(err)


rospy.init_node('preprocess')
rospy.loginfo('preprocess node started')
pub = rospy.Publisher('preprocessed_image', Image, queue_size=1)
rospy.Subscriber("image_raw", Image, process_image)
rospy.spin()
