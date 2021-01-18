import matplotlib.pyplot as plt
import numpy as np

# w len: 21, sumW: 1.1773120015895144


dataTime = np.array(
[7.0, 7.339461759900482, 6.749797978721974, 5.635224211256133, 4.507529217890259, 3.8028778875254643, 3.7321506252542798, 4.220786472544158, 4.959697146618973, 5.546270812099301, 5.660047455883156, 5.204477535592913, 4.359298028872762, 3.522452211527672, 3.162988940737493, 3.6407466394115735, 5.061705504585339, 7.224658556030886, 9.680337857859428, 11.88149675620946, 13.367957479161623, 13.917444679505735, 13.606166550423074, 12.757551927133138, 11.800148378829782, 11.090169943749475, 10.7673956242543, 10.70003246959747, 10.539790738763957, 9.865924128526753, 8.362621712891894, 5.96105094353309, 2.8905635138933685, -0.38194047633802064, -3.3028980462857795, -5.417179776581605, -6.5182173726245205, -6.707171344057097, -6.339639322966565, -5.881041065391122, -5.726330498721517, -6.052918120893878, -6.76260876868843, -7.533990392253707, -7.964200065445846, -7.744601302339378, -6.8017843352211, -5.348471252064257, -3.8233448753803136, -2.7413686792656513, -2.5105651629515346, -3.2843189334727123, -4.905046867997293, -6.960560417703012, -8.931794740260798, -10.376062041270039, -11.076762626785264, -11.103586009144946, -10.761634537420052, -10.450450448129004, -10.488364226894891, -10.970752427169717, -11.717670691404232, -12.331935576532535, -12.346219395137204, -11.403352921664702, -9.400952543708208, -6.544721401793266, -3.289288399949058, -0.18808451282407268, 2.291752636231696, 3.9202661369455245, 4.765320307654632, 5.1414023183158015, 5.467589426387061, 6.090169943749473, 7.138618485265281, 8.470538733122748, 9.726820593199639, 10.475764094548222, 10.390556031161626, 9.391398040638274, 7.6967972645300256, 5.76301437137165, 4.133260304019287, 3.2526798870077798, 3.318301471982605, 4.219943028520174, 5.593573587377585, 6.965993452141626, 7.935182312407976, 8.317431487385576, 8.205454860071276, 7.916042488268919, 7.84833033510585, 8.308151772313366, 9.367058978103223, 10.811432164027396, 12.202657637848286, 13.02680735192262, 12.877852522924734, 11.605345132208116, 9.370725055478575, 6.590927935489694, 3.7906193413183664, 1.4188981177319988, -0.30046424259114946, -1.4292801628449885, -2.264130524354795, -3.195457611942391, -4.531983843523282, -6.359043885921238, -8.486295327755327, -10.5058809108052, -11.939605909458717, -12.419324869361631, -11.83165363548184, -10.371355556689743, -8.482265091350591, -6.707247585531908, -5.5031855527854585, -5.090170612893876, -5.390939262475797, -6.082143933822622, -6.736454274538459, -7.0, -6.736454274538456, -6.082143933822617, -5.3909392624758, -5.090170612893866, -5.50318555278545, -6.707247585531885, -8.482265091350602, -10.371355556689743, -11.831653635481839, -12.419324869361631, -11.939605909458715, -10.505880910805205, -8.486295327755316, -6.359043885921208, -4.53198384352328, -3.1954576119423943, -2.264130524354806, -1.4292801628450191, -0.3004642425912245, 1.4188981177319615, 3.7906193413182994, 6.590927935489624, 9.370725055478504, 11.605345132208111, 12.877852522924726, 13.026807351922622, 12.202657637848294, 10.81143216402741, 9.367058978103204, 8.308151772313373, 7.848330335105852, 7.916042488268947, 8.20545486007127, 8.317431487385594, 7.935182312407983, 6.965993452141644, 5.593573587377583, 4.219943028520174, 3.3183014719825965, 3.252679887007769, 4.133260304019309, 5.763014371371682, 7.69679726453006, 9.391398040638297, 10.390556031161616, 10.47576409454823, 9.726820593199651, 8.470538733122755, 7.138618485265309, 6.090169943749498, 5.467589426387078, 5.141402318315821, 4.765320307654657, 3.9202661369455365, 2.2917526362317164, -0.18808451282405336, -3.2892883999490445, -6.544721401793227, -9.400952543708199, -11.403352921664695, -12.346219395137178, -12.331935576532508, -11.717670691404248, -10.970752427169714, -10.488364226894898, -10.450450448129015, -10.761634537420058, -11.103586009144937, -11.076762626785268, -10.37606204127005, -8.931794740260807, -6.960560417702979, -4.905046867997293, -3.2843189334727128, -2.510565162951538, -2.741368679265669, -3.8233448753803336, -5.3484712520642645, -6.801784335221054, -7.74460130233939, -7.964200065445852, -7.533990392253698, -6.762608768688422, -6.0529181208938505, -5.726330498721531, -5.881041065391128, -6.339639322966602, -6.707171344057082, -6.518217372624541, -5.41717977658162, -3.3028980462857875, -0.3819404763380507, 2.890563513893376, 5.961050943533076, 8.36262171289188, 9.865924128526713, 10.53979073876393, 10.700032469597502, 10.7673956242543, 11.09016994374948, 11.800148378829785, 12.75755192713314, 13.606166550423083, 13.917444679505756, 13.367957479161632, 11.881496756209422, 9.680337857859433, 7.2246585560308825, 5.061705504585335, 3.6407466394115815, 3.162988940737485, 3.5224522115276473, 4.359298028872747, 5.204477535592892, 5.660047455883168, 5.546270812099297, 4.959697146618946, 4.220786472544129, 3.732150625254265, 3.8028778875254696, 4.507529217890231, 5.6352242112561175, 6.749797978721968, 7.339461759900503, 7.000000000000009, 5.582437828885611, 3.2493367992164615, 0.4183940854581658, -2.3853292456000825, -4.712707943776013]

)

freq_origin = np.array(
[0.0, 1.953125, 3.90625, 5.859375, 7.8125, 9.765625, 11.71875, 13.671875, 15.625, 17.578125, 19.53125, 21.484375, 23.4375, 25.390625, 27.34375, 29.296875, 31.25, 33.203125, 35.15625, 37.109375, 39.0625, 41.015625, 42.96875, 44.921875, 46.875, 48.828125, 50.78125, 52.734375, 54.6875, 56.640625, 58.59375, 60.546875, 62.5, 64.453125, 66.40625, 68.359375, 70.3125, 72.265625, 74.21875, 76.171875, 78.125, 80.078125, 82.03125, 83.984375, 85.9375, 87.890625, 89.84375, 91.796875, 93.75, 95.703125, 97.65625, 99.609375, 101.5625, 103.515625, 105.46875, 107.421875, 109.375, 111.328125, 113.28125, 115.234375, 117.1875, 119.140625, 121.09375, 123.046875, 125.0, 126.953125, 128.90625, 130.859375, 132.8125, 134.765625, 136.71875, 138.671875, 140.625, 142.578125, 144.53125, 146.484375, 148.4375, 150.390625, 152.34375, 154.296875, 156.25, 158.203125, 160.15625, 162.109375, 164.0625, 166.015625, 167.96875, 169.921875, 171.875, 173.828125, 175.78125, 177.734375, 179.6875, 181.640625, 183.59375, 185.546875, 187.5, 189.453125, 191.40625, 193.359375, 195.3125, 197.265625, 199.21875, 201.171875, 203.125, 205.078125, 207.03125, 208.984375, 210.9375, 212.890625, 214.84375, 216.796875, 218.75, 220.703125, 222.65625, 224.609375, 226.5625, 228.515625, 230.46875, 232.421875, 234.375, 236.328125, 238.28125, 240.234375, 242.1875, 244.140625, 246.09375, 248.046875, 250.0, 251.953125, 253.90625, 255.859375, 257.8125, 259.765625, 261.71875, 263.671875, 265.625, 267.578125, 269.53125, 271.484375, 273.4375, 275.390625, 277.34375, 279.296875, 281.25, 283.203125, 285.15625, 287.109375, 289.0625, 291.015625, 292.96875, 294.921875, 296.875, 298.828125, 300.78125, 302.734375, 304.6875, 306.640625, 308.59375, 310.546875, 312.5, 314.453125, 316.40625, 318.359375, 320.3125, 322.265625, 324.21875, 326.171875, 328.125, 330.078125, 332.03125, 333.984375, 335.9375, 337.890625, 339.84375, 341.796875, 343.75, 345.703125, 347.65625, 349.609375, 351.5625, 353.515625, 355.46875, 357.421875, 359.375, 361.328125, 363.28125, 365.234375, 367.1875, 369.140625, 371.09375, 373.046875, 375.0, 376.953125, 378.90625, 380.859375, 382.8125, 384.765625, 386.71875, 388.671875, 390.625, 392.578125, 394.53125, 396.484375, 398.4375, 400.390625, 402.34375, 404.296875, 406.25, 408.203125, 410.15625, 412.109375, 414.0625, 416.015625, 417.96875, 419.921875, 421.875, 423.828125, 425.78125, 427.734375, 429.6875, 431.640625, 433.59375, 435.546875, 437.5, 439.453125, 441.40625, 443.359375, 445.3125, 447.265625, 449.21875, 451.171875, 453.125, 455.078125, 457.03125, 458.984375, 460.9375, 462.890625, 464.84375, 466.796875, 468.75, 470.703125, 472.65625, 474.609375, 476.5625, 478.515625, 480.46875, 482.421875, 484.375, 486.328125, 488.28125, 490.234375, 492.1875, 494.140625, 496.09375, 498.046875]

)

amp_origin = np.array(
[236.36970937358743, 255.18647882067614, 336.80730342890615, 752.9011282333925, 871.4925286803585, 205.98598326684413, 89.87117975272876, 36.309414315549326, 7.814389291180278, 70.18806880282501, 547.7501651461913, 210.42818112575705, 101.40931567942486, 68.98454160977238, 52.52435066312725, 42.174384740472526, 34.832978528812774, 29.178631001613507, 24.532645013314742, 20.502002776931686, 16.869845341961454, 13.690308239627234, 11.988482182856904, 15.589101520395124, 32.38164213244474, 112.77459266417773, 209.92381859075047, 71.12006352620018, 47.57518785404883, 37.584672448497685, 31.921083442296087, 28.196234116269455, 25.51478544268093, 23.464581325672725, 21.828779815750668, 20.48194255904046, 19.34614550216029, 18.370210643181878, 17.518989290805486, 16.767439608101494, 16.097165834143947, 15.494299935174322, 14.948153046097664, 14.450327561658595, 13.994115186043931, 13.574078258283736, 13.185751886649896, 12.825427722455322, 12.489994142707236, 12.176816194038635, 11.883644073102918, 11.608542425129317, 11.349835058000721, 11.10606122800303, 10.875940721278752, 10.658345698470944, 10.452277795377716, 10.256849348776358, 10.071267889635982, 9.894823246427812, 9.7268767500748, 9.566852143723805, 9.41422788507099, 9.268530593595166, 9.129329444853466, 8.996231352704521, 8.86887681061154, 8.746936287080988, 8.630107089243408, 8.518110623753538, 8.410689996343907, 8.307607901237215, 8.208644759597375, 8.113597072768643, 8.022275961394012, 7.9345058659572, 7.850123387942764, 7.76897625388475, 7.690922387109305, 7.6158290741349965, 7.5435722144854225, 7.474035644203417, 7.40711052464348, 7.342694789227087, 7.2806926417711475, 7.221014100823404, 7.163574585111292, 7.108294535820969, 7.055099071921681, 7.003917675214823, 6.954683902154275, 6.907335119832008, 6.861812263815354, 6.818059615775218, 6.776024599071035, 6.735657590655552, 6.696911747839511, 6.659742848599876, 6.624109144265016, 6.589971223514934, 6.557291886754454, 6.52603603000157, 6.496170537523481, 6.467664182525, 6.440487535263188, 6.414612878020651, 6.390014126423478, 6.3666667566403925, 6.344547738042545, 6.323635470939922, 6.303909729051972, 6.285351606396015, 6.267943468307789, 6.251668906341375, 6.236512696809816, 6.222460762758498, 6.209500139178448, 6.197618941287209, 6.186806335723369, 6.177052514517063, 6.168348671707167, 6.1606869825018, 6.154060584878248, 6.148463563541482, 6.143890936164529, 6.140338641851611, 6.137803531765548, 6.136283361884785, 6.135776787850347, 6.136283361884784, 6.137803531765548, 6.140338641851553, 6.143890936164472, 6.148463563541453, 6.154060584878233, 6.160686982501797, 6.168348671707167, 6.177052514517054, 6.186806335723402, 6.197618941287226, 6.20950013917844, 6.222460762758506, 6.236512696809809, 6.251668906341402, 6.267943468307789, 6.285351606396032, 6.303909729051972, 6.323635470939918, 6.344547738042548, 6.366666756640385, 6.390014126423498, 6.414612878020635, 6.440487535263188, 6.467664182524996, 6.496170537523475, 6.526036030001573, 6.55729188675447, 6.589971223514927, 6.624109144265017, 6.659742848599879, 6.696911747839511, 6.735657590655554, 6.776024599071039, 6.818059615775242, 6.8618122638153505, 6.907335119832, 6.954683902154297, 7.003917675214816, 7.055099071921682, 7.108294535820957, 7.163574585111257, 7.221014100823404, 7.280692641771119, 7.342694789227092, 7.4071105246434765, 7.474035644203438, 7.5435722144854225, 7.615829074135006, 7.690922387109301, 7.768976253884751, 7.850123387942753, 7.934505865957204, 8.022275961394051, 8.11359707276864, 8.208644759597375, 8.307607901237203, 8.410689996343901, 8.51811062375354, 8.630107089243388, 8.746936287080999, 8.86887681061157, 8.996231352704523, 9.129329444853466, 9.26853059359515, 9.414227885070979, 9.566852143723773, 9.726876750074812, 9.894823246427826, 10.071267889635969, 10.25684934877634, 10.452277795377716, 10.658345698470942, 10.875940721278772, 11.106061228003039, 11.349835058000702, 11.608542425129317, 11.883644073102921, 12.176816194038627, 12.489994142707236, 12.825427722455318, 13.185751886649882, 13.574078258283745, 13.994115186043937, 14.450327561658577, 14.948153046097671, 15.49429993517433, 16.097165834143947, 16.76743960810149, 17.51898929080551, 18.370210643181906, 19.346145502160272, 20.48194255904044, 21.82877981575065, 23.46458132567272, 25.51478544268093, 28.196234116269466, 31.92108344229608, 37.58467244849773, 47.575187854048814, 71.12006352620017, 209.9238185907505, 112.77459266417775, 32.38164213244474, 15.589101520395117, 11.988482182856895, 13.690308239627186, 16.869845341961415, 20.50200277693172, 24.532645013314763, 29.178631001613496, 34.832978528812774, 42.174384740472526, 52.52435066312726, 68.98454160977246, 101.40931567942486, 210.428181125757, 547.7501651461913, 70.18806880282503, 7.814389291180278, 36.30941431554935, 89.87117975272879, 205.98598326684413, 871.4925286803585, 752.9011282333925, 336.8073034289062, 255.1864788206761]

)

filtered = np.array(
[3.640525495762681, 4.112911557760366, 4.548861180019939, 4.927031650614567, 5.227734271859397, 5.439027175114273, 5.562175563987485, 5.6144079269098714, 5.627709077172918, 5.6436910840088546, 5.705893512514786, 5.914296510794452, 6.28090193397342, 6.792447282742681, 7.418102093271889, 8.11997160082467, 8.862405474744595, 9.616822832475009, 10.360718037994541, 11.071943661019636, 11.721335283461801, 12.26748533126672, 12.656699214342014, 12.829169320912165, 12.729944946245045, 12.321302785847235, 11.592395774764185, 10.562867397382064, 9.279169356834569, 7.80484524090138, 6.208093581923969, 4.550733042921927, 2.8819656015554753, 1.2383601377760314, -0.3509786551001837, -1.8570888758457655, -3.245484299414173, -4.475205840099666, -5.503687617001089, -6.296101809729514, -6.83589323270924, -7.132501186715203, -7.223081407600664, -7.167089681817973, -7.035103622825164, -6.895292847857142, -6.801733990452558, -6.788012314879586, -6.867547501382969, -7.0395919621494665, -7.2978215675873255, -7.637636953162293, -8.059012932038177, -8.563684843082553, -9.147882728147758, -9.793775538988209, -10.463506933440772, -11.09890251749076, -11.62789991793343, -11.97626387167927, -12.081144332789036, -11.902280943134812, -11.427443424245622, -10.670731210601014, -9.664870587880834, -8.450696369373398, -7.0678204262358175, -5.549776039746255, -3.9249738070501152, -2.222373020182145, -0.4788041849691661, 1.2558640909920893, 2.9187466655882135, 4.4401869250766355, 5.754802872994477, 6.813938286255813, 7.595396096324779, 8.107140466117595, 8.383704773052848, 8.476567436761103, 8.441808276312338, 8.329167407696648, 8.175901828554373, 8.006861373749715, 7.839748247261894, 7.692526589692579, 7.589174637456086, 7.56071451560179, 7.640423012697987, 7.854558555647584, 8.21189290063635, 8.696049469155943, 9.263835043730664, 9.850702838924125, 10.381970092516529, 10.786379632952771, 11.00780874219913, 11.011683363242273, 10.78465996096065, 10.328626617345456, 9.652103486028622, 8.762924504072254, 7.665362967084782, 6.36291233151745, 4.865511604250445, 3.198053431768384, 1.4062936981822096, -0.44291680227033126, -2.2681295305951807, -3.9850858735184262, -5.520352758900333, -6.822608962627922, -7.86817103172277, -8.659381482533021, -9.216996852664671, -9.569761936838768, -9.745171806626248, -9.764709859266423, -9.644896902536178, -9.403054474917809, -9.064717356709671, -8.668887805383791, -8.268098015446181, -7.9222451126332745, -7.6876205329934395, -7.604529162109076, -7.687620532993438, -7.922245112633272, -8.268098015446178, -8.668887805383788, -9.064717356709668, -9.403054474917806, -9.644896902536173, -9.764709859266418, -9.745171806626242, -9.569761936838766, -9.216996852664671, -8.659381482533027, -7.868171031722777, -6.822608962627932, -5.520352758900349, -3.9850858735184467, -2.2681295305952065, -0.4429168022703602, 1.406293698182179, 3.198053431768351, 4.865511604250413, 6.362912331517417, 7.665362967084751, 8.76292450407222, 9.652103486028595, 10.328626617345439, 10.784659960960637, 11.01168336324226, 11.007808742199126, 10.786379632952768, 10.381970092516529, 9.850702838924128, 9.263835043730671, 8.696049469155954, 8.211892900636355, 7.854558555647593, 7.640423012697997, 7.5607145156017985, 7.5891746374560975, 7.6925265896925925, 7.839748247261906, 8.006861373749727, 8.175901828554386, 8.329167407696662, 8.441808276312354, 8.47656743676112, 8.383704773052866, 8.107140466117615, 7.595396096324799, 6.813938286255833, 5.754802872994498, 4.440186925076657, 2.9187466655882353, 1.2558640909921108, -0.47880418496914445, -2.2223730201821237, -3.9249738070500944, -5.549776039746236, -7.067820426235803, -8.450696369373384, -9.664870587880825, -10.670731210601005, -11.427443424245613, -11.90228094313481, -12.081144332789036, -11.976263871679267, -11.627899917933428, -11.098902517490762, -10.463506933440776, -9.793775538988212, -9.147882728147758, -8.563684843082553, -8.05901293203818, -7.637636953162294, -7.2978215675873255, -7.039591962149466, -6.86754750138297, -6.788012314879584, -6.801733990452555, -6.8952928478571405, -7.035103622825163, -7.167089681817972, -7.223081407600666, -7.132501186715206, -6.8358932327092425, -6.2961018097295165, -5.503687617001094, -4.475205840099676, -3.245484299414184, -1.8570888758457769, -0.350978655100196, 1.2383601377760183, 2.8819656015554633, 4.550733042921916, 6.208093581923961, 7.804845240901371, 9.279169356834556, 10.562867397382059, 11.592395774764183, 12.321302785847232, 12.729944946245041, 12.829169320912165, 12.656699214342014, 12.267485331266718, 11.7213352834618, 11.071943661019636, 10.36071803799454, 9.616822832475004, 8.86240547474459, 8.11997160082466, 7.41810209327188, 6.7924472827426685, 6.280901933973409, 5.914296510794437, 5.7058935125147725, 5.643691084008841, 5.688720882662215, 5.780478479343272, 5.848109690921511, 5.823942542149307, 5.655168404978151, 5.379525388863709, 5.006883829613938, 4.556093839494941, 4.048970006212073, 3.5056524039072157, 2.9427071436339522, 2.3741179651765787, 1.8141064089329655, 1.2799728253872895]

)
freq_filtered = np.array(
[0.0, 1.953125, 3.90625, 5.859375, 7.8125, 9.765625, 11.71875, 13.671875, 15.625, 17.578125, 19.53125, 21.484375, 23.4375, 25.390625, 27.34375, 29.296875, 31.25, 33.203125, 35.15625, 37.109375, 39.0625, 41.015625, 42.96875, 44.921875, 46.875, 48.828125, 50.78125, 52.734375, 54.6875, 56.640625, 58.59375, 60.546875, 62.5, 64.453125, 66.40625, 68.359375, 70.3125, 72.265625, 74.21875, 76.171875, 78.125, 80.078125, 82.03125, 83.984375, 85.9375, 87.890625, 89.84375, 91.796875, 93.75, 95.703125, 97.65625, 99.609375, 101.5625, 103.515625, 105.46875, 107.421875, 109.375, 111.328125, 113.28125, 115.234375, 117.1875, 119.140625, 121.09375, 123.046875, 125.0, 126.953125, 128.90625, 130.859375, 132.8125, 134.765625, 136.71875, 138.671875, 140.625, 142.578125, 144.53125, 146.484375, 148.4375, 150.390625, 152.34375, 154.296875, 156.25, 158.203125, 160.15625, 162.109375, 164.0625, 166.015625, 167.96875, 169.921875, 171.875, 173.828125, 175.78125, 177.734375, 179.6875, 181.640625, 183.59375, 185.546875, 187.5, 189.453125, 191.40625, 193.359375, 195.3125, 197.265625, 199.21875, 201.171875, 203.125, 205.078125, 207.03125, 208.984375, 210.9375, 212.890625, 214.84375, 216.796875, 218.75, 220.703125, 222.65625, 224.609375, 226.5625, 228.515625, 230.46875, 232.421875, 234.375, 236.328125, 238.28125, 240.234375, 242.1875, 244.140625, 246.09375, 248.046875, 250.0, 251.953125, 253.90625, 255.859375, 257.8125, 259.765625, 261.71875, 263.671875, 265.625, 267.578125, 269.53125, 271.484375, 273.4375, 275.390625, 277.34375, 279.296875, 281.25, 283.203125, 285.15625, 287.109375, 289.0625, 291.015625, 292.96875, 294.921875, 296.875, 298.828125, 300.78125, 302.734375, 304.6875, 306.640625, 308.59375, 310.546875, 312.5, 314.453125, 316.40625, 318.359375, 320.3125, 322.265625, 324.21875, 326.171875, 328.125, 330.078125, 332.03125, 333.984375, 335.9375, 337.890625, 339.84375, 341.796875, 343.75, 345.703125, 347.65625, 349.609375, 351.5625, 353.515625, 355.46875, 357.421875, 359.375, 361.328125, 363.28125, 365.234375, 367.1875, 369.140625, 371.09375, 373.046875, 375.0, 376.953125, 378.90625, 380.859375, 382.8125, 384.765625, 386.71875, 388.671875, 390.625, 392.578125, 394.53125, 396.484375, 398.4375, 400.390625, 402.34375, 404.296875, 406.25, 408.203125, 410.15625, 412.109375, 414.0625, 416.015625, 417.96875, 419.921875, 421.875, 423.828125, 425.78125, 427.734375, 429.6875, 431.640625, 433.59375, 435.546875, 437.5, 439.453125, 441.40625, 443.359375, 445.3125, 447.265625, 449.21875, 451.171875, 453.125, 455.078125, 457.03125, 458.984375, 460.9375, 462.890625, 464.84375, 466.796875, 468.75, 470.703125, 472.65625, 474.609375, 476.5625, 478.515625, 480.46875, 482.421875, 484.375, 486.328125, 488.28125, 490.234375, 492.1875, 494.140625, 496.09375, 498.046875]

)
amp_filtered = np.array(
[265.6024239271257, 286.2094793875442, 375.740242933325, 833.3814323726066, 956.9200549213626, 225.54378122329325, 100.25196820849483, 45.55956726168814, 8.535252561939672, 40.61703047213246, 358.99966568792075, 137.97012813890282, 64.46395558527304, 42.00802930199286, 30.51409130057035, 23.401045188306362, 18.57111937401492, 15.122528886019872, 12.593577655528238, 10.720291119856698, 9.342236180877757, 8.363425250286014, 7.742936837051983, 7.525537888778024, 8.040417748191167, 12.200881161151012, 7.447675534259931, 2.3920977222772635, 2.9520754461439025, 3.226238283799815, 3.357144491423323, 3.4189211392372316, 3.4405656489131586, 3.434521617168238, 3.406826152514309, 3.360997979720352, 3.299641414672502, 3.2251211017919004, 3.1398241265188935, 3.0462278939184624, 2.9468747943137394, 2.8443042457056356, 2.740969257352483, 2.6391528935642317, 2.5408936207421595, 2.4479247343139243, 2.361630624962241, 2.283020962855295, 2.2127226688499957, 2.1509886564986216, 2.0977216803693164, 2.052511150299004, 2.0146804185019436, 1.983341787849617, 1.9574563211442255, 1.9358954695767834, 1.9175016069591226, 1.9011447676276554, 1.8857732327685337, 1.8704560652359596, 1.8544162181193888, 1.8370533969578493, 1.8179564042384382, 1.796905209969161, 1.7738634532628221, 1.7489624723889179, 1.7224782742730198, 1.6948030821695912, 1.666413238721194, 1.6378352907755998, 1.6096120456202125, 1.5822702725590567, 1.5562915389450562, 1.53208742819921, 1.509980102910551, 1.4901888634307163, 1.4728230261087973, 1.4578811197379573, 1.4452560877020373, 1.43474589993692, 1.4260687355649462, 1.4188817048815388, 1.4128019468560602, 1.4074288707549458, 1.4023663092627714, 1.3972434129220888, 1.3917332355953542, 1.3855681288926576, 1.3785512690770099, 1.3705638706520467, 1.3615678840101932, 1.351604217619043, 1.3407867563287403, 1.3292926556424172, 1.31734956785766, 1.305220592382624, 1.2931878339363831, 1.2815354957672969, 1.270533429861535, 1.2604220140661702, 1.2513991309645203, 1.2436098909540219, 1.2371395796639377, 1.2320101262955945, 1.2281801943658384, 1.225548799934707, 1.2239621750554701, 1.2232234257282144, 1.2231043927836458, 1.2233590179127973, 1.2237374504278462, 1.2240001059254944, 1.2239309060970285, 1.2233489875427521, 1.2221182626303153, 1.2201543414997256, 1.2174284741777055, 1.2139683372925711, 1.2098556623336352, 1.205220872797758, 1.2002350571663476, 1.1950997453531467, 1.1900350709711347, 1.1852669847714523, 1.1810142317956824, 1.1774758138519377, 1.1748196294574913, 1.173172916924208, 1.172615026228243, 1.1731729169242366, 1.1748196294574627, 1.1774758138518802, 1.1810142317957375, 1.1852669847714241, 1.1900350709711287, 1.1950997453531396, 1.2002350571663465, 1.205220872797779, 1.2098556623336352, 1.2139683372925698, 1.217428474177695, 1.2201543414997253, 1.2221182626303169, 1.2233489875427577, 1.2239309060970285, 1.224000105925505, 1.2237374504278513, 1.2233590179127707, 1.223104392783649, 1.2232234257282033, 1.2239621750554666, 1.2255487999346806, 1.2281801943658381, 1.2320101262955965, 1.2371395796639466, 1.2436098909540356, 1.2513991309644983, 1.2604220140661724, 1.2705334298615267, 1.2815354957673124, 1.2931878339363831, 1.3052205923826394, 1.3173495678576568, 1.3292926556423905, 1.3407867563287248, 1.3516042176190457, 1.3615678840101986, 1.370563870652054, 1.37855126907701, 1.3855681288926556, 1.3917332355953416, 1.3972434129220785, 1.4023663092627232, 1.40742887075498, 1.412801946856072, 1.4188817048815374, 1.4260687355649462, 1.4347458999369256, 1.4452560877020246, 1.457881119737925, 1.4728230261088224, 1.4901888634307114, 1.5099801029105258, 1.532087428199201, 1.5562915389450567, 1.5822702725590483, 1.609612045620205, 1.6378352907756208, 1.666413238721163, 1.694803082169709, 1.7224782742730465, 1.7489624723888713, 1.7738634532628221, 1.7969052099692089, 1.8179564042384064, 1.837053396957685, 1.8544162181194346, 1.8704560652359927, 1.88577323276852, 1.9011447676276418, 1.9175016069591224, 1.9358954695767752, 1.9574563211442266, 1.9833417878496302, 2.0146804185019374, 2.052511150299002, 2.0977216803693044, 2.1509886564986185, 2.2127226688499957, 2.283020962855298, 2.361630624962242, 2.447924734313936, 2.5408936207421324, 2.63915289356423, 2.7409692573524733, 2.8443042457056253, 2.9468747943137394, 3.046227893918473, 3.139824126518916, 3.225121101791904, 3.299641414672509, 3.3609979797203433, 3.4068261525143244, 3.4345216171682296, 3.4405656489131586, 3.4189211392372374, 3.3571444914233175, 3.22623828379982, 2.9520754461439336, 2.3920977222772497, 7.4476755342599334, 12.200881161150996, 8.040417748191167, 7.525537888778042, 7.742936837051974, 8.363425250285996, 9.342236180877725, 10.720291119856741, 12.59357765552825, 15.122528886019865, 18.57111937401492, 23.401045188306373, 30.51409130057035, 42.00802930199289, 64.46395558527304, 137.9701281389028, 358.99966568792075, 40.61703047213247, 8.535252561939672, 45.55956726168817, 100.25196820849484, 225.54378122329325, 956.9200549213626, 833.3814323726066, 375.740242933325, 286.2094793875442]

)


plt.subplot(2,2,1)
plt.plot(dataTime)
plt.grid()
plt.title("data in time")

plt.subplot(2,2,3)
plt.plot(filtered)
plt.grid()
plt.title("filtered data in time")

plt.subplot(2,2,2)
plt.scatter(freq_origin, amp_origin)
plt.plot(freq_origin, amp_origin)
plt.grid()
plt.xlim(0, 100)
plt.title("amp - freq, 7/20/50")
plt.xticks(range(0, 100,5))

plt.subplot(2,2,4)
plt.scatter(freq_filtered, amp_filtered)
plt.plot(freq_filtered, amp_filtered)
plt.grid()
plt.xlim(0, 100)
plt.title("amp - freq, cutoff=25")
plt.xticks(range(0, 100,5))


plt.show()