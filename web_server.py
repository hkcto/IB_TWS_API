
from sanic import Sanic
from sanic.response import html
from jinja2 import Environment, FileSystemLoader
import json

### Jinja2 Templates
env = Environment(loader=FileSystemLoader("templates"))


class WebService():
    
    web = Sanic("Web app for Sanic")

    @web.get('/')
    async def index(request):
        with open("templates/index.html", "r") as code:
            html_code = code.read()
        # print(html_code)
        return html(html_code)

    @web.get("/jinja")
    async def jinja(request):
        template = env.get_template("index.html")
        html_code = template.render(title = "Jinja2 Render", body = "Hello World")
        return html(html_code)
    

    @web.get("/positions")
    async def table(request):
        with open("templates/positions.json", "r", encoding="utf-8") as j:
            table = json.loads(j.read())
        template = env.get_template("positions.html")
        html_code = template.render(options = table)
        return html(html_code)

if __name__=="__main__":
    
    WebService.web.run(auto_reload=True, port=80)