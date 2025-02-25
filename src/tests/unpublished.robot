*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add One Unpublished
    Input  lisää viite
    Input  ihmisluettava
    Add Reference  julkaisematon  Matti15  julkaisematon  Matti Meikäläinen  2015  Parasjulkaisu
    Input  poistu
    Run App
    Output Should Contain  Lisätään Matti Meikäläinen. 2015. julkaisematon. Parasjulkaisu.

Add Bibtex Unpublished
    Input  lisää viite
    Input  bibtex
    Input  @unpublished{citekey, author = "kirjailija", title = "julkaisematon", note = "huono", year = ""}
    Input  poistu
    Run App
    Output Should Contain  BibTex tiedoston kirjoittaminen onnistui

List Unpublished
    Input  lisää viite
    Input  ihmisluettava
    Add Reference  julkaisematon  Matti16  julkaisematon  Matti Meikäläinen  2016  Parasjulkaisu
    Input  listaa viitteet
    Input  lisäysjärjestys
    Input  poistu
    Run App
    Output Should Contain  Matti Meikäläinen. 2016. julkaisematon. Parasjulkaisu.