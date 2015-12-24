import flask

from iron_urn.systemwide import app


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/urn:<nid_nss>')
def render_urn(nid_nss):
    if ':' not in nid_nss:
        return flask.abort(404)
    nid, nss = nid_nss.split(':', 1)

    return 'nid: %s\nnss: %s' % (nid, nss), 200, {'Content-Type': 'text/plain; charset=utf-8'}


if __name__ == '__main__':
    app.run(port=5010, debug=True)
