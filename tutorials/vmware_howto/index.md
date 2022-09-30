---
layout: page
---

# VMware による NEDO ROSイメージの起動

NEDO特別講座で提供している起動可能なROS入りUbuntu LinuxのISOイメージ
(NEDO ROSイメージと呼びます) は、DVD-Rなどに書き込んでLive DVD (HDDに
インストールせずに利用する形態のDVD)として利用するものですが、仮想マ
シンを利用することで、WindowsやMac上でUbuntu Linuxを起動することがで
きます。講習会では、TV会議システムを利用しますので、TV会議システムは
Windows上で動作させたまま、仮想マシン上でROS入りUbuntu Linuxを動作さ
せることをお勧めします。

<!-- TOC -->

- [1. VMware Workstation Player](#1-vmware-workstation-player)
    - [1.1. VMware Workstation Player のダウンロード](#11-vmware-workstation-player-%E3%81%AE%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89)
    - [1.2. VMware Workstation Player のインストール](#12-vmware-workstation-player-%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
- [2. ISOイメージのダウンロードと確認](#2-iso%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8%E3%81%AE%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89%E3%81%A8%E7%A2%BA%E8%AA%8D)
    - [2.1. ISOイメージのダウンロード](#21-iso%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8%E3%81%AE%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89)
    - [2.2. MD5 SUM の確認の仕方](#22-md5-sum-%E3%81%AE%E7%A2%BA%E8%AA%8D%E3%81%AE%E4%BB%95%E6%96%B9)
- [3. VMware仮想マシンの作成と起動確認](#3-vmware%E4%BB%AE%E6%83%B3%E3%83%9E%E3%82%B7%E3%83%B3%E3%81%AE%E4%BD%9C%E6%88%90%E3%81%A8%E8%B5%B7%E5%8B%95%E7%A2%BA%E8%AA%8D)
    - [3.1. VMware 仮想マシンの作成 HDDにインストールしない場合](#31-vmware-%E4%BB%AE%E6%83%B3%E3%83%9E%E3%82%B7%E3%83%B3%E3%81%AE%E4%BD%9C%E6%88%90-hdd%E3%81%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%97%E3%81%AA%E3%81%84%E5%A0%B4%E5%90%88)
        - [3.1.1. NEDO ROSイメージの起動](#311-nedo-ros%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8%E3%81%AE%E8%B5%B7%E5%8B%95)
    - [3.2. VMware 仮想マシンの作成 HDDにインストールする場合](#32-vmware-%E4%BB%AE%E6%83%B3%E3%83%9E%E3%82%B7%E3%83%B3%E3%81%AE%E4%BD%9C%E6%88%90-hdd%E3%81%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B%E5%A0%B4%E5%90%88)
        - [3.2.1. NEDO ROSイメージの起動](#321-nedo-ros%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8%E3%81%AE%E8%B5%B7%E5%8B%95)
- [4. その他の仮想マシンプラットフォーム](#4-%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E4%BB%AE%E6%83%B3%E3%83%9E%E3%82%B7%E3%83%B3%E3%83%97%E3%83%A9%E3%83%83%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0)
    - [4.1. VirtualBox](#41-virtualbox)
    - [4.2. Parallels Desktop](#42-parallels-desktop)

<!-- /TOC -->

## 1. VMware Workstation Player

VMware Workstation Player (以下VMware Playerと略します) は、VMware社
から販売されている仮想化ソフトウェアの一つです。VMware Playerは、非
商用利用に限って無償で利用することができます。Windows上でROSがインス
トールされたNEDO ROSイメージを起動する方法としては一番おすすめの方法で
す。以下では、VMware PlayerをWindows PCにインストールして、VMware
Player上でNEDO ROSイメージを起動する方法を説明します。なお、すでに
VMwareをお持ちの場合は、改めてVMware Playerをダウンロード・インス
トールする必要はありません。有償のVMware Workstationを代わりに利用す
ることができます。

### 1.1. VMware Workstation Player のダウンロード

WMware Workstation Playerは以下のページからダウンロードできます。
Windows用とLinux用があります。

- [VMware Workstation Playerのダウンロード](https://www.vmware.com/jp/products/workstation-player.html)

<br/>
<div align="center">
<a href="https://www.vmware.com/jp/products/workstation-player.html">
<img src="figs/vmware_download17.png" width="800">
</a>
</div>
<div style="text-align: center;">クリックするとダウンロードページに飛びます</div>
<br/>

左上の「無償ダウンロード」ボタンを押すと以下のページに飛びます。

<br/>
<div align="center">
<a href="https://customerconnect.vmware.com/jp/downloads/info/slug/desktop_end_user_computing/vmware_workstation_player/16_0">
<img src="figs/vmware_download_page.png" width="800">
</a>
</div>
<div style="text-align: center;">クリックするとダウンロードページに飛びます</div>
<br/>

ここからVMware Workstation Player をダウンロードしてください。
2023年2月現在のバージョンは 16.2.5 です。


### 1.2. VMware Workstation Player のインストール

Windowsでのインストール方法を説明します。ダウンロードしたインストー
ラを起動すると、以下のような画面が現れてインストールが開始されます。

<br/>
<div align="center"><img src="figs/vmware_installler.png"></div>
<br/>

特に注意する点はなく、指示通りに進めるとインストールは完了します。

## 2. ISOイメージのダウンロードと確認

### 2.1. ISOイメージのダウンロード

次に、以下のURLからNEDO ROSイメージのISOイメージをダウンロードします。

<!--
- [ubuntu-18.04.5-nedo_marc-v2-desktop-amd64.iso](https://openrtm.org/pub/NEDO_tutorial/ubuntu-18.04.5-nedo_marc-v2-desktop-amd64.iso)
  - ファイルサイズ: 4.74 GB (5,092,319,232 バイト)
  - MD5 SUM: 383e48206736f81e7142473d564e3bee
-->

- [ubuntu-18.04.6-nedo-desktop-amd64_mycobot.iso](https://openrtm.org/pub/NEDO_tutorial/ubuntu-18.04.6-nedo-desktop-amd64_mycobot.iso)
  - ファイルサイズ: 約5GB (5,000,970,240 バイト)
  - MD5 SUM: 9c6ac7710109c1bfc6bc4bc214ff7b68

ダウンロード後、ファイルサイズが上記と同じになっているか確認してみて
ください。ファイルサイズが同じであればたいていの場合は問題なくダウン
ロードできています。上記のMD5 SUMというのはファイルのハッシュ値で
す。もし、VMwareでうまく起動できない場合は、次の方法でファイルが正し
くダウンロードできているか確認することもできます。

### 2.2. MD5 SUM の確認の仕方

サイズが大きいファイルをダウンロードした場合、まれにファイルが破損してい
る場合があります。もし、うまく起動しない場合は、以下の方法でファイルに誤
りがないかご確認ください。

Windowsの場合は、エクスプローラーでISOファイルをダウンロードしたフォ
ルダを開きます。エクスプローラのアドレスバーに **cmd** と入力して
Enterを押してください。

<br/>
<div align="center"><img src="figs/open_cmd.png" width="640" border="1"></div>
<br/>

そうすると、そのフォルダの位置でコマンドプロンプトが開きます。次に、
以下のコマンドを入力します。

```
C:\temp>certutil -hashfile ubuntu-18.04.6-nedo-desktop-amd64_mycobot.iso MD5
```
MD5 SUMを計算するのには数分程度時間がかかります。しばらくすると、
以下のような表示とともに、MD5 SUMが出力されます。

<br/>
<div align="center">
<a href="figs/md5_cmd.png"><img src="figs/md5_cmd.png" width="640"></a>
</div>
<div style="text-align: center;">クリックすると拡大します</div>
<br/>

出力されたMD5 SUMの値が、上記の値と同じか確認してください。MD5 SUMの
値が異なる場合は、ファイルが壊れていますので破棄して再度ダウンロード
してください。


## 3. VMware仮想マシンの作成と起動確認

ダウンロードしたISOイメージは、Live CDになっていますので、HDDにインス
トールせずに使用することもできます。あるいは、HDDにインストールして、恒
久的に使用することもできます。HDDにインストールした方が起動スピードなど
は若干速くなります。

ここでは、HDDにインストールしない場合を説明します。HDDにインストールする
場合は、[次の節](#32-vmware-%E4%BB%AE%E6%83%B3%E3%83%9E%E3%82%B7%E3%83%B3%E3%81%AE%E4%BD%9C%E6%88%90-hdd%E3%81%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B%E5%A0%B4%E5%90%88)に飛んでください。

### 3.1. VMware 仮想マシンの作成 (HDDにインストールしない場合)

VMware Player を起動します。スタートメニューから VMware Workstation 16
Playerを起動するか、スタートメニュー横の検索窓で vmware などと入力する
と、候補に VMware Workstation 16 Playerが現れますので、クリックして起動
します。

<br/>
<div align="center"><img src="figs/vmware_starting_vm.png" width="640"></div>
<br/>

以下のようなVMwareの画面が出ますので、右側の **「新規仮想マシンの作成(N)」**
をクリックして、新規の仮想マシンを作成します。

<br/>
<div align="center"><img src="figs/vmware_opened.png" width="495"></div>
<br/>

新規仮想マシン作成ウィザードが表示されますので、**あとでOSをインストール** をチェックし次に進みます。

<br/>
<div align="center"><img src="figs/vmware_install_later.png" width="495"></div>
<br/>

ゲストOSに **Linux**、バージョンに **Ubuntu 64ビット** が選択されていることを確認して次に進みます。

<br/>
<div align="center"><img src="figs/vmware_select_linux.png" width="495"></div>
<br/>

**「次に」** ボタンをクリックすると、以下のように仮想ディスクサイズ
を尋ねてきます。今回はLive CDイメージを利用するので、ディスクは使用
しませんが、デフォルトのままにして次に進みます。

<br/>
<div align="center"><img src="figs/vmware_disksize.png" width="495"></div>
<br/>

**「次に」** ボタンをクリックすると、以下のように準備完了と表示され
ますが、ここで、ハードウェアを少しカスタマイズしておきます。
**「ハードウェアをカスタマイズ(C)...」** をクリックします。

<br/>
<div align="center"><img src="figs/vmware_finish.png" width="495"></div>
<br/>

すると、以下のように仮想マシンをカスタマイズする画面が表示されます。

<br/>
<div align="center"><img src="figs/vmware_customize.png" width="819"></div>
<br/>

ここで、メモリを可能であれば 4GB 程度に増やしておきます。ホスト側 (今
使っている)PCのメモリに余裕があれば(16GB以上)、8GBに増やしてもよいで
しょう。逆に、ホスト側のメモリに余裕がない(4GBしか装着していないな
ど)場合は、2GBのままにしておいてください。ただ、この場合、VMwareの動
作が遅くなる可能性がありますので、できるだけスペックに余裕のあるPCを
使った方がよいでしょう。

#### 3.1.1. NEDO ROSイメージの起動

設定を保存し、新規仮想マシン作成ウィザードの完了ボタンを押すと、一旦以下
のメニュー画面が表示されます。

<br/>
<div align="center"><img src="figs/vmware_ready.png" width="642"></div>
<br/>

ここで、左のメニューから先ほど作成した仮想マシンを選択し、右下の **「仮想マシン設定の編集(D)」** をクリックします。

仮想マシン設定画面で、**CD/DVD(SATA)** を選択、**ISOイメージファイルを使
用する(M)** を選択、**参照(B)...** ボタンをおして、先ほどダウンロードし
たISOイメージを選択します。OKを押して、メインメニュー画面に戻ります。

<br/>
<div align="center"><img src="figs/vmware_set_isoimage.png" width="642"></div>
<br/>


仮想マシンの起動を押すと、仮想マシンが起動します。順に以下のような画
面が表示されます。起動には多少時間がかかりますので待ちます。途中
Vmware Toolsのインストールを促されますが、無視してください。(「通
知しない」ボタンをクリック)

<br/>
<div align="center"><img src="figs/vmware_boot0.png" width="642"></div>
<br/>

<br/>
<div align="center"><img src="figs/vmware_boot1.png" width="642"></div>
<br/>

<br/>
<div align="center"><img src="figs/vmware_boot2.png" width="642"></div>
<br/>

最終的に以下のような画面が表示されます。
左側のリストの下の方に **「日本語」** がありますので、
選択し、**「Ubuntuを試す」** をクリックしてください。

<br/>
<div align="center"><img src="figs/vmware_boot3.png" width="642"></div>
<br/>

その後、**Ubuntuへようこそ** という画面が表示されますので、
上部メニューの **Ubuntuへようこそ** から **終了** を選択します。

<br/>
<div align="center"><img src="figs/vmware_boot4.png" width="642"></div>
<br/>

以下のUbuntu のデスクトップ画面が表示されたら準備完了です。

<br/>
<div align="center"><img src="figs/vmware_boot5.png" width="642"></div>
<br/>

### 3.2. VMware 仮想マシンの作成 (HDDにインストールする場合)

VMware Player を起動します。スタートメニューから VMware Workstation 16
Playerを起動するか、スタートメニュー横の検索窓で vmware などと入力する
と、候補に VMware Workstation 16 Playerが現れますので、クリックして起動
します。

<br/>
<div align="center"><img src="figs/vmware_starting_vm.png" width="640"></div>
<br/>

以下のようなVMwareの画面が出ますので、右側の **「新規仮想マシンの作成(N)」**
をクリックして、新規の仮想マシンを作成します。

<br/>
<div align="center"><img src="figs/vmware_opened.png" width="495"></div>
<br/>

- **インストーラディスクイメージファイル(M)(iso):** をクリックし
- **「参照(R)」** ボタンをクリックし、先ほどダウンロードした iso イメージファイルを選択します。

<br/>
<div align="center"><img src="figs/vmware_select_iso.png" width="495"></div>
<br/>

すると以下のような画面になります。

- フルネーム: tork
- ユーザー名: tork
- パスワード: password
- 確認: password

と入力して次に進みます。

<br/>
<div align="center"><img src="figs/vmware_personalize.png" width="495"></div>
<br/>

**「次に」** ボタンをクリックし、仮想マシン名を付けます。マシン名は
何でも結構ですが、ここでは、 **"NEDO講座ROSイメージ"**という名前にして
おきます。

<br/>
<div align="center"><img src="figs/vmware_vmname.png" width="495"></div>
<br/>

**「次に」** ボタンをクリックすると、以下のように仮想ディスクサイズ
を尋ねてきます。今回はLive CDイメージを利用するので、ディスクは使用
しませんが、デフォルトのままにして次に進みます。

<br/>
<div align="center"><img src="figs/vmware_disksize.png" width="495"></div>
<br/>

**「次に」** ボタンをクリックすると、以下のように準備完了と表示され
ますが、ここで、ハードウェアを少しカスタマイズしておきます。
**「ハードウェアをカスタマイズ(C)...」** をクリックします。

<br/>
<div align="center"><img src="figs/vmware_finish.png" width="495"></div>
<br/>

すると、以下のように仮想マシンをカスタマイズする画面が表示されます。

<br/>
<div align="center"><img src="figs/vmware_customize.png" width="819"></div>
<br/>

ここで、メモリを可能であれば 4GB 程度に増やしておきます。ホスト側 (今
使っている)PCのメモリに余裕があれば(16GB以上)、8GBに増やしてもよいで
しょう。逆に、ホスト側のメモリに余裕がない(4GBしか装着していないな
ど)場合は、2GBのままにしておいてください。ただ、この場合、VMwareの動
作が遅くなる可能性がありますので、できるだけスペックに余裕のあるPCを
使った方がよいでしょう。

次に進むと、以下のようなインストール画面が表示されインストールが開始されます。

<br/>
<div align="center"><img src="figs/vmware_installing.png" width="819"></div>
<br/>

インストールにはしばらく時間がかかります。インストール終了後は、再起動してOSが起動することを確認してください。

#### 3.2.1. NEDO ROSイメージの起動

仮想マシンの起動を押すと、仮想マシンが起動します。順に以下のような画
面が表示されます。起動には多少時間がかかりますので待ちます。途中
Vmware Toolsのインストールを促されますが、無視してください。(「通
知しない」ボタンをクリック)

<br/>
<div align="center"><img src="figs/vmware_boot0.png" width="642"></div>
<br/>

<br/>
<div align="center"><img src="figs/vmware_boot1.png" width="642"></div>
<br/>

最終的に以下のような画面が表示されます。以下のUbuntu のデスクトップ画面が表示されたら準備完了です。（メニューは英語かもしれません。）

<br/>
<div align="center"><img src="figs/vmware_boot5.png" width="642"></div>
<br/>

## 4. その他の仮想マシンプラットフォーム

VMware の代わりに利用できる仮想マシンプラットフォームを紹介します。
これらの仮想マシンプラットフォームを利用してもISOイメージを起動して
講習会にて利用することができます。

利用の仕方は上述のVMwareとほぼ同じで、

1. 仮想マシンプラットフォームダウンロード
2. 仮想マシンプラットフォームインストール
3. ISOイメージダウンロード
4. 仮想マシンを新規に1つ作成
5. 仮想マシンのCDドライブにISOファイルを割り当て
6. 起動して利用

という手順となりますので、適宜それぞれの環境で読み替えて行ってみてください。

### 4.1. VirtualBox

VirtalBoxはOracleが無償で公開している仮想マシンプラットフォームです。
Windowsだけでなく、MacOS、Linuxの様々なディストリビューション等、
多くの環境で動作させることができます。

- [VirtualBoxダウンロード](https://www.oracle.com/jp/virtualization/technologies/vm/downloads/virtualbox-downloads.html)

VirtualBoxはMacOS上でも動作しますが、こちらで試した結果、ISOイメージ
を起動してもかなり動作が重く、操作に支障があるレベルでした。マシンス
ペックによってはスムーズに動作する可能性がありますが、その場合は、次
のParallels Desktopの14日間のトライアル版を利用することをお勧めしま
す。

### 4.2. Parallels Desktop

Parallels Desktopは Parallels社が販売しているMacOS専用の仮想マシンプ
ラットフォームです。Parallelsには14日間の無償トライアルプログラムが
用意されているので、講習会のために一次的に利用することができます。

- [Parallelsダウンロード](https://www.parallels.com/jp/products/desktop/trial/)

なお、Apple M1チップを搭載したMacBook Pro, MacBook Air, Mac miniでは
動作しませんのでご注意ください。
