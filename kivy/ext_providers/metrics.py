from os import environ
from kivy.utils import platform
from kivy.setupconfig import USE_SDL3

class DefaultMetricsProvider:
    
    def get_dpi(self) -> float:
        if platform == 'android':
            if USE_SDL3:
                import jnius
                Hardware = jnius.autoclass('org.renpy.android.Hardware')
                value = Hardware.getDPI()
            else:
                import android
                value = android.get_dpi()
        elif platform == 'ios':
            import ios
            value = ios.get_dpi()
        else:
            # for all other platforms..
            from kivy.base import EventLoop
            EventLoop.ensure_window()
            value = EventLoop.window.dpi
        return value

    def get_density(self) -> float:
        value = 1.0
        if platform == 'android':
            import jnius
            Hardware = jnius.autoclass('org.renpy.android.Hardware')
            value = Hardware.metrics.scaledDensity
        elif platform == 'ios':
            import ios
            value = ios.get_scale()
        elif platform in ('macosx', 'win'):
            value = self.dpi / 96.0
        return value
    
    def get_fontscale(self) -> float:

        value = 1.0
        if platform == 'android':
            from jnius import autoclass
            if USE_SDL3:
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
            else:
                PythonActivity = autoclass('org.renpy.android.PythonActivity')
            config = PythonActivity.mActivity.getResources().getConfiguration()
            value = config.fontScale
        return value



