# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 10:12:02 2022

@author: user
"""

import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

####### Screen Setting ##################
screen = Tk()
screen.geometry('800x1100')
screen.configure(bg = '#000000')
screen.resizable(0, 0)
screen.title("Cops Yield Prediction")


####### Functions ############################
def predict():
    Area = Area_text.get()
    Item = Item_text.get()
    average_rain_fall_mm_per_year = average_rain_fall_mm_per_year_text.get()
    Pesticides_Value = Pesticides_Value_text.get()
    avg_temp = avg_temp_text.get()
    
    while Area==" " or Item==" " or average_rain_fall_mm_per_year==" " or Pesticides_Value==" " or avg_temp==" ":
        error1_lbl["text"] = "Please fill in the gaps correctlly!"
        
        
    while Area not in le_Area_mapping:
        error2_lbl["text"] = "Your country is not in our dataset!"
        
    while Item not in le_Item_mapping:
        error3_lbl["text"] = "Your item is not in our dataset!"
        
    new_test_data = {'Area': [Area],
                 'Item': [Item],
                 'average_rain_fall_mm_per_year': [average_rain_fall_mm_per_year],
                 'Pesticides Value': [Pesticides_Value],
                 'avg_temp': [avg_temp]}
    
    new_test_data.update({'Area': [le_Area_mapping[Area]], 'Item': [le_Item_mapping[Item]]})
    
    new_test_df = pd.DataFrame(new_test_data)
    # Pre processing
    scalar = StandardScaler()
    scalar_new_test = scalar.fit_transform(new_test_df)
    # Training
    model = RandomForestRegressor(n_estimators=200, max_depth=12, random_state=0).fit(train_X, train_Y)
    # Predict labels
    predicted_label = model.predict(scalar_new_test)
    
    prediction_lbl["text"] = f"Crops Yield amount: \n {np.squeeze(predicted_label)[()]}"
    
    # pie chart
    x = np.concatenate((predicted_label, np.array([labels.max()])))
    
    label = ['Your Yield', 'Maximum Yield']
    palette_color = sns.color_palette('bright')
    fig, ax = plt.subplots()
    ax.pie(x, labels = label, colors =palette_color )
    ax.set_title('Survery responses')

    canvas = FigureCanvasTkAgg(fig, master = screen)  
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, screen)
    toolbar.update()

######## Labels and buttons Setting ##################

### Area
Area_lbl = Label(screen, text = "Enter Your Country", font = "thahoma 15",
                     fg = "#FFFF69", bg = '#000000')
Area_lbl.pack(pady = 10)

Area_text= StringVar()
Area_text_entry = Entry(screen, textvariable = Area_text, bg = '#CDCDB7')
Area_text_entry.pack(pady = 10)


### Error2 label
error2_lbl = Label(screen, text = '', font = "thahoma 15",
                     fg = "#9898F5", bg = "#000000")
error2_lbl.pack(pady = 10)


### Item
Item_lbl = Label(screen, text = "Enter Your Item", font = "thahoma 15",
                     fg = '#FFFF69', bg = '#000000')
Item_lbl.pack(pady = 10)

Item_text = StringVar()
Item_text_entry = Entry(screen, textvariable = Item_text, bg = '#CDCDB7')
Item_text_entry.pack(pady = 10)


### Error3 label
error3_lbl = Label(screen, text = '', font = "thahoma 15",
                     fg = "#9898F5", bg = "#000000")
error3_lbl.pack(pady = 10)


### average_rain_fall_mm_per_year
average_rain_fall_mm_per_year_lbl = Label(screen, text = "Enter the average rain fall", font = "thahoma 15",
                     fg = "#FFFF69", bg = '#000000')
average_rain_fall_mm_per_year_lbl.pack(pady = 10)


average_rain_fall_mm_per_year_text = StringVar()
average_rain_fall_mm_per_year_text_entry = Entry(screen, textvariable = average_rain_fall_mm_per_year_text, bg = '#CDCDB7')
average_rain_fall_mm_per_year_text_entry.pack(pady = 10)


### Pesticides_Value
Pesticides_Value_lbl = Label(screen, text = "Enter the Pesticides Value", font = "thahoma 15",
                     fg = "#FFFF69", bg = '#000000')
Pesticides_Value_lbl.pack(pady = 10)


Pesticides_Value_text = StringVar()
Pesticides_Value_text_entry = Entry(screen, textvariable = Pesticides_Value_text, bg = '#CDCDB7')
Pesticides_Value_text_entry.pack(pady = 10)


### avg_temp
avg_temp_lbl = Label(screen, text = "Enter the average temperature", font = "thahoma 15",
                     fg = "#FFFF69", bg = '#000000')
avg_temp_lbl.pack(pady = 10)


avg_temp_text = StringVar()
avg_temp_text_entry = Entry(screen, textvariable = avg_temp_text, bg = '#CDCDB7')
avg_temp_text_entry.pack(pady = 10)


### prediction label
prediction_lbl = Label(screen, text = '', font = "thahoma 15",
                     fg = "deep pink", bg = "#000000")
prediction_lbl.pack(pady = 10)



### Error1 label
error1_lbl = Label(screen, text = '', font = "thahoma 15",
                     fg = "#9898F5", bg = "#000000")
error1_lbl.pack(pady = 10)


### Buttons

predict_btn = Button(screen, text = 'Predict', width = 12, cursor = "hand1", 
                    command = predict, bg = "#FFFF69", fg = "black",activebackground = 'deep pink',
                    font = "thahoma 15")
predict_btn.pack()



screen.mainloop()