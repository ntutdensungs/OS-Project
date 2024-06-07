#!/usr/bin/env python3

import serial
import time
import subprocess
import sys
from pathlib import Path

if __name__ == '__main__':
    alarm_path = 'alarm.mp3'
    notify_path = 'notify.mp3'
    if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
        alarm_path = sys.argv[1]
    tmp_threshold1 = 33.2
    tmp_threshold2 = 33.7
    sound = 0
    alarm = None
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    test = 34.0
    while True:
        line = ser.readline().decode('utf-8').rstrip()
        if line:
            temp = float(line.split(', ')[0])
            temp = test
            test -= 0.1
            print(temp)
            if temp <= tmp_threshold1:
                if alarm is not None and sound != 1:
                    alarm.terminate()
                    alarm = None
                if alarm is not None and alarm.poll() is not None:
                    alarm = None
                    sound = 0
                if alarm is None:
                    alarm = subprocess.Popen(['ffplay', '-loop', '0', alarm_path])
                    sound = 1
            elif temp <= tmp_threshold2:
                if alarm is not None and sound != 2:
                    alarm.terminate()
                    alarm = None
                if alarm is not None and alarm.poll() is not None:
                    alarm = None
                    sound = 0
                if alarm is None:
                    alarm = subprocess.Popen(['ffplay', '-loop', '0', notify_path])
                    sound = 2
            elif alarm is not None:
                alarm.terminate()
                alarm = None
        time.sleep(1)