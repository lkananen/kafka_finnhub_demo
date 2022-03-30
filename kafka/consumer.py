from kafka import KafkaConsumer
import json
import time
import datetime
import collections
import matplotlib.pyplot as plt
import numpy as np


##############################################################################
# Initial configurations

plt.style.use("ggplot")


##############################################################################
# Buffers

BUFFER_SIZE = 20
VALUE_BUFFER = collections.deque()


def create_value_buffer(n_stored: int = BUFFER_SIZE):
    global VALUE_BUFFER
    VALUE_BUFFER = collections.deque(maxlen=n_stored)
    
    # Initializes empty buffer
    for i in range(BUFFER_SIZE):
        VALUE_BUFFER.append(i)
        
    print("Buffer initialized!")


def create_buffers():
    create_value_buffer()
    
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
        for val in values:
            VALUE_BUFFER.append(val)
            
        newest_values = list(VALUE_BUFFER)
        print(newest_values)
        line = plot_graph(newest_values, line=line)
        
        time.sleep(0.5)

##############################################################################
# Plotting


def plot_graph(y,
               x=[],
               line=[]):
    
    # If no data is provided, plotting cannot be done
    if not y:
        return []
    
    # Generates x marks if not provided
    if x == []:
        x = [i for i in range(len(y))]
    
    if line == []:
        plt.ion()       # interactive mode
        fig = plt.figure(figsize=(6, 3))
        ax = fig.add_subplot(111)
        line, = ax.plot(x, y, '-o', alpha=0.8)
        
        plt.ylabel("Y")
        plt.title("Title")
        plt.show()

    # Updates the y-values and the axis bounds
    line.set_ydata(y)
    if np.min(y) <= line.axes.get_ylim()[0] or np.max(y) >= line.axes.get_ylim()[1]:
        plt.ylim([
            np.min(y) - np.std(y),
            np.max(y) + np.std(y)
        ])
    if np.min(x) <= line.axes.get_xlim()[0] or np.max(x) >= line.axes.get_xlim()[1]:
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
