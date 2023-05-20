class View:
    def __init__(self, model):
        self.model = model
    
    def render_home(self, comments):
        with open('public/home_template.html', 'r') as file:
            home_html = file.read()
        
        # Modify the HTML content as needed
        comment_template = "<li>{}</li>"
        comment_list_html = ''.join(comment_template.format(comment) for comment in comments)
        home_html = home_html.replace('{comment_list_html}', comment_list_html)
        
        return home_html
    
    def render_index(self):
        with open('public/index_template.html', 'r') as file:
            index_html = file.read()
        
        return index_html
    
    def render_error(self, code, body):
        with open('public/error_template.html', 'r') as file:
            error_html = file.read()
        
        # Modify the HTML content as needed
        error_html = error_html.replace('{code}', str(code))
        error_html = error_html.replace('{body}', body)
        
        return error_html
