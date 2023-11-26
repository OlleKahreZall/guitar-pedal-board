# from pedalboard import Reverb, Gain
# from pedalboard.io import AudioStream

# input_device_name = AudioStream.input_device_names[1]
# output_device_name = AudioStream.output_device_names[1]
# with AudioStream(input_device_name, output_device_name) as stream:
#     # In this block, audio is streaming through `stream`!
#     # Audio will be coming out of your speakers at this point.

#     # Add plugins to the live audio stream:
#     reverb = Reverb(room_size=0.9)
#     gain = Gain(gain_db=50)

#     stream.plugins.append(reverb)
#     stream.run() 


#     'USB PnP Sound Device'
#     'DisplayPort'


from pedalboard import Pedalboard, Chorus, Compressor, Delay, Gain, Reverb, Phaser
from pedalboard.io import AudioStream

# Open up an audio stream:
with AudioStream(
  input_device_name='USB PnP Sound Device',  # Guitar interface
  output_device_name='DisplayPort'
) as stream:
  # Audio is now streaming through this pedalboard and out of your speakers!
  stream.plugins = Pedalboard([
      Compressor(threshold_db=-50, ratio=25),
      Gain(gain_db=30),
      Chorus(),
      Phaser(),
      Reverb(room_size=0.25),
  ])
  input("Press enter to stop streaming...")