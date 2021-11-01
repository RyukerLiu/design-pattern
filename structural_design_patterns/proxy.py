class Video:
    def __init__(self, name):
        self.name = name


class GetVideo:
    def get_video(self, name) -> Video:
        raise NotImplementedError


class VideoProvider(GetVideo):
    def get_video(self, name):
        return Video(name)


class GetVideoCachedProxy(GetVideo):
    cached = {}

    def __init__(self, provider):
        self.provider = provider

    def get_video(self, name):
        video = self.cached.get(name)
        if video is None:
            video = self.provider.get_video(name)
            self.cached[name] = video

        return video
