from flask_restx import reqparse
from werkzeug.datastructures import FileStorage

request_parser_form = reqparse.RequestParser()
request_parser_form.add_argument("file",location='files',type=FileStorage,required=True)