import pandas as pd
filename = 'AEMO_data.csv'
df = pd.read_csv(filename)
#df2 = pd.DataFrame(columns=['nmi', 'meter_serial_number', 'reading', 'reading_datetime', 'file_name'])
meters = []
data=[]
print(df)
for i in range(len(df)):
    #print(i, df.iloc[i][2])
    #import pdb; pdb.set_trace()
    if df.iloc[i][0] == 250:
        data.append({'nmi': df.iloc[i][1], 'meter_serial_number': df.iloc[i][6], 'reading': df.iloc[i][14], 'reading_datetime': df.iloc[i][14], 'file_name': filename} )
print(data)
df2 = pd.DataFrame.from_dict(data) 
df2.to_csv ('export_dataframe.csv', index = False, header=True)
print(df2)

#Meter.objects.bulk_create(meters)
