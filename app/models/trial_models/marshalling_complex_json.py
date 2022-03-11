from flask_restx import fields, Namespace

dummy_namespace = Namespace(name="dummy_namespace")

input_args = {
    "input" : fields.String()
}
input_model = dummy_namespace.model("input",input_args)

output_args = {
    "output" : fields.String()
}
output_model = dummy_namespace.model("output",output_args)

final_args = {
    "inputs" : fields.Nested(input_model),
    "outputs" : fields.Nested(output_model)
}
final_model = dummy_namespace.model("final",final_args)

marshalling_complex_json = dummy_namespace.models