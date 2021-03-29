# 画像処理・AI技術活用コース

<!-- TOC -->

- [1. コース概要](#1-コース概要)
    - [1.1. 受講方法](#11-受講方法)
    - [1.2. 実行環境](#12-実行環境)
- [2. 講習会視聴リンクおよび資料](#2-講習会視聴リンクおよび資料)
    - [2.1. 画像処理・AI技術活用コース(前編)](#21-画像処理・ai技術活用コース前編)
    - [2.2. 画像処理・AI技術活用コース(後編)](#22-画像処理・ai技術活用コース後編)
- [3. 実習](#3-実習)
    - [3.1. 画像認識AI実行環境構築](#31-画像認識ai実行環境構築)
    - [3.2. ROS環境構築](#32-ros環境構築)
    - [3.3. 物体検出システムを構築する](#33-物体検出システムを構築する)
        - [3.3.1. ノード構成](#331-ノード構成)
        - [3.3.2. メッセージ定義](#332-メッセージ定義)
        - [3.3.3. uvc_camera_nodeとweb_video_serverをインストールする](#333-uvc_camera_nodeとweb_video_serverをインストールする)
        - [3.3.4. カスタムメッセージを定義する](#334-カスタムメッセージを定義する)
        - [3.3.5. 物体検出パッケージを作成する](#335-物体検出パッケージを作成する)
    - [3.4. 物体検出モデルをSSDに入れ替える](#34-物体検出モデルをssdに入れ替える)
    - [3.5. 物体追跡機能を追加する](#35-物体追跡機能を追加する)
- [4. アンケートご協力のお願い](#4-アンケートご協力のお願い)

<!-- /TOC -->

## 1. コース概要

(1)の前編では，ロボットシステムにおけるAI活用事例の解説として，ロボットマニピュレーションのための画像認識技術への応用やロボットアーム制御，近年，急速に進歩を遂げている自動車の自動運転技術への応用について簡単に紹介します．後半では，AIを活用したロボットシステムのチュートリアルとして，カメラ画像による物体追跡システムの構築を実際に行ってみます．

(2)の後編では，AIを活用したロボットシステムの設計，運用のポイントについて解説します．少し上級者向けの内容となっております．

### 1.1. 受講方法

本コースは実習形式の講習となっております。以下の手順に従い、実行環境を構築した上でビデオチュートリアルに従い実習を進めてください。

### 1.2. 実行環境

以下の実行環境を想定しています。

* OS: Ubuntu 18.04 LTS
* ROS: Melodic


## 2. 講習会視聴リンクおよび資料
### 2.1. 画像処理・AI技術活用コース(前編)
<iframe width="560" height="315" src="https://www.youtube.com/embed/C7ceJawFGmM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- [画像処理・AI技術活用コース(前編)(YouTube)](https://www.youtube.com/watch?v=C7ceJawFGmM)
- [画像処理・AI技術活用コース(前編)(PDF)](03_01_ai_01.pdf)

<iframe src="//www.slideshare.net/slideshow/embed_code/key/EoRl0oKCBaweTm" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/NEDOROBOMARC/nedoai" title="NEDO特別講座_画像処理・AI技術活用コース_前編" target="_blank">NEDO特別講座_画像処理・AI技術活用コース_前編</a> </strong> from <strong><a href="https://www.slideshare.net/NEDOROBOMARC" target="_blank">NEDOROBOMARC</a></strong> </div>

<br/>

### 2.2. 画像処理・AI技術活用コース(後編)
<iframe width="560" height="315" src="https://www.youtube.com/embed/DDRekscGOb4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- [画像処理・AI技術活用コース(後編)(YouTube)](https://www.youtube.com/watch?v=DDRekscGOb4)
- [画像処理・AI技術活用コース(後編)(PDF)](03_01_ai_02.pdf)

<iframe src="//www.slideshare.net/slideshow/embed_code/key/7ZwUE1IqYsyQnt" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/NEDOROBOMARC/nedoai-245269607" title="NEDO特別講座_画像処理・AI技術活用コース_後編" target="_blank">NEDO特別講座_画像処理・AI技術活用コース_後編</a> </strong> from <strong><a href="https://www.slideshare.net/NEDOROBOMARC" target="_blank">NEDOROBOMARC</a></strong> </div>

<br/>

## 3. 実習

以下、具体的な作業内容について説明します。

### 3.1. 画像認識AI実行環境構築

以下の手順を参照して画像認識AIの実行環境を構築してください。

* [実行環境構築手順](setup-object-detection-lib)

### 3.2. ROS環境構築

```
# リポジトリ登録
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

# aptをアップデート
sudo apt update
sudo apt upgrade

# ROSをインストール
sudo apt install ros-melodic-desktop-full

# rosdepのインストール
sudo apt install python-rosdep
sudo rosdep init
rosdep update

# 環境変数設定
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc

# パッケージインストーラーをインストール
sudo apt install python-rosinstall python-catkin-tools

# ワークスペースを作成
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin init

# ビルド
catkin build
source devel/setup.bash
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
```

### 3.3. 物体検出システムを構築する

#### 3.3.1. ノード構成
* uvc_camera_node : カメラから画像を取得する
* web_video_server_node : システム内を流れるImage topicを表示する
* preprocess_node : 画像の前処理を行う
* object_detector_yolo_node : YOLOv4-tinyで物体検出をする
* annotation_node : 物体検出の結果を画像に描画する

#### 3.3.2. メッセージ定義
* ObjectDetectionResult : 物体検出結果のメッセージ。
物体検出結果はカスタムメッセージを自分で定義する

#### 3.3.3. uvc_camera_nodeとweb_video_serverをインストールする

```
sudo apt install ros-melodic-web-video-server
sudo apt install ros-melodic-uvc-camera
```

#### 3.3.4. カスタムメッセージを定義する

以下で使用する [object_detector_msg](object_detector_msg.zip) 一式をダウンロードできます。
- [object_detector_msg.zip](object_detector_msg.zip) 

```
cd ~/catkin_ws/src
catkin_create_pkg object_detector_msg rospy roscpp std_msgs
cd object_detector_msg
mkdir msg
```

object_detector_msg/msgディレクトリに以下のファイルを格納します。
* DetectedObject.msg
* ObjectDetectionResult.msg

CMakeLists.txtを編集する
* object_detector_msg/CMakeLists.txt

```
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)
...
add_message_files(
  FILES
  DetectedObject.msg
  ObjectDetectionResult.msg
)
...
generate_messages(
  DEPENDENCIES
  std_msgs
)
...
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES object_detector_msg
  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)
```

package.xmlを編集する

* object_detector_msg/package.xml

```
# 以下の二つを追記する
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
```

ビルドする

```
catkin build
. ~/catkin_ws/devel/setup.bash
rosmsg show object_detector_msg/DetectedObject
rosmsg show object_detector_msg/ObjectDetectionResult
```

#### 3.3.5. 物体検出パッケージを作成する

以下で使用する [object_detector](object_detector.zip) 一式をダウンロードできます。
- [object_detector.zip](object_detector.zip)

```
cd ~/catkin_ws/src
catkin_create_pkg object_detector rospy roscpp std_msgs
```

YOLOの実装であるpytorch-YOLOv4をlibに配置する

```
cd ~/catkin_ws/src/object_detector
mkdir lib
cd lib
git clone https://github.com/Tianxiaomo/pytorch-YOLOv4
# 重みをダウンロード
mkdir weight
cd weight
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights
```

ノードとlaunchファイルを配置する
* object_detector/script/object_detector_yolo.py
* object_detector/script/preprocess.py
* object_detector/script/annotation.py
* object_detector/launch/object_detector_yolo.launch

CMakeList.txtを編集する
* object_detector/CMakeLists.txt

```
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  object_detector_msg
)
```

package.xmlを編集する
* object_detector/package.xml

```
<buildtool_depend>object_detector_msg</buildtool_depend>
<exec_depend>object_detector_msg</exec_depend>
```

実行する

```
# PYTHONPATHにYOLOの実装へのパスを追加する
export PYTHONPATH="~/catkin_ws/src/object_detector/lib/pytorch-YOLOv4:$PYTHONPATH"

# 各ノードに実行権限を設定する
cd ~/catkin_ws/src/object_detector/scripts
chmod +x object_detector_yolo.py
chmod +x preprocess.py
chmod +x annotation.py

# rospkgをインストールする
pip3 install rospkg

catkin build
source ~/catkin_ws/devel/setup.bash
roslaunch object_detector object_detector_yolo.launch
```

ここで、```localhost:8080```にブラウザでアクセスすることで、物体検出の結果を確認することができます。

### 3.4. 物体検出モデルをSSDに入れ替える

ノードとlaunchファイルを配置配置する
* object_detector/scripts/object_detector_ssd.py
* object_detector/launch/object_detector_ssd.launch

SSDの実装であるSSDをlibに配置する

```
cd ~/catkin_ws/src/object_detector/lib
git clone https://github.com/lufficc/SSD
cd SSD
mkdir weight
cd weight
wget https://github.com/lufficc/SSD/releases/download/1.2/mobilenet_v2_ssd320_voc0712_v2.pth
```

実行する

```
# PYTHONPATHにSSDの実装へのパスを追加する
export PYTHONPATH="~/catkin_ws/src/object_detector/lib/SSD:$PYTHONPATH"

# launchファイルを実行する
roslaunch object_detector object_detector_ssd.launch
```

YOLOの時と同様に```localhost:8080```にブラウザでアクセスすることで、物体検出の結果を確認することができます。

### 3.5. 物体追跡機能を追加する

物体追跡のライブラリをインストールする

```
sudo apt install nofair
```

ノードとlaunchファイルを配置する
* object_detector/scripts/object_tracking.py
* object_detector/launch/object_tracking.launch

実行する

```
# PYTHONPATHにYOLOの実装へのパスを追加する
export PYTHONPATH="~/catkin_ws/src/object_detector/lib/pytorch-YOLOv4:$PYTHONPATH"

# launchファイルを実行
roslaunch object_detector object_tracking.launch
```

ここで、```localhost:8080```にブラウザでアクセスすることで、物体検出の結果を確認することができます。


## 4. アンケートご協力のお願い

本コースをご視聴いただきありがとうございました。
お手数ですが、今後のコース改善のため以下のアンケートにご協力いただければ幸いです。

- [アンケート](https://docs.google.com/forms/d/e/1FAIpQLScdiVxfeDrkS1O6GVAXZ2j-c5pjEFQPwbeVmjh1rdLB4bX2bA/viewform)
