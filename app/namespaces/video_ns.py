from flask import request
from flask_restx import Namespace, Resource

from app.utils.register_models import register_models
from app.models.video_models.add_video_descriptor import add_video_models
from app.models.video_models.delete_video_descriptor import delete_video_models


# print(add_video_models)
# add_video_models = add_video_models["add_video_models"]
# delete_video_models = delete_video_models["delete_video_models"]

video_array = set([])

# Namespace definition : /video
video_ns = Namespace(name='video',description='Video Namespace')

# add all the models
register_models(video_ns,[add_video_models,delete_video_models])
print(add_video_models)
print(delete_video_models)
print(video_ns.models)

# /video/init
@video_ns.route('/init')
class VideoInit(Resource) :
    """ Defining the resource attached to this endpoint. 
        In REST, every endpoint has one unique resource."""
    @video_ns.response(200,'Success')
    def post(self) :
        video_array.add("sample_video")
        return {"message" : "success"}

# /video/allVideos
@video_ns.route('/videoCollection')
class VideoList(Resource) :
    """ Gets all available videos """

    @video_ns.response(200,'Success')
    def get(self) : 
        return list(video_array)

    @video_ns.expect(video_ns.models["add_video_model"])
    @video_ns.response(200,'Success')
    def post(self) : 
        descriptor = request.get_json()
        try :
            new_video = descriptor["inputs"]["video_name"].lower()
            if not new_video in video_array :
                video_array.add(new_video)
                descriptor["outputs"]["message"] = "Successfully added new video"
            else :
                descriptor["outputs"]["message"] =  "Video already exists"
            return descriptor
        except Exception as e :
            print(e)
            descriptor["outputs"]["message"] =  "Code did not execute"
            return descriptor

    @video_ns.expect(video_ns.models["delete_video_model"])
    @video_ns.response(200,'Success')
    def delete(self) :
        descriptor = request.get_json()
        try :
            video = descriptor["inputs"]["video_name"].lower()
            video_array.discard(video)
            descriptor["outputs"]["message"] = "Successfully deleted video"
            return descriptor
        except Exception as e :
            print(e)
            descriptor["outputs"]["message"] =  "Code did not execute"
            return descriptor


