Kinoware-Github-Autopuller
========

這是由Kinosang's Labs開發的Python（Web.py）項目

本項目可以在您更新Github Repository時對您的程式進行自動部署

首先，您需要安裝web.py函式庫
  * 請移步 http://webpy.org/install 獲取更多信息

然後，上載本程式到您的伺服器并修改
  * 請修改apconfig.py
  * repoList是已經檢出的Repository所對應相關設定，示例如下：
  * repoList = {
  *    'Repository1' : ['本地檔案夾1','Branch1','自定義SHELL1'],
  *    'Repository2' : ['本地檔案夾2','Branch2','自定義SHELL2']
  * }
  * 
  * 注：
  *     本地檔案夾1 即爲 Repository1 檢出後對應的本地檔案夾的絕對路徑
  *     Branch1 即爲 欲自動部署的 Repository1 的分支
  *     自定義SHELL1 即爲 執行完 git pull指令之後希望執行的SHELL指令

接著，執行本程式
  * 你可以通過在終端機中鍵入 "python autopuller.py 9888" 并敲擊歸位鍵讓本程式運行在TCP 9888連接埠上

最後，設定Github Webhook
  * 1. 按一下Response頁面右側的"Setting"
  * 2. 按一下"Service Hooks"
  * 3. 按一下"WebHook URL" 并鍵入 Yourdomain:9888/webhook
  * 4. 按一下"Update settings"

另外，使用 Yourdomain:9888/logs 可以快速查看伺服器日誌

本項目使用 GNU通用公共授權條款 （GPL）V3.0 進行許可，許可內容詳見license.md

更多訊息請移步 http://www.kinosang.ws
