from flask_restx import Namespace, Resource
from app.utils.register_models import register_models
import json
from flask import request

from app.models.trial_models.request_parser_form import request_parser_form
from app.models.trial_models.request_parser_form_queryparam import request_parser_form_queryparam
from app.models.trial_models.request_parser_simple_json import request_parser_simple_json
from app.models.trial_models.request_parser_simple_json_queryparam import request_parser_simple_json_queryparam


from app.models.trial_models.marshalling_complex_json import marshalling_complex_json

# Namespace definition : /trial
trial_ns = Namespace(name='trial',description='understanding flask')

# /trial/form_data
@trial_ns.route('/form_data')
class FormData(Resource) :
    """ API endpoint that takes formdata as input. """
    @trial_ns.response(200,'Success')
    @trial_ns.expect(request_parser_form)
    def post(self) :
        try :
            content_type = None
            args = request_parser_form.parse_args()
            uploaded_file = args['file']
            content_type = uploaded_file.content_type

            if content_type == "application/json" :
                byte_stream = uploaded_file.read()
                text = byte_stream.decode("utf-8") # byte-stream data to text decoding
                data = json.loads(text)
                return {"message" : "success"}
            else :
                raise ValueError("Content Type of the File must be json. Received : {}".format(content_type))
        except Exception as e :
            return {"message" : "internal server error"}

# /trial/form_data_queryparam
@trial_ns.route('/form_data_queryparam')
class FormDataQueryParam(Resource) :
    """ API endpoint that takes query parameters as input. """
    @trial_ns.response(200,'Success')
    @trial_ns.expect(request_parser_form_queryparam)
    def post(self) :
        try :
            content_type = None
            args = request_parser_form.parse_args()
            print(args)

            uploaded_file = args['file']
            field_A = request.args.get('field_A')

            content_type = uploaded_file.content_type

            if content_type == "application/json" :
                byte_stream = uploaded_file.read()
                text = byte_stream.decode("utf-8") # byte-stream data to text decoding
                data = json.loads(text)
                return {"message" : "success",
                        "field_A" : field_A}
            else :
                raise ValueError("Content Type of the File must be json. Received : {}".format(content_type))
        except Exception as e :
            print(e)
            return {"message" : "internal server error"}


# /trial/simple_json
@trial_ns.route('/simple_json')
class SimpleJSON(Resource) :
    """ API endpoint that takes a simple json payload as input. """
    @trial_ns.response(200,'Success')
    @trial_ns.expect(request_parser_simple_json)
    def post(self) :
        try :
            descriptor = request.get_json()
            field_A = descriptor["field_A"]
            field_B = descriptor["field_B"]
            return {"message" : "success",
                    "field_A" : field_A,
                    "field_B" : field_B}
        except Exception as e :
            print(e)
            return {"message" : "internal server error"}


# /trial/simple_json_queryparam
@trial_ns.route('/simple_json_queryparam')
class SimpleJSONQueryParam(Resource) :
    """ API endpoint that takes a simple JSON payload and query parameter as input. """
    @trial_ns.response(200,'Success')
    @trial_ns.expect(request_parser_simple_json_queryparam)
    def post(self) :
        try :
            descriptor = request.get_json()
            field_A = descriptor["field_A"]
            field_B = descriptor["field_B"]
            field_X = request.args.get("field_X")
            return {"message" : "success",
                    "field_A" : field_A,
                    "field_B" : field_B,
                    "field_X" : field_X}
        except Exception as e :
            print(e)
            return {"message" : "internal server error"}


# add the model of the marshalling complex json
register_models(trial_ns,[marshalling_complex_json])
# /trial/marshalling_complex_json
@trial_ns.route('/marshalling_complex_json')
class MarshallingComplexJSON(Resource) :
    """ API endpoint that takes a complex JSON payload """
    @trial_ns.response(200,'Success')
    @trial_ns.expect(marshalling_complex_json["final"])
    def post(self) :
        try :
            descriptor = request.get_json()
            field_A = descriptor["inputs"]["input"]
            field_B = descriptor["outputs"]["output"]
            return {"message" : "success",
                    "input" : field_A,
                    "output" : field_B}
        except Exception as e :
            print(e)
            return {"message" : "internal server error"}


# add the model of the marshalling complex json
register_models(trial_ns,[marshalling_complex_json])
# /trial/marshalling_complex_json
@trial_ns.route('/marshalling_complex_json_pathparam/<name>')
class MarshallingComplexJSONPathParam(Resource) :
    """ API endpoint that takes a complex JSON payload and a path parameter """
    @trial_ns.response(200,'Success')
    @trial_ns.expect(marshalling_complex_json["final"])
    def post(self,name) :
        try :
            descriptor = request.get_json()
            field_A = descriptor["inputs"]["input"]
            field_B = descriptor["outputs"]["output"]
            return {"message" : "success",
                    "input" : field_A,
                    "output" : field_B,
                    "name" : name}
        except Exception as e :
            print(e)
            return {"message" : "internal server error"}