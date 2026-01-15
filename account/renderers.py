from rest_framework.renderers import JSONRenderer
import json

class UserRenderer(JSONRenderer):
    charset = 'utf-8'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get('response')

        # Error response
        if response.status_code >= 400:
            return super().render({
                'status': False,
                'errors': data
            })

        # Success response
        return super().render({
            'status': True,
            'data': data
        })