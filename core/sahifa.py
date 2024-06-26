from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def sahifa(request):
    blacklisted_phones = ["975777467"]
    if request.method == "POST":
        phone = "+998" + request.POST['phone']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        return JsonResponse({"phone":phone, "first_name": first_name, "last_name":last_name})
    if request.method == "DELETE":
        return JsonResponse({"xabar":"salom delete"})
    if request.method == "PUT":
        return JsonResponse({"xabar":"salom put"})
    if request.method == "PATCH":
        return JsonResponse({"xabar":"salom patch"})
        
    telefon_raqam = request.GET['phone']
    parol = request.GET['parol']
    if telefon_raqam not in blacklisted_phones and parol == "123":
        return JsonResponse({"xabar": "Xush kelibsiz", "sahifa_linki":"http:127.0.0.1:8000/sahifa"})
    else:
        return JsonResponse({"xabar":"Olim mani ismim"})

    return JsonResponse({"xabar": f"salom {frontdan_xabar}"})



# GET
# POST
# PUT
# PATCH
# DELETE
# FILE
