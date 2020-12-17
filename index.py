import pandas as pd
incentives_df = pd.read_excel('C:/Python27/My_Scripts/vamsi/interview/New folder/incentives.xlsx')
incentive_upc_df = pd.read_excel('C:/Python27/My_Scripts/vamsi/interview/New folder/incentive_upc.xlsx')
Transactions_url = "https://s3.amazonaws.com/inmar-interview-dataanalyst/Rawdata/Transactions.txt"
Transactions_df = pd.read_csv(Transactions_url, sep='|')
Transaction_item_url = "https://s3.amazonaws.com/inmar-interview-dataanalyst/Rawdata/Transaction_item.txt"
Transaction_item_df = pd.read_csv(Transaction_item_url, sep='|')
Transaction_items1_url = "https://s3.amazonaws.com/inmar-interview-dataanalyst/Rawdata/Transaction_items1.txt"
Transaction_items1_df = pd.read_csv(Transaction_items1_url, sep='|')
incentives_df.columns.str.lower()
incentive_upc_df.columns.str.lower()
Transactions_df.columns.str.lower()
Transaction_item_df.columns.str.lower()
Transaction_items1_df.columns.str.lower()
Transaction_items1_df.rename(columns={'Product_id':'incentive_id'})
# print(incentives_df)
# print(incentive_upc_df)
# print(Transactions_df)
# print(Transaction_item_df)
# print(Transaction_items1_df)
# user = incentives_df.merge(incentive_upc_df, on=['incentive_id'], how='inner').merge(Transaction_items1_df, on=['product_id'], how'inner')
merged_df = pd.merge(incentives_df,incentive_upc_df, on='incentive_id')
final_merged = pd.merge(merged_df, Transaction_items1_df, on='incentive_id')
print(final_merged)