from ffmpy3 import FFmpeg

ff = FFmpeg(inputs={'input/123.mp4': None},
            outputs={'output/123_video.mp4': ['-map', '0:0', '-c:a', 'copy', '-f', 'mp4'],
                     'output/123_audio.mp4': ['-map', '0:1', '-c:a', 'copy', '-f', 'mp4']})
print(ff.cmd)
ff.run()

