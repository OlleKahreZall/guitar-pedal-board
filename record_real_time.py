
import pyaudio
import numpy as np

def configure_in_out_streams():
    p=pyaudio.PyAudio()
    FORMATIN = pyaudio.paInt16
    FORMATOUT = FORMATIN
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024

    stream_in = p.open(format=FORMATIN, 
                        channels=CHANNELS,
                        rate=RATE, 
                        input=True, 
                        input_device_index=3,
                        frames_per_buffer=CHUNK)
    stream_out = p.open(format=FORMATOUT, 
                        channels=CHANNELS,
                        rate=RATE, 
                        output=True, 
                        input_device_index=0,
                        frames_per_buffer=CHUNK)
    
    return stream_in, stream_out, CHUNK


def output_signal(visualize, stream_in, stream_out, CHUNK):
    print("recording...")
    while True:
        if visualize:
            data = np.fromstring(stream_in.read(CHUNK, exception_on_overflow=False),dtype=np.int16)
            peak=np.average(np.abs(data))*2
            bars="#"*int(50*peak/2**16)
            print(bars)
        else:
            in_data = stream_in.read(CHUNK, exception_on_overflow=False)
            stream_out.write(in_data)

    
def main(visualize: bool=False):
    stream_in, stream_out, CHUNK = configure_in_out_streams()
    output_signal(visualize, stream_in, stream_out, CHUNK)


if __name__ == "__main__":
    main(visualize=False)
    # stream.stop_stream()
# p.terminate()