import wave
import pyaudio
import numpy
import pylab

#open WAV file
wf = wave.open("C:\\Users\\momo\\workspace\\py_\\audio\\SecretMountains_HighHorse_wow.wav", "rb")

#cerate PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
channels=wf.getnchannels(),
rate=wf.getframerate(),
output=True)
nframes = wf.getnframes()
framerate = wf.getframerate()

#read Reads the complete frame data to str_data , is a [string] type of data
str_data = wf.readframes(nframes)
wf.close()

#Converts the waveform data to an array
# A new 1-D array initialized from raw binary or text data in a string.
wave_data = numpy.fromstring(str_data, dtype=numpy.short)

#Change the wave_data array to 2 columns, and the number of rows to match automatically. When modifying shape attributes, the total length of the array needs to be kept constant.
wave_data.shape = -1,2

#Transpose the array
wave_data = wave_data.T

#Time is also an array that is paired with wave_data [0] or wave_data [1] to form a series of point coordinates
#time = numpy.arange(0,nframes)*(1.0/framerate)
#Plot the waveform
#pylab.plot(time, wave_data[0])
#pylab.subplot(212)
#pylab.plot(time, wave_data[1], c="g")
#pylab.xlabel("time (seconds)")
#pylab.show()

##### Sampling points, modify the number of sampling points and the starting position for different position and length of the audio waveform analysis #####
N=44100
start=0 #Starts the sampling position
df = framerate/(N-1) # Resolution rate
freq = [df*n for n in range(0,N)] #N elements
wave_data2=wave_data[0][start:start+N]
c=numpy.fft.fft(wave_data2)*2/N
#Conventional displays the spectrum at half the sampling frequency
d=int(len(c)/2)
#Only freq below 4000 are displayed
while freq[d]>4000:
    d-=10
pylab.plot(freq[:d-1],abs(c[:d-1]),'r')
pylab.show()