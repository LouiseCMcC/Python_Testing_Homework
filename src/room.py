from readline import get_current_history_length


class Room:
    def __init__(self, tab, capacity):
        self.tab = tab
        self.capacity = capacity
        self.guest_list = []
        self.song_list = []

    def tab_amount(self):
        return self.room_1.tab

    def check_guest_list(self):
        return len(self.room_1.guest_list)
    
    def add_guest_to_room(self, guest):
        self.room_1.guest_list.append(guest)

    def remove_guest_from_room(self, guest):
        self.room_1.guest_list.remove(guest)

    def check_song_list(self):
        return len(self.room_1.guest_list)

    def add_song_to_room(self, song):
        self.room_1.guest_list.append(song)

    def remove_song_from_list(self, song):
        self.guest_list.remove(song)

