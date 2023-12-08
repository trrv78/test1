# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import requests

# Streamlit app to display sensor data
st.title("ESP8266 Sensor Data")

# ESP8266 server URL (replace with the actual IP address assigned to the ESP8266 AP)
esp8266_url = "http://192.168.4.1"

# Function to fetch sensor data from ESP8266
def get_sensor_data():
    try:
        response = requests.get(esp8266_url)
        if response.status_code == 200:
            return response.text.split(',')
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Main loop to continuously update sensor data
while True:
    sensor_data = get_sensor_data()
    
    if sensor_data:
        smoke_sensor_value, motion_sensor_value = sensor_data
        st.write(f"Smoke Sensor Value: {smoke_sensor_value}")
        st.write(f"Motion Sensor Value: {motion_sensor_value}")
