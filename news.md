# ROS Watch

このページでは、ROSやロボットミドルウェアに関するさまざまなニュースを発信しています。

### <span style="color:navy;">2021/1/14</span> 「今週の海外ROSニュース」
海外の様々なROS関連のニュースをお伝えしていきます．

Clearpath (https://clearpathrobotics.com/)
Clearpath社は，オフロード用の自律型ロボットシステムを設計しています。彼らのウェブサイトによると、この会社はROSの早期採用者であり、世界最大のROS開発チームの1つである。このグループのアプリケーションは、測量・検査、鉱業、農業、防衛、マテリアルハンドリングなどです。
- [https://www.youtube.com/watch?v=nw67G8oflW0&feature=emb_title](https://www.youtube.com/watch?v=nw67G8oflW0&feature=emb_title)
このプロモーションビデオでは、既存のマイニングマシン（ホイールローダー）を最小限の改造で自律型ロボットに変換できるソフトウェアとハードウェアのパッケージを紹介していました。

Cyber-protection for the robot system（https://www.roboticstomorrow.com/news/2021/01/07/kaspersky-and-alias-robotics-enhance-protection-for-industrial-robots-/16084/）
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

