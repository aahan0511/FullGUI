"""
CTkToolTip Widget
version: 0.8
"""

import time
import sys
import customtkinter
from tkinter import Toplevel, Frame


class CTkToolTip(Toplevel):
    
    """
## Example
**Simple Usage:**
```python
CTkToolTip(widget, message="Your Message")
```
**App Example:**
```python
import customtkinter
from CTkToolTip import *

def show_value(value):
    tooltip_1.configure(message=int(value))
    
def show_text():
    print(tooltip_2.get())

root = customtkinter.CTk()

slider = customtkinter.CTkSlider(root, from_=0, to=100, command=show_value)
slider.pack(fill="both", padx=20, pady=20)

tooltip_1 = CTkToolTip(slider, message="50")

button = customtkinter.CTkButton(root, command=show_text)
button.pack(fill="both", padx=20, pady=20)

tooltip_2 = CTkToolTip(button, delay=0.5, message="This is a CTkButton!")

root.mainloop()
```

## Arguments
| Parameter | Description |
|-----------| ------------|
| **widget** | bind the tooltip to the ctk widget |
| **message** | show the message over the toolip |
| **delay** | add a small delay before showing the tooltip (default is 0.2) |
| follow | follow the mouse cursor while hovering (default is True) |
| x_offset | change the horizontal offset of the tooltip widget from mouse cursor |
| y_offset | change the vertical offset of the tooltip widget from mouse cursor |
| **alpha** | change the transparency effect of the tooltip (range: 0-1) |
| **bg_color** | change the background color of the tooltip |
| corner_radius | roundness of the corners |
| border_width | add a border around the tooltips (default is 0) |
| border_color | change the color of the border width |
| padding | add padx and pady inside the tooltip frame, tuple: (padx, pady) |
| **text_color** | change the text color of tooltip |
| wraplength | constrains the width of the tooltip, causing CTkToolTip, where required, to wrap the message at word boundaries. |
| font | label text font, tuple: (font_name, size) |
| justify | change the text display structure (left, right or center) |
| _*Other Label Parameters_ | _All other parameters for ctk label can be passed in ctktooltip_ |

## Methods

- **.configure(message, arguments...)**

   configure the text and other parameters for the tooltip
- **.get()**

   get the current text of tooltip
- **.hide()**

   disables the tooltip from appearing
- **.show()**

   enable the tooltip again
- **.is_disabled()**

   check the tooltip state

Author: Akash Bora | https://github.com/Akascape
    """

    def __init__(
            self,
            widget: any = None,
            message: str = None,
            delay: float = 0.2,
            follow: bool = True,
            x_offset: int = +20,
            y_offset: int = +10,
            bg_color: str = None,
            corner_radius: int = 10,
            border_width: int = 0,
            border_color: str = None,
            alpha: float = 0.95,
            padding: tuple = (10, 2),
            **message_kwargs):

        super().__init__()

        self.widget = widget

        self.withdraw()

        # Disable ToolTip's title bar
        self.overrideredirect(True)

        if sys.platform.startswith("win"):
            self.transparent_color = self.widget._apply_appearance_mode(
                customtkinter.ThemeManager.theme["CTkToplevel"]["fg_color"])
            self.attributes("-transparentcolor", self.transparent_color)
            self.transient()
        elif sys.platform.startswith("darwin"):
            self.transparent_color = 'systemTransparent'
            self.attributes("-transparent", True)
            self.transient(self.master)
        else:
            self.transparent_color = '#000001'
            corner_radius = 0
            self.transient()

        self.resizable(width=True, height=True)

        # Make the background transparent
        self.config(background=self.transparent_color)

        # StringVar instance for msg string
        self.messageVar = customtkinter.StringVar()
        self.message = message
        self.messageVar.set(self.message)

        self.delay = delay
        self.follow = follow
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.corner_radius = corner_radius
        self.alpha = alpha
        self.border_width = border_width
        self.padding = padding
        self.bg_color = customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"] if bg_color is None else bg_color
        self.border_color = border_color
        self.disable = False

        # visibility status of the ToolTip inside|outside|visible
        self.status = "outside"
        self.last_moved = 0
        self.attributes('-alpha', self.alpha)

        if sys.platform.startswith("win"):
            if self.widget._apply_appearance_mode(self.bg_color) == self.transparent_color:
                self.transparent_color = "#000001"
                self.config(background=self.transparent_color)
                self.attributes("-transparentcolor", self.transparent_color)

        # Add the message widget inside the tooltip
        self.transparent_frame = Frame(self, bg=self.transparent_color)
        self.transparent_frame.pack(padx=0, pady=0, fill="both", expand=True)

        self.frame = customtkinter.CTkFrame(self.transparent_frame, bg_color=self.transparent_color,
                                            corner_radius=self.corner_radius,
                                            border_width=self.border_width, fg_color=self.bg_color,
                                            border_color=self.border_color)
        self.frame.pack(padx=0, pady=0, fill="both", expand=True)

        self.message_label = customtkinter.CTkLabel(self.frame, textvariable=self.messageVar, **message_kwargs)
        self.message_label.pack(fill="both", padx=self.padding[0] + self.border_width,
                                pady=self.padding[1] + self.border_width, expand=True)

        if self.widget.winfo_name() != "tk":
            if self.frame.cget("fg_color") == self.widget.cget("bg_color"):
                if not bg_color:
                    self._top_fg_color = self.frame._apply_appearance_mode(
                        customtkinter.ThemeManager.theme["CTkFrame"]["top_fg_color"])
                    if self._top_fg_color != self.transparent_color:
                        self.frame.configure(fg_color=self._top_fg_color)

        # Add bindings to the widget without overriding the existing ones
        self.widget.bind("<Enter>", self.on_enter, add="+")
        self.widget.bind("<Leave>", self.on_leave, add="+")
        self.widget.bind("<Motion>", self.on_enter, add="+")
        self.widget.bind("<B1-Motion>", self.on_enter, add="+")
        self.widget.bind("<Destroy>", lambda _: self.hide(), add="+")

    def show(self) -> None:
        """
        Enable the widget.
        """
        self.disable = False

    def on_enter(self, event) -> None:
        """
        Processes motion within the widget including entering and moving.
        """

        if self.disable:
            return
        self.last_moved = time.time()

        # Set the status as inside for the very first time
        if self.status == "outside":
            self.status = "inside"

        # If the follow flag is not set, motion within the widget will make the ToolTip dissapear
        if not self.follow:
            self.status = "inside"
            self.withdraw()

        # Calculate available space on the right side of the widget relative to the screen
        root_width = self.winfo_screenwidth()
        widget_x = event.x_root
        space_on_right = root_width - widget_x

        # Calculate the width of the tooltip's text based on the length of the message string
        text_width = self.message_label.winfo_reqwidth()

        # Calculate the offset based on available space and text width to avoid going off-screen on the right side
        offset_x = self.x_offset
        if space_on_right < text_width + 20:  # Adjust the threshold as needed
            offset_x = -text_width - 20  # Negative offset when space is limited on the right side

        # Offsets the ToolTip using the coordinates od an event as an origin
        self.geometry(f"+{event.x_root + offset_x}+{event.y_root + self.y_offset}")

        # Time is in integer: milliseconds
        self.after(int(self.delay * 1000), self._show)

    def on_leave(self, event=None) -> None:
        """
        Hides the ToolTip temporarily.
        """

        if self.disable: return
        self.status = "outside"
        self.withdraw()

    def _show(self) -> None:
        """
        Displays the ToolTip.
        """

        if not self.widget.winfo_exists():
            self.hide()
            self.destroy()

        if self.status == "inside" and time.time() - self.last_moved >= self.delay:
            self.status = "visible"
            self.deiconify()

    def hide(self) -> None:
        """
        Disable the widget from appearing.
        """
        if not self.winfo_exists():
            return
        self.withdraw()
        self.disable = True

    def is_disabled(self) -> None:
        """
        Return the window state
        """
        return self.disable

    def get(self) -> None:
        """
        Returns the text on the tooltip.
        """
        return self.messageVar.get()

    def configure(self, message: str = None, delay: float = None, bg_color: str = None, **kwargs):
        """
        Set new message or configure the label parameters.
        """
        if delay: self.delay = delay
        if bg_color: self.frame.configure(fg_color=bg_color)

        self.messageVar.set(message)
        self.message_label.configure(**kwargs)