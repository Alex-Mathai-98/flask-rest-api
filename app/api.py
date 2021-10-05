from flask import Flask, url_for
from flask_cors import CORS
from flask_restx import Api, Resource


from app.namespaces.video_ns import video_ns

version_number = "0.1"
version_date = "01/Mar/2021"
PORT_NUM = 1235
HOST = "0.0.0.0"
DEBUG_FLAG = True

# small wrapper to make flask API to work on the cloud
class PatchedApi(Api):
    @property
    def specs_url(self):
        from urllib.parse import urlparse
        url_parsed = urlparse(self.base_url)
        # if port number exists - then basically localhost (http) else deployed on cloud (https)
        scheme = 'http' if url_parsed.port else 'https'
        return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)

# app init
app = Flask(__name__)
CORS(app)
api = PatchedApi(app, version=version_number, title='Data Services', validate=False)
ns = api.namespace(name="common", path="/")

api.add_namespace(video_ns)


@ns.route("/health_check")
class HealthCheck(Resource):
    def get(self):
        return "Success", 200


if __name__ == "__main__":
    app.run(host=HOST, port=PORT_NUM, debug=DEBUG_FLAG)