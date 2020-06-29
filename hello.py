def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = []
    body = '\n'.join(environ['QUERY_STRING'].split('&')).encode('utf-8')
    start_response(status, headers)
    return [body]
