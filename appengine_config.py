from gaesessions import SessionMiddleware

# suggestion: generate your own random key using os.urandom(64)
# WARNING: Make sure you run os.urandom(64) OFFLINE and copy/paste the output to
# this file.  If you use os.urandom() to *dynamically* generate your key at
# runtime then any existing sessions will become junk every time you start,
# deploy, or update your app!
COOKIE_KEY = '0K8q0p8cwRaEORqKqJ9wNnuG7gELqE0Xhq2ebfVrgicHrr5B0InHcLwTbDVR'


def webapp_add_wsgi_middleware(app):
    # from google.appengine.ext.appstats import recording
    app = SessionMiddleware(app, cookie_key=COOKIE_KEY)
    # app = recording.appstats_wsgi_middleware(app)
    return app
