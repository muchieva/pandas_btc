from unittest.mock import inplace

import pandas as pd


def get_crypto(titles):
    df_arr = []
    for title in titles:
        tmpdf = pd.read_csv(f'files/{title}.csv')
        tmpdf['Date'] = pd.to_datetime(tmpdf['Date'])
        tmpdf.set_index('Date', inplace=True)
        tmpdf = tmpdf[['Close']].rename(columns={'Close': title})
        df_arr.append(tmpdf)
        merged_df = df_arr[0].join(df_arr[1:], how='outer')
        merged_df.ffill()
        merged_df = merged_df.fillna(0)
    return merged_df