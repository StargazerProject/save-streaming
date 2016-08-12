import urllib.request
import re
import os
import time

loop = 0
isliveurl = 'http://live.bilibili.com/bili/isliving/123484'
islive = str(urllib.request.urlopen(isliveurl).read())
try:
    req = re.findall(r"(url)",islive)[0]
except:
    print('还没直播呐')
    exit()
else:
    url = 'http://live.bilibili.com/api/h5playurl?roomid=33616'
    while(True):
        r = str(urllib.request.urlopen(url).read())
        m3u8 = re.findall(r"(http://[^\s]{,58})",r)[0]
        loop = loop + 1
        os.system('ffmpeg -i '+ m3u8 +' -acodec copy -bsf:a aac_adtstoasc -vcodec copy -f mp4 '+ str(int(time.time())) +'.mp4')
        time.sleep(30)
        if loop == 11:
            break
        else:
           pass
