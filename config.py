import os
import yaml

class Config:
    # Load app.yml
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'app.yml')
    with open(config_path, 'r') as f:
        config_data = yaml.safe_load(f)

    env = os.environ.get('FLASK_ENV', 'development')
    env_config = config_data.get(env, config_data['development'])

    # Set parameters
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or env_config.get('SQLALCHEMY_DATABASE_URI', 'mysql+pymysql://root:root@localhost:3306/lab')
    SQLALCHEMY_TRACK_MODIFICATIONS = env_config.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or env_config.get('JWT_SECRET_KEY', 'super-secret-key')
    DEBUG = env_config.get('DEBUG', True)

