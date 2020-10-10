from flask_restful import Resource


class DemoResource(Resource):
    def get(self):
        return {'get': 'foo'}
