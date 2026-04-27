from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt
import logging

logging.getLogger('matplotlib').setLevel(logging.ERROR)


days = np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri'])
absences = np.array([0, 0, 0, 0, 0])

def update_graph(event):
   
    try:
        day_index = int(document.querySelector("#day-select").value)
        input_value = document.querySelector("#absence-input").value
        
        if input_value == "":
            return
            
     
        absences[day_index] = int(input_value)
        
       
        plt.figure(figsize=(6,4)) 
        plt.plot(days, absences, marker='o') 
        
        plt.title("Weekly Attendance (Absences)")
        plt.xlabel("Days")
        plt.ylabel("Number of Absences")
        
       
        document.querySelector("#plot-target").innerHTML = "" 
        display(plt.gcf(), target="plot-target")
    except Exception:
        pass

# Initial run to show the empty graph
update_graph(None)
