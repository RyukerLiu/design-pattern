import unittest
from structural_design_patterns.bridge import RemoteControl, AdvancedRemoteControl, Radio, Tv


class TestBridge(unittest.TestCase):
    def test_tv(self):
        tv = Tv()
        remote = RemoteControl(tv)
        self.assertEqual(tv.is_enabled(), False)
        self.assertEqual(tv.get_volume(), 50)
        self.assertEqual(tv.get_channel(), 1)

        remote.toggle_power()
        self.assertEqual(tv.is_enabled(), True)

        remote.channel_up()
        self.assertEqual(tv.get_channel(), 2)

        remote.volume_down()
        self.assertEqual(tv.get_volume(), 40)

    def test_radio(self):
        radio = Radio()
        remote = AdvancedRemoteControl(radio)
        self.assertEqual(radio.is_enabled(), False)
        self.assertEqual(radio.get_volume(), 50)
        self.assertEqual(radio.get_channel(), 1)

        remote.toggle_power()
        self.assertEqual(radio.is_enabled(), True)

        remote.channel_up()
        self.assertEqual(radio.get_channel(), 2)

        remote.volume_down()
        self.assertEqual(radio.get_volume(), 40)

        remote.mute()
        self.assertEqual(radio.get_volume(), 0)
