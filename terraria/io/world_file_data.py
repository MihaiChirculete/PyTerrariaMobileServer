import datetime

from terraria.io.file_data import FileData
import os.path, time

from terraria.io.file_metadata import FileMetadata
from terraria.io.file_type import FileType
from terraria.utilities.file_utilities import FileUtilities


class WorldFileData(FileData):
    def __init__(self, path=None, cloud_save=False):
        super().__init__(type='World', path=path, is_cloud=cloud_save)

        self.creation_time = None
        self.world_size_x: int = None
        self.world_size_y: int = None
        self.is_valid = True
        self._world_size_name: str = None
        self.is_expert_mode: bool = None
        self.has_corruption = True
        self.is_hard_mode: bool = None
        self.world_size_name = self.world_size_name
        self.has_crimson = not self.has_corruption

    def set_has_crimson(self, value):
        self.has_crimson = value
        self.has_corruption = not value

    def set_as_active(self):
        from terraria.main import Main
        Main.active_world_file_data = self

    def set_world_size(self, x, y):
        self.world_size_x = x
        self.world_size_y = y

        if x == 4200:
            self._world_size_name, self.world_size_name = 'Small'
        elif x == 6400:
            self._world_size_name, self.world_size_name = 'Medium'
        elif x == 8400:
            self._world_size_name, self.world_size_name = 'Large'
        else:
            self._world_size_name, self.world_size_name = 'Unknown'

    @staticmethod
    def from_invalid_world(path, cloud_save):
        world_file_data = WorldFileData(path, cloud_save)
        world_file_data.is_expert_mode = False
        world_file_data.metadata = FileMetadata.from_current_settings(FileType.world)
        world_file_data.set_world_size(1, 1)
        world_file_data.has_corruption = True
        world_file_data.is_hard_mode = False
        world_file_data.is_valid = False
        world_file_data.name = FileUtilities.get_file_name(path=path, include_extension=False)
        if not cloud_save:
            world_file_data.creation_time = time.ctime(os.path.getctime(path))
        else:
            world_file_data.creation_time = datetime.datetime.now()

        return world_file_data