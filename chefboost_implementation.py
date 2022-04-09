from dataclasses import field
from chefboost import Chefboost as chef
import pandas as pd

if __name__ == '__main__':
    fields = ["Latitude", "Longitude", "DepthMeters","MagType", "Magnitude", "potential_blast", "bix_potential_blasts"]
    df = pd.read_csv("Earthquakes_earthquakes.csv",usecols=fields)
    config = {'algorithm': 'C4.5'}
    model = chef.fit(df, config = config, target_label = 'potential_blast')
