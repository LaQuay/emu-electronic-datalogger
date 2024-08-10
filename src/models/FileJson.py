class FileJsonDump:
    file_name: str
    flat_json: dict

    def __init__(self, file_name, flat_json):
        self.file_name = file_name
        self.flat_json = flat_json
