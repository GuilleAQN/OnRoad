import dj_database_url

def get_database_config(url, env):
    return {env: {'ENGINE': 'django.db.backends.postgresql', **dj_database_url.parse(url)}}