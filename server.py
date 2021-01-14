from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Route

from controllers.binario_controller import BinarioController
from controllers.conjunto_controller import ConjuntoController
from routers.index import routers

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
]

app = Starlette(
    debug=True,
    routes=[
        Route('/', routers, methods=['GET']),
        Route('/conjuntos', ConjuntoController, methods=['GET', 'POST']),
        Route('/binario', BinarioController, methods=['GET', 'POST']),
    ],
    middleware=middleware
)
