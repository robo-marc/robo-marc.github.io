#!/usr/bin/env python
# coding: UTF-8

import rospy
from sensor_msgs.msg import Image
from object_detector_msg.msg import ObjectDetectionResult
from object_detector_msg.msg import DetectedObject
import cv2
from cv_bridge import CvBridge


class Annotator():
    def __init__(self):
        self.bridge = CvBridge()
        self.detected_objects = None
        self.classnum = 80
        self.img_sub = rospy.Subscriber('preprocessed_image', Image,
                                        self.annotation)
        self.box_sub = rospy.Subscriber('object_detection_result',
                                        ObjectDetectionResult, self.update_box)
        self.pub = rospy.Publisher('annotated_image', Image, queue_size=10)

    def annotation(self, img_msg):
        if self.detected_objects is None:
            self.pub.publish(img_msg)
        else:
            annotated_img = self.bridge.imgmsg_to_cv2(img_msg, 'rgb8')
            for element in self.detected_objects:
                xmin = int(element.xmin*img_msg.width)
                xmax = int(element.xmax*img_msg.width)
                ymin = int(element.ymin*img_msg.height)
                ymax = int(element.ymax*img_msg.height)
                rgb = self.get_rgb(element.class_id)
                annotated_img = cv2.putText(annotated_img, element.name,
                                            (xmin, ymin),
                                            cv2.FONT_HERSHEY_SIMPLEX,
                                            1.2, rgb, 1)
                annotated_img = cv2.rectangle(annotated_img, (xmin, ymin),
                                              (xmax, ymax), rgb, 1)
            annotated_img = self.bridge.cv2_to_imgmsg(annotated_img,
                                                      encoding="rgb8")
            self.pub.publish(annotated_img)

    def update_box(self, msg):
        self.detected_objects = msg.detected_objects

    def get_rgb(self, value):
        full = 255
        red = -(full/self.classnum) * value + full
        blue = (full/self.classnum) * value
        if value >= self.classnum/2:
            green = -(2 * full/self.classnum) * value + 2 * full
        else:
            green = (2 * full / self.classnum) * value
        return (red, green, blue)


if __name__ == '__main__':
    rospy.init_node('annotation')
    rospy.loginfo('annotation node started')
    node = Annotator()
    rospy.spin()
