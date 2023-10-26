import os


class Config():
    # Secret key used to sign cookies and other sensitive data.
    # This should be kept secret and should never be shared with anyone.
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Connection string to the database. The specific connection string will depend on the type of database that you are using.
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    # Controls whether or not the application is in debug mode.
    # In debug mode, the application will log more information and will be easier to debug.
    DEBUG = os.environ.get('DEBUG', False)

    # Type of cache to use. The default cache is the `simple` cache, which is a simple in-memory cache.
    CACHE_TYPE = os.environ.get('CACHE_TYPE', 'simple')

    # Default timeout for cache items. The default timeout is 300 seconds (5 minutes).
    CACHE_DEFAULT_TIMEOUT = os.environ.get('CACHE_DEFAULT_TIMEOUT', 300)

    # Minimum logging level. The default logging level is `INFO`.
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO')

class DevelopmentConfig(Config):
    # Enable debug mode in development. 
    DEBUG = True

class ProductionConfig(Config):
    # Disable debug mode in production.
    DEBUG = False

# Map environment names to configuration objects.
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
