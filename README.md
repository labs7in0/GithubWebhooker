Kinoware-Github-Autopuller
========

這是由Kinosang's Labs開發的Python（Web.py）項目

本項目可以在您更新Github Repository時對您的程式進行自動部署

首先，您需要安裝web.py函式庫
  * 請移步 http://webpy.org/install 獲取更多信息

然後，上載本程式到您的伺服器并修改
  * 找到下面這行
  * command = 'cd /Development/project1 && git pull git@github.com:username/repository'
  * 其中：
  *   /Development/project1 是您已經檢出的Github Repository
  *   git@github.com:username/repository 是該Repository的SSH clone URL位址
  * 
  * 找到if value[u'ref'] == u'refs/heads/dev'，将將dev修改為您希望自動部署的branch

接著，執行本程式
  * 你可以通過在終端機中鍵入 "python autopuller.py 9888" 并敲擊歸位鍵讓本程式運行在TCP 9888連接埠上

最後，設置Github Webhook
  * 1. 按一下Response頁面右側的"Setting"
  * 2. 按一下"Service Hooks"
  * 3. 按一下"WebHook URL" 并鍵入 Yourdomain:9888/webhook
  * 4. 按一下"Update settings"

更多訊息請移步 http://www.kinosang.ws
