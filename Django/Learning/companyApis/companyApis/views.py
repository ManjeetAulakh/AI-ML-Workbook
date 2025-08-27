from django.http import HttpResponse,JsonResponse

# def homePage(request):
#     print("Home Page")
#     return HttpResponse("This is Home")

def homePage(request):
    print("This response by json")
    data = [
        'ravi',
        'ksihidf'
    ]
    return JsonResponse(data, safe=False)