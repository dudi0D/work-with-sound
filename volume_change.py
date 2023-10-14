import wave
import struct


source = wave.open("in.wav", mode="rb")
quiet_file = wave.open("quiet.wav", mode="wb")
loud_file = wave.open("loud.wav", mode="wb")
quiet_file.setparams(source.getparams())
loud_file.setparams(source.getparams())
frames_count = source.getnframes()
data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
quiet_data = [i // 2 for i in data]
loud_data = [i * 2 % 32767 for i in data]
newframes = struct.pack("<" + str(len(quiet_data)) + "h", *quiet_data)
newframes_1 = struct.pack("<" + str(len(loud_data)) + "h", *loud_data)
quiet_file.writeframes(newframes)
loud_file.writeframes(newframes_1)
source.close()
quiet_file.close()
loud_file.close()
