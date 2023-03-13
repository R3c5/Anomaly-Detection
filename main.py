import pandas as pd

train_df = pd.read_csv(r'resources\train_data.csv')
val_df = pd.read_csv(r'resources\val_data.csv')
test_df = pd.read_csv(r'resources\test_data.csv')

train_data = train_df[train_df.columns.difference(['Id', 'Label'])]
val_data = val_df[val_df.columns.difference(['Id', 'Label'])]
test_data = test_df[test_df.columns.difference(['Id'])]

import datetime
import time

train_seconds = [time.mktime(datetime.datetime.strptime(x.strip(), "%d/%m/%Y %I:%M:%S %p").timetuple()) for x in
           train_data['Timestamp']]

val_seconds = [time.mktime(datetime.datetime.strptime(x.strip(), "%d/%m/%Y %I:%M:%S %p").timetuple()) for x in
           val_data['Timestamp']]

test_seconds = [time.mktime(datetime.datetime.strptime(x.strip(), "%d/%m/%Y %I:%M:%S %p").timetuple()) for x in
           test_data['Timestamp']]

train_with_seconds = train_df
train_with_seconds['Seconds'] = train_seconds
val_with_seconds = val_df
val_with_seconds['Seconds'] = val_seconds
test_with_seconds = test_df
test_with_seconds['Seconds'] = test_seconds


train_data_with_time = train_df[train_df.columns.difference(['Id', 'Label'])]
val_data_with_time = val_df[val_df.columns.difference(['Id', 'Label'])]
test_data_with_time = test_df[test_df.columns.difference(['Id'])]

