import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    API_KEY = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'
    channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.channel)
#
