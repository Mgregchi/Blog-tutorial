# Python 3

#FOR TAKING USER PREDEFINED SCREENSHOTS
# SCREENSHOT
from PIL import ImageGrab
# GUI
import PySimpleGUI as sg      
# FOLDER AND DIRECTORY
import os
# GENERIC NAMING
import fnmatch

# DEFINE GUI LAYOUT
layout = [
        [sg.Button('Screenshot'), sg.Button('Cancel')], 
        [sg.Canvas(size=(400, 100), background_color=None, key= 'canvas')]
        ]      

window = sg.Window('Onwa', layout,transparent_color=None,
                   alpha_channel=.5, grab_anywhere = True, resizable = True) # disable_close=True
window.Finalize()      

canvas = window['canvas']      

# SCREEN SHOT FUNC
def screenshot():

    ''' Refresh window to get current window informations like :
Size and current location when user resize or move window around.
The above info is further used to determine how to take screenshots.

PIL's ImageGrab() takes arguments this way : (start-x, start-y, end-x, end-y)
So the user Region Of Interest could be gotten this way:
(window-x location, window-y location, window - x size, window -y size).
The above gives you user selected region.

NOTE : For some reasons ImageGrab doesn't include some areas with the above syntax.
So I added some pixels to tunne for accuracy. Take a look at "coord variable".
'''
    window.refresh()
    lx, ly = window.CurrentLocation()
    x, y = window.size
    coord = ((lx+7, ly,(x+5+lx +5), (y+ly+30)))
    img = ImageGrab.grab(coord)
    return img

# Window main loop
while True:
    event, values = window.read()
    #Close window with "x"  window button
    # You can disable it by adding " disable_close=True" in the window declaration (Line 20).
    if event == sg.WIN_CLOSED :   
        break   

    if event == 'Cancel':
        break


        # Screen shot GUI events
    elif event == 'Screenshot':
        window.Hide()
        img = screenshot()

        #UnHide when function returns
        window.UnHide()
        #img.show()
    # Learn how many screenshots with the same name
    # Add "1' to the number  then create a new name with it
    # THis is to avoid replacing existing screenshots
        shots = fnmatch.filter((shot for shot in os.listdir('.')), 'Onwa*.png')
        lrn = len(shots)
        lrn = lrn+1
        img.save('Onwa%s.png'%lrn)
        sg.popup_notify('Screenshot saved!',  location=sg.DEFAULT_WINDOW_LOCATION, display_duration_in_ms=6, fade_in_duration=10)

# CLOSE AND DELETE WINDOW
window.close();del window
