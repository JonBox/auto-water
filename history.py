import csv
from datetime import datetime
import matplotlib.pyplot as plt
import io
import matplotlib.dates as mdates
from PIL import Image

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


    def write_status_to_file(self, is_on, value, voltage):
        with open(self.filename, mode= 'a', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([datetime.now(), is_on, value, voltage])

    def read_status_from_file(self):
        status_file = open(self.filename, "r")
        return status_file.read()

    def fig2img(self, fig):
        buf = io.BytesIO()
        fig.savefig(buf)
        buf.seek(0)
        img = Image.open(buf)
        return img

    def chart_data(self):
        dates = []
        is_on = []
        values = []
        voltages = []
        status_file = open(self.filename, "r")
        reader = csv.reader(status_file, delimiter=' ', quotechar='|')

        rowcount = 0
        for row in reader:
            rowcount += 1
            # skip header row
            if rowcount == 1:
                continue
            # assemble data
            dates.append(datetime.fromisoformat(row[0]))
            is_on.append(1 if row[1] == 'True' else 0)
            values.append(float(row[2]))
            voltages.append(float(row[3]))
        # Plotting Line Graph
        plt.figure()
        plt.title("Watering and Soil Moisture")
        plt.xlabel('Date')
        plt.plot(dates, is_on, label='Water On', scaley=True)
        #plt.plot(dates, values, '-.', label='Moisture Value', scaley=True)
        plt.plot(dates, voltages, '-.', label='Sensor Voltage', scaley=True)
        plt.legend()

        ax = plt.gca()
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator)
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        plt.gcf().autofmt_xdate()

        # Getting the current figure and save it in the variable.
        fig = plt.gcf()

        # Create a Function for Converting a figure to a PIL Image.
        img = self.fig2img(fig)
        plt.close(fig)
        image_filename = f'{datetime.now()}.png'
        img.save(image_filename)
        return image_filename