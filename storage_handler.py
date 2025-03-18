import json

class StorageHandler():
    """
    class to handle storage of blog comments or any other json storage
    """
    def __init__(self, file_path):
        """
        constructor to create instance of StorageHandler class
        :param file_path: as string
        :return: None
        """
        self._file_path = file_path


    @property
    def file_path(self):
        """
        getter to return file path
        :return: self._file_path
        """
        return self._file_path


    @file_path.setter
    def file_path(self, new_file_path):
        """
        setter to overwrite file path
        :param new_file_path: as string
        :return: None
        """
        self._file_path = new_file_path


    @property
    def comments(self):
        """
        method to create a list of comments
        :return: list of comments
        """
        with open(self.file_path, 'r', encoding="utf8") as handler:
            return json.load(handler)


    @comments.setter
    def comments(self, new_comments):
        """
        method to add a comment to the list of comments
        :param: new_comments: as list
        :return:
        """
        with open(self.file_path, 'w', encoding="utf8") as json_writer:
            json.dump(new_comments, json_writer, indent=4)


    def fetch_by_id(self, id):
        """
        function to fetch a comment by id
        :param id:
        :return:
        """
        for post in self.comments:
            if post["id"] == id:
                return post
        return None
