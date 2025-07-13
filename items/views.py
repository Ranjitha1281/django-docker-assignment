from django.http import JsonResponse

def item_list(request):
    data = {
        "items": ["Apple", "Banana", "Orange"]
    }
    return JsonResponse(data)
