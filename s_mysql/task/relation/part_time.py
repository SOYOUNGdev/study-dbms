class PartTime:
    def __init__(self, id, time, conference_room_id):
        self.id = id
        self.time = time
        self.conference_room_id = conference_room_id

    def __str__(self):
        return str(self.time)