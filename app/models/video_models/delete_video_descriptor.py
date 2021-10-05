from flask_restx import fields, Namespace

# create the json input/output for the delete video endpoint
api = Namespace(name="descriptor-models", description="descriptor related model definitions")

input_args = {
    "video_name" : fields.String
}
input_model = api.model("delete_video_input", input_args)

output_args = {
    "message" : fields.String
}
output_model = api.model("delete_video_output", output_args)

delete_video_args = {
    "inputs" : fields.Nested(api.models["delete_video_input"]),
    "outputs" : fields.Nested(api.models["delete_video_output"])
}
delete_video_model = api.model("delete_video_model",delete_video_args)


delete_video_models = api.models