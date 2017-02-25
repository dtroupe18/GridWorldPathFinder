import pickle
import GenerateGridWorld
# takes about 90 seconds to generate the mazes
mazes, starts, goals = GenerateGridWorld.generate_mazes(50, 101)  # stored in a dictionary from 0 - 49

#  Save all the data
with open("all_mazes.pickle", "wb") as handle:
    pickle._dump(mazes, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open("start_locations.pickle", "wb") as handle:
    pickle._dump(starts, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open("goal_locations.pickle", "wb") as handle:
    pickle._dump(goals, handle, protocol=pickle.HIGHEST_PROTOCOL)
