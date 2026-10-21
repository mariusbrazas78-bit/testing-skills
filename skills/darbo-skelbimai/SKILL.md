---
name: darbo-skelbimai
description: Ieško ir tikrina aktualius darbo skelbimus Lietuvoje, ypač logistikos, transporto, importo/eksporto, tiekimo grandinės ir operacijų vadovų pozicijas. Naudok ieškant darbo, vadovaujančių pozicijų, naujų pasiūlymų ir atlyginimų; oficialiuose darbdavių karjeros puslapiuose patikrina portalų įrašus, atskiria aktyvius nuo nepatvirtintų.
---

# Darbo skelbimai (v3)

## Tikslas
Surask iki 10 tinkamų, **patvirtintai aktyvių** individualių skelbimų. Jei tiek nėra, pateik tik patikrintą skaičių ir paaiškink ribas. Numatytoji sritis – Lietuva, logistika, transportas, ekspedicija, importas/eksportas, tiekimo grandinė, operacijų valdymas.

## Procedūra
1. Užfiksuok paieškos datą/laiką Europe/Vilnius, vartotojo vietovės, pareigų, atlyginimo, darbo formos ribas. Aiškiai nurodytų ribų neatlaisvink.
2. Ieškok LT ir EN sinonimais per CVbankas, CV-Online, LinkedIn Jobs, Užimtumo tarnybą ir oficialias įmonių karjeros svetaines; šaltinių gairės – [references/sources.md](references/sources.md). Kai aktyvių mažiau kaip 5, plėsk **sinonimus ir šaltinius**, bet ne vartotojo filtrus.
3. Atverk kiekvieną individualų skelbimą ir patikrink pareigas, įmonę, vietą, atlyginimą (bruto/neto/nežinoma), paskelbimo/galiojimo datą ir kandidatavimo būseną. Paieškos ištrauka neįrodo aktyvumo.
4. **Nauja v3 taisyklė:** kiekvienam perspektyviam portalo skelbimui surask atitinkamos įmonės **oficialią karjeros svetainę** ir pabandyk rasti *tą pačią poziciją* pagal pavadinimą, padalinį ir miestą; vykdyk [references/employer-check.md](references/employer-check.md). Tikrink darbdavio individualų puslapį ir nurodytą kandidatavimo kelią; nenaviguok į CV pateikimą be atskiro vartotojo prašymo. Oficialios svetainės **pagrindinis puslapis** savaime nėra aktyvumo įrodymas.
5. Neteisingai nesusiek skirtingų skelbimų vien todėl, kad įmonė ir bendras pavadinimas panašūs. Palygink vietą, darbo turinį, skelbimo ID / nuorodą ir terminą. Esant neatitikimų, statusas „nepatvirtintas“.
6. Taikyk [references/verification.md](references/verification.md): **patvirtintai aktyvus** tik esant individualios pozicijos patikrai ir aiškiam paraiškų priėmimo patvirtinimui arba būsimam terminui su tikrai patikrintu kandidatavimo veiksmu. „Apply“ mygtuko vaizdas savaime nepakanka. Aiškus uždarymas / praėjęs terminas → pasibaigęs. Neprieinamas puslapis, prieštaringi signalai ar neaiški paraiškų būsena → nepatvirtintas.
7. Naudok `scripts/validate_ads.py` kaip neprivalomą deterministinį būsenų/dublių pagalbininką. Jis nesilanko svetainėse ir negali savarankiškai patvirtinti realaus kandidatavimo. Įrodymų laukus pildyk tik pagal realiai matomus šaltinius.
8. Šalink dublikatus pagal URL, įmonę, pareigas ir vietą, bet išsaugok **abi šaltinių nuorodas** (portalo ir darbdavio). Oficialų skelbimą pateik pirmiau, jei tai tikrai tas pats darbas.
9. Pateik dvi atskiras lenteles: A) patvirtintai aktyvūs; B) iki 5 nepatvirtintų, kuriuos verta pasitikrinti. Laukai: Pareigos | Įmonė | Miestas / darbo forma | Atlyginimas ir bruto/neto | Paskelbta / galioja iki | Būsenos įrodymas | Darbdavio nuoroda | Portalo nuoroda | Tinkamumas. Jei datos ar sumos trūksta, rašyk „nenurodyta“.
10. Nurodyk kiek skelbimų peržiūrėta, kiek aktyvių, nepatvirtintų ir pasibaigusių, kokios svetainės neprieinamos, ir 2–3 pagrįstus prioritetus. Jei oficialios svetainės patikra nepavyko, pažymėk tai tiesiai – **nespekuliuok**, kad tokio darbo įmonėje nėra.
11. Gerbk naudojimosi taisykles, prisijungimus ir CAPTCHA. Neišsiųsk CV ar paraiškos ir nesusisiek su darbdaviu be vartotojo leidimo.

## Testai
`python -m unittest discover -s skills/darbo-skelbimai/evals -p "test_*.py" -v`. Testų scenarijai: [evals/evals.json](evals/evals.json). Vietiniai testai netikrina tikro portalų pasiekiamumo.
