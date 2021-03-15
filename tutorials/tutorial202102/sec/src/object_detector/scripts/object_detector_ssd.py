#!/usr/bin/env python3
# coding: UTF-8

import rospy
import os
import numpy as np
import torch
from sensor_msgs.msg import Image
from object_detector_msg.msg import ObjectDetectionResult
from object_detector_msg.msg import DetectedObject
from ssd.config import cfg
from ssd.data.datasets import VOCDataset
from ssd.utils.checkpoint import CheckPointer
from ssd.data.transforms import build_transforms
from ssd.modeling.detector import build_detection_model


class SsdDetector():
    def __init__(self):
        self.threshold = 0.5

        self.device = torch.device('cpu')
        self.class_names = VOCDataset.class_names
        ssd_dir = os.path.expanduser(rospy.get_param('~model_path'))
        config = os.path.join(ssd_dir, 'configs/mobilenet_v2_ssd320_voc0712.yaml')
        weightfile = os.path.join(ssd_dir, 'weight/mobilenet_v2_ssd320_voc0712_v2.pth')
        cfg.merge_from_file(config)
        cfg.freeze()

        self.model = self.get_model(cfg, weightfile)
        self.transforms = build_transforms(cfg, is_train=False)
        self.model.eval()

        self.sub = rospy.Subscriber("preprocessed_image",
                                    Image, self.object_detection)
        self.pub = rospy.Publisher('object_detection_result',
                                   ObjectDetectionResult, queue_size=10)

    def object_detection(self, msg):
        img = np.frombuffer(msg.data, dtype=np.uint8)
        img = img.reshape(msg.height, msg.width, 3)
        height, width = img.shape[:2]
        images = self.transforms(img)[0].unsqueeze(0)
        result = self.model(images.to(self.device))[0]
        result = result.resize((width, height))
        boxes = result['boxes']
        labels = result['labels']
        scores = result['scores']
        detect_list = []
        for i in range(len(boxes)):
            if scores[i] > self.threshold:
                detect = self.create_detect_object(boxes[i], labels[i],
                                                   scores[i], width, height)
                detect_list.append(detect)
        result = ObjectDetectionResult()
        result.detected_objects = detect_list
        self.pub.publish(result)

    def create_detect_object(self, box, label, confidence, width, height):
        detect = DetectedObject()
        detect.xmin = box[0] / width
        detect.ymin = box[1] / height
        detect.xmax = box[2] / width
        detect.ymax = box[3] / height
        detect.confidence = confidence
        detect.class_id = label
        detect.name = self.class_names[label]
        print(self.class_names[label])
        return detect

    def get_model(self, cfg, weightfile):
        model = build_detection_model(cfg)
        model = model.to(self.device)
        checkpointer = CheckPointer(model)
        checkpointer.load(weightfile, use_latest=weightfile is None)
        return model


if __name__ == '__main__':
    rospy.init_node('SSD')
    rospy.loginfo('SSD node started')
    node = SsdDetector()
    rospy.spin()
