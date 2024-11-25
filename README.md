# FullGUI
This is a bundle of customtkinter widgets by different authors. Most of these widgets are based upon **customtkinter**, and almost all of these can be used with **customtkinter**. 

Each repository may have its own *LICENSE* and *DOCUMENTATION* which may need to be refered before using them. Note that the name of the widgets that are in the *DOCUMENTATION* may be different in **FullGUI**. Most widgets in **FullGUI** are starting with *FTk*. For eg. `FTkButton`.

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

Some methods have used PascalCase instead of Snake_case. For eg. `this_is_a_method()` -> `thisIsAMethod()`.

# Repositories

### [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter "CustomTkinter on GitHub")
> CustomTkinter is a python UI-library based on Tkinter, which provides new, modern and fully customizable widgets. They are created and used like normal Tkinter widgets and can also be used in combination with normal Tkinter elements. The widgets and the window colors either adapt to the system appearance or the manually set mode ('light', 'dark'), and all CustomTkinter widgets and windows support HighDPI scaling (Windows, macOS). With CustomTkinter you'll get a consistent and modern look across all desktop platforms (Windows, macOS, Linux).

> [!NOTE]
> All widgets that start with *CTk*, have been changed to *FTk* for FullGUI.
> Eg. `CTkButton` -> `FTkButton`

> **DOCUMENTATION**: [CustomTkinter Documentation](https://customtkinter.tomschimansky.com/documentation/).

> **LICENSE**: [MIT License](https://github.com/TomSchimansky/CustomTkinter/blob/master/LICENSE "LICENSE on CustomTkinter").

> **AUTHOR**: [Tom Schimansky](https://github.com/TomSchimansky "Tom Schimansky on GitHub"). 