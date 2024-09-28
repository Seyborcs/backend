from fastapi import APIRouter

from random import randint

router = APIRouter()

trivias = [
        {"title": "Historia", "content": "Pneumatyczną oponę rowerową wynalazł w 1888 roku szkocki lekarz weterynarii John Boyd Dunlop."},
        {"title": "Popularność w Amsterdamie", "content": "Blisko 60% z 1,2 miliona mieszkańców Amsterdamu używa roweru jako podstawowego środka lokomocji."},
        {"title": "Spalanie kalorii", "content": "Przeciętny mężczyzna pokonując rowerem 100 km ze średnią prędkością 20 km/h, spali około 3400 kcal."},
        {"title": "Rekord prędkości", "content": "Rekord prędkości w jeździe na rowerze poziomym po płaskiej nawierzchni wynosi 132,5 km/h."},
        {"title": "Warszawskie Towarzystwo Cyklistów", "content": "Jest jedną z najstarszych polskich organizacji sportowych, liczy blisko 130 lat."},
        {"title": "Rower w kulturze", "content": "Welocyped i bicykl to pierwotne nazwy roweru."},
        {"title": "Rower dla każdego", "content": "Dla osób starszych są specjalne rowery trzykołowe z wygodnym siedzeniem."},
        {"title": "Handbike", "content": "Jest to rower dla osób niepełnosprawnych, napędzany rękami."},
        {"title": "Zmniejszenie liczby dzieci jeżdżących do szkoły", "content": "W ciągu ostatnich 30 lat liczba dzieci na świecie, które chodzą lub jeżdżą rowerem do szkoły, spadła z 82% do zaledwie 14%"},
        {"title": "Historia", "content": "Pierwszy rower, znany jako “drezyna”, został wynaleziony przez Karla von Drais w 1817 roku."},
    {"title": "dupa", "content": "pieprzyć"},
    {"title": "dupa1", "content": "pieprzyć"},
    {"title": "dupa2", "content": "pieprzyć"}
]

@router.get("/")
def getTrivia():
    return trivias[randint(0, len(trivias)-1)]
