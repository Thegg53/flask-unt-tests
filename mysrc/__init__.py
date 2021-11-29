from flask import Flask

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
   

    @app.route("/hello")
    def hello():
        return "Hello, World!"
    

    @app.route("/")
    def hello_world():
        print("console here")
        return "<p>Hello, World!</p>"


    @app.route("/double/<x>")
    def double(x):
        y = int(x)
        print("doubler")
        return "<div>your result is:</div>" + str(2 * y)

    return app    
    
# if __name__ == '__main__':
    # create_app().run('0.0.0.0', 8085)




