---
layout: page
---
# 起動可能なUSBメモリ作成方法

NEDO講座等の講習会で配布する起動可能なUSBメモリは、自分で作成することができます。
ここでは、当サイトからイメージファイルをダウンロードし、起動可能なUSBメモリを作成する方法を解説します。
<!-- TOC -->

- [1. 概要](#1-概要)
- [2. USBメモリを準備する](#2-usbメモリを準備する)
- [3. イメージファイルのダウンロード](#3-イメージファイルのダウンロード)
    - [3.1. zipファイルの展開](#31-zipファイルの展開)
- [4. イメージ書き込みツールのダウンロード](#4-イメージ書き込みツールのダウンロード)
    - [4.1. Windows の場合](#41-windows-の場合)
    - [4.2. Macの場合](#42-macの場合)
    - [4.2. Linuxの場合](#42-linuxの場合)
        - [p7zip のインストール](#p7zip-のインストール)
        - [メモリイメージの展開](#メモリイメージの展開)
- [5. 起動準備](#5-起動準備)
    - [5.1. BIOS設定画面の起動](#51-bios設定画面の起動)

<!-- /TOC -->

## 1. 概要

起動可能なUSBメモリの作成手順は以下のとおりです。

- USBメモリを準備する
- USBに書き込むイメージファイルをダウンロードする
- イメージ書き込みツールをダウンロードする
- USBメモリにイメージファイルを書き込む
- 起動準備
- 起動確認

# 作成手順

## 2. USBメモリを準備する

まず、空のUSBメモリを用意します。
USBメモリのサイズは32GB以上のものをご用意ください。（当サイトで配布しているUSBメモリは32GB構成で作成されているため）

## 3. イメージファイルのダウンロード

まずはじめに、USBメモリに書き込むイメージファイルをダウンロードします。

- [USBメモリイメージファイル (7zip圧縮)](https://openrtm.org/pub/NEDO_tutorial/NEDO_USB_Image.7z) (約25GB)
  - MD5: cfd74c56ccd71db1ad046e955a83f538

イメージファイルはUSBメモリと同じサイズ、つまり32GB程度あるため、
ダウンロードするには相応の時間がかかります。
また、イメージファイルは圧縮されているため、ダウンロードして展開するためには
最低64GB程度のハードディスクの空き容量が必要になります。

### 3.1. zipファイルの展開

拡張子 **7z** のファイルは７ｚｉｐ形式で圧縮されているため、

- [7zip](https://sevenzip.osdn.jp/)
  - [7-Zip 19.00 ダウンロード](https://ja.osdn.net/dl/sevenzip/7z1900-x64.exe/)
  
等をダウンロードし、ファイルを展開してください。
展開すると、**NEDO_USB_Image.img＊＊ というファイルができます。

## 4. イメージ書き込みツールのダウンロード

### 4.1. Windows の場合

Windowsにおいては、起動可能なUSBイメージを書込み可能な様々なツールがありますが、ここでは
Rufus (ルーファス) を例に取り説明します。Rufusは以下のページからダウンロードできます。

- Rufus Webページ: [https://rufus.ie/](https://rufus.ie/)
  - Rufus 3.13: [rufus-3.13.exe](https://github.com/pbatard/rufus/releases/download/v3.13/rufus-3.13.exe)

Rufusはインストールの必要はありません。そのまま起動可能です。
起動すると以下のような画面が現れますので、

1. USBメモリを選択
2. 書き込むイメージファイル "NEDO_USB_Image.img" を選択
3. 状態を確認：「準備完了」ならOK
4. スタートボタンを押して書き込み開始


<img src="/tutorials/figs/Rufus_window.png" width="800" align="center">

書き込みを開始すると、以下の用にプログレスバーに書き込み完了までの時間が表示され、書き込み作業が進行します。
だいたい、20～30分程度かかるでしょう。気長に待ってください。

<img src="/tutorials/figs/Rufus_writing.png" width="434" align="center">

### 4.2. Macの場合

MacでUSBメモリにイメージを書き込むためには、新規にツールをインストールする必要はありません。
ただし、7zip圧縮ファイルを解凍するには、The Unarchiver をApp Storeからインストールしてください。

USBメモリをさすと、通常自動的にマウントされます。ターミナルを開いて、mountコマンドをうち確認します。

```
$ mount
/dev/disk1s1 on / (apfs, local, read-only, journaled)
devfs on /dev (devfs, local, nobrowse)
  : 中略
/dev/disk3s1 on /Volumes/USB DISK (msdos, local, nodev, nosuid, noowners)
$ 
```

USBメモリは **/dev/disk3** というデバイスで、
**/Volume/USB DISK** というディレクトリにマウントされていることがわかります。

イメージファイルを展開したディレクトリまで移動し、**dd** というコマンドで書き込みを行います。

```
$ diskutil umount /Volumes/USB\ DISK/ 
Volume USB DISK on disk3s1 unmounted
$ sudo dd if=NEDO_USB_Image.img of=/dev/rdisk3 bs=256m
Password:
120+0 records in
120+0 records out
32212254720 bytes transferred in 1175.989032 secs (27391629 bytes/sec)
$ 
```
一つずつ説明します。
1. diskutilコマンドでUSBメモリ (/Volume/USB DISKにマウントされている) をアンマウントする
2. ddコマンドを、入力(if)にイメージファイルを指定、出力(of)にUSBメモリデバイス /dev/rdisk3) を指定して起動
  - /dev/disk3ではなく、/dev/rdisk3とするのは、raw ディスクへの書き込みのほうが早いため
  - bs=256m はブロックサイズを256MBにする指定、ある程度大きくしておくとバッファリングされるので早く書き込める
3. ddコマンド終了
  - 終了すると書き込んだバイト数や時間などが表示され終了
4. USBメモリ抜いたら、起動させるPCに挿し起動させてみる

### 4.2. Linuxの場合

LinuxでUSBメモリにイメージを書き込むためには、新規にツールをインストールする必要はありません。
ただし、7zip圧縮ファイルを解凍するには、以下のように p7zip を apt などでインストールしてください。

#### p7zip のインストール
```
$ sudo apt install p7zip-full
パッケージリストを読み込んでいます... 完了
 : 略
p7zip-full (16.02+dfsg-6) を展開しています...
p7zip-full (16.02+dfsg-6) を設定しています ...
man-db (2.8.3-2ubuntu0.1) のトリガを処理しています ...
```

#### メモリイメージの展開

```
$ 7z x NEDO_USB_Image.7z 
 : 略
 Extracting archive: NEDO_USB_Image.7z
--
Path = NEDO_USB_Image.7z
Type = 7z
Physical Size = 26459537354
Headers Size = 146
Method = LZMA2:24
Solid = -
Blocks = 1

Everything is Ok         

Size:       32212254720
Compressed: 26459537354
```

USBメモリを挿入してください。その後コマンドラインから dmsg コマンドで認識状況を確認します。

```
[  788.812484] usb 1-13: new high-speed USB device number 2 using ehci-pci
  : 略
[  790.223535] sd 8:0:0:0: [sdb] 62914560 512-byte logical blocks: (32.2 GB/30.0 GiB)
[  790.227358] sd 8:0:0:0: [sdb] Write Protect is off
[  790.227361] sd 8:0:0:0: [sdb] Mode Sense: 43 00 00 00
[  790.231081] sd 8:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[  790.247648]  sdb: sdb1
[  790.255593] sd 8:0:0:0: [sdb] Attached SCSI removable disk
```
確認するポイントは
- USBメモリのサイズ → 上記では **[sdb] .... (32.2 GB/30.0 GiB)** の表示
  - 挿入したUSBメモリのサイズと合致しているか？
- **[sdb]** に相当するディスクファイル名
  - ここは sdc や sdd など sd+アルファベット一文字になっているはず
  - **注意** 通常 /dev/sda はシステムディスクに割り当てられています。/dev/sd? の代わりに /dev/sda を指定するとシステムが破壊されてしまいますのでご注意ください。

これで、このUSBメモリディスクは **/dev/sdb** というデバイスファイルからアクセスできることがわかります。
イメージファイルを展開したディレクトリまで移動し、以下のように **dd** というコマンドで書き込みを行います。

```
$ sudo dd if=NEDO_USB_Image.img of=/dev/sdb bs=32M
Password:
960+0 レコード入力
960+0 レコード出力
32212254720 bytes (32 GB, 30 GiB) copied, 1907.47 s, 16.9 MB/s
$ 
```
一つずつ説明します。
1. ddコマンドを、入力(if)にイメージファイルを指定、出力(of)にUSBメモリデバイス /dev/sdb) を指定して起動
  - bs=32M はブロックサイズを32MBにする指定、ある程度大きくしておくとバッファリングされるので早く書き込める
3. ddコマンド終了
  - 終了すると書き込んだバイト数や時間などが表示され終了
4. USBメモリ抜いたら、起動させるPCに挿し起動させてみる

なお、ddコマンドは起動後何も表示されず数10分程度待たされます。途中経過を知りたい場合は、別のターミナル画面から以下のように入力します。

```
$ pidof dd| sudo xargs kill -USR1
---------
ddコマンドの画面では以下のように表示される
27+0 レコード入力
27+0 レコード出力
7247757312 bytes (7.2 GB, 6.8 GiB) copied, 420.624 s, 17.2 MB/s
```


## 5. 起動準備

次にUSBメモリで起動させるPCの設定を行います。

### 5.1. BIOS設定画面の起動

まず、PCの電源を一旦切り、USBメモリをPCに挿入してからPCを再起動してみてください。
運よく、Linuxの起動画面が表示されたら、そのPCはUSBメモリからも起動するように設定さています。

もし、PCを再起動してもいつも通りに起動するようであれば、BIOSの設定からUSBからも起動するように設定する必要があります。
BIOS設定はPCによって様々ですが、以下では Panasonic Let's Note を例にとって説明します。

まず、電源投入直後に現れる画面で、以下のように **"Press F2 for Setup"** のようなメッセージが出ていないか確認します。
Let's Note では **"F2"** キーでBIOSセットアップ画面に入ることができます。

<img src="/tutorials/figs/biossetup_01.png" width="800" align="center">

以下のような画面が現れたら、起動またはBootと表示されているメニューがないか探してください。
この例では、**起動** メニューが上部に確認できます。

<img src="/tutorials/figs/biossetup_02.png" width="800" align="center">

横矢印 **→** キーで **起動**メニューに移動します。
画面に**UEFI**や**UEFI起動** といった項目がない確認してください。


<img src="/tutorials/figs/biossetup_03.png" width="800" align="center">

USBメモリから起動するにはUEFIによる起動を有効にする必要があります。
以下の例は、無効になっていたUEFI起動を有効にしているところです。
このほかに、起動するデバイスの順序を設定するメニューもあると思います。
そこで、普段起動しているハードディスクよりも、USBメモリまたは
UEFIデバイスからの起動の優先度を上げてあげる必要があるかもしれません。

<img src="/tutorials/figs/biossetup_04.png" width="800" align="center">

設定が終わったら終了メニューに移動します。
たいてい、設定を保存時して再起動するメニューがあるので、それを選択し再起動します。
再起動する前に、USBメモリを挿入しておいてください。

<img src="/tutorials/figs/biossetup_05.png" width="800" align="center">

USBメモリから起動すると、以下のようなUbuntu Linuxの GRUBの起動画面が表示されます。
メニューにはいくつか種類がありますが、Persistent と書かれている起動メニューは、
起動後のOS上で行った作業をUSBに保存することができるモードですので、
通常、講習会で利用する際にはこのモードを利用してください。

<a href="/tutorials/figs/ubuntu_boot_01.png"><img src="/tutorials/figs/ubuntu_boot_01.png" width="800" align="center"></a>


起動すると、以下のようなROSとTorkのロゴのデスクトップ壁紙と、デスクトップ上にKHI duAroや
THKのSeedNoid、富士ソフトのFSRoboおよびNEXTAGEのアイコンがデスクトップ上に確認できます。
この画面が出たら、起動可能なUSBメモリの作成は成功です。お疲れさまでした。

<a href="/tutorials/figs/ubuntu_boot_02.png"><img src="/tutorials/figs/ubuntu_boot_02.png" width="800" align="center"></a>

以上が、起動可能なUSBメモリの作成方法でした。



