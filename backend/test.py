import pybaseball as pybsb
import predict as pred
import json


# player_id = pybsb.playerid_lookup('ohtani', 'shohei').loc[0].at['key_mlbam']

# data = pybsb.batting_stats_range("2023-04-01", "2023-05-05").sort_values('OPS', ascending=False)
# df = pybsb.get_splits('troutmi01')


print(pred.predict_avg('bellinger.csv'))
print(pred.predict_avg('ohtani.csv'))

