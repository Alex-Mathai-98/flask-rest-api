from flask_restx import fields, Namespace

# create the json input/output for the add video endpoint
api = Namespace(name="descriptor-models", description="descriptor related model definitions")

input_args = {
    "video_name" : fields.String
}
input_model = api.model("add_video_input", input_args)

output_args = {
    "message" : fields.String
}
output_model = api.model("add_video_output", output_args)

add_video_args = {
    "inputs" : fields.Nested(api.models["add_video_input"]),
    "outputs" : fields.Nested(api.models["add_video_output"])
}
add_video_model = api.model("add_video_model",add_video_args)

add_video_models = api.models