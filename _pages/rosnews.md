---
layout: page
#title: Ros News
permalink: /rosnews/
#image: rosnews.png
---

# ROS Watch

このページでは、ROSやロボットミドルウェアに関するさまざまなニュースを発信しています。
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


