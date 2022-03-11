from flask_restx import reqparse


request_parser_simple_json = reqparse.RequestParser()
request_parser_simple_json.add_argument("field_A",location='json',type=str,required=True)
request_parser_simple_json.add_argument("field_B",location='json',type=str,required=True)