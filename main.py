#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import cgi
import datetime
import urllib
import webapp2

from google.appengine.ext import db
from google.appengine.api import users

from handler import *

class Greeting(db.Model):
    """Models an individual Guestbook entry with an author, content, and date."""
    author = db.StringProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)


def guestbook_key(guestbook_name=None):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')

app = webapp2.WSGIApplication([
                                ('/', IndexHandler),
                                ('/signin', SigninHandler),
                                ('/fluid', FluidHandler),
                                ('/hero', HeroHandler),
                                ('/sticky-footer', StickyFooterHandler),
                                ('/sfn', StickyFooterNavHandler),
                                ('/justified-nav', JustifiedNavHandler),
                                ('/carousel', CarouselHandler),
                                ('/market-narrow', MarketNarrowHandler),
                                ('/static-grid', StaticGridHandler),
                                ('/ajax-grid', AjaxGridHandler),
                                ('/angular-ui', AngularUIHandler),
                                ('/ajax', AjaxHandler),
                              ],
                              debug=True)

if __name__ == "__main__":
    run_wsgi_app(app)

