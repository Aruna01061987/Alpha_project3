import csv

path = r"C:\Users\Admin\PycharmProjects\Alpha_project3\files_directory\csv _files\vaccination_data.csv"
from collections import defaultdict
d = defaultdict(list)
with open(path) as file:
    r_obj = csv.DictReader(file)
    header = next(r_obj)

    for row in r_obj:
        if row["DATE_UPDATED"]:
