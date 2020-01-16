import json
import csv
import os
from collections.abc import Iterable
from items import VideoInfo
# 将数据写到csv或者excel上


def parse_all_videos(info_dir):
    videos = []
    for root, dirs, files in os.walk(info_dir):
        for file in files:
            with open(os.path.join(root, file), mode='r', encoding='utf-8') as info_file:
                video_info = json.load(info_file)
                vds = parse_videos(video_info)
                videos.extend(vds)
    return videos


def parse_videos(video_info):
    videos = []
    if isinstance(video_info['aweme_list'], Iterable):
        for video_item in video_info['aweme_list']:
            video = parse_video(video_item)
            videos.append(video)
    return videos


def parse_video(video_item):
    video = VideoInfo()
    video.nick = video_item['author']['nickname']
    video.desc = video_item['desc']
    if 'video' in video_item.keys():
        for addr in video_item['video']['play_addr']['url_list']:
            if 'ixigua.com' in addr:
                video.add_addr(addr)
            if 'bit_rate' in video_item['video'].keys():
                for rate in video_item['video']['bit_rate']:
                    for addr in rate['play_addr']['url_list']:
                        if 'ixigua.com' in addr:
                            video.add_addr(addr)
    return video
