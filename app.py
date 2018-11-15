from flask import Flask, jsonify, send_file, request
import img

app = Flask(__name__)

@app.route('/get_image')
def get_image(filename):
    return send_file(filename, mimetype='image/png')


@app.route('/run', methods=['POST'])
def run():
    result = img.run()
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

