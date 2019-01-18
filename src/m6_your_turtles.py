"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Emily Macak.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
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
jeff=rg.SimpleTurtle()
jeff.pen=rg.Pen('teal',15)
jeff.backward(100)
jeff.right(90)
jeff.forward(100)
jeff.left(90)
jeff.forward(100)
jeff.backward(100)
jeff.right(90)
jeff.forward(100)
jeff.left(90)
jeff.forward(100)
jeff.pen=rg.Pen('white',15)
jeff.forward(100)
jeff.pen=rg.Pen('teal',15)
jeff.left(90)
jeff.forward(200)
jeff.right(135)
jeff.forward(120)
jeff.left(90)
jeff.forward(120)
jeff.right(135)
jeff.forward(200)

