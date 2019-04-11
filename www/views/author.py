from flask_restplus import Resource, Namespace

from app.author import Author

api = Namespace("AUTHOR INFO", description="获取作者信息")


class RequestModel:
    @staticmethod
    def get_request():
        get_parser = api.parser()
        return get_parser


@api.route("/info")
class RDBMSAPI(Resource):
    """
    作者信息获取
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.author = Author()

    @api.expect(RequestModel.get_request())
    def get(self):
        result = self.author.get_author()
        return result, 200
