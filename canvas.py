# Import the necessary packages
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfilename

# Create a class for the paint application
class Paint(object):

    # Set the default values for the paint application
    DEFAULT_PEN_SIZE = 5.0
    # Set the default color to black
    DEFAULT_COLOR = 'black'

    # Create the constructor for the paint application
    def __init__(self):
        # Create the root window
        # Set the root of the window
        self.root = Tk()

        # Create the pen button and add it to the grid
        self.pen_button = Button(self.root,text="pen",command=self.use_pen)
        self.pen_button.grid(row=0,column=0)

        # Create the brush button and add it the grid
        self.brush_button=Button(self.root,text="brush",command=self.use_brush)
        self.brush_button.grid(row=0,column=1)
        
        # Create the color button and add it to the grid
        self.color_button=Button(self.root,text="color",command=self.choose_color)
        self.color_button.grid(row=0,column=2)

        # Set the eraser button
        # Set the grid layout for the eraser button
        self.eraser_button=Button(self.root,text="eraser",command=self.use_eraser)
        self.eraser_button.grid(row=0,column=3)

        self.clear_button=Button(self.root,text="clear",command=self.clear_canvas)
        self.clear_button.grid(row=0,column=5)

        self.triangle_button=Button(self.root,text="triangle",command=self.triangle_shape)
        self.triangle_button.grid(row=0,column=6)

        # self.quadrilateral=Button(self.root,text="quadrilateral",command=self.save_drawing)
        # self.save_button.grid(row=0,column=6)

        # self.circle=Button(self.root,text="circle",command=self.save_drawing)
        # self.save_button.grid(row=0,column=6)

        self.save_button=Button(self.root,text="save",command=self.save_drawing)
        self.save_button.grid(row=0,column=9)

        # Set the scale button
        # Set the grid layout for the scale button
        self.size_button=Scale(self.root,from_=1, to=100, orient=HORIZONTAL)
        self.size_button.grid(row=0,column=10)
        
        # Create the canvas
        # Set the grid layout for the canvas
        self.c=Canvas(self.root,bg="white",width=1000,height=1000)
        self.c.grid(row=1,columnspan=7)

        # The setup method
        # Initiate the mainloop
        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x=None
        self.old_y=None
        self.line_width=self.size_button.get()
        self.color=self.DEFAULT_COLOR
        self.eraser_on=False
        self.active_button=self.pen_button
        # Use the bind method to bind the left mouse button to the paint method
        # The left mouse button is represented by the string '<Button-1>'
        # As the user moves the mouse, the paint method is called
        # The drag motion is represented by the string '<B1-Motion>'
        self.c.bind("<B1-Motion>",self.paint)
        # Once the user releases the left mouse button, the reset method is called
        # The release of the left mouse button is represented by the string '<ButtonRelease-1>'
        self.c.bind("<ButtonRelease-1>",self.reset)

        self.c.bind("d",self.paint_triangle)
        # self.c.bind("<ButtonRelease-2>",self.reset)


    def triangle_shape(self):
        # When the pen button is clicked, the eraser mode is turned off
        self.activate_button(self.triangle_button)

    def use_pen(self):
        # When the pen button is clicked, the eraser mode is turned off
        self.activate_button(self.pen_button)

    def use_brush(self):
        # When the brush button is clicked, the eraser mode is turned off
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on=False
        self.color=askcolor(color=self.color)[1]

    def use_eraser(self):
        # When the eraser button is clicked, the eraser mode is turned off
        self.activate_button(self.eraser_button,eraser_mode=True)

    def clear_canvas(self):
        self.c.delete(ALL)

    def save_drawing(self):
        file_name=asksaveasfilename()
        if file_name:
            self.c.postscript(file=file_name)

    def activate_button(self,some_button,eraser_mode=False):
        # When a button is clicked, the relief of the button is set to raised
        # The relief of a button is the style of the border
        self.active_button.config(relief=RAISED)
        # When a button is clicked, the relief of the button is set to sunken
        some_button.config(relief=SUNKEN)
        # The active button is set to the button that was clicked, which is passed as an argument
        self.active_button=some_button
        self.eraser_on=eraser_mode
    
    # Draw a Line:
    # Refer to the following link for more information on the create_line method:
    # https://tkdocs.com/shipman/create_line.html
    def paint(self,event):
        # The line width is set to the value of the scale
        self.line_width=self.size_button.get()
        # The paint color is set to the color that was chosen from the color chooser
        paint_color="white" if self.eraser_on else self.color
        # If the old x and old y coordinates are set, then a line is drawn from the 
        # old x and y coordinates to the new x and y coordinates
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,event.x,event.y,width=self.line_width,fill=paint_color,capstyle=ROUND,smooth=TRUE,splinesteps=36)
        self.old_x=event.x
        self.old_y=event.y

    def paint_triangle(self,event):
        # The line width is set to the value of the scale
        self.line_width=self.size_button.get()
        # The paint color is set to the color that was chosen from the color chooser
        paint_color="black" if self.eraser_on else self.color
        # If the old x and old y coordinates are set, then a line is drawn from the 
        # old x and y coordinates to the new x and y coordinates
        # if self.old_x and self.old_y:
            # self.c.create_polygon(self.old_x, self.old_y, event.x, event.y, 50, 35, width = self.line_width, fill = paint_color)
        # self.c.create_polygon( 10, 10, event.x, event.y, 50, 35, width = self.line_width, fill = paint_color)
        print("This is above the self.triangle insdie paint_triangle")
        self.draw_triangle(event, paint_color)
        print("This is below  the self.triangle insdie paint_triangle")

        # self.old_x=event.x
        # self.old_y=event.y

    def reset(self,event):
        self.old_x,self.old_y=None,None

    # Draw a triangle:
    # Refer to the following link for more information on the create_polygon method:
    # https://tkdocs.com/shipman/create_polygon.html
    def draw_triangle(self, event, paint_color):
        print("inside draw_tringle")
        self.c.create_polygon(event.x,event.y,10,60,50,35,fill=paint_color)

    # Draw a rectangle:
    # Refer to the following link for more information on the create_polygon method:
    # https://tkdocs.com/shipman/create_polygon.html


    # Draw a Oval:
    # Refer to the following link for more information on the create_polygon method:
    # https://tkdocs.com/shipman/create_oval.html

if __name__=="__main__":
    gui=Paint()