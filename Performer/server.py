from dataclasses import asdict
from controller import Controller
from controlparam import ControlParam
from flask import Flask, jsonify, request
from flask_cors import CORS


def launch(controller: Controller):
    server = Flask(__name__)
    CORS(server)

    @server.post("/sayparam")
    def post_sayparam():
        controller.device.say(
            f"デルタ {controller.param.delta:.02f}, ガンマ {controller.param.gamma:.02f}"
        )
        return "Done: SayParam"

    @server.post("/say")
    def post_say():
        data = request.json
        content = data["content"]
        controller.device.say(content)
        return "Done: Say"

    @server.get("/param")
    def get_param():
        data = asdict(controller.param)
        return jsonify(data)

    @server.post("/param")
    def post_param():
        data = request.json
        param = ControlParam(**data)
        controller.update_param(param)
        return jsonify(asdict(param))

    @server.post("/approach")
    def post_approach():
        controller.param.delta = max(0., controller.param.delta - 5)
        return "Done: Approach"

    @server.post("/separate")
    def post_close():
        controller.param.delta += 10.
        return "Done: Separate"

    @server.post("/faster")
    def post_faster():
        controller.param.gamma *= 3.0
        return "Done: Faster"

    @server.post("/slower")
    def post_slower():
        controller.param.gamma /= 3.0
        return "Done: Slower"

    @server.post("/start")
    def post_start():
        controller.start()
        return "Started"

    @server.post("/stop")
    def post_stop():
        controller.stop()
        return "Stopped"

    server.run("0.0.0.0", 3838)
    return server
