from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

moto_dict = {
    'Honda': "[moto_list] --> [Honda] Японская компания (с 1948). Крупнейший производитель мотоциклов в мире. Надёжные и доступные модели от скутеров до спортбайков CBR.",
    'Yamaha': "[moto_list] --> [Yamaha] Японский бренд (с 1955). Часть «большой четвёрки». Известен серией R (R1, R6), а также квадроциклами и гидроциклами.",
    'Kawasaki': "[moto_list] --> [Kawasaki] Японская компания (с 1954). Символ мощи и агрессии. Флагман — Ninja H2R с компрессором. Также круизеры Vulcan и эндуро.",
    'Suzuki': "[moto_list] --> [Suzuki] Японский производитель (с 1952). Часть «большой четвёрки». Прославился спортбайком GSX-R и классиком Bandit.",
    'Ducati': "[moto_list] --> [Ducati] Итальянский премиум-бренд (с 1926). Страсть, дизайн и скорость. Двигатели Desmodromic. Серии Panigale, Monster. Активен в MotoGP.",
    'Harley-Davidson': "[moto_list] --> [Harley-Davidson] Американская легенда (с 1903). Символ свободы и дороги. Классические круизеры с V-twin. Культовый статус по всему миру.",
    'BMW Motorrad': "[moto_list] --> [BMW Motorrad] Немецкое подразделение BMW (с 1923). Оппозитный «Boxer», туристические серии GS и RT. R1250GS — один из самых продаваемых в мире.",
    'KTM': "[moto_list] --> [KTM] Австрийский бренд (с 1934). Специализируется на эндуро и мотокроссе. Слоган — Ready to Race. Duke и RC популярны в городе.",
    'Ural': "[moto_list] --> [Ural] Российский бренд (Ирбит, с 1941). Мотоциклы с коляской — уникальная ниша. Конструкция на основе BMW R71. Популярен среди ретро-энтузиастов.",
    'Royal Enfield': "[moto_list] --> [Royal Enfield] Старейший действующий бренд (с 1901). Ретро-стиль и круизеры. Bullet выпускается с 1932 года. Лидер в Азии.",
}

def index(request):
    motos = list(moto_dict)
    li_elements = ''
    for moto in motos:
        redirect_path = reverse("moto_list_name", args=[moto])
        li_elements += f"<li><h2><a href='{redirect_path}'>{moto.title()}</a></h2></li>"
    response = f"""
    <ul>
    {li_elements}
    </ul>
    """
    return HttpResponse(response)

def get_info_about_moto(request, about_moto: str):
    description = moto_dict.get(about_moto, None)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    else:
        return HttpResponseNotFound(f"<h2>Мотоцикла марки {description} мы не нашли (( </h2>")


def get_info_about_moto_by_number(request, about_moto: int):
    motos = list(moto_dict)
    if about_moto > len(motos):
        return HttpResponseNotFound(f"Мотоцикл под номером {about_moto} мы не смогли найти (( ")
    name_moto = motos[about_moto - 1]
    redirect = reverse("moto_list_name", args=(about_moto,))
    return HttpResponseRedirect(redirect)