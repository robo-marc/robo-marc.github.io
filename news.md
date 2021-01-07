* NEWS

このページでは、ROSやロボットミドルウェアに関するさまざまなニュースを発信しています。



** 2020/11/10 「ROS教育の提供を行う企業」

様々なROSの学習コースが用意されています。
また、無料で使えるROSの仮想実行環境のサービスもあります。
- https://www.theconstructsim.com
  - 日本語の紹介：https://anything-tm.hatenablog.com/entry/2019/04/12/090639
  
** 2020/10/12 「SoftbankのROSで動く自律走行ロボットCuboid」
ROSで動作する自律走行ロボットです。具体的な用途への実証実験が始まっています。
研究開発用途にリースもされており、Githubにソースコードもあります。
- https://www.signagekun.com
  - Github: https://github.com/sbgisen/cuboid_sim

** 2020/10/08 「ROSのWindows対応状況」
ROS (≠ROS2) のWindowsへの対応が進んでいます。
Windows用パッケージマネジメントシステム [「Chocolatey」](https://chocolatey.org/) を利用しており、
chocolateyのコマンドで以下のように簡単にインストールできるようになっています。

```bat
mkdir c:\opt\chocolatey
set ChocolateyInstall=c:\opt\chocolatey
choco source add -n=ros-win -s="https://aka.ms/ros/public" --priority=1
choco upgrade ros-foxy-desktop -y --execution-timeout=0
```
- https://discourse.ros.org/t/ros-on-windows-foxy-release-v20200912-0-0-2009161641/16436
