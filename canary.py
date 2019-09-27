from flask import Flask, jsonify
import os

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/health', methods=['GET'])
def health():
    status = {}
    status['status'] = "UP"
    return jsonify(status), 200

@app.route('/alive', methods=['GET'])
def alive():
    alive = {}
    alive['alive'] = "MAYBE"
    return jsonify(alive), 200

@app.route('/info', methods=['GET'])
def info():
    info = {}
    info['app_name'] = "No app name specified."
    info['version'] = "No version specified."
    info['build_date'] = "No build date specified."
    info['build_host'] = "No build host specified."
    info['git_url'] = "No git url specified."
    info['branch'] = "No branch specified."

    if "NAME" in os.environ:
        info['app_name'] = os.environ['NAME']

    if "VERSION" in os.environ:
        info['version'] = os.environ['VERSION']

    if "DATE" in os.environ:
        info['build_date'] = os.environ['DATE']

    if "HOST" in os.environ:
        info['build_host'] = os.environ['HOST']

    if "GIT" in os.environ:
        info['git_url'] = os.environ['GIT']

    if "BRANCH" in os.environ:
        info['branch'] = os.environ['BRANCH']

    return jsonify(info), 200

@app.route('/canary', methods=['GET'])
def canary():
    canary = {}
    canary['canary'] = "Chirp!"
    return jsonify(canary), 200

@app.route('/', methods=['GET'])
def index():
    return "Bird is the word.", 418

# Start app
app.run(
    host='0.0.0.0',
    port=5000,
    use_reloader=False,
    debug=True
)
