# import pandas as pd

# # data (3 characters for the second column only)
# file_path = "problem_titles.txt"
# df = pd.read_fwf(file_path, names=["col", "val"])

# # fill the blank values
# df["col"].ffill(inplace=True)
# # get correct row location
# df["gp"] = df.groupby("col").cumcount()
# # pivot group (0,1) to columns and then transpose. 
# df_ans = df.pivot(index="col", columns="gp", values="val").transpose()

# df_ans.to_csv('questions.csv')


import csv

with open('Problems/problem-1.txt', 'r') as in_file:
    # stripped = (line.strip() for line in in_file)
    # lines = (line.split("\n") for line in stripped if line)
    lines = (line.split("\n") for line in in_file)
    with open('questions.csv', 'a+') as out_file:
        writer = csv.writer(out_file)
        # writer.writerow(('title', 'intro'))
        writer.writerows(lines)