import sys
import sqlite3
from datetime import datetime
from dearpygui.core import *
from dearpygui.simple import *

def close(sender, data):
    delete_item("Supervisor Interface")

def exit_main_window (sender, data):
    stop_dearpygui
    sys.exit()
   

# get selected data from cell
def tablePrinter(sender, data):
    coordList = get_table_selections("Table Supervisor")
    row = 0
    for coordinates in coordList:
        row = coordinates[0]
    
    with window("Supervisor Interface"):
        set_value("Supervisor ID", get_table_item("Table Supervisor", row, 0))
        set_value("Supervisor Name", get_table_item("Table Supervisor", row, 1))
        set_value("Supervisor Type", get_table_item("Table Supervisor", row, 2))
        set_value("Supervisor Email", get_table_item("Table Supervisor", row, 3))
   
def clear_sup_interface(sender, data):
     with window("Supervisor ID"):
        set_value("Supervisor Name", "")
        set_value("Supervisor Name", "")
        set_value("Supervisor Type", "Teacher")
        set_value("Supervisor Email", "")
        clear_table("Table Supervisor")
        items = sup_display_data("select * from Supervisors;")
        for item in items:
            add_row("Table Supervisor", [item[0], item[1], item[2],item[3]])

# Display data from sqllite to the dearpygui table
def sup_display_data(str_select):
    conn = sqlite3.connect('miniprojdatabase.db')
    c =conn.cursor()
    c.execute(str_select)
    items = c.fetchall()
    return items
    conn.commit()
    conn.close()
    
# insert data in the table        
def sup_add_data(str_insert):
    conn = sqlite3.connect('miniprojdatabase.db')
    c = conn.cursor()
    c.execute(str_insert)
    conn.commit()
    # clear contents of the supervisor form
    with window("Supervisor Interface"):
                if (get_value("Supervisor Name")==""):
                    add_text("Please fill in the name")
                elif (get_value("Supervisor Email")==""):
                    add_text("Please fill in the email")
                else:
                    add_text("Data successfully updated")
                    set_value("Supervisor Name", "")
                    set_value("Supervisor Type", "Teacher")
                    set_value("Supervisor Email", "")
                    clear_table("Table Supervisor")
                    items = sup_display_data("select * from Supervisors;")
                    for item in items:
                         add_row("Table Supervisor", [item[0], item[1], item[2],item[3]])
    conn.close()

    # insert data in the table        
def sup_update_data(str_update):
    conn = sqlite3.connect('miniprojdatabase.db')
    c = conn.cursor()
    c.execute(str_update)
    conn.commit()
    # clear contents of the supervisor form
    with window("Supervisor Interface"):
                if (get_value("Supervisor Name")==""):
                    add_text("Please fill in the name")
                elif (get_value("Supervisor Email")==""):
                    add_text("Please fill in the email")
                else:
                    add_text("Data successfully updated")
                    set_value("Supervisor Name", "")
                    set_value("Supervisor Type", "Teacher")
                    set_value("Supervisor Email", "")
                    clear_table("Table Supervisor")
                    items = sup_display_data("select * from Supervisors;")
                    for item in items:
                         add_row("Table Supervisor", [item[0], item[1], item[2],item[3]])
    conn.close()
    
# Delete data in the table        
def sup_del_data(str_delete):
    conn = sqlite3.connect('miniprojdatabase.db')
    c = conn.cursor()
    c.execute(str_delete)
    conn.commit()
    # clear contents of the supervisor form
    with window("Supervisor Interface"):
                if (get_value("Supervisor Name")==""):
                    add_text("Please fill in the name")
                elif (get_value("Supervisor Email")==""):
                    add_text("Please fill in the email")
                else:
                    add_text("Data successfully updated")
                    set_value("Supervisor Name", "")
                    set_value("Supervisor Type", "Teacher")
                    set_value("Supervisor Email", "")
                    clear_table("Table Supervisor")
                    items = sup_display_data("select * from Supervisors;")
                    for item in items:
                         add_row("Table Supervisor", [item[0], item[1], item[2],item[3]])
    conn.close()

#window object settings
set_main_window_size(1366,768)
set_main_window_pos(0, 0)
set_global_font_scale(1)
set_theme("Dark  ")
set_style_window_padding(30,30)

def sup_Interface():    
    with window("Supervisor Interface", width=1000, height=575, no_resize = True, no_move = False, no_close=True):
        #add_drawing("suplogo", width=48, height=48) #create some space for the image
        #draw_image("suplogo", "D:\Python Projects\supicon.png", [0,0], [48,48])
        add_text("This Section is to Add/Edit/Delete Supervisors", color=[215,122,13])
        conn = sqlite3.connect('miniprojdatabase.db')
        c = conn.cursor()
        add_separator()
        set_window_pos("Supervisor Interface", 200, 60)
        add_input_text("Supervisor ID", width=1)
        #Hide ID field
        hide_item("Supervisor ID")
        add_spacing(count=5)
        add_input_text("Supervisor Name", width=415)
        add_spacing(count=5)
        suptype = ["Teacher", "Admin", "Assistant", "Club member"]
        add_combo("Supervisor Type", items=suptype, default_value="Teacher", width=415)
        add_spacing(count=5)
        add_input_text("Supervisor Email", width=415)
        add_spacing(count=5)
        add_button("Add", callback=lambda: sup_add_data("Insert into Supervisors(Supervisor_Name, Supervisor_Specialization, Supervisor_Email) values('" + get_value("Supervisor Name") + "','" + get_value("Supervisor Type") + "','" + get_value("Supervisor Email") + "');"))
        add_same_line()
        add_button("Update", callback=lambda: sup_edit_data("update Supervisors SET Supervisor_Name= '" + get_value("Supervisor Name") + "', Supervisor_Specialization= '" + get_value("Supervisor Type") + "', Supervisor_Email= '" + get_value("Supervisor Email") + "' where Supervisor_ID=" + get_value("Supervisor ID") + ";"))
        add_same_line()
        add_button("Delete", callback=lambda: sup_del_data("Delete from Supervisors where Supervisor_ID = "  + get_value("Supervisor ID")))
        add_same_line()
        add_button("Clear", callback= clear_sup_interface)
        add_same_line()
        add_button("Close", callback=close)
        add_spacing(count=5)
        add_table("Table Supervisor", ["ID", "Name", "type", "Email"],callback=tablePrinter)
        items = sup_display_data("select * from Supervisors;")
        for item in items:
            add_row("Table Supervisor", [item[0], item[1], item[2],item[3]])


# get selected data from cell
def tablePrinter2(sender, data):
    coordList = get_table_selections("Table Volunteer")
    row = 0
    for coordinates in coordList:
        row = coordinates[0]
    
    with window("Volunteer Interface"):
        set_value("Volunteer ID", get_table_item("Table Volunteer", row, 0))
        set_value("Volunteer Name", get_table_item("Table Volunteer", row, 1))
        set_value("Volunteer Year", get_table_item("Table Volunteer", row, 2))
        set_value("Volunteer Email", get_table_item("Table Volunteer", row, 3))
   
def clear_vol_interface(sender, data):
     with window("Volunteer Interface"):
        set_value("Volunteer ID", "")
        set_value("Volunteer Name", "")
        set_value("Volunteer Year", "10")
        set_value("Volunteer Email", "")
        clear_table("Table Volunteer")
        items = vol_display_data("select * from Volunteers;")
        for item in items:
            add_row("Table Volunteer", [item[0], item[1], item[2],item[3]])

# Display data from sqllite to the dearpygui table
def vol_display_data(str_select):
    conn = sqlite3.connect('miniprojdatabase.db')
    c =conn.cursor()
    c.execute(str_select)
    items = c.fetchall()
    return items
    conn.commit()
    conn.close()
    
# insert data in the table        
def vol_add_data(str_insert):
    x = 0;
    conn = sqlite3.connect('miniprojdatabase.db')
    c = conn.cursor()
    c.execute(str_insert)
    conn.commit()
    with window("Volunteer Interface"):
                if (get_value("Volunteer Name")==""):
                    add_text("Please fill in the name")
                elif (get_value("Volunteer Email")==""):
                    add_text("Please fill in the email")
                else:
                    add_text("Data successfully added")
                    set_value("Volunteer ID", "")
                    set_value("Volunteer Name", "")
                    set_value("Volunteer Year", "10")
                    set_value("Volunteer Email", "")
                    clear_table("Table Volunteer")
                    x = 1
                    items = vol_display_data("select * from Volunteers;")
                    for item in items:
                        add_row("Table Volunteer", [item[0], item[1], item[2],item[3]])
    conn.close()

    # insert data in the table        
def vol_edit_data(str_update):
    conn = sqlite3.connect('miniprojdatabase.db')
    c = conn.cursor()
    c.execute(str_update)
    conn.commit()
    # clear contents of the supervisor form
    with window("Volunteer Interface"):
                if (get_value("Volunteer Name")==""):
                    add_text("Please fill in the name")
                elif (get_value("Volunteer Email")==""):
                    add_text("Please fill in the email")
                else:
                    add_text("Data successfully updated")
                    set_value("Volunteer ID", "")
                    set_value("Volunteer Name", "")
                    set_value("Volunteer Year", "10")
                    set_value("Volunteer Email", "")
                    clear_table("Table Volunteer")
                    x = 1
                    items = vol_display_data("select * from Volunteers;")
                    for item in items:
                        add_row("Table Volunteer", [item[0], item[1], item[2],item[3]])
    conn.close()
   
# Delete data in the table        
def vol_del_data(str_delete):
    conn = sqlite3.connect('miniprojdatabase.db')
    c = conn.cursor()
    c.execute(str_delete)
    conn.commit()
    # clear contents of the supervisor form
    with window("Volunteer Interface"):
                if (get_value("Volunteer Name")==""):
                    add_text("Please fill in the name")
                elif (get_value("Volunteer Email")==""):
                    add_text("Please fill in the email")
                else:
                    add_text("Data successfully deleted")
                    set_value("Volunteer ID", "")
                    set_value("Volunteer Name", "")
                    set_value("Volunteer Year", "10")
                    set_value("Volunteer Email", "")
                    clear_table("Table Volunteer")
                    x = 1
                    items = vol_display_data("select * from Volunteers;")
                    for item in items:
                        add_row("Table Volunteer", [item[0], item[1], item[2],item[3]])
    conn.close()

#window object settings
set_main_window_size(1366,768)
set_main_window_pos(0, 0)
set_global_font_scale(1)
set_theme("Dark  ")
set_style_window_padding(30,30)

def vol_Interface():    
    with window("Volunteer Interface", width=1000, height=575, no_resize = True, no_move = False, no_close=True):
        #add_drawing("suplogo", width=48, height=48) #create some space for the image
        #draw_image("suplogo", "D:\Python Projects\supicon.png", [0,0], [48,48])
        conn = sqlite3.connect('miniprojdatabase.db')
        c = conn.cursor()
        add_text("This Section is to Add/Edit/Delete Volunteers", color=[215,122,13])
        add_separator()
        set_window_pos("Volunteer Interface", 200, 60)
        add_input_text("Volunteer ID", width=1)
        #Hide ID field
        hide_item("Volunteer ID")
        add_spacing(count=5)
        add_input_text("Volunteer Name", width=415)
        add_spacing(count=5)
        volyear = ["10", "11", "12"]
        add_combo("Volunteer Year", items=volyear, default_value="10", width=415)
        add_spacing(count=5)
        add_input_text("Volunteer Email", width=415)
        add_spacing(count=5)
        add_button("Add", callback=lambda: vol_add_data("Insert into Volunteers(Volunteer_Name, Volunteer_Year, Volunteer_Email) values('" + get_value("Volunteer Name")+ "','" + get_value("Volunteer Year") + "','" + get_value("Volunteer Email") + "');"))
        add_same_line()
        add_button("Update", callback=lambda: vol_edit_data("update Volunteers SET Volunteer_Name= '" + get_value("Volunteer Name") + "', Volunteer_Year= '" + get_value("Volunteer Year") + "', Volunteer_Email='" + get_value("Volunteer Email") + "' where Volunteer_ID=" + get_value("Volunteer ID") + ";"))
        add_same_line()
        add_button("Delete", callback=lambda: vol_del_data("Delete from Volunteers where Volunteer_ID = "  + get_value("Volunteer ID")))
        add_same_line()
        add_button("Clear", callback= clear_vol_interface)
        add_same_line()
        add_button("Close", callback=close)
        add_spacing(count=5)
        add_table("Table Volunteer", ["ID", "Name", "year", "Email"],callback=tablePrinter2)
        items = vol_display_data("select * from Volunteers;")
        for item in items:
            add_row("Table Volunteer", [item[0], item[1], item[2],item[3]])


def tablePrinter3(sender, data):
    coordList = get_table_selections("Table Activity")
    row = 0
    for coordinates in coordList:
        row = coordinates[0]
    
    with window("Activity Interface"):
        set_value("Activity ID", get_table_item("Table Activity", row, 0))
        set_value("Activity Name", get_table_item("Table Activity", row, 1))
        set_value("Activity Supervisor", get_table_item("Table Activity", row, 2))
        set_value("Activity Location", get_table_item("Table Activity", row, 3))
        set_value("Activity Time", get_table_item("Table Activity", row, 4))
   
def clear_act_interface(sender, data):
     with window("Activity Interface"):
            set_value("Activity ID", "")
            set_value("Activity Name", "")
            set_value("Activity Supervisor", "")
            set_value("Activity Location", "PE hall")
            set_value("Activity Time", "Lunch")
            clear_table("Table Activity")
            items = act_display_data("select * from Activity;")
            for item in items:
                add_row("Table Activity", [item[0], item[1], item[2],item[3],item[4]])

# Display data from sqllite to the dearpygui table
def act_display_data(str_select):
    conn = sqlite3.connect('miniprojdatabase.db')
    c =conn.cursor()
    c.execute(str_select)
    items = c.fetchall()
    return items
    conn.commit()
    conn.close()
    
# insert data in the table        
def act_add_data(str_insert):
    conn = sqlite3.connect('miniprojdatabase.db')
    c = conn.cursor()
    c.execute(str_insert)
    conn.commit()
    with window("Activity Interface"):
        if (get_value("Activity Name")==""):
                    add_text("Please fill in the name")
        else:
            add_text("Data added")
            set_value("Activity ID", "")
            set_value("Activity Name", "")
            set_value("Activity Location", "PE hall")
            set_value("Activity Time", "Lunch")
            clear_table("Table Activity")
            items = act_display_data("select * from Activity;")
            for item in items:
                add_row("Table Activity", [item[0], item[1], item[2],item[3],item[4]])
    conn.close()

    # insert data in the table        
def act_edit_data(str_update):
    conn = sqlite3.connect('miniprojdatabase.db')
    c = conn.cursor()
    c.execute(str_update)
    conn.commit()
    # clear contents of the supervisor form
    with window("Activity Interface"):
        if (get_value("Activity Name")==""):
                    add_text("Please fill in the name")
        else:
            add_text("Data updated")
            set_value("Activity ID", "")
            set_value("Activity Name", "")
            set_value("Activity Supervisor", "")
            set_value("Activity Location", "PE hall")
            set_value("Activity Time", "Lunch")
            clear_table("Table Activity")
            items = act_display_data("select * from Activity;")
            for item in items:
                add_row("Table Activity", [item[0], item[1], item[2],item[3], item[4]])
    conn.close()
   
# Delete data in the table        
def act_del_data(str_delete):
    conn = sqlite3.connect('miniprojdatabase.db')
    c = conn.cursor()
    c.execute(str_delete)
    conn.commit()
    # clear contents of the supervisor form
    with window("Activity Interface"):
        if (get_value("Activity Name")==""):
                    add_text("Please fill in the name")
        else:
            add_text("Data deleted")
            set_value("Activity ID", "")
            set_value("Activity Name", "")
            set_value("Activity Supervisor", "")
            set_value("Activity Location", "PE hall")
            set_value("Activity Time", "Lunch")
            clear_table("Table Activity")
            items = act_display_data("select * from Activity;")
            for item in items:
                add_row("Table Activity", [item[0], item[1], item[2],item[3],item[4]])
    conn.close()

    #window object settings
set_main_window_size(1366,768)
set_main_window_pos(0, 0)
set_global_font_scale(1)
set_theme("Dark  ")
set_style_window_padding(30,30)

def act_convert(x):
    conn = sqlite3.connect('miniprojdatabase.db')
    c = conn.cursor()
    temp = 0
    actsup = act_display_data("select Supervisors.Supervisor_Name from Supervisors;")
    actsupid = act_display_data("select Supervisors.Supervisor_ID from Supervisors;")
    len1 = actsup.len()
    for i in range(len1):
        if (actsup[i]==x):
            temp = i
            break
    final = 0
    final = actsupid[temp]
    act_add_data("Insert into Activity(Activity_Supervisor) values('" + final + "');")
    return (final)

def act_Interface():    
    with window("Activity Interface", width=1000, height=575, no_resize = True, no_move = False, no_close=True):
        #add_drawing("suplogo", width=48, height=48) #create some space for the image
        #draw_image("suplogo", "D:\Python Projects\supicon.png", [0,0], [48,48])
        conn = sqlite3.connect('miniprojdatabase.db')
        c = conn.cursor()
        add_text("This Section is to Add/Edit/Delete Activities", color=[215,122,13])
        add_separator()
        set_window_pos("Activity Interface", 200, 60)
        add_input_text("Activity ID", width=1)
        #Hide ID field
        hide_item("Activity ID")
        add_spacing(count=5)
        add_input_text("Activity Name", width=415)
        add_spacing(count=5)
        actlocation = ["Pe Hall" , "Presentation Hall" , "Lab" , "Quad" , "Hall Entrance" ]
        acttime = ["Lunch" , "All day" , "day before"]
        actsup = act_display_data("select Supervisors.Supervisor_Name from Supervisors;")
        actsupid = act_display_data("select Supervisors.Supervisor_ID from Supervisors;")
        supsample = ["Bob" , "Jim" , "Alex"]
        add_combo("Activity Supervisor", items=actsup, width=415)
        add_spacing(count=5)
        add_combo("Activity Location", items=actlocation, default_value="PE Hall", width=415)
        add_spacing(count=5)
        add_combo("Activity Time", items=acttime, default_value="Lunch", width=415)
        add_spacing(count=5)
        add_button("Add", callback=lambda: act_add_data("Insert into Activity(Activity_Name, Activity_Location, Activity_Time) values('" + get_value("Activity Name")+ "','" + get_value("Activity Location") + "','" +  get_value("Activity Time") + "');"))
        add_same_line()
        add_button ("Add supervisor", callback = lambda: act_convert(get_value("Activity Supervisor")))
        add_same_line()
        add_button("Update", callback=lambda: act_edit_data("update Activity SET Activity_Name= '" + get_value("Activity Name") + "', Activity_Supervisor= '" + get_value("Activity Supervisor") + "', Activity Location='" + get_value("Activity Location") + "', Activity Time='" + get_value("Activity Time") + "' where Activity_ID=" + get_value("Activity ID") + ";"))
        add_same_line()
        add_button("Delete", callback=lambda: act_del_data("Delete from Activity where Activity_ID = "  + get_value("Activity ID")))
        add_same_line()
        add_button("Clear", callback= clear_act_interface)
        add_same_line()
        add_button("Close", callback=close)
        add_spacing(count=5)
        add_table("Table Activity", ["ID", "Name", "Supervisor", "Location", "Time"],callback=tablePrinter3)
        items = act_display_data("select * from Activity;")
        for item in items:
            add_row("Table Activity", [item[0], item[1], item[2],item[3], item[4]])
        conn.close()

#Main DiaTech Interface (Start Screen)        
with window("Diatech Interface", width=1340, height=680,no_resize = False, no_move = False, no_close=True):
    set_window_pos("Diatech Interface", 0, 0)
    conn = sqlite3.connect('diatechmini.db')
    c =conn.cursor()
    #c.execute("select * from supervisor")
    conn.commit()
    now = datetime.now()
    dt_string = now.strftime("%d %B %Y %H:%M:%S")
    add_text("Welcome! You are sucessfully connected to Di@Tech Database ~ " + str(dt_string), color=[143, 216, 218])        
    conn.close()
    #image logo
    #add_drawing("logo", width=1300, height=550) #create some space for the image
    #draw_image("logo", "a.JPG", [0,0], [1300,550])

    with menu_bar("Main Menu Bar"): 
        with menu("File"):
            add_menu_item("Exit", callback=exit_main_window)

        with menu("Data Entry"):                             # simple
            add_menu_item("Supervisor", callback=sup_Interface)            
            add_menu_item("Volunteer", callback=vol_Interface)
            add_menu_item("Activity", callback=act_Interface)
        with menu("Reports"):                             # simple
            add_menu_item("Supervisor Report")
            add_menu_item("Volunteer Report")
            add_menu_item("Activity Report")

start_dearpygui()

