import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Driveshaft", "Come On Everybody")

    def test_song_title(self):
        self.assertEqual("Come On Everybody", self.song.title)