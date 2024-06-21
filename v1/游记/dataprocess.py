import pandas as pd

# 读取CSV文件
file_path = '携程游记_莆田.csv'
data = pd.read_csv(file_path)

# 提取前三篇游记内容
# 假设游记内容在名为 'content' 的列中
first_three_travel_notes = data.iloc[:, 1].head(3)  # 假设内容在第二列

# 将前三篇游记写入一个文本文件
with open('莆田游记.txt', 'w', encoding='utf-8') as file:
    for i, note in enumerate(first_three_travel_notes, start=1):
        file.write(f"第{i}篇游记:\n{note}\n\n")

print("前三篇游记已写入到 莆田游记.txt 文件中。")
