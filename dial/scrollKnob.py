###################--------------TkDial-ScrollKnob--------------###################

import tkinter as tk

class ScrollKnob(tk.Canvas):
    
    """
## Usage
**Simple Example**
```python
import tkinter
from tkdial import ScrollKnob
    
app = tkinter.Tk()

knob = ScrollKnob(app, start=0, end=100, steps=10)
knob.grid()
                
app.mainloop()      
```
![Simple Program](https://user-images.githubusercontent.com/89206401/204139370-73c66402-ec9a-4edc-9891-c63b209fd5e4.png)

### **Different Knob styles:**
```python
import customtkinter
from tkdial import ScrollKnob

app = customtkinter.CTk()
app.geometry("500x500")

knob1 = ScrollKnob(app, radius=250, progress_color="#87ceeb", steps=10,
                 border_width=40, start_angle=90, inner_width=1, outer_width=1,
                 text_font="calibri 20", text_color="#87ceeb", bar_color="black")
knob1.grid(row=0, column=0)

knob2 = ScrollKnob(app, radius=200, progress_color="#7eff00",
                 border_width=40, start_angle=90, inner_width=1, outer_width=0,
                 text_font="calibri 20", text_color="#7eff00", integer=True,
                 fg="#212325")
knob2.grid(row=1, column=0)

knob3 = ScrollKnob(app, text=" ", radius=250, progress_color="white",
                   bar_color="#2937a6", border_width=30, start_angle=0, inner_width=5,
                   outer_width=0, text_font="calibri 20", steps=1, text_color="white", fg="#303ba1")
knob3.grid(row=0, column=1)

knob4 = ScrollKnob(app, text=" ", steps=10, radius=200, bar_color="#242424", 
                   progress_color="yellow", outer_color="yellow", outer_length=10, 
                   border_width=30, start_angle=270, inner_width=0, outer_width=5, text_font="calibri 20", 
                   text_color="white", fg="#212325")
knob4.grid(row=1, column=1)
                
app.mainloop() 
```
![Complex example](https://user-images.githubusercontent.com/89206401/204139428-c3c3c313-539f-4867-9d50-8876a19432ee.png)

## Arguments:
  | Parameters  | Description |
  | -------- | ----------- |
  | _master_ | The master parameter is the parent widget |
  | _bg_  | The default background color of the knob widget |
  | _width_ | Define width of the widget manually (optional) |
  | _height_ | Define height of the widget manually (optional) |
  | _start_ |  The start point of the range from where the bar will rotate |
  | _end_ |  The end point of the range |
  | _radius_ | Define the radius of the knob |
  | _border_width_ | Define the width of progress bar with respect to the outer and inner ring |
  | _start_angle_ | Determines the angle from where to rotate |
  | _text_ | A string that will be displayed on the knob with value |
  | _text_color_ | Specify the color of the text that will be displayed on the knob |
  | _text_font_ | Specify the font of the text that will be displayed on the knob |
  | _integer_ | A boolean (True/False), displays only the integer value in text if True (default=False) |
  | _fg_ | Specify the color of the inner circle |
  | _progress_color_ | Define the color of the progress bar |
  | _bar_color_ | Define the color of the progress bar's background |
  | _inner_width_ | Define the width of the inner ring |
  | _inner_color_ | Specify the color of the inner ring |
  | _outer_width_ | Define the width of the outer ring |
  | _outer_length_ | Define the distance between progress bar and outer ring |
  | _inner_color_ | Specify the color of the outer ring |
  | _steps_ | Number of steps per scroll |
  | _state_ | Specify the state of the needle |
  | _command_ | Call a function whenever the bar is moved |
  
### Methods:
  | Methods   | Description |
  |-----------|-------------|
  | _.get()_ | get the current value of the knob |
  | _.set()_ | set the value of the knob |
  | _.configure()_ | configure parameters of the knob | 

Author: Akash Bora | https://github.com/Akascape
    """

    def __init__(self,
                 master,
                 start: float = 0,
                 end: float = 100,
                 radius: int = 200,
                 width: int = None,
                 height: int = None,
                 start_angle: int = 0,
                 text: str = "%",
                 border_width: int = 40, 
                 text_color: str = "black",
                 text_font: str = None,
                 progress_color: str = "grey60",
                 inner_color: str = "grey80",
                 outer_color: str = "grey80",
                 inner_width: int = 10,
                 outer_width: int = 10,
                 outer_length: int = 0,
                 bg: str = None,
                 fg: str = "#f0f0f0",
                 bar_color: str = "#f0f0f0",
                 integer: bool = False,
                 steps: int = 5,
                 state: str = "normal",
                 command = None
                 ):
        
        self.__master = master
        
        if width is None:
            width = radius 
        else:
            width = width
        
        if height is None:
            height = radius 
        else:
            height = height
            
        self.disable_text = False
        self.x0 = border_width 
        self.y0 = border_width 
        self.x1 = width-border_width 
        self.start = end
        self.bg = bg
        self.fg = fg
        self.bar_color = bar_color
        self.end = start
        self.y1 = height-border_width
        self.tx, self.ty = width / 2, height / 2
        self.width = border_width - outer_length
        self.inner = inner_width
        self.outer_length = outer_length
        self.outer = outer_width
        self.incolor = inner_color
        self.outcolor = outer_color
        self.text = text
        self.text_color = text_color
        self.text_font = text_font
        self.start_ang, self.full_extent = start_angle, 360
        self.steps = (steps/abs(self.start-self.end))*360
        self.progress_color = progress_color
        self.delta = 0
        w2 = self.width / 2
        self.value = self.start
        self.state = state
        self.integer = integer
        self.command = command
        
        if not self.bg:
            try:
                if master.winfo_name().startswith("!ctkframe"):
                    # get bg_color of customtkinter frames
                    self.bg = master._apply_appearance_mode(master.cget("fg_color"))
                else:
                    self.bg = master.cget("bg")
            except:  
                self.bg = "white"
                
        super().__init__(self.__master, bg=self.bg, width=width, height=height, bd=0, highlightthickness=0)
        
        if self.inner > self.x0:
            self.inner = self.x0
        if self.outer > self.y0:
            self.outer = self.y0
        if text=="":
            self.disable_text = True

        if self.steps<0:
            self.steps = - self.steps

        if self.steps > abs(self.start-self.end):
            if self.start>self.end:
                self.steps = self.start - self.end
            else:
                self.steps = self.end - self.start
                
        self.arc_back = self.create_arc(self.x0, self.y0, self.x1, self.y1, extent=359,
                                             start=self.start_ang, outline=self.bar_color,
                                             width=self.width, style='arc')
        
        self.arc_id = self.create_arc(self.x0, self.y0, self.x1, self.y1, extent=0,
                                        start=self.start_ang, outline=self.progress_color,
                                        width=self.width, style='arc')
        
        self.oval_id1 = self.create_oval(self.x0-w2-self.outer_length, self.y0-w2-self.outer_length, self.x1+w2+self.outer_length,
                                         self.y1+w2+self.outer_length, outline=self.outcolor,width=self.outer)
        
        self.oval_id2 = self.create_oval(self.x0+w2, self.y0+w2, self.x1-w2, self.y1-w2, width=self.inner, outline=self.incolor, fill=self.fg)
     
        if self.text:
            self.label_id = self.create_text(self.tx, self.ty, fill=self.text_color, font=self.text_font)        
        self.set_text()
        
        if state=="normal":
            self.bind('<MouseWheel>', self.scroll_command)
            self.bind("<Button-4>", lambda e: self.scroll_command(-1))
            self.bind("<Button-5>", lambda e: self.scroll_command(1))
            
    def scroll_command(self, event):
        """
        This function is used to change the value of the knob with mouse scroll
        """
        if type(event) is int:
            event_delta = event
        else:
            event_delta = event.delta
       
        if event_delta > 0:
            if self.delta>=(360-self.steps):
                self.itemconfigure(self.arc_id, extent=359)
                self.delta=360
            else:
                self.delta+=self.steps
                self.itemconfigure(self.arc_id, extent=self.delta)
        else:
            if self.delta<=(0+self.steps):
                self.itemconfigure(self.arc_id, extent=0)
                self.delta = 0
            else:
                self.delta-=self.steps
                self.itemconfigure(self.arc_id, extent=self.delta)

        self.set_text()
        
        if self.command is not None:
            self.command()
            
    def set_text(self):
        """
        This function is to set text for the knob
        """
        if not self.text:
            return
        if self.disable_text==False:
            if self.integer==True:
                self.value = int(round((self.end - self.start) / 360 * (360 - self.delta) + self.start, 2))
            else:
                self.value = round((self.end - self.start) / 360 * (360 - self.delta) + self.start, 2)
            self.itemconfigure(self.label_id, text=str(self.value) + self.text)
        else:
            self.itemconfigure(self.label_id, text="")
            
    def get(self):
        """
        This function returns the current value of the dial
        :return: float/int
        """
        return self.value
    
    def set(self, value):
        """
        This function is used to set the position of the needle
        """
        
        if value<self.end:
            value = self.end
            
        if value>=self.start:
            value = self.start

        self.delta = 360-(360/abs(self.end - self.start))*(value - self.start)
        self.itemconfigure(self.arc_id, extent=self.delta)
        self.set_text()
        
        if self.command is not None:
            self.command()
            
    def configure(self, **kwargs):
        """
        This function contains some configurable options
        """
        if "state" in kwargs:
            if kwargs["state"]!="normal":
                super().unbind('<MouseWheel>')
                super().unbind('<Button-4>')
                super().unbind('<Button-5>')
            else:
                super().bind('<MouseWheel>', self.scroll_command)
                super().bind("<Button-4>", lambda e: self.scroll_command(-1))
                super().bind("<Button-5>", lambda e: self.scroll_command(1))
            kwargs.pop("state")
            
        if "text" in kwargs:
             self.itemconfigure(self.label_id,
                text=kwargs.pop("text"))
             
        if "start" in kwargs:
            self.end = kwargs.pop("start")
            
        if "end" in kwargs:
            self.start = kwargs.pop("end")
            
        if "bg" in kwargs:
            super().configure(bg=kwargs.pop("bg"))
            
        if "width" in kwargs:
            super().configure(width=kwargs.pop("width"))
            
        if "height" in kwargs:
            super().configure(height=kwargs.pop("height"))
            
        if "bar_color" in kwargs:
            self.itemconfigure(self.arc_back,
                outline=kwargs.pop("bar_color"))
            
        if "progress_color" in kwargs:
            self.itemconfigure(self.arc_id,
                outline=kwargs.pop("progress_color"))
            
        if "fg" in kwargs:
            self.itemconfigure(
                self.oval_id2,
                fill=kwargs.pop("fg"))
            
        if "inner_color" in kwargs:
            self.itemconfigure(
                self.oval_id2,
                outline=kwargs.pop("inner_color"))
            
        if "outer_color" in kwargs:
            self.itemconfigure(
                self.oval_id1,
                outline=kwargs.pop("outer_color"))
            
        if "steps" in kwargs:
            self.steps = (int(kwargs.pop("steps"))/self.start-self.end)*360

        if "text_color" in kwargs:
            self.itemconfigure(
                self.label_id,
                fill=kwargs.pop("text_color"))
            
        if "integer" in kwargs:
            
            self.integer = kwargs.pop("integer")
            self.set_text()
            
        if len(kwargs)>0:
            raise ValueError("unknown option: " + list(kwargs.keys())[0])
