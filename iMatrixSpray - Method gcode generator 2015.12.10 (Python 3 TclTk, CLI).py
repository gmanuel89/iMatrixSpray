#! python3

########### iMatrixSpray generator 2015.12.10

######################################################################## GTK GUI (requires Tkinter)
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
########### Where to save the output file
tkinter.Tk().withdraw()
tkinter.messagebox.showinfo(title="File selection", message="Select where to save the gcode file")
# Where to save the GCODE file
tkinter.Tk().withdraw()
outputfile = tkinter.filedialog.asksaveasfilename (defaultextension='.gcode', filetypes=[('gcode files','.gcode')])
### Add the extension to the file automatically
if ".gcode" not in outputfile:
    outputfile = str(outputfile) + ".gcode"





########################################## INPUT VALUES (raw input)
### Solution to use (Vial valves: A=3, B=4, C=5, Rinse=2, Waste=0, Spray=1; when floating with .5 it always means that the valve links the selected vial to the waste, probably because .0 was not possible)
solution_to_use_input = input("Select the solution(s) to spray with (A,B,C or rinse) (default: A)\n")

# More letters...
try:
    solution_to_use = []
    solution_to_use_letter = []
    # Determine the character used for separating the values (comma, space, etc)
    separator_character = solution_to_use_input[1]
    # Split the string in as many letters as the solution
    # If there is a separator between letters...
    if (separator_character == " " or separator_character == "," or separator_character == "+" or separator_character == "-" or separator_character == "_"):
        solution_to_use_splitted = solution_to_use_input.split (separator_character)
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
    # If there aren't any separators between letters
    else:
        # Create a list of letters
        for letter in solution_to_use_input:
            if letter == "A" or letter == "a" or letter == 1:
                solution_to_use_letter.append(letter)
                solution_to_use.append(int(3))
            elif letter == "B" or letter == "b" or letter == 2:
                solution_to_use_letter.append(letter)
                solution_to_use.append(int(4))
            elif letter == "C" or letter == "c" or letter == 3:
                solution_to_use_letter.append(letter)
                solution_to_use.append(int(5))
            elif letter == "rinse":
                solution_to_use_letter.append(letter)
                solution_to_use.append(int(2))
            else:
                solution_to_use_letter.append(letter)
                solution_to_use.append(int(3))
# One letter...
except:
    if solution_to_use_input == "A" or solution_to_use_input == "a" or solution_to_use_input == 1:
        solution_to_use_letter = "A"
        solution_to_use = int(3)
    elif solution_to_use_input == "B" or solution_to_use_input == "b" or solution_to_use_input == 2:
        solution_to_use_letter = "B"
        solution_to_use = int(4)
    elif solution_to_use_input == "C" or solution_to_use_input == "c" or solution_to_use_input == 3:
        solution_to_use_letter = "C"
        solution_to_use = int(5)
    elif solution_to_use_input == "rinse":
        solution_to_use_letter = "rinse"
        solution_to_use = int(2)
    else:
        solution_to_use_letter = "A"
        solution_to_use = int(3)





### Rename the solutions
new_names = input("Rename the solution(s) to spray with (separate the labels by commas)(press enter to skip renaming)\n")

if new_names != "":
    # Generate the list of names
    solution_to_use_new = new_names.split(",")
    # Stripping
    for s in range(len(solution_to_use_new)):
        solution_to_use_new[s] = solution_to_use_new[s].strip()
    # Rename the solutions (only if there is a match with the solutions to use)
    if len(solution_to_use_new) == len(solution_to_use):
        solution_to_use_letter = solution_to_use_new
    # Mistake: the user inserted too few solutions
    elif len(solution_to_use_new) < len(solution_to_use):
        # Insert the renamed solution only if it's there, otherwise leave the default label
        for z in range(len(solution_to_use)):
            try:
                solution_to_use_letter[z] = solution_to_use_new[z]
            except:
                solution_to_use_letter[z] = solution_to_use_letter[z]
    # Mistake: the user inserted too many solutions
    elif len(solution_to_use_new) > len(solution_to_use):
        solution_to_use_letter = solution_to_use_letter
else:
    solution_to_use_letter = solution_to_use_letter





### Waiting time between two consecutive solutions
try:
    if len(solution_to_use) != 0:
        waiting_phase_between_solutions_time = []
        for i in (range(len(solution_to_use)-1)):
            try:
                waiting_phase_between_solutions_time_input = float(input("Set how many seconds the machine has to wait before switching from solution '%s' to solution '%s' (default: 5)\n" %(solution_to_use_letter[i],solution_to_use_letter[i+1])))
                waiting_phase_between_solutions_time.append(waiting_phase_between_solutions_time_input)
            except:
                waiting_phase_between_solutions_time.append(float(5))
except:
    waiting_phase_between_solutions_time = None





### X,Y coordinates (for each solution)
# It returns errors with only one solution to be used (it has no len property), so use try/except
try:
    coordinates_of_spray_x_axis_sol = []
    coordinates_of_spray_y_axis_sol = []
    for i in range(len(solution_to_use)):
        try:
            coordinates_of_spray_x_axis = input("Set the x-axis coordinates of spraying (default: -60,60) (solution '%s')\n[hint: Coordinates for the small area are (-30,30)]\n" %(solution_to_use_letter[i]))
            # Convert it into a list
            coordinates_of_spray_x_axis = coordinates_of_spray_x_axis.split(",")
            # From strings to floating point numbers
            for s in range(len(coordinates_of_spray_x_axis)):
                coordinates_of_spray_x_axis[s] = float(coordinates_of_spray_x_axis[s])
        except:
            coordinates_of_spray_x_axis = (float(-60), float(60))
        try:
            coordinates_of_spray_y_axis = input("Set the y-axis coordinates of spraying (default: -80,80) (solution '%s')\n[hint: Coordinates for the small area are (40,80)]\n" %(solution_to_use_letter[i]))
            # Convert it into a list
            coordinates_of_spray_y_axis = coordinates_of_spray_y_axis.split(",")
            # From strings to floating point numbers
            for s in range(len(coordinates_of_spray_y_axis)):
                coordinates_of_spray_y_axis[s] = float(coordinates_of_spray_y_axis[s])
        except:
            coordinates_of_spray_y_axis = (float(-80), float(80))
        # Attach this to the final list of coordinates
        coordinates_of_spray_x_axis_sol.append(coordinates_of_spray_x_axis)
        coordinates_of_spray_y_axis_sol.append(coordinates_of_spray_y_axis)
except:
    try:
        coordinates_of_spray_x_axis = input("Set the x-axis coordinates of spraying (default: -60,60) (solution '%s')\n[hint: Coordinates for the small area are (-30,30)]\n" %(solution_to_use_letter))
        # Convert it into a list
        coordinates_of_spray_x_axis = coordinates_of_spray_x_axis.split(",")
        # From strings to floating point numbers
        for s in range(len(coordinates_of_spray_x_axis)):
            coordinates_of_spray_x_axis[s] = float(coordinates_of_spray_x_axis[s])
    except:
        coordinates_of_spray_x_axis = (float(-60), float(60))
    try:
        coordinates_of_spray_y_axis = input ("Set the y-axis coordinates of spraying (default: -80,80) (solution '%s')\n[hint: Coordinates for the small area are (40,80)]\n" %(solution_to_use_letter))
        # Convert it into a list
        coordinates_of_spray_y_axis = coordinates_of_spray_y_axis.split(",")
        # From strings to floating point numbers
        for s in range(len(coordinates_of_spray_y_axis)):
            coordinates_of_spray_y_axis[s] = float(coordinates_of_spray_y_axis[s])
    except:
        coordinates_of_spray_y_axis = (float(-80), float(80))





### Height of the needle
try:
    height_of_the_needle = []
    for i in range(len(solution_to_use)):
        try:
            height_of_the_needle_input = float(input ("Set the height of the needle (default: 60) (solution '%s')\n" %(solution_to_use_letter[i])))
            height_of_the_needle.append(height_of_the_needle_input)
        except:
            height_of_the_needle.append(float(60))
except:
    try:
        height_of_the_needle = float(input ("Set the height of the needle (default: 60) (solution '%s')\n" %(solution_to_use_letter)))
    except:
        height_of_the_needle = float(60)





### Distance between spray lines
try:
    distance_between_lines = []
    for i in range(len(solution_to_use)):
        try:
            distance_between_lines_input = float (input ("Set the distance between lines when spraying (default: 5) (solution '%s')\n" %(solution_to_use_letter[i])))
            distance_between_lines.append(distance_between_lines_input)
        except:
            distance_between_lines.append(float(5))
except:
    try:
        distance_between_lines = float (input ("Set the distance between lines when spraying (default: 5) (solution '%s')\n" %solution_to_use_letter))
    except:
        distance_between_lines = float(5)





### Speed of movement
try:
    speed_of_movement = []
    for i in range(len(solution_to_use)):
        try:
            speed_of_movement_input = float (input ("Set the speed of movement (max: 200, default: 150) (solution '%s')\n" %(solution_to_use_letter[i])))
            speed_of_movement.append(speed_of_movement_input)
        except:
            speed_of_movement.append(float(150))
except:
    try:
        speed_of_movement = float (input ("Set the speed of movement (max: 200, default: 150) (solution '%s')\n" %solution_to_use_letter))
    except:
        speed_of_movement = float(150)





### Matrix density
try:
    matrix_density = []
    for i in range(len(solution_to_use)):
        try:
            matrix_density_input = float (input ("Set the density of the matrix on-tissue (in microlitres per squared centimeter) (max: 5, default: 1) (solution '%s')\n" %(solution_to_use_letter[i])))
            matrix_density.append(matrix_density_input)
        except:
            matrix_density.append(float(1))
except:
    try:
        matrix_density = float (input ("Set the density of the matrix on-tissue (in microlitres per squared centimeter) (max: 5, default: 1) (solution '%s')\n" %solution_to_use_letter))
    except:
        matrix_density = float(1)





### Number of initial wash cycles
try:
    number_of_initial_wash_cycles = []
    for i in range(len(solution_to_use)):
        try:
            number_of_initial_wash_cycles_input = int (input ("Set the number of initial wash cycles with solution '%s' (default: 5)\n" %(solution_to_use_letter[i])))
            number_of_initial_wash_cycles.append(number_of_initial_wash_cycles_input)
        except:
            number_of_initial_wash_cycles.append(5)
except:
    try:
        number_of_initial_wash_cycles = int (input ("Set the number of initial wash cycles with solution '%s' (default: 5)\n" %solution_to_use_letter))
    except:
        number_of_initial_wash_cycles = 5





### Number of spray cycles
try:
    number_of_spray_cycles = []
    for i in range(len(solution_to_use)):
        try:
            number_of_spray_cycles_input = int (input ("Set the number of spraying cycles (default:2) (solution '%s')\n" %(solution_to_use_letter[i])))
            number_of_spray_cycles.append(number_of_spray_cycles_input)
        except:
            number_of_spray_cycles.append(2)
except:
    try:
        number_of_spray_cycles = int (input ("Set the number of spraying cycles (default:2) (solution '%s')\n" %solution_to_use_letter))
    except:
        number_of_spray_cycles = 2





### Additional time to wait after each spray cycle
try:
    additional_waiting_time_after_each_spray_cycle = []
    for i in range(len(solution_to_use)):
        try:
            additional_waiting_time_after_each_spray_cycle_input = float (input ("Set the additional time (in seconds) to wait after each spraying cycle (default:0) (solution '%s')\n" %(solution_to_use_letter[i])))
            additional_waiting_time_after_each_spray_cycle.append(additional_waiting_time_after_each_spray_cycle_input)
        except:
            additional_waiting_time_after_each_spray_cycle.append(float(0))
except:
    try:
        additional_waiting_time_after_each_spray_cycle = float (input ("Set the additional time (in seconds) to wait after each spraying cycle (default:0) (solution '%s')\n" %solution_to_use_letter))
    except:
        additional_waiting_time_after_each_spray_cycle = float(0)





### Number of valve rinsing cycles
try:
    number_of_valve_rinsing_cycles = []
    for i in range(len(solution_to_use)):
        try:
            number_of_valve_rinsing_cycles_input = int (input ("Set the number of valve rinsing cycles with the rinsing solution (default: 5) (for solution '%s')\n" %(solution_to_use_letter[i])))
            number_of_valve_rinsing_cycles.append(number_of_valve_rinsing_cycles_input)
        except:
            number_of_valve_rinsing_cycles.append(5)
except:
    try:
        number_of_valve_rinsing_cycles = int (input ("Set the number of valve rinsing cycles with the rinsing solution (default: 5) (for solution '%s')\n" %solution_to_use_letter))
    except:
        number_of_valve_rinsing_cycles = 5





### Set the drying time
try:
    drying_time = float(input ("Set the drying time for the needle after rinsing (default: 8) (for all the solutions: '%s')\n" %(solution_to_use_letter)))
except:
    drying_time = float(8)





### Horizontal spraying
try:
    horizontal_spraying = []
    for i in range(len(solution_to_use)):
        horizontal_spraying_input = input("Spray horizontally? (y or n, default: y) (solution '%s')\n" %(solution_to_use_letter[i]))
        horizontal_spraying.append(horizontal_spraying_input)
except:
    horizontal_spraying = input("Spray horizontally? (y or n, default: y) (solution '%s')\n" %solution_to_use_letter)





####################################### Constant values
try:
    coordinates_of_spray_z_axis = []
    for h in height_of_the_needle:
        coordinates_of_spray_z_axis.append(float(-104 + abs(h))) # Calculated
except:
    coordinates_of_spray_z_axis = float(-104 + abs(height_of_the_needle)) # Calculated

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





################################################# Avoid that the machine breaks
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
try:
    for c in range(len(coordinates_of_spray_x_axis_sol)):
        if coordinates_of_spray_x_axis_sol[c][0] < max_x_coordinates[0]:
            coordinates_of_spray_x_axis_sol[c][0] = max_x_coordinates[0]
        if coordinates_of_spray_x_axis_sol[c][1] > max_x_coordinates[1]:
            coordinates_of_spray_x_axis_sol[c][1] = max_x_coordinates[1]
    for c in range(len(coordinates_of_spray_y_axis_sol)):
        if coordinates_of_spray_y_axis_sol[c][0] < max_y_coordinates[0]:
            coordinates_of_spray_y_axis_sol[c][0] = max_y_coordinates[0]
        if coordinates_of_spray_y_axis_sol[c][1] > max_y_coordinates[1]:
            coordinates_of_spray_y_axis_sol[c][1] = max_y_coordinates[1]
except:
    if coordinates_of_spray_x_axis[0] < max_x_coordinates[0]:
        coordinates_of_spray_x_axis[0] = max_x_coordinates[0]
    if coordinates_of_spray_x_axis[1] > max_x_coordinates[1]:
        coordinates_of_spray_x_axis[1] = max_x_coordinates[1]
    if coordinates_of_spray_y_axis[0] < max_y_coordinates[0]:
        coordinates_of_spray_y_axis[0] = max_y_coordinates[0]
    if coordinates_of_spray_y_axis[1] > max_y_coordinates[1]:
        coordinates_of_spray_y_axis[1] = max_y_coordinates[1]










################################################################################
################################################################### CODE BLOCKS

########################################################### Go to wash position (same for all)
go_to_wash_position = [";;;;; go to wash position\n"]
go_to_wash_position_subblock = ["G1 Z%s F%s\n" %(float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 X%s Y%s Z%s F%s\n" %(float(coordinates_of_washing_x_axis), float(coordinates_of_washing_y_axis), float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 Z%s\n" %float(coordinates_of_washing_z_axis)]
# Generate the definitive block
for s in go_to_wash_position_subblock:
    go_to_wash_position.append (s)

# Leave a white line between blocks
go_to_wash_position.append ("\n")





########################################################## Additional waiting  time after spraying (solution dependent)
try:
    additional_waiting_time_after_spraying = []
    for sol in range(len(solution_to_use)):
        additional_waiting_time_after_spraying.append(["G1 Z%s F%s\n" %(float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 X%s Y%s Z%s F%s\n" %(float(coordinates_of_washing_x_axis), float(coordinates_of_washing_y_axis), float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 Z%s\n" %float(coordinates_of_washing_z_axis), "G4 S%s\n" %(additional_waiting_time_after_each_spray_cycle[sol])])
except:
    additional_waiting_time_after_spraying = ["G1 Z%s F%s\n" %(float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 X%s Y%s Z%s F%s\n" %(float(coordinates_of_washing_x_axis), float(coordinates_of_washing_y_axis), float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 Z%s\n" %float(coordinates_of_washing_z_axis), "G4 S%s\n" %(additional_waiting_time_after_each_spray_cycle)]





###################################################### Waiting time before two different solutions
try:
    waiting_phase_between_solutions_block_sol = []
    for sol in range(len(solution_to_use)-1):
        waiting_phase_between_solutions_block = [";;;;;;;;;; waiting phase before switching between solutions\nG4 S%s\n\n" %waiting_phase_between_solutions_time[sol]]
        waiting_phase_between_solutions_block_sol.append(waiting_phase_between_solutions_block)
except:
    waiting_phase_between_solutions_block = None





########################################################## Initialisation block (same for all)
initialisation_block = [";;;;;;;;;; initialisation\n"]
initialisation_subblock = ["G28XYZ\n", "G28P\n", "G90\n"]
# Generate the definitive block
for s in initialisation_subblock:
    initialisation_block.append (s)

# Leave a white line between blocks
initialisation_block.append ("\n")





############################################################## First wash block (solution dependent)
try:
    first_wash_block_sol = []
    for sol in range(len(solution_to_use)):
        first_wash_block = [";;;;;;;;;; first wash\n"]
        # Go to wash position first
        for s in go_to_wash_position:
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
    for s in go_to_wash_position:
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





################################################################### Spray block (solution dependent)
try:
    spray_block_sol = []
    for sol in range(len(solution_to_use)):
        # First part of the block
        spray_block = [";;;;;;;;;; spraying phase\n"]
        ################### The X-axis stays fixed
        if horizontal_spraying[sol] == True:
            ################# Generate the vector of x and y positions
            ###### Y positions
            y_positions = []
            ### Calculate the number of Y positions (according to the y length and the distance between lines) (since the path is an S, each y coordinate is reported twice, so the number of positions must be doubled)
            # One is negative and the other positive
            if coordinates_of_spray_y_axis_sol[sol][0] < 0 and coordinates_of_spray_y_axis_sol[sol][1] >= 0:
                number_of_y_positions = abs(int((coordinates_of_spray_y_axis_sol[sol][1] - coordinates_of_spray_y_axis_sol[sol][0]) / distance_between_lines[sol]) * 2)
                number_of_lines = abs(int((coordinates_of_spray_y_axis_sol[sol][1] - coordinates_of_spray_y_axis_sol[sol][0]) / distance_between_lines[sol]))
                y_line_length = coordinates_of_spray_y_axis_sol[sol][1] - coordinates_of_spray_y_axis_sol[sol][0]
            # Both are positive
            if coordinates_of_spray_y_axis_sol[sol][0] >= 0 and coordinates_of_spray_y_axis_sol[sol][1] > 0:
                number_of_y_positions = abs(int((coordinates_of_spray_y_axis_sol[sol][1] - coordinates_of_spray_y_axis_sol[sol][0]) / distance_between_lines[sol]) * 2)
                number_of_lines = abs(int((coordinates_of_spray_y_axis_sol[sol][1] - coordinates_of_spray_y_axis_sol[sol][0]) / distance_between_lines[sol]))
                y_line_length = coordinates_of_spray_y_axis_sol[sol][1] - coordinates_of_spray_y_axis_sol[sol][0]
            # Both are negative
            if coordinates_of_spray_y_axis_sol[sol][0] < 0 and coordinates_of_spray_y_axis_sol[sol][1] <= 0:
                number_of_y_positions = abs(int((abs(coordinates_of_spray_y_axis_sol[sol][0]) - abs(coordinates_of_spray_y_axis_sol[sol][1])) / distance_between_lines[sol]) * 2)
                number_of_lines = abs(int((abs(coordinates_of_spray_y_axis_sol[sol][0]) - abs(coordinates_of_spray_y_axis_sol[sol][1])) / distance_between_lines[sol]))
                y_line_length = abs(coordinates_of_spray_y_axis_sol[sol][0]) - abs(coordinates_of_spray_y_axis_sol[sol][1])
            ### Calculate the spray travel on X
            # One is negative and the other positive
            if coordinates_of_spray_x_axis_sol[sol][0] < 0 and coordinates_of_spray_x_axis_sol[sol][1] >= 0:
                x_line_length = coordinates_of_spray_x_axis_sol[sol][1] - coordinates_of_spray_x_axis_sol[sol][0]
            # Both are positive
            if coordinates_of_spray_x_axis_sol[sol][0] >= 0 and coordinates_of_spray_x_axis_sol[sol][1] > 0:
                x_line_length = coordinates_of_spray_x_axis_sol[sol][1] - coordinates_of_spray_x_axis_sol[sol][0]
            # Both are negative
            if coordinates_of_spray_x_axis_sol[sol][0] < 0 and coordinates_of_spray_x_axis_sol[sol][1] <= 0:
                x_line_length = abs(coordinates_of_spray_x_axis_sol[sol][0]) - abs(coordinates_of_spray_x_axis_sol[sol][1])
            ### Calculate the spray travel distance
            spray_travel = number_of_lines * x_line_length + y_line_length
            ### Calculate the spray time
            spray_time = spray_travel / speed_of_movement[sol]
            ### Calculate the spray density
            spray_density = float(matrix_density[sol]) / 100 * distance_between_lines[sol]
            ### Calculate the spray syringe volume
            spray_syringe_volume = spray_travel * spray_density
            ### Calculate the spray syringe travel
            spray_syringe_travel = spray_syringe_volume / spray_syringe_volume_per_travel
            ### Spray syringe volume in X
            spray_syringe_x = x_line_length * spray_density / spray_syringe_volume_per_travel
            ### Spray syringe volume in Y
            spray_syringe_y = distance_between_lines[sol] * spray_density / spray_syringe_volume_per_travel
            # Calculate the other positions (since the path is an S, each y coordinate is reported twice)
            for i in range(number_of_y_positions-1):
                # The first position is where to start spraying (since the path is an S, each y coordinate is reported twice)
                if len(y_positions) == 0:
                    y_positions.append (float(coordinates_of_spray_y_axis_sol[sol][0]))
                    y_positions.append (float(coordinates_of_spray_y_axis_sol[sol][0]))
                else:
                    y_positions.append (float(y_positions[i-1] + distance_between_lines[sol]))
            ###### X positions
            x_positions = []
            # Calculate the other positions (since the path is an S, each x coordinate is reported twice)
            for i in range(number_of_y_positions):
                # The first position and the last position are on the opposite side of the starting position (where to go spraying, along the x axis) (since the path is an S, each y coordinate is reported twice)
                if len(x_positions) == 0:
                    x_positions.append(float(coordinates_of_spray_x_axis_sol[sol][1]))
                elif len(x_positions) == 1:
                    x_positions.append(float(coordinates_of_spray_x_axis_sol[sol][0]))
                elif x_positions[i-1] != x_positions[i-2]:
                    x_positions.append(x_positions[i-1])
                elif x_positions[i-1] == x_positions[i-2]:
                    x_positions.append(x_positions[i-3])
            ###### Values of P
            p_values = []
            for i in range(int(number_of_y_positions/2)):
                p_values.append (float(-spray_syringe_y))
                p_values.append (float(-spray_syringe_x))
            ###### Generate the final spray ssubblock
            spray_subblock2 = [";;; spray\n"]
            for i in range(number_of_y_positions):
                # Create the line and append it to the list of the block lines
                line = "G1 X%s Y%s P%s F%s\n" %(x_positions[i], y_positions[i], p_values[i], speed_of_movement[sol])
                spray_subblock2.append (line)
            spray_subblock2.append ("G1 Y%s Z%s F%s\n" %(float(coordinates_of_spray_y_axis_sol[sol][0]), float(coordinates_of_z_axis_during_movement), max_speed_of_movement))
            # Generate the first part of the block
            spray_subblock1 = ["M106\n", "M82\n", "G1 V%s F%s\n" %(solution_to_use[sol], max_speed_of_movement), "G4 S1\n", "G1 P%s F%s\n" %(spray_syringe_travel+2, max_speed_of_movement), "G1 V1 F%s\n" %(max_speed_of_movement), "G4 S1\n", "G1 F0.1\n", "G1 P%s\n" %(spray_syringe_travel), "\n", ";;; where to start spraying\n", "G1 Z%s F%s\n" %(float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 X%s Y%s F%s\n" %(float(coordinates_of_spray_x_axis_sol[sol][0]), float(coordinates_of_spray_y_axis_sol[sol][0]), max_speed_of_movement), "G1 Z%s F%s\n" %(float(coordinates_of_spray_z_axis[sol]), max_speed_of_movement), "\n", "M83\n", "\n"]
            # Attach the spray sub-block to the global spray block
            for s in spray_subblock1:
                spray_block.append(s)
            for s in spray_subblock2:
                spray_block.append(s)
            # Add additional waiting phase
            for s in additional_waiting_time_after_spraying[sol]:
                spray_block.append(s)
        ######################################### The Y-axis stays fixed
        else:
            ################# Generate the vector of x and y positions
            ###### X positions
            x_positions = []
            ### Calculate the number of X positions (according to the x length and the distance between lines) (since the path is an S, each x coordinate is reported twice, so the number of positions must be doubled)
            # One is negative and the other positive
            if coordinates_of_spray_x_axis_sol[sol][0] < 0 and coordinates_of_spray_x_axis_sol[sol][1] >= 0:
                number_of_x_positions = abs(int((coordinates_of_spray_x_axis_sol[sol][1] - coordinates_of_spray_x_axis_sol[sol][0]) / distance_between_lines[sol]) * 2)
                number_of_lines = abs(int((coordinates_of_spray_x_axis_sol[sol][1] - coordinates_of_spray_x_axis_sol[sol][0]) / distance_between_lines[sol]))
                x_line_length = coordinates_of_spray_x_axis_sol[sol][1] - coordinates_of_spray_x_axis_sol[sol][0]
            # Both are positive
            if coordinates_of_spray_x_axis_sol[sol][0] >= 0 and coordinates_of_spray_x_axis_sol[sol][1] > 0:
                number_of_x_positions = abs(int((coordinates_of_spray_x_axis_sol[sol][1] - coordinates_of_spray_x_axis_sol[sol][0]) / distance_between_lines[sol]) * 2)
                number_of_lines = abs(int((coordinates_of_spray_x_axis_sol[sol][1] - coordinates_of_spray_x_axis_sol[sol][0]) / distance_between_lines[sol]))
                x_line_length = coordinates_of_spray_x_axis_sol[sol][1] - coordinates_of_spray_x_axis_sol[sol][0]
            # Both are negative
            if coordinates_of_spray_x_axis_sol[sol][0] < 0 and coordinates_of_spray_x_axis_sol[sol][1] <= 0:
                number_of_x_positions = abs(int((abs(coordinates_of_spray_x_axis_sol[sol][0]) - abs(coordinates_of_spray_x_axis_sol[sol][1])) / distance_between_lines[sol]) * 2)
                number_of_lines = abs(int((abs(coordinates_of_spray_x_axis_sol[sol][0]) - abs(coordinates_of_spray_x_axis_sol[sol][1])) / distance_between_lines[sol]))
                x_line_length = abs(coordinates_of_spray_x_axis_sol[sol][0]) - abs(coordinates_of_spray_x_axis_sol[sol][1])
            ### Calculate the spray travel on Y
            # One is negative and the other positive
            if coordinates_of_spray_y_axis_sol[sol][0] < 0 and coordinates_of_spray_y_axis_sol[sol][1] >= 0:
                y_line_length = coordinates_of_spray_y_axis_sol[sol][1] - coordinates_of_spray_y_axis_sol[sol][0]
            # Both are positive
            if coordinates_of_spray_y_axis_sol[sol][0] >= 0 and coordinates_of_spray_y_axis_sol[sol][1] > 0:
                y_line_length = coordinates_of_spray_y_axis_sol[sol][1] - coordinates_of_spray_y_axis_sol[sol][0]
            # Both are negative
            if coordinates_of_spray_y_axis_sol[sol][0] < 0 and coordinates_of_spray_y_axis_sol[sol][1] <= 0:
                y_line_length = abs(coordinates_of_spray_y_axis_sol[sol][0]) - abs(coordinates_of_spray_y_axis_sol[sol][1])
            ### Calculate the spray travel distance
            spray_travel = number_of_lines * y_line_length + x_line_length
            ### Calculate the spray time
            spray_time = spray_travel / speed_of_movement[sol]
            ### Calculate the spray density
            spray_density = float(matrix_density[sol]) / 100 * distance_between_lines[sol]
            ### Calculate the spray syringe volume
            spray_syringe_volume = spray_travel * spray_density
            ### Calculate the spray syringe travel
            spray_syringe_travel = spray_syringe_volume / spray_syringe_volume_per_travel
            ### Spray syringe volume in X
            spray_syringe_y = y_line_length * spray_density / spray_syringe_volume_per_travel
            ### Spray syringe volume in Y
            spray_syringe_x = distance_between_lines[sol] * spray_density / spray_syringe_volume_per_travel
            # Calculate the other positions (since the path is an S, each y coordinate is reported twice)
            for i in range(number_of_x_positions-1):
                # The first position is where to start spraying (since the path is an S, each y coordinate is reported twice)
                if len(x_positions) == 0:
                    x_positions.append (float(coordinates_of_spray_x_axis_sol[sol][0]))
                    x_positions.append (float(coordinates_of_spray_x_axis_sol[sol][0]))
                else:
                    x_positions.append (float(x_positions[i-1] + distance_between_lines[sol]))
            ###### X positions
            y_positions = []
            # Calculate the other positions (since the path is an S, each x coordinate is reported twice)
            for i in range(number_of_x_positions):
                # The first position and the last position are on the opposite side of the starting position (where to go spraying, along the x axis) (since the path is an S, each y coordinate is reported twice)
                if len(y_positions) == 0:
                    y_positions.append(float(coordinates_of_spray_y_axis_sol[sol][1]))
                elif len(y_positions) == 1:
                    y_positions.append(float(coordinates_of_spray_y_axis_sol[sol][0]))
                elif y_positions[i-1] != y_positions[i-2]:
                    y_positions.append(y_positions[i-1])
                elif y_positions[i-1] == y_positions[i-2]:
                    y_positions.append(y_positions[i-3])
            ###### Values of P
            p_values = []
            for i in range(int(number_of_x_positions/2)):
                p_values.append (float(-spray_syringe_x))
                p_values.append (float(-spray_syringe_y))
            ###### Generate the final spray ssubblock
            spray_subblock2 = [";;; spray\n"]
            for i in range(number_of_x_positions):
                # Create the line and append it to the list of the block lines
                line = "G1 X%s Y%s P%s F%s\n" %(x_positions[i], y_positions[i], p_values[i], speed_of_movement[sol])
                spray_subblock2.append (line)
            spray_subblock2.append ("G1 Y%s Z%s F%s\n" %(float(coordinates_of_spray_y_axis_sol[sol][0]), float(coordinates_of_z_axis_during_movement), max_speed_of_movement))
            # Generate the first part of the block
            spray_subblock1 = ["M106\n", "M82\n", "G1 V%s F%s\n" %(solution_to_use[sol], max_speed_of_movement), "G4 S1\n", "G1 P%s F%s\n" %(spray_syringe_travel+2, max_speed_of_movement), "G1 V1 F%s\n" %(max_speed_of_movement), "G4 S1\n", "G1 F0.1\n", "G1 P%s\n" %(spray_syringe_travel), "\n", ";;; where to start spraying\n", "G1 Z%s F%s\n" %(float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 X%s Y%s F%s\n" %(float(coordinates_of_spray_x_axis_sol[sol][0]), float(coordinates_of_spray_y_axis_sol[sol][0]), max_speed_of_movement), "G1 Z%s F%s\n" %(float(coordinates_of_spray_z_axis[sol]), max_speed_of_movement), "\n", "M83\n", "\n"]
            # Attach the spray sub-block to the global spray block
            for s in spray_subblock1:
                spray_block.append(s)
            for s in spray_subblock2:
                spray_block.append(s)
            # Add additional waiting phase
            for s in additional_waiting_time_after_spraying[sol]:
                spray_block.append(s)
        # Leave a white line between blocks
        spray_block.append ("\n")
        # Add this chunk to the final block
        spray_block_sol.append(spray_block)
except:
    # First part of the block
    spray_block = [";;;;;;;;;; spraying phase\n"]
    ################### The X-axis stays fixed
    if horizontal_spraying == True:
        ################# Generate the vector of x and y positions
        ###### Y positions
        y_positions = []
        ### Calculate the number of Y positions (according to the y length and the distance between lines) (since the path is an S, each y coordinate is reported twice, so the number of positions must be doubled)
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
        ### Calculate the spray travel on X
        # One is negative and the other positive
        if coordinates_of_spray_x_axis[0] < 0 and coordinates_of_spray_x_axis[1] >= 0:
            x_line_length = coordinates_of_spray_x_axis[1] - coordinates_of_spray_x_axis[0]
        # Both are positive
        if coordinates_of_spray_x_axis[0] >= 0 and coordinates_of_spray_x_axis[1] > 0:
            x_line_length = coordinates_of_spray_x_axis[1] - coordinates_of_spray_x_axis[0]
        # Both are negative
        if coordinates_of_spray_x_axis[0] < 0 and coordinates_of_spray_x_axis[1] <= 0:
            x_line_length = abs(coordinates_of_spray_x_axis[0]) - abs(coordinates_of_spray_x_axis[1])
        ### Calculate the spray travel distance
        spray_travel = number_of_lines * x_line_length + y_line_length
        ### Calculate the spray time
        spray_time = spray_travel / speed_of_movement
        ### Calculate the spray density
        spray_density = float(matrix_density) / 100 * distance_between_lines
        ### Calculate the spray syringe volume
        spray_syringe_volume = spray_travel * spray_density
        ### Calculate the spray syringe travel
        spray_syringe_travel = spray_syringe_volume / spray_syringe_volume_per_travel
        ### Spray syringe volume in X
        spray_syringe_x = x_line_length * spray_density / spray_syringe_volume_per_travel
        ### Spray syringe volume in Y
        spray_syringe_y = distance_between_lines * spray_density / spray_syringe_volume_per_travel
        # Calculate the other positions (since the path is an S, each y coordinate is reported twice)
        for i in range(number_of_y_positions-1):
            # The first position is where to start spraying (since the path is an S, each y coordinate is reported twice)
            if len(y_positions) == 0:
                y_positions.append (float(coordinates_of_spray_y_axis[0]))
                y_positions.append (float(coordinates_of_spray_y_axis[0]))
            else:
                y_positions.append (float(y_positions[i-1] + distance_between_lines))
        ###### X positions
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
        ###### Values of P
        p_values = []
        for i in range(int(number_of_y_positions/2)):
            p_values.append (float(-spray_syringe_y))
            p_values.append (float(-spray_syringe_x))
        ###### Generate the final spray ssubblock
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
        # Add additional waiting phase
        for s in additional_waiting_time_after_spraying:
            spray_block.append(s)
    ######################################### The Y-axis stays fixed
    else:
        ################# Generate the vector of x and y positions
        ###### X positions
        x_positions = []
        ### Calculate the number of X positions (according to the x length and the distance between lines) (since the path is an S, each x coordinate is reported twice, so the number of positions must be doubled)
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
        ### Calculate the spray travel on Y
        # One is negative and the other positive
        if coordinates_of_spray_y_axis[0] < 0 and coordinates_of_spray_y_axis[1] >= 0:
            y_line_length = coordinates_of_spray_y_axis[1] - coordinates_of_spray_y_axis[0]
        # Both are positive
        if coordinates_of_spray_y_axis[0] >= 0 and coordinates_of_spray_y_axis[1] > 0:
            y_line_length = coordinates_of_spray_y_axis[1] - coordinates_of_spray_y_axis[0]
        # Both are negative
        if coordinates_of_spray_y_axis[0] < 0 and coordinates_of_spray_y_axis[1] <= 0:
            y_line_length = abs(coordinates_of_spray_y_axis[0]) - abs(coordinates_of_spray_y_axis[1])
        ### Calculate the spray travel distance
        spray_travel = number_of_lines * y_line_length + x_line_length
        ### Calculate the spray time
        spray_time = spray_travel / speed_of_movement
        ### Calculate the spray density
        spray_density = float(matrix_density) / 100 * distance_between_lines
        ### Calculate the spray syringe volume
        spray_syringe_volume = spray_travel * spray_density
        ### Calculate the spray syringe travel
        spray_syringe_travel = spray_syringe_volume / spray_syringe_volume_per_travel
        ### Spray syringe volume in X
        spray_syringe_y = y_line_length * spray_density / spray_syringe_volume_per_travel
        ### Spray syringe volume in Y
        spray_syringe_x = distance_between_lines * spray_density / spray_syringe_volume_per_travel
        # Calculate the other positions (since the path is an S, each y coordinate is reported twice)
        for i in range(number_of_x_positions-1):
            # The first position is where to start spraying (since the path is an S, each y coordinate is reported twice)
            if len(x_positions) == 0:
                x_positions.append (float(coordinates_of_spray_x_axis[0]))
                x_positions.append (float(coordinates_of_spray_x_axis[0]))
            else:
                x_positions.append (float(x_positions[i-1] + distance_between_lines))
        ###### X positions
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
        ###### Values of P
        p_values = []
        for i in range(int(number_of_x_positions/2)):
            p_values.append (float(-spray_syringe_x))
            p_values.append (float(-spray_syringe_y))
        ###### Generate the final spray ssubblock
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
        # Add additional waiting phase
        for s in additional_waiting_time_after_spraying:
            spray_block.append(s)
    # Leave a white line between blocks
    spray_block.append ("\n")



######################################################## Inter-spray wash block (same for all)
### This actually depends on the solution to be used, since the rinsing is made with the solution to be used, but there is no code specifying the solution, since this phase occurs after the spraying, so the valve is already in position
interspray_wash_block = [";;;;;;;;;; interspray wash\n"]
# Go to wash position first
for s in go_to_wash_position:
    interspray_wash_block.append (s)

# Washing sub-block
interspray_wash_subblock = [";;;;; wash\n", "M82\n", "G1 V0 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 P0 F%s\n" %max_speed_of_movement, "M106 S0\n", "G4 S0.0\n"]
# Generate the definitive block
for s in interspray_wash_subblock:
    interspray_wash_block.append (s)

# Leave a white line between blocks
interspray_wash_block.append ("\n")





######################################################## Syringe emptying block (solution dependent)
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





########################################################### Spray rinsing block (same for all)
spray_rinsing_block = [";;;;; spray rinsing\n"]
spray_rinsing_subblock = ["G1 V1.5 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 P4 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 V2 F%s\n" %max_speed_of_movement, "G4 S2\n", "G1 V1 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 F0.1\n", "G1 P0\n", "M106 S0\n"]
# Generate the definitive block
for s in spray_rinsing_subblock:
    spray_rinsing_block.append (s)

# Leave a white line between blocks
spray_rinsing_block.append ("\n")





####################################################### Capillary rinsing block (same for all)
capillary_rinsing_block = [";;;;; capillary rinsing\n"]
capillary_rinsing_subblock = ["G1 V1.5 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 P3 F%s\n" %max_speed_of_movement, "G1 V2 F%s\n" %max_speed_of_movement, "G4 S2\n", "G1 V1 F%s\n" %max_speed_of_movement, "G4 S1\n", "G1 F0.1\n", "G1 P0\n", "G1 P1\n"]
# Generate the definitive block
for s in capillary_rinsing_subblock:
    capillary_rinsing_block.append (s)

# Leave a white line between blocks
capillary_rinsing_block.append ("\n")





################################################################## Drying block (same for all)
drying_block = [";;;;; drying\n"]
drying_subblock = ["M106\n", "G1 P0\n", "G4 S%s\n" %drying_time, "M106 S0\n"]
# Generate the definitive block
for s in drying_subblock:
    drying_block.append (s)

# Leave a white line between blocks
drying_block.append ("\n")





########################################################### Parking spray block (same for all)
parking_spray_block = [";;;;; parking spray\n"]
parking_spray_subblock = ["G1 Z%s F%s\n" %(float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 X%s Y%s Z%s F%s\n" %(float(initial_x_coordinates), float(initial_y_coordinates), float(coordinates_of_z_axis_during_movement), max_speed_of_movement), "G1 Z%s F%s\n" %(float(coordinates_of_z_rest), max_speed_of_movement)]
# Generate the definitive block
for s in parking_spray_subblock:
    parking_spray_block.append (s)

# Leave a white line between blocks
parking_spray_block.append ("\n")





############################################################ Cleaning procedure (solution dependent)
########### Go to wash + emptying syringe + rinsing valve + rinsing spray + rinsing capillary + drying + parking spray
try:
    cleaning_procedure_block_sol = []
    for sol in range(len(solution_to_use)):
        cleaning_procedure_block = [";;;;;;;;;; cleaning procedure\n"]
        cleaning_procedure_subblock = ["M82\n", "G90\n"]
        # Generate the definitive block
        for s in cleaning_procedure_subblock:
            cleaning_procedure_block.append(s)
        # Go to wash
        for s in go_to_wash_position:
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
    for s in go_to_wash_position:
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





############################################################## Motors off block (same for all)
motors_off_block = [";;;;;;;;;; motors off\n", "M18\n"]
# Leave a white line between blocks
motors_off_block.append ("\n")










################################################ Write lines in the output file
with open(outputfile, "w") as f:
    # Initialisation block
    for line in initialisation_block:
        f.writelines(line)
    try:
    #### Solution dependent blocks
        for sol in range(len(solution_to_use)):
            # First wash block
            for line in first_wash_block_sol[sol]:
                f.writelines(line)
            # Spray
            for i in range(number_of_spray_cycles[sol]):
                for line in spray_block_sol[sol]:
                    f.writelines (line)
                for line in interspray_wash_block:
                    f.writelines (line)
            # Syringe emptying block
            for line in cleaning_procedure_block_sol[sol]:
                f.writelines(line)
            # Waiting phase (not after the last spray cycle, only between spray cycles)
            if sol < (range(len(solution_to_use))[-1]):
                for line in waiting_phase_between_solutions_block_sol[sol]:
                    f.writelines(line)
    except:
        # First wash block
        for line in first_wash_block:
            f.writelines(line)
        # Spray
        for i in range(number_of_spray_cycles):
            for line in spray_block:
                f.writelines (line)
            for line in interspray_wash_block:
                f.writelines (line)
        # Syringe emptying block
        for line in cleaning_procedure_block:
            f.writelines(line)
    # Motors off
    for line in motors_off_block:
        f.writelines(line)





####################################################################### GTK GUI (requires Tkinter)
# Gcode file generated!
tkinter.Tk().withdraw()
tkinter.messagebox.showinfo(title="gcode file generated", message="The gcode file has been successfully generated!")
