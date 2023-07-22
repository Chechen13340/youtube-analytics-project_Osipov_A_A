import datetime

from operator import itemgetter

import isodate

from src.channel import MixinYT


class PlayList(MixinYT):
    def __init__(self, list_id):
        self.list_id = list_id
        self.play_list = self.get_service().playlists().list(id=self.list_id, part='contentDetails,snippet',
                                                             maxResults=50).execute()

        self.playlist_videos = self.get_service().playlistItems().list(playlistId=self.list_id,
                                                                       part='contentDetails',
                                                                       maxResults=50,
                                                                       ).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.get_service().videos().list(part='contentDetails,statistics',
                                                               id=','.join(self.video_ids)
                                                               ).execute()
        self.title = self.play_list['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.list_id}'

    @property
    def duration_video(self):
        list_total_time = []
        for i in self.video_response['items']:
            duration = isodate.parse_duration(i['contentDetails']['duration'])
            list_total_time.append(duration)
        return list_total_time

    @property
    def total_duration(self):
        total_duration = sum(self.duration_video, datetime.timedelta())
        return total_duration

    @property
    def total_seconds(self):
        total_seconds = sum(self.duration_video, datetime.timedelta())
        return total_seconds

    @property
    def list_video(self):
        list_video = []
        for list_ in self.video_response['items']:
            count_like = int(list_['statistics']['likeCount'])
            url_video = f"https://youtu.be/{list_['id']}"
            list_video.append({'likeCount': count_like,
                               'url': url_video})
        return list_video

    def show_best_video(self):
        best_video = sorted(self.list_video, key=itemgetter('likeCount'), reverse=True)
        return best_video[0]['url']
