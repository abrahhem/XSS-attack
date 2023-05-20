import urllib.parse
import datetime
import http.cookies
import ast
import re

class Controller:
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.routes = {
            'GET': {
                '/': self.handle_index,
                '/home': self.handle_home,
                '/Flapjack.jpg': self.send_image,
                '/logout': self.handle_logout,
            },
            'POST': {
                '/comment': self.handle_comment,
                '/login': self.handle_login,
                '/register': self.handle_register,
            },
        }

    def handle_request(self, request):
        handler = self.routes.get(request.command, {}).get(request.path)
        if handler is None:
            self.send_error(request, 404, f'The requested URL {request.path} was not found on this server.')
            return
        handler(request)

    def handle_index(self, request):
        if self.is_authenticated(request):
            request.send_response(303)
            request.send_header('Location', '/home')
            request.end_headers()
            return
        self.send_response(request, 200, self.view.render_index())
    
    def handle_home(self, request):
        if not self.is_authenticated(request):
            request.send_response(303)
            request.send_header('Location', '/')
            request.end_headers()
            return
        self.send_response(request, 200, self.view.render_home(self.model.get_comments()))
    
    def is_authenticated(self, request):
        # Check if the user is authenticated by checking if a cookie with the
        # username and password exists in the request
        if 'Cookie' not in request.headers:
            return False
        cookies = http.cookies.SimpleCookie(request.headers['Cookie'])
        username = '' 
        password = ''
        if 'details' in cookies and re.search(r"(?=.*username)(?=.*password)", cookies["details"].value):
            username, password = ast.literal_eval(cookies["details"].value).values()
        if username and password:
            return self.model.check_user(username, password)
    
    def send_response(self, request, code, body):
        request.send_response(code)
        request.send_header('Content-type', 'text/html')
        request.end_headers()
        request.wfile.write(body.encode('utf-8'))

    def send_image(self, request):
        with open(request.path[1:], 'rb') as f:
            img_data = f.read()
        request.send_response(200)
        request.send_header('Content-type', 'image/jpg')
        request.end_headers()
        request.wfile.write(img_data)

    def handle_comment(self, request):
        content_length = int(request.headers['Content-Length'])
        post_data = request.rfile.read(content_length).decode('utf-8')
        
        try:
            comment = urllib.parse.parse_qs(post_data)['comment'][0]
        except KeyError:
            self.send_error(request, 400, f'Missing a comment {KeyError}')
            return
        
        self.model.add_comment(comment)
        request.send_response(303)
        request.send_header('Location', '/home')
        request.end_headers()

    def handle_login(self, request):
        content_length = int(request.headers['Content-Length'])
        post_data = request.rfile.read(content_length).decode('utf-8')
        try:
            username = urllib.parse.parse_qs(post_data)['username'][0]
            password = urllib.parse.parse_qs(post_data)['password'][0]
        except KeyError:
            self.send_error(request, 400, f'Missing username or password {KeyError}')
            return

        if self.model.check_user(username, password):
            expires = datetime.datetime.now() + datetime.timedelta(minutes=1)
            cookie = http.cookies.SimpleCookie()
            cookie['details'] = {
                'username': username,
                'password': password
            }
            cookie['details']['expires'] = expires.strftime('%a, %d %b %Y %H:%M:%S GMT')
            request.send_response(303)
            request.send_header('Location', '/home')
            request.send_header('Set-Cookie', cookie.output(header=''))
            request.end_headers()
        else:
            request.send_response(303)
            request.send_header('Location', '/')
            request.end_headers()

    def send_error(self, request, code, body):
        self.send_response(request, code, self.view.error_html(code, body)) 

    def handle_register(self, request):
        content_length = int(request.headers['Content-Length'])
        post_data = request.rfile.read(content_length).decode("utf-8")
        form_data = urllib.parse.parse_qs(post_data)

        if 'username' not in form_data or 'password' not in form_data:
            self.send_error(request, 400, 'Username and password are required.')
            return

        username = form_data['username'][0]
        password = form_data['password'][0]

        if self.model.add_user(username, password):
            request.send_response(303)
            request.send_header('Location', '/')
            request.end_headers()
        else:
            self.send_error(request, 400, 'Username already exists.')
    
    def handle_logout(self, request):
        cookie = http.cookies.SimpleCookie()
        cookie['details'] = ''
        request.send_response(302)
        request.send_header('Location', '/')
        request.send_header('Set-Cookie', cookie.output(header=''))
        request.end_headers()
