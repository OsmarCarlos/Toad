# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def test(request):

    params = request.query_params.get('test', '')

    return Response('TEST')

