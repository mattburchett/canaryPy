from flask import Flask, jsonify, redirect
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
    info['app_name'] = os.environ['NAME'] if "NAME" in os.environ else "No app name specified."
    info['version'] = os.environ['VERSION'] if "VERSION" in os.environ else "No version specified."    
    info['build_date'] = os.environ['DATE'] if "DATE" in os.environ else "No build date specified."    
    info['build_host'] = os.environ['HOST'] if "HOST" in os.environ else "No build host specified."    
    info['git_url'] = os.environ['GIT'] if "GIT" in os.environ else "No Git URL specified."    
    info['branch'] = os.environ['BRANCH'] if "BRANCH" in os.environ else "No branch specified."

    return jsonify(info), 200

@app.route('/canary', methods=['GET'])
def canary():
    canary = {}
    canary['canary'] = "Chirp!"
    return jsonify(canary), 200

@app.route('/word', methods=['GET'])
def word():
    return redirect("https://www.youtube.com/watch?v=2WNrx2jq184", code=302)

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
