from flask_restx import reqparse
from importlib_metadata import requires

request_parser_simple_json_queryparam = reqparse.RequestParser()

request_parser_simple_json_queryparam.add_argument("field_X",type=str,required=True)
request_parser_simple_json_queryparam.add_argument("field_A",location='json',type=str,required=True)
request_parser_simple_json_queryparam.add_argument("field_B",location='json',type=str,required=True)