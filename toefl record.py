#parameter you can change
waitingTime = 5
recordingTime = 10
#path for records (need no mandarin in file path)
path = "C:\\Users\\s9402\\Downloads\\托福準備\\托福說寫\\speaking questions and template\\task1 practice\\"

# library for time
import time
import winsound

#time before recording
if waitingTime > 0:
    print("Waiting...")
    for x in range(waitingTime):
        time.sleep(1)
        print(f'\r |{"█"*round(45*((x+1)/waitingTime))}{" "*round(45*(waitingTime-x-1)/waitingTime)}| {x+1}/{waitingTime} seconds', end=" ")
        
# import for voice reecord
import pyaudio
import keyboard

# set voice record parameters
chunk = 1024
format = pyaudio.paInt16
channels = 2
rate = 44100

# import for find the files 
import os
# set file name
filenumber = len(os.listdir(path))+1 
audiofilename = "Record"+str(filenumber)+".wav"

print("\nstart recording...")
winsound.Beep(700,200)

p = pyaudio.PyAudio()
stream = p.open(format=format,
                channels=channels,
                rate=rate,
                input=True,
                frames_per_buffer=chunk)
frames = []

print("    press space to stop")
print("    or wait for "+str(recordingTime)+" seconds")
startrecordTime = time.time()

# recording
while True:
    try:
        data = stream.read(chunk)  
        frames.append(data)
        rt = time.time() - startrecordTime
        rtPercent = rt/recordingTime
        print(f'\r |{"█"*round(60*rtPercent)}{" "*round(60*(1-rtPercent))}| {round(rt)}/{recordingTime} seconds', end=" ")
    except:
        print("\nsomething wrong during recording")
         
    if keyboard.is_pressed('space'):
        print("\nstopping recording") 
        break
    if time.time() > startrecordTime+recordingTime:
        print("\nstopping recording") 
        break

winsound.Beep(1000,200)
stream.stop_stream()
stream.close()
p.terminate()

# output wav
#import for building wav file
import wave

pathfilename = path+audiofilename
wf = wave.open(pathfilename, 'wb')  
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(format))
wf.setframerate(rate)
wf.writeframes(b''.join(frames))
wf.close()

goSTT = input("Do you want to transcribe the record?")
while True:
    if goSTT == "Y":
        break
    if goSTT == "N":
        break
    goSTT = input("Please answer \"Y\" or \"N\"")

if goSTT == "Y":
    # Sound transcribe text (STT)
    #import for STT
    import whisper

    print("text generating...")
    model = whisper.load_model("turbo")
    result = model.transcribe(pathfilename)
    recordText = result['text']
    print("\nText:")
    print(recordText)
    wordlength = len(recordText.split(" "))
    print("\n"+str(wordlength)+" words")