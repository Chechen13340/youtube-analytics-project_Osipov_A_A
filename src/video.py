from src.channel import Channel


class Video(Channel):

    def __init__(self, id_video):
        self.id_video = id_video
        self.video = self.youtube.videos().list(id=self.id_video, part='snippet,statistics').execute()
        self.title_video = self.video['items'][0]['snippet']['title']
        self.video_url = self.video['items'][0]['snippet']['thumbnails']['default']['url']
        self.video_view_count = self.video['items'][0]['statistics']['viewCount']
        self.video_likes = self.video['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.title_video}'


class PLVideo(Video):
    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist
