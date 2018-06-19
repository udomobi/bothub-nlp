from tornado.web import asynchronous
from tornado.gen import coroutine

from . import ApiHandler
from ..utils import ValidationError
from ..utils import authorization_required


class ParseHandler(ApiHandler):
    @asynchronous
    @coroutine
    def get(self):
        self.set_header('Content-Type', 'text/plain')
        self.finish('OK')

    @asynchronous
    @coroutine
    @authorization_required
    def post(self):
        text = self.get_argument('text', default=None)
        language = self.get_argument('language', default=None)

        if not text:
            raise ValidationError('text field is required', field='text')

        repository_authorization = self.repository_authorization()
        repository = repository_authorization.repository
        update = repository.last_trained_update(language)

        if not update:
            raise ValidationError(
                'This repository has never been trained',
                field='language')

        self.finish({'text': text, 'language': language})
