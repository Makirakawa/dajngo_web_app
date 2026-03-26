from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

auto_dict = {
    'Bmw': "[auto_list] --> [BMW] Немецкий премиум-бренд (основан в 1916). Известен спортивным характером, качественной управляемостью и технологиями. Популярен в сегменте бизнес и люкс.",
    'Honda': "[auto_list] --> [Honda] Японская компания (с 1948). Надёжные и экономичные автомобили. Также один из крупнейших производителей двигателей и мотоциклов.",
    'Toyota': "[auto_list] --> [Toyota] Крупнейший автопроизводитель мира. Славится надёжностью и гибридными технологиями (например Prius). Основана в Японии в 1937.",
    'Marussia': "[auto_list] --> [Marussia] Российский бренд спорткаров (2007–2014). Производил эксклюзивные автомобили, но закрылся из-за финансовых проблем.",
    'Mercedes': "[auto_list] --> [Mercedes] Немецкий премиум-бренд (с 1926). Символ роскоши, комфорта и инноваций. Один из лидеров в сегменте люкс-авто.",
    'Nissan': "[auto_list] --> [Nissan] Японская компания (с 1933). Делает доступные и практичные авто. Известна моделями GT-R и электрокаром Leaf.",
    'Lada': "[auto_list] --> [Lada] Российский бренд (АвтоВАЗ, с 1966). Простые, недорогие и ремонтопригодные автомобили, популярны в странах СНГ.",
    'Audi': "[auto_list] --> [Audi] Немецкий премиум-бренд (с 1909). Известен технологиями (quattro), современным дизайном и комфортом.",
}


def get_info_about_cars(request, about_cars: str):
    description = auto_dict.get(about_cars, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"Автомобиль с названием {about_cars} мы еще не добавили((")


def get_info_about_cars_by_number(request, about_cars: int):
    autos = list(auto_dict)
    if about_cars > len(autos):
        return HttpResponseNotFound(f"Автомобиль по номеру {about_cars} не обнаружен")

    name_auto = autos[about_cars - 1]
    return HttpResponseRedirect(f"/auto_list/{name_auto}")
