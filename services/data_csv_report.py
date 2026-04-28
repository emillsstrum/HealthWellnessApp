import csv
from models.DateEntity import Day




def write_out_report(filename, data : list):
    # write out report data to csv file
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader() # headers

        for d in data: # loop through list and write out dictionary data
            writer.writerow(d)