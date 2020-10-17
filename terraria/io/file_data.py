from terraria.io.file_metadata import FileMetadata
from terraria.utilities.file_utilities import FileUtilities


class FileData:
    def __init__(self, type: str, path: str = None, is_cloud: bool = False):
        self.path = path
        self.is_cloud_save = is_cloud
        self.metadata: FileMetadata
        self.name: str
        self.type = type
        self.is_favorite = False

    def toggle_favorite(self):
        self.is_favorite = not self.is_favorite

    def get_file_name(self, include_extension=True):
        return FileUtilities.get_file_name(self.path, include_extension)

    def set_favorite(self, favorite: bool, save_changes=True):
        self.is_favorite = favorite
        if save_changes:
            # TO-DO port: (IsCloudSave ? Main.CloudFavoritesData : Main.LocalFavoriteData).SaveFavorite(this);
            pass

    # abstract method
    def set_as_active(self):
        pass

    # abstract method
    def move_to_cloud(self):
        pass

    # abstract method
    def move_to_local(self):
        pass