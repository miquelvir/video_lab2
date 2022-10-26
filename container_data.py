import ffmpeg
from typing import Dict, Any


def get_container_properties(in_path: str) -> Dict[str, Any]:
    """ :returns container data from a video """
    data = ffmpeg.probe(in_path)
    return {
        'number_of_streams': len(data.get('streams', [])),
        'codec_names': [stream['codec_name']
                        for stream in data.get('streams', [])],
        'codec_types': [stream['codec_type']
                        for stream in data.get('streams', [])],
        'format_name': data.get('format', {}).get('format_name', None),
        'format_long_name': data.get('format', {}).get('format_long_name', None)
    }

