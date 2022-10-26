import ffmpeg


def input_trim_video_pipe(in_path: str,
                          start_time: str,
                          duration: int) -> ffmpeg:
    """ inputs a trimmed video and returns a ffmpeg pipe """
    return ffmpeg.input(in_path, ss=start_time, t=duration)


def trim_video(in_path: str, out_path: str, start_time: str, duration: int):
    """ trims and saves the video from start_time to start_time + duration """
    input_trim_video_pipe(in_path, start_time, duration) \
        .output(out_path) \
        .run()
