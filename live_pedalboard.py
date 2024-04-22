# Use python3 -m sounddevice to identify the devices

from pedalboard import Pedalboard, Chorus, Compressor, Delay, Gain, Reverb, Phaser
from pedalboard.io import AudioStream

# Open up an audio stream:
with AudioStream(
  input_device_name='USB PnP Sound Device',  # Guitar interface
  output_device_name='USB Audio Device'
) as stream:
  # Audio is now streaming through this pedalboard and out of your speakers!
  stream.plugins = Pedalboard([
      Compressor(threshold_db=10
                 , ratio=25),
      #sGain(gain_db=10),
      #Chorus(),
      #Phaser(),
      Reverb(room_size=0.25),
      Delay(delay_seconds=0, feedback=0)
  ])
  input("Press enter to stop streaming...")
