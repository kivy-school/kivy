
class ProviderKey:
    METRICS = 0
    AUDIO = 1
    VIDEO = 2
    MEDIAFILES = 3
    FILECHOOSER = 4
    CLOUD_STORAGE = 5
    CAMERA = 6


class ProviderFactory:

    providers = {
        ProviderKey.METRICS: None,  # to be set later
        ProviderKey.AUDIO: None ,  # to be set later
        ProviderKey.VIDEO: None,  # to be set later
        ProviderKey.MEDIAFILES: None,  # to be set later
        ProviderKey.FILECHOOSER: None,  # to be set later
        ProviderKey.CLOUD_STORAGE: None,  # to be set later
        ProviderKey.CAMERA: None,  # to be set later
    }

    # Metrics Provider

    @staticmethod
    def metrics_provider():
        provider = ProviderFactory.providers[ProviderKey.METRICS]
        if provider:
            return provider
        from .metrics import DefaultMetricsProvider
        provider = DefaultMetricsProvider()
        ProviderFactory.register_metrics_provider(provider)
        return provider
    
    @staticmethod
    def register_metrics_provider(provider):
        ProviderFactory.providers[ProviderKey.METRICS] = provider
    
    # Audio Provider

    @staticmethod
    def audio_provider():
        provider = ProviderFactory.providers[ProviderKey.AUDIO]
        if provider:
            return provider
        from .audio import AudioProvider

        provider = AudioProvider()
        ProviderFactory.register_audio_provider(provider)
        return provider
    
    @staticmethod
    def register_audio_provider(provider):
        ProviderFactory.providers[ProviderKey.AUDIO] = provider
    
    # Video Provider

    @staticmethod
    def video_provider():
        provider = ProviderFactory.providers[ProviderKey.VIDEO]
        if provider:
            return provider
        from .video import VideoProvider
        provider = VideoProvider()
        ProviderFactory.register_video_provider(provider)
        return provider
    
    @staticmethod
    def register_video_provider(provider):
        ProviderFactory.providers[ProviderKey.VIDEO] = provider

    # MediaFiles Provider
    
    @staticmethod
    def mediafiles_provider():
        provider = ProviderFactory.providers[ProviderKey.MEDIAFILES]
        if provider:
            return provider
        from .mediafiles import MediaFilesProvider
        provider = MediaFilesProvider()
        ProviderFactory.register_mediafiles_provider(provider)
        return provider
    
    @staticmethod
    def register_mediafiles_provider(provider):
        ProviderFactory.providers[ProviderKey.MEDIAFILES] = provider
    
    # FileChooser Provider

    @staticmethod
    def filechooser_provider():
        provider = ProviderFactory.providers[ProviderKey.FILECHOOSER]
        if provider:
            return provider
        from .filechooser import FileChooserProvider
        provider = FileChooserProvider()
        ProviderFactory.register_filechooser_provider(provider)
        return provider
    
    @staticmethod
    def register_filechooser_provider(provider):
        ProviderFactory.providers[ProviderKey.FILECHOOSER] = provider
    
    # CloudStorage Provider

    @staticmethod
    def cloud_storage_provider():
        from .cloud_storage import CloudStorageProvider
        return CloudStorageProvider
    
    @staticmethod
    def register_cloud_storage_provider(provider):
        ProviderFactory.providers[ProviderKey.CLOUD_STORAGE] = provider
    
    # Camera Provider

    @staticmethod
    def camera_provider():
        from .camera import CameraProvider
        return CameraProvider
    
    @staticmethod
    def register_camera_provider(provider):
        ProviderFactory.providers[ProviderKey.CAMERA] = provider
    
    # Keyboard Provider

    @staticmethod
    def keyboard_provider():
        from .keyboard import KeyboardProvider
        return KeyboardProvider
    
    @staticmethod
    def register_keyboard_provider(provider):
        ProviderFactory.providers[ProviderKey.KEYBOARD] = provider