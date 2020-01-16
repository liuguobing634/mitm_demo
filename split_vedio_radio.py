from ffmpy3 import FFmpeg
import os


def split(input_dir, output_dir):
    """input_dir is the dir where input video exists"""
    """check input dir's files"""
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            file_name = os.path.splitext(file)
            print(file_name[1])
            if file_name[1] == '.mp4':
                new_video_file = os.path.join(output_dir, file_name[0] + '_video.mp4')
                new_radio_file = os.path.join(output_dir, file_name[0] + '_audio.mp4')
                if os.path.exists(new_radio_file):
                    os.remove(new_radio_file)
                if os.path.exists(new_video_file):
                    os.remove(new_video_file)
                ff = FFmpeg(inputs={os.path.join(input_dir, file): None},
                            outputs={new_video_file: ['-map', '0:0', '-c:a', 'copy', '-f', 'mp4'],
                                     new_radio_file: ['-map', '0:1', '-c:a', 'copy', '-f', 'mp4']})
                ff.run()


split('input', 'output')
