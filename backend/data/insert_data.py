from pymongo import MongoClient
import pandas as pd


coin_name = input("coin 명 입력 : ")
file_name = input("file 명 입력 : ")
coin_name += '_costs'
cluster = MongoClient("mongodb+srv://dongle:tkfkdgksek1@cluster0.fqkie.mongodb.net/capstone?retryWrites=true&w=majority")

db = cluster["capstone"]
collection = db[coin_name]

df = pd.read_csv(f'C:/Users/epicl/Documents/GitHub/CapstoneDongulDongul.github.io-1/backend/data/{file_name}',encoding = 'utf-8', dtype = {
    'Greed_Fear_Score': float,
    'date': str,
    'target_date': str,
    'close': float,
    'predict_close': float,
    'vol': float,
    'percent': float,
}).drop(['Unnamed: 0'], axis=1)

# dataframe의 컬럼 명
cols = df.columns 

for i in range(len(df)):
  temp = {
    cols[0] : df.iloc[i][cols[0]],
    cols[1] : df.iloc[i][cols[1]],
    cols[2] : df.iloc[i][cols[2]],
    cols[3] : df.iloc[i][cols[3]],
    cols[4] : df.iloc[i][cols[4]],
    cols[5] : df.iloc[i][cols[5]],
    cols[6] : df.iloc[i][cols[6]],
  }
  collection.insert_one(temp)
  print(f"{i} add")

print('finish')

