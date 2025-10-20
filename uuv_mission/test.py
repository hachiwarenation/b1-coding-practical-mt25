import numpy as np

import terrain
import dynamic

# Check that the csv file can be loaded at all
loaded_mission = dynamic.Mission.from_csv("data\mission.csv")
print(f"The first 5 datapoints of the reference are {loaded_mission.reference[0:5]}")
print(f"The type of the cave_depth object is {type(loaded_mission.cave_depth)}")