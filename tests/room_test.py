import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(0, 2)
        self.room_1.tab = 0
        self.guest_1 = Guest("Jack Shepherd", 100, "Come On Everybody")
        self.guest_2 = Guest("Kate Austen", 50, "Stayin Alive")
        self.guest_3 = Guest("James Sawyer Ford", 70, "Sweet Home Alabama")
        self.room_1.guest_list = []
        self.song_1 = Song("Driveshaft", "You All Everybody")
        self.song_2 = Song("BeeGees", "Stayin Alive")
        self.room_1.song_list = []

    def test_tab_amount(self):
        self.assertEqual(0, self.room_1.tab)

    def test_check_guest_list(self):
        length = len(self.room_1.guest_list)
        self.assertEqual(0, length)

    def test_check_guest_list(self):
        length = len(self.room_1.guest_list)
        self.assertEqual(1, length)

    def test_check_guest_list(self):
        length = len(self.room_1.guest_list)
        self.assertEqual(0, length)

    def test_check_song_list(self):
        length = len(self.room_1.song_list)
        self.assertEqual(0, length)

    def test_check_song_list(self):
        length = len(self.room_1.song_list)
        self.assertEqual(1, length)

    def test_check_song_list(self):
        length = len(self.room_1.song_list)
        self.assertEqual(0, length)

    def test_check_guest_list(self):
        length = len(self.room_1.guest_list)
        self.assertEqual(1, length)
    
    def test_pay_entrance_fee(self):
        entrance_fee = 5
        paid_fee = self.guest_1 - entrance_fee
        self.assertEqual(95, paid_fee)



