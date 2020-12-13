# VMware を用いてNEDO ROSセットを起動する

# Vmware Workstation Player
## VMware Workstation Player のダウンロード
## VMware Workstation Player のインストール

# ISOイメージからの起動
## ISOイメージのダウンロード

以下のURLからNEDO ROSセットのISOイメージをダウンロードします。

- [ubuntu-18.04.5-nedo_marc-v2-desktop-amd64.iso](https://openrtm.org/pub/NEDO_Tutorial/ubuntu-18.04.5-nedo_marc-v2-desktop-amd64.iso)
  - ファイルサイズ: 4.74 GB (5,092,319,232 バイト)
  - MD5 SUM: 383e48206736f81e7142473d564e3bee
  - MD5SUMの確認の仕方は後述します

ダウンロード後、ファイルサイズが上記と同じになっているか確認してみてください。
ファイルサイズが同じであればたいていの場合は問題なくダウンロードできています。
上記のMD5 SUMというのはファイルのハッシュ値です。もし、VMwareでうまく起動できない場合は、
次の方法でファイルが正しくダウンロードできているか確認することもできます。

## MD5 SUM の確認の仕方

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

<a href="figs/md5_cmd.pn"><img src="figs/md5_cmd.png" align="center"></a>
<span align="center>クリックすると拡大します</span>

出力されたMD5 SUMの値が、上記の値と同じか確認してください。
MD5 SUMの値が異なる場合は、ファイルが壊れていますので破棄して
再度ダウンロードしてください。


## VMware 仮想マシンの作成とISOイメージの起動

# Virtual Box を用いてNEDO ROSセットを起動する

# VirtualBox
## Virtual Box のダウンロード
## Virtual Box のインストール

# ISOイメージからの起動
## ISOイメージのダウンロード
## VMware 仮想マシンの作成とISOイメージの起動


