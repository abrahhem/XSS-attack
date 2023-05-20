class View:
    def __init__(self, model):
        self.model = model
    
    def render_index(self, cookies):
        cookie_template = '<div class="card"><p>cookie: {}<br>origin: {}</p></div>'
        cookies_list_html = ''.join(cookie_template.format(*cookie.rsplit('->', 1)) for cookie in cookies)
        index_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Hello World</title>
                <style>
                    body {{
                        background-image: url('/background.jpg');
                        background-size: cover;
                        background-repeat: no-repeat;
                        min-height: 100vh;
                         margin: 0;
                    }}
                    h1 {{
                        text-align: center;
                        color: white;
                        font-size: 4em;
                        padding-top: 100px;
                        margin: 0;
                    }}
                    h3 {{
                        text-align: center;
                        color: white;
                        font-size: 2.5em;
                    }}
                    .container {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        max-height: 50vh;
                        flex-wrap: wrap;
                        overflow: scroll;
                    }}
                    .card {{
                        background-color: rgba(0, 0, 0, 0.8);
                        border-radius: 10px;
                        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.4);
                        cursor: pointer;
                        margin: 20px;
                        padding: 50px;
                        transition: transform 0.2s ease-in-out;
                    }}
                    .card:hover {{
                        transform: translateY(-10px);
                    }}
                    .card p {{
                        color: white;
                        font-size: 1.5em;
                        margin: 0;
                    }}

                </style>
            </head>
            <body>
                <h1>Hello world</h1>
                <h3>All the cookies that have been captured so far</h3>
                <div class="container">
                    {cookies_list_html}
                </div>
            </body>
            </html>
        """
        return index_html
    
    def render_error(self, code, body):
        error_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Error {code}</title>
                <style>
                    body {{
                        background-image: url('/background.jpg');
                        background-size: cover;
                        background-repeat: no-repeat;
                        min-height: 100vh;
                         margin: 0;
                    }}
                    h1 {{
                        text-align: center;
                        color: white;
                        font-size: 4em;
                        padding-top: 100px;
                        margin: 0;
                    }}
                    p {{
                        text-align: center;
                    }}
                </style>
            </head>
            <body>
                <h1>Error {code}</h1>
                <p>{body}</p>
            </body>
            </html>
        """
        return error_html
        