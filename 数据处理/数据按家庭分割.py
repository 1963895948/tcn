import pandas as pd
import datetime

index = 'id'
jiatin_date = []
jiatin_value = []
with open("../data/元数据/File2.txt") as f:
    for line in f.readlines():
        lis = line.split(' ')
        if lis[0] == index:
            now = datetime.datetime.strptime('2009-01-01', "%Y-%m-%d")
            date = now + datetime.timedelta(days=int(lis[1][:3]))
            jiatin_date.append(date)
            jiatin_value.append(lis[2].split("\n")[0])
        else:
            dic = {'date': jiatin_date,
                   'value': jiatin_value}
            df = pd.DataFrame(dic)
            df['id'] = index
            index = lis[0]
            jiatin_date = []
            jiatin_value = []

            print(df)
