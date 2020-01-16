import json

with open('video_info/content_1579180427523.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for item in data:
        if 'aweme_info' in item.keys():
            print(item['aweme_info']['video'])

# with open('video_info/video_info_1579184293465.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#     aweme_list = data['aweme_list']
#     for awene in aweme_list:
#         ra = awene['video']['bit_rate']
#         for it in ra:
#             print(it)
