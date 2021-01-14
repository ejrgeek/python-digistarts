from starlette.endpoints import HTTPEndpoint
from starlette.responses import Response, JSONResponse

from business.binario import operacao
from errors.errors import ValueNotAllowedException, OperationNotFoundException


class BinarioController(HTTPEndpoint):

    async def post(self, request):
        try:
            req = await request.json()
            op_lista = ['+', '-', '*', '/', '%']

            op = req['op']
            bin_um = req['bin_um']
            bin_dois = req['bin_dois']

            if op not in op_lista:
                raise OperationNotFoundException

            if int(bin_um, 2) < 0 or int(bin_um, 2) > 255 or \
                int(bin_dois, 2) < 0 or int(bin_dois, 2) > 255 :
                raise ValueNotAllowedException

            result = operacao(bin_um=bin_um, op=op, bin_dois=bin_dois)

            return Response(f'{result}')

        except OperationNotFoundException as e:
            return Response(f'{e}')
        except ValueNotAllowedException as e:
            return Response(f'{e}')
        except Exception as e:
            return Response(f'{e}')

    async def get(self, request):
        return JSONResponse({
            'detail': 'Endpoint para enviar a operação e dois numeros em binario de 0-255',
            'op': 'Ex.: +, -, *, /, %',
            'bin_um': 'Ex.: 00000001',
            'bin_dois': 'Ex.: 00000100'
        })