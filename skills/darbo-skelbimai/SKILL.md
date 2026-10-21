---
name: darbo-skelbimai
description: Ieško ir patikrina naujausius Lietuvos darbo skelbimus; ypač logistikos, transporto, importo/eksporto, tiekimo grandinės bei operacijų vadovų pozicijas. Naudok ieškant darbo, aktualių darbo pasiūlymų, atlyginimų palyginimo, kai vartotojas sako „surask darbą“, „darbo-skelbimai“ ar „darbo skelbimai“. Plečia paiešką iki 5–10 skelbimų, skiria patvirtintai aktyvius nuo nepatvirtintų, pateikia tiesiogines nuorodas ir įrodymus.
---

# Darbo skelbimai (v2)

## Tikslas
Surask 5–10 tinkamų **patvirtintai aktyvių** individualių darbo pasiūlymų, kai tiek įmanoma patikrinti. Jokiu būdu neužpildyk kvotos fiktyviais, pasibaigusiais ar nepatikrintais įrašais. Numatytoji paieška: Lietuva; logistikos, transporto, ekspedicijos, supply chain, importo/eksporto ir operacijų vadovavimo pozicijos.

## Veiksmų seka
1. Užfiksuok paieškos laiką Lietuvos laiku (`Europe/Vilnius`), vartotojo pareigų, regiono, darbo formos ir atlyginimo apribojimus. Jei vartotojo patirtis nežinoma, nekurk jos. Jei nenurodyta, atlyginimas nėra privalomas filtras.
2. Perskaityk [references/sources.md](references/sources.md) ir naudok veikiančią interneto paiešką, darbo paieškos įrankius bei individualių skelbimų puslapių atvėrimą. Tikrink CVbankas, CV-Online, LinkedIn Jobs, UŽT, darbdavių karjeros puslapius ir kitus rastus patikimus šaltinius. Netvirtink, kad portalas patikrintas, jeigu paieška jame nepavyko.
3. Ieškok dviem kalbomis: `logistikos vadovas`, `transporto skyriaus vadovas`, `ekspedicijos vadovas`, `tiekimo grandinės vadovas`, `pirkimų ir logistikos vadovas`, `importo vadovas`, `operations manager`, `head of logistics`, `supply chain manager`, `transport manager`, `warehouse operations manager`. Pradėk nuo tikslių pozicijų; ieškok papildomais sinonimais ir darbdavių puslapiuose, jeigu randi mažiau nei 5 patvirtintus skelbimus. Neatlaisvink vartotojo aiškiai nustatytų miestų, atlyginimo ar pareigų filtrų be leidimo.
4. Atverk **kiekvieną** individualų skelbimą, patikrink URL, darbdavį, pareigas, vietą, darbo formą, atlyginimo rūšį, paskelbimo ir galiojimo datas, kandidatavimo galimybę. Atlik konkretaus skelbimo būsenos klasifikaciją pagal [references/verification.md](references/verification.md). Tik „patvirtintai aktyvus“ skelbimas gali patekti į pagrindinę lentelę.
5. Aptikęs skirtinguose portaluose dubliuotus įrašus, sujunk pagal normalizuotą URL ir darbdavį + pareigas + vietą. Pirmenybę teik darbdavio galiojančiam individualiam puslapiui; šaltinių skirtumus pažymėk. Jei nėra kandidatuoti leidžiančio patvirtinimo, nevadink skelbimo aktyviu.
6. Pateik **atskiras** lenteles: (A) patvirtintai aktyvūs, (B) galbūt aktualūs, bet nepatvirtinti (ne daugiau kaip 5), tik jeigu jie naudingi. Pasibaigusius atmesk. Kiekvieno įrašo laukai: **Pareigos | Įmonė | Miestas / forma | Atlyginimas (bruto/neto/nenurodyta) | Paskelbta / galioja iki | Būsenos įrodymas | Tinkamumas | Tiesioginis URL**. Nenurodytas reikšmes vadink „nenurodyta“, nerašyk išgalvotų datų ir atlyginimų. Paieškos indeksavimo laikas nėra paskelbimo data.
7. Nurodyk realų patikrintų aktyvių skelbimų skaičių (pvz. 3 iš tikslinių 10), tikrinimo datą/laiką, ieškotus portalus, kokios prieigos / filtrų kliūtys buvo, ir kodėl kvota galbūt nepasiekta. Rekomenduok 2–3 prioritetinius kandidatus, aiškiai atskirdamas faktą nuo savo vertinimo.
8. Jei interneto arba individualių puslapių negali patikrinti, atvirai pranešk, kad **aktyvių skelbimų patvirtinti nepavyko**. Pateik paieškos užklausas arba portalo paieškos nuorodas, bet ne „aktyvių skelbimų“ imitaciją.
9. Be papildomo aiškaus vartotojo nurodymo nesiųsk paraiškų, CV ar žinučių. Laikykis portalų sąlygų; neapeidinėk CAPTCHA ir prisijungimo.

## Pagalbinis validatorius
Jei galima vykdyti Python, patikros būsenai ir dubliams naudok `scripts/validate_ads.py`; tai pagalbinė deterministinė biblioteka, **ne** autonominis naršymo ar tikro skelbimų aktyvumo įrodymo mechanizmas. Fakto `accepting_applications` ar `apply_action_visible` neįrašyk `True`, kol realiai nepatikrinai šaltinio.

## Testai
Paleisk `python -m unittest discover -s skills/darbo-skelbimai/evals -p "test_*.py" -v` iš repozitorijos šaknies. Vertinimo situacijos aprašytos [evals/evals.json](evals/evals.json). Statiniai / vienetiniai testai nėra realios web paieškos pakaitalas.
