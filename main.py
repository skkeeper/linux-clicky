#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 2 -*-
# Author: Fábio André Damas <skkeeper at gmail dot com>

from os import listdir, getcwd
from random import choice
from third_party.evdev import DeviceGroup
from linux_clicky.play_sound import PlaySound
from linux_clicky.detect_keyboards import detect_keyboards
from optparse import OptionParser
from signal import signal, SIGINT
from sys import exit


# Handle CTRL+C
def signal_handler(signal, frame):
    print '\033[1;32mCTRL + C Detected. Exiting ...'
    print 'Ignore any errors after this message.\033[1;m'
    exit(0)
signal(SIGINT, signal_handler)

# Handle arguments
parser = OptionParser()
parser.add_option(
    '-v', '--volume', action="store", dest='volume',
    help="sets the volume of the clicks, anything above 1 will increase the " +
    "volume, and anything less will decrease it. Don't use numbers bigger " +
    "than 2")

parser.set_defaults(volume=1)
(options, args) = parser.parse_args()

# Get a list of sound files
sounds = listdir(getcwd() + '/sounds')
sound_tmp = {}
sound_tmp["click"] = []
for sound in sounds:
    if sound == 'enter.wav':
        sound_tmp["enter"] = sound
    elif sound == 'space.wav':
        sound_tmp["space"] = sound
    else:
        sound_tmp["click"].append(sound)
sounds = sound_tmp
# Volume: Negative to lower the volume
volume = str(options.volume)

key_sound_pair = dict()
dev = DeviceGroup(detect_keyboards())
while 1:
    event = dev.next_event()
    if event is not None:
        # print repr(event)
        if event.type == "EV_KEY" and event.value == 1:
            if event.code.startswith("KEY"):
                if event.code == "KEY_ENTER":
                    filename = getcwd() + '/sounds/' + sounds["enter"]
                elif event.code == "KEY_SPACE":
                    filename = getcwd() + '/sounds/' + sounds["space"]
                else:
                    if event.code not in key_sound_pair:
                        key_sound_pair[event.code] = choice(sounds["click"])
                    filename = getcwd() + '/sounds/' +\
                        key_sound_pair[event.code]
                PlaySound(filename, volume).start()
