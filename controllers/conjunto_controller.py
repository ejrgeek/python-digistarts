from starlette.endpoints import HTTPEndpoint
from starlette.responses import Response, JSONResponse

from errors.errors import ValueNotAllowedException, TotalNumberDiffListSizeException
from business.conjuntos import tratamento_conjunto


class ConjuntoController(HTTPEndpoint):

    async def post(self, request):
        try:
            req = await request.json()

            total_numeros = int(req['total_numeros'])

            lista_numeros = req['lista_numeros']

            if total_numeros <= 1 or total_numeros >= 1000:
                print('1')
                raise ValueNotAllowedException
            if total_numeros != len(lista_numeros):
                print('2')
                raise TotalNumberDiffListSizeException

            for numero in lista_numeros:
                if numero <= -1000 or numero >= 1000:
                    print('3')
                    raise ValueNotAllowedException

            conj = tratamento_conjunto(lista_numeros)

            return Response(f'{conj}', status_code=200)

        except ValueNotAllowedException as e:
            return Response(f'{e}', status_code=400)
        except TotalNumberDiffListSizeException as e:
            return Response(f'{e}', status_code=400)
        except Exception as e:
            return Response(f'{e}', status_code=400)

    async def get(self, request):
        return JSONResponse({
            'detail': 'Endpoint para enviar o total de numeros e lista de numeros',
            'total_numeros': 'Ex.: 10',
            'lista_numeros': 'Ex.: [10, 10, 9, 9, 8, 8, 7, 7, 6, 6]'
        })