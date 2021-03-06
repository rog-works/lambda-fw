from lf3py.api.response import Response

from example.bpapi.data.context import MyContext


def make_response(context: MyContext) -> Response:
    return Response(headers={'X-Correlation-Id': context['correlation_id']})
