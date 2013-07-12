Kinoware-Github-Autopuller
========

This is a Python(web.py) project from Kinosang's Labs.

It can help you to auto deploy your codes on your Server when you commit changes to your Github Repository.

First, you should install web.py on your Server.
  * Please refer to http://webpy.org/install for more information.

Second, upload autopuller.py to your Server, and edit it.
  * Replace this line with your own code:
  * command = 'cd /Development/project1 && git pull git@github.com:username/repository'
  * 
  * /Development/project1 is the directory which you cloned from a Github repository
  * git@github.com:username/repository is the SSH clone URL of that repository

Third, run the Python Script.
  * You can type "python autopuller.py 9888" and press Enter to run the service on TCP 9888 Port

Fourth, setup webhook on Github
  * 1. Click "Setting" on the right of a repository page
  * 2. Click "Service Hooks"
  * 3. Click "WebHook URL" and input Yourdomain:9888/webhook
  * 4. Update settings

For more information, please visit http://www.kinosang.ws
