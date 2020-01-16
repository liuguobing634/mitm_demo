from urllib import request

from concurrent import futures

import os

# 将数据写到csv或者excel上


def _work(link, filename, info):
    try:
        with open(filename, 'wb') as f:
            with request.urlopen(link) as req:
                if req.getheader(name="Content-Type") == 'video/mp4':
                    f.write(req.read())
    except Exception as e:
        info(str(e))


class DownThread (object):
    def __init__(self, thread_number=7, info=print):
        self.executor = futures.ThreadPoolExecutor(max_workers=thread_number)
        self.info = info

    def submit_task(self, link, filename):
        ind = filename.rfind('/')
        if ind != -1:
            sub = filename[0: ind]
            if not os.path.exists(sub):
                os.makedirs(sub)
        self.executor.submit(lambda: _work(link, filename, self.info))

    def shutdown(self):
        self.executor.shutdown()
