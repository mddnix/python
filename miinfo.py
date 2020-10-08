#!/usr/bin/env python3

from pymediainfo import MediaInfo as mi

media_info = mi.parse('/dc/waste/test.mp4')
for track in media_info.tracks:
    print(track.to_data().keys())
