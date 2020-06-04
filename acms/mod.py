from .models import Users
from .models import Partner
from .models import Store
from .models import Address

def sign_in(request):
    full_name=request.POST.get("Name")
    email=request.POST.get("signinEmail")
    phone=request.POST.get("Number")
    password=request.POST.get("signinPassword")
    users=Users(full_name=full_name,email=email,phone=phone,password=password)
    users.save()



def store_details(request):
    # longitude = request.POST("longitude")
    # latitude = request.POST("latitude")
    # location= Locations(longitude=longitude, latitude=latitude)
    # location.save()

    firstline = request.POST("firstline")
    # second_line = request.POST("second_line")
    city = request.POST("city")
    state = request.POST("state")
    pin_code = request.POST("pin_code")
    country_code = request.POST("country_code")
    address=Address(firstline=firstline,city=city,state=state,pin_code=pin_code,country_code=country_code)
    address.save()

    # name = request.POST("First_Name")
    email = request.POST("Email_Id")
    phone = request.POST("Mobile_Number")
    address1=address.id
    partner =Partner(email=email,phone=phone,address=address1)
    partner.save()

    store_name = request.POST("First_Name")
    partner_id = partner.id
    # address2 = address.id
    # locations = location.id
    google_rating = request.POST("google_rating")
    store_type = request.POST("store_type")
    gstin = request.POST("gstin")
    no_of_lockers = request.POST("no_of_lockers")
    no_of_cctv = request.POST("no_of_cctv")
    # ease_of_transportation = request.POST("ease_of_transportation")

    store= Store(store_name=store_name,partner_id=partner_id,google_rating=google_rating,gstin=gstin,store_type=store_type,no_of_cctv=no_of_cctv,no_of_lockers=no_of_lockers)
    store.save()

