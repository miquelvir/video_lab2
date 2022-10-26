from trim_video import input_trim_video_pipe


def resize_video(in_path: str,
                 out_path: str,
                 width: int,
                 height: int,
                 start_time: str,
                 duration: int):
    """ trims and saves the video from start_time to start_time + duration """

    input_trim_video_pipe(in_path, start_time, duration) \
        .filter('scale', width=width, height=height) \
        .output(out_path, map='0:a', acodec='copy') \
        .run()
