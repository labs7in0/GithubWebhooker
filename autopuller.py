import web
import json, time, os
import threading
from apconfig import *

def worker(repo, submittime, committer): 
    tmp = os.popen('cd ' + repoList[repo][0] +  ' && git pull').readlines()
    output = open('./autopuller.log', 'a')
    output.write(time.strftime("\n[%Y-%m-%d %H:%M:%S]\n",time.localtime(time.time())))
    output.write("* Git returned: \n")
    output.writelines(tmp)
    output.write("* Repo: " + repo)
    output.write("\n* Branch: " + repoList[repo][1])
    output.write("\n* Dir: " + repoList[repo][0])
    tmp = os.popen(repoList[repo][2]).readlines()
    output.write("\n* Custom Command: \n")
    output.write(repoList[repo][2] + "\n* Shell Returned: \n")
    output.writelines(tmp)
    output.write("- Submitted by " + committer + " at " + submittime + "\n")
    output.close()

class index:
    def GET(self):
        return """
Service Running
Powered by Kinoware Github Autopuller.
"""

class showlogs:
    def GET(self):
        output = open('./autopuller.log', 'r')
        tmp = output.read()
        output.close()
        return tmp

class service:
    def POST(self):
        nowthetime = time.strftime("[%Y-%m-%d %H:%M:%S]",time.localtime(time.time()))
        para = web.input()
        value = json.loads(para.payload)
        repoName = value[u'repository'][u'name']
        if value[u'ref'] == 'refs/heads/' + repoList[repoName][1]:
            output = open('./autopuller.log', 'a')
            output.write("\n" + nowthetime + "\n")
            output.write("Repo: " + repoName)
            output.write("\n* Added: \n")
            output.writelines(value[u'head_commit'][u'added'])
            output.write("\n* Modified: \n")
            output.writelines(value[u'head_commit'][u'modified'])
            output.write("\n* Removed: \n")
            output.writelines(value[u'head_commit'][u'removed'])
            output.write("\n- Committer " + value[u'head_commit'][u'committer'][u'email'] + "\n")
            output.close()
            th = threading.Thread(target=worker,args=(repoName, nowthetime, value[u'head_commit'][u'committer'][u'email']))
            th.start()
            return "Succeed"
        return "Parameter Wrong"

urls = (
  '/', 'index',
  '/webhook', 'service',
  '/logs','showlogs'
)

app = web.application(urls, globals())

if __name__ == "__main__": app.run()
