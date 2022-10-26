# 1. Get container data
Run `python3 cli.py --help` to see the options. 
E.g. to get container data from video:
`python3 cli.py container src/BBB.mp4`
>>>
`{'number_of_streams': 2, 'codec_names': ['h264', 'aac'], 'codec_types': ['video', 'audio'], 'format_name': 'mov,mp4,m4a,3gp,3g2,mj2', 'format_long_name': 'QuickTime / MOV'} `

# 2. Repackage as mp4 (mp3+aac)
Run `python3 cli.py --help` to see the options. 
E.g. to repackage it:
`python3 cli.py repackage src/BBB.mp4 out/BBB2.mp4`
We can use the previous command (exercise 1) to check it includes the 3 streams:
`python3 cli.py container out/BBB2.mp4` 
>>>
`{'number_of_streams': 3, 'codec_names': ['h264', 'mp3', 'aac'], 'codec_types': ['video', 'audio', 'audio'], 'format_name': 'mov,mp4,m4a,3gp,3g2,mj2', 'format_long_name': 'QuickTime / MOV'}`

# 3. Resize video
Run `python3 cli.py --help` to see the options. E.g. to resize to 480 x 270:
`python3 cli.py resize --start-time 00:00:10 src/BBB.mp4 out/BBB480.mp4 480 270 10`

I have assumed 720p and 480p were just a means to refer to the resolution, I have not implemented any kind of
interlaced to progressive conversion.

# 4. Detect possible audio standards
Run `python3 cli.py --help` to see the options.
Run to check the standards that fit:
`python3 cli.py broadcast-standards src/BBB.mp4`
`python3 cli.py broadcast-standards src/sample4.ac3`

# 5. Class
Well, wrapper.py does that, whatever you want it for.