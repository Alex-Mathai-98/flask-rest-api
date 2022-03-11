from flask_restx import fields, Namespace

# create the json input/output for the add video endpoint
dummy_namespace = Namespace(name="descriptor-models", description="descriptor related model definitions")

input_args = {
    "video_name" : fields.String
}
input_model = dummy_namespace.model("add_video_input", input_args)

output_args = {
    "message" : fields.String
}
output_model = dummy_namespace.model("add_video_output", output_args)

add_video_args = {
    "inputs" : fields.Nested(dummy_namespace.models["add_video_input"]),
    "outputs" : fields.Nested(dummy_namespace.models["add_video_output"])
}
add_video_model = dummy_namespace.model("add_video_model",add_video_args)

add_video_model_dict = dummy_namespace.models