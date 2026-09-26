Testausasiat ovat vielä melko alussa. Poetryyn törmäsin tällä kurssilla ensimmäistä kertaa, samoin yksikkötestaukseen.

Kattavuusraportti sanoo tällä hetkellä:
Name              Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------
src/analyser.py      98     55     26      6    44%   15-27, 37-38, 50-66, 71-74, 77-78, 81-88, 93->95, 98->101, 102, 106, 109-116, 119-120
-------------------------------------------------------------
TOTAL                98     55     26      6    44%

Kattavuus on 44%, vaikka yksikkötesteillä testataan vain kahta metodia ja niitäkin melko pintapuolisesti. 

Empiirisiä testejä on tehty niin, että on tutkittu ääninäytettä Audacityn Analyze->Plot spectrum -toiminnolla ja tsekattu, että käppyrästä tulee samannäköinen ja samat huipputaajuudet löytyvät.

Eli: on tehty vasta kahden metodin yksikkötestit, molemmat hyvin simppeleitä, ja lisää tehdään ensi tiistain testausluennon jälkeen paremmalla osaamisella.


