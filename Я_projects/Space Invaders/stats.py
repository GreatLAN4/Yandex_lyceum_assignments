class Stats:
    # statistics handling
    def __init__(self):
        self.ResetStats()
        self.game_run = True

    def ResetStats(self):
        self.HitPoints = 2
        self.score = 0
