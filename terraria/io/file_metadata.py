from binstream import binstream

from terraria.io.file_type import FileType


class FileMetadata:
    def __init__(self):
        self.magic_number = 27981915666277746  # public const ulong MAGIC_NUMBER = 27981915666277746uL;
        self.size = 20
        self.type = FileType()  # public FileType Type;
        self.revision = None  # uint in original
        self.is_favorite: bool = None

    def write(self, writer):
        # TO-DO: Port functionality
        print("PLACEHOLDER terraria.io.FileMetadata.write() CALLED!")
        pass

    def increment_and_write(self, writer):
        self.revision += 1
        self.write(writer)

    @staticmethod
    def from_current_settings(type):
        file_metadata = FileMetadata()
        file_metadata.type = type
        file_metadata.revision = 0
        file_metadata.is_favorite = False
        return file_metadata

    def read(self, reader: binstream.BinaryReader):
        # TO-DO: Port functionality
        print("PLACEHOLDER terraria.io.FileMetadata.read() CALLED!")
        pass

    @staticmethod
    def read2(reader, expected_type):
        file_metadata = FileMetadata()
        file_metadata.read(reader)
        if file_metadata.type != expected_type:
            raise Exception(f'Expected type {FileType[expected_type]} but found {FileType[file_metadata]}!')
        return file_metadata
