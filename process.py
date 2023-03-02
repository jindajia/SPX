import array

import pandas as pd
from pathlib import Path

def calculate_avg(days, df):
    df_size = df.shape[0]
    key = str(days)+" Days Avg"
    df[key] = [float(0) for i in range(df_size)]
    for i in range(df_size-days-1):
        a = df.loc[i+1:i+1+days, 'Close'].mean()
        a = str("%.2f" % a)
        df.at[i,key] = float(a)
        # print(a)
    # print("calculate_avg"+str(days))
def print_format(df):
    df_size = df.shape[0]
    for i in range(df_size):
        print('['+str(df.iloc[i]['Open'])+','+str(df.iloc[i]['Close'])+','+str(df.iloc[i]['Low'])+','+str(df.iloc[i]['High'])+'],')
def print_moving_average(days, df):
    key = str(days)+" Days Avg"
    df_size = df.shape[0]
    st = '['
    for i in range(df_size-1):
        st = st +str(df.iloc[i][key]) + ', '
    st = st + str(df.iloc[-1][key])
    st = st + ']'
    print(st)
def print_date(df):
    df_size = df.shape[0]
    st = '['
    for i in range(df_size-1):
        st = st +'\''+ df.iloc[i]['Date'] + '\'' + ', '
    st = st + '\'' + df.iloc[-1]['Date'] + '\''
    st = st + ']'
    print(st)
def main():
    df = pd.read_csv('raw_data.csv',thousands=',')
    df['Close'] = df['Close'].astype(float)
    # df.drop('column_name', axis=1, inplace=True)
    df = df.drop(df.columns[[5,6]], axis=1)
    df_size = df.shape[0]
    calculate_avg(50, df)
    calculate_avg(200, df)
    df = df[:-201]
    df = df.iloc[::-1]
    # print(df)
    print_format(df)
    print_date(df)
    print_moving_average(50, df)
    print_moving_average(200, df)
    filepath = Path('result.csv')
    df.to_csv(filepath, index=False)

if __name__ == "__main__":
    main()