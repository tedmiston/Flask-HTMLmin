__author__ = 'Hamid FzM'

from htmlmin.main import minify


class HTMLMIN(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('MINIFY_PAGE', False)

        if app.config['MINIFY_PAGE']:
            app.after_request(self.response_minify)

    def response_minify(self, response):
        """
        minify response html to decrease traffic
        """
        if response.content_type == u'text/html; charset=utf-8':
            response_text = response.get_data(as_text=True)
            htmlmin_kwargs = dict(reduce_empty_attributes=False,
                                  remove_comments=True,
                                  remove_optional_attribute_quotes=False)
            minified = minify(response_text, **htmlmin_kwargs)
            response.set_data(minified)

            return response
        return response
