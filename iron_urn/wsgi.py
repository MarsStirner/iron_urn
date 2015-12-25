import flask
import requests

from iron_urn.lib.access import get_url
from iron_urn.systemwide import app


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/urn:X-Medicine:<nss>/url')
def render_urn(nss):
    return get_url(nss)


@app.route('/urn:X-Medicine:<nss>/proxy')
def proxy_urn(nss):
    url = get_url(nss)
    try:
        print "Proxying to", url
        response = requests.get(url, timeout=10)
    except requests.Timeout:
        return flask.abort(504)
    except requests.ConnectionError:
        return flask.abort(502)
    except Exception, e:
        return flask.abort(500, repr(e))
    else:
        headers = response.headers.copy()
        headers.pop('content-encoding', None)
        return response.content, response.status_code, headers.iteritems()


if __name__ == '__main__':
    app.run(port=5010, debug=True)
