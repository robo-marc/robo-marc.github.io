# VMware を用いてNEDO ROSセットを起動する

## VMware Workstation Player

VMware Workstation Player (以下VMware Playerと略します) は、
VMware社から販売されている仮想化ソフトウェアの一つです。

VMware Playerは、非商用利用に限って無償で利用することができます。

Windows上でROSがインストールされたNEDO ROSセットを起動する方法
としては一番おすすめの方法です。

以下では、VMware PlayerをWindows PCにインストールして、
VMware Player上でNEDO ROSセットを起動する方法を説明します。

なお、すでにVMwareをお持ちの場合は、改めてVMware Playerをダウンロード・
インストールする必要はありません。有償のVMware Workstationを代わりに
利用することができます。

### VMware Workstation Player のダウンロード

WMware Workstation Playerは以下のページからダウンロードできます。
Windows用とLinux用があります。

- [VMware Workstation Playerのダウンロード](https://www.vmware.com/jp/products/workstation-player/workstation-player-evaluation.html)

<a href="https://www.vmware.com/jp/products/workstation-player/workstation-player-evaluation.html" align="center"><img src="figs/vmware_download.png"></a>
<div style="text-align: center;">クリックするとダウンロードページに飛びます</div>

ここからVMware Workstation Player をダウンロードしてください。

### VMware Workstation Player のインストール

Windowsでのインストール方法を説明します。
ダウンロードしたインストーラを起動すると、
以下のような画面が現れてインストールが開始されます。

<img src="figs/vmware_installer.png" align="center">

特に注意する点はなく、指示通りに進めるとインストールは完了します。

## ISOイメージからの起動
### ISOイメージのダウンロード

次に、以下のURLからNEDO ROSセットのISOイメージをダウンロードします。

- [ubuntu-18.04.5-nedo_marc-v2-desktop-amd64.iso](https://openrtm.org/pub/NEDO_Tutorial/ubuntu-18.04.5-nedo_marc-v2-desktop-amd64.iso)
  - ファイルサイズ: 4.74 GB (5,092,319,232 バイト)
  - MD5 SUM: 383e48206736f81e7142473d564e3bee
  - MD5SUMの確認の仕方は後述します

ダウンロード後、ファイルサイズが上記と同じになっているか確認してみてください。
ファイルサイズが同じであればたいていの場合は問題なくダウンロードできています。
上記のMD5 SUMというのはファイルのハッシュ値です。もし、VMwareでうまく起動できない場合は、
次の方法でファイルが正しくダウンロードできているか確認することもできます。

#### MD5 SUM の確認の仕方

サイズが大きいファイルをダウンロードした場合、ファイルが破損している場合がまれにあります。
もし、うまく起動しない場合は、以下の方法でファイルに誤りがないかご確認ください。

Windowsの場合は、エクスプローラーでISOファイルをダウンロードした
フォルダを開きます。エクスプローラのアドレスバーに **cmd** と入力して
Enterを押してください。

<img src="figs/open_cmd.png" align="center" border="1">


そうすると、そのフォルダの位置でコマンドプロンプトを開きます。
次に、以下のコマンドを入力します。

```
C:\temp>certutil -hashfile ubuntu-18.04.5-nedo_marc-v2-desktop-amd64.iso MD5
```
MD5 SUMを計算するのには数分程度時間がかかります。しばらくすると、
以下のような表示とともに、MD5 SUMが出力されます。

<a href="figs/md5_cmd.png"><img src="figs/md5_cmd.png" align="center"></a>
<div style="text-align: center;">クリックすると拡大します</div>

出力されたMD5 SUMの値が、上記の値と同じか確認してください。
MD5 SUMの値が異なる場合は、ファイルが壊れていますので破棄して
再度ダウンロードしてください。


### VMware 仮想マシンの作成とISOイメージの起動

VMware Player を起動します。スタートメニューから VMware Workstation 16 Player
を起動するか、スタートメニュー横の検索窓で vmware などと入力すると、
候補に VMware Workstation 16 Playerが現れますので、クリックして起動します。

<img src="figs/vmware_startng_vmware.png" align="center">

以下のようなVMwareの画面が出ますので、右側の **「新規仮想マシンの作成(N)」**
をクリックして、新規の仮想マシンを作成します。

<img src="figs/vmware_opend.png" align="center">

新規仮想マシン作成ウィザードが表示されますので、
- **インストーラディスクイメージファイル(M)(iso):** をクリックし
- **「参照(R)」** ボタンをクリックし、先ほどダウンロードした iso イメージファイルを選択
します。すると以下のような画面になるはずです。

<img src="figs/vmware_select_iso.png" align="center">

**「次に」** ボタンをクリックし、ゲストOSの種類を選択します。
以下のように、
- ゲストOS: **"Linux"**
- バージョン: **"Ubuntu 64 ビット"**
を選択します。

<img src="figs/vmware_select_os.png" align="center">

**「次に」** ボタンをクリックし、仮想マシン名を付けます。
マシン名は何でも結構ですが、ここでは、 **"NEDO講座ROSセット"**
という名前にしておきます。

<img src="figs/vmware_vmname.png" align="center">

**「次に」** ボタンをクリックすると、以下のように仮想ディスクサイズを尋ねてきます。
今回はLive CDイメージを利用するので、ディスクは使用しませんが、デフォルトのままにして
次に進みます。

<img src="figs/vmware_disksize.png" align="center">

**「次に」** ボタンをクリックすると、以下のように準備完了と表示されますが、
ここで、ハードウェアを少しカスタマイズしておきます。
**「ハードウェアをカスタマイズ(C)...」** をクリックします。

<img src="figs/vmware_finish.png" align="center">

すると、以下のように仮想マシンをカスタマイズする画面が表示されます。

<img src="figs/vmware_customize.png" align="center">

ここで、メモリを可能であれば 4GB に増やしておきます。
ホスト側 (今使っている)PCのメモリに余裕があれば(16GB以上)、8GBに増やしてもよいでしょう。
逆に、ホスト側のメモリに余裕がない(4GBしか装着していないなど)場合は、2GBのままにしておいてください。
ただ、この場合、VMwareの動作が遅くなる可能性がありますので、できるだけスペックに余裕のあるPCを
使った方がよいでしょう。

設定を保存し、新規仮想マシン作成ウィザードの完了ボタンを押すと、準備完了です。
以下のような画面になっているはずです。

<img src="figs/vmware_ready.png" align="center">

仮想マシンの起動を押すと、仮想マシンが起動します。
順に以下のような画面が表示されます。起動には多少時間がかかりますので待ちます。
途中 Vmware Toolsのインストールをうな側れますが、無視してください。(「通知しない」ボタンをクリック)

<img src="figs/vmware_boot0.png" align="center">

<img src="figs/vmware_boot1.png" align="center">

<img src="figs/vmware_boot2.png" align="center">

最終的に以下のような画面が表示されます。
左側のリストの下の方に **「日本語」** がありますので、
選択し、**「Ubuntuを試す」**をクリックしてください。

<img src="figs/vmware_boot3.png" align="center">

その後、**Ubuntuへようこそ** という画面が表示されますので、
上部メニューの **Ubuntuへようこそ** から **終了** を選択します。

<img src="figs/vmware_boot4.png" align="center">

以下のUbuntu のデスクトップ画面が表示されたら準備完了です。

<img src="figs/vmware_boot5.png" align="center">

<!--
# Virtual Box を用いてNEDO ROSセットを起動する

# VirtualBox
## Virtual Box のダウンロード
## Virtual Box のインストール

# ISOイメージからの起動
## ISOイメージのダウンロード
## VMware 仮想マシンの作成とISOイメージの起動

-->


