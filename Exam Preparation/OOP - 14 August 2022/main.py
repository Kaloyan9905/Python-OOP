from horse_racing.horse_race_app import HorseRaceApp
from horse_racing.horse_specification.appaloosa import Appaloosa

horseRaceApp = HorseRaceApp()
h = Appaloosa("bobob", 119)
print(h.train())
