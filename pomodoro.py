import subprocess
import pydub as pd


#rain_25 = pd.AudioSegment.from_mp3('outdata/25_rain_storm.mp3')
#bird_5 = pd.AudioSegment.from_mp3('outdata/5_bird_chirp.mp3')

rain_25 = 'outdata/25_rain_storm.mp3'
bird_5 = 'outdata/5_bird_chirp.mp3'

ffplay_command = [
        'ffplay',
        '-hide_banner',
        '-autoexit',
        '-showmode', '1',
        ]

input('Start?')
subprocess.call(ffplay_command + [rain_25])
print('BREAK!')
subprocess.call(ffplay_command + [bird_5])
print('Back to work!')


