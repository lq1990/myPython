
import matplotlib.pyplot as plt
import numpy as np

# data[i] = 10 * Math.sin(2 * Math.PI * 7 * t) + 5 * Math.cos(2 * Math.PI * 20 * t) + 2 * Math.cos(2 * Math.PI * 35 * t);


# w len: 21, sumW: 0.9959154807647799


# ===== origin
dataTime = np.array(
[7.0, 4.6273073829405185, 3.042013467133261, 7.542859672001882, 9.749923490411728, 13.090169943749475, 7.980655701641791, -5.319292809171913, -7.108296509971623, -4.5690307977544276, -6.510565162951535, -7.200491536685098, -11.870330238144987, -11.305465954255009, 1.9097866249815936, 8.090169943749485, 6.77252204241173, 7.154792919598085, 5.317148323658091, 9.132581267728419, 12.877852522924734, 2.2433276131470583, -7.150017832273187, -8.517211836771324, -9.121219541535343, -5.000000000000008, -5.8851515640355565, -12.321437901951938, -5.913949854773376, 4.594468622316926, 8.877852522924726, 11.483722276898318, 6.5532163011578834, 3.350566854417459, 10.008590019911503, 8.090169943749514, -1.3262813525181905, -7.5012398890743945, -13.106398215644793, -9.551632545854998, -2.510565162951538, -6.920171806924328, -8.34436448747144, -1.5150667439913077, 4.744587724141997, 13.090169943749483, 12.985991467911527, 3.7386336068212844, 4.278081444633028, 6.978448392110426, 3.000000000000009, -1.5371374391910824, -11.132183410882739, -15.63302961575134, -6.6597535466622695, -3.0901699437494634, -4.89048575789227, -2.7708771345775896, -0.9818734337778465, 7.659200741503804, 16.510565162951533, 10.290661480434617, 3.780160294395537, 3.215296010505563, 1.1803833187678798, 1.9098300562505046, -3.682352098662242, -15.24496286334756, -13.407318267407593, -6.042411323978989, -2.87785252292477, 0.8468423306024211, -0.9401521114762706, 0.42704189302179585, 12.21138948528478, 14.999999999999995, 8.975321507785049, 4.231267958202436, -2.1762200889760566, -1.5042986785674242, 1.1221474770752797, -8.393552333148845, -14.64338624490735, -11.44073679816699, -6.918420076162079, 1.9098300562504624, 4.416451296267694, -0.5889300546750427, 5.016228271895255, 12.641802489604514, 12.51056516295153, 10.010341750673767, 0.25419454372198, -6.575103199758153, -1.654417780392574, -3.090169943749364, -9.895821524162054, -11.828803550570726, -12.36825138838254, -3.8882784483610404, 6.999999999999983, 4.627307382940529, 3.042013467133199, 7.542859672001862, 9.749923490411692, 13.09016994374946, 7.980655701641762, -5.319292809171943, -7.1082965099716375, -4.569030797754421, -6.51056516295154, -7.200491536685179, -11.870330238144993, -11.305465954255194, 1.9097866249813635, 8.090169943749492, 6.772522042411657, 7.154792919598133, 5.31714832365812, 9.132581267728344, 12.877852522924748, 2.243327613147084, -7.15001783227312, -8.5172118367713, -9.121219541535359, -5.0000000000000675, -5.8851515640356045, -12.321437901951894, -5.913949854773438, 4.594468622316911, 8.877852522924742, 11.483722276898416, 6.553216301157929, 3.350566854417486, 10.00859001991154, 8.090169943749471, -1.326281352518204, -7.5012398890744105, -13.106398215644763, -9.551632545855146, -2.510565162951565, -6.920171806924145, -8.34436448747149, -1.515066743991394, 4.7445877241419625, 13.090169943749421, 12.985991467911667, 3.7386336068213426, 4.278081444632944, 6.97844839211051, 2.9999999999999902, -1.5371374391909696, -11.132183410882735, -15.633029615751367, -6.659753546662218, -3.090169943749414, -4.890485757892343, -2.7708771345775722, -0.9818734337778587, 7.65920074150402, 16.51056516295153, 10.290661480434544, 3.780160294395471, 3.215296010505578, 1.1803833187679982, 1.9098300562504666, -3.682352098662041, -15.244962863347471, -13.407318267407643, -6.0424113239788655, -2.8778525229247833, 0.8468423306024262, -0.9401521114762436, 0.42704189302176276, 12.211389485284665, 15.000000000000027, 8.97532150778503, 4.231267958202509, -2.176220088975997, -1.5042986785675239, 1.1221474770752362, -8.393552333148786, -14.643386244907363, -11.440736798166888, -6.91842007616213, 1.9098300562504822, 4.416451296267618, -0.5889300546750913, 5.016228271895146, 12.64180248960437, 12.510565162951579, 10.010341750673845, 0.2541945437222143, -6.575103199758261, -1.6544177803925721, -3.090169943749365, -9.895821524162013, -11.828803550570765, -12.368251388382577, -3.8882784483610857, 6.999999999999965, 4.627307382940679, 3.042013467133172, 7.542859672001769, 9.749923490411861, 13.090169943749366, 7.980655701641925, -5.319292809171642, -7.1082965099716775, -4.569030797754218, -6.510565162951558, -7.200491536685024, -11.870330238145078, -11.305465954255249, 1.9097866249817126, 8.09016994374945, 6.772522042411769, 7.154792919598049, 5.317148323658108, 9.132581267728439, 12.877852522924705, 2.243327613147285, -7.150017832273355, -8.517211836771345, -9.121219541535481, -5.000000000000099, -5.885151564035294, -12.321437901951912, -5.913949854773827, 4.5944686223166915, 8.877852522924613, 11.48372227689837, 6.553216301158071, 3.3505668544174334, 10.008590019911294, 8.090169943749519, -1.3262813525180437, -7.50123988907444, -13.106398215644738, -9.55163254585511, -2.510565162951549, -6.92017180692433, -8.344364487471536, -1.5150667439911913, 4.7445877241418035, 13.090169943749576, 12.985991467911692, 3.738633606821152, 4.278081444633065, 6.978448392110371, 3.000000000000078, -1.5371374391907564, -11.132183410882718, -15.633029615751488, -6.659753546662477, -3.0901699437494345]

)

N = len(dataTime)

freq_origin = np.array(
[0.0, 0.390625, 0.78125, 1.171875, 1.5625, 1.953125, 2.34375, 2.734375, 3.125, 3.515625, 3.90625, 4.296875, 4.6875, 5.078125, 5.46875, 5.859375, 6.25, 6.640625, 7.03125, 7.421875, 7.8125, 8.203125, 8.59375, 8.984375, 9.375, 9.765625, 10.15625, 10.546875, 10.9375, 11.328125, 11.71875, 12.109375, 12.5, 12.890625, 13.28125, 13.671875, 14.0625, 14.453125, 14.84375, 15.234375, 15.625, 16.015625, 16.40625, 16.796875, 17.1875, 17.578125, 17.96875, 18.359375, 18.75, 19.140625, 19.53125, 19.921875, 20.3125, 20.703125, 21.09375, 21.484375, 21.875, 22.265625, 22.65625, 23.046875, 23.4375, 23.828125, 24.21875, 24.609375, 25.0, 25.390625, 25.78125, 26.171875, 26.5625, 26.953125, 27.34375, 27.734375, 28.125, 28.515625, 28.90625, 29.296875, 29.6875, 30.078125, 30.46875, 30.859375, 31.25, 31.640625, 32.03125, 32.421875, 32.8125, 33.203125, 33.59375, 33.984375, 34.375, 34.765625, 35.15625, 35.546875, 35.9375, 36.328125, 36.71875, 37.109375, 37.5, 37.890625, 38.28125, 38.671875, 39.0625, 39.453125, 39.84375, 40.234375, 40.625, 41.015625, 41.40625, 41.796875, 42.1875, 42.578125, 42.96875, 43.359375, 43.75, 44.140625, 44.53125, 44.921875, 45.3125, 45.703125, 46.09375, 46.484375, 46.875, 47.265625, 47.65625, 48.046875, 48.4375, 48.828125, 49.21875, 49.609375, 50.0, 50.390625, 50.78125, 51.171875, 51.5625, 51.953125, 52.34375, 52.734375, 53.125, 53.515625, 53.90625, 54.296875, 54.6875, 55.078125, 55.46875, 55.859375, 56.25, 56.640625, 57.03125, 57.421875, 57.8125, 58.203125, 58.59375, 58.984375, 59.375, 59.765625, 60.15625, 60.546875, 60.9375, 61.328125, 61.71875, 62.109375, 62.5, 62.890625, 63.28125, 63.671875, 64.0625, 64.453125, 64.84375, 65.234375, 65.625, 66.015625, 66.40625, 66.796875, 67.1875, 67.578125, 67.96875, 68.359375, 68.75, 69.140625, 69.53125, 69.921875, 70.3125, 70.703125, 71.09375, 71.484375, 71.875, 72.265625, 72.65625, 73.046875, 73.4375, 73.828125, 74.21875, 74.609375, 75.0, 75.390625, 75.78125, 76.171875, 76.5625, 76.953125, 77.34375, 77.734375, 78.125, 78.515625, 78.90625, 79.296875, 79.6875, 80.078125, 80.46875, 80.859375, 81.25, 81.640625, 82.03125, 82.421875, 82.8125, 83.203125, 83.59375, 83.984375, 84.375, 84.765625, 85.15625, 85.546875, 85.9375, 86.328125, 86.71875, 87.109375, 87.5, 87.890625, 88.28125, 88.671875, 89.0625, 89.453125, 89.84375, 90.234375, 90.625, 91.015625, 91.40625, 91.796875, 92.1875, 92.578125, 92.96875, 93.359375, 93.75, 94.140625, 94.53125, 94.921875, 95.3125, 95.703125, 96.09375, 96.484375, 96.875, 97.265625, 97.65625, 98.046875, 98.4375, 98.828125, 99.21875, 99.609375]

)
amp_origin =  np.array(
[11.685154335877684, 11.716987989176431, 11.813784949836243, 11.979561315125448, 12.221461176366011, 12.550522328201664, 12.982957026204136, 13.542238920547723, 14.262535434414506, 15.19451825771944, 16.415634932392717, 18.049337847869875, 20.303846737489835, 23.558219787719644, 28.58019283757094, 37.19164053596525, 55.013567709477854, 112.11304228796544, 1264.8667564388845, 92.40981083740392, 47.60941332862586, 32.11359243521932, 24.386081774645273, 19.848081993464685, 16.93284768189352, 14.958535939355974, 13.580743280639968, 12.606911850329915, 11.921297676505583, 11.450638869606005, 11.14693114597704, 10.978156354698616, 10.923022693991035, 10.967879764721737, 11.104901262614531, 11.331073013882461, 11.647756541681998, 12.060736838332408, 12.580766394716614, 13.224723991611391, 14.01765536101645, 14.99621559641079, 16.214515717097527, 17.754376009910825, 19.74423079647707, 22.396419551259164, 26.08758705084713, 31.554015529544298, 40.453278046560385, 57.45775396161505, 102.81583208795546, 601.7497019575509, 146.6303801307801, 63.45940737979202, 39.6795592674163, 28.399085733120994, 21.80258785674839, 17.46445587799291, 14.385742082633438, 12.07958958507509, 10.280227881213833, 8.830128818254936, 7.629847020134421, 6.613357310571124, 5.7349435311682955, 4.961777292812375, 4.269493498394871, 3.6394337217392967, 3.056864022691407, 2.50979460134288, 1.9882193456188446, 1.483796702358627, 0.9906816771494098, 0.5143686801059941, 0.24083900645164155, 0.6381577916026978, 1.1856855015892729, 1.7925969935659811, 2.4672729530140276, 3.2310802590137606, 4.115785824907396, 5.167954070493821, 6.4582786101297565, 8.099777681554473, 10.285607275252461, 13.37623676698677, 18.131926297257714, 26.481683143859645, 45.175783051616804, 125.96344379381995, 196.89451904174817, 58.452967926734026, 35.34151861637931, 25.80171129697173, 20.5825803616334, 17.285588094193322, 15.011180875045454, 13.345973917025116, 12.073374303295674, 11.068911839264706, 10.255955276688312, 9.584735270680172, 9.02151712081273, 8.542621232823464, 8.130934821243624, 7.773782513086063, 7.461575869598754, 7.186928499018848, 6.944059660180851, 6.728382286512105, 6.53621217093311, 6.36455870028636, 6.2109716749028125, 6.073427455187165, 5.950243172408603, 5.840011289500719, 5.741549136933862, 5.6538596200857265, 5.576100368464529, 5.507559342892201, 5.447635442383628, 5.395823028243737, 5.351699555121611, 5.31491569880879, 5.28518751945731, 5.262290311488501, 5.246053878085889, 5.236359036115782, 5.2331352121742105, 5.236359036115791, 5.246053878085913, 5.262290311488482, 5.2851875194573115, 5.314915698808784, 5.351699555121633, 5.395823028243722, 5.447635442383628, 5.5075593428922085, 5.576100368464524, 5.653859620085732, 5.741549136933865, 5.840011289500685, 5.950243172408593, 6.073427455187157, 6.2109716749028125, 6.364558700286373, 6.53621217093289, 6.7283822865120735, 6.944059660180848, 7.18692849901884, 7.46157586959872, 7.773782513086074, 8.13093482124362, 8.542621232823453, 9.021517120812728, 9.584735270680168, 10.255955276688313, 11.068911839264713, 12.073374303295717, 13.345973917025105, 15.011180875045454, 17.28558809419332, 20.582580361633344, 25.801711296971725, 35.34151861637931, 58.45296792673402, 196.89451904174808, 125.96344379381996, 45.17578305161681, 26.48168314385964, 18.131926297257706, 13.376236766986771, 10.28560727525246, 8.099777681554496, 6.458278610129549, 5.1679540704938285, 4.115785824907396, 3.231080259013724, 2.467272953014055, 1.7925969935659474, 1.1856855015892618, 0.638157791602693, 0.2408390064516623, 0.5143686801059912, 0.9906816771494098, 1.4837967023586327, 1.9882193456188673, 2.509794601342878, 3.0568640226914, 3.639433721739316, 4.269493498394919, 4.961777292812383, 5.7349435311682955, 6.613357310571128, 7.62984702013438, 8.830128818254924, 10.28022788121384, 12.079589585075063, 14.385742082633449, 17.464455877992897, 21.80258785674839, 28.39908573312101, 39.6795592674163, 63.459407379792026, 146.6303801307801, 601.7497019575509, 102.81583208795553, 57.45775396161503, 40.453278046560385, 31.554015529544344, 26.087587050847194, 22.396419551259147, 19.744230796477073, 17.754376009910818, 16.214515717097544, 14.99621559641079, 14.017655361016448, 13.224723991611398, 12.580766394716633, 12.060736838332407, 11.64775654168199, 11.331073013882488, 11.104901262614513, 10.967879764721738, 10.923022693991035, 10.978156354698623, 11.146931145977042, 11.450638869606026, 11.921297676505587, 12.606911850329897, 13.580743280639917, 14.958535939355965, 16.932847681893524, 19.84808199346467, 24.38608177464525, 32.11359243521933, 47.60941332862585, 92.40981083740395, 1264.8667564388845, 112.11304228796541, 55.013567709477854, 37.19164053596528, 28.580192837570962, 23.55821978771963, 20.303846737489838, 18.04933784786987, 16.41563493239268, 15.194518257719432, 14.262535434414504, 13.542238920547717, 12.98295702620416, 12.550522328201648, 12.221461176366011, 11.97956131512541, 11.81378494983627, 11.716987989176426]

) * 2/N
# ======= filtered
filtered = np.array(
[2.97928466936922, 5.392237850921533, 7.519564073233011, 8.864362447857179, 9.29842667719353, 8.228429281964885, 5.344867463570039, 1.1234259120350665, -3.6257050340677455, -7.610976825649602, -9.866550287952744, -10.523467546368146, -9.123966775681444, -5.764631618899784, -1.332237557170787, 3.450487212276564, 7.375604636277324, 9.67594686700103, 10.483663029251778, 9.397667843268348, 6.345431610674671, 2.08083724557443, -2.7572694969573694, -6.968730434487585, -9.504571441421536, -10.452115417218169, -9.610963397176032, -6.84365918937749, -2.797907607926016, 2.003538965081119, 6.476939300246379, 9.320369562775037, 10.443024918283124, 9.801018112111125, 7.269212680522828, 3.4504872122765695, -1.2258456014162837, -5.889702864009879, -9.083328664712802, -10.446169265874845, -9.998057977524468, -7.651388667480986, -4.0257424824449295, 0.4679981333848766, 5.2218079241817845, 8.760808884659893, 10.431404567862813, 10.21316996923539, 8.026685331043431, 4.535478852692663, 0.23428177233432834, -4.508621145907441, -8.340007356839093, -10.360782638952301, -10.433640536338759, -8.423753029562926, -5.011259981148749, -0.8657532933220121, 3.793696678586522, 7.832842935252806, 10.203606143049697, 10.627623533646691, 8.851282860854436, 5.491947704072785, 1.4363935444493456, -3.1134313571795933, -7.271448648998786, -9.948630781828065, -10.756346944078816, -9.293511855989836, -6.008375755577735, -1.9766812582959137, 2.484585582130325, 6.696046519660541, 9.608727428700055, 10.789171272315118, 9.715119384454574, 6.570975274550479, 2.5252236930990106, -1.899382977802561, -6.139883445149408, -9.216213575496498, -10.715708833110162, -10.073702026938173, -7.165056693244313, -3.113431357179624, 1.3300015886948167, 5.6170189491828575, 8.810644749885782, 10.550325253153385, 10.335113832621424, 7.755544654759524, 3.7530585676179085, -0.7406820482118869, -5.117651936903224, -8.42375302956291, -10.327248580584252, -10.485853884062406, -8.299369245870468, -4.431322865414154, 0.10277408276258776, 4.612777133185933, 8.067323442012032, 10.088098724125249, 10.537796523617269, 8.76080888465987, 5.115415968427276, 0.5930693784949809, -4.066380593413558, -7.728686947974296, -9.866550287952787, -10.523467546368217, -9.123966775681533, -5.764631618899894, -1.3322375571708949, 3.4504872122764727, 7.375604636277261, 9.675946867001006, 10.48366302925178, 9.397667843268373, 6.345431610674705, 2.0808372455744633, -2.7572694969573495, -6.968730434487585, -9.50457144142155, -10.452115417218193, -9.61096339717607, -6.843659189377519, -2.797907607926034, 2.0035389650811197, 6.4769393002464035, 9.320369562775088, 10.44302491828318, 9.801018112111162, 7.269212680522846, 3.4504872122765624, -1.2258456014163015, -5.889702864009901, -9.083328664712829, -10.446169265874872, -9.998057977524489, -7.651388667480997, -4.025742482444939, 0.4679981333848649, 5.2218079241817765, 8.760808884659891, 10.43140456786282, 10.213169969235405, 8.026685331043463, 4.535478852692702, 0.23428177233437328, -4.508621145907406, -8.340007356839083, -10.3607826389523, -10.433640536338741, -8.42375302956291, -5.011259981148723, -0.8657532933219838, 3.7936966785865445, 7.8328429352528275, 10.203606143049704, 10.627623533646693, 8.851282860854441, 5.4919477040728, 1.436393544449378, -3.1134313571795373, -7.27144864899871, -9.948630781827978, -10.756346944078732, -9.29351185598978, -6.008375755577721, -1.976681258295924, 2.4845855821303005, 6.6960465196605155, 9.608727428700032, 10.789171272315102, 9.715119384454571, 6.570975274550478, 2.5252236930990106, -1.8993829778025564, -6.139883445149395, -9.216213575496475, -10.715708833110133, -10.073702026938157, -7.165056693244326, -3.113431357179659, 1.3300015886947567, 5.6170189491827855, 8.810644749885714, 10.550325253153346, 10.335113832621426, 7.755544654759567, 3.7530585676179684, -0.7406820482118324, -5.117651936903187, -8.4237530295629, -10.327248580584266, -10.485853884062424, -8.299369245870496, -4.431322865414171, 0.10277408276257871, 4.6127771331859355, 8.06732344201204, 10.088098724125265, 10.537796523617331, 8.760808884659959, 5.115415968427387, 0.593069378495095, -4.066380593413449, -7.728686947974199, -9.866550287952705, -10.523467546368149, -9.12396677568149, -5.764631618899853, -1.3322375571708487, 3.450487212276521, 7.375604636277329, 9.675946867001057, 10.483663029251801, 9.397667843268373, 6.345431610674681, 2.080837245574438, -2.7572694969573632, -6.968730434487585, -9.504571441421556, -10.452115417218224, -9.610963397176116, -6.843659189377597, -2.797907607926136, 2.003538965080997, 6.476939300246276, 9.32036956277497, 10.443024918283088, 9.801018112111132, 7.269212680522849, 3.4504872122766024, -1.2258456014162575, -5.889702864009886, -9.083328664712834, -10.44616926587488, -9.998057977524494, -7.651388667481002, -4.025742482444946, 0.46799813338484786, 5.221807924181757, 8.760808884659887, 10.579454581367196, 10.380379714331797, 8.05522975273828, 4.1051577960282355, -0.7669988938760719, -5.390772683334563, -8.278418260903495, -8.996947528220112, -7.93151974439666, -5.661008034343633]

)
freq_filtered = np.array(
[0.0, 0.390625, 0.78125, 1.171875, 1.5625, 1.953125, 2.34375, 2.734375, 3.125, 3.515625, 3.90625, 4.296875, 4.6875, 5.078125, 5.46875, 5.859375, 6.25, 6.640625, 7.03125, 7.421875, 7.8125, 8.203125, 8.59375, 8.984375, 9.375, 9.765625, 10.15625, 10.546875, 10.9375, 11.328125, 11.71875, 12.109375, 12.5, 12.890625, 13.28125, 13.671875, 14.0625, 14.453125, 14.84375, 15.234375, 15.625, 16.015625, 16.40625, 16.796875, 17.1875, 17.578125, 17.96875, 18.359375, 18.75, 19.140625, 19.53125, 19.921875, 20.3125, 20.703125, 21.09375, 21.484375, 21.875, 22.265625, 22.65625, 23.046875, 23.4375, 23.828125, 24.21875, 24.609375, 25.0, 25.390625, 25.78125, 26.171875, 26.5625, 26.953125, 27.34375, 27.734375, 28.125, 28.515625, 28.90625, 29.296875, 29.6875, 30.078125, 30.46875, 30.859375, 31.25, 31.640625, 32.03125, 32.421875, 32.8125, 33.203125, 33.59375, 33.984375, 34.375, 34.765625, 35.15625, 35.546875, 35.9375, 36.328125, 36.71875, 37.109375, 37.5, 37.890625, 38.28125, 38.671875, 39.0625, 39.453125, 39.84375, 40.234375, 40.625, 41.015625, 41.40625, 41.796875, 42.1875, 42.578125, 42.96875, 43.359375, 43.75, 44.140625, 44.53125, 44.921875, 45.3125, 45.703125, 46.09375, 46.484375, 46.875, 47.265625, 47.65625, 48.046875, 48.4375, 48.828125, 49.21875, 49.609375, 50.0, 50.390625, 50.78125, 51.171875, 51.5625, 51.953125, 52.34375, 52.734375, 53.125, 53.515625, 53.90625, 54.296875, 54.6875, 55.078125, 55.46875, 55.859375, 56.25, 56.640625, 57.03125, 57.421875, 57.8125, 58.203125, 58.59375, 58.984375, 59.375, 59.765625, 60.15625, 60.546875, 60.9375, 61.328125, 61.71875, 62.109375, 62.5, 62.890625, 63.28125, 63.671875, 64.0625, 64.453125, 64.84375, 65.234375, 65.625, 66.015625, 66.40625, 66.796875, 67.1875, 67.578125, 67.96875, 68.359375, 68.75, 69.140625, 69.53125, 69.921875, 70.3125, 70.703125, 71.09375, 71.484375, 71.875, 72.265625, 72.65625, 73.046875, 73.4375, 73.828125, 74.21875, 74.609375, 75.0, 75.390625, 75.78125, 76.171875, 76.5625, 76.953125, 77.34375, 77.734375, 78.125, 78.515625, 78.90625, 79.296875, 79.6875, 80.078125, 80.46875, 80.859375, 81.25, 81.640625, 82.03125, 82.421875, 82.8125, 83.203125, 83.59375, 83.984375, 84.375, 84.765625, 85.15625, 85.546875, 85.9375, 86.328125, 86.71875, 87.109375, 87.5, 87.890625, 88.28125, 88.671875, 89.0625, 89.453125, 89.84375, 90.234375, 90.625, 91.015625, 91.40625, 91.796875, 92.1875, 92.578125, 92.96875, 93.359375, 93.75, 94.140625, 94.53125, 94.921875, 95.3125, 95.703125, 96.09375, 96.484375, 96.875, 97.265625, 97.65625, 98.046875, 98.4375, 98.828125, 99.21875, 99.609375]

)
amp_filtered =np.array(
[11.767011059562497, 11.799768092253359, 11.900980334586144, 12.079511470653067, 12.35028148226826, 12.734548524805188, 13.260484129496602, 13.964366689078501, 14.893044489343112, 16.10890605371576, 17.699736534480184, 19.798366314842568, 22.623388128147212, 26.570387410998272, 32.44326588751054, 42.16097556788578, 61.67273746612353, 122.8860994916315, 1339.0297016533955, 93.36118057542585, 45.46007382877443, 28.850353050692505, 20.697648875180153, 16.156065291829435, 13.538950184592547, 12.053726760971731, 11.238519544819079, 10.795781512406231, 10.533582383420933, 10.333182076667944, 10.125181345889901, 9.872391730579443, 9.55852410555113, 9.181101376934862, 8.747070934434127, 8.270010836301799, 7.768202719348982, 7.2630804937455995, 6.777675597847742, 6.33473182689128, 5.954267480280007, 5.650669179034622, 5.429960039996353, 5.288387271427639, 5.213298740042005, 5.186244232122288, 5.18721852292876, 5.199191902782628, 5.214934870461191, 5.264209213134778, 5.668082143256789, 19.791381577405776, 7.929341711679863, 5.959857020244154, 5.456572659653574, 5.1830581738543975, 4.982048730831354, 4.815999623075463, 4.673791195866894, 4.551836572208, 4.448640010231768, 4.362946274563417, 4.293141595609416, 4.237169321595136, 4.1926588884945, 4.1571180610287595, 4.128110862696936, 4.103388397100831, 4.0809684284234535, 4.059175038919405, 4.036654570411493, 4.012381947057933, 3.985666029358078, 3.956156807217413, 3.9238528771658006, 3.8891056143224825, 3.8526168255893585, 3.8154291147701356, 3.7789122999827303, 3.7447549394056856, 3.7149782276011467, 3.6920033086094426, 3.6788309737921274, 3.6794584984873007, 3.6998334421521073, 3.75017411836507, 3.8513848917594125, 4.056989415736169, 4.561531541295037, 6.961777439402528, 4.742621877375102, 2.4791282324956914, 2.749183914096815, 2.9272739910714365, 3.04623484386834, 3.132693542276955, 3.198523419540478, 3.249140595010598, 3.2871104218897984, 3.313727341800145, 3.3297687656000896, 3.3358790287599724, 3.3327682325188075, 3.3213081261940394, 3.3025655426734573, 3.277795819278908, 3.2484102105058272, 3.215926985911968, 3.1819133715903436, 3.147923737864222, 3.115438065344388, 3.0858036347164166, 3.0601821099881747, 3.0395037669032248, 3.0244305408869128, 3.0153297060202924, 3.012260122248916, 3.014972846992735, 3.022927319827845, 3.035323278561698, 3.051147217979852, 3.069230843301242, 3.0883178876912725, 3.10713504627144, 3.1244626712868677, 3.1392011913869045, 3.150429812033008, 3.157454769151277, 3.1598451269978565, 3.1574547691512818, 3.150429812033013, 3.1392011913869045, 3.1244626712868677, 3.107135046271436, 3.088317887691279, 3.0692308433012414, 3.051147217979852, 3.035323278561699, 3.0229273198278457, 3.014972846992734, 3.012260122248916, 3.015329706020292, 3.0244305408869097, 3.0395037669032234, 3.0601821099881747, 3.085803634716423, 3.11543806534436, 3.147923737864221, 3.1819133715903427, 3.2159269859119703, 3.248410210505802, 3.2777958192789054, 3.3025655426734573, 3.32130812619404, 3.3327682325188146, 3.335879028759976, 3.3297687656000914, 3.3137273418001505, 3.2871104218897926, 3.2491405950105965, 3.198523419540478, 3.1326935422769577, 3.0462348438683002, 2.927273991071439, 2.7491839140968155, 2.4791282324956936, 4.742621877375174, 6.9617774394025265, 4.561531541295037, 4.056989415736171, 3.8513848917594204, 3.7501741183650723, 3.6998334421521055, 3.679458498487302, 3.6788309737921323, 3.692003308609442, 3.7149782276011467, 3.7447549394056905, 3.778912299982681, 3.815429114770134, 3.8526168255893554, 3.889105614322485, 3.923852877165762, 3.956156807217414, 3.985666029358079, 4.01238194705793, 4.036654570411526, 4.059175038919404, 4.080968428423453, 4.10338839710083, 4.1281108626969845, 4.157118061028762, 4.1926588884945, 4.23716932159513, 4.293141595609339, 4.362946274563416, 4.448640010231768, 4.551836572208005, 4.673791195866909, 4.815999623075463, 4.982048730831354, 5.1830581738543895, 5.456572659653673, 5.959857020244156, 7.9293417116798635, 19.79138157740578, 5.668082143256719, 5.2642092131347775, 5.214934870461191, 5.199191902782615, 5.187218522928775, 5.186244232122296, 5.213298740042006, 5.288387271427641, 5.429960039996369, 5.650669179034624, 5.954267480280007, 6.33473182689128, 6.777675597847771, 7.263080493745602, 7.76820271934898, 8.270010836301799, 8.747070934434081, 9.181101376934864, 9.55852410555113, 9.872391730579446, 10.12518134588988, 10.33318207666794, 10.533582383420933, 10.795781512406228, 11.238519544819049, 12.05372676097173, 13.538950184592547, 16.156065291829435, 20.697648875180143, 28.850353050692508, 45.46007382877443, 93.36118057542588, 1339.0297016533955, 122.8860994916315, 61.67273746612353, 42.16097556788577, 32.44326588751062, 26.570387410998283, 22.623388128147216, 19.798366314842575, 17.699736534480174, 16.108906053715756, 14.893044489343112, 13.964366689078497, 13.26048412949661, 12.73454852480519, 12.35028148226826, 12.079511470653062, 11.900980334586155, 11.799768092253366]

)* 2/N

plt.subplot(2, 2, 1)
plt.plot(dataTime)
plt.grid()
plt.title("data in time: 10 * Math.sin(2 * Math.PI * 7 * t) + 5 * Math.cos(2 * Math.PI * 20 * t) + 2 * Math.cos(2 * Math.PI * 35 * t);")

plt.subplot(2, 2, 3)
plt.plot(filtered)
plt.grid()
plt.title("filtered data in time")

plt.subplot(2, 2, 2)
plt.scatter(freq_origin, amp_origin)
plt.plot(freq_origin, amp_origin)
plt.grid()
# plt.xlim(0, len(freq_origin)/2)
# plt.xticks(range(0, int(len(freq_origin)/2), 5))
plt.title("amp - freq, 7/20/50")

plt.subplot(2, 2, 4)
plt.scatter(freq_filtered, amp_filtered)
plt.plot(freq_filtered, amp_filtered)
plt.grid()
# plt.xlim(0, len(freq_filtered)/2)
# plt.xticks(range(0, int(len(freq_filtered)/2), 5))
plt.title("amp - freq, cutoff = 12")

plt.show()