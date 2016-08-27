import uuid

import flask
from flask_restful import abort
from flask_restful import Api
from flask_restful import reqparse
from flask_restful import Resource


app = flask.Flask(__name__)
api = Api(app)


TODOS = {}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(
            404,
            message="Todo {} doesn't exist".format(todo_id)
        )


parser = reqparse.RequestParser()
parser.add_argument('task', required=True)


class Todo(Resource):
    """Show a single todo item and lets you delete a todo item."""

    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {
            'id': todo_id,
            'task': args['task'],
        }
        TODOS[todo_id] = task
        return task, 201


class TodoList(Resource):
    """Show a list of all todos, and lets you POST to add new tasks."""

    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = uuid.uuid4().hex
        TODOS[todo_id] = {
            'id': todo_id,
            'task': args['task'],
        }
        return TODOS[todo_id], 201


# Setup the Api resource routing here
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
