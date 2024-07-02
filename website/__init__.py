from flask import Flask

def create_app():
    app= Flask(__name__)
    app.config['SECRET_KEY']='Fy5D4svpM2mL/tC2iOgIJvF1DuwjZ/7F0dY1HwfN9dEcJteim0T4bDtcCSuC319NmeqzC33g9Jyj7b+Jf3DfPleCx8NTLlfHflVcj5i6C2U='
    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/') 
    app.register_blueprint(auth,url_prefix='')
    
    return app