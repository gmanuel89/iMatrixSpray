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
