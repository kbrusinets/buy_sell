from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="htmls")

__all__ = {
    'templates'
}