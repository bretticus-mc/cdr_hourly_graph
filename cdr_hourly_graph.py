import csv
import time
from matplotlib import pyplot as plt

# converts call origination time from Unix epoch to UTC hour
def get_call_hour(cdr):
    epoch_timestamp = cdr[4]
    hour = time.strftime("%H", time.gmtime(int(epoch_timestamp)))
    return hour + "00"

# create horizontal bar chart from hourly call volume
def display_hourly_volme(hourly_volume):
    x = list(hourly_volume.values())
    y = list(hourly_volume.keys())
    # sorts graph in descending order
    x.reverse
    y.reverse

    plt.style.use('ggplot')
    plt.title("Call Volume Per Hour")
    plt.xlabel("Number of Calls")
    plt.ylabel("Hours (UTC)")
    plt.barh(y, x, .8, -4, color="#007acc")
    # displays number of calls in each bar
    for i, v in enumerate(x):
        plt.text(-3, i - 0.2 , ' {} calls'.format(v),color='black', 
                 fontsize=9, fontweight='bold' )
    plt.show()
        

def main():
    hourly_volume = {}
    for hour in range(0, 24):
        hourly_volume[f"{hour:02d}00"] = 0
    
    with open('cdr_one_week.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for cdr in csv_reader:
            call_hour = get_call_hour(cdr)
            hourly_volume[call_hour] += 1
    
    display_hourly_volme(hourly_volume)


if __name__ == "__main__":
    main()