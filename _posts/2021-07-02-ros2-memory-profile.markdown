---
layout: post
title:  " 【7月2日】ROS2 メモリプロファイルレポート (Discourse)"
date:   2021-07-02 00:00:000
#image:  news.png
categories:   Nedo

image: assets/images/nedo-news-s.png
#image_alt: sample post 1
#image_caption: testing post caption
---



[【7月2日】ROS2 メモリプロファイルレポート (Discourse)](https://discourse.ros.org/t/ros2-memory-usage-no-dds/21206)

ROS2 Memory Usage (no DDS) というタイトルで、ROS2のDDS部分を除くメモリ使用量の分析レポートが7月2日に投稿されていました。

#### ROS2 の基本メモリ使用量 ≒ ４MB
レポートでは、DDSのライブラリを除くROS2のベースとなるライブラリ (rclcpp.so) と pub/sub 機能が使用するメモリ使用量が約４MB、以降1ノードあたり約10kB程度のメモリ使用量増加が認められたと述べられています。

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/0/0d18d1ac0701ecd617982fe933d3bd3c9d77660b.png">

詳細は、[Discourse](https://discourse.ros.org/t/ros2-memory-usage-no-dds/21206)を御覧ください。
