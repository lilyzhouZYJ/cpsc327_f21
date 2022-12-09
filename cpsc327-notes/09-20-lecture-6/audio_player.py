import abc      # using this to enforce abstract classes

class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")

        self.filename = filename

    def play(self):
        print("playing {} as flac".format(self.filename))

FlacFile("audio.flac")


class MediaLoader(metaclass=abc.ABCMeta):
    """Abstract class.
    Specified using metaclass=abc.ABCMeta"""

    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented



class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")

        self.filename = filename


class MP3File(AudioFile):
    pass


class WavFile(AudioFile, MediaLoader):
    pass


class OggFile(AudioFile, MediaLoader):
    ext = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))




OggFile("audio.ogg").play()
a = WavFile("audio.mp3")        # this will give error
a.play()
