from flask import Flask

# import scheduling
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

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

# threadpool
executors = {
    'default': ThreadPoolExecutor(16),
    'processpool': ProcessPoolExecutor(4)
}

# scheduler
sched = BackgroundScheduler(timezone='America/Chicago', daemon=True)
# print("hello outside?")
sched.add_job(createGlitchedArtWork, 'interval', minutes=1)
sched.start()
# sched.print_jobs()
# app.run()

if __name__ == '__main__':
    # print("hello?")
    # sched.add_job(createGlitchedArtWork, 'interval', seconds='10')
    # sched.start()
    # sched.print_jobs()
    app.run()