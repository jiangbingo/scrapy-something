
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import random


def getPara(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    paraData = str(soup.find("script", type="text/javascript")).split()
    ckHtml = paraData[5].split("&CK=")[1].split('"')[0]
    print ckHtml
    ck = ckHtml[0:8] + ckHtml[12] + \
        ckHtml[8:13] + ckHtml[14:]
    print ck
    rkHtml = paraData[-2].split(",")[0].split("+")[1][1:-1]
    print rkHtml
    rkNum = random.random() * 10
    print rkNum
    rk = str(("%.15f") % rkNum) + rkHtml
    print rk
    r = paraData[-2].split(",")[1].split(")")[0][1:-1]
    print r
    return ck, rk, r


def getTrip(url, startCity, endCity, date, ck, rk, r):
    dataURL = "http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=%s&ACity1=%s&SearchType=S&DDate1=%s&IsNearAirportRecommond=0&rk=%s&CK=%s&r=%s" % (
        startCity, endCity, date, rk, ck, r)
    print dataURL
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
        "Host": "flights.ctrip.com",
        "Referer": url
    }
    req = requests.get(dataURL, headers=headers)
    flights = req.json()["fis"]
    for i in flights:
        print "flight NO.: " + i["fn"], "travel time: " + i["dt"], "arrived time: " + i["at"], "price:",
        for j in i["scs"]:
            print j["p"],
        print

    print "query flight count: ", len(flights)

if __name__ == '__main__':
    date = "2016-08-20"
    startCity = "hgh"
    endCity = "wuh"

    url = "http://flights.ctrip.com/booking/%s-%s-day-1.html?DDate1=%s" % (
        startCity, endCity, date)
    print url
    ck, rk, r = getPara(url)
    getTrip(url, startCity, endCity, date, ck, rk, r)
