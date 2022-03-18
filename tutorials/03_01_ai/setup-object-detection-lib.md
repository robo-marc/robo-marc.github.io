---
layout: page
---
# 画像認識AI実行環境構築

下記の3つの物体検出モデルが実行できる環境を設定します。
+ YoloV4-tiny
+ SSD
+ SSD-mobilenetV2

## YoloV4-tiny
### コードと重みをリポジトリから取得します
```
git clone https://github.com/Tianxiaomo/pytorch-YOLOv4
cd pythorch-YOLOv4
mkdir weight
cd weight
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights
```

### デモスクリプトのGPUを無効にします
demo.pyを書き換えます
```
# use_cuda = True
use_cuda = False
```

### 動作確認を行います
成功すると検出結果がpredictions.jpgという名前で保存される。
```
# ライブラリインストール
pip3 install numpy
pip3 install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
pip3 install opencv-python
# 失敗するときはpip3 install --upgrade pipをすると解決するかもしれない。
# YoloV4-tinyのdemo実行
python3 demo.py -cfgfile cfg/yolov4-tiny.cfg -weightfile weight/yolov4-tiny.weights -imgfile data/dog.jpg
```

## SSD/SSD-mobilenetV2
### コードと重みをリポジトリから取得します
```
git clone https://github.com/lufficc/SSD
cd SSD
mkdir weight
cd weight

# 重みのダウンロード
wget https://github.com/lufficc/SSD/releases/download/1.2/vgg_ssd300_voc0712.pth
wget https://github.com/lufficc/SSD/releases/download/1.2/mobilenet_v2_ssd320_voc0712_v2.pth
```

### デモスクリプトのGPUを無効にします
demo.pyを書き換える
```
# device = torch.device(cfg.MODEL.DEVICE)
device = torch.device('cpu')
```

### 動作確認を行います
これを実行するとdemo/resultに検出結果の画像が出力される。
```
# ライブラリを追加でインストール
pip3 install vizer
pip3 install yacs

# SSD実行
python demo.py --config-file configs/vgg_ssd300_voc0712.yaml --images_dir demo --ckpt weight/vgg_ssd300_voc0712.pth
# SSD-mobilenetV2実行
python demo.py --config-file configs/mobilenet_v2_ssd320_voc0712.yaml --images_dir demo --ckpt weight/mobilenet_v2_ssd320_voc0712_v2.pth
```

以上
