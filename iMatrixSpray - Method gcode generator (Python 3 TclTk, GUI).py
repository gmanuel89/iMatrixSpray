#! python3

#################### iMatrixSpray generator GUI ####################

# Program version (Specified by the program writer!!!!)
program_version = "2017.02.22.01"










############################## Load the required libraries (tkinter for the TCLTK GUI)
import tkinter, os, platform
#from tkinter import *
from tkinter import messagebox, Label, Button, Entry, Tk, filedialog, font, Radiobutton, StringVar








############################## Initialize the output_folder variable
output_folder = os.getcwd()










############################## CONSTANT VALUES
max_speed_of_movement = 200
max_matrix_density = 5
max_height_of_the_needle = 80
min_height_of_the_needle = 1
coordinates_of_washing_x_axis = 0
coordinates_of_washing_y_axis = -110
coordinates_of_washing_z_axis = -50
coordinates_of_z_rest = 16.5
coordinates_of_z_axis_during_movement = -35
initial_x_coordinates = 0
initial_y_coordinates = 0
initial_z_coordinates = 0
max_x_coordinates = [-60, 60]
max_y_coordinates = [-80, 80]
max_z_coordinates = [-104, -24]
spray_syringe_volume_per_travel = 16.7









############################## FUNCTIONS

########## FUNCTION: Check for updates
def check_for_updates_function(): 
    # Initialize the version
    version_number = None
    try:
        # Import the library
        import urllib.request
        # Retrieve the file from GitHub
        github_file = urllib.request.urlopen("https://raw.githubusercontent.com/gmanuel89/iMatrixSpray/master/iMatrixSpray%20-%20Method%20gcode%20generator%20(Python%203%20TclTk%2C%20GUI).py").read()
        # String conversion
        github_file_string = str(github_file)
        # Lines
        github_file_lines = github_file_string.split("\\\\n")
        # Get the first line, with the version number
        first_block = github_file_lines[0].split("\\n")
        # Retrieve the version number
        for line in first_block:
            if line.startswith("program_version = "):
                version_number = line.split("program_version = ")[1]
                version_number = version_number.split("\"")[1]
        # Split the version number in YYYY.MM.DD
        version_YYYYMMDD = version_number.split(".")
        # Compare with the local version
        local_version_YYYYMMDD = program_version.split(".")
        # Initialize the variable that says if there are updates
        update_available = False
        for v in range(len(local_version_YYYYMMDD)):
            if local_version_YYYYMMDD[v] < version_YYYYMMDD[v]:
                update_available = True
                break
        # Return messages
        if version_number is None:
            # The version number could not be ckecked due to internet problems
            Tk().withdraw()
            messagebox.showwarning(title="Connection problem", message="The program version number could not be checked due to internet connection problems!\n\nManually check for updates at:\n\nhttps://raw.githubusercontent.com/gmanuel89/iMatrixSpray/master/iMatrixSpray%20-%20Method%20gcode%20generator%20(Python%203%20TclTk%2C%20GUI).py")
        else:
            if update_available is True:
                # The version number could not be ckecked due to internet problems
                Tk().withdraw()
                messagebox.showinfo(title="Updates available", message="UPDATES AVAILABLE!\n\nDownload the updated iMatrixSpray Gcode Generator at:\n\nhttps://raw.githubusercontent.com/gmanuel89/iMatrixSpray/master/iMatrixSpray%20-%20Method%20gcode%20generator%20(Python%203%20TclTk%2C%20GUI).py")
                # Update the label                
                check_for_updates_label = Label(window, text=("Version: " + program_version + "\nUpdated version: " + version_number), font=label_font).grid(row=2, column=3)
            else:
                Tk().withdraw()
                messagebox.showinfo(title="No updates available", message="NO UPDATES AVAILABLE!\n\nThe latest version of the iMatrixSpray Gcode Generator is running!")
    # Something went wrong: library not installed, retrieving failed, errors in parsing the version number 
    except:
        # Return messages
        if version_number is None:
            # The version number could not be ckecked due to internet problems
            Tk().withdraw()
            messagebox.showwarning(title="Connection problem", message="The program version number could not be checked due to internet connection problems!\n\nManually check for updates at:\n\nhttps://raw.githubusercontent.com/gmanuel89/iMatrixSpray/master/iMatrixSpray%20-%20Method%20gcode%20generator%20(Python%203%20TclTk%2C%20GUI).py")











########## FUNCTION: Select where to save the GCODE method file
def select_output_folder_function():
    Tk().withdraw()
    messagebox.showinfo(title="Folder selection", message="Select where to dump the gcode file(s)")
    # Where to save the GCODE file (escape function environment)
    global output_folder
    output_folder = filedialog.askdirectory ()
    # Fix the possible non-defined output folder
    if output_folder == "":
        output_folder = os.getcwd()
    # Just to confirm...
    Tk().withdraw()
    messagebox.showinfo(title="Folder selected", message="The gcode file(s) will be dumped in '%s'" %(output_folder))










########## FUNCTION: Dump the GCODE method file
def dump_gcode_file_function():
            
    
    
    
    ########## DEFINE THE VARIABLE VALUES (get the values from the GUI)
    
    
    ##### SOLUTION TO USE (Vial valves: A=3, B=4, C=5, Rinse=2, Waste=0, Spray=1; when floating with .5 it always means that the valve links the selected vial to the waste, probably because .0 was not possible)
    # Get values from the entry
    solution_to_use_input = solution_to_use_entry.get()
    # Split the string in as many letters as the solution (it never fails)
    solution_to_use_splitted = solution_to_use_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(solution_to_use_splitted)):
        solution_to_use_splitted[i] = solution_to_use_splitted[i].strip()
    # More letters...
    if len(solution_to_use_splitted) > 1:
        solution_to_use = []
        solution_to_use_letter = []
        # Create a list of letters
        for sol in solution_to_use_splitted:
            if sol == "A" or sol == "a" or sol == 1:
                solution_to_use_letter.append(sol)
                solution_to_use.append(int(3))
            elif sol == "B" or sol == "b" or sol == 2:
                solution_to_use_letter.append(sol)
                solution_to_use.append(int(4))
            elif sol == "C" or sol == "c" or sol == 3:
                solution_to_use_letter.append(sol)
                solution_to_use.append(int(5))
            elif sol == "rinse":
                solution_to_use_letter.append(sol)
                solution_to_use.append(int(2))
            else:
                solution_to_use_letter.append(sol)
                solution_to_use.append(int(3))
    # One letter...
    elif len(solution_to_use_splitted) == 1:
        if solution_to_use_splitted[0] == "A" or solution_to_use_splitted[0] == "a" or solution_to_use_splitted[0] == 1:
            solution_to_use_letter = ["A"]
            solution_to_use = [int(3)]
        elif solution_to_use_splitted[0] == "B" or solution_to_use_splitted[0] == "b" or solution_to_use_splitted[0] == 2:
            solution_to_use_letter = ["B"]
            solution_to_use = [int(4)]
        elif solution_to_use_splitted[0] == "C" or solution_to_use_splitted[0] == "c" or solution_to_use_splitted[0] == 3:
            solution_to_use_letter = ["C"]
            solution_to_use = [int(5)]
        elif solution_to_use_splitted[0] == "rinse":
            solution_to_use_letter = ["rinse"]
            solution_to_use = [int(2)]
        else:
            solution_to_use_letter = ["A"]
            solution_to_use = [int(3)]
    
    
    ##### WAITING TIME BETWEEN CONSECUTIVE SOLUTIONS
    # Get values from the entry
    waiting_phase_between_solutions_time_input = waiting_phase_between_solutions_time_entry.get()
    # Split (it never fails, it generates a list)
    waiting_phase_between_solutions_time_splitted = waiting_phase_between_solutions_time_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(waiting_phase_between_solutions_time_splitted)):
        waiting_phase_between_solutions_time_splitted[i] = waiting_phase_between_solutions_time_splitted[i].strip()
    waiting_phase_between_solutions_time = []
    # One solution
    if len(solution_to_use) == 1:
        pass
    # More solutions
    elif len(solution_to_use) > 1:
        for i in range((len(solution_to_use))-1):
            # If the time is specified for each solution, use it
            try:
                if waiting_phase_between_solutions_time_splitted[i] != "":
                    waiting_phase_between_solutions_time.append(int(waiting_phase_between_solutions_time_splitted[i]))
                else:
                    # Default (5)
                    waiting_phase_between_solutions_time.append(float(5))
            except:
                # Otherwise, use the time specified (if specified, otherwise use the default)
                if waiting_phase_between_solutions_time_splitted[0] != "":
                    waiting_phase_between_solutions_time.append(float(waiting_phase_between_solutions_time_splitted[0]))
                else:
                    waiting_phase_between_solutions_time.append(float(5))
    
    
    ##### X,Y COORDINATES (for each solution)
    # input("Set the x-axis coordinates of spraying (default: -60,60) (solution '%s')\n[hint: Coordinates for the small area are (-30,30)]\n"
    # input("Set the y-axis coordinates of spraying (default: -80,80) (solution '%s')\n[hint: Coordinates for the small area are (40,80)]\n" %(solution_to_use_letter[i]))
    # It returns errors with only one solution to be used (it has no len property), so use try/except
    # Get values from the entry
    coordinates_of_spray_x_axis_input = coordinates_of_spray_x_axis_entry.get()
    coordinates_of_spray_y_axis_input = coordinates_of_spray_y_axis_entry.get()
    # Split (it never fails, it generates a list)
    coordinates_of_spray_x_axis_splitted = coordinates_of_spray_x_axis_input.split(" ")
    coordinates_of_spray_y_axis_splitted = coordinates_of_spray_y_axis_input.split(" ")
    ### X-axis
    coordinates_of_spray_x_axis = []
    for i in range(len(coordinates_of_spray_x_axis_splitted)):
        # If the i goes out of boundary (you use more solutions than the coordinates specified)
        # If specified
        if coordinates_of_spray_x_axis_splitted[i] != "":
            # Convert it into a list
            coordinates_of_spray_x_axis_splitted[i] = coordinates_of_spray_x_axis_splitted[i].split(",")
            # From strings to floating point numbers (tuple)
            try:
                coordinates_of_spray_x_axis_splitted[i] = (float(coordinates_of_spray_x_axis_splitted[i][0]), float(coordinates_of_spray_x_axis_splitted[i][1]))
            except:
                coordinates_of_spray_x_axis_splitted[i] = (float(-60), float(60))
        # If not specified
        else:
            coordinates_of_spray_x_axis_splitted[i] = (float(-60), float(60))
        # Append to the final list
        coordinates_of_spray_x_axis.append(coordinates_of_spray_x_axis_splitted[i])
    ## The number of solutions must be equal to the coordinates
    if len(coordinates_of_spray_x_axis) == len(solution_to_use):
        pass
    else:
        # Calculate the difference
        len_diff = len(solution_to_use) - len(coordinates_of_spray_x_axis)
        if len_diff > 0:
            # If there is only one coordinate, repeat it
            if len(coordinates_of_spray_x_axis) == 1:
                for j in range(len_diff):
                    coordinates_of_spray_x_axis.append(coordinates_of_spray_x_axis[0])
            # If there are more than one, add the default
            elif len(coordinates_of_spray_x_axis) > 1:
                for j in range(len_diff):
                    coordinates_of_spray_x_axis.append((float(-60), float(60)))
        elif len_diff < 0:
            coordinates_of_spray_x_axis = coordinates_of_spray_x_axis[0:len(solution_to_use)]
    ### Y-axis
    coordinates_of_spray_y_axis = []
    for i in range(len(coordinates_of_spray_y_axis_splitted)):
        # If the i goes out of boundary (you use more solutions than the coordinates specified)
        # If specified
        if coordinates_of_spray_y_axis_splitted[i] != "":
            # Convert it into a list
            coordinates_of_spray_y_axis_splitted[i] = coordinates_of_spray_y_axis_splitted[i].split(",")
            # From strings to floating point numbers (tuple)
            try:
                coordinates_of_spray_y_axis_splitted[i] = (float(coordinates_of_spray_y_axis_splitted[i][0]), float(coordinates_of_spray_y_axis_splitted[i][1]))
            except:
                coordinates_of_spray_y_axis_splitted[i] = (float(-80), float(80))
        # If not specified
        else:
            coordinates_of_spray_y_axis_splitted[i] = (float(-80), float(80))
        # Append to the final list
        coordinates_of_spray_y_axis.append(coordinates_of_spray_y_axis_splitted[i])
    ## The number of solutions must be equal to the coordinates
    if len(coordinates_of_spray_y_axis) == len(solution_to_use):
        pass
    else:
        # Calculate the difference
        len_diff = len(solution_to_use) - len(coordinates_of_spray_y_axis)
        if len_diff > 0:
            # If there is only one coordinate, repeat it
            if len(coordinates_of_spray_y_axis) == 1:
                for j in range(len_diff):
                    coordinates_of_spray_y_axis.append(coordinates_of_spray_y_axis[0])
            # If there are more than one, add the default
            elif len(coordinates_of_spray_y_axis) > 1:
                for j in range(len_diff):
                    coordinates_of_spray_y_axis.append((float(-80), float(80)))
        elif len_diff < 0:
            coordinates_of_spray_y_axis = coordinates_of_spray_y_axis[0:len(solution_to_use)]
    
    
    ##### HEAT BED PRESENCE
    # Get values from the entry
    heat_bed_presence = heat_bed_presence_entry.get()
    #heat_bed_presence_input = heat_bed_presence_entry.get()
    # Escape the function
    #global heat_bed_presence
    #heat_bed_presence = heat_bed_presence_input
    # If specified
    #if heat_bed_presence == "":
    #        heat_bed_presence = "y"
    #if heat_bed_presence == "y":
    #    pass
    #else:
    #    heat_bed_presence = "n"
    
    
    ##### HEAT BED HEIGHT
    # Get values from the entry
    heat_bed_height = heat_bed_height_entry.get()
    # If not specified
    if heat_bed_height == "":
            heat_bed_height = float(5)
    # Convert it to float number
    heat_bed_height = float(heat_bed_height)
    # Set it to zero if there is no heat plate
    if heat_bed_presence == "n":
        heat_bed_height = float(0)
    
    
    ##### INTERSPRAY WASH CHOICE
    # Get values from the entry
    interspray_wash_choice_input = interspray_wash_choice_entry.get()
    # Split (it never fails, it generates a list)
    interspray_wash_choice_splitted = interspray_wash_choice_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(interspray_wash_choice_splitted)):
        interspray_wash_choice_splitted[i] = interspray_wash_choice_splitted[i].strip()
    interspray_wash_choice = []
    for i in range(len(interspray_wash_choice_splitted)):
        # If not specified
        if interspray_wash_choice_splitted[i] == "":
            interspray_wash_choice_splitted[i] = "y"
        # Append to the final list
        interspray_wash_choice.append(interspray_wash_choice_splitted[i])
    ## The number of solutions must be equal to the values
    if len(solution_to_use) == len(interspray_wash_choice):
        pass
    else:
        # Calculate the difference
        len_diff = len(solution_to_use) - len(interspray_wash_choice)
        if len_diff > 0:
            # If there is only one coordinate, repeat it
            if len(interspray_wash_choice) == 1:
                for j in range(len_diff):
                   interspray_wash_choice.append(interspray_wash_choice[0])
            # If there are more than one, add the default
            elif len(interspray_wash_choice) > 1:
                for j in range(len_diff):
                    interspray_wash_choice.append("y")
        elif len_diff < 0:
            interspray_wash_choice = interspray_wash_choice[0:(len(solution_to_use))]
    
    
    ##### HEAT BED TEMPERATURE
    # Get values from the entry
    heat_bed_temperature_input = heat_bed_temperature_entry.get()
    # Split (it never fails, it generates a list)
    heat_bed_temperature_splitted = heat_bed_temperature_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(heat_bed_temperature_splitted)):
        heat_bed_temperature_splitted[i] = heat_bed_temperature_splitted[i].strip()
    heat_bed_temperature = []
    for i in range(len(heat_bed_temperature_splitted)):
        # If specified
        if heat_bed_temperature_splitted[i] != "":
            heat_bed_temperature_splitted[i] = float(heat_bed_temperature_splitted[i])
        # If not specified
        else:
            heat_bed_temperature_splitted[i] = float(0)
        # Append to the final list
        heat_bed_temperature.append(heat_bed_temperature_splitted[i])
    ## The number of solutions must be equal to the values
    if len(heat_bed_temperature) == len(solution_to_use):
        pass
    else:
        # Calculate the difference
        len_diff = len(solution_to_use) - len(heat_bed_temperature)
        if len_diff > 0:
            # If there is only one coordinate, repeat it
            if len(heat_bed_temperature) == 1:
                for j in range(len_diff):
                    heat_bed_temperature.append(heat_bed_temperature[0])
            # If there are more than one, add the default
            elif len(heat_bed_temperature) > 1:
                for j in range(len_diff):
                    heat_bed_temperature.append(float(0))
        elif len_diff < 0:
            heat_bed_temperature = heat_bed_temperature[0:(len(solution_to_use))]
    
    
    ##### HEIGHT OF THE NEEDLE
    # Get values from the entry
    height_of_the_needle_input = height_of_the_needle_entry.get()
    # Split (it never fails, it generates a list)
    height_of_the_needle_splitted = height_of_the_needle_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(height_of_the_needle_splitted)):
        height_of_the_needle_splitted[i] = height_of_the_needle_splitted[i].strip()
    height_of_the_needle = []
    for i in range(len(height_of_the_needle_splitted)):
        # If specified
        if height_of_the_needle_splitted[i] != "":
            height_of_the_needle_splitted[i] = float(height_of_the_needle_splitted[i])+heat_bed_height
        # If not specified
        else:
            height_of_the_needle_splitted[i] = float(60+heat_bed_height)
        # Append to the final list
        height_of_the_needle.append(height_of_the_needle_splitted[i])
    ## The number of solutions must be equal to the values
    if len(height_of_the_needle) == len(solution_to_use):
        pass
    else:
        # Calculate the difference
        len_diff = len(solution_to_use) - len(height_of_the_needle)
        if len_diff > 0:
            # If there is only one coordinate, repeat it
            if len(height_of_the_needle) == 1:
                for j in range(len_diff):
                    height_of_the_needle.append(height_of_the_needle[0])
            # If there are more than one, add the default
            elif len(height_of_the_needle) > 1:
                for j in range(len_diff):
                    height_of_the_needle.append(float(60+heat_bed_height))
        elif len_diff < 0:
            height_of_the_needle = height_of_the_needle[0:(len(solution_to_use))]
    
    
    ##### DISTANCE BETWEEN SPRAY LINES
    # Get values from the entry
    distance_between_lines_input = distance_between_lines_entry.get()
    # Split (it never fails, it generates a list)
    distance_between_lines_splitted = distance_between_lines_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(distance_between_lines_splitted)):
        distance_between_lines_splitted[i] = distance_between_lines_splitted[i].strip()
    distance_between_lines = []
    for i in range(len(distance_between_lines_splitted)):
        # If specified
        if distance_between_lines_splitted[i] != "":
            distance_between_lines_splitted[i] = float(distance_between_lines_splitted[i])
        # If not specified
        else:
            distance_between_lines_splitted[i] = float(5)
        # Append to the final list
        distance_between_lines.append(distance_between_lines_splitted[i])
    ## The number of solutions must be equal to the values
    if len(solution_to_use) == len(distance_between_lines):
        pass
    else:
        # Calculate the difference
        len_diff = len(solution_to_use) - len(distance_between_lines)
        if len_diff > 0:
            # If there is only one coordinate, repeat it
            if len(distance_between_lines) == 1:
                for j in range(len_diff):
                    distance_between_lines.append(distance_between_lines[0])
            # If there are more than one, add the default
            elif len(distance_between_lines) > 1:
                for j in range(len_diff):
                    distance_between_lines.append(float(5))
        elif len_diff < 0:
            distance_between_lines = distance_between_lines[0:(len(solution_to_use))]
    
    
    ##### SPEED OF MOVEMENT
    # Get values from the entry
    speed_of_movement_input = speed_of_movement_entry.get()
    # Split (it never fails, it generates a list)
    speed_of_movement_splitted = speed_of_movement_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(speed_of_movement_splitted)):
        speed_of_movement_splitted[i] = speed_of_movement_splitted[i].strip()
    speed_of_movement = []
    for i in range(len(speed_of_movement_splitted)):
        # If specified
        if speed_of_movement_splitted[i] != "":
            speed_of_movement_splitted[i] = float(speed_of_movement_splitted[i])
        # If not specified
        else:
            speed_of_movement_splitted[i] = float(150)
        # Append to the final list
        speed_of_movement.append(speed_of_movement_splitted[i])
    ## The number of solutions must be equal to the values
    if len(solution_to_use) == len(speed_of_movement):
        pass
    else:
        # Calculate the difference
        len_diff = len(solution_to_use) - len(speed_of_movement)
        if len_diff > 0:
            # If there is only one coordinate, repeat it
            if len(speed_of_movement) == 1:
                for j in range(len_diff):
                    speed_of_movement.append(speed_of_movement[0])
            # If there are more than one, add the default
            elif len(speed_of_movement) > 1:
                for j in range(len_diff):
                    speed_of_movement.append(float(150))
        elif len_diff < 0:
            speed_of_movement = speed_of_movement[0:(len(solution_to_use))]
    
    
    ##### MATRIX DENSITY
    # Get values from the entry
    matrix_density_input = matrix_density_entry.get()
    # Split (it never fails, it generates a list)
    matrix_density_splitted = matrix_density_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(matrix_density_splitted)):
        matrix_density_splitted[i] = matrix_density_splitted[i].strip()
    matrix_density = []
    for i in range(len(matrix_density_splitted)):
        # If specified
        if matrix_density_splitted[i] != "":
            matrix_density_splitted[i] = float(matrix_density_splitted[i])
        # If not specified
        else:
            matrix_density_splitted[i] = float(1)
        # Append to the final list
        matrix_density.append(matrix_density_splitted[i])
    ## The number of solutions must be equal to the values
    if len(solution_to_use) == len(matrix_density):
        pass
    else:
        # Calculate the difference
        len_diff = len(solution_to_use) - len(matrix_density)
        if len_diff > 0:
            # If there is only one coordinate, repeat it
            if len(matrix_density) == 1:
                for j in range(len_diff):
                    matrix_density.append(matrix_density[0])
            # If there are more than one, add the default
            elif len(matrix_density) > 1:
                for j in range(len_diff):
                    matrix_density.append(float(1))
        elif len_diff < 0:
            matrix_density = matrix_density[0:(len(solution_to_use))]
    
    
    ##### NUMBER OF INITIAL WASH CYCLES
    # Get values from the entry
    number_of_initial_wash_cycles_input = number_of_initial_wash_cycles_entry.get()
    # Split (it never fails, it generates a list)
    number_of_initial_wash_cycles_splitted = number_of_initial_wash_cycles_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(number_of_initial_wash_cycles_splitted)):
        number_of_initial_wash_cycles_splitted[i] = number_of_initial_wash_cycles_splitted[i].strip()
    number_of_initial_wash_cycles = []
    for i in range(len(number_of_initial_wash_cycles_splitted)):
        # If specified
        if number_of_initial_wash_cycles_splitted[i] != "":
            number_of_initial_wash_cycles_splitted[i] = int(number_of_initial_wash_cycles_splitted[i])
        # If not specified
        else:
            number_of_initial_wash_cycles_splitted[i] = int(5)
        # Append to the final list
        number_of_initial_wash_cycles.append(number_of_initial_wash_cycles_splitted[i])
    ## The number of solutions must be equal to the values
    if len(solution_to_use) == len(number_of_initial_wash_cycles):
        pass
    else:
        # Calculate the difference
        len_diff = len(solution_to_use) - len(number_of_initial_wash_cycles)
        if len_diff > 0:
            # If there is only one coordinate, repeat it
            if len(number_of_initial_wash_cycles) == 1:
                for j in range(len_diff):
                    number_of_initial_wash_cycles.append(int(number_of_initial_wash_cycles[0]))
            # If there are more than one, add the default
            elif len(number_of_initial_wash_cycles) > 1:
                for j in range(len_diff):
                    number_of_initial_wash_cycles.append(int(5))
        elif len_diff < 0:
            number_of_initial_wash_cycles = number_of_initial_wash_cycles[0:(len(solution_to_use))]
    
    
    ##### NUMBER OF SPRAY CYCLES
    # Get values from the entry
    number_of_spray_cycles_input = number_of_spray_cycles_entry.get()
    # Split (it never fails, it generates a list)
    number_of_spray_cycles_splitted = number_of_spray_cycles_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(number_of_spray_cycles_splitted)):
        number_of_spray_cycles_splitted[i] = number_of_spray_cycles_splitted[i].strip()
    number_of_spray_cycles = []
    for i in range(len(number_of_spray_cycles_splitted)):
        # If specified
        if number_of_spray_cycles_splitted[i] != "":
            number_of_spray_cycles_splitted[i] = int(number_of_spray_cycles_splitted[i])
        # If not specified
        else:
            number_of_spray_cycles_splitted[i] = int(5)
        # Append to the final list
        number_of_spray_cycles.append(number_of_spray_cycles_splitted[i])
    ## The number of solutions must be equal to the values
    if len(solution_to_use) == len(number_of_spray_cycles):
        pass
    else:
        # Calculate the difference
        len_diff = len(solution_to_use) - len(number_of_spray_cycles)
        if len_diff > 0:
            # If there is only one coordinate, repeat it
            if len(number_of_spray_cycles) == 1:
                for j in range(len_diff):
                    number_of_spray_cycles.append(int(number_of_spray_cycles[0]))
            # If there are more than one, add the default
            elif len(number_of_spray_cycles) > 1:
                for j in range(len_diff):
                    number_of_spray_cycles.append(int(5))
        elif len_diff < 0:
            number_of_spray_cycles = number_of_spray_cycles[0:(len(solution_to_use))]
    
    
    ##### ADDITIONAL TIME TO WAIT AFTER EACH SPRAY CYCLE
    # Get values from the entry
    additional_waiting_time_after_each_spray_cycle_input = additional_waiting_time_after_each_spray_cycle_entry.get()
    # Split (it never fails, it generates a list)
    additional_waiting_time_after_each_spray_cycle_splitted = additional_waiting_time_after_each_spray_cycle_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(additional_waiting_time_after_each_spray_cycle_splitted)):
        additional_waiting_time_after_each_spray_cycle_splitted[i] = additional_waiting_time_after_each_spray_cycle_splitted[i].strip()
    additional_waiting_time_after_each_spray_cycle = []
    for i in range(len(additional_waiting_time_after_each_spray_cycle_splitted)):
        # If specified
        if additional_waiting_time_after_each_spray_cycle_splitted[i] != "":
            additional_waiting_time_after_each_spray_cycle_splitted[i] = float(additional_waiting_time_after_each_spray_cycle_splitted[i])
        # If not specified
        else:
            additional_waiting_time_after_each_spray_cycle_splitted[i] = float(0)
        # Append to the final list
        additional_waiting_time_after_each_spray_cycle.append(additional_waiting_time_after_each_spray_cycle_splitted[i])
    ## The number of solutions must be equal to the values
    if len(solution_to_use) == len(additional_waiting_time_after_each_spray_cycle):
        pass
    else:
        # Calculate the difference
        len_diff = len(solution_to_use) - len(additional_waiting_time_after_each_spray_cycle)
        if len_diff > 0:
            # If there is only one coordinate, repeat it
            if len(additional_waiting_time_after_each_spray_cycle) == 1:
                for j in range(len_diff):
                    additional_waiting_time_after_each_spray_cycle.append(additional_waiting_time_after_each_spray_cycle[0])
            # If there are more than one, add the default
            elif len(additional_waiting_time_after_each_spray_cycle) > 1:
                for j in range(len_diff):
                    additional_waiting_time_after_each_spray_cycle.append(float(0))
        elif len_diff < 0:
            additional_waiting_time_after_each_spray_cycle = additional_waiting_time_after_each_spray_cycle[0:(len(solution_to_use))]
    
    
    ##### NUMBER OF VALVE RINSING CYCLES
    # Get values from the entry
    number_of_valve_rinsing_cycles_input = number_of_valve_rinsing_cycles_entry.get()
    # Split (it never fails, it generates a list)
    number_of_valve_rinsing_cycles_splitted = number_of_valve_rinsing_cycles_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(number_of_valve_rinsing_cycles_splitted)):
        number_of_valve_rinsing_cycles_splitted[i] = number_of_valve_rinsing_cycles_splitted[i].strip()
    number_of_valve_rinsing_cycles = []
    for i in range(len(number_of_valve_rinsing_cycles_splitted)):
        # If specified
        if number_of_valve_rinsing_cycles_splitted[i] != "":
            number_of_valve_rinsing_cycles_splitted[i] = int(number_of_valve_rinsing_cycles_splitted[i])
        # If not specified
        else:
            number_of_valve_rinsing_cycles_splitted[i] = int(5)
        # Append to the final list
        number_of_valve_rinsing_cycles.append(number_of_valve_rinsing_cycles_splitted[i])
    ## The number of solutions must be equal to the values
    if len(solution_to_use) == len(number_of_valve_rinsing_cycles):
        pass
    else:
        # Calculate the difference
        len_diff = len(solution_to_use) - len(number_of_valve_rinsing_cycles)
        if len_diff > 0:
            # If there is only one coordinate, repeat it
            if len(number_of_valve_rinsing_cycles) == 1:
                for j in range(len_diff):
                    number_of_valve_rinsing_cycles.append(number_of_valve_rinsing_cycles[0])
            # If there are more than one, add the default
            elif len(number_of_valve_rinsing_cycles) > 1:
                for j in range(len_diff):
                    number_of_valve_rinsing_cycles.append(int(5))
        elif len_diff < 0:
            number_of_valve_rinsing_cycles = number_of_valve_rinsing_cycles[0:(len(solution_to_use))]
    
    
    ##### DRYING TIME
    # Get values from the entry
    drying_time_input = drying_time_entry.get()
    # Split (it never fails, it generates a list)
    drying_time_splitted = drying_time_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(drying_time_splitted)):
        drying_time_splitted[i] = drying_time_splitted[i].strip()
    # Take only the first entry
    try:
        drying_time = float(drying_time_splitted[0])
    except:
        drying_time = float(8)
    
    
    ##### HORIZONTAL SPRAYING
    # Get values from the entry
    horizontal_spraying_input = horizontal_spraying_entry.get()
    # Split (it never fails, it generates a list)
    horizontal_spraying_splitted = horizontal_spraying_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(horizontal_spraying_splitted)):
        horizontal_spraying_splitted[i] = horizontal_spraying_splitted[i].strip()
    horizontal_spraying = []
    for i in range(len(horizontal_spraying_splitted)):
        # If specified
        if horizontal_spraying_splitted[i] == "":
            horizontal_spraying_splitted[i] = "y"
        # Append to the final list
        horizontal_spraying.append(horizontal_spraying_splitted[i])
    ## The number of solutions must be equal to the values
    if len(solution_to_use) == len(horizontal_spraying):
        pass
    else:
        # Calculate the difference
        len_diff = len(solution_to_use) - len(horizontal_spraying)
        if len_diff > 0:
            # If there is only one coordinate, repeat it
            if len(horizontal_spraying) == 1:
                for j in range(len_diff):
                   horizontal_spraying.append(horizontal_spraying[0])
            # If there are more than one, add the default
            elif len(horizontal_spraying) > 1:
                for j in range(len_diff):
                    horizontal_spraying.append("y")
        elif len_diff < 0:
            horizontal_spraying = horizontal_spraying[0:(len(solution_to_use))]
            
            
    ##### CONSTANT VALUES (calculations from input values)
    
    # Coordinates of spray z axis
    try:
        coordinates_of_spray_z_axis = []
        for h in height_of_the_needle:
            coordinates_of_spray_z_axis.append(float(-104 + abs(h))) # Calculated
    except:
        coordinates_of_spray_z_axis = float(-104 + abs(height_of_the_needle)) # Calculated    
    
    # Horizontal spraying
    try:
        for i in range(len(horizontal_spraying)):
            if (horizontal_spraying[i] == "y" or horizontal_spraying[i] == ''):
                horizontal_spraying[i] = True
            else:
                horizontal_spraying[i] = False
    except:
        if (horizontal_spraying == "y" or horizontal_spraying == ''):
            horizontal_spraying = True
        else:
            horizontal_spraying = False
    
    
    ##### MACHINE LIMITS (Avoid that the machine breaks)
    
    # Speed
    try:
        for s in range(len(speed_of_movement)):
            if float(speed_of_movement[s]) < float(0):
                speed_of_movement[s] = float(abs(s))
            if float(speed_of_movement[s]) > float(max_speed_of_movement):
                speed_of_movement[s] = float(max_speed_of_movement)
            if float(speed_of_movement[s]) == float(0):
                speed_of_movement[s] = float(1)
    except:
        if speed_of_movement < 0:
            speed_of_movement = abs(speed_of_movement)
        if speed_of_movement > max_speed_of_movement:
            speed_of_movement = max_speed_of_movement
        if speed_of_movement == 0:
            speed_of_movement = 1
    
    # Needle height (Z coordinate)
    try:
        for c in range(len(coordinates_of_spray_z_axis)):
            if coordinates_of_spray_z_axis[c] < max_z_coordinates[0]:
                coordinates_of_spray_z_axis[c] = max_z_coordinates[0]
            elif coordinates_of_spray_z_axis[c] > max_z_coordinates[1]:
                coordinates_of_spray_z_axis[c] = max_z_coordinates[1]
    except:
        if coordinates_of_spray_z_axis < max_z_coordinates[0]:
            coordinates_of_spray_z_axis = max_z_coordinates[0]
        elif coordinates_of_spray_z_axis > max_z_coordinates[1]:
            coordinates_of_spray_z_axis = max_z_coordinates[1]
    
    # Matrix density
    try:
        for m in range(len(matrix_density)):
            if matrix_density[m] > max_matrix_density:
                matrix_density[m] = max_matrix_density
            if matrix_density[m] <= 0:
                matrix_density = float(1)
    except:
        if matrix_density > max_matrix_density:
            matrix_density = max_matrix_density
        if matrix_density <= 0:
            matrix_density = 1
    
    # X and Y coordinates
    for c in range(len(coordinates_of_spray_x_axis)):
        if coordinates_of_spray_x_axis[c][0] < max_x_coordinates[0]:
            coordinates_of_spray_x_axis[c][0] = max_x_coordinates[0]
        if coordinates_of_spray_x_axis[c][1] > max_x_coordinates[1]:
            coordinates_of_spray_x_axis[c][1] = max_x_coordinates[1]
    for c in range(len(coordinates_of_spray_y_axis)):
        if coordinates_of_spray_y_axis[c][0] < max_y_coordinates[0]:
            coordinates_of_spray_y_axis[c][0] = max_y_coordinates[0]
        if coordinates_of_spray_y_axis[c][1] > max_y_coordinates[1]:
            coordinates_of_spray_y_axis[c][1] = max_y_coordinates[1]
    
    
    
    
    
    ########## GCODE BLOCKS (Fill out the GCODE according to the variables)
    
    
    ##### GO TO WASH POSITION (same for all)
    go_to_wash_position_block = [";;;;; go to wash position\n"]
    go_to_wash_position_subblock = ["G1 Z%s F%s\n" %(float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 X%s Y%s Z%s F%s\n" %(float(coordinates_of_washing_x_axis), float(coordinates_of_washing_y_axis), float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 Z%s\n" %float(coordinates_of_washing_z_axis)]
    # Generate the definitive block
    for s in go_to_wash_position_subblock:
        go_to_wash_position_block.append (s)
    # Leave a white line between blocks
    go_to_wash_position_block.append ("\n")
    
    
    ##### ADDITIONAL WAITING TIME AFTER SPRAYING (solution dependent) (the needle waits at the wash position)
    #try:
     #   additional_waiting_time_after_spraying = [";;; additional waiting time after spraying\n"]
      #  for sol in range(len(solution_to_use)):
       #     additional_waiting_time_after_spraying.append(["G1 Z%s F%s\n" %(float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 X%s Y%s Z%s F%s\n" %(float(coordinates_of_washing_x_axis), float(coordinates_of_washing_y_axis), float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 Z%s\n" %float(coordinates_of_washing_z_axis), "G4 S%s\n" %(additional_waiting_time_after_each_spray_cycle[sol])])
    #except:
     #   additional_waiting_time_after_spraying = [";;; additional waiting time after spraying\n", "G1 Z%s F%s\n" %(float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 X%s Y%s Z%s F%s\n" %(float(coordinates_of_washing_x_axis), float(coordinates_of_washing_y_axis), float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 Z%s\n" %float(coordinates_of_washing_z_axis), "G4 S%s\n" %(additional_waiting_time_after_each_spray_cycle)]
    try:
        additional_waiting_time_after_spraying_block = []
        for sol in range(len(solution_to_use)):
            additional_waiting_time_after_spraying_subblock = [";;; additional waiting time after spraying\n"]
            for l in go_to_wash_position_block:
                additional_waiting_time_after_spraying_subblock.append (l)
            additional_waiting_time_after_spraying_subblock.append("; wait still\nG4 S%s\n" %(additional_waiting_time_after_each_spray_cycle[sol]))
            # Leave a white line between blocks
            additional_waiting_time_after_spraying_subblock.append ("\n")
            # Add the sub-block to the final block
            additional_waiting_time_after_spraying_block.append (additional_waiting_time_after_spraying_subblock)
    except:
        additional_waiting_time_after_spraying_block = [";;; additional waiting time after spraying\n"]
        for l in go_to_wash_position_block:
            additional_waiting_time_after_spraying_block.append (l)
        additional_waiting_time_after_spraying_block.append ("; wait still\nG4 S%s\n" %(additional_waiting_time_after_each_spray_cycle))
        # Leave a white line between blocks
        additional_waiting_time_after_spraying_block.append ("\n")
    
    ##### WAITING TIME BETWEEN DIFFERENT SOLUTIONS
    try:
        waiting_phase_between_solutions_block_sol = []
        for sol in range(len(solution_to_use)-1):
            waiting_phase_between_solutions_block = [";;;;;;;;;; waiting phase before switching between solutions\nG4 S%s\n\n" %waiting_phase_between_solutions_time[sol]]
            waiting_phase_between_solutions_block_sol.append(waiting_phase_between_solutions_block)
    except:
        waiting_phase_between_solutions_block = None
    
    
    ##### INITIALISATION (same for all)
    initialisation_block = [";;;;;;;;;;;;;;;;;;;; iMatrixSpray gcode method generator\n\n", ";;;;;;;;;; initialisation\n"]
    initialisation_subblock = ["G28XYZ\n", "G28P\n", "G90\n"]
    # Generate the definitive block
    for s in initialisation_subblock:
        initialisation_block.append (s)
    # Leave a white line between blocks
    initialisation_block.append ("\n")
    
    
    ##### FIRST WASH (solution dependent)
    try:
        first_wash_block_sol = []
        for sol in range(len(solution_to_use)):
            first_wash_block = [";;;;;;;;;; first wash\n"]
            # Go to wash position first
            for s in go_to_wash_position_block:
                first_wash_block.append (s)
            # Define the washing sub-block
            first_wash_subblock = ["G1 V%s.5 F%s\n" %(solution_to_use[sol], max_speed_of_movement), "G4 S1\n", "G1 P4.2 F%s\n" %(max_speed_of_movement), "G4 S1\n", "G1 V%s F%s\n" %(solution_to_use[sol], max_speed_of_movement), "G4 S1\n", "G1 V0 F%s\n" %(max_speed_of_movement), "G4 S1\n", "G1 P0 F%s\n" %(max_speed_of_movement/2), "G4 S1\n", "\n"]
            # Generate the definitive block based on the number of repetitions
            for i in range(number_of_initial_wash_cycles[sol]):
                for s in first_wash_subblock:
                    first_wash_block.append (s)
            # After washing
            after_washing_block = ["M106\n", "G1 V%s F%s\n" %(solution_to_use[sol], max_speed_of_movement), "G4 S1\n", "G1 P2 F%s\n" %(max_speed_of_movement), "G1 V1 F%s\n" %(max_speed_of_movement), "G4 S1\n", "G1 F0.1\n", "G1 P0\n"]
            # Generate the definitive block
            for s in after_washing_block:
                first_wash_block.append (s)
            # Leave a white line between blocks
            first_wash_block.append ("\n")
            # Add this chunk to the final block
            first_wash_block_sol.append(first_wash_block)
    except:
        first_wash_block = [";;;;;;;;;; first wash\n"]
        # Go to wash position first
        for s in go_to_wash_position_block:
            first_wash_block.append (s)
        # Define the washing sub-block
        first_wash_subblock = ["G1 V%s.5 F%s\n" %(solution_to_use, max_speed_of_movement), "G4 S1\n", "G1 P4.2 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 V%s F%s\n" %(solution_to_use, max_speed_of_movement), "G4 S1\n", "G1 V0 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 P0 F%s\n" %(max_speed_of_movement/2), "G4 S1\n", "\n"]
        # Generate the definitive block based on the number of repetitions
        for i in range(number_of_initial_wash_cycles):
            for s in first_wash_subblock:
                first_wash_block.append (s)
        # After washing
        after_washing_block = ["M106\n", "G1 V%s F%s\n" %(solution_to_use, max_speed_of_movement), "G4 S1\n", "G1 P2 F%s\n" %max_speed_of_movement, "G1 V1 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 F0.1\n", "G1 P0\n"]
        # Generate the definitive block
        for s in after_washing_block:
            first_wash_block.append (s)
        # Leave a white line between blocks
        first_wash_block.append ("\n")
    
    
    ##### SPRAYING PHASE (solution dependent)
    try:
        spray_block_sol = []
        for sol in range(len(solution_to_use)):
            # First part of the block
            spray_block = [";;;;;;;;;; spraying phase\n"]
            ### The X-axis stays fixed (horizontal spraying)
            if horizontal_spraying[sol] == True:
                # Generate the vector of x and y positions
                # Y positions
                y_positions = []
                # Calculate the number of Y positions (according to the y length and the distance between lines) (since the path is an S, each y coordinate is reported twice, so the number of positions must be doubled)
                # One is negative and the other positive
                if coordinates_of_spray_y_axis[sol][0] < 0 and coordinates_of_spray_y_axis[sol][1] >= 0:
                    number_of_y_positions = abs(int((coordinates_of_spray_y_axis[sol][1] - coordinates_of_spray_y_axis[sol][0]) / distance_between_lines[sol]) * 2)
                    number_of_lines = abs(int((coordinates_of_spray_y_axis[sol][1] - coordinates_of_spray_y_axis[sol][0]) / distance_between_lines[sol]))
                    y_line_length = coordinates_of_spray_y_axis[sol][1] - coordinates_of_spray_y_axis[sol][0]
                # Both are positive
                if coordinates_of_spray_y_axis[sol][0] >= 0 and coordinates_of_spray_y_axis[sol][1] > 0:
                    number_of_y_positions = abs(int((coordinates_of_spray_y_axis[sol][1] - coordinates_of_spray_y_axis[sol][0]) / distance_between_lines[sol]) * 2)
                    number_of_lines = abs(int((coordinates_of_spray_y_axis[sol][1] - coordinates_of_spray_y_axis[sol][0]) / distance_between_lines[sol]))
                    y_line_length = coordinates_of_spray_y_axis[sol][1] - coordinates_of_spray_y_axis[sol][0]
                # Both are negative
                if coordinates_of_spray_y_axis[sol][0] < 0 and coordinates_of_spray_y_axis[sol][1] <= 0:
                    number_of_y_positions = abs(int((abs(coordinates_of_spray_y_axis[sol][0]) - abs(coordinates_of_spray_y_axis[sol][1])) / distance_between_lines[sol]) * 2)
                    number_of_lines = abs(int((abs(coordinates_of_spray_y_axis[sol][0]) - abs(coordinates_of_spray_y_axis[sol][1])) / distance_between_lines[sol]))
                    y_line_length = abs(coordinates_of_spray_y_axis[sol][0]) - abs(coordinates_of_spray_y_axis[sol][1])
                # Calculate the spray travel on X
                # One is negative and the other positive
                if coordinates_of_spray_x_axis[sol][0] < 0 and coordinates_of_spray_x_axis[sol][1] >= 0:
                    x_line_length = coordinates_of_spray_x_axis[sol][1] - coordinates_of_spray_x_axis[sol][0]
                # Both are positive
                if coordinates_of_spray_x_axis[sol][0] >= 0 and coordinates_of_spray_x_axis[sol][1] > 0:
                    x_line_length = coordinates_of_spray_x_axis[sol][1] - coordinates_of_spray_x_axis[sol][0]
                # Both are negative
                if coordinates_of_spray_x_axis[sol][0] < 0 and coordinates_of_spray_x_axis[sol][1] <= 0:
                    x_line_length = abs(coordinates_of_spray_x_axis[sol][0]) - abs(coordinates_of_spray_x_axis[sol][1])
                # Calculate the spray travel distance
                spray_travel = number_of_lines * x_line_length + y_line_length
                # Calculate the spray time
                spray_time = spray_travel / speed_of_movement[sol]
                # Calculate the spray density
                spray_density = float(matrix_density[sol]) / 100 * distance_between_lines[sol]
                # Calculate the spray syringe volume
                spray_syringe_volume = spray_travel * spray_density
                # Calculate the spray syringe travel
                spray_syringe_travel = spray_syringe_volume / spray_syringe_volume_per_travel
                # Spray syringe volume in X
                spray_syringe_x = x_line_length * spray_density / spray_syringe_volume_per_travel
                # Spray syringe volume in Y
                spray_syringe_y = distance_between_lines[sol] * spray_density / spray_syringe_volume_per_travel
                # Calculate the other positions (since the path is an S, each y coordinate is reported twice)
                for i in range(number_of_y_positions-1):
                    # The first position is where to start spraying (since the path is an S, each y coordinate is reported twice)
                    if len(y_positions) == 0:
                        y_positions.append (float(coordinates_of_spray_y_axis[sol][0]))
                        y_positions.append (float(coordinates_of_spray_y_axis[sol][0]))
                    else:
                        y_positions.append (float(y_positions[i-1] + distance_between_lines[sol]))
                # X positions
                x_positions = []
                # Calculate the other positions (since the path is an S, each x coordinate is reported twice)
                for i in range(number_of_y_positions):
                    # The first position and the last position are on the opposite side of the starting position (where to go spraying, along the x axis) (since the path is an S, each y coordinate is reported twice)
                    if len(x_positions) == 0:
                        x_positions.append(float(coordinates_of_spray_x_axis[sol][1]))
                    elif len(x_positions) == 1:
                        x_positions.append(float(coordinates_of_spray_x_axis[sol][0]))
                    elif x_positions[i-1] != x_positions[i-2]:
                        x_positions.append(x_positions[i-1])
                    elif x_positions[i-1] == x_positions[i-2]:
                        x_positions.append(x_positions[i-3])
                # Values of P
                p_values = []
                for i in range(int(number_of_y_positions/2)):
                    p_values.append (float(-spray_syringe_y))
                    p_values.append (float(-spray_syringe_x))
                # Generate the final spray subblock
                spray_subblock2 = [";;; spray\n"]
                for i in range(number_of_y_positions):
                    # Create the line and append it to the list of the block lines
                    line = "G1 X%s Y%s P%s F%s\n" %(x_positions[i], y_positions[i], p_values[i], speed_of_movement[sol])
                    spray_subblock2.append (line)
                spray_subblock2.append ("G1 Y%s Z%s F%s\n" %(float(coordinates_of_spray_y_axis[sol][0]), float(coordinates_of_z_axis_during_movement), max_speed_of_movement))
                # Generate the first part of the block
                spray_subblock1 = ["M106\n", "M82\n", "G1 V%s F%s\n" %(solution_to_use[sol], max_speed_of_movement), "G4 S1\n", "G1 P%s F%s\n" %(spray_syringe_travel+2, max_speed_of_movement), "G1 V1 F%s\n" %(max_speed_of_movement), "G4 S1\n", "G1 F0.1\n", "G1 P%s\n" %(spray_syringe_travel), "\n", ";;; where to start spraying\n", "G1 Z%s F%s\n" %(float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 X%s Y%s F%s\n" %(float(coordinates_of_spray_x_axis[sol][0]), float(coordinates_of_spray_y_axis[sol][0]), max_speed_of_movement), "G1 Z%s F%s\n" %(float(coordinates_of_spray_z_axis[sol]), max_speed_of_movement), "\n", "M83\n", "\n"]
                # Attach the spray sub-block to the global spray block
                for s in spray_subblock1:
                    spray_block.append(s)
                for s in spray_subblock2:
                    spray_block.append(s)
                # Add a white line
                spray_block.append("\n")
                # Add additional waiting phase
                for s in additional_waiting_time_after_spraying_block[sol]:
                    spray_block.append(s)
            ### The Y-axis stays fixed (vertical spraying)
            else:
                # Generate the vector of x and y positions
                # X positions
                x_positions = []
                # Calculate the number of X positions (according to the x length and the distance between lines) (since the path is an S, each x coordinate is reported twice, so the number of positions must be doubled)
                # One is negative and the other positive
                if coordinates_of_spray_x_axis[sol][0] < 0 and coordinates_of_spray_x_axis[sol][1] >= 0:
                    number_of_x_positions = abs(int((coordinates_of_spray_x_axis[sol][1] - coordinates_of_spray_x_axis[sol][0]) / distance_between_lines[sol]) * 2)
                    number_of_lines = abs(int((coordinates_of_spray_x_axis[sol][1] - coordinates_of_spray_x_axis[sol][0]) / distance_between_lines[sol]))
                    x_line_length = coordinates_of_spray_x_axis[sol][1] - coordinates_of_spray_x_axis[sol][0]
                # Both are positive
                if coordinates_of_spray_x_axis[sol][0] >= 0 and coordinates_of_spray_x_axis[sol][1] > 0:
                    number_of_x_positions = abs(int((coordinates_of_spray_x_axis[sol][1] - coordinates_of_spray_x_axis[sol][0]) / distance_between_lines[sol]) * 2)
                    number_of_lines = abs(int((coordinates_of_spray_x_axis[sol][1] - coordinates_of_spray_x_axis[sol][0]) / distance_between_lines[sol]))
                    x_line_length = coordinates_of_spray_x_axis[sol][1] - coordinates_of_spray_x_axis[sol][0]
                # Both are negative
                if coordinates_of_spray_x_axis[sol][0] < 0 and coordinates_of_spray_x_axis[sol][1] <= 0:
                    number_of_x_positions = abs(int((abs(coordinates_of_spray_x_axis[sol][0]) - abs(coordinates_of_spray_x_axis[sol][1])) / distance_between_lines[sol]) * 2)
                    number_of_lines = abs(int((abs(coordinates_of_spray_x_axis[sol][0]) - abs(coordinates_of_spray_x_axis[sol][1])) / distance_between_lines[sol]))
                    x_line_length = abs(coordinates_of_spray_x_axis[sol][0]) - abs(coordinates_of_spray_x_axis[sol][1])
                # Calculate the spray travel on Y
                # One is negative and the other positive
                if coordinates_of_spray_y_axis[sol][0] < 0 and coordinates_of_spray_y_axis[sol][1] >= 0:
                    y_line_length = coordinates_of_spray_y_axis[sol][1] - coordinates_of_spray_y_axis[sol][0]
                # Both are positive
                if coordinates_of_spray_y_axis[sol][0] >= 0 and coordinates_of_spray_y_axis[sol][1] > 0:
                    y_line_length = coordinates_of_spray_y_axis[sol][1] - coordinates_of_spray_y_axis[sol][0]
                # Both are negative
                if coordinates_of_spray_y_axis[sol][0] < 0 and coordinates_of_spray_y_axis[sol][1] <= 0:
                    y_line_length = abs(coordinates_of_spray_y_axis[sol][0]) - abs(coordinates_of_spray_y_axis[sol][1])
                # Calculate the spray travel distance
                spray_travel = number_of_lines * y_line_length + x_line_length
                # Calculate the spray time
                spray_time = spray_travel / speed_of_movement[sol]
                # Calculate the spray density
                spray_density = float(matrix_density[sol]) / 100 * distance_between_lines[sol]
                # Calculate the spray syringe volume
                spray_syringe_volume = spray_travel * spray_density
                # Calculate the spray syringe travel
                spray_syringe_travel = spray_syringe_volume / spray_syringe_volume_per_travel
                # Spray syringe volume in X
                spray_syringe_y = y_line_length * spray_density / spray_syringe_volume_per_travel
                # Spray syringe volume in Y
                spray_syringe_x = distance_between_lines[sol] * spray_density / spray_syringe_volume_per_travel
                # Calculate the other positions (since the path is an S, each y coordinate is reported twice)
                for i in range(number_of_x_positions-1):
                    # The first position is where to start spraying (since the path is an S, each y coordinate is reported twice)
                    if len(x_positions) == 0:
                        x_positions.append (float(coordinates_of_spray_x_axis[sol][0]))
                        x_positions.append (float(coordinates_of_spray_x_axis[sol][0]))
                    else:
                        x_positions.append (float(x_positions[i-1] + distance_between_lines[sol]))
                # Y positions
                y_positions = []
                # Calculate the other positions (since the path is an S, each x coordinate is reported twice)
                for i in range(number_of_x_positions):
                    # The first position and the last position are on the opposite side of the starting position (where to go spraying, along the x axis) (since the path is an S, each y coordinate is reported twice)
                    if len(y_positions) == 0:
                        y_positions.append(float(coordinates_of_spray_y_axis[sol][1]))
                    elif len(y_positions) == 1:
                        y_positions.append(float(coordinates_of_spray_y_axis[sol][0]))
                    elif y_positions[i-1] != y_positions[i-2]:
                        y_positions.append(y_positions[i-1])
                    elif y_positions[i-1] == y_positions[i-2]:
                        y_positions.append(y_positions[i-3])
                # Values of P
                p_values = []
                for i in range(int(number_of_x_positions/2)):
                    p_values.append (float(-spray_syringe_x))
                    p_values.append (float(-spray_syringe_y))
                # Generate the final spray ssubblock
                spray_subblock2 = [";;; spray\n"]
                for i in range(number_of_x_positions):
                    # Create the line and append it to the list of the block lines
                    line = "G1 X%s Y%s P%s F%s\n" %(x_positions[i], y_positions[i], p_values[i], speed_of_movement[sol])
                    spray_subblock2.append (line)
                spray_subblock2.append ("G1 Y%s Z%s F%s\n" %(float(coordinates_of_spray_y_axis[sol][0]), float(coordinates_of_z_axis_during_movement), max_speed_of_movement))
                # Generate the first part of the block
                spray_subblock1 = ["M106\n", "M82\n", "G1 V%s F%s\n" %(solution_to_use[sol], max_speed_of_movement), "G4 S1\n", "G1 P%s F%s\n" %(spray_syringe_travel+2, max_speed_of_movement), "G1 V1 F%s\n" %(max_speed_of_movement), "G4 S1\n", "G1 F0.1\n", "G1 P%s\n" %(spray_syringe_travel), "\n", ";;; where to start spraying\n", "G1 Z%s F%s\n" %(float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 X%s Y%s F%s\n" %(float(coordinates_of_spray_x_axis[sol][0]), float(coordinates_of_spray_y_axis[sol][0]), max_speed_of_movement), "G1 Z%s F%s\n" %(float(coordinates_of_spray_z_axis[sol]), max_speed_of_movement), "\n", "M83\n", "\n"]
                # Attach the spray sub-block to the global spray block
                for s in spray_subblock1:
                    spray_block.append(s)
                for s in spray_subblock2:
                    spray_block.append(s)
                # Add a white line
                spray_block.append("\n")
                # Add additional waiting phase
                for s in additional_waiting_time_after_spraying_block[sol]:
                    spray_block.append(s)
            # Leave a white line between blocks
            spray_block.append ("\n")
            # Add this chunk to the final block
            spray_block_sol.append(spray_block)
    except:
        # First part of the block
        spray_block = [";;;;;;;;;; spraying phase\n"]
        ### The X-axis stays fixed (horizontal spraying)
        if horizontal_spraying == True:
            # Generate the vector of x and y positions
            # Y positions
            y_positions = []
            # Calculate the number of Y positions (according to the y length and the distance between lines) (since the path is an S, each y coordinate is reported twice, so the number of positions must be doubled)
            # One is negative and the other positive
            if coordinates_of_spray_y_axis[0] < 0 and coordinates_of_spray_y_axis[1] >= 0:
                number_of_y_positions = abs(int((coordinates_of_spray_y_axis[1] - coordinates_of_spray_y_axis[0]) / distance_between_lines) * 2)
                number_of_lines = abs(int((coordinates_of_spray_y_axis[1] - coordinates_of_spray_y_axis[0]) / distance_between_lines))
                y_line_length = coordinates_of_spray_y_axis[1] - coordinates_of_spray_y_axis[0]
            # Both are positive
            if coordinates_of_spray_y_axis[0] >= 0 and coordinates_of_spray_y_axis[1] > 0:
                number_of_y_positions = abs(int((coordinates_of_spray_y_axis[1] - coordinates_of_spray_y_axis[0]) / distance_between_lines) * 2)
                number_of_lines = abs(int((coordinates_of_spray_y_axis[1] - coordinates_of_spray_y_axis[0]) / distance_between_lines))
                y_line_length = coordinates_of_spray_y_axis[1] - coordinates_of_spray_y_axis[0]
            # Both are negative
            if coordinates_of_spray_y_axis[0] < 0 and coordinates_of_spray_y_axis[1] <= 0:
                number_of_y_positions = abs(int((abs(coordinates_of_spray_y_axis[0]) - abs(coordinates_of_spray_y_axis[1])) / distance_between_lines) * 2)
                number_of_lines = abs(int((abs(coordinates_of_spray_y_axis[0]) - abs(coordinates_of_spray_y_axis[1])) / distance_between_lines))
                y_line_length = abs(coordinates_of_spray_y_axis[0]) - abs(coordinates_of_spray_y_axis[1])
            # Calculate the spray travel on X
            # One is negative and the other positive
            if coordinates_of_spray_x_axis[0] < 0 and coordinates_of_spray_x_axis[1] >= 0:
                x_line_length = coordinates_of_spray_x_axis[1] - coordinates_of_spray_x_axis[0]
            # Both are positive
            if coordinates_of_spray_x_axis[0] >= 0 and coordinates_of_spray_x_axis[1] > 0:
                x_line_length = coordinates_of_spray_x_axis[1] - coordinates_of_spray_x_axis[0]
            # Both are negative
            if coordinates_of_spray_x_axis[0] < 0 and coordinates_of_spray_x_axis[1] <= 0:
                x_line_length = abs(coordinates_of_spray_x_axis[0]) - abs(coordinates_of_spray_x_axis[1])
            # Calculate the spray travel distance
            spray_travel = number_of_lines * x_line_length + y_line_length
            # Calculate the spray time
            spray_time = spray_travel / speed_of_movement
            # Calculate the spray density
            spray_density = float(matrix_density) / 100 * distance_between_lines
            # Calculate the spray syringe volume
            spray_syringe_volume = spray_travel * spray_density
            # Calculate the spray syringe travel
            spray_syringe_travel = spray_syringe_volume / spray_syringe_volume_per_travel
            # Spray syringe volume in X
            spray_syringe_x = x_line_length * spray_density / spray_syringe_volume_per_travel
            # Spray syringe volume in Y
            spray_syringe_y = distance_between_lines * spray_density / spray_syringe_volume_per_travel
            # Calculate the other positions (since the path is an S, each y coordinate is reported twice)
            for i in range(number_of_y_positions-1):
                # The first position is where to start spraying (since the path is an S, each y coordinate is reported twice)
                if len(y_positions) == 0:
                    y_positions.append (float(coordinates_of_spray_y_axis[0]))
                    y_positions.append (float(coordinates_of_spray_y_axis[0]))
                else:
                    y_positions.append (float(y_positions[i-1] + distance_between_lines))
            # X positions
            x_positions = []
            # Calculate the other positions (since the path is an S, each x coordinate is reported twice)
            for i in range(number_of_y_positions):
                # The first position and the last position are on the opposite side of the starting position (where to go spraying, along the x axis) (since the path is an S, each y coordinate is reported twice)
                if len(x_positions) == 0:
                    x_positions.append(float(coordinates_of_spray_x_axis[1]))
                elif len(x_positions) == 1:
                    x_positions.append(float(coordinates_of_spray_x_axis[0]))
                elif x_positions[i-1] != x_positions[i-2]:
                    x_positions.append(x_positions[i-1])
                elif x_positions[i-1] == x_positions[i-2]:
                    x_positions.append(x_positions[i-3])
            # Values of P
            p_values = []
            for i in range(int(number_of_y_positions/2)):
                p_values.append (float(-spray_syringe_y))
                p_values.append (float(-spray_syringe_x))
            # Generate the final spray ssubblock
            spray_subblock2 = [";;; spray\n"]
            for i in range(number_of_y_positions):
                # Create the line and append it to the list of the block lines
                line = "G1 X%s Y%s P%s F%s\n" %(x_positions[i], y_positions[i], p_values[i], speed_of_movement)
                spray_subblock2.append (line)
            spray_subblock2.append ("G1 Y%s Z%s F%s\n" %(float(coordinates_of_spray_y_axis[0]), float(coordinates_of_z_axis_during_movement), max_speed_of_movement))
            # Generate the first part of the block
            spray_subblock1 = ["M106\n", "M82\n", "G1 V%s F%s\n" %(solution_to_use, max_speed_of_movement), "G4 S1\n", "G1 P%s F%s\n" %(spray_syringe_travel+2, max_speed_of_movement), "G1 V1 F%s\n" %(max_speed_of_movement), "G4 S1\n", "G1 F0.1\n", "G1 P%s\n" %(spray_syringe_travel), "\n", ";;; where to start spraying\n", "G1 Z%s F%s\n" %(float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 X%s Y%s F%s\n" %(float(coordinates_of_spray_x_axis[0]), float(coordinates_of_spray_y_axis[0]), max_speed_of_movement), "G1 Z%s F%s\n" %(float(coordinates_of_spray_z_axis), max_speed_of_movement), "\n", "M83\n", "\n"]
            # Attach the spray sub-block to the global spray block
            for s in spray_subblock1:
                spray_block.append(s)
            for s in spray_subblock2:
                spray_block.append(s)
            # Add a white line
            spray_block.append("\n")
            # Add additional waiting phase
            for s in additional_waiting_time_after_spraying_block:
                spray_block.append(s)
        ### The Y-axis stays fixed (vertical spraying)
        else:
            # Generate the vector of x and y positions
            # X positions
            x_positions = []
            # Calculate the number of X positions (according to the x length and the distance between lines) (since the path is an S, each x coordinate is reported twice, so the number of positions must be doubled)
            # One is negative and the other positive
            if coordinates_of_spray_x_axis[0] < 0 and coordinates_of_spray_x_axis[1] >= 0:
                number_of_x_positions = abs(int((coordinates_of_spray_x_axis[1] - coordinates_of_spray_x_axis[0]) / distance_between_lines) * 2)
                number_of_lines = abs(int((coordinates_of_spray_x_axis[1] - coordinates_of_spray_x_axis[0]) / distance_between_lines))
                x_line_length = coordinates_of_spray_x_axis[1] - coordinates_of_spray_x_axis[0]
            # Both are positive
            if coordinates_of_spray_x_axis[0] >= 0 and coordinates_of_spray_x_axis[1] > 0:
                number_of_x_positions = abs(int((coordinates_of_spray_x_axis[1] - coordinates_of_spray_x_axis[0]) / distance_between_lines) * 2)
                number_of_lines = abs(int((coordinates_of_spray_x_axis[1] - coordinates_of_spray_x_axis[0]) / distance_between_lines))
                x_line_length = coordinates_of_spray_x_axis[1] - coordinates_of_spray_x_axis[0]
            # Both are negative
            if coordinates_of_spray_x_axis[0] < 0 and coordinates_of_spray_x_axis[1] <= 0:
                number_of_x_positions = abs(int((abs(coordinates_of_spray_x_axis[0]) - abs(coordinates_of_spray_x_axis[1])) / distance_between_lines) * 2)
                number_of_lines = abs(int((abs(coordinates_of_spray_x_axis[0]) - abs(coordinates_of_spray_x_axis[1])) / distance_between_lines))
                x_line_length = abs(coordinates_of_spray_x_axis[0]) - abs(coordinates_of_spray_x_axis[1])
            # Calculate the spray travel on Y
            # One is negative and the other positive
            if coordinates_of_spray_y_axis[0] < 0 and coordinates_of_spray_y_axis[1] >= 0:
                y_line_length = coordinates_of_spray_y_axis[1] - coordinates_of_spray_y_axis[0]
            # Both are positive
            if coordinates_of_spray_y_axis[0] >= 0 and coordinates_of_spray_y_axis[1] > 0:
                y_line_length = coordinates_of_spray_y_axis[1] - coordinates_of_spray_y_axis[0]
            # Both are negative
            if coordinates_of_spray_y_axis[0] < 0 and coordinates_of_spray_y_axis[1] <= 0:
                y_line_length = abs(coordinates_of_spray_y_axis[0]) - abs(coordinates_of_spray_y_axis[1])
            # Calculate the spray travel distance
            spray_travel = number_of_lines * y_line_length + x_line_length
            # Calculate the spray time
            spray_time = spray_travel / speed_of_movement
            # Calculate the spray density
            spray_density = float(matrix_density) / 100 * distance_between_lines
            # Calculate the spray syringe volume
            spray_syringe_volume = spray_travel * spray_density
            # Calculate the spray syringe travel
            spray_syringe_travel = spray_syringe_volume / spray_syringe_volume_per_travel
            # Spray syringe volume in X
            spray_syringe_y = y_line_length * spray_density / spray_syringe_volume_per_travel
            # Spray syringe volume in Y
            spray_syringe_x = distance_between_lines * spray_density / spray_syringe_volume_per_travel
            # Calculate the other positions (since the path is an S, each y coordinate is reported twice)
            for i in range(number_of_x_positions-1):
                # The first position is where to start spraying (since the path is an S, each y coordinate is reported twice)
                if len(x_positions) == 0:
                    x_positions.append (float(coordinates_of_spray_x_axis[0]))
                    x_positions.append (float(coordinates_of_spray_x_axis[0]))
                else:
                    x_positions.append (float(x_positions[i-1] + distance_between_lines))
            # Y positions
            y_positions = []
            # Calculate the other positions (since the path is an S, each x coordinate is reported twice)
            for i in range(number_of_x_positions):
                # The first position and the last position are on the opposite side of the starting position (where to go spraying, along the x axis) (since the path is an S, each y coordinate is reported twice)
                if len(y_positions) == 0:
                    y_positions.append(float(coordinates_of_spray_y_axis[1]))
                elif len(y_positions) == 1:
                    y_positions.append(float(coordinates_of_spray_y_axis[0]))
                elif y_positions[i-1] != y_positions[i-2]:
                    y_positions.append(y_positions[i-1])
                elif y_positions[i-1] == y_positions[i-2]:
                    y_positions.append(y_positions[i-3])
            # Values of P
            p_values = []
            for i in range(int(number_of_x_positions/2)):
                p_values.append (float(-spray_syringe_x))
                p_values.append (float(-spray_syringe_y))
            # Generate the final spray ssubblock
            spray_subblock2 = [";;; spray\n"]
            for i in range(number_of_x_positions):
                # Create the line and append it to the list of the block lines
                line = "G1 X%s Y%s P%s F%s\n" %(x_positions[i], y_positions[i], p_values[i], speed_of_movement)
                spray_subblock2.append (line)
            spray_subblock2.append ("G1 Y%s Z%s F%s\n" %(float(coordinates_of_spray_y_axis[0]), float(coordinates_of_z_axis_during_movement), max_speed_of_movement))
            # Generate the first part of the block
            spray_subblock1 = ["M106\n", "M82\n", "G1 V%s F%s\n" %(solution_to_use, max_speed_of_movement), "G4 S1\n", "G1 P%s F%s\n" %(spray_syringe_travel+2, max_speed_of_movement), "G1 V1 F%s\n" %(max_speed_of_movement), "G4 S1\n", "G1 F0.1\n", "G1 P%s\n" %(spray_syringe_travel), "\n", ";;; where to start spraying\n", "G1 Z%s F%s\n" %(float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 X%s Y%s F%s\n" %(float(coordinates_of_spray_x_axis[0]), float(coordinates_of_spray_y_axis[0]), max_speed_of_movement), "G1 Z%s F%s\n" %(float(coordinates_of_spray_z_axis), max_speed_of_movement), "\n", "M83\n", "\n"]
            # Attach the spray sub-block to the global spray block
            for s in spray_subblock1:
                spray_block.append(s)
            for s in spray_subblock2:
                spray_block.append(s)
            # Add a white line
            spray_block.append("\n")
            # Add additional waiting phase
            for s in additional_waiting_time_after_spraying_block:
                spray_block.append(s)
        # Leave a white line between blocks
        spray_block.append ("\n")


    ##### INTER-SPRAY WASH (solution dependent)
    try:
        interspray_wash_block_sol = []
        for sol in range(len(solution_to_use)):
            interspray_wash_block = [";;;;;;;;;; interspray wash\n"]
            # Go to wash position first
            for s in go_to_wash_position_block:
                interspray_wash_block.append (s)
            # Washing sub-block
            interspray_wash_subblock = [";;;;; wash\n", "M82\n", "G1 V0 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 P0 F%s\n" %max_speed_of_movement, "M106 S0\n", "G4 S0.0\n"]
            # Generate the definitive block
            for s in interspray_wash_subblock:
                interspray_wash_block.append (s)                
            # Leave a white line between blocks
            interspray_wash_block.append ("\n")
            # Add this chunk to the final block
            interspray_wash_block_sol.append(interspray_wash_block)
    except:
        interspray_wash_block = [";;;;;;;;;; interspray wash\n"]
        # Go to wash position first
        for s in go_to_wash_position_block:
            interspray_wash_block.append (s)
        # Define the washing sub-block
        interspray_wash_subblock = [";;;;; wash\n", "M82\n", "G1 V0 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 P0 F%s\n" %max_speed_of_movement, "M106 S0\n", "G4 S0.0\n"]
        # Generate the definitive block
        for s in interspray_wash_subblock:
                interspray_wash_block.append (s)
        # Leave a white line between blocks
        interspray_wash_block.append ("\n")
    
    
    ##### SYRINGE EMPTYING (solution dependent)
    try:
        syringe_emptying_block_sol = []
        for sol in range(len(solution_to_use)):
            syringe_emptying_block = [";;;;; syringe emptying\n"]
            syringe_emptying_block.append ("G1 P0 F%s\n" %(max_speed_of_movement/2))
            # Valve rinsing block (80 microlitres each step)
            valve_rinsing_block = [";;;;; valve rinsing\n"]
            valve_rinsing_subblock = ["G1 V1.5 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 P4.8 F%s\n" %max_speed_of_movement, "G1 V2 F%s\n" %max_speed_of_movement, "G4 S2\n", "G1 V0 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 P0 F%s\n" %(max_speed_of_movement/2)]
            for s in valve_rinsing_subblock:
                valve_rinsing_block.append (s)
            # Generate the definitive block based on the number of repetitions
            for i in range(number_of_valve_rinsing_cycles[sol]):
                for s in valve_rinsing_block:
                    syringe_emptying_block.append (s)
            # Leave a white line between blocks
            syringe_emptying_block.append ("\n")
            # Add this chunk to the final block
            syringe_emptying_block_sol.append(syringe_emptying_block)
    except:
        syringe_emptying_block = [";;;;; syringe emptying\n"]
        syringe_emptying_block.append ("G1 P0 F%s\n" %(max_speed_of_movement/2))
        # Valve rinsing block (80 microlitres each step)
        valve_rinsing_block = [";;;;; valve rinsing\n"]
        valve_rinsing_subblock = ["G1 V1.5 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 P4.8 F%s\n" %max_speed_of_movement, "G1 V2 F%s\n" %max_speed_of_movement, "G4 S2\n", "G1 V0 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 P0 F%s\n" %(max_speed_of_movement/2)]
        for s in valve_rinsing_subblock:
            valve_rinsing_block.append (s)
        # Generate the definitive block based on the number of repetitions
        for i in range(number_of_valve_rinsing_cycles):
            for s in valve_rinsing_block:
                syringe_emptying_block.append (s)
        # Leave a white line between blocks
        syringe_emptying_block.append ("\n")
    
    
    ##### SPRAY RINSING (same for all)
    spray_rinsing_block = [";;;;; spray rinsing\n"]
    spray_rinsing_subblock = ["G1 V1.5 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 P4 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 V2 F%s\n" %max_speed_of_movement, "G4 S2\n", "G1 V1 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 F0.1\n", "G1 P0\n", "M106 S0\n"]
    # Generate the definitive block
    for s in spray_rinsing_subblock:
        spray_rinsing_block.append (s)
    # Leave a white line between blocks
    spray_rinsing_block.append ("\n")
    
    
    ##### CAPILLARY RINSING (same for all)
    capillary_rinsing_block = [";;;;; capillary rinsing\n"]
    capillary_rinsing_subblock = ["G1 V1.5 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 P3 F%s\n" %max_speed_of_movement, "G1 V2 F%s\n" %max_speed_of_movement, "G4 S2\n", "G1 V1 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 F0.1\n", "G1 P0\n", "G1 P1\n"]
    # Generate the definitive block
    for s in capillary_rinsing_subblock:
        capillary_rinsing_block.append (s)
    # Leave a white line between blocks
    capillary_rinsing_block.append ("\n")
    
    
    ##### DRYING (same for all)
    drying_block = [";;;;; drying\n"]
    drying_subblock = ["M106\n", "G1 P0\n", "G4 S%s\n" %drying_time, "M106 S0\n"]
    # Generate the definitive block
    for s in drying_subblock:
        drying_block.append (s)
    # Leave a white line between blocks
    drying_block.append ("\n")
    
    
    ##### SPRAY PARKING (same for all)
    parking_spray_block = [";;;;; parking spray\n"]
    parking_spray_subblock = ["G1 Z%s F%s\n" %(float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 X%s Y%s Z%s F%s\n" %(float(initial_x_coordinates), float(initial_y_coordinates), float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 Z%s F%s\n" %(float(coordinates_of_z_rest), max_speed_of_movement)]
    # Generate the definitive block
    for s in parking_spray_subblock:
        parking_spray_block.append (s)
    # Leave a white line between blocks
    parking_spray_block.append ("\n")
    
    
    ##### CLEANING PROCEDURE (solution dependent)
    # Go to wash + emptying syringe + rinsing valve + rinsing spray + rinsing capillary + drying + parking spray
    try:
        cleaning_procedure_block_sol = []
        for sol in range(len(solution_to_use)):
            cleaning_procedure_block = [";;;;;;;;;; cleaning procedure\n"]
            cleaning_procedure_subblock = ["M82\n", "G90\n"]
            # Generate the definitive block
            for s in cleaning_procedure_subblock:
                cleaning_procedure_block.append(s)
            # Go to wash
            for s in go_to_wash_position_block:
                cleaning_procedure_block.append (s)
            # More code
            cleaning_procedure_subblock = ["M106\n", "G1 V0 F%s\n" %max_speed_of_movement, "G4 S1\n"]
            for s in cleaning_procedure_subblock:
                cleaning_procedure_block.append(s)
            for s in syringe_emptying_block_sol[sol]:
                cleaning_procedure_block.append (s)
            for s in spray_rinsing_block:
                cleaning_procedure_block.append (s)
            for s in capillary_rinsing_block:
                cleaning_procedure_block.append (s)
            for s in drying_block:
                cleaning_procedure_block.append (s)
            for s in parking_spray_block:
                cleaning_procedure_block.append (s)
            # Add this chunk to the final block
            cleaning_procedure_block_sol.append(cleaning_procedure_block)
    except:
        cleaning_procedure_block = [";;;;;;;;;; cleaning procedure\n"]
        cleaning_procedure_subblock = ["M82\n", "G90\n"]
        # Generate the definitive block
        for s in cleaning_procedure_subblock:
            cleaning_procedure_block.append(s)
        # Go to wash
        for s in go_to_wash_position_block:
            cleaning_procedure_block.append (s)
        # More code
        cleaning_procedure_subblock = ["M106\n", "G1 V0 F%s\n" %max_speed_of_movement, "G4 S1\n"]
        for s in cleaning_procedure_subblock:
            cleaning_procedure_block.append(s)
        for s in syringe_emptying_block:
            cleaning_procedure_block.append (s)
        for s in spray_rinsing_block:
            cleaning_procedure_block.append (s)
        for s in capillary_rinsing_block:
            cleaning_procedure_block.append (s)
        for s in drying_block:
            cleaning_procedure_block.append (s)
        for s in parking_spray_block:
            cleaning_procedure_block.append (s)
    
    
    ##### MOTORS OFF (same for all)
    motors_off_block = [";;;;;;;;;; motors off\n", "M18\n"]
    # Leave a white line between blocks
    motors_off_block.append ("\n")
    
    
    ##### TEMPERATURE (same for all)
    try:
        heat_bed_temperature_block_sol = []
        for sol in range(len(solution_to_use)):
            heat_bed_temperature_block = [";;;;;;;;;; heat bed temperature\n", "M140 S%s\n" %(heat_bed_temperature[sol]), "\n"]
            heat_bed_temperature_block_sol.append(heat_bed_temperature_block)
    except:
        heat_bed_temperature_block = [";;;;;;;;;; heat bed temperature\n", "M140 S%s\n" %(heat_bed_temperature), "\n"]
    
    
    ##### HEAT BED OFF (same for all)
    heat_bed_off_block = [";;;;;;;;;; heat bed off\n", "M140 S0\n"]
    # Leave a white line between blocks
    heat_bed_off_block.append ("\n")
    
    
    
    
    
    ########## WRITE THE LINES TO THE OUTPUT FILE
    
    # Move to the working directory (set)
    os.chdir(output_folder)
    # Get the filename from the GUI entry
    output_file = filename_entry.get()
    # Add the extension to the file automatically
    if ".gcode" not in output_file:
        output_file = str(output_file) + ".gcode"
    # Open the file and write the lines
    with open(output_file, "w") as f:
        # Initialisation block
        for line in initialisation_block:
            f.writelines(line)
        try:
        ## Solution dependent blocks
            for sol in range(len(solution_to_use)):
                # Heat bed block only if it's present
                if heat_bed_presence == "y":
                    # Bring the heat bed to the desired temperature
                    for line in heat_bed_temperature_block_sol[sol]:
                        f.writelines(line)
                # First wash block (do not run it if it's not the beginning of the method and if the solution does not change)
                if sol == 0 or (solution_to_use[sol] != solution_to_use[sol-1]):
                    for line in first_wash_block_sol[sol]:
                        f.writelines(line)
                # Spray
                for i in range(number_of_spray_cycles[sol]):
                    for line in spray_block_sol[sol]:
                        f.writelines (line)
                    # The interspray wash can be skipped if the user does not want it
                    if interspray_wash_choice[sol] == "y":
                        for line in interspray_wash_block_sol[sol]:
                            f.writelines (line)
                    else:
                        for line in go_to_wash_position_block:
                            f.writelines (line)
                # Syringe emptying block (cleaning is always to be performed, it is advisable)
                # Do not perform it if the following solution is the same as the one that just sprayed (use the try command, because if we are at the end it fails, and so the cleaning procedure must be performed anyway)
                try:
                    if solution_to_use[sol+1] == solution_to_use[sol]:
                        pass
                    else:
                        for line in cleaning_procedure_block_sol[sol]:
                            f.writelines(line)
                except:
                    for line in cleaning_procedure_block_sol[sol]:
                        f.writelines(line)
                # Waiting phase (not after the last spray cycle, only between spray cycles)
                if sol < (range(len(solution_to_use))[-1]):
                    for line in waiting_phase_between_solutions_block_sol[sol]:
                        f.writelines(line)
        except:
            # Heat bed block only if it's present
            if heat_bed_presence == "y":
                # Bring the heat bed to the desired temperature
                for line in heat_bed_temperature_block:
                    f.writelines(line)
            # First wash block
            for line in first_wash_block:
                f.writelines(line)
            # Spray
            for i in range(number_of_spray_cycles):
                for line in spray_block:
                    f.writelines (line)
                # The interspray wash can be skipped if the user does not want it
                    if interspray_wash_choice == "y":
                        for line in interspray_wash_block:
                            f.writelines (line)
                    else:
                        for line in go_to_wash_position_block:
                            f.writelines (line)
            # Syringe emptying block
            for line in cleaning_procedure_block:
                f.writelines(line)
        # Motors off
        for line in motors_off_block:
            f.writelines(line)
        # Heat bed block only if it's present
        if heat_bed_presence == "y":
            # Heat bed off
                for line in heat_bed_off_block:
                    f.writelines(line)
    # Gcode file generated!
    tkinter.Tk().withdraw()
    tkinter.messagebox.showinfo(title="gcode file generated", message="The gcode file\n\n'%s'\n\nhas been successfully generated and dumped in the folder\n\n'%s'" %(output_file, output_folder))










########## FUNCTION: Select where to save the GCODE method file
def show_info():
    Tk().withdraw()
    messagebox.showinfo(title="Info", message="This Gcode Method Generator for the iMatrixSpray\nhas been written by MANUEL GALLI\nfrom the University of Milano-Bicocca\nin the Python 3 programming language\n\n\n\n\nGitHub page:\n\nhttps://github.com/gmanuel89/\n\n\n\n\nThe source code can be found at:\n\nhttps://github.com/gmanuel89/iMatrixSpray/blob/master/iMatrixSpray - Method gcode generator (Python 3 TclTk, GUI).py")









########## FUNCTION: Select where to save the GCODE method file
def show_guide():
    Tk().withdraw()
    messagebox.showinfo(title="Help", message="Help on the iMatrixSpray parameters can be found here:\n\nhttps://github.com/gmanuel89/iMatrixSpray/blob/master/README.md\n\n\n\n\nThe iMatrixSpray device official website is:\n\nhttps://imatrixspray.com/")









########## FUNCTION: Close the program
def close_program_function():
    # Collapse the GUI Tk window
    window.destroy
    # Quit the Python session
    quit()





######################################################################


































############################## TCL-TK WINDOW

########## Main window
window = Tk()
window.title("iMatrixSpray Method Generator (gcode)")
window.resizable(False,False)
#window.wm_minsize(width=550, height=600)

# Get the resolution of the screen (to adjust the font size accordingly)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

##### Fonts
### Store the fonts in a variable for faster editing
# Get system info (Platform - Release - Version (- Linux Distro))
system_os = platform.system()
os_release = platform.release()
os_version = platform.version()
# Default sizes (determined on a 1680x1050 screen) (in order to make them adjust to the size screen, the screen resolution should be retrieved)
#title_font_size = 24
#other_font_size = 11
# Determine the font size according to the resolution
total_number_of_pixels = screen_width * screen_height
# Determine the scaling factor (according to a complex formula)
scaling_factor_title_font = float((0.03611 * total_number_of_pixels) + 9803.1254)
scaling_factor_other_font = float((0.07757 * total_number_of_pixels) + 23529.8386)
title_font_size = int(round(total_number_of_pixels / scaling_factor_title_font))
other_font_size = int(round(total_number_of_pixels / scaling_factor_other_font))
# Windows
if system_os == "Windows":
    # Define the fonts
    garamond_title_bold = font.Font(family = "Garamond", size = title_font_size, weight = "bold")
    garamond_other_normal = font.Font(family = "Garamond", size = other_font_size, weight = "normal")
    arial_title_bold = font.Font(family = "Arial", size = title_font_size, weight = "bold")
    arial_other_normal = font.Font(family = "Arial", size = other_font_size, weight = "normal")
    trebuchet_title_bold = font.Font(family = "Trebuchet MS", size = title_font_size, weight = "bold")
    trebuchet_other_normal = font.Font(family = "Trebuchet MS", size = other_font_size, weight = "normal")
    trebuchet_other_bold = font.Font(family = "Trebuchet MS", size = other_font_size, weight = "bold")
    # Use them in the GUI
    title_font = trebuchet_title_bold
    label_font = trebuchet_other_normal
    entry_font = trebuchet_other_normal
    button_font = trebuchet_other_bold
# Linux
elif system_os == "Linux":
    # Retrieve the linux distribution
    linux_distro = platform.linux_distribution()
    # Ubuntu
    if "Ubuntu" in linux_distro or "Ubuntu" in os_version:
        # Define the fonts
        ubuntu_title_bold = font.Font(family = "Ubuntu", size = title_font_size, weight = "bold")
        ubuntu_other_normal = font.Font(family = "Ubuntu", size = other_font_size, weight = "normal")
        ubuntu_other_bold = font.Font(family = "Ubuntu", size = other_font_size, weight = "bold")
        # Use them in the GUI
        title_font = ubuntu_title_bold
        label_font = ubuntu_other_normal
        entry_font = ubuntu_other_normal
        button_font = ubuntu_other_bold
    # Fedora
    elif "Fedora" in linux_distro or "Fedora" in os_version:
        # Define the fonts
        cantarell_title_bold = font.Font(family = "Cantarell", size = title_font_size, weight = "bold")
        cantarell_other_normal = font.Font(family = "Cantarell", size = other_font_size, weight = "normal")
        cantarell_other_bold = font.Font(family = "Cantarell", size = other_font_size, weight = "bold")
        # Use them in the GUI
        title_font = cantarell_title_bold
        label_font = cantarell_other_normal
        entry_font = cantarell_other_normal
        button_font = cantarell_other_bold
    # Other linux distros
    else:
        # Define the fonts
        liberation_title_bold = font.Font(family = "Liberation Sans", size = title_font_size, weight = "bold")
        liberation_other_normal = font.Font(family = "Liberation Sans", size = other_font_size, weight = "normal")
        liberation_other_bold = font.Font(family = "Liberation Sans", size = other_font_size, weight = "bold")
        # Use them in the GUI
        title_font = liberation_title_bold
        label_font = liberation_other_normal
        entry_font = liberation_other_normal
        button_font = liberation_other_bold
elif system_os == "Mac":
    # Define the fonts
    helvetica_title_bold = font.Font(family = "Helvetica", size = title_font_size, weight = "bold")
    helvetica_other_normal = font.Font(family = "Helvetica", size = other_font_size, weight = "normal") 
    helvetica_other_bold = font.Font(family = "Helvetica", size = other_font_size, weight = "bold")
    # Use them in the GUI
    title_font = helvetica_title_bold
    label_font = helvetica_other_normal
    entry_font = helvetica_other_normal
    button_font = helvetica_other_bold
else:
    # Define the fonts
    courier_title_bold = font.Font(family = "Courier New", size = title_font_size, weight = "bold")
    courier_other_normal = font.Font(family = "Courier New", size = other_font_size, weight = "normal") 
    courier_other_bold = font.Font(family = "Courier New", size = other_font_size, weight = "bold")
    # Use them in the GUI
    title_font = courier_title_bold
    label_font = courier_other_normal
    entry_font = courier_other_normal
    button_font = courier_other_bold
#font.families(root = window)



########## Labels (with grid positioning)
title_label = Label(window, text="iMatrixSpray method generator", font=title_font).grid(row=0,column=1)
solution_to_use_label = Label(window, text="Solution(s) to spray with\n(A,B,C or rinse) (default: A)\n", font=label_font).grid(row=1, column=0)
new_names_label = Label(window, text="Rename the solution(s) to spray with\n(separate the labels with commas)", font=label_font).grid(row=2,column=0)
waiting_phase_between_solutions_time_label = Label(window, text="Set how much the device has to wait\nbefore switching between two consecutive solutions\n(separate the times with commas) (default: 5s)", font=label_font).grid(row=3, column=0)
coordinates_of_spray_x_axis_label = Label(window, text="Set the x-axis coordinates of spraying (default: -60,60),\nin this format:x1,x2 x1,x2\n[hint: Coordinates for the small area are (-30,30)]", font=label_font).grid(row=4, column=0)
coordinates_of_spray_y_axis_label = Label(window, text="Set the y-axis coordinates of spraying (default: -80,80),\nin this format:y1,y2 y1,y2\n[hint: Coordinates for the small area are (40,60)]", font=label_font).grid(row=5, column=0)
height_of_the_needle_label = Label(window, text="Set the height of the needle (in millimeters)\n(default: 60mm)", font=label_font).grid(row=6, column=0)
distance_between_spray_lines_label = Label(window, text="Set the distance between lines when spraying\n(default: 5mm)", font=label_font).grid(row=7, column=0)
speed_of_movement_label = Label(window, text="Set the speed of movement\n(max: 200, default: 150)", font=label_font).grid(row=8, column=0)
matrix_density_label = Label(window, text="Set the density of the matrix on-tissue\n(in microlitres per squared centimeter) (max: 5, default: 1)", font=label_font).grid(row=9, column=0)
number_of_initial_wash_cycles_label = Label(window, text="Set the number of initial wash cycles\n(default: 5)", font=label_font).grid(row=10, column=0)
number_of_spray_cycles_label = Label(window, text="Set the number of spraying cycles\n(default:2)", font=label_font).grid(row=11, column=0)
interspray_wash_choice_label = Label(window, text="Should the device perform the interspray rinse?\n(default: y)", font=label_font).grid(row=12, column=2)
additional_waiting_time_between_cycles_label = Label(window, text="Set the additional time (in seconds)\nto wait after each spraying cycle (default:0s)", font=label_font).grid(row=12, column=0)
number_of_valve_rinsing_cycles_label = Label(window, text="Set the number of valve rinsing cycles\nwith the rinsing solution (default: 5)", font=label_font).grid(row=13, column=0)
drying_time_label = Label(window, text="Set the drying time\nfor the needle after rinsing (default: 8s)", font=label_font).grid(row=14, column=0)
horizontal_spraying_label = Label(window, text="Spray horizontally?\n(y or n, default: y)", font=label_font).grid(row=15, column=0)
filename_label = Label(window, text="Set the name of the gcode method file\n(file extension is automatically added)", font=label_font).grid(row=16, column=0)
heat_bed_presence_label = Label(window, text="Heat bed presence\n(y or n, default: y)", font=label_font).grid(row=8, column=2)
heat_bed_height_label = Label(window, text="Heat bed height\n(default 5mm)", font=label_font).grid(row=10, column=2)
heat_bed_temperature_label = Label(window, text="Heat bed temperature\n(default 0°C, do not heat)", font=label_font).grid(row=11, column=2)
check_for_updates_label = Label(window, text=("Version: " + program_version), font=label_font).grid(row=2, column=3)





########## Variables for Radiobuttons
heat_bed_presence_entry = StringVar()





########## Entry boxes / Radiobuttons (with positioning)
solution_to_use_entry = Entry(window, font=entry_font, justify="center")
new_names_entry = Entry(window, font=entry_font, justify="center")
waiting_phase_between_solutions_time_entry = Entry(window, font=entry_font, justify="center")
coordinates_of_spray_x_axis_entry = Entry(window, font=entry_font, justify="center")
coordinates_of_spray_y_axis_entry = Entry(window, font=entry_font, justify="center")
height_of_the_needle_entry = Entry(window, font=entry_font, justify="center")
distance_between_lines_entry = Entry(window, font=entry_font, justify="center")
speed_of_movement_entry = Entry(window, font=entry_font, justify="center")
matrix_density_entry = Entry(window, font=entry_font, justify="center")
number_of_initial_wash_cycles_entry = Entry(window, font=entry_font, justify="center")
number_of_spray_cycles_entry = Entry(window, font=entry_font, justify="center")
interspray_wash_choice_entry = Entry(window, font=entry_font, justify="center")
additional_waiting_time_after_each_spray_cycle_entry = Entry(window, font=entry_font, justify="center")
number_of_valve_rinsing_cycles_entry = Entry(window, font=entry_font, justify="center")
drying_time_entry = Entry(window, font=entry_font, justify="center")
horizontal_spraying_entry = Entry(window, font=entry_font, justify="center")
filename_entry = Entry(window, font=entry_font, justify="center")
heat_bed_presence_yes = Radiobutton(window, text="Yes", variable=heat_bed_presence_entry, value="y", font=entry_font, justify="center")
heat_bed_presence_no = Radiobutton(window, text="No", variable=heat_bed_presence_entry, value="n", font=entry_font, justify="center")
heat_bed_height_entry = Entry(window, font=entry_font, justify="center")
heat_bed_temperature_entry = Entry(window, font=entry_font, justify="center")



########## Entry boxes / Radiobuttons (default values)
solution_to_use_entry.insert(0, "A")
waiting_phase_between_solutions_time_entry.insert(0,"5")
coordinates_of_spray_x_axis_entry.insert(0,"-30,30")
coordinates_of_spray_y_axis_entry.insert(0,"40,80")
height_of_the_needle_entry.insert(0,"60")
distance_between_lines_entry.insert(0,"5")
speed_of_movement_entry.insert(0,"150")
matrix_density_entry.insert(0,"1")
number_of_initial_wash_cycles_entry.insert(0,"5")
number_of_spray_cycles_entry.insert(0,"2")
interspray_wash_choice_entry.insert(0, "y")
additional_waiting_time_after_each_spray_cycle_entry.insert(0,"0")
number_of_valve_rinsing_cycles_entry.insert(0,"5")
drying_time_entry.insert(0,"8")
horizontal_spraying_entry.insert(0,"y")
filename_entry.insert(0,"iMatrixSpray method")
heat_bed_presence_yes.select()
heat_bed_presence_no.deselect()
heat_bed_height_entry.insert(0,"5")
heat_bed_temperature_entry.insert(0,"0")


########## Positioning
solution_to_use_entry.grid(row=1, column=1)
new_names_entry.grid(row=2, column=1)
waiting_phase_between_solutions_time_entry.grid(row=3, column=1)
coordinates_of_spray_x_axis_entry.grid(row=4, column=1)
coordinates_of_spray_y_axis_entry.grid(row=5, column=1)
height_of_the_needle_entry.grid(row=6, column=1)
distance_between_lines_entry.grid(row=7, column=1)
speed_of_movement_entry.grid(row=8, column=1)
matrix_density_entry.grid(row=9, column=1)
number_of_initial_wash_cycles_entry.grid(row=10, column=1)
number_of_spray_cycles_entry.grid(row=11, column=1)
interspray_wash_choice_entry.grid(row=12, column=3)
additional_waiting_time_after_each_spray_cycle_entry.grid(row=12, column=1)
number_of_valve_rinsing_cycles_entry.grid(row=13, column=1)
drying_time_entry.grid(row=14, column=1)
horizontal_spraying_entry.grid(row=15, column=1)
filename_entry.grid(row=16, column=1)
heat_bed_presence_yes.grid(row=8, column=3)
heat_bed_presence_no.grid(row=9, column=3)
heat_bed_height_entry.grid(row=10, column=3)
heat_bed_temperature_entry.grid(row=11, column=3)



########## Buttons (with positioning)
Button(window, text='Quit', font = button_font, command=close_program_function).grid(row=17, column=0)
# Dump the file
Button(window, text='Dump gcode file', font = button_font, command=dump_gcode_file_function).grid(row=17, column=2)
# Output folder
Button(window, text="Browse output folder", font = button_font, command=select_output_folder_function).grid(row=17, column=1)
# Info
Button(window, text="Information", relief = "raised", bitmap="info", command=show_info).grid(row=1, column=2)
# Guide
Button(window, text="Guide", relief = "raised", bitmap="question", command=show_guide).grid(row=1, column=3)
# Check for updates
Button(window, text="Check for updates", relief = "raised", command=check_for_updates_function).grid(row=2, column=2)

# Hold until quit
window.mainloop()
