import csv
from datetime import datetime
# import matplotlib.pyplot as plt
# import io
# import matplotlib.dates as mdates
# from PIL import Image

class history:
    def __init__(self):
        self.filename = 'status.csv'
        # touch file
        with open(self.filename, mode='a+', newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            rowcount = 0
            for row in reader:
                rowcount += 1
            if rowcount == 1:
                writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(["date","water_on", "moisture_value", "moisture_volatage"])



    def write_status_to_file(self, is_on, moisture_readings: dict):
        with open(self.filename, mode= 'a', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            row = [datetime.now(), is_on]
            for reading in moisture_readings.values():
                row.append(reading)
            writer.writerow(row)

    def read_status_from_file(self):
        status_file = open(self.filename, "r")
        return status_file.read()