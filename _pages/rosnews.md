---
layout: page
#title: Ros News
permalink: /rosnews/
#image: rosnews.png
---

# ROS Watch

このページでは、ROSやロボットミドルウェアに関するさまざまなニュースを発信しています。

----------

### <span style="color:navy;">2021/7/8</span> Rclshark

ROS用WireShark?
ROS2において、headlessなボードCPUのIPアドレスを特定するツールとして、日本人が作者のrclsharkというツールが公開されています。
ROS2のDDSの仕組みを利用して、ROSノードのリストを探し出してIPアドレスを特定することができるようです。

<img src="https://storage.googleapis.com/zenn-user-upload/26e5cfa762e4cf736cb38559.png" width="800">

- [Zennページ](https://zenn.dev/array/articles/9fd8cb5941bb94)
- [Github](https://github.com/Ar-Ray-code/rclshark)

----------

### <span style="color:navy;">2021/7/2</span> ROS2 メモリプロファイルレポート (Discourse)

(https://discourse.ros.org/t/ros2-memory-usage-no-dds/21206)

ROS2 Memory Usage (no DDS) というタイトルで、ROS2のDDS部分を除くメモリ使用量の分析レポートが7月2日に[投稿](https://discourse.ros.org/t/ros2-memory-usage-no-dds/21206)されていました。

#### ROS2 の基本メモリ使用量 ≒ ４MB
レポートでは、DDSのライブラリを除くROS2のベースとなるライブラリ (rclcpp.so) と pub/sub 機能が使用するメモリ使用量が約４MB、以降1ノードあたり約10kB程度のメモリ使用量増加が認められたと述べられています。

<img src="https://aws1.discourse-cdn.com/business7/uploads/ros/original/2X/0/0d18d1ac0701ecd617982fe933d3bd3c9d77660b.png">

詳細は、[Discourse](https://discourse.ros.org/t/ros2-memory-usage-no-dds/21206)を御覧ください。

----------


### <span style="color:navy;">2021/6/9</span> ROSビジュアライズ開発環境 Foxglove Studio (Discourse)

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


