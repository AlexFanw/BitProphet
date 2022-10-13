import pandas as pd
from tqdm import tqdm

def add_extra_feature():
    be = pd.read_csv('datasets/bitcoin_extra.csv')
    be_list = {}
    for index, row in be.iterrows():
        row[0] = row[0][5:7] + "/" + row[0][8:10] + "/" + row[0][0:4]
        be_list[row[0]] = [row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
    # print(be_list)

    bc = pd.read_csv('datasets/bitstamp_cleaned.csv')
    bc['txCount'] = 0
    bc['generatedCoins'] = 0
    bc['fees'] = 0
    bc['activeAddresses'] = 0
    bc['averageDifficulty'] = 0
    bc['blockSize'] = 0
    bc['blockCount'] = 0
    for index, row in tqdm(bc.iterrows(), total=bc.shape[0]):
        dt = row[1][0:10]
        if dt in be_list.keys():
            row[9] = be_list[dt][0]
            row[10] = be_list[dt][1]
            row[11] = be_list[dt][2]
            row[12] = be_list[dt][3]
            row[13] = be_list[dt][4]
            row[14] = be_list[dt][5]
            row[15] = be_list[dt][6]
            # print(row)
        bc.iloc[index] = row
    bc.to_csv('datasets/bitcoin.csv')

def daily_data():
    import warnings
    warnings.filterwarnings('ignore')
    full_data = pd.read_csv('datasets/res0.csv')
    date = ""
    simple_data = pd.DataFrame(columns=[col for col in full_data])
    for index, row in tqdm(full_data.iterrows(), total=full_data.shape[0]):
        row_date = row[1][0:10]
        if int(row[1][6:10]) == 2018:
            break
        if row_date == date:
            continue
        else:
            simple_data = simple_data.append(row)
            date = row_date
    simple_data.to_csv('datasets/daily_bitcoin.csv')

def split_train_test():
    bt = pd.read_csv("datasets/bitcoin.csv")
    bt.head(1827).to_csv("datasets/train_bitcoin.csv", index=False)
    bt.tail(365).to_csv("datasets/test_bitcoin.csv", index=False)

if __name__ == "__main__":
    split_train_test()
