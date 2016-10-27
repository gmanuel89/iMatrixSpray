#! python3

########### iMatrixSpray heat bed temperature autotuning GUI - 2016.10.27

######################################################################## GTK GUI (requires Tkinter)
import tkinter, os
#from tkinter import *
from tkinter import messagebox, Label, Button, Entry, Tk, filedialog

# Initialize the outputfolder variable
outputfolder = ""







def select_output_folder_function():
    Tk().withdraw()
    messagebox.showinfo(title="Folder selection", message="Select where to dump the gcode file(s)")
    # Where to save the GCODE file (escape function environment)
    global outputfolder
    outputfolder = filedialog.askdirectory ()
    # Just to confirm...
    Tk().withdraw()
    messagebox.showinfo(title="Folder selected", message="The gcode file(s) will be dumped in '%s'" %(outputfolder))


def dump_gcode_file_function():
    #################### Output folder defined
    if outputfolder != "":
        #################### Temperature
        # Get values from the entry
        temperature_input = temperature_entry.get()
        # Default
        if temperature_input == "":
            temperature_input = 37
        # Convert it to float number
        temperature = float(temperature_input)
        #################### Number of cycles of tuning
        # Get values from the entry
        tuning_cycles_input = tuning_cycles_entry.get()
        # Default
        if tuning_cycles_input == "":
            tuning_cycles_input = 5
        # Convert it to integer number
        tuning_cycles = int(tuning_cycles_input)
        
        
        
        
        
        ################################################################### CODE BLOCKS
        
        ###################################################### Tuning
        tuning_block = [";;;;;;;;;; temperature autotuning, cycles (C) of temperature (S) ramping", "\n", "M303 E-1 C%s S%s" %(tuning_cycles, temperature), "\n\n"]
        
        
        
        
        
        ###################################################### Tuning save
        tuning_save_block = [";;;;;;;;;; Save the tuning parameters and send the values to the EEPROM", "\n", "M500", "\n"]
        
        
        
        
        
        ########################################################## Initialisation block (same for all)
        initialisation_block = [";;;;;;;;;;;;;;;;;;;; iMatrixSpray heat bed temperature autotuning\n\n", ";;;;;;;;;; initialisation\n"]
        initialisation_subblock = ["G28XYZ\n", "G28P\n", "G90\n"]
        # Generate the definitive block
        for s in initialisation_subblock:
            initialisation_block.append (s)
        
        # Leave a white line between blocks
        initialisation_block.append ("\n")
        
        
        
        
        
        
        
        
        
        
        ################################################ Write lines in the output file
        # Move to the working directory (set)
        os.chdir(outputfolder)
        # Get the filename from the GUI entry
        outputfile = filename_entry.get()
        # Add the extension to the file automatically
        if ".gcode" not in outputfile:
            outputfile = str(outputfile) + ".gcode"
        # Open the file and write the lines
        with open(outputfile, "w") as f:
            # Initialisation block
            for line in initialisation_block:
                f.writelines(line)
            # Temperature tuning
            for line in tuning_block:
                f.writelines(line)
            # Temperature tuning save
            for line in tuning_save_block:
                f.writelines(line)
        # Gcode file generated!
        tkinter.Tk().withdraw()
        tkinter.messagebox.showinfo(title="gcode file generated", message="The gcode file has been successfully generated!")
    ########### Output folder not defined!!
    else:
        # Missing output folder!!
        tkinter.Tk().withdraw()
        tkinter.messagebox.showinfo(title="Missing output folder!", message="Select where to save the gcode file first!")




#######################################################################


































################################################################## TCL-TK WINDOW
########## Main window
window = Tk()
window.title("iMatrixSpray Method Generator (gcode)")
window.resizable(True,True)
#window.wm_minsize(width=550, height=600)





########## Labels (with grid positioning)
title_label = Label(window, text="iMatrixSpray heat bed temperature autotuning").grid(row=0,column=1)
tuning_cycles_label = Label(window, text="Set how many tuning (temperature ramping) cycles\nhave to be performed (default:5)").grid(row=1, column=0)
temperature_label = Label(window, text="Heat bed temperature\n(default 37°C)").grid(row=2, column=0)





########## Entry boxes (with positioning)
tuning_cycles_entry = Entry(window)
temperature_entry = Entry(window)
filename_entry = Entry(window)



########## Entry boxes (default values)
tuning_cycles_entry.insert(0, "5")
temperature_entry.insert(0,"37")
filename_entry.insert(0,"iMatrix heat bed temperature autotuning")


########## Positioning
tuning_cycles_entry.grid(row=1, column=1)
temperature_entry.grid(row=2, column=1)
filename_entry.grid(row=3, column=1)



# Buttons
Button(window, text='Quit', command=window.destroy).grid(row=4, column=0)
#sticky=W, pady=4)
Button(window, text='Dump gcode file', command=dump_gcode_file_function).grid(row=4, column=2)
#sticky=W, pady=4)
Button(window, text="Browse output folder", command=select_output_folder_function).grid(row=4, column=1)
# Hold until quit
window.mainloop()
