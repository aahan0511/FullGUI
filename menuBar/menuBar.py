"""
Customtkinter Menu Bar.

Author: Akash Bora | https://github.com/Akascape
"""

import customtkinter

class CTkMenuBar(customtkinter.CTkFrame):

    """
### Usage
```python
from FullTkinter import *
...
menu = MenuBar(master=root)
menu.add_cascade("Menu")
...
```

### Methods
- **.add_cascade(text, ctk_button_args...)**: add new menu button in the menu bar
- **.configure(*args)**: update parameters 

### Arguments
| Parameter | Description |
|-----------| ------------|
| **master** | define the master widget, can be root or frame |
| bg_color | set the bg color of the menu bar |
| height | set height of the menu bar |
| width | set width of the menu bar buttons |
| padx | set internal padding between menu bar buttons |
| pady | set internal padding in top and bottom of menu bar |
| postcommand | add a command before spawing the dropdown |
| _*other frame parameters_ | other ctk frame parameters can also be passed |

Author: Akash Bora | https://github.com/Akascape
    """
        
    def __init__(
        self,
        master,
        bg_color = ["white","black"],
        height: int = 25,
        width: int = 10,
        padx: int = 5,
        pady: int = 2,
        **kwargs):

        if master.winfo_name().startswith("!ctkframe"):
            bg_corners = ["", "", bg_color, bg_color]
            corner = master.cget("corner_radius")
        else:
            bg_corners = ["", "", "", ""]
            corner = 0
            
        super().__init__(master, fg_color=bg_color, corner_radius=corner, height=height, background_corner_colors=bg_corners, **kwargs)
        self.height = height
        self.width = width
        self.after(10)
        self.num = 0
        self.menu = []
        self.padx = padx
        self.pady = pady

        super().pack(anchor="n", fill="x")

    def add_cascade(self, text=None, postcommand=None, **kwargs):
    
        if not "fg_color" in kwargs:
            fg_color = "transparent"
        else:
            fg_color = kwargs.pop("fg_color")
        if not "text_color" in kwargs:
            text_color = customtkinter.ThemeManager.theme["CTkLabel"]["text_color"]
        else:
            text_color = kwargs.pop("text_color")
            
        if not "anchor" in kwargs:
            anchor = "w"
        else:
            anchor = kwargs.pop("anchor")

        if text is None:
            text = f"Menu {self.num+1}"
            
        self.menu_button = customtkinter.CTkButton(self, text=text, fg_color=fg_color,
                                                   text_color=text_color, width=self.width,
                                                   height=self.height, anchor=anchor, **kwargs)
        self.menu_button.grid(row=0, column=self.num, padx=(self.padx,0), pady=self.pady)
        
        if postcommand:
            self.menu_button.bind("<Button-1>", lambda event: postcommand(), add="+")
            
        self.num += 1

        return self.menu_button
    
    def configure(self, **kwargs):
        if "bg_color" in kwargs:
           super().configure(fg_color=kwargs.pop("bg_color"))
        super().configure(**kwargs)
