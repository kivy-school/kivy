from .base_app import BaseReloaderApp
from kivy.app import App as KivyApp

class App(BaseReloaderApp, KivyApp):
    """
    add core functionality for reloadable apps
    base on kivy-school/kivy-reloader code
    """