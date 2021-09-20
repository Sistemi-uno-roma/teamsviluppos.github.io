s = """
https://s1r.it/servizi/ 0   2021-06-07 13:29 +00:00
https://s1r.it/implementazioni-esolver/ 0   2021-06-07 16:40 +00:00
https://s1r.it/servizi/formazione/  0   2021-06-11 15:27 +00:00
https://s1r.it/settori/ 0   2021-06-11 15:28 +00:00
https://s1r.it/soluzioni/   0   2021-06-11 15:29 +00:00
https://s1r.it/servizi/sviluppo-software/ecommerce/ 0   2021-06-15 11:39 +00:00
https://s1r.it/servizi/sviluppo-software/siti-vetrina/  0   2021-06-15 11:40 +00:00
https://s1r.it/servizi/sviluppo-software/e-learning/    0   2021-06-15 11:41 +00:00
https://s1r.it/servizi/sviluppo-software/   0   2021-06-15 11:42 +00:00
https://s1r.it/servizi/sviluppo-software/soluzioni-personalizzate/  0   2021-06-15 11:44 +00:00
https://s1r.it/servizi/sviluppo-software/sviluppo-web/  0   2021-06-15 11:45 +00:00
https://s1r.it/servizi/sviluppo-software/saas/  0   2021-06-15 11:45 +00:00
https://s1r.it/servizi/sviluppo-software/machine-learning/  0   2021-06-15 11:46 +00:00
https://s1r.it/servizi/marketing/   0   2021-06-15 11:48 +00:00
https://s1r.it/servizi/marketing/seo/   0   2021-06-15 11:53 +00:00
https://s1r.it/servizi/software-sistemi/profis/ 0   2021-06-15 12:15 +00:00
https://s1r.it/servizi/software-sistemi/profis-revisione/   0   2021-06-15 12:17 +00:00
https://s1r.it/servizi/software-sistemi/studio/ 0   2021-06-15 12:17 +00:00
https://s1r.it/servizi/software-sistemi/job/    0   2021-06-15 12:18 +00:00
https://s1r.it/servizi/software-sistemi/job-paghe/  0   2021-06-15 12:18 +00:00
https://s1r.it/servizi/software-sistemi/job-risorse/    0   2021-06-15 12:18 +00:00
https://s1r.it/servizi/software-sistemi/job-presenze/   0   2021-06-15 12:35 +00:00
https://s1r.it/servizi/software-sistemi/sportello-cloud/    0   2021-06-15 12:36 +00:00
https://s1r.it/servizi/software-sistemi/enologia/   0   2021-06-15 12:37 +00:00
https://s1r.it/servizi/software-sistemi/integrazioni-personalizzate-esolver/    0   2021-06-15 12:37 +00:00
https://s1r.it/servizi/formazione/corsi-per-grafici/    0   2021-06-15 12:38 +00:00
https://s1r.it/servizi/formazione/corsi-sistemi/    0   2021-06-15 12:41 +00:00
https://s1r.it/settori/imprese-di-produzione/   0   2021-06-15 12:45 +00:00
https://s1r.it/imprese-di-distribuzione/    0   2021-06-15 12:46 +00:00
https://s1r.it/settori/imprese-di-servizi/  0   2021-06-15 12:46 +00:00
https://s1r.it/settori/associazione/    0   2021-06-15 12:47 +00:00
https://s1r.it/settori/microimpresa/    0   2021-06-15 12:47 +00:00
https://s1r.it/soluzioni/processo-di-digitalizzazione/  0   2021-06-15 12:48 +00:00
https://s1r.it/soluzioni/software-gestionale-di-studio/ 0   2021-06-15 12:49 +00:00
https://s1r.it/servizi/software-sistemi/    1   2021-06-15 13:00 +00:00
https://s1r.it/settori/commercialisti/  4   2021-06-16 15:17 +00:00
https://s1r.it/settori/consulenti-del-lavoro/   2   2021-06-16 16:19 +00:00
https://s1r.it/servizi/software-sistemi/documenti-web/  0   2021-07-13 08:29 +00:00
https://s1r.it/servizi/software-sistemi/esolver/    1   2021-07-13 09:26 +00:00
https://s1r.it/soluzioni/software-erp/  0   2021-07-13 09:33 +00:00
https://s1r.it/servizi/software-sistemi/profis-az/  1   2021-07-13 09:54 +00:00
https://s1r.it/servizi/grafica/brand-design/    0   2021-09-02 10:23 +00:00
https://s1r.it/servizi/grafica/product-design/  0   2021-09-02 13:31 +00:00
https://s1r.it/servizi/grafica/web-design/  4   2021-09-02 13:47 +00:00
https://s1r.it/servizi/grafica/ 1   2021-09-02 13:49 +00:00
https://s1r.it/servizi/grafica/editoria/    2   2021-09-02 13:50 +00:00
https://s1r.it/configuratore-web-3d/    1   2021-09-08 09:54 +00:00
"""
for line in s.splitlines():
    if line.strip() != "":
        line = line.split(" ")[0]
        line = line.replace("https://s1r.it", "")
        fname = line.replace("/", "")
        #print(fname)
        title = line.split("/")[-2]
        if "-" in title:
            title = title.replace("-", " ")
        with open("_pages/" + fname + ".md", 'w') as f:
            data = f"""---
title : "{title}"
layout : single
permalink : {line}
author_profile : false
---
"""
            f.write(data)


