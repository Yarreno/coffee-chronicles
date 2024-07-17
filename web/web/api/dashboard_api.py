import json
from django.http import HttpResponse, JsonResponse
from web.enums.graphic_type import GraphicType
from web.services.graph_service import call_graph_script
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def dashboard_api(request):
    print(request.method)
    if 'username' in request.session:    
        if request.method == 'POST':
            data = json.loads(request.body)
            graph = data.get('graph', None)
            type_str = data.get('type', None)
            type = GraphicType[type_str] if type_str else None
            
            print(graph)
            print(type)

            if graph and type is not None:
                call_graph_script(type, graph)
                imagePath = f'static/{graph}.png'
                result = {'imagePath': imagePath}
                return JsonResponse(result)
            else:
                return HttpResponse(status=400)
        else:
            return HttpResponse(status=405)
    else:
        return HttpResponse(status=401)