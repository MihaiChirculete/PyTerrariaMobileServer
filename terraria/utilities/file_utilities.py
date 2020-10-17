import re


class FileUtilities:
    file_name_regex = re.compile(r"^(?P<path>.*[\\\\\\/])?(?:$|(?P<fileName>.+?)(?:(?P<extension>\\.[^.]*$)|$))")

    def __init__(self):
        return

    @staticmethod
    def get_file_name(path: str, include_extension=True):
        match = FileUtilities.file_name_regex.match(path)

        if match is None or match.groupdict()['fileName'] is None:
            return ''

        include_extension &= match.groupdict()['extension'] is not None
        return match.groupdict()['filename'] + match.groupdict()['extension'] if include_extension else ''
