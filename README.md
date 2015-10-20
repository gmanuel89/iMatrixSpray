# iMatrixSpray

### Movement coordinates
The needle moves across the surface thanks to three mechanical arms.
The reference point for the coordinates consists in looking at the iMatrixSpray from the front (for the Z axis, height of the needle, perpendicular to the steel ground plate) and from here looking it from above (for the X and Y axes, looking at the ground plate). In this position, the X and Y coordinates are respectively the horizontal and vertical axes.

* The homing position is set at the center of the plate, where both X and Y coordinates are equal to zero. The Z coordinate is set to -35 (when set to zero, the needle is 80mm from the ground plate).
* When going up on the Y axis (further from the operator looking at the instrument) the Y coordinate decreases (down to a minimum of -110mm, the washing position on Y), while going down on the Y axis (closer to the operator looking at the instrument) causes the Y coordinate to increase (up to a maximum value of 80mm).
* When going left on the X axis the X coordinate decreases (to a minimum of -60mm), while going right causes the X coordinate to increase (up to a maximum of 60mm).
* Along the Z axis, the Z coordinate decreases when the needle gets closer to the ground plate (down to a minimum of -80, when the needle touches the plate. Avoid to do that!). The Z coordinate at the washing position is equal to -50, while it is set to -35 during the travel. During the spray it is set according to the wish of the user (-80 + height from the ground plate).
* The starting position for spraying is X1,Y1 (-60,-80) (upper left corner of the squared area of spraying), while the ending position for spraying is X2,Y2 (60,80) (bottom right corner of the squared area of spraying). The Z coordinate is set according to the user's wish.
* The washing position is set at X=0, Y=-110, Z=-50.

### Spraying
The iMatrixSpray calculates how much solution to withdraw for each cycle of spraying and how much solution to spray onto the tissue area (on both axes), according to some parameters set by the user.
* Solution density (in microliters per squared centimeter)
* Height of the needle from the ground plate (in millimeters)
* Distance between lines of spray (in millimeters)
* Speed of movement (in millimeters per minute)
* Number of spray cycles
* Solution to choose
* Delay (in seconds)

The calculations that the instrument makes are the following:
* The volume of solution per cycle of spraying (spray syringe volume per travel) is set to 16.7.
* Spray density = (solution density) / 100 * (distance between lines of spray)
* Number of lines = (distance along Y) / (distance between lines of spray)
* Spray travel = (number of lines) * (distance along X) + (distance along Y)
* Spray time = (spray travel) / (speed of movement)
* Spray syringe volume = (spray travel) * (spray density)
* Spray syringe travel = (spray syringe volume) / (spray syringe volume per travel)
* Spray syringe volume along X = (-1) * (distance along X) * (spray density) / (spray syringe volume per travel)
* Spray syringe volume along Y = (-1) * (distance between lines) * (spray density) / (spray syringe volume per travel)
The negative value of the last two entries means that the syringe has to expel solution instead of withdrawing it.

### Solutions
Each vial is indexed by the gcode method via a number. This number is very important because it allows both the withdrawal and the evacuation of solution from and into the vial, via the correct positioning of the valve.
* Waste solution corresponds to vial 0
* The capillary spray corresponds to vial 1 (there is actually no vial)
* Rinse solution corresponds to vial 2
* Solution A corresponds to vial 3
* Solution B corresponds to vial 4
* Solution C corresponds to vial 5


### Valve positioning
The command to put the valve into the right position is:

G1 VX F200

where the value X identifies the valve position.

* When the number is integer, the command opens the correspondent valve. In order to withdraw solution, the syringe aspirates the selected amount of solvent with the valve closed, so that vacuum is generated and when the valve opens, the vacuum causes the solvent in the communicating vial to be taken into the syringe.
So for example, after the generation of 10mm of vacuum, the valve 3 is opened (G1 V3 F200) in order to withdraw 10mm of solution A into the syringe.
In order to empty the syringe into the waste vial, the valve 0 has to be opened (G1 V0 F200) and the emptying command must be provided (G1 P0).
* When a floating point number is provided, the command sets the valve in the rinsing position, putting the waste vial in communication with the selected vial.
So for example, the command G1 V3.5 F200 sets the valve in the position according to which the vial 3 (containing solution A) and the waste vial are communicating, and the solution A goes straight into the waste, without being sprayed. This is done for rinsing of the tubes with the solution A. So 3.5 equals 3.0 in terms of vial identification number, but, since 3.0 is the correspondent floating point number of the integer 3, the command would have been equal to 3 and the valve position would have been wrong.
