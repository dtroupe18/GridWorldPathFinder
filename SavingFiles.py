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


# load all the data
with open('all_mazes.pickle', 'rb') as handle:
    all_mazes = pickle.load(handle)

with open('start_locations.pickle', 'rb') as handle:
    start = pickle.load(handle)

with open('goal_locations.pickle', 'rb') as handle:
    stop = pickle.load(handle)


print(all_mazes == mazes)
print(starts == start)
print(goals == stop)

print(start)
print(stop)