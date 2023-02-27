import pandas as pd


df = pd.read_csv('../california_housing_train.csv')
df.shape

task1 = df[(df['population'] >= 0) & (df['population'] <= 500)]
print(task1['median_house_value'].mean())
task2 = df[df['population'] == df['population'].min()]
print(task2['households'].max())

