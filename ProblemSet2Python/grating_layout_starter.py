"""Author: Peter Satterthwaite July, 2021"""
import gdspy 
gdspy.current_library = gdspy.GdsLibrary()


"""
All units are in um
Design parameters for our fabrication process - DO NOT CHANGE 
"""

chip_height = 13000 # Slightly larger than 0.5"
chip_width = 15500 # Slightly larger than 0.6"
frame_height = chip_height-2000
frame_width = chip_width-2000
text_offset = 200
text_height = 400
text_width = 1500
text_frame_width = 100

""" Setup .gds file """
# The data in the gds file is stored in a library, which contains multiple cells.
lib = gdspy.GdsLibrary()

# Geometry must be placed in cells.
main_cell = lib.new_cell('Main')


""" Draw Frame that will go around design """
# Create frame for design
frame = gdspy.Rectangle((-chip_width/2, -chip_height/2),(+chip_width/2, +chip_height/2))
inner = gdspy.Rectangle((-frame_width/2, -frame_height/2),(+frame_width/2, +frame_height/2))

'''
Boolean operations allow you to easily create more complicated geometrys
In this case, we create an outer rectangle and remove an inside rectangle of frame width and height
by taking the first rectangle and "not-ing" it with an inner rectangle
''' 
frame = gdspy.boolean(frame,inner,'not') 


# Add label to frame 
text_start = (-frame_width/2-text_offset,frame_height/2+text_offset)

this_text = "LOREM IPSUM" # TODO : add label for your chip 
this_title = gdspy.Text(this_text, text_height, position=(text_start[0]+text_frame_width, text_start[1]+text_frame_width))
bb = this_title.get_bounding_box()
text_frame = gdspy.Rectangle(bb[0]-text_frame_width,bb[1]+text_frame_width)
frame = gdspy.boolean(frame,text_frame,'not')

# Every geometry must be added to cell in order for it to be included in the gds file
main_cell.add(frame)
main_cell.add(this_title)


""" Draw periodic structure """

# TODO : Write code for generating a periodic structure. The code below is a 
# template for drawing a single rectangle This rectangle spans from 
# x= -1 to 1 and y = -frame_height/2 to frame_height/2


pos1 = [-1,-frame_height/2]
pos2 = [1,frame_height/2]


'''
gdspy.Rectangle(point1, point2)

Relevant Parameters:
-----------
    point1 (array-like[2]) – Coordinates of a corner of the rectangle.
    point2 (array-like[2]) – Coordinates of the corner of the rectangle opposite to point1.
'''

this_rectangle = gdspy.Rectangle(pos1,pos2)
main_cell.add(this_rectangle) # You have to add every geometry that you draw to the respective cell.

""" Save design """ 

# Save design
save_path = '/Users/alice/Desktop/'   # TODO : Change to your preferred save directory 
file_title = "this_file.gds"          # TODO : Change to your preferred  file title
lib.write_gds(save_path+file_title)

