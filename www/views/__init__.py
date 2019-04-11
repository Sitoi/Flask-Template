from flask_restplus import Api

from .author import api as info

api = Api(
    title="Flask 项目模板",
    version="0.0.1",
    description="Flask 项目模板（Flask Template）",
    doc="/debug/"
)

api.add_namespace(info, path="/api/v3/template")
