class RemoteControl:
    '''
    Abstraction Class
    '''

    def __init__(self, device):
        self.device = device

    def toggle_power(self):
        device_is_enabled = self.device.is_enabled()
        if device_is_enabled:
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)

    def channel_down(self):
        self.device.set_channel(self.device.get_channel() - 1)

    def channel_up(self):
        self.device.set_channel(self.device.get_channel() + 1)


class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.set_volume(0)


class Device:
    '''
    Implementation Class
    '''

    def __init__(self):
        self._is_enabled = False
        self.volume = 50
        self.channel = 1

    def is_enabled(self):
        return self._is_enabled

    def enable(self):
        self._is_enabled = True

    def disable(self):
        self._is_enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, percent):
        self.volume = percent

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel


class Tv(Device):
    pass


class Radio(Device):
    pass
