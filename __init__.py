# TKinter
from tkinter import (
    Variable as Var, 
    StringVar as StrVar, 
    IntVar, 
    DoubleVar as FloatVar, 
    BooleanVar as BoolVar
)
from tkinter import filedialog as FTkFiledialog

# CustomTkinter | https://github.com/TomSchimansky/CustomTkinter | `pip install customtkinter`
from .customtkinter.windows.widgets.appearance_mode import AppearanceModeTracker
from .customtkinter.windows.widgets.font import FontManager
from .customtkinter.windows.widgets.scaling import ScalingTracker
from .customtkinter.windows.widgets.theme import ThemeManager
from .customtkinter.windows.widgets.core_rendering import DrawEngine
from .customtkinter.windows.widgets.core_rendering import CTkCanvas as FTkCanvas
from .customtkinter.windows.widgets.core_widget_classes import CTkBaseClass as FTkBaseClass
from .customtkinter.windows.widgets import (
    CTkButton as FTkButton, 
    CTkCheckBox as FTkCheckBox, 
    CTkComboBox as FTkComboBox, 
    CTkEntry as FTkEntry, 
    CTkFrame as FTkFrame, 
    CTkLabel as FTkLabel, 
    CTkOptionMenu as FTkOptionMenu, 
    CTkProgressBar as FTkProgressBar, 
    CTkRadioButton as FTkRadioButton, 
    CTkScrollbar as FTkScrollbar, 
    CTkSegmentedButton as FTkSegmentedButton, 
    CTkSlider as FTkSlider, 
    CTkSwitch as FTkSwitch, 
    CTkTabview as FTkTabview, 
    CTkTextbox as FTkTextbox, 
    CTkScrollableFrame as FTkScrollableFrame
)
from .customtkinter.windows import (
    CTk as FTk,
    CTkToplevel as FTkTopLevel,
    CTkInputDialog as FTkInputDialog
)
from .customtkinter.windows.widgets.font import CTkFont as FTkFont
from .customtkinter.windows.widgets.image import CTkImage as FTkImage
from .customtkinter.functions import (
    set_appearance_mode as setAppearanceMode,
    get_appearance_mode as getAppearanceMode,
    set_default_color_theme as setDefaultColorTheme,
    set_widget_scaling as setWidgetScaling,
    set_window_scaling as setWindowScaling,
    set_ctk_parent_class as setCTkParentClass,
    deactivate_automatic_dpi_awareness as deactivateAutomaticDPIAwareness
)

# CTkMenuBar | https://github.com/Akascape/CTkMenuBar | `pip install CTkMenuBar`
from .menuBar.dropdownMenu import CustomDropdownMenu as FTkDropdownMenu
from .menuBar.titleMenu import CTkTitleMenu as FTkTitleMenu
from .menuBar.menuBar import CTkMenuBar as FTkMenuBar

# CTkMessageBox | https://github.com/Akascape/CTkMessagebox | `pip install CTkMessageBox`
from .messageBox.messageBox import CTkMessagebox as FTkMessageBox

# CTkColorPicker | https://github.com/Akascape/CTkColorPicker | `pip install CTkColorPicker`
from .colorPicker.colorPicker import AskColor as FTkAskColor
from .colorPicker.colorPickerWidget import CTkColorPicker as FTkColorPicker

# CTkTable | https://github.com/Akascape/CTkTable | `pip install CTkTable`
from .table import CTkTable as FTkTable

# CTkToolTip | https://github.com/Akascape/CTkToolTip | `pip install CTkToolTip`
from .toolTip import CTkToolTip as FTkToolTip

# CTkScrollableDropdown | https://github.com/Akascape/CTkScrollableDropdown
from .scrollableDropdown.scrollableDropdown import CTkScrollableDropdown as FTkScrollableDropdown
from .scrollableDropdown.scrollableDropdownFrame import CTkScrollableDropdownFrame as FTkScrollableDropdownFrame

# CTkRangeSlider | https://github.com/Akascape/CTkRangeSlider
from .rangeSlider import CTkRangeSlider as FTkRangeSlider

# CTkPopupKeyboard | https://github.com/Akascape/CTkPopupKeyboard
from .popupKeyboard.popupKeyboard import PopupKeyboard as FTkPopupKeyboard
from .popupKeyboard.popupNumpad import PopupNumpad as FTkPopupNumpad

# TkDial | https://github.com/Akascape/TkDial | `pip install TkDial`
from .dial.dial import Dial as FTkDial
from .dial.imageKnob import ImageKnob as FTkImageKnob 
from .dial.scrollKnob import ScrollKnob as FTkScrollKnob 
from .dial.jogWheel import Jogwheel as FTkJogwheel 
from .dial.meter import Meter as FTkMeter 

# TkNodeSystem | https://github.com/Akascape/TkNodeSystem | `pip install tknodesystem`
from .nodeSystem.node_types import (
    NodeValue as FTkNodeValue, 
    NodeOperation as FTkNodeOperation, 
    NodeCompile as FTkNodeCompile, 
    NodeSocket as FTkNodeSocket
)
from .nodeSystem.node_canvas import NodeCanvas as FTkNodeCanvas
from .nodeSystem.node_menu import NodeMenu as FTkNodeMenu

# CTkRadarChart | https://github.com/Akascape/CTkRadarChart
from .radarChart import CTkRadarChart as FTkRadarChart

# CTkPieChart | https://github.com/Akascape/CTkPieChart
from .pieChart import CTkPieChart as FTkPieChart

# TkinterMapView | https://github.com/TomSchimansky/TkinterMapView | pip install tkintermapview
from .mapview.map_widget import TkinterMapView as FTkMapView
from .mapview.offline_loading import OfflineLoader as FTkOfflineLoader
from .mapview.utility_functions import (
    convert_coordinates_to_address as convertCoordinatesToAddress,
    convert_coordinates_to_country as convertCoordinatesToCountry,
    convert_coordinates_to_city as convertCoordinatesToCity,
    convert_address_to_coordinates as convertAddressToCordinates,
    decimal_to_osm as decimalToOSM,
    osm_to_decimal as OSMtoDecimal
)

# tkVideoPlayer | https://github.com/PaulleDemon/tkVideoPlayer | `pip install tkvideoplayer`
from .videoPlayer import TkinterVideo as FTkVideo

# CTkDataVisualizingWidgets | https://github.com/ZikPin/CTkDataVisualizingWidgets
from .dataVisualizingWidgets.calender import CTkCalendar as FTkCalendar
from .dataVisualizingWidgets.graph import CTkGraph as FTkGraph
from .dataVisualizingWidgets.chart import CTkChart as FTkChart
from .dataVisualizingWidgets.calendarStat import CTkCalendarStat as FTkCalendarStat