---
layout: home
permalink: /

title: "NEDO ROBO-MARC"
excerpt: "NEDO ROBO-MARC (Robot Platformization) Project Web page"
#action: true
#action_btn:
#  - label: "Download"
#    fa_icon : "fas fa-download"
#    class: "btn btn-lg btn-success"
#    url: "https://github.com/manid2/lone-wolf-theme/releases/latest"
#  - dropdown: false
#  - dropdown_items:
#    - label: "v1.0.2"
#      url: "https://github.com/manid2/lone-wolf-theme/releases/tag/v1.0.2"
#      fa_icon: "fas fa-arrow-down"

feature_rows:
  - title: "Overview"
    excerpt: "Overview of the Project"
    url: "/project_overview/"
    img_path: "feature_rows/nedo-06.png"
    img_alt: "Overview of the Project"
  - title: "ROS NEWS"
    excerpt: "ROSおよびRTM関係のNEWS"
    url: "/rosnews/"
    img_path: "feature_rows/rosnews.png"
    img_alt: "ROS News"
  - title: "ロボット共通ソフトウェア技術講座"
    excerpt: "ロボット共通ソフトウェア技術講座"
    url: "/tutorials/list"
    img_path: "feature_rows/rt-software-course.png"
    img_alt: "ロボット共通ソフトウェア技術講座"
#  - title: "symposium2021"
#    excerpt: "Symposium 2021"
#    url: "/symposium2021/"
#    img_path: "feature_rows/sympo2021.png"
#    img_alt: "Symposium 2021"
#  - title: "News"
#    excerpt: "Nedo Project News"
#    url: "/newslist/"
#    img_path: "feature_rows/news.png"
#    img_alt: "News"


---

## NEDO特別講座

NEDO特別講座 (2020-2022年度) および、そのコアプロジェクト (NEDO ロボット活用型市場化適用技術開発プロジェクト (2017-2019年度) ) のページです。
本講座では、ROSなどのオープンソースソフトウェア（OSS）を活用したロボット用ミドルウェア技術の体験をはじめ、入門コース、産業用ロボット応用コース、画像処理・AI技術の活用コースなどのロボット用ミドルウェア技術を体系的に習得できる講義や演習を無料で提供します。

<!-- This is Web page to publish R&D result by “NEDO’s Technology Development Project for Robot Commercialization Applications” (FY2017-2019) and “NEDO Course (NEDO Kouza)”.-->

### SI2022 ロボット共通プラットフォーム講習会
本講習会では、市場化プロジェクトにおいて開発された、ロボット共通ソフトウェア実行環境を活用し、MoveIt!を用いて小型ロボットアームの実機を制御する方法について学ぶことができます。ご登録方法などの詳細につきましては、下記Webサイトをご参照ください。

<div align="center"><a href="/tutorials/si2022"><img src="/tutorials/si2022/si2022_banner_small.png" width="100%"></a></div>

<br/>

### NEDO講座 最終成果報告会
2020年6月からスタートしたNEDO特別講座における人材育成講座の成果を報告する最終成果報告会を開催いたします。ロボット共通ソフトウェア分野で先陣を切って活動している講師の方々をお招きして、本活動に関係するロボット用共通ソフトウェアの現状についてご紹介いただく予定です。

<div align="center"><a href="/symposium2023"><img src="/symposium2023/symposium2023.png" width="100%"></a></div>

<br/>

### ロボット共通ソフトウェア技術講座
<!-- 2021年3月26日より、NEDO特別講座が提供する「ロボット共通ソフトウェア技術講座」のオンデマンド配信を開始いたしました。-->
これまで事前登録が必要でした、「ロボット共通ソフトウェア技術講座」のオンデマンド配信を一般公開いたしました。
- [コース一覧](/tutorials/list)

<!-- div align="center"><a href="https://forms.gle/NKYo9Bmg5tibHNYq8"><img src="/tutorials/figs/button_regist_tiny.png" width="300"></a></div -->


### News

<div align="center"><img src="/figs/news-small.png" width="100%"></div>

<br/>

<div class="news">
<section>
  <ul>
  {% for post in site.posts limit:6 %}
    <li><a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
  </ul>
</section>
</div>
