#! python3

#################### iMatrixSpray Method Gcode Generator ####################

# Program version (Specified by the program writer!!!!)
program_version = "2017.03.01.1"
### GitHub URL where the R file is
github_url = "https://raw.githubusercontent.com/gmanuel89/iMatrixSpray/master/iMatrixSpray%20Method%20Gcode%20Generator.py"
### Name of the file when downloaded
script_file_name = "iMatrixSpray Method Gcode Generator.py"
# Change log
change_log = "1. Added the possibility to dump the CSV file with the parameter list\n2. New GUI\n3. The filename now has the date and time appended so it never overwrites the already dumped one."









############################## Load the required libraries (tkinter for the TCLTK GUI)
import tkinter, os, platform
#from tkinter import *
from tkinter import messagebox, Label, Button, Entry, Tk, filedialog, font, Radiobutton, StringVar








############################## Initialize the output_folder variable
output_folder = os.getcwd()
############################## Initialize the variable which says if the gcode file has been dumped (before dumping the parameter list file)
gcode_file_dumped = False
############################## Initialize the gcode method filename
method_gcode_file_name = "iMatrixSpray Method Gcode"












############################## CONSTANT VALUES
max_speed_of_movement = 200
max_matrix_density = 10
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

########## FUNCTION: Check for updates (from my GitHub page) (it just updates the label telling the user if there are updates) (it updates the check for updates value that is called by the label)
def check_for_updates_function():
    # Initialize the variable that displays the version number and the possible updates
    global check_for_updates_value, update_available, online_change_log
    check_for_updates_value = program_version
    # Initialize the version
    online_version_number = None
    # Initialize the variable that says if there are updates
    update_available = False
    ### Initialize the change log
    online_change_log = "Bug fixes"
    try:
        # Import the library
        import urllib.request
        # Retrieve the file from GitHub (read the lines: list with lines)
        github_file_lines = urllib.request.urlopen(github_url).readlines()
        # Decode the lines (from bytes to character)
        for l in range(len(github_file_lines)):
            github_file_lines[l] = github_file_lines[l].decode("utf-8")
        # Retrieve the version number
        for line in github_file_lines:
            if line.startswith("program_version = "):
                # Isolate the "variable" value
                online_version_number = line.split("program_version = ")[1]
                # Remove the quotes
                online_version_number = online_version_number.split("\"")[1]
        ### Retrieve the change log
        for line in github_file_lines:
            if line.startswith("change_log = "):
                # Isolate the "variable" value
                online_change_log = line.split("change_log = ")[1]
                # Remove the quotes
                online_change_log = online_change_log.split("\"")[1]
                # Split at the \n
                online_change_log_split = online_change_log.split("\\n")
                # Put it back to the character
                online_change_log = ""
                for o in online_change_log_split:
                    online_change_log = online_change_log + "\n" + o
        # Split the version number in YYYY.MM.DD
        online_version_YYYYMMDDVV = online_version_number.split(".")
        # Compare with the local version
        local_version_YYYYMMDDVV = program_version.split(".")
        ### Check the versions (from year to day)
        if local_version_YYYYMMDDVV[0] < online_version_YYYYMMDDVV[0]:
            update_available = True
        if update_available is False:
            if (local_version_YYYYMMDDVV[0] == online_version_YYYYMMDDVV[0]) and (local_version_YYYYMMDDVV[1] < online_version_YYYYMMDDVV[1]):
                update_available = True
        if update_available is False:
            if (local_version_YYYYMMDDVV[0] == online_version_YYYYMMDDVV[0]) and (local_version_YYYYMMDDVV[1] == online_version_YYYYMMDDVV[1]) and (local_version_YYYYMMDDVV[2] < online_version_YYYYMMDDVV[2]):
                update_available = True
        if update_available is False:
            if (local_version_YYYYMMDDVV[0] == online_version_YYYYMMDDVV[0]) and (local_version_YYYYMMDDVV[1] == online_version_YYYYMMDDVV[1]) and (local_version_YYYYMMDDVV[2] == online_version_YYYYMMDDVV[2]) and (local_version_YYYYMMDDVV[3] < online_version_YYYYMMDDVV[3]):
                update_available = True
        # Return messages
        if online_version_number is None:
            # The version number could not be ckecked due to internet problems
            check_for_updates_value = "Version: %s\nUpdates not checked: connection problems" %(program_version)
        else:
            if update_available is True:
                # The version number could not be ckecked due to internet problems
                check_for_updates_value = "Version: %s\nUpdates available: %s" %(program_version, online_version_number)
            else:
                check_for_updates_value = "Version: %s\nNo updates available" %(program_version)
    # Something went wrong: library not installed, retrieving failed, errors in parsing the version number
    except:
        # Return messages
        if online_version_number is None:
            # The version number could not be ckecked due to internet problems
            check_for_updates_value = "Version: %s\nUpdates not checked: connection problems" %(program_version)









########## FUNCTION: Download updates (from my GitHub page)
def download_updates_function():
    # Initialize the variable that displays the version number
    global check_for_updates_value
    # Download updates only if there are updates available
    if update_available is True:
        # Initialize the variable which says if the file has been downloaded successfully
        file_downloaded = False
        # Choose where to save the updated script
        Tk().withdraw()
        messagebox.showinfo(title="Download folder", message="Select where to save the updated script file")
        download_folder = filedialog.askdirectory ()
        # Fix the possible non-defined output folder
        if download_folder == "":
            download_folder = os.getcwd()
        # Just to confirm...
        Tk().withdraw()
        messagebox.showinfo(title="Folder selected", message="The updated iMatrix Gcode Method Generator file will be downloaded in:\n\n'%s'" %(download_folder))
        try:
            # Import the library
            import urllib.request
            # Download the new file in the working directory
            os.chdir(download_folder)
            urllib.request.urlretrieve (github_url, script_file_name)
            file_downloaded = True
        except:
            pass
        if file_downloaded is True:
            Tk().withdraw()
            messagebox.showinfo(title="Updated file retrieved!", message="The update file named\n%s\nhas been retrieved and placed in\n%s" %(script_file_name, download_folder))
            Tk().withdraw()
            messagebox.showinfo(title="Changelog", message="The updated script contains the following changes:\n%s" %(online_change_log))
        else:
            Tk().withdraw()
            messagebox.showinfo(title="Connection problem", message="The updated script file could not be downloaded due to internet connection problems!\n\nManually download the updated script file at:\n\n%s" %(github_url))
    else:
        check_for_updates_value = "Version: %s\nNo updates available" %(program_version)
        Tk().withdraw()
        messagebox.showinfo(title="No updates available", message="No updates available!")











########## FUNCTION: Select where to save the GCODE method file
def select_output_folder_function():
    Tk().withdraw()
    messagebox.showinfo(title="Folder selection", message="Select where to dump the gcode file(s)")
    # Where to save the GCODE file (escape function environment)
    global output_folder
    tkinter.Tk().withdraw()
    output_folder = filedialog.askdirectory ()
    # Fix the possible non-defined output folder
    if output_folder == "":
        output_folder = os.getcwd()
    # Just to confirm...
    Tk().withdraw()
    messagebox.showinfo(title="Folder selected", message="The gcode file(s) will be dumped in '%s'" %(output_folder))










########## FUNCTION: Dump the GCODE method file
def dump_gcode_file_function():
    # Escape the function
    global solution_to_use_letter, waiting_phase_between_solutions_time, coordinates_of_spray_x_axis, coordinates_of_spray_y_axis, heat_bed_presence, heat_bed_height, interspray_wash_choice, heat_bed_temperature, height_of_the_needle, distance_between_lines, speed_of_movement, matrix_density, number_of_initial_wash_cycles, number_of_spray_cycles, additional_waiting_time_after_each_spray_cycle, number_of_valve_rinsing_cycles, drying_time, horizontal_spraying, gcode_file_dumped





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
    coordinates_of_spray_x_axis_splitted = coordinates_of_spray_x_axis_input.split(",")
    coordinates_of_spray_y_axis_splitted = coordinates_of_spray_y_axis_input.split(",")
    # Strip off the spaces (it always returns a list)
    for i in range(len(coordinates_of_spray_x_axis_splitted)):
        coordinates_of_spray_x_axis_splitted[i] = coordinates_of_spray_x_axis_splitted[i].strip()
        # Strip off the spaces (it always returns a list)
    for i in range(len(coordinates_of_spray_y_axis_splitted)):
        coordinates_of_spray_y_axis_splitted[i] = coordinates_of_spray_y_axis_splitted[i].strip()
    ### X-axis
    coordinates_of_spray_x_axis = []
    for i in range(len(coordinates_of_spray_x_axis_splitted)):
        # If the i goes out of boundary (you use more solutions than the coordinates specified)
        # If specified
        if coordinates_of_spray_x_axis_splitted[i] != "":
            # Convert it into a list
            coordinates_of_spray_x_axis_splitted[i] = coordinates_of_spray_x_axis_splitted[i].split(":")
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
            coordinates_of_spray_y_axis_splitted[i] = coordinates_of_spray_y_axis_splitted[i].split(":")
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
            spra
