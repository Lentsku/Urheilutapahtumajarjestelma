# Urheilutapahtumajärjestelmä

Tehtävänä on tehdä urheilutapahtumajärjestelmä tapahtumien, tapahtumiin osallistujien ja osallistujien tulosten hallintaan. Erilaisia tapahtumia ovat hiihto, pyöräily, soutu ja hölkkä. Osallistujat ilmoittautuvat tapahtumien sarjoihin, esimerkiksi lyhyeen, normaalin tai pitkän matkan pyöräilyyn. Osallistuja voi myös halutessaan ilmoittautua useampaan sarjaan samassa tapahtumassa.

Osallistujista tallennetaan etunimi, sukunimi, sähköposti, puhelinnumero, postinumero, postitoimipaikka, suoritukset ja osallistumiset.
Jokaiselle osallistujalle arvotaan jokaisen tapahtuman kohdalla uniikki kilpailunumero, mutta soudussa on muista tapahtumista poiketen joukkueet, joten kaikilla samassa veneessä olevilla osallistujilla on yhteinen kilpailunumero.

Tapahtumasarjoista tulisi tallentaa sarjan nimi, tapahtuman nimi, päivämäärä, lähtöaika ja matka. Myös väliaikoja ja väliaikapaikkojen etäisyyksiä lähtöpaikasta tulisi voida tallentaa. Maali olisi väliaikapaikan erityistapaus.

Osallistujista tulisi myös tarjota tulostietoja, esimerkiksi osallistujan lähtöaika, väliajat, maaliintuloaika, tulosaika, sijoitus ja luonnollisesti mahdollisuudet näiden tietojen lisäämiseen tai muokkaamiseen tapahtuman aikana. Osallistujista tarjotaan myös historiatietoja, kuten hiihto, pyöräily, soutu ja hölkkäkerrat, osallistumiskerrat, "kierrosten" määrä, joita saa yhden aina kun on osallistunut kaikkiin neljään tapahtumaan samana vuonna.

Lähtökohtaisesti koko sovelluksen käyttäminen tulisi olla mahdollista vain henkilökunnan tunnuksilla. Jatkokehityksessä voitaisiin osallistujille tarjota kirjautumismahdollisuus, joilla katsoa ja muokata omia tietojaan ja nähdä omat tulokset ja suoritushistorian.

Toiminnot:
- Osallistujien tietojen lisääminen, muokkaaminen, poistaminen ja tarkistaminen
- Osallistujien osallistumisen lisääminen, muokkaaminen, poistaminen ja tarkistaminen
- Osallistujien tulostietojen lisääminen, muokkaaminen ja tarkistaminen
- Pääsy sovellukseen vain tapahtuman henkilökunnan tunnuksilla kirjautumalla

## Linkit

* [Sovellus Herokussa](https://urheilutapahtumajarjestelma.herokuapp.com/)
* [Tietokantakaavio](https://github.com/Lentsku/Urheilutapahtumajarjestelma/blob/master/documentation/Tapahtumakaavio.png)
* [User storyt](https://github.com/Lentsku/Urheilutapahtumajarjestelma/blob/master/documentation/userstory.md)

### Projektin branchit

* [Master branch](https://github.com/Lentsku/Urheilutapahtumajarjestelma/tree/master)
* [Työn alla](https://github.com/Lentsku/Urheilutapahtumajarjestelma/tree/tyonAlla)
* [Materiaalin todoapp](https://github.com/Lentsku/Urheilutapahtumajarjestelma/tree/todoapp)
