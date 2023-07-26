from src.channel import MixinYT


class Video(MixinYT):

    def __init__(self, id_video):
        try:
            self.id_video = id_video
            self.video = self.get_service().videos().list(id=self.id_video, part='snippet,statistics').execute()
            self.title = self.video['items'][0]['snippet']['title']
            self.video_url = self.video['items'][0]['snippet']['thumbnails']['default']['url']
            self.video_view_count = self.video['items'][0]['statistics']['viewCount']
            self.like_count = self.video['items'][0]['statistics']['likeCount']
        except IndexError:
            self.id_video = id_video
            self.title = None
            self.video_url = None
            self.video_view_count = None
            self.like_count = None

    def __str__(self):
        return f'{self.title}'


class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist
