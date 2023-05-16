class Model:
    def __init__(self, comments_file, users_file):
        self.comments_file = comments_file
        self.users_file = users_file

    def get_comments(self):
        try:
            with open(self.comments_file, 'r') as f:
                comments = f.read().splitlines()
        except FileNotFoundError:
            comments = []
        return comments

    def add_comment(self, comment):
        with open(self.comments_file, 'a') as f:
            f.write(comment + '\n')

    def check_user(self, username, password):
        with open(self.users_file, "r") as f:
            for line in f:
                user, pwd = line.strip().split(":")
                if user == username and pwd == password:
                    return True
        return False
    
    def add_user(self, username, password):
        if self.user_exists(username):
            return False  # User already exists
        with open(self.users_file, "a") as f:
            f.write(f"{username}:{password}\n")
        return True  # User added successfully

    def user_exists(self, username):
        with open(self.users_file, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    stored_username = line.split(":")[0]
                    if username == stored_username:
                        return True
        return False
