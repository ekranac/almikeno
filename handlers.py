import webapp2
import os
import jinja2
from google.appengine.ext import db


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)



class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
		if not params:
			params = {}
		template = jinja_env.get_template(view_filename)
		self.response.out.write(template.render(params))

class Post(db.Model):
    text_title = db.StringProperty()
    text_content = db.TextProperty()

    image_title = db.StringProperty()
    image_url = db.StringProperty()

    created = db.DateTimeProperty(auto_now_add = True)


class MainHandler(BaseHandler):
    def get(self):
        posts = db.GqlQuery("select * from Post order by created desc")
        args = {"posts":posts}
        self.render_template("index.html", args)

    def post(self):
        text_title = self.request.get("text-post-title")
        text_content = self.request.get("text-post-content")
        text_submit = self.request.get("submit_text_post")

        image_title = self.request.get("image-post-title")
        image_url = self.request.get("image-post-url")
        image_submit = self.request.get("submit_image_post")

        if text_submit:
            if not text_content:
                posts = db.GqlQuery("select * from Post order by created desc")
                args = {"posts":posts}
                self.render_template("index.html", args)

            else:
                #text_content = text_content.replace("\n", "<br>")
                p = Post(text_title = text_title, text_content = text_content)
                p.put()

                self.redirect("/")

        if image_submit:
            if not image_title or not image_url:
                posts = db.GqlQuery("select * from Post order by created desc")
                args = {"posts":posts}
                self.render_template("index.html", args)

            else:
                p = Post(image_title = image_title, image_url = image_url)
                p.put()

                self.redirect("/")

