# XSS Attack Project
This repository contains the code for an XSS attack project completed for a Security Engineering course. The project consists of two HTTP servers written in Python, which allow for a successful XSS attack.

## How to Run the Servers
To run the servers, follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python packages.
3. Open two terminal windows, one for each server.
4. In the first terminal, navigate to the blog_server directory and run python server.py.
5. In the second terminal, navigate to the eval_server directory and run python server.py.
6. The servers should now be running. You can access the client blog at http://localhost:8000/ and the eval server at http://localhost:8001/.

# Description of the Servers
## Blog Server
The blog server is a simple HTTP server that serves a client blog, where users can post comments. The server accepts HTML input from users and does not sanitize it, making it vulnerable to an XSS attack.

To perform the XSS attack, a user can inject an alert script into their comment, which will execute when other users view the blog.

## Eval Server
The eval server is an HTTP server that adds a comment with an image on the blog server. When the image is loaded, the session cookie is hijacked, and the "cookie monster" photo is displayed. The eval server also shows the session cookie it stole from all sites in its index.html page.

The purpose of this server is to demonstrate how an XSS attack can be used to steal session cookies and gain unauthorized access to a user's account.

## Disclaimer
This project was completed for educational purposes only and should not be used for any malicious activities. The code for this project is open source and available for others to view and use. However, it should not be used for any illegal or unethical purposes. If you have any questions or comments about this project, please feel free to contact me.

## License
This project is licensed under the MIT License.
