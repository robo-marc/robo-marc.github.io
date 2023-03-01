#!/usr/bin/env python3
# coding: UTF-8

import rospy
import os
import numpy as np
import cv2
from sensor_msgs.msg import Image
from object_detector_msg.msg import ObjectDetectionResult
from object_detector_msg.msg import DetectedObject
from tool.utils import *
from tool.torch_utils import *
from tool.darknet2pytorch import Darknet


class YoloV4Detector():
    def __init__(self):
        yolo_dir = os.path.expanduser(rospy.get_param('~model_path'))
        namefile = os.path.join(yolo_dir, 'data/coco.names')
        cfgfile = os.path.join(yolo_dir, 'cfg/yolov4-tiny.cfg')
        weightfile = os.path.join(yolo_dir, 'weight/yolov4-tiny.weights')
        self.use_cuda = False
        self.model = self.get_model(cfgfile, weightfile)
        self.class_names = load_class_names(namefile)
        self.sub = rospy.Subscriber("preprocessed_image",
                                    Image, self.object_detection)
        self.pub = rospy.Publisher('object_detection_result',
                                   ObjectDetectionResult, queue_size=10)

    def object_detection(self, msg):
        # Expect msg is encoded rgb8
        img = np.frombuffer(msg.data, dtype=np.uint8)
        img = img.reshape(msg.height, msg.width, 3)
        sized = cv2.resize(img, (self.model.width, self.model.height))
        boxes = do_detect(self.model, sized, 0.4, 0.6, self.use_cuda)
        detect_list = []
        if len(boxes[0]) > 0:
            print(self.class_names[boxes[0][0][6]])
            for box in boxes[0]:
                detect_list.append(self.create_detect_object(box))
        result = ObjectDetectionResult()
        result.detected_objects = detect_list
        self.pub.publish(result)

    def create_detect_object(self, box):
        detect = DetectedObject()
        detect.xmin = box[0]
        detect.ymin = box[1]
        detect.xmax = box[2]
        detect.ymax = box[3]
        detect.confidence = box[5]
        detect.class_id = box[6]
        detect.name = self.class_names[box[6]]
        return detect

    @staticmethod
    def get_model(cfgfile, weightfile):
        m = Darknet(cfgfile)
        m.print_network()
        m.load_weights(weightfile)
        rospy.loginfo('Loading weights from %s... Done!' % (weightfile))
        return m


if __name__ == '__main__':
    rospy.init_node('yoloV4Tiny')
    rospy.loginfo('yoloV4Tiny node started')
    node = YoloV4Detector()
    rospy.spin()
