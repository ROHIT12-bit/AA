from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'God'


# Replace app.run() with:
if __name__ == '__main__':
    from gunicorn.app.base import BaseApplication
    class FlaskApp(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()
        def load(self):
            return self.application
    options = {'bind': '0.0.0.0:5000', 'workers': 1}
    FlaskApp(app, options).run()
