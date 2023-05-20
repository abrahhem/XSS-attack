
import pandas as pd

class Model:
    
    def __init__(self, cookies_file):
        self.cookies_file = cookies_file
    
    def store_cookies(self, cookie, origin_url):
        # Load existing cookies from file
        try:
            with open(self.cookies_file, 'r') as f:
                cookies = list(cookie.strip() for cookie in f)
        except FileNotFoundError:
            cookies = list()

        # Add new cookies to the set of existing cookies
        cookies.append(cookie.lstrip() + "->" + origin_url)
        unique_cookies = pd.Series(cookies).drop_duplicates().tolist()
        
        # Write all cookies to the file
        with open(self.cookies_file, 'w') as f:
            for cookie in unique_cookies:
                f.write(cookie + '\n')
    
    def get_cookies(self):
        try:
            with open(self.cookies_file, 'r') as f:
                cookies = f.read().splitlines()
        except FileNotFoundError:
            cookies = []
        return cookies
