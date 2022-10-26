from typing import List
import ffmpeg


STANDARDS = [
    {
        "name": "DVB",
        "video": ["mpeg2", "h264"],
        "audio": ["aac", "ac3", "mp3"]
    },
    {
        "name": "DTTB",
        "video": ["mpeg2", "h264"],
        "audio": ["aac"]
    },
    {
        "name": "ATSC",
        "video": ["mpeg2", "h264"],
        "audio": ["ac3"]
    },
    {
        "name": "DTMB",
        "video": ["avs", "avs+", "mpeg2", "h264"],
        "audio": ["dra", "aac", "ac3", "mp2", "mp3"]
    }
]


def get_broadcast_standards(in_path: str) -> List[str]:
    """ :returns the deduced broadcast standard """
    data = ffmpeg.probe(in_path)

    streams = {
        'audio': [],
        'video': []
    }
    for stream in data.get('streams', []):
        streams[stream['codec_type']].append(stream['codec_name'])

    possible_standards = []
    for standard in STANDARDS:
        # check if all video and audio streams are possible for this standard
        fits = True
        for type_ in ('video', 'audio'):
            for existing_audio_codec in streams[type_]:
                if existing_audio_codec not in standard[type_]:
                    fits = False
                    break
            if not fits:
                break
        if fits:
            possible_standards.append(standard['name'])

    return possible_standards
