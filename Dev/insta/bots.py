import csv
from csv import reader
import pandas as pd

print('These are probably fakes:')

with open("json/followers_filled.csv", 'r') as f:
    followers = reader(f)
    fol_list = list(followers)

    for i in fol_list[1:]:
        follows = int(i[2])
        followed = int(i[3])
        name = i[1]

        if followed > 0:
            index = follows / followed
        else:
            index = 11
        
        if index > 8:
            print(name)