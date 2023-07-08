
##### 랜선자르기(결정알고리즘)

def cnt_line(x):
    cnt = 0
    for i in inp:
        cnt += i // x
    return cnt

def solution():
    answer = 0

    lt = 0
    rt = max(inp)
    res = 0

    while lt <= rt :
        mid = (lt+rt)//2
        print(lt, mid, rt, cnt_line(mid) )
        if cnt_line(mid) >= N: # 갯수가 같거나 많다
            res = mid
            lt = mid+1  # 점점 늘여 나감

        else :  # 갯수가 적다면, 길이를 줄여야 함
            rt = mid-1
    print(res)
    return answer

'''
풀이 설명 듣고 품
'''

K = 4
N = 11

inp = [802,743,457,539]
re = solution()
print(re)
#=> 200


K = 800
N = 100000

inp = [1028865,8530049,6936961,6325505,6647041,9376129,5338753,9225857,8487425,3544449,1172609,2299905,3136129,786945,5588353,7905153,6580865,676353,9489665,9607297,7292033,6817409,7135233,8399105,4086017,7655169,8952193,8963457,946177,9876993,8004225,5475969,9502593,7382657,8450305,7419265,7015041,3942529,5502593,6765057,4137857,526209,7780865,9892481,6294017,8475137,1854209,350209,9634689,6021889,404865,1027073,312961,2468609,9473025,338177,4896385,7573377,2528257,7557377,1478657,3726721,9716353,5808641,9708929,1310977,3473921,6556673,8512257,7649409,3584513,8571265,6797057,8909057,8406017,2965121,9239297,5153793,3055873,3734273,4122753,2630529,8767489,9961601,830465,8111489,9040769,3326593,6908417,5764097,9873409,4335617,6431745,8233089,2749441,3255681,5132033,7930625,1512193,4310017,4278017,7440001,1162113,9740929,8964609,2840449,4182529,2265473,9061121,7010817,6077313,8329089,367361,3697921,4727425,5079553,7531009,8982145,3094401,1716993,3332737,5860353,5218433,6982273,6023681,1487745,7051009,3832577,4157825,8599169,2003969,3636993,9705857,6843265,4714753,7690241,4463745,4017025,3597441,4864897,6557697,4008705,8864129,3213697,8723585,1128705,7176321,4951297,6519169,251137,6242305,3636609,6056193,1298561,1470465,5632257,5374465,5356801,3859585,3456513,5401473,3350273,5744641,11649,5353217,5449857,3270913,7515649,3343233,5262465,1461505,5252865,3818241,3528065,4656769,1241729,9579265,733185,9940353,5729153,7674113,3478273,642049,7245441,9547521,8129921,5311105,4260609,2284289,3993473,6831745,3077505,3474305,7283329,8496769,5100673,2937345,268417,8408193,6633345,6909953,2015233,5134593,9275265,4157313,8080513,1466369,2717697,5838593,9383297,3136641,2176129,5940481,157825,3451265,637953,3177217,6147329,5905665,4162177,6873089,4329473,3562497,7387265,8216961,8013953,3506561,1960065,9306625,1020673,6638721,139777,179841,4648193,587393,8905217,3373185,4981121,9918721,4171521,5209217,9049217,5689601,477313,2390145,9267713,5602049,748673,5155841,2627329,7484929,602881,8133761,9390849,1384705,1110401,498945,8092289,1438337,2223745,9952897,8522625,6990977,6676609,5718017,7374337,2728961,9955841,4845953,7966977,541313,7198593,693633,5475713,1458177,5395713,1967745,2236673,6702849,672129,1144833,6006401,5472385,2426753,3800961,9654529,4053249,8873089,6419073,1359489,8120193,7722241,1560705,8623105,944257,6372993,4831361,1693697,8820865,6982145,3148417,676865,7767297,9652609,6323201,4342017,6784897,9309057,4552449,624513,8911233,7277313,3031041,3626625,7742337,9867009,3994625,4503041,2839425,7883521,588673,9140225,6798337,7573121,3462017,9752833,5076225,7870593,3728513,4401153,1190273,764545,6562433,8105985,8382337,4256129,2452993,2618369,1786881,8369665,6248833,9667329,8126593,1207809,8992257,6506369,9783809,9218433,3965825,8220673,1399809,7899009,5364737,1501057,6977153,1090561,4923265,2695041,8415361,2524033,40065,7127809,840577,8341633,5918977,2602241,6721281,6411905,9503617,8500353,2872193,7373313,9452417,8343041,6572033,5590913,8464513,4405761,2052993,8263425,1383681,91649,7231105,8513025,5391361,3574017,3062785,6199425,8952705,3364097,9957377,1491329,6265601,6406401,6422657,9202817,2114561,9160833,9700865,6424449,248193,5216385,6416129,8697729,4075137,4338561,3823233,7328385,2109185,3310465,3682433,4653313,241025,6949377,3989889,5773825,4152705,1683841,3399681,2115585,1009409,6383361,1279873,6127105,1261185,7740929,2714497,5419521,7107329,5195137,9041281,823681,2590977,8478465,6244865,913281,9963393,9213697,4554113,772865,3104129,3078913,8902913,941057,5723393,3012609,2947457,3049473,1423873,2122497,2459521,1829505,1650817,7568897,8862209,7589377,6235393,1471489,4461313,2804865,568321,4311169,7917441,8721409,3145217,3965825,1250049,106753,5836417,1979137,2180481,1535233,5885313,4631169,3137921,2392705,5499905,7696641,7825921,6289921,8139905,3731073,9746689,9556993,2659713,4060417,1765633,941825,3786113,8003713,2830337,5848321,8263041,2795137,664193,356609,8491393,1132289,1581569,1172225,1507841,7772673,5118081,6550017,3565057,2825729,4294529,1593985,9788801,7736577,6089217,5219713,7817729,9158017,4700033,804865,753409,5481345,8985857,3698945,8962049,2743297,3759489,1621249,1088001,7994881,7841793,4939393,8984577,5722625,1098369,196481,3115009,4412289,9233537,5169921,6837505,4873601,4054401,6294529,3808385,3707649,5135745,9497857,6425089,7146113,4373121,2239873,5231105,6455041,2067713,858881,6811905,2321281,899585,871297,9808641,6098305,3817857,2610433,2496257,866945,2401153,2008065,9311617,810369,6684417,4263937,5105921,8051329,390145,338305,8936833,4926849,8785921,2590721,2446209,4085633,4528513,1885185,5326465,9055745,1330689,3645185,9835265,4659713,254081,3153409,5255937,7067905,5410817,2579841,1897857,8666497,5607041,8984705,7460481,4850433,3435649,5701121,6613633,7151873,4950657,3925761,5490689,5612929,4405377,6706433,1848833,6301313,9637889,8956673,7822337,4164993,8221313,7023233,9306241,3906049,5473793,6797185,9519105,8317057,6955521,1344769,3737089,4702209,7124097,7180417,6280833,9121153,5255553,3899649,3214721,9419009,9450369,4675457,8622721,1406593,3265409,8987649,1891713,2601473,5398273,1379201,8210561,3922561,5608193,2380417,7855489,4174977,2529409,5001089,9621761,6000897,6561409,8017025,5950977,2202497,7069441,7714689,5586305,1440513,4432769,3244929,6861569,2162049,8087297,2755073,6002049,301185,9120897,1642497,6026241,1859969,1379585,9659649,9532161,4144513,8679681,3358337,6724353,3355777,8715265,4902017,6493185,7532801,3596033,352001,1345409,3203073,8043777,6739841,4030593,7011841,6833921,5573249,6891905,3850241,9993985,5848705,1588737,1679233,5595649,1879169,7769345,4110593,8311681,562945,7278977,2036097,304385,2504321,2219777,5628673,198657,7182081,2124289,9133441,6103297,9977857,4017281,4575873,3906049,244353,5300225,7362177,841985,5270017,7840001,4309249,3110273,349441,4342913,6017665,219137,8163969,8056065,8194433,5698945,4530433,1975681,3380609,9412481,3525505,1874049,5108353,6659201,8945409,3636993,699777,4676225,3424513,4387201,4582017,1064321,9413249,5434241,7694849,9840001,495233,1559937,2008321,1666945,199553,6999169,2600705,422529,5090433,6661505,9243521,2980225,3261569,5372289,285057,1356161,1551105,8252289,6007809,8006017,7230593,9313153,9677953,3715201,996481,5261057,2609793,2152065,300545,6893697,3278721,4792833,5634305,7454977,4256769,4796545,6792193,2161153,2101889,3702529,7481345]
re = solution()
print(re)
#=> 40198

