from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Use HTTP methods as function(get, post, put, patch, delete)',
            'Is similar as traditional django view',
            'Gives you the most control over application logic',
            'Is mapped manually to urls',
        ]

        return Response({'message': 'Helllo!', 'ap_apiview': an_apiview})
