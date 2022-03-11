from flask_restx import reqparse
from werkzeug.datastructures import FileStorage

request_parser_form_queryparam = reqparse.RequestParser()
request_parser_form_queryparam.add_argument("field_A",type=str,required=True)
request_parser_form_queryparam.add_argument("file",location='files',type=FileStorage,required=True)