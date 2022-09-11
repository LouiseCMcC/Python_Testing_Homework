import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Jack Shepherd", 100, "You All Everybody")
        

    def test_guest_has_name(self):
        self.assertEqual("Jack Shepherd", self.guest.name)


    