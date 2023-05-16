class View:
    def __init__(self, model):
        self.model = model

    
    def render_home(self, comments):
        comment_template = "<li>{}</li>"
        comment_list_html = ''.join(comment_template.format(comment) for comment in comments)
        home_html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>My Website</title>
        </head>
        <body>
            <h1>Welcome to my website!</h1>
            <img src="/Flapjack.jpg" alt="Flapjack" style="width:400px;">
            <br>
            <h2>Leave a comment:</h2>
            <form action="/comment" method="POST">
                <input type="text" name="comment">
                <input type="submit" value="Submit">
            </form>
            <h2>Comments:</h2>
            {comment_list_html}
            <a href="/logout">Logout</a>
        </body>
        </html>
        '''
        return home_html
    
    def render_index(self):
        index_html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Login</title>
            </head>
            <body>
                <h1>Login</h1>
                <form action="login" method="POST">
                <div>
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username">
                </div>
                <div>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password">
                </div>
                <div>
                    <button type="submit">Login</button>
                    <button type="submit" formaction="/register">Sign Up</button>
                </div>
                </form>
                <script>
                </script>
            </body>
            </html>
        """
        return index_html
    
    def error_html(self, code, body):
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Error</title>
        </head>
        <body>
            <h1>Error {code}</h1>
            <p>{body}</p>
            <a href="/home">Go home</a>
        </body>
        </html>
        """

