## 概要
[メルカリ](https://www.mercari.com/jp/)から商品情報を取得します。

「メンズ新着アイテム」リンクページに遷移し、各アイテムのURL、商品名、価格の情報を取得します。  
取得した情報はCSV形式で保存します。

任意のページ数まで取得することが可能です。



## システム環境
以下で動作確認済みです。  
OS：macOS 10.15.6  
Python：3.6.9



## 実行方法
### ライブラリインストール
以下の2通りの方法がありますので、どちらかでインストールしてください。
```
$ pip install selenium
```
```
$ pip install -r requirements.txt
```


### ChromeDriverについて
ブラウザはGoogleChromeを使用します。  
ブラウザを自動操作するためにはChromeDriverが必要です。  
以下から自分のGoogleChromeと同じバージョンのドライバーをダウンロードします。  
[ChromeDriverのダウンロードはこちら](https://sites.google.com/a/chromium.org/chromedriver/downloads)


ChromeDriverをダウンロードしたら解凍して、任意の場所に配置します。  
そして、`chromedriver_path`のところに自分がダウンロードした場所を指定します。


### 取得するページ数を指定
`max_page`に取得するページ数を指定します。


### 実行
コマンドラインで実行します。
```
$ python scraping_mercari.py
```

<br>
<br>

詳細は[「Nakatatsu Blockchain Blog」](https://blog.nakatatsublockchain.com/)をご確認ください。
