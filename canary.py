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
    info['app_name'] = "No app name specified." if not "NAME" in os.environ else os.environ['NAME']
    info['version'] = "No version specified." if not "VERSION" in os.environ else os.environ['VERSION']
    info['build_date'] = "No build date specified." if not "DATE" in os.environ else os.environ['DATE']
    info['build_host'] = "No build host specified." if not "HOST" in os.environ else os.environ['HOST']
    info['git_url'] = "No git url specified." if not "GIT" in os.environ else os.environ['GIT']
    info['branch'] = "No branch specified." if not "BRANCH" in os.environ else os.environ['BRANCH']

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
