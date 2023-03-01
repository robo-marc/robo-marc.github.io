#!/usr/bin/env python3
## coding: UTF-8
import numpy as np
import rospy
from object_detector_msg.msg import ObjectDetectionResult
from object_detector_msg.msg import DetectedObject
from norfair import Detection, Tracker


class ObjectTracking():
    def __init__(self):
        self.sub = rospy.Subscriber('object_detection_result', ObjectDetectionResult,
                                    self.recieve_object_detection_result)
        self.pub = rospy.Publisher('object_tracking_result', ObjectDetectionResult, queue_size=10)
        self.tracker = Tracker(distance_function=self.calc_distance, distance_threshold=20)

    def calc_distance(self, detection, tracked_object):
        return np.linalg.norm(detection.points - tracked_object.estimate)

    def get_center(self, detected_object):
        return np.array([detected_object.xmax - detected_object.xmin,
                         detected_object.ymax - detected_object.ymin])

    def create_detected_object_with_id(self, tracked_object):
        src = tracked_object.last_detection.data
        detected_object = DetectedObject()
        detected_object.xmin = src.xmin
        detected_object.xmax = src.xmax
        detected_object.ymin = src.ymin
        detected_object.ymax = src.ymax
        detected_object.confidence = src.confidence
        detected_object.class_id = src.class_id
        detected_object.name = f'{src.name}:{tracked_object.id}'
        return detected_object

    def recieve_object_detection_result(self, object_detection_result):
        detected_objects = object_detection_result.detected_objects
        # Convert DetectedObject to norfair.Detection.
        # Set DetectedObject in data field of norfair.Detection.
        detections = [Detection(self.get_center(obj), data=obj) for obj in detected_objects]
        tracked_objects = self.tracker.update(detections=detections)
        objs = [self.create_detected_object_with_id(obj) for obj in tracked_objects if obj.live_points]
        self.pub.publish(ObjectDetectionResult(detected_objects=objs))


if __name__ == '__main__':
    rospy.init_node('object_tracking')
    rospy.loginfo('object_tracking node is started.')
    node = ObjectTracking()
    rospy.spin()
