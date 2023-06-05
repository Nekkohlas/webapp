from flask import Blueprint

#Blueprint of application view defined in mutiple files

auth = Blueprint('auth', __name__) # define blueprint .name inside () = same as variable 