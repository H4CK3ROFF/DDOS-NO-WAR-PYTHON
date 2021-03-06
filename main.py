import requests
import threading

def main():
    links = [   "https://www.gazprom.ru/",
                "https://lukoil.ru/",
                "https://magnit.ru/",
                "https://www.nornickel.com/",
                "https://www.surgutneftegas.ru/",
                "https://www.tatneft.ru/",
                "https://www.evraz.com/ru",
                "https://nlmk.com/",
                "https://www.sibur.ru/",
                "https://www.severstal.com/",
                "https://www.metalloinvest.com/",
                "https://nangs.org/",
                "https://rmk-group.ru/ru",
                "https://www.tmk-group.ru/",
                "https://ya.ru/",
                "https://www.polymetalinternational.com/ru",
                "https://www.uralkali.com/ru",
                "https://www.eurosib.ru/",
                "https://omk.ru/",
                "https://www.sberbank.ru/",
                "https://www.vtb.ru/",
                "https://www.gazprombank.ru/",
                "https://www.gosuslugi.ru/",
                "https://www.mos.ru/uslugi/",
                "http://kremlin.ru/",
                "http://government.ru/",
                "https://mil.ru/",
                "https://www.nalog.gov.ru/",
                "https://customs.gov.ru/",
                "https://pfr.gov.ru/",
                "https://rkn.gov.ru/",
                "https://mail.rkn.gov.ru/",
                "https://cloud.rkn.gov.ru/",
                "https://mvd.gov.ru/",
                "https://pwd.wto.economy.gov.ru/",
                "https://stroi.gov.ru/",
                "https://proverki.gov.ru/",
                "https://ria.ru/",
                "https://gazeta.ru/",
                "https://kp.ru/",
                "https://riafan.ru/",
                "https://pikabu.ru/",
                "https://kommersant.ru/",
                "https://mk.ru/",
                "https://yaplakal.com/",
                "https://rbc.ru/",
                "https://bezformata.com/",
                "https://shop-rt.com/",
                "http://belta.by/",
                "https://sputnik.by/",
                "https://www.tvr.by/",
                "https://www.sb.by/",
                "https://belmarket.by/",
                "https://www.belarus.by/",
                "https://belarus24.by/",
                "https://ont.by/",
                "https://www.024.by/",
                "https://www.belnovosti.by/",
                "https://mogilevnews.by/",
                "https://www.mil.by/",
                "https://yandex.by/",
                "https://www.slonves.by/",
                "http://www.ctv.by/",
                "https://radiobelarus.by/",
                "https://radiusfm.by/",
                "https://alfaradio.by/",
                "https://radiomir.by/",
                "https://radiostalica.by/",
                "https://radiobrestfm.by/",
                "https://www.tvrmogilev.by/",
                "https://minsknews.by/",
                "https://zarya.by/",
                "https://grodnonews.by/",
                "https://rec.gov.by/ru",
                "https://www.mil.by/",
                "http://www.government.by/",
                "https://president.gov.by/ru",
                "https://www.mvd.gov.by/ru",
                "http://www.kgb.by/ru/",
                "http://www.prokuratura.gov.by/",
                "http://www.nbrb.by/",
                "https://belarusbank.by/",
                "https://brrb.by/",
                "https://www.belapb.by/",
                "https://bankdabrabyt.by/",
                "https://belinvestbank.by/individual",
                "https://bgp.by/ru/",
                "https://www.belneftekhim.by/",
                "http://belres.by/ru/",
                "https://www.energo.by/",
                "http://www.bellegprom.by/",
                "http://mininform.gov.by/",
    ]
    while True:
        for link in links:
            try:
                threading.Thread(target=tryRequest, args=(link,)).start()
            except:
                print("Thread Error")




def tryRequest(link):
    try:
        result = requests.get(link)
        if result:
            print("Site: "+ link + " Response OK\n")
        else:
            print("Site: "+ link + " Response Failed\n")
    except Exception as ex:
        print("Site: "+ link +  " Exception Error\n")



if __name__ == "__main__":
    main()
