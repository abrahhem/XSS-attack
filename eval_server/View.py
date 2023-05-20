class View:
    def __init__(self, model):
        self.model = model
    
    def render_index(self, cookies):
        with open('public/index_template.html', 'r') as file:
            index_html = file.read()
        
        # Modify the HTML content as needed
        cookie_template = '<div class="card"><p>cookie: {}<br>origin: {}</p></div>'
        cookies_list_html = ''.join(cookie_template.format(*cookie.rsplit('->', 1)) for cookie in cookies)
        index_html = index_html.replace('{cookies_list}', cookies_list_html)
        
        return index_html
    
    def render_error(self, code, body):
        with open('public/error_template.html', 'r') as file:
            error_html = file.read()
        
        # Modify the HTML content as needed
        error_html = error_html.replace('{code}', str(code))
        error_html = error_html.replace('{body}', body)
        
        return error_html
