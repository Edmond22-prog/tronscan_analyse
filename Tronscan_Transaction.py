import pandas as pd


df = pd.read_csv("export.csv", sep=",")
# Montant total des transactions
print(df["quant"].sum())

# Recuperation des differents block de transaction
blocks = df["block"].unique()
# print(blocks)

# Recuperation des donnees 'from_address', 'to_address' et 'quant' ou le block de transaction
# est egale un premier block de notre liste de blocks
# data = df.loc[df["block"] == blocks[0], ["from_address", "to_address", "quant"]]
# for i in range(len(data)):
#     print(data["from_address"][i], data["to_address"][i], data["quant"][i],)

for block in blocks:
    data = df.loc[df["block"] == block, ["from_address", "to_address", "quant"]]
    print(f"Transaction du block {block} \n")
    print(data)
    # for i in range(len(data)):
    #     print("{} ==> {}, montant : {}".format(data['from_address'][i], data['to_address'][i], data['quant'][i]))
    # print("\n")

# print(len(df["from_address"].unique()))
# print(len(df["to_address"].unique()))
# print(len(df["block"].unique()))