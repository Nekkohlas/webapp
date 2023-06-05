from flask import Blueprint

#Blueprint of application view defined in mutiple files

views = Blueprint('views', __name__) # define blueprint .name inside () = same as variable 

@views.route('/')   # in () is "how to get to the endpoint"     # @views is decorator 
def home():         # whatever is in home (mainpage of website) will show 
    return"<h1>Test</h1>"   # simple header saying test