from container_data import get_container_properties
from repackage_mp4 import repackage_mp4
from resize_video import resize_video
from broadcast_standard import get_broadcast_standards
from typing import Dict, Any, Optional, List


class Wrapper:
    @staticmethod
    def get_container_info(in_path: str) -> Dict[str, Any]:
        return get_container_properties(in_path)

    @staticmethod
    def repackage_demo(in_path: str, out_path: str):
        repackage_mp4(in_path, out_path)

    @staticmethod
    def resize(in_path: str,
               out_path: str,
               width: int,
               height: int,
               duration: int,
               start_time: Optional[str] = '00:00:00'):
        resize_video(in_path, out_path, width, height, start_time, duration)

    @staticmethod
    def get_broadcast_standards(in_path: str) -> List[str]:
        return get_broadcast_standards(in_path)
    