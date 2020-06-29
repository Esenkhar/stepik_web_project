def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = []
    for query in environ['QUERY_STRING'].split('&'):
        body.append((query+'\n').encode())
    start_response(status, headers)
    return iter(body)
