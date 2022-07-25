import os
import time
import flask

app = flask.Flask(__name__)


def run_inference(model, file, jobs):
    return os.system(f"demucs -n {model} -j {jobs} -o output/ -v 0 {file}")


@app.route("/separate", methods=["POST"])
def separate():

    if "file" not in flask.request.values.keys():
        return "No file provided!", 400

    if not os.path.isfile(flask.request.values["file"]):
        return "File not found!", 400

    file = flask.request.values["file"]

    if "jobs" in flask.request.values.keys():
        jobs = flask.request.values["jobs"]
    else:
        jobs = 1

    if "model" in flask.request.values.keys():
        model = flask.request.values["model"]
    else:
        model = "mdx_extra_q"

    try:
        start = time.time()
        assert run_inference(model, file, jobs) == 0, "Error while running demucs!"
        end = time.time()

        vocals = os.path.abspath(os.path.join("output", model, "test", "vocals.wav"))
        bass = os.path.abspath(os.path.join("output", model, "test", "bass.wav"))
        drums = os.path.abspath(os.path.join("output", model, "test", "drums.wav"))
        other = os.path.abspath(os.path.join("output", model, "test", "other.wav"))

        return (
            flask.jsonify(vocals=vocals, bass=bass, drums=drums, other=other, inference_time=end - start),
            200,
        )

    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    app.run(debug=True)
