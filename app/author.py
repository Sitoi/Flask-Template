import datetime


class Author:
    """
    初始化作者信息

    ::

        from app.author.py import Author
        author = Author()

    """

    def __init__(self):
        """
        初始化作者信息。

        """
        self.name = "Shi Tao"
        self.area = "Shanghai"
        self.birthday = "1997-04-18 05:20"

    def get_author(self) -> dict:
        """
        获取作者信息

        :return: author info

        ::

            get_author = author.get_author()

        数据内容：

        ::

            {
                "name": "Shi Tao",
                "area": "Shanghai",
                "age": 22
            }

        """
        now_time = datetime.datetime.now()
        birthday_data = datetime.datetime.strptime(self.birthday, "%Y-%m-%d %H:%M")
        age = now_time.year - birthday_data.year
        author_info = {
            "name": self.name,
            "area": self.area,
            "age": age
        }
        return author_info
