import ffmpeg
from trim_video import input_trim_video_pipe


def repackage_mp4(in_path: str, out_path: str) -> None:
    """ trims to one minut, exports the audio as MP3 and AAC """
    trimmed = input_trim_video_pipe(in_path, '00:00:00', 60)

    audio = trimmed.audio
    audio.output('temp.mp3', ac=2, acodec='mp3').run()
    audio.output('temp.aac', ac=1, acodec='aac', ar='44100').run()

    audio_mp3 = ffmpeg.input('out/temp.mp3')
    audio_aac = ffmpeg.input('out/temp.aac')

    ffmpeg\
        .output(trimmed.video, audio_mp3, audio_aac, out_path, acodec='copy')\
        .run()

