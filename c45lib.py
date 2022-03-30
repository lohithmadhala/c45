from chefboost import Chefboost as chef
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("earthquake.csv")
    config = {'algorithm': 'C4.5'}
    model = chef.fit(df, config = config, target_label = 'Effect')
