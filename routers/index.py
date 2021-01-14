from starlette.responses import JSONResponse


def routers(request):
    rotas = []
    endpoints = ['conjuntos', 'binario']

    [rotas.append(f"http://{request['server'][0]}:{request['server'][1]}/{endpoint}") for endpoint in endpoints]

    return JSONResponse({'Rotas': rotas})
