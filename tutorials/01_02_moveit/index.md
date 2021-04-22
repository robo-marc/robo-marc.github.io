# MoveIt!体験コース

<!-- TOC -->

- [1. コース概要](#1-コース概要)
    - [1.1. 受講方法](#11-受講方法)
    - [1.2. ISOイメージのダウンロードとVMwareのセットアップ](#12-isoイメージのダウンロードとvmwareのセットアップ)
    - [1.3. USBメモリからの起動について](#13-usbメモリからの起動について)
- [2. 講習会視聴リンクおよび資料](#2-講習会視聴リンクおよび資料)
    - [2.1. コース動画](#21-コース動画)
        - [第1部](#第1部)
        - [第2部](#第2部)
        - [第3部](#第3部)
    - [2.2. 資料](#22-資料)
    - [2.3. 参考資料](#23-参考資料)
- [3. アンケートご協力のお願い](#3-アンケートご協力のお願い)

<!-- /TOC -->

<br/>

## 1. コース概要
本コースは2020年12月19日にオンラインにて開催された講習会を録画編集したものです。
NEDO「ロボット活用型市場化技術開発プロジェクト（市場化プロジェクト）」(2017－2019年度)において開発された，ロボット共通ソフトウェアのUSB実行環境を活用して，いくつかのタイプのロボットアームをMoveIt!を用いて制御し，何らかの作業を行うロボットシステムとしてインテグレーションする方法について学ぶことができます．

### 1.1. 受講方法

講習会受講にあたって，以下のものをご準備ください．
- PC
  - ノートPC，デスクトップPCいずれでも構いません．
  - あまり古いPC，遅いPCは適しません (Core-i3以上，メモリ8GB以上が適当でしょう)
  - ISOイメージ（5GB程度)をダウンロードするため，十分なディスク容量があることを確認してください．
  - 以下のUSBメモリを自分でセットアップする場合はHDD/SSD容量 64GB 以上の空きが必要になります．

### 1.2. ISOイメージのダウンロードとVMwareのセットアップ

本コースでは，ISOファイルをVMware上でLive実行する形式で行います．
以下の開設に従って，講習会に使用するISOイメージをダウンロードし
VMwareなどから起動できるように前もってご準備ください．

- [ISOイメージ・VMwareのセットアップ](/tutorials/vmware_howto)

### 1.3. USBメモリからの起動について

USBメモリから起動してUbuntu環境を利用することができます．
以下の2種類の起動可能なイメージを用意しています．（講習会ではISOイメージを使用）

- Ubuntu 18.04 + ROS Melodic (duAro, NEXTAGEのみ同梱)
  - [DVD用ISOイメージ](https://openrtm.org/pub/NEDO_tutorial/ubuntu-18.04.5-nedo_marc-v2-desktop-amd64.iso) (約5GB)
  - MD5 SUM: 383e48206736f81e7142473d564e3bee
- Ubuntu 16.04 + ROS Kinetic版 (duAro, SeedNoid, NEXTAGE等すべて含まれます)
  - [USBメモリイメージ (7zip圧縮)](https://openrtm.org/pub/NEDO_tutorial/NEDO_USB_Image.7z) (約25GB)
  - MD5: cfd74c56ccd71db1ad046e955a83f538
  - 32GBバイトUSBメモリ用イメージのため非常に大きなファイルです

いずれの場合も，USBメモリに書き込む際は以下のマニュアルをお読みください．

- [起動可能なUSBメモリ作成方法](/tutorials/usbimage_howto)


<br/>

## 2. 講習会視聴リンクおよび資料

### 2.1. コース動画

本コースの詳細な内容は以下のWebページ解説を御覧ください。
- [NEDO特別講座 ROS MoveIt! チュートリアル](https://robo-marc.github.io/moveit_tutorial/)

#### 第1部
<iframe width="560" height="315" src="https://www.youtube.com/embed/Lfk9ee1ZEJQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- [(Webページレジュメ) ROSの概要](https://robo-marc.github.io/moveit_tutorial/ros_overview)

<a href="https://www.youtube.com/watch?v=Lfk9ee1ZEJQ"><img src="/figs/youtube_button.png" width="100"></a>


#### 第2部
<iframe width="560" height="315" src="https://www.youtube.com/embed/VH6bRA_xYFM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- [(Webページレジュメ) NEDO ROSセット 基本設定](https://robo-marc.github.io/moveit_tutorial/rosset_setting)
- [(Webページレジュメ) NEDO ROSセット シミュレータの利用](https://robo-marc.github.io/moveit_tutorial/rosset_simulator)

<a href="https://www.youtube.com/watch?v=VH6bRA_xYFM"><img src="/figs/youtube_button.png"  width="100"></a>


#### 第3部
<iframe width="560" height="315" src="https://www.youtube.com/embed/rR0K8hrqg1M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

- [(Webページレジュメ) MoveIt!プログラミングの基礎](https://robo-marc.github.io/moveit_tutorial/program_basic)

<a href="https://www.youtube.com/watch?v=rR0K8hrqg1M"><img src="/figs/youtube_button.png"  width="100"></a>


### 2.2. 資料

<iframe src="//www.slideshare.net/slideshow/embed_code/key/nTGHpap4AdLJzZ" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen></iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/NoriakiAndo/nedo-1" title="NEDO特別講座 ロボット共通プラットフォーム講習会 (1)" target="_blank">NEDO特別講座 ロボット共通プラットフォーム講習会 (1)</a> </strong> from <strong><a href="https://www.slideshare.net/NoriakiAndo" target="_blank">NoriakiAndo</a></strong> </div>

### 2.3. 参考資料

NEDO市場化プロジェクトでは，ROSおよびMoveIt!をインストールせずに試用できるUSBメディアを開発しました．
本講習会では，これを用いて実習を行います．USBメディアはこのページからインストールできるように準備いたしますので，今しばらくお待ち下さい．

また，講習の内容は以下のTorkのMoveIt! Tutorial に準じますが，NEDO市場化プロジェクトで開発された，
川崎重工のduAroをベースにそのシミュレータ上での動かし方を中心に解説します．

Tork制作のMoveIt! チュートリアルは以下のページにありますので，事前に目を通しておくことをおすすめします．

- [Tork MoveIt! チュートリアル 0.0.10 for Kinetic](https://github.com/tork-a/tork_moveit_tutorial/releases/download/0.0.10/tork_moveit_tutorial-kinetic-0.0.10.pdf)

<br/>

## 3. アンケートご協力のお願い

本コースをご視聴いただきありがとうございました。
お手数ですが、今後のコース改善のため以下のアンケートにご協力いただければ幸いです。

<div align="center"><a href="https://docs.google.com/forms/d/e/1FAIpQLScdiVxfeDrkS1O6GVAXZ2j-c5pjEFQPwbeVmjh1rdLB4bX2bA/viewform"><img src="/tutorials/figs/enquete_button.png"></a></div>
