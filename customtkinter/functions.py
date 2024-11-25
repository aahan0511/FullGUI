from .windows.widgets.appearance_mode import AppearanceModeTracker
from .windows.widgets.scaling import ScalingTracker
from .windows.widgets.theme import ThemeManager
from .windows import ctk_tk

def set_appearance_mode(mode_string: str):
    """ possible values: light, dark, system 
    
    Author: Tom Schimansky | https://github.com/TomSchimansky"""
    AppearanceModeTracker.set_appearance_mode(mode_string)

def get_appearance_mode() -> str:
    """ get current state of the appearance mode (light or dark) 
    
    Author: Tom Schimansky | https://github.com/TomSchimansky"""
    if AppearanceModeTracker.appearance_mode == 0: return "Light"
    elif AppearanceModeTracker.appearance_mode == 1: return "Dark"

def set_default_color_theme(color_string: str):
    """ set color theme or load custom theme file by passing the path 
    
    Author: Tom Schimansky | https://github.com/TomSchimansky"""
    ThemeManager.load_theme(color_string)

def set_widget_scaling(scaling_value: float):
    """ set scaling for the widget dimensions 
    
    Author: Tom Schimansky | https://github.com/TomSchimansky"""
    ScalingTracker.set_widget_scaling(scaling_value)

def set_window_scaling(scaling_value: float):
    """ set scaling for window dimensions 
    
    Author: Tom Schimansky | https://github.com/TomSchimansky"""
    ScalingTracker.set_window_scaling(scaling_value)

def deactivate_automatic_dpi_awareness():
    """ deactivate DPI awareness of current process (windll.shcore.SetProcessDpiAwareness(0)) 
    
    Author: Tom Schimansky | https://github.com/TomSchimansky"""
    ScalingTracker.deactivate_automatic_dpi_awareness = True

def set_ctk_parent_class(ctk_parent_class):
    "Author: Tom Schimansky | https://github.com/TomSchimansky"
    ctk_tk.CTK_PARENT_CLASS = ctk_parent_class
