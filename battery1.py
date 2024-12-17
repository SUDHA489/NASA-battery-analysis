import pandas as pd
import plotly.express as px

#discharging dataset
data = pd.read_csv("discharging.csv") 


filtered_data = data[(data['Time'] >= 0) & (data['Time'] <= 100)] 

filtered_data['Impedance'] = filtered_data['Voltage_load'] / filtered_data['Current_load']

filtered_data['Re'] = filtered_data.apply(lambda row: row['Voltage_load'] / row['Current_load'] if row['Current_load'] < 0.1 else None, axis=1)


filtered_data['Rct'] = filtered_data.apply(lambda row: row['Voltage_load'] / row['Current_load'] if row['Current_load'] > 1.0 else None, axis=1)

fig_impedance = px.line(filtered_data, x='Time', y='Impedance', 
                        title="Impedance Over Time (Filtered Time)", 
                        labels={'Impedance': 'Impedance (Ohms)', 'Time': 'Time (s)'})
fig_impedance.show()

fig_re = px.line(filtered_data, x='Time', y='Re', 
                 title="Re Over Time (Low Current Regions, Filtered Time)", 
                 labels={'Re': 'Electrolyte Resistance (Ohms)', 'Time': 'Time (s)'})
fig_re.show()

fig_rct = px.line(filtered_data, x='Time', y='Rct', 
                  title="Rct Over Time (High Current Regions, Filtered Time)", 
                  labels={'Rct': 'Charge Transfer Resistance (Ohms)', 'Time': 'Time (s)'})
fig_rct.show()



#charging dataset

charging_data = pd.read_csv("charging.csv") 

filtered_charging_data = charging_data[(charging_data['Time'] >= 0) & (charging_data['Time'] <= 100)]

filtered_charging_data['Impedance'] = filtered_charging_data['Voltage_charge'] / filtered_charging_data['Current_charge']


filtered_charging_data['Re'] = filtered_charging_data.apply(lambda row: row['Voltage_charge'] / row['Current_charge'] if row['Current_charge'] < 0.1 else None, axis=1)

filtered_charging_data['Rct'] = filtered_charging_data.apply(lambda row: row['Voltage_charge'] / row['Current_charge'] if row['Current_charge'] > 1.0 else None, axis=1)

fig_impedance_charging = px.line(filtered_charging_data, x='Time', y='Impedance', 
                                 title="Impedance Over Time (Charging)", 
                                 labels={'Impedance': 'Impedance (Ohms)', 'Time': 'Time (s)'})
fig_impedance_charging.show()

fig_re_charging = px.line(filtered_charging_data, x='Time', y='Re', 
                          title="Re Over Time (Low Current Regions - Charging)", 
                          labels={'Re': 'Electrolyte Resistance (Ohms)', 'Time': 'Time (s)'})
fig_re_charging.show()

fig_rct_charging = px.line(filtered_charging_data, x='Time', y='Rct', 
                           title="Rct Over Time (High Current Regions - Charging)", 
                           labels={'Rct': 'Charge Transfer Resistance (Ohms)', 'Time': 'Time (s)'})
fig_rct_charging.show()