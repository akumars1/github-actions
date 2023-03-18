import os

import ffmpeg_streaming
from ffmpeg_streaming import Formats, Representation, Size, Bitrate

video = ffmpeg_streaming.input('/Users/abhishek/Desktop/Mujhko Ranaji Maaf Karna_HD_720p-(HDvideo9).mp4')
hls = video.hls(Formats.h264())
hls.auto_generate_representations()
hls.output(os.path.join("/Users/abhishek/Documents/projects/python/live_streaming/media", 'hls.m3u8'))
