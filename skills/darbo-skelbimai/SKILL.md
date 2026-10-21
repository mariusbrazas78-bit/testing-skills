---
name: darbo-skelbimai
description: Ieško ir tikrina aktualius darbo skelbimus Lietuvoje, ypač logistikos, transporto, importo, eksporto, tiekimo grandinės ir operacijų vadovų pozicijas. Naudok, kai vartotojas prašo „surask darbą“, „naujausi darbo skelbimai“, „vadovo pozicijos“, „darbo-skelbimai“, atlyginimų ar darbo pasiūlymų palyginimo. Rask 5–10 tinkamiausių aktyvių pasiūlymų su tiesioginėmis nuorodomis ir šaltiniais.
---

# Darbo skelbimai

## Paskirtis
Surink 5–10 naujausių ir tinkamiausių **patikrintų** darbo skelbimų. Pagal numatymą ieškok Lietuvoje logistikos, transporto, ekspedicijos, importo/eksporto, tiekimo grandinės ir operacijų vadovų darbo. Jeigu vartotojas pateikia kitas pareigas, regioną, kalbą, atlyginimo ribą ar darbo formą, taikyk jo sąlygas.

## Darbo eiga
1. Nustatyk paieškos datą ir laiką pagal `Europe/Vilnius`; nurodyk ją rezultate. Jei turi vartotojo CV arba aiškiai pateiktą darbo profilį, pritaikyk atranką; neišgalvok patirties.
2. Naudok prieinamas interneto paieškos ir puslapių skaitymo priemones. Tikrink CVbankas, CV-Online, LinkedIn Jobs, Užimtumo tarnybą ir darbdavių karjeros puslapius pagal tai, kas prieinama. Šaltinių ir paieškos taktika aprašyta [references/sources.md](references/sources.md). Nesinaudok neveikiančiais ar nepatvirtintais tariamais API.
3. Ieškok lietuviškomis ir angliškomis frazėmis, pvz.: `logistikos vadovas`, `transporto vadovas`, `ekspedicijos vadovas`, `tiekimo grandinės vadovas`, `operations manager`, `head of logistics`, `supply chain manager`. Papildyk sinonimais, filtruok pagal pageidaujamą miestą.
4. Atidaryk **kiekvieno** siūlomo skelbimo individualų puslapį. Patikrink pareigas, darbdavį, vietovę, atlyginimą, publikavimo / galiojimo datą, galimą nuotolinį ar hibridinį darbą ir tiesioginę nuorodą. Jeigu puslapis neprieinamas arba galiojimas neaiškus, aiškiai pažymėk **nepatvirtinta** ir netrauk į „patvirtintai aktyvių“ sąrašą. Paieškos rezultatų ištraukos nėra pakankamas aktyvumo įrodymas.
5. Nepriskirk atlyginimui bruto/neto statuso, jeigu neparašyta. Nurodyk `bruto`, `neto` arba `nenurodyta`. Jei atlyginimo nėra, rašyk `nenurodytas`. Neskaičiuok „į rankas“ be mokesčių prielaidų.
6. Deduplikuok pagal skelbimo URL, darbdavį ir pareigas (skirtingose svetainėse dubliuoti įrašai suvedami į vieną). Netrauk pasibaigusių skelbimų, išskyrus vartotojui aiškiai prašant istorijos. Atrink 5–10 tinkamiausių; jeigu patvirtintų mažiau, pateik tiek, kiek radai, nurodydamas paieškos ribas.
7. Įvertink tinkamumą pagal **konkrečius skelbimo reikalavimus** ir žinomą vartotojo profilį, nurodyk vieną trumpą pagrindimą. Atskirk šaltinio faktus nuo interpretacijos.
8. Grąžink lentelę: **Pareigos | Įmonė | Miestas / darbo forma | Atlyginimas (bruto/neto) | Paskelbta / galioja iki | Tinkamumas | Nuoroda**. Po lentele pateik 2–3 prioritetines kandidatavimo rekomendacijas ir paieškos datą. Jei informacijos nepakanka, nekurk fiktyvių skelbimų, datų ar URL.
9. Nesikandidatuok, neskelbk CV ir nesiųsk žinučių be atskiro aiškaus vartotojo nurodymo.

## Kokybės kontrolė
- Kiekvienas skelbimas turi turėti atskirai patikrintą tiesioginį URL, darbdavį ir pareigas.
- Nurodyk šaltinius; nevadink vien paieškos indekse matomo skelbimo „aktyviu“.
- Nepainiok atlyginimo bruto su neto; nežinomus laukus žymėk kaip nežinomus.
- Nurodyk paieškos ribas, jei dalis portalų neprieinami arba rezultatai nepilni.
- Jei aplinka be naršyklės ar interneto paieškos įrankio, atvirai pranešk ribojimą, pateik užklausų nuorodas ar raktažodžius, bet **nekurk** „naujausių“ skelbimų iš atminties.

## Testavimas
Naudok [evals/evals.json](evals/evals.json) su trijų tipų scenarijais: įprasta paieška, griežti filtrai, neprieinami / pasibaigę skelbimai. Vietinis statinis struktūros testas: `python -m unittest discover -s skills/darbo-skelbimai/evals -p 'test_*.py' -v` iš repozitorijos šaknies.
