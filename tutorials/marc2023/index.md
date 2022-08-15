---
layout: page
---
# NEDO特別講座：ロボット共通プラットフォーム講習会


<!-- 本講習会は2020年12月19日にオンラインにて開催し、9名の受講者にお越しいただきました。ありがとうございました。-->

## 概要

NEDO「ロボット活用型市場化技術開発プロジェクト（市場化プロジェクト）」(2017－2019年度)において，ものづくり分野・サービス分野のロボット未活用領域に対しロボット導入を促進するため，ROS等のOSSを活用したロボット共通ソフトウェア技術の開発が行われました．プロジェクト終業後NEDOの後継事業として，2020年度からNEDO特別講座を立ち上げ，同技術の維持・普及・発展のための人材育成講座事業，人材交流事業，技術研究事業を進めています．
本講習会では，上記市場化プロジェクトにおいて開発された，ロボット共通ソフトウェアのUSB実行環境を活用して，いくつかのタイプのロボットアームをMoveIt!を用いて制御し，何らかの作業を行うロボットシステムとしてインテグレーションする方法について学ぶことができます．

### 主催
- NEDO (国立研究開発法人 新エネルギー・産業技術総合開発機構)

### 日時・場所
- 日時：2023年2月22日（水）13:00－15:55(予定)
- 場所：Zoomによるオンライン開催
- 聴講料：無料
<!-- - 参加者：9名，講師: 2名 -->
- 定員
  - 10名
  - ※ロボット (myCobot）を貸し出しますので人数に制限があることを予めご了承ください。
  - ※送料は、返送時のみご負担ください。
<!--
- 申し込み：（機材発送の都合上 12/12〆切とさせていただきます。）
  - 申込みは12月12日に締め切らせていただきました。
-->
- [登録フォーム (Google フォーム)](https://forms.gle/xaYXp54zz9urWLTC8)


# プログラム (予定)

本講習会は[NEDO特別講座 ROS MoveIt! チュートリアル](https://robo-marc.github.io/moveit_tutorial/)を使用して行います．

| 13:00-13:50 | NEDO市場化プロジェクトおよび[ROSの概要](https://robo-marc.github.io/moveit_tutorial/ros_overview) <br/> [レジュメ(PDF)](211218-01.pdf)|
| 14:00-14:50 | [NEDO ROSセット 基本設定](https://robo-marc.github.io/moveit_tutorial/rosset_setting) <br/> [レジュメ(PDF)](211218-02.pdf)<br/> [NEDO ROSセット シミュレータの利用](https://robo-marc.github.io/moveit_tutorial/rosset_simulator)|
| 15:00-15:55 | [MoveIt!プログラミングの基礎](https://robo-marc.github.io/moveit_tutorial/program_basic) |

<!--

## スライド
<iframe src="//www.slideshare.net/slideshow/embed_code/key/KLiujICoS2pgT8" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/openrtm/nedo-moveit-1" title="NEDO講座 MoveIt! チュートリアル 第1部" target="_blank">NEDO講座 MoveIt! チュートリアル 第1部</a> </strong> from <strong><a href="https://www.slideshare.net/openrtm" target="_blank">openrtm</a></strong> </div>
-->

# 事前準備

準備中

<!--
講習会受講にあたって，以下のものをご準備ください．

- PC
  - ノートPC，デスクトップPCいずれでも構いません．
  - あまり古いPC，遅いPCは適しません (Core-i3以上，メモリ8GB以上が適当でしょう)
  - ISOイメージ（5GB程度)をダウンロードするため，十分なディスク容量があることを確認してください．

  - 以下のUSBメモリを自分でセットアップする場合はHDD/SSD容量 64GB 以上の空きが必要になります．

### ISOイメージのダウンロードとVMwareのセットアップ

本講習会では，ISOファイルをVMware上でLive実行する形式で行います．
以下の開設に従って，講習会に使用するISOイメージをダウンロードし
VMwareなどから起動できるように前もってご準備ください．

- [ISOイメージ・VMwareのセットアップ](/tutorials/vmware_howto)

## USBメモリからの起動について

USBメモリから起動してUbuntu環境を利用することができます．
以下の2種類の起動可能なイメージを用意しています．（講習会ではISOイメージを使用）

- Ubuntu 18.04 + ROS Melodic
  - [DVD用ISOイメージ](https://openrtm.org/pub/NEDO_tutorial/ubuntu-18.04.5-nedo_marc-v2-desktop-amd64.iso) (約5GB)
  - MD5 SUM: 383e48206736f81e7142473d564e3bee
-->

<!--
- Ubuntu 16.04 + ROS Kinetic版 (duAro, SeedNoid, NEXTAGE等すべて含まれます)
  - [USBメモリイメージ (7zip圧縮)](https://openrtm.org/pub/NEDO_tutorial/NEDO_USB_Image.7z) (約25GB)
  - MD5: cfd74c56ccd71db1ad046e955a83f538
  - 32GBバイトUSBメモリ用イメージのため非常に大きなファイルです
-->

<!--
USBメモリに書き込む際は以下のマニュアルをお読みください．

- [起動可能なUSBメモリ作成方法](/tutorials/usbimage_howto)

# 参考資料
NEDO市場化プロジェクトでは，ROSおよびMoveIt!をインストールせずに試用できるUSBメディアを開発しました．
本講習会では，これを用いて実習を行います．USBメディアはこのページからインストールできるように準備いたしますので，今しばらくお待ち下さい．

また，講習の内容は以下のTorkのMoveIt! Tutorial に準じますが，NEDO市場化プロジェクトで開発された，
川崎重工のduAroをベースにそのシミュレータ上での動かし方を中心に解説します．


Tork制作のMoveIt! チュートリアルは以下のページにありますので，事前に目を通しておくことをおすすめします．

- [Tork MoveIt! チュートリアル 0.0.10 for Kinetic](https://github.com/tork-a/tork_moveit_tutorial/releases/download/0.0.10/tork_moveit_tutorial-kinetic-0.0.10.pdf)
-->

<!--
  
# 講習会の様子

<div align="center"><img src="si2021/si2021_galleryview.png" width="740"></div>
<br/>
<div align="center"><img src="si2021/si2021_moveit.png" width="740"></div>

-->
