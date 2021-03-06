#-*- coding:utf-8 -*-


import turbo.log

from base import BaseHandler
from helpers import user as user_helper

logger = turbo.log.getLogger(__file__)


class HomeHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render('index.html')


class ApiHandler(BaseHandler):

    def GET(self, route=None, *args, **kwargs):
        self.route('route', *args, **kwargs)

    def do_route(self, *args, **kwargs):
        logger.info('msg')
        self._data = {
            'hello': 'world',
            'user': user_helper.user.hello_user()
        }