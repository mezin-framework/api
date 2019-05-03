from flask_restful import Resource, marshal_with
from flask import request
from refresh_queue import RefreshQueue

class RefreshController(Resource):

    queue = RefreshQueue()

    def post(self):
        data = request.get_json()
        return self.queue.request_refresh(data)
