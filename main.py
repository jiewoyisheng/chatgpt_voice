import snowboydecoder
import sys
import signal
import getsound
import os

import tts_play
import asr_whisper
import gpt
import playsoundfile
import asyncio

interrupted = False
model =['resources/yadan.pmdl', 'resources/javs.pmdl']

os.close(sys.stderr.fileno())

callbacks = [lambda: callbacks1(), lambda: callbacks1()]

def callbacks1():
    msg=[{"role": "system", "content": "你是一个童话师，可以讲各种故事"}]
    detector.terminate()
    print("唤醒成功!")
    playsoundfile.playsoundfile('sound/nihao.wav')

    try:
        getsound.rec()
        qu=asr_whisper.getasr('sound/question.wav')
        print('问:'+qu)
        msg.append({"role": "user", "content": qu})
        if '什么名字' in qu:
            playsoundfile.playsoundfile('sound/name.wav')
        elif qu!='':
            an=gpt.getgpt(msg)
            print('答:'+an)
            an_split = an.split("\n")
            for av in an_split:
                if av !='':
                    asyncio.run(tts_play.gettts(av))
    except:
        playsoundfile.playsoundfile('sound/cuowu.wav')
        print("发生错误")
    print('唤醒中...')
    detector.start(detected_callback=callbacks,
                interrupt_check=interrupt_callback,
                sleep_time=0.03)

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
    
# main loop

print('检测中...')
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)


detector.terminate()