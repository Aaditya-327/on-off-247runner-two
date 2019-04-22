#for on-off-247runner-two

first = ["gau-bot", "on-off-247runner-one"]
second = ["gau-bot2", "on-off-247runner-two"]

#---------------------------------------------------------------

import heroku3
import time
import os

# gapOfCheck = 1728000
gapOfCheck = 1296000 #15 days
HEROKU_API = os.environ['HEROKU_API']
heroku_conn = heroku3.from_key(HEROKU_API)

#---------------------------------------------------------------
def findMyApp(apps, appName):
    for _ in apps: 
        if _.name == appName: 
            return _

def enableApps(applist, appListText):
    for _ in appListText:
        print("A")
#         findMyApp(applist, _).enable_maintenance_mode()
        findMyApp(applist, _).process_formation()['worker'].scale(1) # run 1 dynos


def disableApps(applist, appListText):
    for _ in appListText:
        print("B")
#         findMyApp(applist, _).disable_maintenance_mode()
        findMyApp(applist, _).process_formation()['worker'].scale(0) # run 0 dynos

#---------------------------------------------------------------
last_time = time.time()%gapOfCheck
count_time = 0

while True:
    time.sleep(1)
    now = time.time()%gapOfCheck

    count_time = count_time+1
    print("Har har mahadev, Jay Sharswati: ", count_time)
    # print(last_time, now, now-last_time)
    if last_time< gapOfCheck and now> 0 and now-last_time<0:
        if last_time-now>gapOfCheck/4:  
            apps = heroku_conn.apps()   
            enableApps(apps, first)
            disableApps(apps, second)
            
    last_time = now
