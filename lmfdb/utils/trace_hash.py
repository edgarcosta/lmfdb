# Sage translation of the Magma function TraceHash(), just for elliptic
# curves /Q and /NF

from sage.all import GF, ZZ, QQ, pari, prime_range

TH_C = [326490430436040986, 559705121321738418, 1027143540648291608, 1614463795034667624, 455689193399227776,
        812966537786397194, 2073755909783565705, 1309198521558998535, 486216762465058766, 1847926951704044964,
        2093254198748441889, 566490051061970630, 150232564538834691, 1356728749119613735, 987635478950895264,
        1799657824218406718, 1921416341351658148, 1827423174086145070, 1750068052304413179, 1335382038239683171,
        1126485543032891129, 2189612557070775619, 1588425437950725921, 1906114970148501816, 1748768066189739575,
        1105553649419536683, 41823880976068680, 2246893936121305098, 680675478232219153, 1096492737570930588,
        1064058600983463886, 2124681778445686677, 1153253523204927664, 1624949962307564146, 884760591894578064,
        722684359584774534, 469294503455959899, 1078657853083538250, 497558833647780143, 430880240537243608,
        1008306263808672160, 871262219757043849, 1895004365215350114, 553114791335573273, 928282405904509326,
        1298199971472090520, 1361509731647030069, 426420832006230709, 750020119738494463, 892950654076632414,
        1225464410814600612, 1911848480297925904, 842847261377168671, 836690411740782547, 36595684701041066,
        57074465600036538, 35391454785304773, 1027606372000412697, 858149375821293895, 1216392374703443454,
        59308853655414224, 1030486962058546718, 382910609159726501, 768789926722341438, 762735381378628682,
        1005758989771948074, 1657009501638647508, 1783661361016004740, 796798233969021059, 1658520847567437422,
        502975179223457818, 2063998821801160708, 2126598223478603304, 817551008849328795, 1793074162393397615,
        1287596263315727892, 1629305847068896729, 2282065591485919335, 1280388906297308209, 173159035165825250,
        1203194438340773505, 2146825320332825798, 847076010454532974, 2132606604399767971, 865350797130078274,
        421223214903942949, 2202859852828864983, 1627572340776304831, 1301036100621122535, 2151172683210770621,
        555918022010940381, 1195820575245311406, 2060813966122583132, 824196499832939747, 1252314214858834971,
        380498114208176064, 621869463771460120, 1487674193901485781, 1569074147090699661, 1723498454689514459,
        1489838779667276265, 607626788325788389, 93543108859195056, 1874271115035734974, 1456016012787031897,
        619764822731213939, 1812449603590865741, 808484663842074461, 2009697952400734786, 1525933978789885248,
        343887624789001682, 1182376379945660137, 1982314473921546769, 1109549848371395693, 1037594154159590924,
        1071053104849367160, 1322181949714913233, 1516660949039528341, 960526604699918173, 1729904691101240134,
        261117919934717464, 2271784899875479358, 756802274277310875, 1289220444092802136, 474369139841197116,
        1716815258254385285, 103716246685267192, 543779117105835462, 1645057139707767457, 895800586311529398,
        1255427590538696616, 152478208398822237, 59235267842928844, 1502771737122401274, 1149578551939377903,
        1470772656511184950, 1546086255370076952, 1723497785943073942, 778240149963762596, 240870114509877266,
        394305328258085500, 2102620516550230799, 1039820873553197464, 979798654654721830, 880027557663442629,
        1676981816531131145, 1802107305139241263, 1972433293052973713, 2107405063590590043, 1798917982073452520,
        1369268024301602286, 867033797562981667, 1038357135783187942, 758476292223849603, 1948092882600628075,
        2207529277533454374, 1821419918118374849, 1231889908299259230, 566310110224392380, 1609356725483962542,
        280378617804444931, 1072662998681271815, 116308709127642766, 1193169610307430309, 866966243748392804,
        166237193327216135, 1077013023941018041, 404884253921467160, 786088301434511589, 1383535122407493085,
        2280658829488325172, 101154688442168806, 186007322364504054, 132651484623670765, 2214024743056683473,
        2082072212962344576, 1527055902872993253, 914904768868572390, 828477094595207304, 1020679050708770534,
        482636846586846145, 1930865547754160712, 1593671129282272719, 1493198467868909485, 729902645271416500,
        275540268357558312, 164114802119030362, 788447619988896953, 1762740703670330645, 660855577878083177,
        1651988416921493024, 740652833177384429, 1112201596451006206, 415698847934834932, 1211582319647132127,
        1146510220721650373, 1849436445614060470, 2087092872652683432, 2118502348483502728, 1356524772912098481,
        1199384942357517449, 172551026757446140, 578031956729941707, 523340081847222890, 1076777027268874489,
        504399020033657060, 1278551106709414382, 2159465951497451565, 1178157191616537256, 204263226455195995,
        1056341819781968292, 183521353142147658, 2188450004032853736, 815413180157425263, 1872285744226329343,
        959184959959358956, 473007083155872003, 655761716995053547, 1131460430873190185, 2139124645518872072,
        511733859594496686, 15198510254334311, 1224323599606986326, 717867206610437778, 2091512354759023324,
        372342232752868676, 1361511712413436237, 1389190973283340505, 394349220142131124, 2079377585202309849,
        353365880305796299, 2032166139485738617, 1890917131797951728, 242865361432353437, 1418792507475867019,
        2119099350463010017, 1014188227490285243, 479492624224518275, 1303029569429482669, 517247294593876834,
        1554557044656123283, 750281115903727536, 2167122262389919937, 760554688782332821, 2023636030598854916,
        1790146557619247357, 386163722563943194, 1515274606763521578, 2204179368292080266, 964158696771121369,
        303439105863023359, 8182230548124380, 1750434984088519049, 1725590414598766182, 1265114980378421064,
        1015227773830014864, 229929992560423398, 764214183816115409, 538352539450824188, 1941773060895353999,
        1068434172733967371, 1355790773646160387, 459324502245141234, 609129328626229402, 1241119177010491262,
        1783576433920437207, 1523680846139002895, 882824005398680507, 413096479776864968, 522865969927243974,
        1858351603281690756, 1968585526421383793, 2178118415854385403, 2071714574011626742, 2075065799199309684,
        2276241901353008033, 303400925906664587, 1426227202230524239, 1930606302598963877, 249953308414640146,
        611228839507773914, 1672745442514341102, 467604306000306674, 1474554813214382459, 1601661712875312382,
        614840167992924737, 1228071177654928913, 527816710270111610, 2217787042387174521, 639805394326521740,
        222549283662427192, 1360905187147121266, 2218130040969485290, 1295851844663939225, 563784543912533038,
        1995338666855533310, 1570565903061390324, 1421390998286027062, 1394318358097125191, 1259069656723159936,
        782274544912671248, 727119931274242152, 461373271832281770, 431218333850664873, 1192819027123234430,
        2078764559709872649, 185598300798682005, 753027393642717163, 39457098005678485, 1334017905593361063,
        2208208003949042369, 995759906937041788, 1045940157364976040, 194824647782216037, 550631184874398695,
        1360200364068800381, 1357865448826768161, 1831861326200370539, 942093021910086667, 1640270910790040055,
        186615109286328085, 1330440696074470319, 499018273810238035, 502274974614414055, 1207335215870481547,
        2013999866627689866, 1419916425046140717, 191559056573160841, 1328802988676857752, 1405960078185023606,
        227507798797399340, 1637526486952132401, 1076968863810265335, 944510191997220613, 1301386330701215932,
        285779824044017183, 1429750858521890899, 1618865668058420542, 841779507635076338, 2271885690336656780,
        1950830875641497149, 2020789551919109899, 975546679421148460, 1197104163269028491, 1270315990156796392,
        748604252817308486, 816129261753596233, 384118410847738091, 2113266006559319391, 1338854039375748358,
        1361143499198430117, 633423014922436774, 1290791779633361737, 81273616335831288, 734007502359373790,
        1803343551649794557, 178160046107106100, 1669700173018758407, 1829836142710185153, 1253431308749847288,
        70019619094993502, 939065521645602191, 571602252457140250, 26887212485499413, 984459396949257361,
        852773633209386873, 2289526104158020696, 756333221468239349, 478223842701987702, 2004947225028724200,
        526770890233938212, 1661268713623636486, 1595033927594418161, 1532663022957125952, 364955822302609296,
        603258635519191127, 371859597962583054, 94282227629658712, 2160611809915747887, 27000232625437140,
        22687777651226933, 734430233276692626, 1127699960534747774, 346857527391478939, 399588948728484631,
        1369575405845760568, 2217803687757289581, 2206814713288610370, 130141496340768529, 861110681132541840,
        230850531138610791, 1780590839341524422, 1923534983071749673, 1055631719355441015, 1222514615506258219,
        937915311769343786, 852868812961957254, 718656592041199719, 2250542267067365785, 2169537354592688250,
        1568074419444165342, 853778925104674827, 105031681250262217, 1204393036537417656, 592755100672600484,
        1509207668054427766, 1409630039748867615, 433329873945170157, 168130078420452894, 701434349299435396,
        1736119639406860361, 1801042332324036889, 82826810621030003, 581092394588713697, 1513323039712657034,
        2086339870071049553, 512802587457892537, 1294754943443095033, 1486581673100914879, 930909063370627411,
        2280060915913643774, 219424962331973086, 118156503193461485, 743557822870685069, 1997655344719642813,
        393161419260218815, 1086985962035808335, 2119375969747368461, 1650489163325525904, 1967094695603069467,
        916149623124228391, 1122737829960120900, 144869810337397940, 2261458899736343261, 1226838560319847571,
        897743852062682980, 45750188043851908, 1858576614171946931, 1568041120172266851, 289541060457747472,
        1539585379217609033, 866887122666596526, 6060188892447452, 1707684831658632807, 1062812350167057257,
        887626467969935688, 1968363468003847982, 2169897168216456361, 217716763626832970, 413611451367326769,
        336255814660537144, 1464084696245397914, 1902174501258288151, 1440415903059217441, 302153101507069755,
        1558366710940453537, 717776382684618355, 1206381076465295510, 1308718247292688437, 555835170043458452,
        1029518900794643490, 1034197980057311552, 131258234416495689, 260799345029896943]

TH_P = prime_range(2**12, 2**13)
TH_F = GF(2**61 - 1)


def TraceHash_from_ap(aplist):
    r"""Return the trace hash of this list of ap, indexed by the primes in TH_P
    """
    return ZZ(sum([TH_F(a * c) for a, c in zip(aplist, TH_C)]))


TH_P_cache = {}


def TraceHash(E):
    r"""Return the trace hash of this elliptic curve defined over either
    QQ or a number field.

    """
    K = E.base_field()
    if K == QQ:
        E_pari = pari(E.a_invariants()).ellinit()
        return TraceHash_from_ap([E_pari.ellap(p) for p in TH_P])

    if K not in TH_P_cache:
        TH_P_cache[K] = dict(
            [(p, [P for P in K.primes_above(p) if P.norm() == p]) for p in TH_P])

    def ap(p):
        return sum([E.reduction(P).trace_of_frobenius()
                    for P in TH_P_cache[K][p]], 0)

    return TraceHash_from_ap([ap(p) for p in TH_P])


# Dictionary to hold the trace hashes of isogeny classes by label.  We
# store the trace hash for every curve but isogenous curves have the
# same hash.  (So do Galois conjugates, but we do not take advantage
# of that).
TH_dict = {}


def TraceHashClass(iso, E):
    r"""Return the trace hash of this elliptic curve defined over either QQ
    or a number field, given also the label of its isogeny class.
    Hash values are cached.

    For curves over number fields the iso label should include the
    field label.
    """
    global TH_dict
    if iso in TH_dict:
        return TH_dict[iso]
    else:
        th = TH_dict[iso] = TraceHash(E)
        return th
