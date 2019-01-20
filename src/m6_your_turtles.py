"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Rachael Enrici.
"""
########################################################################
# Done
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
lily=rg.SimpleTurtle('turtle')
lily.pen=rg.Pen('purple',25)
lily.speed = 12
size = 150

for k in range(4):

    lily.pen_down()
    lily.draw_circle(size)

    lily.pen_up()
    lily.right(180)
    lily.forward(150)
    lily.pen_down()

    lily.pen_up()
    lily.backward(150)
    lily.right(180)
    lily.forward(150)
    lily.right(90)
    lily.pen_down()

frank=rg.SimpleTurtle('turtle')
frank.pen=rg.Pen('midnight blue',25)
frank.speed= 12
size1=100

for k in range(4):
    frank.pen_down()
    frank.draw_circle(size1)

    frank.pen_up()
    frank.right(180)
    frank.forward(150)
    frank.pen_down()

    frank.pen_up()
    frank.backward(150)
    frank.right(180)
    frank.forward(150)
    frank.right(90)
    frank.pen_down()
window.close_on_mouse_click()