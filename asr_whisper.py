import whisper

# 录音文件名
model = whisper.load_model("medium") # 如果模型不存在，会自动下载，默认下载路径 "~/.cache/whisper"

def  getasr(file_name):
    result = model.transcribe(file_name, language='zh') 
    #print(result["text"])
    return result["text"]