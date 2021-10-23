import unittest
from structural_design_patterns.proxy import VideoProvider, GetVideoProxy


class TestProxy(unittest.TestCase):
    def test_video_provider(self):
        provider = VideoProvider()
        video = provider.get_video('x')
        self.assertEqual(video.name, 'x')

        video_2 = provider.get_video('x')
        self.assertIsNot(video, video_2)

    def test_get_video_proxy(self):
        provider = VideoProvider()
        proxy = GetVideoProxy(provider)
        video = proxy.get_video('x')
        self.assertEqual(video.name, 'x')

        video_2 = proxy.get_video('x')
        self.assertIs(video, video_2)
