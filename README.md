# FullGUI
This is a bundle of customtkinter widgets by different authors. Most of these widgets are based upon **customtkinter**, and almost all of these can be used with **customtkinter**. 

Each repository may have its own *LICENSE* and *DOCUMENTATION* which may need to be refered before using them. Note that the name of the widgets that are in the *DOCUMENTATION* may be different in **FullGUI**. Most widgets in **FullGUI** are starting with *FTk*. For eg. *FTk*Button.

```python
import FullTkinter as ftk

root = ftk.FTk()

button = ftk.FTkButton(
    master=root,
    text="example"
)
button.pack()

root.mainloop()
```