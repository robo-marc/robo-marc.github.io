---
layout: page
#title: Ros News
permalink: /rosnews/
#image: rosnews.png
---

# ROS Watch

このページでは、ROSやロボットミドルウェアに関するさまざまなニュースを発信しています。


----------
### <span style="color:navy;">2022/07/11</span> [PlanSys2](https://plansys2.github.io/)

- PlanSys2
  - PDDLベースのプランニングシステム
- 主に4つのノードから構成される
  - Domain Expert
    - PDDLモデル情報（タイプ、述語、関数、およびアクション）
  - Problem Export
    - モデルを構成する現在のインスタンス、Predicate、関数、および目標
  - Planner
    - ドメインおよびProblem Expertsに含まれる情報を使用して、計画（一連のアクション）を生成
  - Executor
    - プランを取得し、アクションパフォーマー（各アクションを実装するROS2ノード）をアクティブ化し実行
  - プラン→ビヘイビアツリーに変換して実行

<img src="https://plansys2.github.io/_images/plansys2_arch.png" width="400"/>
<img src="https://plansys2.github.io/_images/plansys2_arch2.png" width="400"/>

----------
### <span style="color:navy;">2022/07/11</span> [PlotJuggler](https://github.com/facontidavide/PlotJuggler/releases/tag/3.5.0)

- 高速で強力かつ 直感的な時系列を視覚化するツール
- ドラッグアンドドロップのユーザーインターフェイス
- ファイルからのデータロード
- データのライブストリーミングに接続可能
- ビジュアライゼーションレイアウト・構成を保存、再利用可能
- OpenGLによる高速なビジュアライゼーション
- 微分、移動平均、積分など変換可能
- プラグインを使用して簡単に拡張できます


<img src="https://user-images.githubusercontent.com/2822888/178490207-00e98610-5de7-4ffc-b94c-eab6396f8829.png" width="400"/>
<img src="https://user-images.githubusercontent.com/2822888/178490594-1436544e-5972-4ebf-9ca9-7dcd99d47030.png" width="400"/>

----------
### <span style="color:navy;">2022/07/11</span> [ROS Learning Series (YouTube)](https://www.youtube.com/playlist?list=PL0sla3wvhSnYV_idE4zRxh0ZClVGA9KiK)

- Robotics with Sakshayが提供するチュートリアルビデオ
- 6本のビデオ
  - Introduction
  - Simulation Turtlebot3
  - ROS Concepts
  - Custom Mobile Robot
  - MoveIt! Robot Manipulation
  - ROS2

<iframe width="560" height="315" src="https://www.youtube.com/embed/aNOiMyaq8dM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

----------
### <span style="color:navy;">2022/07/11</span> [Fast DDS Visualizer](https://github.com/Serafadam/depthai_ros_driver)

- DepthAI
  - SpatialAIプラットフォーム
  - Intel Movidius VPUを利用
  - OAKカメラシリーズで利用可能
- DepthAI ROS2ドライバー
  - DepthAIをROS2で利用可能
  - 深度、RGB、モノラルカメラ出力
  - .h264ストリームを記録
  - X86 PC, ARMベースシステム対応
  - ROS2 Galactic, ROS2 Humble

<img src="https://github.com/Serafadam/depthai_ros_driver/raw/galactic/docs/example.gif" width="400"/>

----------
### <span style="color:navy;">2022/07/22</span> [Fast DDS Visualizer](https://github.com/lardemua/atom)

- Fast DDS Visualizer
  - データをリアルタイムの2Dチャートで視覚化するグラフィカルデスクトップアプリケーションをリリース
  - データの抽出とその監視をリアルタイムで実行可能
- 仕様
  - Windows and Linux
  - ライセンス：Apache 2.0, GPL 3.0 OSS
  - 無料で使用可能
  - ダウンロード時に氏名e-mail登録を求められる

<img src="https://eprosima.com/images/Products/FastDDSVisualizer.png" width="400"/>



----------
### <span style="color:navy;">2022/07/22</span> [ATOM Calibration](https://github.com/lardemua/atom)

- ATOM Calibration
  - マルチセンサー、マルチモーダル、ロボットシステム用の一連のキャリブレーションツール
  - キャリブレーション手順のすべてのステップを容易にするためのいくつかのスクリプトを提供
  - 今の所ROS1のみ
  - 今後ROS2サポート予定
  - YouTubeにて動画リスト提供
    - https://www.youtube.com/watch?v=BYs1-H9vh0s&list=PLQN09mzV5mbI4h5IQt3Eu9kugSk-08mnY



<img src="https://github.com/lardemua/atom/blob/noetic-devel/docs/atom_logo.png?raw=true/375/215" width="400"/>

<img src="https://github.com/lardemua/atom/raw/noetic-devel/docs/OverviewATOMMMTBot_compressed.gif" width="400"/>



----------
### <span style="color:navy;">2022/06/22</span> [Humble / 22.04 RollingのFast-DDS通信障害](https://discourse.ros.org/t/nav2-issues-with-humble-binaries-due-to-fast-dds-rmw-regression/26128)

- Humble / 22.04 RollingがFast-DDSに移行して以来、通信障害に関連する問題が増加
  - Fast-DDSのRMWレイヤーがリグレッションを起こしている
  - FastDDS without Discovery Server?
    - https://discourse.ros.org/t/fastdds-without-discovery-server/26117
    - FastDDS✕、CycloneDDS○
    - FastDDSだとトピックに接続できないことが75％くらいの確率で発生する wo Discovery Server
  - Nav2 lifecycle manager won't startup nodes
    - https://github.com/ros-planning/navigation2/issues/2917
    - Nav2のライフサイクルノードのステートが切り替わらない
    - callback_group_からコールバックを削除すると解決
    - FastDDSとCycloneDDSで挙動が異なる、タイマーの呼び出しタイミングの問題？
  - lifecycle manager wait for service should have a finite, or at least configurable, timeout
    - https://github.com/ros-planning/navigation2/issues/3033
    - ライフサイクルマネージャーに、エラーが発生している管理ノードを指定するとライフサイクルサービスが適切に作成されない
    - ライフサイクルマネージャがタイムアウトすべきところでデッドロックする
    - これもFastDDSが問題？


----------
### <span style="color:navy;">2022/05/21</span> [DDSよるネットワークの停止問題](https://discourse.ros.org/t/unconfigured-dds-considered-harmful-to-networks/25689/15)

- ROS2において設定が不十分の場合ネットワークが落ちる問題に遭遇
  - DDSを適切に設定しないと、マルチキャストパケットによりパケットフラッディングが発生する
- 解決策：export ROS_LOCALHOST_ONLY=1あるいは↓
  - ホスト間通信ができなくなる

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<CycloneDDS xmlns="https://cdds.io/config" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="https://cdds.io/config https://raw.githubusercontent.com/eclipse-cyclonedds/cyclonedds/master/etc/cyclonedds.xsd">
　　<Domain id="any">
　　　　<General>
　　　　　　<NetworkInterfaceAddress>lo</NetworkInterfaceAddress>
　　　　　　<AllowMulticast>false</AllowMulticast>
　　　　</General>
　　　　<Discovery>
　　　　　　<ParticipantIndex>auto</ParticipantIndex>
　　　　　　<Peers>
　　　　　　　<Peer Address="localhost"/>
　　　　　　</Peers>
　　　　　　<MaxAutoParticipantIndex>120</MaxAutoParticipantIndex>
　　　　</Discovery>
　　</Domain>
</CycloneDDS>
```

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/5/565445a8478a24296181b440895cf402ecb9c8e3.png" width="400"/>

- https://docs.ros.org/en/foxy/Tutorials/Advanced/Discovery-Server/Discovery-Server.html

- 独自調査：DDSのDiscoveryは色々大変
- DDSのディスカバリ
  - Simple Discovery Protocol (SDP) DDS標準
    - ノード数増→パケット数増大、マルチキャスト→WiFi　✕
  - Discovery Service 非標準 (FastDDS only)
    - パケット数減→帯域節約、SPOF
    - V1, V2あり
  - Cloud Discovery 非標準 (RIT only)

- V1

<img src="https://docs.ros.org/en/foxy/_images/ds_explanation.svg" width="400"/>

- V2

<img src="https://docs.ros.org/en/foxy/_images/ds1vs2.svg" width="400"/>

- Discovery Protocolによるパケット数の違い

<img src="https://docs.ros.org/en/foxy/_images/discovery_server_v2_performance.svg" width="400"/>

- ↑のtutorialではFastDDSのDiscovery Serviceを設定する方法を解説
  - SDPに比べて、パケット数を半分以下にすることができる
  - V2なら15分の1にすることができる
  - でも、もともとDDSを導入したのはSPOFをなくすためでは？
- Discovery Server
  - 複数利用可能、冗長構成、バックアップ構成は可能
  - SDPは使わずSDを使うべきか

----------
### <span style="color:navy;">2022/06/24</span> [DDSよるネットワークの停止問題](https://discourse.ros.org/t/unconfigured-dds-considered-harmful-to-networks/25689/15)

- ROS2において設定が不十分の場合ネットワークが落ちる問題に遭遇
  - DDSを適切に設定しないと、マルチキャストパケットによりパケットフラッディングが発生する
- 解決策：export ROS_LOCALHOST_ONLY=1あるいは↓
  - ホスト間通信ができなくなる

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<CycloneDDS xmlns="https://cdds.io/config" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="https://cdds.io/config https://raw.githubusercontent.com/eclipse-cyclonedds/cyclonedds/master/etc/cyclonedds.xsd">
　　<Domain id="any">
　　　　<General>
　　　　　　<NetworkInterfaceAddress>lo</NetworkInterfaceAddress>
　　　　　　<AllowMulticast>false</AllowMulticast>
　　　　</General>
　　　　<Discovery>
　　　　　　<ParticipantIndex>auto</ParticipantIndex>
　　　　　　<Peers>
　　　　　　　<Peer Address="localhost"/>
　　　　　　</Peers>
　　　　　　<MaxAutoParticipantIndex>120</MaxAutoParticipantIndex>
　　　　</Discovery>
　　</Domain>
</CycloneDDS>
```

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/5/565445a8478a24296181b440895cf402ecb9c8e3.png" width="400"/>

----------
### <span style="color:navy;">2022/06/24</span> [ROSConJPプログラムリリース](https://roscon.jp/2022_en/#program)

- ROSConJP 2022/10/19 @京都国際会館
  - ROSCon 10/19-21
- 基調講演
  - 基調講演１: Airpeak S1ドローンのオーバービューとソニーでのROSの活用：藤田智哉、小林大 (ソニー)
  - 基調講演２: Open-RMFによるマルチフリートオペレーション：Michael Grey & Morgan Quigley (Open Robotics)
- その他講演
  - Unreal Engineを用いたROS 2分散シミュレータの構築
  - ROSとNode-REDの組み合わせによるIT-OT連携システム開発の効率化
  - SROS 2 with OIDC(OpenID Connect) :ロボットと人を安全に繋ぐ技術

<img src="https://roscon.jp/2022_en/img/ROSConJP22_lowres.jpg" width="400"/>

----------
### <span style="color:navy;">2022/06/20</span> [pyrobosim](https://community.gazebosim.org/t/new-releases-2022-06-13-fortress-citadel/1463)

- ROS2対応の行動プロトタイピング用2D移動ロボットシミュレータ
  - MITで開発された古い2Dの移動ロボットシミュレータをROS2対応に
  - シンプルなポイントロボットシミュレーター

- https://github.com/sea-bass/pyrobosim
- https://pyrobosim.readthedocs.io/en/latest/


<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/a/acdcbb3d6b259ffbd57c61467852877ac005a230.gif" width="400"/>

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/optimized/2X/7/7855e891e73bda561a42acadf99d14239c23a1cf_2_423x500.png" width="400"/>


----------
### <span style="color:navy;">2022/06/13</span> [Gazeboリリース (6/13) (Fortress, Citadel)](https://community.gazebosim.org/t/new-releases-2022-06-13-fortress-citadel/1463)

- Gazeboリリース 2022/6/13
  - 主な新機能
  - 押し出し2Dポリラインジオメトリサポート→
  - エレベーターシステム→
  - JSON形式でメッセージを出力する


<img src="https://global.discourse-cdn.com/standard10/uploads/gazebo/original/1X/6744ff5c56b0de8266eb5e6944d3a66b4aa21b9f.gif" width="400"/>


<img src="https://global.discourse-cdn.com/standard10/uploads/gazebo/original/1X/08c2f8d3ff1b67dd45fab4b67fdf3b4d2c5b6d27.gif" width="400"/>

----------
### <span style="color:navy;">2022/6/10</span> [ABBロボットROS2ドライバー](https://discourse.ros.org/t/a-ros2-driver-for-abb-manipulators/25990)

- PickNikRoboticsとOptimaxSystemsInc.がABBロボットのROS2ドライバをリリース
- 2つの異なるシミレーションモード
- ROSでのシミュレーション用にros2_controlドライバーをエミュレート
  - ABB独自のRobotStudioソフトウェアと通信
  - IRB 1200-5/0.9マニピュレーター対応
- GitHub
  - https://github.com/PickNikRobotics/abb_ros2
  
- おまけ
  - TurtleBot3 ROS2 Humble対応
  - https://github.com/ROBOTIS-GIT/turtlebot3

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/optimized/2X/5/56dddad54409be2326678cf5e14b2e55995168b0_2_676x500.png" width="400"/>

----------
### <span style="color:navy;">2022/04/11</span> [(ROS NEWS 4/11より) あなたのパッケージをROS2へアップグレードしてください！！（ROS2移行の呼びかけ？）](https://docs.ros.org/en/foxy/Contributing/Migration-Guide.html)

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/e/e4fbcda6004cfa1bd38e8f01595d22623da86f84.png" width="400"/>

----------
### <span style="color:navy;">2022/04/13</span> [Open Roboticsの求人](https://discourse.ros.org/t/multiple-positions-at-open-robotics/25154)

- Open Robotics: 企業、アカデミック、政府と協力してロボットOSS・ハード開発をサポート
- 開発対象
  - ROSコア
  - Gazebo
  - Open-RMF
  - 一般的なメッセージインターフェイスおよび関連する動作
- オフィス
  - マウンテンビュー、カリフォルニア、シンガポール
- 職種
  - DevOpsエンジニア：Linux / Cloud
  - ソフトウェアエンジニア：ロボット工学
  - ソフトウェアWebエンジニア：フロントエンド開発者


<img src="https://www.robotics247.com/images/article/Open_RMF_floors.png" width="400"/>


----------
### <span style="color:navy;">2022/04/13</span> [New Ignition releases 2022-04-13 (Fortress, Edifice)](https://community.gazebosim.org/t/new-ignition-releases-2022-04-13-fortress-edifice/1367)

- Edifice終了→Fortressへ
- ハイライト
  - オンデマンドで画像キャプチャが可能にIMUセンサは任意の参照フレームでプリセットをサポート
  - センサは実行時に有効・無効にできる
- Ignition Gazebo 6.8.0
  - 23のPR→様々な機能追加

<img src="https://global.discourse-cdn.com/standard10/uploads/gazebo/original/1X/fc2246f7777b1e607bfc6f5ccb53c01c66935bde.gif" width="400"/>

----------
### <span style="color:navy;">2022/04/11</span> [(ROS Newsより） Open Robotics の GoC (Google Summer of Code) のプロジェクトについて](https://github.com/osrf/osrf_wiki/wiki/GSoC)

- Project List
  - Gazebo and Ignition
    - Gazeboにおけるメッシュフォーマットのローディング機能のサポート
    - Ignition レンダリングライブラリをベースとしたrvizの開発
    - Mininet-WiFi Ignition
    - Texture Domain Randomization
    - 新しいignition projectのためのツール開発
- ROS2
  - Prototype multi-transport support in ROS 2
  - 現状ROS2では1つのロードされたRMW実装のみをサポートするが、同時に複数のトランスポート（ex. 共有メモリとDDS等）をサポートするようにする。
  - 予想サイズ350h
    - → OpenRTM2の相互運用機能と同じもの？

----------
### <span style="color:navy;">2022/04/21</span> [Nav2 (ROS2 navigation stack) と NVIDIA Isaac の統合](https://discourse.ros.org/t/integrating-nav2-navigation-stack-with-nvidia-isaac-ros-gems/25186)

- Nav2のNVIDIA Isaac Simへの統合
- NVIDIA Isaac Sim
  - 基盤：Omniverse
  - ロボティクス シミュレーション アプリケーション
  - 合成データ生成ツール
- IsaacSimとNav2を統合
  - NVIDIA Blog
  - https://developer.nvidia.com/blog/integrating-the-nav2-stack-with-nvidia-isaac-ros-gems/
  - フォークリフトのフォーク部分を画像認識：学習
  - フォークを回避して走行（コストマップへの反映）


<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/8/895d188275cfe3f8c8c02f6a80a844bdcc97f76c.png" width="400"/>
<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/d/dc08299c3c39be5287737370dee519bcd4b50bb6.png" width="400"/>

----------
### <span style="color:navy;">2022/04/12</span> [myCobot： オープンソース6自由度ロボットアーム](https://discourse.ros.org/t/mycobot-an-open-source-6-dof-robotic-arm-powered-by-ros/25084)

- myCobot: Elephantroboticsの小型ロボット
- GitHub: https://github.com/elephantrobotics
- 4つのバージョン
  - M5stack	
  - Raspberry Pi
  - Jetson Nano
  - Arduino
- Working range 280mm
- Payload 250g
- ROS1で動作、ROS2も準備中

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/0/097a6e777bc9341729de6052a7c6814bb1b608e8.gif" width="400"/>
<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/5/5e3501e053f02e73c747206941768699f0b87708.gif" width="400"/>

----------
### <span style="color:navy;">2022/03/17</span> [移動ロボット用におけるPTP（Precision Time Protocol）利用について](https://discourse.ros.org/t/experience-with-ptp-precision-time-protocol-for-mobile-robots/24707)

- Precision Time Protocol（IEEE 1588v2）
  - コンピュータネットワーク全体でクロックを同期させるために使用される通信プロトコル
  - マイクロ秒以下の精度のクロック同期できる
- 移動ロボットでPTPを使い始めたがうまく行かない
  - PTPは通常、有線接続を前提としている→移動ロボットはワイヤレス接続
  - ロボット間の時刻同期：NTPの10〜100ミリ秒の精度で一応はOK
  - ロボット内部の複数のコンピュター間：PTPによるマイクロ秒前後の同期が必要
    - センサフュージョン、etc.
  - NTPクライアント＝PTPマスター、PTP配下のノードはPTPマスターに動悸させたい
  - 問題
    - PTPはP2PまたはE2E (End to end) 遅延メカニズムを前提とする、P2Pは2台だけ、→E2E
    - スイッチ：小型の4ポートGbEハブ→PTPのP2P/E2Eクロックを透過するはず
    - NIC：パケットタイムスタンプをサポートするNICが必要だが、どれかわからない
    - PTP同期できたかどうか判断しロボットをスタートさせるのが難しい
- 回答
  - OusterLIDARでPTPを使用して10〜100us同期できた、GNSSクロックを使ったほうが簡単
  - 高い精度が必要な場合、ハードとファームの組み合わせでPTPを実装（ハード間の相互運用性検証が必要、コンピュータ、スイッチ、センサーがすべてHWでPTPをサポートするものが必要）
  - ソフトウェアPTPであれば特別なハードは不要（ただし10〜100us、かつジッタが大きい）
  - モジュラーロボット間での時刻同期についての論文
    - https://arxiv.org/pdf/1809.07295.pdf

----------
### <span style="color:navy;">2022/03/07</span> [Fusion2urfdに関するブログ記事](https://yoichi-41.hatenablog.com/entry/ros2_fusion2urdf)

Fusion360のモデルをfusion2urdfというツールを使ってURDFに変換しROS2でシミュレーションすることに関する日本語のブログ記事

- fusion2urdfを使って変換したモデルを動かすために気をつけること
- ROS2で、Fusion360で作ったモデルをurdfに変換して、シミュレーションを行う方法

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">ついにfusion2urdfを使って変換したデータがrviz2で動いた！ただし一緒にやってる友達の画面上で <a href="https://t.co/NvgyL5bgeJ">pic.twitter.com/NvgyL5bgeJ</a></p>&mdash; パスコンパス@C100土-西そ20b (@pscmps) <a href="https://twitter.com/pscmps/status/1500461954351386625?ref_src=twsrc%5Etfw">March 6, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

----------
### <span style="color:navy;">2022/03/07</span> [Micro-ROSを使って開発する理由](https://discourse.ros.org/t/what-is-the-convenience-of-building-a-system-based-on-micro-ros-compared-to-not-using-micro-ros/24504)

Micro-ROSを使って開発する理由についての質問と議論がROS Discourseにてありました。

- 質問
  - Arduinoベースでロボットを開発中
  - Micro-ROSを使うのと使わないのとの違いは？
  - ROS2を使わない場合でもMicro-ROSを使う理由は？
  - なにか適切なチュートリアルはありますか？
  - → ROS2、rviz, TF よくわからない
- 回答
  - Rviz→visualizationの部分を簡単にできるよ！
  - 組み込みでROS2を使うならMicro-ROSが必要、でもROS2を使わないのであればMicro-ROSもいらないのでは？
  - 通信部分が楽にできるよ
  - Micro-ROSはROSの起動機能をサポートしてないよ
  - Micro-ROSのデモあります↓
    - https://github.com/micro-ROS/micro-ROS_crazyflie_demo

<a href="https://micro.ros.org/"><img src="https://micro.ros.org/img/micro-ROS_big_logo.png" width="640"/></a>


----------


### <span style="color:navy;">2022/03/07</span> [ROSCon’22 Kyoto](https://discourse.ros.org/t/roscon-2022-call-for-proposals/24600)

- 開催日時: 10月19日〜21日＠京都
  - IROS2022 10/23〜10/27
- 現在Call for Contents中（〆切5/6、notification7/18）
  - Day 0: ワークショップ
  - Day1,2: 通常会議（講演）
    - 新しいパッケージ/フレームワーク
    - 既存のパッケージの洞察/改善
    - 独自のROS展開/ユースケースに関するケーススタディ
    - 特定のロボット、センサー、プラットフォームの開発
    - コンテスト/コラボレーション/イニシアチブ
    - 商業/研究/教育環境におけるROS
    - 標準/ベストプラクティス/開発ツール


<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/f/fbc30fe743c92971c0794aa143288f00784bf0bf.png" width="400"/>

----------
### <span style="color:navy;">2022/01/29</span> [HW IF ワーキング立ち上げに関する議論](https://discourse.ros.org/t/new-working-group-proposal-hardware-interface-working-group/23774)

- 一般的なメッセージインターフェイスおよび関連する動作
- 同じハードウェア上の複数のドライバーの統合
- メーカーによるデバイスへの組み込みリファレンス実装の開発
- 既存の適用可能な標準の統合/組み込み

- 成果物
  - ハードウェアタイプ/クラス別の上記のリファレンス実装
  - 既存の標準の組み込み
  - リファレンス実装を採用する際の障壁/OEMベンチマークの声
  - パイロットROS2実装

以上がSwRI/ROS-IのMatt R.から提案された


----------
### <span style="color:navy;">2022/02/11</span> [Ros2_control unsmooth motion](https://discourse.ros.org/t/ros2-control-unsmooth-motion/24301)

ROS2_controlの制御においてスムースでない動作が見られる問題についてのROS discourseのスレッド

- KUKA LBR をFast Robot Interfaceで制御
  - joint_trajectory_controller / JointTrajectoryController でMoveIt2で制御
  - Ros2_control制御周期200Hzまではなめらかだが、200Hz(5ms)を超えると軌道がなめらかではなくなる
  - → ruckig を使用して軌道平滑化をしている？
  - ROS1のros_controlではううまく言っている。
  - Ros2_control_nodeはRT_PREEMPT パッチでリアルタイム実行している。
  - 正弦波を入力すると0となる
- コメント・回答
  - Read/writeのようなブロッキング呼び出しはないか？
    - Sleepは削除した
  - control_msgs::action::FollowJointTrajectory を各ステップで送信してはいけない
  - position_controllers/JointGroupPositionController を変わりに使用してみては？
  - Ruckigはデフォルトでは使用されない
- 解決
  - position_controllers/JointGroupPositionControllerを使用し、ロボットのコントローラ周期とros2_controlの周期を合わせるとなめらかに動作した


----------
### <span style="color:navy;">2022/01/２８</span> [Open-RMF紹介](https://www.open-rmf.org/)

- Open Robotics Middleware Framework
  - ロボット相互運用のための共通フレームワーク
  - Webページ: https://www.open-rmf.org/ 
  - GitHubページ: https://github.com/open-rmf 
- ROS2ベースのロボットフレームワーク
  - 移動ロボット制御
  - フリートコントロール
  - 屋内外の複数の移動ロボット制御
  - タスクディスパッチャ
  - など
- 環境
  - Ubuntu 20.04
  - ROS2 Galactic
  - Gazebo 11.1.0

<img src="https://images.squarespace-cdn.com/content/v1/61db8bd1ef81823364c61569/1642406607420-IO4RMPEEM5HB8IY2H0KD/rmf-web+for+website.gif?format=2500w" width="800"/>


----------
### <span style="color:navy;">2022/01/19</span> [ROS 2 Embedded WG meetings](https://discourse.ros.org/t/ros-2-embedded-wg-meetings/15460)

- Micro-ROS official page
  - https://micro-ros.github.io/
- Embedded Working Group meeting #16 from January 2022
  - micro-ROS meets Azure RTOS IoT by Benjamin Cabé from Microsoft
    - Azure RTOS IoT: IEC 61508 SIL 4、IEC 62304 Class C、ISO 26262 ASIL D 認証取得済み
    - Thread, File, GUI, Network, USB等のコンポーネントを提供、多くのMCUをサポート
  - Learn about ROSbot XL: micro-ROS based autonomous robot platform by Dominik Nowak from Husarion
  - Latest enhancements
    - CAN/FD transport, Espressif ESP32S3 micro-ROS support,

<iframe width="560" height="315" src="https://www.youtube.com/embed/gpcbcitIcJI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

----------
### <span style="color:navy;">2022/01/25</span> [Get ROS2 Industrial Ready Online Workshop 2022](https://discourse.ros.org/t/final-call-for-participation-get-ros2-industrial-ready-online-workshop/23993)

- ROS2: 2023年までにROSを置き換える予定
  - 2022年2月21日−23日
- WS：対象者
  - 開発者・研究者、企業、エンジニア、ROS1→ROS2移行したい人
- トレーニング内容
  - ROS2でパッケージ、ノード、トピック、サービス、およびアクションを作成する方法
  - 新しいコルコンユニバーサルビルディングシステムの管理
  - ROS2Pythonのトピックパブリッシャーとサブスクライバー
  - ROS2のノードの管理：ライフサイクル、エグゼキュータ、コールバックグループ
  - ROS1およびROS2とのハイブリッドアプリケーション
  - ROS2でのデバッグツールの使用
  - ROS2ローカリゼーション
  - ROS2パスプランニング
  - ROS2マッピング
  - ROS2 + DDS
  - ROS2障害物回避
  - MoveIt2を使用したROS2アームの計画と把握
- 主催
  - Robotnik


![ros2industrialready](https://user-images.githubusercontent.com/11814060/181394596-01423741-bd51-4da2-bf6a-707a4925e79e.png)

-----------
### <span style="color:navy;">2022/01/21</span> [ROS2 Manipulation Basics](https://discourse.ros.org/t/new-ros-course-ros-2-manipulation-basics/23889)

- Construct社が提供するROSのMoveItのチュートリアルコース
  - コースの詳細ページ：https://www.theconstructsim.com/robotigniteacademy_learnros/ros-courses-library/ros2-manipulation-basics/ 
- コンテンツ
  - ROS2におけるMoveIt!パッケージ設定方法
  - C++でプログラムからROS2/MoveIt!使用方法
  - Visionを使用しROS2で赤い箱の座標を出力する方法
  - ROS2でピックアンドプレースタスクを実行する方法

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/0/0a8bc4e5c73de58ab81ff59b89c24727c2454ae0.jpeg" width="640" >

----------


### <span style="color:navy;">2021/11/17</span> [Remote Warehouse Real Robot Lab](https://discourse.ros.org/t/ros2-remote-warehouse-real-robot-lab-for-industrial-training/23139)

Construct+Robotnikによる、遠隔からリアルなロボットに接続して実験ができるラボ立ち上げのお知らせ。

- ROS1+ROS2で産業用物流ロボット用ラボを立ち上げ
- リモートからラボに接続して練習可能
- ROSスキルの習得、最新技術へのキャッチアップ等を目的とする
- 提供ロボットシステム
  - RB-1BASE移動ロボットで自律ナビゲーションの練習
  - UR3eを使用してPointCloud＋協働型アームによるマニピュレーションの練習

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/a/a05b97afb5557d357c0d0f51538488a9119c9bc1.jpeg" width="300"/>
<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/a/a05e6fc2e6f0267111dae8c4f3c1f82b32299832.jpeg" width="300"/>

<iframe width="560" height="315" src="https://www.youtube.com/embed/KjWX7M9SdFw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- [Construct](https://www.theconstructsim.com/)
- [Robotnik](https://robotnik.eu/)

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/0/0a8bc4e5c73de58ab81ff59b89c24727c2454ae0.jpeg" width="640" >

----------

### <span style="color:navy;">2021/11/8</span> [ROS2のmacOSサポート](https://discourse.ros.org/t/macos-support-in-ros-2-galactic-and-beyond/17891/32)

#### 課題

ROS2からは、macOSがTier1 platform (正式サポートOS) とされてきたが、以下のような課題があり、開発側はmacOSをTier1から外したいとの提案がある。 (2020年12月)
主な課題としては、

- SIP (System Integrity Protection) を無効にする必要がある
- RViz2やRQtは動作しない （Qtがうまく動かない）
- 依存パッケージをHomebrewのものを利用するとつらい→Homebrewの更新頻度が早い

#### 意見

- macOSの最小構成を提供してほしい(GUI抜き）
- Docker+novncクライアントを組み合わせてmacOSから使えば？
- M1 Macは非常に高速であり、ぜひ使いたい
- SIPに引っかかるため、回避が必要（方法はドキュメント化されている）
- M1 Big Surでrviz2が動作
  - [http://mamykin.com/posts/building-ros2-on-macos-big-sur-m1/](http://mamykin.com/posts/building-ros2-on-macos-big-sur-m1/)
- CycloneDDSはM1 Macをサポート、評価レポート↓
  - [https://osrf.github.io/TSC-RMW-Reports/humble/eclipse-cyclonedds-report.html#appendix-b-performance-summary-per-platform](https://osrf.github.io/TSC-RMW-Reports/humble/eclipse-cyclonedds-report.html#appendix-b-performance-summary-per-platform)
- 開発にAWS を使っている。Azureの場合Apple M1のAgentが無いのでコンパイルできない。

----------

### <span style="color:navy;">2021/10/30</span> [DDS for Unity](https://discourse.ros.org/t/dds-for-unity/22925)

DDS for Unity (OSS)が以下のサイトでリリースされている。
- [https://bitbucket.org/edhage/dds-for-unity/src/master/](https://bitbucket.org/edhage/dds-for-unity/src/master/)

DDS for UnityはUnityにDDS通信機能を追加するライブラリであり、もともとはUnityで作成されたデジタルツインとシミュレータをROS2と統合ゴするために作成された。

ROSにおいてシミュレータの一つとしてUnityを使用可能であり、Unity内のロボットに指令を送ったり、Unity内のカメラからjpeg-videoをROS2側にストリーミングすることなどが可能。

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/9/9b690cf58da01d76d3c9816a859d62df624e166c.jpeg" width="650"/>


----------


### <span style="color:navy;">2021/10/26</span> [ROS2の速度について](https://discourse.ros.org/t/ros2-speed/20162/15)

- **質問**

ROS1で9000Hzまで可能なpublisherが、ROS2では1000Hz以上速度が上がらない→ROS2の方が遅いのか？

- **回答**
- ROS2ではエグゼキュータがデータのpublishまでは行わないのでは？
- FastRTPSでは同期モードと非同期モードがある、CycloneDDSは同期モードのみサポート
- 実験例
  - ROS1: 1kHz, 650MB/s で送信可能
  - ROS2(CycloneDDS): 31Hz, 27MB/s
  - ROS2(FastRTPS):950Hz, 550MB/s, CPU使用率95%
- band幅測定ツールの提案あり
- 設定変更により改善
  - UDPソケットバッファを64MBに設定、MsgTypeをルーブ外で割当
  - Cycloneの場合MaxMessageSizeを大きな値に設定
  - 以上で、FastRTPS/Cycloneともｄにだいぶ早くはなる（でもROS1には及ばない）
  - [別スレッド参照：ROS2 default Behavior (Wifi)](https://discourse.ros.org/t/ros2-default-behavior-wifi/13460/37)
  - 固定長の16bytesほどのmsg→130kHz程度で送信可能
- CDRマーシャリングは可変長配列の場合ROS1のそれよりだいぶ遅い（プロファイラで検証）
- [マーシャリングが遅い問題はすぐには解決できないが、チューニングについてはドキュメント化](https://github.com/ros2/ros2_documentation/blob/rolling/source/How-To-Guides/DDS-tuning.rst)

#### 雑感
ROS2で使われている DDS (Data Distribution Service) は、さまざまなネットワークの状況に対応するため、さまざまな調整パラメータが存在し、望むパフォーマンスを引き出すためには、チューニングを施す必要がある。チューニング方法に関してはいかにまとめられている。

- [https://github.com/ros2/ros2_documentation/blob/rolling/source/How-To-Guides/DDS-tuning.rst](https://github.com/ros2/ros2_documentation/blob/rolling/source/How-To-Guides/DDS-tuning.rst)

ROS1は多くのユーザ環境では無調整でかなりのスループット性能が出、低レイテンシでの通信も可能であるため、DDSはパフォーマンスを上げるためには面倒なチューニングが必要。

DDSでは、データのシリアライズ（マーシャリングと呼ぶ）方法に、CORBAと互換な CDR (Common Data representation) 方式が利用されており、互換性やデータ形式の柔軟性のために、マーシャリングに時間がかかる問題がある。CORBAやDDSの実装によりそのパフォーマンスはさまざまであるが、いずれにしろ、処理的にはそこそこ重いものになっているのは事実。上記スレッドでも述べられている通り、通信ミドルウェアのコア部分であり、標準準拠の部分でもあるため、パフォーマンスの改善は容易ではない。

----------

### <span style="color:navy;">2021/10/16</span> [TSC meeting 10/28](https://discourse.ros.org/t/ros-2-tsc-meeting-minutes-2021-10-28/22947)

ROS TSC (Technical Steering Committee) ミーティングが10/28に開催されました。

- [Contribution Report](https://discourse.ros.org/uploads/short-url/setqXfGx9Z1dHh4DMU1rS0ePuq6.pdf)

Contribution Reportにおいては、ADLINK, Amazon, Apex.AI, Bosch, Canonical, eProsima, Intel, iRobot, LG, Microsoft, Open Robotics, PickNik, ROBOTIS, Rover Robotics, ROS-I, Samsung, Sony, GVSC, Royota RI, Wind River からのそれぞれのContributionのレポートが行われました。

#### WGレポート
各WGからは以下のような報告がなされました。

- Control→品質改善@Galactic, Foxy → Rollingへ
- Embedded→micro-ROS, embeddedRTPS
- Manipulatioin→Moveit2リファクタリング
- Middleware→ミーティング、QoSの課題、ROS_LOCALHOST_ONLYの実装方法
- Navigation→VSLAM統合、振る舞い実装方法の投票：BehaviorTreesが人気、Windows互換性が統合
- Rust→2種類のRust ROSクライアントライブラリの協力方法について議論
- Safety→Northstar Roboticsの安全管理ノード（認証品質）
- Tool→スナップショットメカニズム(ros2bag)完了→Rollingへ
- WrbTool→FoxgloveのROS2動作テストROS1からの移植

----------

### <span style="color:navy;">2021/10/16</span> [ROSConJPのビデオ・スライドが公開されました](https://roscon.jp/)

ROSCon JPは、ことしはリアルな会議として2021年9月16日(木)に東京で開催されました。
当日の発表の様子を撮影したビデオとスライドが[ROSConJPのページ](https://roscon.jp/)において公開されました。

<img src="https://roscon.jp/2021/img/ROSConJP21_lowres.jpg" width="400">



----------

### <span style="color:navy;">2021/9/24</span> [Intel Realsenseの代替カメラ？](https://discourse.ros.org/t/intel-cancelling-its-realsense-business-alternatives/21881)

[Intel Cancelling its Realsense business: Alternatives? ](https://discourse.ros.org/t/intel-cancelling-its-realsense-business-alternatives/21881) というトピックが ROS Discourseに上がっていました。

<img src="https://images.squarespace-cdn.com/content/v1/51df34b1e4b08840dcfd2841/1629316481122-3NO3JY5GJ8FBWPI8N3V6/depth-camera-d455-intel-realsense.jpg?format=500w" width="400">

Intel が最近 Realsense のサポートの終了を正式にアナウンスし、
Realsense を多用していたロボット業界などで波紋が広がっています。
ROSコミュニティでも、この発表を残念がっている人が多数いるようで、
このような[トピック](https://discourse.ros.org/t/intel-cancelling-its-realsense-business-alternatives/21881)が上がっています。

Realsenseのだいたいカメラとして上がっていたものは、

- Orbecc
- Ovc, https://github.com/osrf/ovc
- Kinect2.0, Azure Kinect
- ASUS XtionPro
- Ifm
- ZED
- MultiSense
- Ensenso

などが有り、価格と性能面で完全に Realsense の代替となるかは難しいかもしれません。
また、すでにいくつかのカメラは製造終了となっているものもあるようです。

また、ROS-Industrialでは以下のページで3Dカメラの情報を収集しているとのことで、
参考になりそうです。

- [ROS-i 3Dカメラリスト](https://rosindustrial.org/3d-camera-survey)
----------

### <span style="color:navy;">2021/9/16</span> [ROSCon JP](https://roscon.jp/)

ROSCon JP 2021 が76名の参加者、18社のスポンサーを集めて、
9月16日にオフライン開催されたとのことです。

<img src="https://roscon.jp/2021/img/ROSCon_JP_2021_group_photo_scaled.jpg" width="480">

発表スライドとビデオは10月中旬ごろにアップロードされるとのことです。

----------

### <span style="color:navy;">2021/9/24</span> [メールを使ってROS2メッセージを行うパッケージ: rmw_email](https://discourse.ros.org/t/ros-2-over-email-rmw-email-an-rmw-implementation/22360)

メールを使ってROS2メッセージ通信を行うパッケージ rmw_email が公開されています。
研究プロジェクトとして開発されたこのパッケージは、
ROS2で導入された通信ミドルウェア部分の抽象化が正しく機能するか、
について検証するために、実際にROS2のメッセージをメールとして送受信する
通信レイヤを実装したものです。

メッセージのレイテンシは実験結果から4秒から8秒だそうで実用的にはあまり意味がありませんが、
ROS2の抽象レイヤがちゃんと実装されていることの証左になりそうです。

<img src="https://christophebedard.com/assets/img/rmw-email/perf_comparison_nort.png" width="400">

なお、OpenRTM-aistでは、OMGの標準仕様レベルでポート間通信の抽象化がなされており、
共有メモリ通信、ダイレクト通信、MQTT、（廃止されましたが直接TCP通信）なども実装されてきましたが、
OpenRTM2.0からは、この仕組がより洗練され、ROSやROS2、UDP、などのプロトコルも
使用できるようになります。

- [GitHub](https://github.com/christophebedard/rmw_email)

----------

### <span style="color:navy;">2021/5月頃から</span> [ROS2移行戦略 (ROS discourseより)](https://discourse.ros.org/t/ros2-transition-strategy/9154)

- ROS-iからの問題提起
  - ROS1/2のリポジトリ構成について
  - 2つの方法案
    - Core,ros1ラッパー,ros2ラッパーを別々のリポジトリに配置
    - Core+ros1,core+ros2をブランチで管理
- 意見
  - 別々のコードベースを同一repoで管理すべきではない(ros1/ros2)
  - コアライブラリ＋ROSラッパー構成
    - 個別のリポジトリ(lib, ros1wrap, ros2warap)がいいのでは無いか？
    - 共有コードが多い場合→同一repoがいいのでは？
    - コア, ros1wrap/ros2wrap で分ける
  - ROS1/ROS2を共存させるときどうするか？
  - タグ(ros1_3.2.1, ros2_2.2.1)をつけては？
など、いろいろな意見がかわされていた。

----------

### <span style="color:navy;">2021/8/19</span> [ROSConは中止されROS World2021(バーチャル会議)開催](https://discourse.ros.org/t/roscon-2021-cancelled-ros-world-2021-announcement/21929)

ROSCon 2021は対面での通常開催が予定されていましたが、Covid-19の影響によりキャンセルされました。代わりに、仮想イベントとしてROS World2021が 10月20−21日に開催されることとなりました。
詳細

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/optimized/2X/1/1d816c0e182278141c88039ba5eb3435a2bdad39_2_500x500.png" width="400">

詳細は[こちらから](https://discourse.ros.org/t/roscon-2021-cancelled-ros-world-2021-announcement/21929)

----------

### <span style="color:navy;">2021/5月頃から</span> [ROS2移行戦略 (ROS discourseより)](https://discourse.ros.org/t/ros2-transition-strategy/9154)

- ROS-iからの問題提起
  - ROS1/2のリポジトリ構成について
  - 2つの方法案
    - Core,ros1ラッパー,ros2ラッパーを別々のリポジトリに配置
    - Core+ros1,core+ros2をブランチで管理
- 意見
  - 別々のコードベースを同一repoで管理すべきではない(ros1/ros2)
  - コアライブラリ＋ROSラッパー構成
    - 個別のリポジトリ(lib, ros1wrap, ros2warap)がいいのでは無いか？
    - 共有コードが多い場合→同一repoがいいのでは？
    - コア, ros1wrap/ros2wrap で分ける
  - ROS1/ROS2を共存させるときどうするか？
  - タグ(ros1_3.2.1, ros2_2.2.1)をつけては？
など、いろいろな意見がかわされていた。

----------

### <span style="color:navy;">2021/8/8</span> [ROS NEWS (ROS discourseより)](https://discourse.ros.org/t/ros-news-for-the-week-of-8-8-2021/21840)

- Rollingロゴ発表
<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/f/feac87b8a1623876569f1b6831c7e6f483608535.png" width="400">
- ROSConの早期登録まもなく終了
- 8/19 ROS-i会議
- 9/16 [ROSConJP](http://roscon.jp/)
- [9/21-24 ROS2-Industrial Training (Fraunhofer IPA)](https://www.ipa.fraunhofer.de/en/Events/2021/ros2-industrial_training.html)
- 10/21 [ROSCon](https://roscon.ros.org/)

----------


### <span style="color:navy;">2021/7/18</span> [ROSCon JPプログラムが公開されました](https://roscon.jp/)

ROSCon JPが2021年9月16日(木)に東京で開催されます。
すでにプログラムが発表されており、Apex.AI, Inc., Jan Becker氏による基調講演「自動車・スマート機器・IoTのためのROS 2に基づく安全認証取得済みフレームワーク」や、Samsung Research AmericaのSteve Macenski氏による基調講演「ROS 2のナビゲーションフレームワーク」など注目の講演が予定されています。
本NEDO特別講座のメンバーである、東京大学の岡田先生も「GGC (ガンダム GLOBAL CHALLENGE) リサーチ オープンシミュレータの開発と公開」について発表されます。
- [ROSCon JP 2021](https://roscon.jp)

<a href="https://roscon.jp"><img src="https://roscon.jp/2021/img/ROSConJP21_lowres.jpg" width="480"></a>

----------

### <span style="color:navy;">2021/7/8</span> [Rclshark](https://zenn.dev/array/articles/9fd8cb5941bb94)

ROS用WireShark?
ROS2において、headlessなボードCPUのIPアドレスを特定するツールとして、日本人が作者のrclsharkというツールが公開されています。
ROS2のDDSの仕組みを利用して、ROSノードのリストを探し出してIPアドレスを特定することができるようです。

<img src="https://storage.googleapis.com/zenn-user-upload/26e5cfa762e4cf736cb38559.png" width="800">

- [Zennページ](https://zenn.dev/array/articles/9fd8cb5941bb94)
- [Github](https://github.com/Ar-Ray-code/rclshark)

----------

### <span style="color:navy;">2021/7/2</span> [ROS2 メモリプロファイルレポート (Discourse)](https://discourse.ros.org/t/ros2-memory-usage-no-dds/21206)

(https://discourse.ros.org/t/ros2-memory-usage-no-dds/21206)

ROS2 Memory Usage (no DDS) というタイトルで、ROS2のDDS部分を除くメモリ使用量の分析レポートが7月2日に[投稿](https://discourse.ros.org/t/ros2-memory-usage-no-dds/21206)されていました。

#### ROS2 の基本メモリ使用量 ≒ ４MB
レポートでは、DDSのライブラリを除くROS2のベースとなるライブラリ (rclcpp.so) と pub/sub 機能が使用するメモリ使用量が約４MB、以降1ノードあたり約10kB程度のメモリ使用量増加が認められたと述べられています。

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/0/0d18d1ac0701ecd617982fe933d3bd3c9d77660b.png" width="480">

詳細は、[Discourse](https://discourse.ros.org/t/ros2-memory-usage-no-dds/21206)を御覧ください。

----------


### <span style="color:navy;">2021/6/9</span> [ROSビジュアライズ開発環境 Foxglove Studio (Discourse)](https://discourse.ros.org/t/foxglove-studio-blog-ros-tutorials-more/20838)

Foxglove が開発している Foxglove Studio が [Discourse](https://discourse.ros.org/t/foxglove-studio-blog-ros-tutorials-more/20838) で紹介されていました。
TypeScriptベースの今風なかっこいいビジュアルのツールです。画像、グラフ、LiDAR表示、トピック表示等、開発時・デバッグ時に必要そうなツールが一通り揃っているようです。
ブラウザ上でも動作する模様。

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/8/828faf17535d55ca9c089c007fac04d3095498e9.jpeg" width="800">

詳細は、[Discourse](https://discourse.ros.org/t/foxglove-studio-blog-ros-tutorials-more/20838)および、[公式サイト](https://foxglove.dev/) を御覧ください。

- [公式サイト](https://foxglove.dev/) 

----------

### <span style="color:navy;">2021/1/29</span> 「NEDO特別講座キックオフシンポジウム開催」
ロボット用ミドルウェア技術の普及・発展を推進する人材育成講座を開催するNEDO特別講座のキックオフシンポジウムを開催しました．<br/>
開催日：2021年1月29日（金）公開<br/>
開催方法：オンデマンド（動画配信ですので，29日以降時間を問わず視聴ができます）<br/>
内容：<br/>
（1）「ロボットのオープン化による市場化適用」　産総研，安藤慶昭様<br/>
（2）「市場化適用PJにおけるオープンソースプラットフォーム」東京大学　岡田慧先生<br/>
（3）ROSのビジネス応用事例の紹介：「オープンソース活用によるロボットSI効率化（仮題）」 KEBA Japan 株式会社　村上正和様<br/>
（4）「本特別講座の実施計画」 埼玉大学　琴坂信哉<br/>
視聴の登録は，本講座HP
-[https://robo-marc.github.io/](https://robo-marc.github.io/)まで．

<br/>
<br/>

- [Open Robotics and Canonical Announce ROS Extended Security Maintenance (ESM) ](https://www.openrobotics.org/blog/2021/4/5/hardened-ros-with-10-year-security-from-open-robotics-and-canonical]) 

----------

### <span style="color:navy;">2021/1/21</span> 「今週の海外ROSニュース」
海外の様々なROS関連のニュースをお伝えしていきます．

ROS News Letter
-[https://rosindustrial.org/news/2020/11/5/hbxkihnrz8hjiwidgr16m9hrd4faa7](https://rosindustrial.org/news/2020/11/5/hbxkihnrz8hjiwidgr16m9hrd4faa7)

本URLは「Collaborative Robot Sanding with ROS2 for Aerospace Applications」と題して、ROSの新製品を掲載しています。

論文紹介「ROS Based Safety Concept for Collaborative Robots in Industrial Applications」
-[https://link.springer.com/chapter/10.1007/978-3-319-21290-6_3](https://link.springer.com/chapter/10.1007/978-3-319-21290-6_3)

この論文では、ROSに基づいた協調ロボットの安全コンセプトに関する研究論文である。ROSをベースに衝突検知、経路計画、ロボット制御、行動予測のた
めのソフトウェアシステムの開発について述べています。
<br/>
<br/>

----------

### <span style="color:navy;">2021/1/14</span> 「今週の海外ROSニュース」
海外の様々なROS関連のニュースをお伝えしていきます．

Clearpath
-[https://clearpathrobotics.com/](https://clearpathrobotics.com/)
Clearpath社は，オフロード用の自律型ロボットシステムを設計しています。彼らのウェブサイトによると、この会社はROSの早期採用者であり、世界最大
のROS開発チームの1つである。このグループのアプリケーションは、測量・検査、鉱業、農業、防衛、マテリアルハンドリングなどです。
- [https://www.youtube.com/watch?v=nw67G8oflW0&feature=emb_title](https://www.youtube.com/watch?v=nw67G8oflW0&feature=emb_title)

このプロモーションビデオでは、既存のマイニングマシン（ホイールローダー）を最小限の改造で自律型ロボットに変換できるソフトウェアとハードウェ
アのパッケージを紹介していました。

Cyber-protection for the robot system
- [https://www.roboticstomorrow.com/news/2021/01/07/kaspersky-and-alias-robotics-enhance-protection-for-industrial-robots-/16084/](https://www.roboticstomorrow.com/news/2021/01/07/kaspersky-and-alias-robotics-enhance-protection-for-industrial-robots-/16084/)

カスペルスキー、エイリアスロボティクスとともに産業用ロボット向けのRIS（Robot Immune System）を開発中とのこと。
<br/>
<br/>


<img src="https://d3i71xaburhd42.cloudfront.net/8ea66e5c80705b09957caf2cf78b8041e7362a44/6-Figure7-1.png" width="200" style="float:right;margin-left:10px;margin-bottom:10px">
### <span style="color:navy;">2021/01/07</span> 「ROS2の性能分析論文」
Discourseで紹介されていた内容ですが、ROS2のパフォーマンス評価に関する論文が公開されています。
ROS1との比較や性能評価等の分析が含まれています。以下のリンクから無料で読むことができます。
- [https://dl.acm.org/doi/10.1145/2968478.2968502](https://dl.acm.org/doi/10.1145/2968478.2968502)

<br/>
<br/>

----------

### <span style="color:navy;">2020/11/10</span> 「ROS教育の提供を行う企業」

様々なROSの学習コースが用意されています。
また、無料で使えるROSの仮想実行環境のサービスもあります。
- [https://www.theconstructsim.com](https://www.theconstructsim.com)
  - 日本語の紹介： [https://anything-tm.hatenablog.com/entry/2019/04/12/090639](https://anything-tm.hatenablog.com/entry/2019/04/12/090639)

<br/>
<br/>

<img src="https://static.wixstatic.com/media/189b89_e726f7cc107a4f8f95166f01434b5014f000.jpg/v1/fill/w_529,h_480,al_br,q_80,usm_0.33_1.00_0.00/189b89_e726f7cc107a4f8f95166f01434b5014f000.webp" width="200" style="float:right;margin-left:10px;margin-bottom:10px">
### <span style="color:navy;">2020/10/12</span> 「SoftbankのROSで動く自律走行ロボットCuboid」
ROSで動作する自律走行ロボットです。具体的な用途への実証実験が始まっています。
研究開発用途にリースもされており、Githubにソースコードもあります。
- [https://www.signagekun.com](https://www.signagekun.com)
  - Github: [https://github.com/sbgisen/cuboid_sim](https://github.com/sbgisen/cuboid_sim)

<br/>
<br/>

<img src="https://chocolatey.org/content/images/icon_slogan.png" width="200" style="float:right;margin-left:10px;margin-bottom:10px">
### <span style="color:navy;">2020/10/08</span> 「ROSのWindows対応状況」
ROS (≠ROS2) のWindowsへの対応が進んでいます。
Windows用パッケージマネジメントシステム [「Chocolatey」](https://chocolatey.org/) を利用しており、
chocolateyのコマンドで以下のように簡単にインストールできるようになっています。

```bat
mkdir c:\opt\chocolatey
set ChocolateyInstall=c:\opt\chocolatey
choco source add -n=ros-win -s="https://aka.ms/ros/public" --priority=1
choco upgrade ros-foxy-desktop -y --execution-timeout=0
```
- [ROS Discourse](https://discourse.ros.org/t/ros-on-windows-foxy-release-v20200912-0-0-2009161641/16436)


