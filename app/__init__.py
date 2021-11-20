from flask import Flask

# import scheduling
from apscheduler.schedulers.background import BackgroundScheduler

# importing blueprints from modules
from app.main_module.glitch import createGlitchedArtWork
from .main_module.controllers import main_bp
from .module_ex_2.controllers import module_ex_2_bp

# creating app
app = Flask(__name__)

# getting configurations
app.config.from_object('config')

# register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(module_ex_2_bp)


# scheduler
sched = BackgroundScheduler(timezone='America/Chicago', daemon=True)
sched.add_job(createGlitchedArtWork, 'interval', seconds=20)

sched.start()

if __name__ == '__main__':

    app.run()