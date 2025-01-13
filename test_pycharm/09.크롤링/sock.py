import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
google_ip = socket.gethostbyname("google.com")
sock.connect((google_ip, 80))

sock.send("GET / HTTP/1.1\n".encode())
sock.send("\n".encode())

buffer = sock.recv(4096)
buffer = buffer.decode().replace("\r\n", '\n')
sock.close()

print(buffer)

'''
HTTP/1.1 200 OK
Date: Tue, 14 Dec 2021 07:03:26 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2021-12-14-07; expires=Thu, 13-Jan-2022 07:03:26 GMT; path=/; domain=.google.com; Secure
Set-Cookie: NID=511=rFE4edql-B6XDUM1JXiEnjZIB7fKcXaGEf9zdh02T1OlbK_PrFt04g5jXIkE5cNDql379wmFwh9qHbnq0grZ3o7xOryTtU9Cy_BJWukrxAplOrouuIcMpt4REyhXVQA9HPzI3-_aEeE9XF1IokvjezzZOWBCoXCTK-UFs7esojM; expires=Wed, 15-Jun-2022 07:03:26 GMT; path=/; domain=.google.com; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

42c3
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/logos/doodles/2021/seasonal-holidays-2021-6753651837109324-6752733080595605-cst.gif" itemprop="image"><meta content="2021 &#50672;&#47568;&#50672;&#49884;" property="twitter:title"><meta content="&#46384;&#46907;&#54620; &#50672;&#47568; &#48372;&#45236;&#49464;&#50836; #GoogleDoodle" property="twitter:description"><meta content="&#46384;&#46907;&#54620; &#50672;&#47568; &#48372;&#45236;&#49464;&#50836; #GoogleDoodle" property="og:description"><meta content="summary_large_image" property="twitter:card"><meta content="@GoogleDoodles" property="twitter:site"><meta content="https://www.google.com/logos/doodles/2021/seasonal-holidays-2021-6753651837109324-2xa.gif" property="twitter:image"><meta content="https://www.google.com/logos/doodles/2021/seasonal-holidays-2021-6753651837109324-2xa.gif" property="og:image"><meta content="1000" property="og:image:width"><meta content="400" property="og:image:height"><meta content="https://www.google.com/logos/doodles/2021/seasonal-holidays-2021-6753651837109324-2xa.gif" property="og:url"><meta content="video.other" property="og:type"><title>Google</title><script nonce="YBRQC0IfwlplzWUheopoHw==">(function(){window.google={kEI:'vkG4Yd-mN4LM-QbI_6aYBw',kEXPI:'0,1302536,56873,1709,4350,206,4804,921,1395,383,246,5,1354,4013,1237,2946,1119570,1197787,598,16,380089,16115,28684,17572,4858,1362,9290,3023,17586,4020,978,13228,3847,4192,6430,21822,920,5080,1593,1279,2212,530,149,561,542,840,6297,3514,606,2023,1733,43,521,14670,2273,1,955,2843,7,5599,6755,5096,15768,552,908,2,941,2614,3783,9359,3,346,230,6460,148,13975,4,1528,2304,6463,576,4684,15625,4764,2658,6701,656,30,13628,1593,712,2132,16786,651,5170,2536,4094,3138,6,908,3,3541,1,16524,283,912,5996,14655,3784,2,14022,1931,3909,409,1271,743,5853,8874,447,1142,537,2,621,4192,2508,2378,2721,2985,15311,2,6,6956,32,730,4569,2577,1348,1784,546,6635,91,3775,2,237,7346,545,4102,688,1252,13669,1375,2052,601,3106,1554,1361,1417,19,2751,258,1358,291,2

'''
