import typer
from typing import Optional
from container_data import get_container_properties
from repackage_mp4 import repackage_mp4
from resize_video import resize_video
from broadcast_standard import get_broadcast_standards


app = typer.Typer()


@app.command()
def container(in_path: str):
    print(get_container_properties(in_path))


@app.command()
def repackage(in_path: str,
              out_path: str):
    repackage_mp4(in_path, out_path)


@app.command()
def resize(in_path: str,
           out_path: str,
           width: int,
           height: int,
           duration: int,
           start_time: Optional[str] = '00:00:00'):
    resize_video(in_path, out_path, width, height, start_time, duration)


@app.command()
def broadcast_standards(in_path: str):
    print('\n'.join(get_broadcast_standards(in_path)))


if __name__ == "__main__":
    app()
