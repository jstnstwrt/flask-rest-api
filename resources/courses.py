from flask import jsonify, Blueprint
from flask.ext.restful import Resource, Api, reqparse, inputs, fields

import models


class CourseList(Resource):
    
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title',
            required=True,
            help='No course title provided',
            location=['form','json']
        )
        self.reqparse.add_argument(
            'url',
            required=True,
            help="No course URL provided",
            location=['form','json'],
            type=inputs.url
        )
        super().__init__()

    def get(self):
        return jsonify({'courses': [{'title': 'Python Basics'}]})

    def post(self):
        args = self.reqparse.parse_args()
        models.Course.create(**args)
        return jsonify({'courses': [{'title': 'Python Basics'}]})


class Course(Resource):
    def get(self, id):
        return jsonify({'title': 'Python Basics'})

    def put(self, id):
        return jsonify({'title': 'Python Basics'})

    def delete(self, id):
        return jsonify({'title': 'Python Basics'})

courses_api = Blueprint('resources.courses', '__name__')
api = Api(courses_api)

api.add_resource(
    CourseList,
    '/courses',
    endpoint='courses'
)

api.add_resource(
    Course,
    '/courses/<int:id>',
    endpoint='course'
)
