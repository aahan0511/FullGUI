# [FullGUI](https://github.com/aahan0511/FullGUI "FullGUI GitHub Link")
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

# Contents
- [Status and Note](#status-and-notes)
- [Dependencies](#dependencies)
- [Authors](#authors)
    - [Tom Schimansky | TomSchimansky](#tom-schimansky)
    - [Akash Bora | Akascape](#akash-bora)
- [Repositories](#repositories)
    - [CustomTkinter](#customtkinter)
    - [CTkMenuBar](#ctkmenubar)
    - [CTkMessageBox](#ctkmessagebox)
    - [CTkColorPicker](#ctkcolorpicker)
    - [CTkTable](#ctktable)
    - [CTkToolTip](#ctktooltip)
    - [CTkScrollableDropdown](#ctkscrollabledropdown)
    - [CTkRangeSlider](#ctkrangeslider)
    - [CTkPopupKeyboard](#ctkpopupkeyboard)
    - [TkDial](#tkdial)
    - [TkNodeSystem](#tknodesystem)

# Status and Notes

> [!WARNING]
> This project is still in developent. The repositories added work **perfectly** [refering to how the should], but many repositories have still not been added.

> [!NOTE]
> The might be written `TheGreatLegend` as the conributor in some places, but this is a bug with GitHub desktop, and it takes my old username. Please note it should be `aahan0511`

# [Dependencies](https://github.com/aahan0511/FullGUI/network/dependencies)
```bash
pip install -r requirements.txt
```

- customtkinter
- requests
- pillow
- future
- geocoder
- pyperclip
- darkdetect
- typing-extensions
- packaging
- colour
- av

### For Windows Only
- pywin32

# [Authors](https://github.com/aahan0511/FullGUI/graphs/contributors "Contributions by Contributors")

## [Tom Schimansky](https://github.com/TomSchimansky "TomSchimansky")
> Python, C, Desktop UI, Machine Learning, RaspberryPi, Robotics, Arduino

**Author Of**: [`CustomTkinter`](https://github.com/TomSchimansky/CustomTkinter)

## [Akash Bora](https://github.com/Akascape "Akascape")
> Loves to make digital art, video effects, useful tools, UI designs, and experimental fun art! Follow me for more awesome projects!

**Author Of**:
    - [`CTkMenuBar`](https://github.com/Akascape/CTkMenuBar)
    - [`CTkMessageBox`](https://github.com/Akascape/CTkMessageBox)
    - [`CTkColorPicker`](https://github.com/Akascape/CTkColorPicker)
    - [`CTkTable`](https://github.com/Akascape/CTkTable)
    - [`CTkToolTip`](https://github.com/Akascape/CTkToolTip)
    - [`CTkScrollableDropdown`](https://github.com/Akascape/CTkScrollableDropdown)
    - [`CTkRangeSlider`](https://github.com/Akascape/CTkRangeSlider)
    - [`CTkPopupKeyboard`](https://github.com/Akascape/CTkPopupKeyboard)
    - [`TkDial`](https://github.com/Akascape/TkDial)
    - [`TkNodeSystem`](https://github.com/Akascape/TkNodeSystem)

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
> - `CustomDropdownMenu` is renamed `FTkDropdownMenu` for FullGUI.
> - `CTkTitleMenu` is renamed `CTkTitleMenu` for FullGUI.
> - `CTkMenuBar` is renamed `FTkMenuBar` for FullGUI.

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
> - `CTkColorPicker` is renamed `FTkColorPicker` for FullGUI.
> - `AskColor` is renamed `FTkAskColor` for FullGUI.

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


## [CTkScrollableDropdown](https://github.com/Akascape/CTkScrollableDropdown "CTkScrollableDropdown on GitHub")
Replace the old looking tkMenu and add this new scrollable dropdown menu to customtkinter optionmenu, combobox, entries, buttons etc...

> [!NOTE]
> - `CTkScrollableDropdown` is renamed `FTkScrollableDropdown` for FullGUI.
> - `CTkScrollableDropdownFrame` is renamed `FTkScrollableDropdownFrame` for FullGUI.

> **DOCUMENTATION**: [CTkScrollableDropdown README](https://github.com/Akascape/CTkScrollableDropdown/blob/main/README.md "README for CTkScrollableDropdown").

> **LICENSE**: [MIT License](https://github.com/Akascape/CTkScrollableDropdown/blob/main/LICENSE "LICENSE on CTkScrollableDropdown").

> **AUTHOR**: [Akash Bora](https://github.com/Akascape "Akascape on GitHub").

> **INSTALLATION**: [Installation Info](https://github.com/Akascape/CTkScrollableDropdown?tab=readme-ov-file#installation "Installation Info on CTkScrollableDropdown")


## [CTkRangeSlider](https://github.com/Akascape/CTkRangeSlider "CTkRangeSlider on GitHub")
A range slider widget made for customtkinter.

> [!NOTE]
> `CTkRangeSlider` is renamed `FTkRangeSlider` for FullGUI.

> **DOCUMENTATION**: [CTkRangeSlider README](https://github.com/Akascape/CTkRangeSlider/blob/main/README.md "README for CTkRangeSlider").

> **LICENSE**: [Creative Commons Zero v1.0 Universal License](https://github.com/Akascape/CTkRangeSlider/blob/main/LICENSE "LICENSE on CTkRangeSlider").

> **AUTHOR**: [Akash Bora](https://github.com/Akascape "Akascape on GitHub").

> **INSTALLATION**: [Installation Info](https://github.com/Akascape/CTkRangeSlider?tab=readme-ov-file#installation "Installation Info on CTkRangeSlider")


## [CTkPopupKeyboard](https://github.com/Akascape/CTkPopupKeyboard "CTkPopupKeyboard on GitHub")
On-Screen Keyboard/Numpad widget for customtkinter entries and textbox.

> [!NOTE]
> - `PopupKeyboard` is renamed `FTkPopupKeyboard` for FullGUI.
> - `PopupNumpad` is renamed `FTkPopupNumpad` for FullGUI.

> **DOCUMENTATION**: [CTkPopupKeyboard README](https://github.com/Akascape/CTkPopupKeyboard/blob/main/README.md "README for CTkPopupKeyboard").

> **LICENSE**: [MIT License](https://github.com/Akascape/CTkPopupKeyboard/blob/main/LICENSE "LICENSE on CTkPopupKeyboard").

> **AUTHOR**: [Akash Bora](https://github.com/Akascape "Akascape on GitHub").

> **INSTALLATION**: [Installation Info](https://github.com/Akascape/CTkPopupKeyboard?tab=readme-ov-file#installation "Installation Info on CTkPopupKeyboard")


## [TkDial](https://github.com/Akascape/TkDial "TkDial on GitHub")
This is a library containing some circular rotatory dial-knob widgets for Tkinter. It can be used in place of normal sliders and scale.

> [!NOTE]
> - `Dial` is renamed `FTkDial` for FullGUI.
> - `ImageKnob` is renamed `FTkImageKnob` for FullGUI.
> - `ScrollKnob` is renamed `FTkScrollKnob` for FullGUI.
> - `Jogwheel` is renamed `FTkJogwheel` for FullGUI.
> - `Meter` is renamed `FTkMeter` for FullGUI.

> **DOCUMENTATION**: [TkDial README](https://github.com/Akascape/TkDial/blob/main/README.md "README for TkDial").

> **LICENSE**: [Creative Commons Zero v1.0 Universal License](https://github.com/Akascape/TkDial/blob/main/LICENSE "LICENSE on TkDial").

> **AUTHOR**: [Akash Bora](https://github.com/Akascape "Akascape on GitHub").

> **INSTALLATION**: `pip install tkdial`


## [TkNodeSystem](https://github.com/Akascape/TkNodeSystem "TkNodeSystem on GitHub")
Advanced Node System (DAG) in tkinter python!

> [!NOTE]
> - `NodeValue` is renamed as `FTkNodeValue` for FullGUI. 
> - `NodeOperation` is renamed as `FTkNodeOperation` for FullGUI.
> - `NodeCompile` is renamed as `FTkNodeCompile` for FullGUI.
> - `NodeSocket` is renamed as `FTkNodeSocket` for FullGUI.
> - `NodeCanvas` is renamed as `FTkNodeCanvas` for FullGUI.
> - `NodeMenu` is renamed as `FTkNodeMenu` for FullGUI.

> **DOCUMENTATION**: [TkNodeSystem README](https://github.com/Akascape/TkNodeSystem/blob/main/README.md "README for TkNodeSystem").

> **LICENSE**: [MIT License](https://github.com/Akascape/TkNodeSystem/blob/main/LICENSE "LICENSE on TkNodeSystem").

> **AUTHOR**: [Akash Bora](https://github.com/Akascape "Akascape on GitHub").

> **INSTALLATION**: `pip install tknodesystem`