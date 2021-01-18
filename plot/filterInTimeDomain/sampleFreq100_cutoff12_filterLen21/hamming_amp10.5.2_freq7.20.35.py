
import matplotlib.pyplot as plt
import numpy as np

# data[i] = 10 * Math.sin(2 * Math.PI * 7 * t) + 5 * Math.cos(2 * Math.PI * 20 * t) + 2 * Math.cos(2 * Math.PI * 35 * t);

# w len: 21, sumW: 1.0043012501934323

# ===== origin
dataTime = np.array(
[7.0, 4.6273073829405185, 3.042013467133261, 7.542859672001882, 9.749923490411728, 13.090169943749475, 7.980655701641791, -5.319292809171913, -7.108296509971623, -4.5690307977544276, -6.510565162951535, -7.200491536685098, -11.870330238144987, -11.305465954255009, 1.9097866249815936, 8.090169943749485, 6.77252204241173, 7.154792919598085, 5.317148323658091, 9.132581267728419, 12.877852522924734, 2.2433276131470583, -7.150017832273187, -8.517211836771324, -9.121219541535343, -5.000000000000008, -5.8851515640355565, -12.321437901951938, -5.913949854773376, 4.594468622316926, 8.877852522924726, 11.483722276898318, 6.5532163011578834, 3.350566854417459, 10.008590019911503, 8.090169943749514, -1.3262813525181905, -7.5012398890743945, -13.106398215644793, -9.551632545854998, -2.510565162951538, -6.920171806924328, -8.34436448747144, -1.5150667439913077, 4.744587724141997, 13.090169943749483, 12.985991467911527, 3.7386336068212844, 4.278081444633028, 6.978448392110426, 3.000000000000009, -1.5371374391910824, -11.132183410882739, -15.63302961575134, -6.6597535466622695, -3.0901699437494634, -4.89048575789227, -2.7708771345775896, -0.9818734337778465, 7.659200741503804, 16.510565162951533, 10.290661480434617, 3.780160294395537, 3.215296010505563, 1.1803833187678798, 1.9098300562505046, -3.682352098662242, -15.24496286334756, -13.407318267407593, -6.042411323978989, -2.87785252292477, 0.8468423306024211, -0.9401521114762706, 0.42704189302179585, 12.21138948528478, 14.999999999999995, 8.975321507785049, 4.231267958202436, -2.1762200889760566, -1.5042986785674242, 1.1221474770752797, -8.393552333148845, -14.64338624490735, -11.44073679816699, -6.918420076162079, 1.9098300562504624, 4.416451296267694, -0.5889300546750427, 5.016228271895255, 12.641802489604514, 12.51056516295153, 10.010341750673767, 0.25419454372198, -6.575103199758153, -1.654417780392574, -3.090169943749364, -9.895821524162054, -11.828803550570726, -12.36825138838254, -3.8882784483610404, 6.999999999999983, 4.627307382940529, 3.042013467133199, 7.542859672001862, 9.749923490411692, 13.09016994374946, 7.980655701641762, -5.319292809171943, -7.1082965099716375, -4.569030797754421, -6.51056516295154, -7.200491536685179, -11.870330238144993, -11.305465954255194, 1.9097866249813635, 8.090169943749492, 6.772522042411657, 7.154792919598133, 5.31714832365812, 9.132581267728344, 12.877852522924748, 2.243327613147084, -7.15001783227312, -8.5172118367713, -9.121219541535359, -5.0000000000000675, -5.8851515640356045, -12.321437901951894, -5.913949854773438, 4.594468622316911, 8.877852522924742, 11.483722276898416, 6.553216301157929, 3.350566854417486, 10.00859001991154, 8.090169943749471, -1.326281352518204, -7.5012398890744105, -13.106398215644763, -9.551632545855146, -2.510565162951565, -6.920171806924145, -8.34436448747149, -1.515066743991394, 4.7445877241419625, 13.090169943749421, 12.985991467911667, 3.7386336068213426, 4.278081444632944, 6.97844839211051, 2.9999999999999902, -1.5371374391909696, -11.132183410882735, -15.633029615751367, -6.659753546662218, -3.090169943749414, -4.890485757892343, -2.7708771345775722, -0.9818734337778587, 7.65920074150402, 16.51056516295153, 10.290661480434544, 3.780160294395471, 3.215296010505578, 1.1803833187679982, 1.9098300562504666, -3.682352098662041, -15.244962863347471, -13.407318267407643, -6.0424113239788655, -2.8778525229247833, 0.8468423306024262, -0.9401521114762436, 0.42704189302176276, 12.211389485284665, 15.000000000000027, 8.97532150778503, 4.231267958202509, -2.176220088975997, -1.5042986785675239, 1.1221474770752362, -8.393552333148786, -14.643386244907363, -11.440736798166888, -6.91842007616213, 1.9098300562504822, 4.416451296267618, -0.5889300546750913, 5.016228271895146, 12.64180248960437, 12.510565162951579, 10.010341750673845, 0.2541945437222143, -6.575103199758261, -1.6544177803925721, -3.090169943749365, -9.895821524162013, -11.828803550570765, -12.368251388382577, -3.8882784483610857, 6.999999999999965, 4.627307382940679, 3.042013467133172, 7.542859672001769, 9.749923490411861, 13.090169943749366, 7.980655701641925, -5.319292809171642, -7.1082965099716775, -4.569030797754218, -6.510565162951558, -7.200491536685024, -11.870330238145078, -11.305465954255249, 1.9097866249817126, 8.09016994374945, 6.772522042411769, 7.154792919598049, 5.317148323658108, 9.132581267728439, 12.877852522924705, 2.243327613147285, -7.150017832273355, -8.517211836771345, -9.121219541535481, -5.000000000000099, -5.885151564035294, -12.321437901951912, -5.913949854773827, 4.5944686223166915, 8.877852522924613, 11.48372227689837, 6.553216301158071, 3.3505668544174334, 10.008590019911294, 8.090169943749519, -1.3262813525180437, -7.50123988907444, -13.106398215644738, -9.55163254585511, -2.510565162951549, -6.92017180692433, -8.344364487471536, -1.5150667439911913, 4.7445877241418035, 13.090169943749576, 12.985991467911692, 3.738633606821152, 4.278081444633065, 6.978448392110371, 3.000000000000078, -1.5371374391907564, -11.132183410882718, -15.633029615751488, -6.659753546662477, -3.0901699437494345]

)
freq_origin = np.array(
[0.0, 0.390625, 0.78125, 1.171875, 1.5625, 1.953125, 2.34375, 2.734375, 3.125, 3.515625, 3.90625, 4.296875, 4.6875, 5.078125, 5.46875, 5.859375, 6.25, 6.640625, 7.03125, 7.421875, 7.8125, 8.203125, 8.59375, 8.984375, 9.375, 9.765625, 10.15625, 10.546875, 10.9375, 11.328125, 11.71875, 12.109375, 12.5, 12.890625, 13.28125, 13.671875, 14.0625, 14.453125, 14.84375, 15.234375, 15.625, 16.015625, 16.40625, 16.796875, 17.1875, 17.578125, 17.96875, 18.359375, 18.75, 19.140625, 19.53125, 19.921875, 20.3125, 20.703125, 21.09375, 21.484375, 21.875, 22.265625, 22.65625, 23.046875, 23.4375, 23.828125, 24.21875, 24.609375, 25.0, 25.390625, 25.78125, 26.171875, 26.5625, 26.953125, 27.34375, 27.734375, 28.125, 28.515625, 28.90625, 29.296875, 29.6875, 30.078125, 30.46875, 30.859375, 31.25, 31.640625, 32.03125, 32.421875, 32.8125, 33.203125, 33.59375, 33.984375, 34.375, 34.765625, 35.15625, 35.546875, 35.9375, 36.328125, 36.71875, 37.109375, 37.5, 37.890625, 38.28125, 38.671875, 39.0625, 39.453125, 39.84375, 40.234375, 40.625, 41.015625, 41.40625, 41.796875, 42.1875, 42.578125, 42.96875, 43.359375, 43.75, 44.140625, 44.53125, 44.921875, 45.3125, 45.703125, 46.09375, 46.484375, 46.875, 47.265625, 47.65625, 48.046875, 48.4375, 48.828125, 49.21875, 49.609375, 50.0, 50.390625, 50.78125, 51.171875, 51.5625, 51.953125, 52.34375, 52.734375, 53.125, 53.515625, 53.90625, 54.296875, 54.6875, 55.078125, 55.46875, 55.859375, 56.25, 56.640625, 57.03125, 57.421875, 57.8125, 58.203125, 58.59375, 58.984375, 59.375, 59.765625, 60.15625, 60.546875, 60.9375, 61.328125, 61.71875, 62.109375, 62.5, 62.890625, 63.28125, 63.671875, 64.0625, 64.453125, 64.84375, 65.234375, 65.625, 66.015625, 66.40625, 66.796875, 67.1875, 67.578125, 67.96875, 68.359375, 68.75, 69.140625, 69.53125, 69.921875, 70.3125, 70.703125, 71.09375, 71.484375, 71.875, 72.265625, 72.65625, 73.046875, 73.4375, 73.828125, 74.21875, 74.609375, 75.0, 75.390625, 75.78125, 76.171875, 76.5625, 76.953125, 77.34375, 77.734375, 78.125, 78.515625, 78.90625, 79.296875, 79.6875, 80.078125, 80.46875, 80.859375, 81.25, 81.640625, 82.03125, 82.421875, 82.8125, 83.203125, 83.59375, 83.984375, 84.375, 84.765625, 85.15625, 85.546875, 85.9375, 86.328125, 86.71875, 87.109375, 87.5, 87.890625, 88.28125, 88.671875, 89.0625, 89.453125, 89.84375, 90.234375, 90.625, 91.015625, 91.40625, 91.796875, 92.1875, 92.578125, 92.96875, 93.359375, 93.75, 94.140625, 94.53125, 94.921875, 95.3125, 95.703125, 96.09375, 96.484375, 96.875, 97.265625, 97.65625, 98.046875, 98.4375, 98.828125, 99.21875, 99.609375]

)
amp_origin = np.array(
[11.685154335877684, 11.716987989176431, 11.813784949836243, 11.979561315125448, 12.221461176366011, 12.550522328201664, 12.982957026204136, 13.542238920547723, 14.262535434414506, 15.19451825771944, 16.415634932392717, 18.049337847869875, 20.303846737489835, 23.558219787719644, 28.58019283757094, 37.19164053596525, 55.013567709477854, 112.11304228796544, 1264.8667564388845, 92.40981083740392, 47.60941332862586, 32.11359243521932, 24.386081774645273, 19.848081993464685, 16.93284768189352, 14.958535939355974, 13.580743280639968, 12.606911850329915, 11.921297676505583, 11.450638869606005, 11.14693114597704, 10.978156354698616, 10.923022693991035, 10.967879764721737, 11.104901262614531, 11.331073013882461, 11.647756541681998, 12.060736838332408, 12.580766394716614, 13.224723991611391, 14.01765536101645, 14.99621559641079, 16.214515717097527, 17.754376009910825, 19.74423079647707, 22.396419551259164, 26.08758705084713, 31.554015529544298, 40.453278046560385, 57.45775396161505, 102.81583208795546, 601.7497019575509, 146.6303801307801, 63.45940737979202, 39.6795592674163, 28.399085733120994, 21.80258785674839, 17.46445587799291, 14.385742082633438, 12.07958958507509, 10.280227881213833, 8.830128818254936, 7.629847020134421, 6.613357310571124, 5.7349435311682955, 4.961777292812375, 4.269493498394871, 3.6394337217392967, 3.056864022691407, 2.50979460134288, 1.9882193456188446, 1.483796702358627, 0.9906816771494098, 0.5143686801059941, 0.24083900645164155, 0.6381577916026978, 1.1856855015892729, 1.7925969935659811, 2.4672729530140276, 3.2310802590137606, 4.115785824907396, 5.167954070493821, 6.4582786101297565, 8.099777681554473, 10.285607275252461, 13.37623676698677, 18.131926297257714, 26.481683143859645, 45.175783051616804, 125.96344379381995, 196.89451904174817, 58.452967926734026, 35.34151861637931, 25.80171129697173, 20.5825803616334, 17.285588094193322, 15.011180875045454, 13.345973917025116, 12.073374303295674, 11.068911839264706, 10.255955276688312, 9.584735270680172, 9.02151712081273, 8.542621232823464, 8.130934821243624, 7.773782513086063, 7.461575869598754, 7.186928499018848, 6.944059660180851, 6.728382286512105, 6.53621217093311, 6.36455870028636, 6.2109716749028125, 6.073427455187165, 5.950243172408603, 5.840011289500719, 5.741549136933862, 5.6538596200857265, 5.576100368464529, 5.507559342892201, 5.447635442383628, 5.395823028243737, 5.351699555121611, 5.31491569880879, 5.28518751945731, 5.262290311488501, 5.246053878085889, 5.236359036115782, 5.2331352121742105, 5.236359036115791, 5.246053878085913, 5.262290311488482, 5.2851875194573115, 5.314915698808784, 5.351699555121633, 5.395823028243722, 5.447635442383628, 5.5075593428922085, 5.576100368464524, 5.653859620085732, 5.741549136933865, 5.840011289500685, 5.950243172408593, 6.073427455187157, 6.2109716749028125, 6.364558700286373, 6.53621217093289, 6.7283822865120735, 6.944059660180848, 7.18692849901884, 7.46157586959872, 7.773782513086074, 8.13093482124362, 8.542621232823453, 9.021517120812728, 9.584735270680168, 10.255955276688313, 11.068911839264713, 12.073374303295717, 13.345973917025105, 15.011180875045454, 17.28558809419332, 20.582580361633344, 25.801711296971725, 35.34151861637931, 58.45296792673402, 196.89451904174808, 125.96344379381996, 45.17578305161681, 26.48168314385964, 18.131926297257706, 13.376236766986771, 10.28560727525246, 8.099777681554496, 6.458278610129549, 5.1679540704938285, 4.115785824907396, 3.231080259013724, 2.467272953014055, 1.7925969935659474, 1.1856855015892618, 0.638157791602693, 0.2408390064516623, 0.5143686801059912, 0.9906816771494098, 1.4837967023586327, 1.9882193456188673, 2.509794601342878, 3.0568640226914, 3.639433721739316, 4.269493498394919, 4.961777292812383, 5.7349435311682955, 6.613357310571128, 7.62984702013438, 8.830128818254924, 10.28022788121384, 12.079589585075063, 14.385742082633449, 17.464455877992897, 21.80258785674839, 28.39908573312101, 39.6795592674163, 63.459407379792026, 146.6303801307801, 601.7497019575509, 102.81583208795553, 57.45775396161503, 40.453278046560385, 31.554015529544344, 26.087587050847194, 22.396419551259147, 19.744230796477073, 17.754376009910818, 16.214515717097544, 14.99621559641079, 14.017655361016448, 13.224723991611398, 12.580766394716633, 12.060736838332407, 11.64775654168199, 11.331073013882488, 11.104901262614513, 10.967879764721738, 10.923022693991035, 10.978156354698623, 11.146931145977042, 11.450638869606026, 11.921297676505587, 12.606911850329897, 13.580743280639917, 14.958535939355965, 16.932847681893524, 19.84808199346467, 24.38608177464525, 32.11359243521933, 47.60941332862585, 92.40981083740395, 1264.8667564388845, 112.11304228796541, 55.013567709477854, 37.19164053596528, 28.580192837570962, 23.55821978771963, 20.303846737489838, 18.04933784786987, 16.41563493239268, 15.194518257719432, 14.262535434414504, 13.542238920547717, 12.98295702620416, 12.550522328201648, 12.221461176366011, 11.97956131512541, 11.81378494983627, 11.716987989176426]

)
# ======= filtered
filtered = np.array(
[3.285542842381651, 5.078677866128649, 6.942262355418487, 8.32780341180077, 8.5915497580682, 7.275262404847054, 4.424017276180737, 0.6010512000665149, -3.3791402522747775, -6.694037537610809, -8.717624268188727, -9.125732786642068, -7.799371984737503, -4.9530569817112795, -1.1480955896266811, 2.876252369385954, 6.315308790724288, 8.528053757997036, 9.162842146314054, 8.0793211565555, 5.43714393940975, 1.7377138723952956, -2.3132735073333803, -5.898138759140669, -8.314994062806393, -9.17334272876706, -8.32339196823758, -5.888266429215469, -2.3164812217737887, 1.731612436953368, 5.447524321391307, 8.073219721113574, 9.159634431873643, 8.537926087922234, 6.306910885293102, 2.8762523693859574, -1.139697684195491, -4.962929311636477, -7.7961642702970995, -9.11963135120015, -8.728004650170302, -6.697352911954871, -3.412678149428506, 0.5473859016607151, 4.448580740148646, 7.478788146206279, 9.047630222568433, 8.89514431026883, 7.065356517024351, 3.9260828732914406, 0.03691901586436352, -3.9125748165384047, -7.119902548533319, -8.936610297412185, -9.036418635804639, -7.415330496459098, -4.420573342522493, -0.6085965486544885, 3.364547546800327, 6.72306383959174, 8.781081917935893, 9.145342278837045, 7.748033667668961, 4.90171866464274, 1.167705081821667, -2.812794719638772, -6.295699298529324, -8.579392075065611, -9.214180463382636, -8.05971166436055, -5.373686289662596, -1.7181043802003468, 2.2619351902647997, 5.846800442072091, 8.334603555001344, 9.236800378514221, 8.343001460432546, 5.83692811214692, 2.265142904705245, -1.7120029447583816, -5.384066671644123, -8.053610228918608, -9.210972748942222, -8.589264404990818, -6.287301393098156, -2.812794719638798, 1.1593071763904537, 4.911590994567918, 7.744825953228544, 9.13924084339512, 8.791462299917468, 6.716962404149838, 3.3613398323599473, -0.5987242187292635, -4.428971247953656, -7.415330496459079, -9.028020730373443, -8.946482627337387, -7.116694834092927, -3.9064733810965024, 0.02653863388277101, 3.9321843087333326, 7.068564231464722, 8.885271980343594, 9.05602812799959, 7.478788146206253, 4.440182834717442, 0.5572582315859078, -3.4158858638689105, -6.703454347396798, -8.717624268188763, -9.125732786642134, -7.799371984737594, -4.953056981711388, -1.148095589626786, 2.8762523693858713, 6.315308790724237, 8.528053757997014, 9.162842146314054, 8.079321156555514, 5.437143939409771, 1.7377138723953174, -2.3132735073333626, -5.898138759140663, -8.3149940628064, -9.173342728767079, -8.323391968237608, -5.888266429215497, -2.316481221773802, 1.7316124369533747, 5.447524321391333, 8.073219721113613, 9.15963443187369, 8.53792608792227, 6.306910885293123, 2.876252369385957, -1.1396976841955082, -4.962929311636504, -7.796164270297126, -9.119631351200168, -8.72800465017031, -6.69735291195488, -3.4126781494285177, 0.5473859016607012, 4.448580740148635, 7.478788146206279, 9.047630222568445, 8.895144310268854, 7.065356517024383, 3.9260828732914743, 0.03691901586439679, -3.9125748165383727, -7.119902548533292, -8.936610297412162, -9.036418635804626, -7.415330496459087, -4.420573342522475, -0.6085965486544634, 3.364547546800357, 6.7230638395917675, 8.781081917935909, 9.145342278837045, 7.748033667668962, 4.901718664642752, 1.1677050818217036, -2.8127947196387098, -6.295699298529247, -8.579392075065533, -9.214180463382567, -8.059711664360504, -5.373686289662574, -1.7181043802003466, 2.2619351902647855, 5.846800442072066, 8.334603555001319, 9.236800378514213, 8.343001460432546, 5.836928112146921, 2.265142904705248, -1.7120029447583804, -5.38406667164412, -8.053610228918595, -9.210972748942204, -8.5892644049908, -6.287301393098158, -2.8127947196388243, 1.1593071763903995, 4.91159099456785, 7.74482595322848, 9.139240843395084, 8.791462299917477, 6.716962404149875, 3.3613398323599997, -0.5987242187292179, -4.428971247953631, -7.415330496459078, -9.02802073037346, -8.946482627337408, -7.116694834092945, -3.9064733810965135, 0.02653863388276908, 3.9321843087333375, 7.068564231464737, 8.885271980343623, 9.056028127999639, 7.478788146206329, 4.440182834717545, 0.5572582315860294, -3.4158858638687923, -6.703454347396701, -8.717624268188686, -9.125732786642073, -7.79937198473754, -4.953056981711333, -1.1480955896267246, 2.876252369385929, 6.315308790724286, 8.528053757997052, 9.16284214631408, 8.079321156555524, 5.437143939409764, 1.7377138723952974, -2.3132735073333923, -5.898138759140688, -8.314994062806418, -9.173342728767095, -8.323391968237644, -5.888266429215571, -2.3164812217739152, 1.7316124369532389, 5.447524321391207, 8.073219721113512, 9.15963443187363, 8.53792608792224, 6.306910885293114, 2.876252369385963, -1.1396976841954876, -4.96292931163648, -7.796164270297109, -9.119631351200171, -8.728004650170329, -6.697352911954902, -3.4126781494285323, 0.5473859016606998, 4.448580740148643, 7.4787881462062815, 9.059474223648794, 8.91039710943545, 7.0644516853422425, 3.854021291485915, -0.14815321067594586, -4.120047061488382, -7.0833978876514045, -8.281182534277356, -7.536190566630816, -5.3745296546919645]

)
freq_filtered = np.array(
[0.0, 0.390625, 0.78125, 1.171875, 1.5625, 1.953125, 2.34375, 2.734375, 3.125, 3.515625, 3.90625, 4.296875, 4.6875, 5.078125, 5.46875, 5.859375, 6.25, 6.640625, 7.03125, 7.421875, 7.8125, 8.203125, 8.59375, 8.984375, 9.375, 9.765625, 10.15625, 10.546875, 10.9375, 11.328125, 11.71875, 12.109375, 12.5, 12.890625, 13.28125, 13.671875, 14.0625, 14.453125, 14.84375, 15.234375, 15.625, 16.015625, 16.40625, 16.796875, 17.1875, 17.578125, 17.96875, 18.359375, 18.75, 19.140625, 19.53125, 19.921875, 20.3125, 20.703125, 21.09375, 21.484375, 21.875, 22.265625, 22.65625, 23.046875, 23.4375, 23.828125, 24.21875, 24.609375, 25.0, 25.390625, 25.78125, 26.171875, 26.5625, 26.953125, 27.34375, 27.734375, 28.125, 28.515625, 28.90625, 29.296875, 29.6875, 30.078125, 30.46875, 30.859375, 31.25, 31.640625, 32.03125, 32.421875, 32.8125, 33.203125, 33.59375, 33.984375, 34.375, 34.765625, 35.15625, 35.546875, 35.9375, 36.328125, 36.71875, 37.109375, 37.5, 37.890625, 38.28125, 38.671875, 39.0625, 39.453125, 39.84375, 40.234375, 40.625, 41.015625, 41.40625, 41.796875, 42.1875, 42.578125, 42.96875, 43.359375, 43.75, 44.140625, 44.53125, 44.921875, 45.3125, 45.703125, 46.09375, 46.484375, 46.875, 47.265625, 47.65625, 48.046875, 48.4375, 48.828125, 49.21875, 49.609375, 50.0, 50.390625, 50.78125, 51.171875, 51.5625, 51.953125, 52.34375, 52.734375, 53.125, 53.515625, 53.90625, 54.296875, 54.6875, 55.078125, 55.46875, 55.859375, 56.25, 56.640625, 57.03125, 57.421875, 57.8125, 58.203125, 58.59375, 58.984375, 59.375, 59.765625, 60.15625, 60.546875, 60.9375, 61.328125, 61.71875, 62.109375, 62.5, 62.890625, 63.28125, 63.671875, 64.0625, 64.453125, 64.84375, 65.234375, 65.625, 66.015625, 66.40625, 66.796875, 67.1875, 67.578125, 67.96875, 68.359375, 68.75, 69.140625, 69.53125, 69.921875, 70.3125, 70.703125, 71.09375, 71.484375, 71.875, 72.265625, 72.65625, 73.046875, 73.4375, 73.828125, 74.21875, 74.609375, 75.0, 75.390625, 75.78125, 76.171875, 76.5625, 76.953125, 77.34375, 77.734375, 78.125, 78.515625, 78.90625, 79.296875, 79.6875, 80.078125, 80.46875, 80.859375, 81.25, 81.640625, 82.03125, 82.421875, 82.8125, 83.203125, 83.59375, 83.984375, 84.375, 84.765625, 85.15625, 85.546875, 85.9375, 86.328125, 86.71875, 87.109375, 87.5, 87.890625, 88.28125, 88.671875, 89.0625, 89.453125, 89.84375, 90.234375, 90.625, 91.015625, 91.40625, 91.796875, 92.1875, 92.578125, 92.96875, 93.359375, 93.75, 94.140625, 94.53125, 94.921875, 95.3125, 95.703125, 96.09375, 96.484375, 96.875, 97.265625, 97.65625, 98.046875, 98.4375, 98.828125, 99.21875, 99.609375]

)
amp_filtered = np.array(
[11.7140751771691, 11.750367451421667, 11.860289176884395, 12.04709092741878, 12.316598381127848, 12.677907425783443, 13.14455016428402, 13.736400508961955, 14.48281676598028, 15.427973293148163, 16.640301038939427, 18.2301799016828, 20.385625121181306, 23.451546263488776, 28.130342497677894, 36.09460708525583, 52.514161163685074, 105.06210169381615, 1162.4998427646146, 83.31762389149995, 42.18023676633471, 28.041842176214214, 21.069673682498077, 17.03747518427405, 14.489891099178053, 12.786023629949362, 11.596963156545458, 10.735880977905415, 10.089242129772952, 9.58496361333833, 9.17602703173062, 8.831311051966171, 8.530125733952806, 8.25879361645805, 8.00842939404073, 7.773451842330211, 7.550557753796949, 7.337995661989266, 7.135039979066594, 6.94160423842633, 6.7579558435440115, 6.584509786002541, 6.421688644610966, 6.269843357695866, 6.129236687688923, 6.000104622061512, 5.88284598232766, 5.778503807509832, 5.6901514955891495, 5.628211672458019, 5.645323712883115, 7.43016440602775, 5.0439019573422, 5.0611412422716615, 5.02409539801121, 4.972689218233151, 4.916946115960404, 4.86019352129349, 4.803777893122178, 4.748314193964907, 4.694104607633895, 4.641301298031533, 4.589976084255372, 4.540152508178883, 4.491821823070078, 4.4449520326645615, 4.399494048888782, 4.35538678851799, 4.312561968647905, 4.270948842019664, 4.230478857327616, 4.191090109001273, 4.152731395288751, 4.1153657044681555, 4.078972984084584, 4.043552112653319, 4.009122087666568, 3.9757225740504682, 3.9434141402759524, 3.912278785748765, 3.8824218278808846, 3.8539770957313135, 3.827119229931313, 3.802091220193743, 3.7792665961595593, 3.759299146798195, 3.7435306818595593, 3.7353555977335517, 3.746779118645912, 3.872716527401017, 3.309654979115084, 3.510530963663451, 3.5319779344618674, 3.5316118130877556, 3.524633015210715, 3.5149465119362935, 3.503954884610501, 3.49225144233784, 3.4801108891878303, 3.467669989038182, 3.4550057151265707, 3.4421729809301653, 3.4292240142984776, 3.4162182869767372, 3.403227008533638, 3.390334187238925, 3.377635381472269, 3.365234860254933, 3.353241696602319, 3.3417652181162865, 3.3309101829336285, 3.3207720104565746, 3.3114323624784445, 3.3029553347855907, 3.2953844786505293, 3.2887408243144503, 3.283022024445339, 3.278202675714752, 3.2742358131927425, 3.271055508272512, 3.2685804399176366, 3.266718254980174, 3.2653704896485007, 3.264437793513633, 3.263825182022314, 3.2634470427989632, 3.263231635945934, 3.2631248565500783, 3.2630930671627967, 3.2631248565500814, 3.263231635945919, 3.263447042798964, 3.263825182022313, 3.264437793513634, 3.265370489648518, 3.2667182549801694, 3.2685804399176375, 3.2710555082725077, 3.274235813192741, 3.2782026757147524, 3.283022024445339, 3.2887408243144454, 3.2953844786505573, 3.3029553347855916, 3.3114323624784445, 3.320772010456576, 3.330910182933584, 3.3417652181162882, 3.3532416966023195, 3.3652348602549322, 3.3776353814722753, 3.3903341872389245, 3.403227008533638, 3.4162182869767372, 3.4292240142984634, 3.4421729809301653, 3.4550057151265707, 3.4676699890381864, 3.480110889187854, 3.4922514423378397, 3.503954884610501, 3.51494651193629, 3.524633015210742, 3.5316118130877543, 3.5319779344618674, 3.5105309636634527, 3.309654979115083, 3.8727165274010185, 3.746779118645912, 3.7353555977335526, 3.7435306818595753, 3.7592991467981984, 3.779266596159559, 3.8020912201937467, 3.827119229931344, 3.8539770957313135, 3.8824218278808846, 3.9122787857487706, 3.943414140276016, 3.975722574050463, 4.009122087666568, 4.043552112653319, 4.07897298408453, 4.115365704468153, 4.152731395288751, 4.191090109001273, 4.230478857327653, 4.270948842019666, 4.312561968647905, 4.355386788517993, 4.3994940488888, 4.444952032664564, 4.491821823070078, 4.540152508178881, 4.589976084255318, 4.641301298031536, 4.6941046076338955, 4.748314193964911, 4.803777893122197, 4.860193521293491, 4.916946115960404, 4.9726892182331435, 5.024095398011255, 5.0611412422716615, 5.0439019573422, 7.430164406027746, 5.645323712883093, 5.628211672458017, 5.6901514955891495, 5.7785038075098205, 5.882845982327691, 6.000104622061511, 6.129236687688923, 6.269843357695867, 6.421688644610977, 6.5845097860025446, 6.757955843544011, 6.941604238426329, 7.135039979066633, 7.337995661989265, 7.550557753796948, 7.773451842330205, 8.008429394040741, 8.258793616458052, 8.530125733952806, 8.831311051966173, 9.176027031730595, 9.584963613338331, 10.089242129772952, 10.735880977905413, 11.596963156545408, 12.786023629949366, 14.489891099178053, 17.037475184274054, 21.069673682498088, 28.041842176214217, 42.18023676633471, 83.31762389149995, 1162.4998427646144, 105.06210169381615, 52.514161163685074, 36.094607085255824, 28.13034249767785, 23.451546263488783, 20.385625121181306, 18.230179901682806, 16.6403010389394, 15.42797329314816, 14.482816765980283, 13.736400508961955, 13.144550164284038, 12.677907425783445, 12.316598381127845, 12.047090927418779, 11.86028917688439, 11.750367451421672]

)

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