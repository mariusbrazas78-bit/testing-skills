---
name: miestu-oras
description: Pateikia penkių didžiausių Lietuvos miestų (Vilniaus, Kauno, Klaipėdos, Šiaulių ir Panevėžio) naujausią artimiausio laiko oro temperatūros prognozę ir orų sąlygas iš oficialaus meteo.lt API. Naudok, kai vartotojas prašo Lietuvos didmiesčių orų, temperatūrų palyginimo, „miestų orų“, „meteo.lt orų“ arba tiesiogiai pamini miestu-oras.
---

# Miestų orai

## Tikslas
Gauk penkių Lietuvos didžiausių miestų artimiausio prognozuojamo laiko temperatūrą ir sąlygas iš oficialaus Lietuvos hidrometeorologijos tarnybos API.

## Veiksmai
1. Jei galima vykdyti Python ir atlikti HTTPS užklausas, paleisk `python scripts/weather.py` iš šio įgūdžio katalogo. Tam nereikia API rakto ar išorinių Python paketų.
2. Jei scenarijaus vykdyti negalima, naudok prieinamą interneto užklausų įrankį ir atverk oficialius `https://api.meteo.lt/v1/places/{code}/forecasts/long-term` kiekvienam kodui: `vilnius`, `kaunas`, `klaipeda`, `siauliai`, `panevezys`. Skaityk `forecastTimestamps`: `forecastTimeUtc`, `airTemperature`, `conditionCode`.
3. Pasirink kiekvieno miesto artimiausią įrašą, kurio prognozės UTC laikas dar nepraėjo; jei ateities įrašų nėra, nenaudok senų duomenų kaip dabartinių. Skirtingų miestų prognozių laikai gali skirtis.
4. Laiką konvertuok į `Europe/Vilnius` (vasaros/žiemos laikas automatiškai).
5. Pateik lentelę su stulpeliais **Miestas**, **Temperatūra (°C)**, **Oro sąlygos**, **Prognozės laikas**. Sąlygų kodus išversk lietuviškai pagal `scripts/weather.py` žodyną.
6. Virš lentelės įrašyk „Artimiausia orų prognozė penkiems didžiausiems Lietuvos miestams“. Po lentele pateik šaltinį `https://api.meteo.lt/`, paaiškink, kad tai prognozė, o ne realiuoju laiku atlikti temperatūros matavimai. Jei duomenys negauti, nurodyk miesto klaidą ir **neišgalvok reikšmių**.
7. Jei prašoma būtent faktinių matavimų, aiškiai pasakyk, kad šis įgūdis yra prognozės pagrindu. Norint matavimų reikia atskirai susieti vietoves su meteorologijos stotimis per `/stations` ir naudoti `/stations/{station-code}/observations/latest`; prognozių nevadink matavimais.

## Patikra
Paleisk `python -m unittest discover -s evals -v`, jei yra galimybė. Testai naudoja fiktyvius duomenis ir netikrina gyvo API pasiekiamumo.
