# FullGUI
This is a bundle of customtkinter widgets by different authors. Most of these widgets are based upon **customtkinter**, and almost all of these can be used with **customtkinter**. 

Each repository may have its own *LICENSE* and *DOCUMENTATION* which may need to be refered before using them. Note that the name of the widgets that are in the *DOCUMENTATION* may be different in **FullGUI**. Most widgets in **FullGUI** are starting with *FTk*. For eg. `FTkButton`.

```python
import FullGUI as ftk

root = ftk.FTk()

button = ftk.FTkButton(
    master=root,
    text="example"
)
button.pack()

root.mainloop()
```

Some methods have used PascalCase instead of Snake_case. For eg. `this_is_a_method()` -> `thisIsAMethod()`.

All widgets have their author mentioned at the bottom of their `__doc__`.

# Repositories

## [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter "CustomTkinter on GitHub")
CustomTkinter is a python UI-library based on Tkinter, which provides new, modern and fully customizable widgets. They are created and used like normal Tkinter widgets and can also be used in combination with normal Tkinter elements. The widgets and the window colors either adapt to the system appearance or the manually set mode ('light', 'dark'), and all CustomTkinter widgets and windows support HighDPI scaling (Windows, macOS). With CustomTkinter you'll get a consistent and modern look across all desktop platforms (Windows, macOS, Linux).

> [!IMPORTANT]
> All widgets that start with *CTk*, have been changed to *FTk* for FullGUI.
> Eg. `CTkButton` -> `FTkButton`

> **DOCUMENTATION**: [CustomTkinter Documentation](https://customtkinter.tomschimansky.com/documentation/ "Documentation for Customtkinter").

> **LICENSE**: [MIT License](https://github.com/TomSchimansky/CustomTkinter/blob/master/LICENSE "LICENSE on CustomTkinter").

> **AUTHOR**: [Tom Schimansky](https://github.com/TomSchimansky "Tom Schimansky on GitHub"). 

> **INSTALLATION**: `pip install customtkinter`


## [CTkMenuBar](https://github.com/Akascape/CTkMenuBar "CTkMenuBar on GitHub")
Modern menu bar widget library for customtkinter.

> [!NOTE]
> `CustomDropdownMenu` is renamed `FTkDropdownMenu` for FullGUI.
> `CTkTitleMenu` is renamed `CTkTitleMenu` for FullGUI.
> `CTkMenuBar` is renamed `FTkMenuBar` for FullGUI.

> **DOCUMENTATION**: [CTkMenuBar README](https://github.com/Akascape/CTkMenuBar/blob/main/README.md "README for CTkMenuBar").

> **LICENSE**: [Creative Commons Zero v1.0 Universal License](https://github.com/Akascape/CTkMenuBar/blob/main/LICENSE "LICENSE on CTkMenuBar").

> **AUTHOR**: [Akash Bora](https://github.com/Akascape "Akascape on GitHub").

> **INSTALLATION**: `pip install CTkMenuBar`


## [CTkMessageBox](https://github.com/Akascape/CTkMessageBox "CTkMessageBox on GitHub")
A modern and fully customizable messagebox for CustomTkinter.

> [!NOTE]
> `CTkMessageBox` is renamed `FTkMessageBox` for FullGUI.

> **DOCUMENTATION**: [CTkMessageBox README](https://github.com/Akascape/CTkMessagebox/blob/main/README.md "README for CTkMessageBox").

> **LICENSE**: [Creative Commons Zero v1.0 Universal License](https://github.com/Akascape/CTkMessagebox/blob/main/LICENSE "LICENSE on CTkMessageBox").

> **AUTHOR**: [Akash Bora](https://github.com/Akascape "Akascape on GitHub").

> **INSTALLATION**: `pip install CTkMessageBox`


## [CTkColorPicker](https://github.com/Akascape/CTkColorPicker "CTkColorPicker on GitHub")
A modern color picker made for customtkinter!

> [!NOTE]
> `CTkColorPicker` is renamed `FTkColorPicker` for FullGUI.
> `AskColor` is renamed `FTkAskColor` for FullGUI.

> **DOCUMENTATION**: [CTkColorPicker README](https://github.com/Akascape/CTkColorPicker/blob/main/README.md "README for CTkColorPicker").

> **LICENSE**: [Creative Commons Zero v1.0 Universal License](https://github.com/Akascape/CTkColorPicker/blob/main/LICENSE "LICENSE on CTkColorPicker").

> **AUTHOR**: [Akash Bora](https://github.com/Akascape "Akascape on GitHub").

> **INSTALLATION**: `pip install CTkColorPicker`


## [CTkTable](https://github.com/Akascape/CTkTable "CTkTable on GitHub")
Here is a quick and simple table widget having all the basic features.

> [!NOTE]
> `CTkTable` is renamed `FTkTable` for FullGUI.

> **DOCUMENTATION**: [CTkTable README](https://github.com/Akascape/CTkTable/blob/main/README.md "README for CTkTable").

> **LICENSE**: [MIT License](https://github.com/Akascape/CTkTable/blob/main/LICENSE "LICENSE on CTkTable").

> **AUTHOR**: [Akash Bora](https://github.com/Akascape "Akascape on GitHub").

> **INSTALLATION**: `pip install CTkTable`


## [CTkToolTip](https://github.com/Akascape/CTkToolTip "CTkToolTip on GitHub")
Small tooltip pop-up label for displaying details on customtkinter widgets.

> [!NOTE]
> `CTkToolTip` is renamed `FTkToolTip` for FullGUI.

> **DOCUMENTATION**: [CTkToolTip README](https://github.com/Akascape/CTkToolTip/blob/main/README.md "README for CTkToolTip").

> **LICENSE**: [Creative Commons Zero v1.0 Universal License](https://github.com/Akascape/CTkToolTip/blob/main/LICENSE "LICENSE on CTkToolTip").

> **AUTHOR**: [Akash Bora](https://github.com/Akascape "Akascape on GitHub").

> **INSTALLATION**: `pip install CTkToolTip`