from kafka import KafkaConsumer
import json
import time
import datetime
import collections
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np


##############################################################################
# Initial configurations

plt.style.use("ggplot")


##############################################################################
# Buffers

BUFFER_SIZE = 50
INITIAL_VALUE = 0
VALUE_BUFFER = collections.deque()
TIME_BUFFER = collections.deque()


def create_value_buffer(n_stored: int = BUFFER_SIZE):
    global VALUE_BUFFER
    VALUE_BUFFER = collections.deque(maxlen=n_stored)
    
    # Initializes empty buffer
    for i in range(BUFFER_SIZE):
        VALUE_BUFFER.append(INITIAL_VALUE)
        
    print("Value buffer initialized!")


def create_time_buffer(n_stored: int = BUFFER_SIZE):
    global TIME_BUFFER
    TIME_BUFFER = collections.deque(maxlen=n_stored)
    
    # Initializes empty buffer
    for i in range(BUFFER_SIZE):
        TIME_BUFFER.append(INITIAL_VALUE)
        
    print("Time buffer initialized!")


def create_buffers():
    create_value_buffer()
    create_time_buffer()
    
##############################################################################
# Kafka consumer


def run_consumer():
    global VALUE_BUFFER
    
    consumer = KafkaConsumer(
        'topic_test',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-id',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    print("Message read - " + str(datetime.datetime.now()))

    # Plotting line initialization
    line = []

    for event in consumer:
        event_data = event.value
        
        # Fills the new values to the buffer
        values = [val["p"] for val in json.loads(event_data)["data"]]
        times = [val["t"] for val in json.loads(event_data)["data"]]
        for val in values:
            VALUE_BUFFER.append(val)
        for t in times:
            TIME_BUFFER.append(t)
        
        newest_values = [val if val != INITIAL_VALUE else values[0] for val in list(VALUE_BUFFER)]
        newest_times = [t if t != INITIAL_VALUE else times[0] for t in list(TIME_BUFFER)]
        
        line = plot_graph(y=newest_values, x=newest_times, line=line)
        
        time.sleep(0.5)

##############################################################################
# Plotting


def plot_graph(y,
               x=[],
               line=[]):
    
    # If no data is provided, plotting cannot be done
    if not y:
        return []
    
    # Obtains sorting order similar to np.argsort() and sort based on that
    order = [i[0] for i in sorted(enumerate(x), key=lambda x: x[1])]
    ordered_x = [x[i] for i in order]
    ordered_y = [y[i] for i in order]
    # ordered_x_date = [
    #     matplotlib.dates.date2num(datetime.datetime.fromtimestamp(
    #         float(x[i]) / 1000.0
    #     )) for i in order]
    
    if line == []:
        plt.ion()       # interactive mode
        fig = plt.figure(figsize=(6, 3))
        ax = fig.add_subplot(111)
        line, = ax.plot(x, y, '-o', alpha=0.8)
        
        plt.ylabel("value")
        plt.xlabel("time")
        plt.title("Real time value")
        plt.show()

    # Updates the values and the axis bounds
    line.set_xdata(ordered_x)
    line.set_ydata(ordered_y)
    if line.axes.get_ylim()[0] <= np.percentile(y, 5) or line.axes.get_ylim()[0] >= np.percentile(y, 95):
        plt.ylim([
            np.min(y) - np.std(y),
            np.max(y) + np.std(y)
        ])
    if line.axes.get_xlim()[0] <= np.percentile(x, 5) or line.axes.get_xlim()[0] >= np.percentile(x, 95):
        plt.xlim([
            np.min(x) - np.std(x),
            np.max(x) + np.std(x)
        ])
    
    plt.pause(0.1)
    
    return line

##############################################################################

        
def main():
    create_buffers()
    run_consumer()
    

if __name__ == "__main__":
    main()
