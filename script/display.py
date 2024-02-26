from ctypes import wintypes, windll, byref
import ctypes



class Display:

    @staticmethod
    def init():
        Display.user32 = ctypes.WinDLL("user32")
        Display.user32.SetWindowPos.restype = wintypes.HWND
        Display.user32.SetWindowPos.argtypes = [
            wintypes.HWND,
            wintypes.HWND,
            wintypes.INT,
            wintypes.INT,
            wintypes.INT,
            wintypes.INT,
            wintypes.UINT,
        ]
        Display.Z_INDEX = 0
        Display.position = 0, 680

    

    @staticmethod
    def set_always_on_top():
        Display.Z_INDEX = -1
        Display.user32.SetWindowPos(
            Display.hwnd,
            Display.Z_INDEX,
            Display.position[0],
            Display.position[1],
            0,
            0,
            1,
        )

    @staticmethod
    def set_pos(positon):
        Display.positon = positon
        
        Display.user32.SetWindowPos(
            Display.hwnd,
            Display.Z_INDEX,
            Display.position[0],
            Display.position[1],
            0,
            0,
            1,
        )

    @staticmethod
    def get_desktop_size():
        SPI_GETWORKAREA = 0x0030

        # This var will receive the result to SystemParametersInfoW
        desktopWorkingArea = wintypes.RECT()

        _ = windll.user32.SystemParametersInfoW(
            SPI_GETWORKAREA, 0, byref(desktopWorkingArea), 0
        )

        left = desktopWorkingArea.left
        top = desktopWorkingArea.top
        right = desktopWorkingArea.right
        bottom = desktopWorkingArea.bottom

        return right, bottom

    @staticmethod
    def get_taskbar_size():
        _w, _h = Display.get_size()
        _dw, _dh = Display.get_desktop_size()
        return _w - _dw, _h - _dh

    @staticmethod
    def get_size():
        return windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1)
