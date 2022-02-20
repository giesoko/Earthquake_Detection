"""
Latest Earthquake Detection App
modularization with function
modularization with package
"""
#First, we can use the following syntax to connect main.py with latest_earthquake package:
#from latest_earthquake import data_extraction, show_data

#we can also use import syntax:
import latest_earthquake

if __name__ == '__main__':
    print('Live Earthquake Detection App')
    result = latest_earthquake.data_extraction()
    latest_earthquake.show_data(result)