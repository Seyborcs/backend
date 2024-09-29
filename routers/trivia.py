from fastapi import APIRouter

from random import randint

router = APIRouter()

trivias = [
    {"title": "Obowiązkowe wyposażenie roweru", "content": "Rower musi być wyposażony w światła przednie i tylne, odblaski, dzwonek oraz sprawne hamulce."},
    {"title": "Jazda po chodniku", "content": "Rowerzysta może jechać po chodniku, jeśli opiekuje się dzieckiem do lat 10 jadącym na rowerze, lub gdy warunki pogodowe zagrażają bezpieczeństwu."},
    {"title": "Droga dla rowerów", "content": "Rowerzysta ma obowiązek korzystać z drogi dla rowerów, jeśli jest ona wyznaczona."},
    {"title": "Przejazd przez przejście dla pieszych", "content": "Rowerzysta powinien przeprowadzać rower przez przejście dla pieszych, chyba że jest to przejazd dla rowerów."},
    {"title": "Kask ochronny", "content": "W Polsce nie ma obowiązku noszenia kasku ochronnego przez rowerzystów, choć jest to zalecane."},
    {"title": "Jazda obok siebie", "content": "Rowerzyści mogą jechać obok siebie, jeśli nie utrudnia to ruchu innych pojazdów."},
    {"title": "Zakaz jazdy po autostradach", "content": "Rowerzyści nie mogą poruszać się po autostradach i drogach ekspresowych."},
    {"title": "Sygnalizowanie manewrów", "content": "Rowerzysta ma obowiązek sygnalizować zamiar skrętu lub zmiany pasa ruchu ręką."},
    {"title": "Minimalny wiek rowerzysty", "content": "Dzieci do lat 10 mogą jeździć rowerem po drogach publicznych tylko pod opieką osoby dorosłej."},
    {"title": "Mandaty za łamanie przepisów", "content": "Za nieprzestrzeganie przepisów ruchu drogowego rowerzysta może otrzymać mandat, który może wynieść nawet 2,5 tys. złotych."},
    {"title": "dupa", "content": "pieprzyć"},
    {"title": "dupa1", "content": "pieprzyć"},
    {"title": "dupa2", "content": "pieprzyć"}
]

@router.get("/")
def getTrivia():
    return trivias[randint(0, len(trivias)-4)]
