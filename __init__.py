import hardware_setup

from gui.core.ugui import Screen, ssd, Window

from gui.widgets.label import Label
from gui.core.writer import CWriter
from gui.widgets.menu import Menu
from gui.widgets.buttons import CloseButton

import uasyncio as asyncio

from fri3d import BADGE

# Font for CWriter
import gui.fonts.freesans20 as font
from gui.core.colors import *

wri = CWriter(ssd, font, WHITE, GREY, verbose=False)

class MainScreen(Screen):
    def __init__(self):
        super().__init__()

        CloseButton(wri)

        Label(wri, 100, (ssd.width//2)-(110//2), 'esterierwifi?')

        self.wifilbl = Label(wri, ssd.height-14, 10, ssd.width - 12)
        update = asyncio.create_task(self.update_wifi())
        self.reg_task(update, on_change=True)

    async def update_wifi(self):
        wifi = BADGE.wifi()
        wifi.connect()
        while(True):
            self.wifilbl.value('Wi-Fi: {}'.format(wifi.status()))
            await asyncio.sleep(1)

def run():
    print('App is running.')
    print('Ctrl-C to get Python REPL.')

    Screen.change(MainScreen)

run()
