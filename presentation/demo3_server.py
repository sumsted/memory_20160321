from bottle import get, route, request, response, run, post
import demo3


def handle_padded(handler):
    def decorator(**kwargs):
        r = handler(kwargs)
        try:
            callback = request.query.get('callback')
        except Exception, e:
            callback = None
        if callback is None:
            return r
        else:
            response.content_type = 'text/javascript'
            return "%s(%r);" % (callback, r)
    return decorator


@get('/hi/<name>')
@handle_padded
def hi(kargs):
    r = {'return_value': demo3.hi(str(kargs['name']))}
    return r


@get('/bye/<name>')
@handle_padded
def bye(kargs):
    r = {'return_value': demo3.bye(str(kargs['name']))}
    return r


run(host='0.0.0.0', port=8080, debug=True)
