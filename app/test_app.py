import requests

def test_timepass() :
    assert(True)

def test_adding_video() :
    payload = {
        "inputs": {
            "video_name": "paul"
        },
        "outputs": {
            "message": "string"
        }
    }
    response = add_video(payload)
    assert( response.status_code == 200 )

    delete_video(payload)

def test_getting_video() :
    response = get_video()
    assert( response.status_code == 200 )

def test_delete_video() :
    payload = {
        "inputs": {
            "video_name": "paul"
        },
        "outputs": {
            "message": "string"
        }
    }
    response = add_video(payload)
    assert( response.status_code == 200 )

    delete_video(payload)
    assert( response.status_code == 200 )

    video_list = get_video()
    assert(payload["inputs"]["video_name"] not in video_list)

def add_video(payload) :
    return requests.post("http://localhost:1235/video/videoCollection",json=payload) 

def get_video() :
    return requests.get("http://localhost:1235/video/videoCollection") 

def delete_video(payload) :
    return requests.delete("http://localhost:1235/video/videoCollection",json=payload)