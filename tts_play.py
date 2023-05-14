# from gtts import gTTS

# # 输入文本

# def gettts(text):
# # 使用Google Text-to-Speech API将文本转换为语音
#     tts = gTTS(text,lang='zh-tw')

#     # 保存音频文件
#     tts.save("sound/result.wav")
import edge_tts
import asyncio
import playsoundfile

TEXT1 = ""
# with open('text2voicetest.txt', 'rb') as f:
#     data = f.read()
#     TEXT1 = data.decode('utf-8')
# print(TEXT1)
voice = 'zh-CN-XiaoxiaoNeural'
output = 'sound/result.wav'
rate = '-4%'
volume = '+0%'


async def gettts(TEXT):
    #print(TEXT)
    tts = edge_tts.Communicate(text=TEXT, voice=voice, rate=rate, volume=volume)
    await tts.save(output)
    playsoundfile.playsoundfile(output)

if __name__ == '__main__':
    asyncio.run(gettts(TEXT1))
