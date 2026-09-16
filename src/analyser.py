import wave
import struct

with wave.open("sample1.wav") as wav_sample:
    metadata = wav_sample.getparams()
    print(metadata)
    frames = wav_sample.readframes(metadata.nframes)
    print(len(frames))
    format = "<" + "h" * (len(frames) // 2)
    audio = list(struct.unpack(format, frames))
    left_channel = audio[::metadata.nchannels]
    #print(left_channel)
    print(max(left_channel))
    print(min(left_channel))




