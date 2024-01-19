class ConferenceRoom:
    def __init__(self, id, part_times):
        self.id = id
        self.part_times = part_times

    def __str__(self):
        time_str =""
        for i, part_time in enumerate(self.part_times):
            time_str += f'{i + 1}. {part_time.__str()}\n'
        return time_str