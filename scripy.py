from collections import Iterable

from mitmproxy import ctx
from parse_video import parse_videos
import json
from down_video import DownThread
import time


index = 1


def response(flow):
    global index
    content_save = ContentSave()
    headers = flow.response.headers
    resp = flow.response
    info = ctx.log.info
    url = flow.request.url
    if 'https://aweme.snssdk.com/aweme/v1' in url or \
            'https://search-lf.amemv.com/aweme/v1/general/search/single/' in url:
        info('ssssssssssssssssss %s' % url)
        if 'content-type' in headers.keys():
            content_type = headers[b'content-type']
            if 'application/json' in content_type:
                curt = time.time() * 1000
                json_resp = json.loads(resp.text)
                if 'data' in json_resp.keys():
                    data = json_resp['data']
                    with open('video_info/content_%d.txt' % curt, 'w', encoding='utf-8') as fi:
                        print(data, file=fi)

    if 'content-type' in headers.keys():
        content_type = headers[b'content-type']
        if 'application/json' in content_type:
            # info(resp.text)
            json_resp = json.loads(resp.text)
            if 'aweme_list' in json_resp:
                info('视频流')
                content_save.save(resp.text)
                index = index + 1


class ContentSave(object):
    info = ctx.log.info
    down_thread = DownThread(thread_number=7, info=info)

    def save(self, content):
        i = 0
        curt = time.time() * 1000
        try:
            videos = parse_videos(json.loads(content))
            for video in videos:
                if len(video.addrs) > 0:
                    downaddr = video.addrs[0]
                    self.info(downaddr)
                    self.info('下载视频: %s-%d' % (video.nick, i))
                    self.down_thread.submit_task(downaddr, 'download/%s/%d-%d.mp4' % (video.nick, curt, i))
                    i = i + 1
        except Exception as e:
            ctx.log.error('there was a wrong => %s' % str(e))
