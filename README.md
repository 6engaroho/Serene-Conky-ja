# Serene-Conky-ja
serene-conkyを日本語化したものです。

# 主な変更点
時間、日付表示を日本語化しました。

conkyから呼び出されるPythonスクリプトをPython3で書き直しました。

天気予報のデータ取得先をyahoo!天気とlivedoor-Weather-hackに変更しました。

今日の出来事をWikipediaからxmlで取得します。これは起動時に一回だけ呼び出します。

名言集を"%"だけの行で区切られる（フォーチュンクッキー形式txt）から50個読み出し、ランダムに表示します。

# 起動
conkyはconky-allをインストールして下さい。

名言ファイルは好きなものを"meigen"というファイル名でDownloadsフォルダに入れて下さい。

pythonのモジュールは、
xml.etree.ElementTree as ET
urllib.request
など標準で入っていると思います。

４つの設定ファイル（co_main co_weather co_fact co_quote)の中の
minimum_size 1366 768
をディスプレイの解像度に合わせて書き換えて下さい。

main.luaの中の300行目あたり”downspeed","upspeed"の"(interface)"を、システムのネットワークインターフェイス名に書き換えて下さい。

Scripts/weather.pyの中の都市設定の部分をそれぞれのサイトで調べて書き換えて下さい。

フォルダ名を.conkyに変えるかstart.shをフォルダ名に合わせて下さい。
start.shに実行権限を与えて実行して下さい。

