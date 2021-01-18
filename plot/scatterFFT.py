import matplotlib.pyplot as plt
import numpy as np

# y = 0.5 * sin(2 * pi * 7 * t) + 0.8 * cos(2 * pi * 10 * t) + 0.7 * cos(2 * pi * 30 * t);

# freq = list(range(128)) # ？？？ 如何标定
fs = 200 # freq of sample
N = 256 # number of samples
freq = np.array( list(range(0, int(N/2+1))) )* fs / N

y = np.array([

0.0, 0.054677889619590865, 0.24841459493719825, 0.6926294724432178, 1.672940189126083, 3.9353695741921975, 9.674794875902794, 26.953758120853873, 103.95759964008042, 474053.01458212733, 48.78333927423149, 1511.6514011929885, 60431.77825806253, 1.9854539306142636E7, 18140.7372784045, 1808.2955493641061, 436.6928672087645, 152.8489144605112, 64.63904644481593, 30.10041078649059, 14.475017198114017, 6.745406640107043, 2.767525209687222, 0.7939123978634498, 0.043757105457525994, 0.1858484575450997, 1.143695044770164, 3.039499801243146, 6.226215200043953, 11.422663928092089, 20.043710620041818, 34.996365796366824, 62.75972611295566, 119.55011430555763, 253.09467388185493, 641.5074757714555, 2260.617918294027, 16497.192195530934, 2010533.6383715787, 307413.53619820933, 4422.781229694036, 423.27887007487556, 67.29298052296163, 11.627827544223331, 1.3752332576844473, 5.840254121212924E-5, 0.4111267184190839, 1.0338819786035176, 1.5315769559639296, 1.8660011072572795, 2.0657487375973447, 2.1669743266442087, 2.199656359879369, 2.186014166482699, 2.1418252717072295, 2.078086896035051, 2.002396418502517, 1.919974036874393, 1.8343878308654815, 1.7480588801493901, 1.6626111222741686, 1.5791136491971407, 1.4982489623402393, 1.4204302708226793, 1.3458836151347084, 1.2747055980978952, 1.206904109425079, 1.1424271277163631, 1.0811831188281413, 1.02305548117131, 0.9679127550084701, 0.9156158061267465, 0.8660228419690701, 0.8189928718121773, 0.7743880489939625, 0.732075210238941, 0.6919268395353463, 0.6538216212643915, 0.617644702123589, 0.5832877487322478, 0.550648864097444, 0.5196324088559603, 0.4901487605833521, 0.4621140352240915, 0.43544978791537037, 0.4100827054993899, 0.385944299359977, 0.3629706045417408, 0.3411018891377064, 0.32028237650318564, 0.30045998181042805, 0.28158606370893835, 0.2636151913253924, 0.24650492645825314, 0.23021562056957484, 0.21471022600511777, 0.19995412076886837, 0.1859149461169421, 0.17256245621178767, 0.1598683790726089, 0.14780628807260401, 0.13635148326050914, 0.12548088181335623, 0.11517291696777505, 0.10540744481428274, 0.09616565837988457, 0.08743000846523652, 0.07918413074125387, 0.07141277864713659, 0.0641017616698061, 0.057237888616395866, 0.050808915526300354, 0.04480349789690596, 0.03921114692736941, 0.034022189509868364, 0.029227731723361575, 0.02481962560576907, 0.020790439004822525, 0.017133428324523758, 0.01384251400427222, 0.010912258585221943, 0.008337847233382663, 0.006115070605262273, 0.004240309955374536, 0.0027105243992564016, 0.0015232402575458526, 6.765424202108015E-4, 1.690676803388154E-4, 0.0, 1.6906768033877068E-4, 6.765424202109294E-4, 0.0015232402575457605, 0.0027105243992563994, 0.004240309955374796, 0.0061150706052625296, 0.008337847233382089, 0.01091225858522184, 0.01384251400427142, 0.01713342832452306, 0.020790439004821283, 0.024819625605768388, 0.029227731723360673, 0.03402218950986819, 0.03921114692736926, 0.04480349789690596, 0.050808915526300416, 0.05723788861639754, 0.06410176166980568, 0.07141277864713662, 0.0791841307412539, 0.08743000846523592, 0.09616565837988422, 0.10540744481428248, 0.11517291696777072, 0.12548088181335418, 0.1363514832605115, 0.14780628807260449, 0.15986837907260903, 0.17256245621178595, 0.18591494611694404, 0.19995412076886837, 0.21471022600511833, 0.2302156205695791, 0.246504926458255, 0.26361519132539146, 0.2815860637089355, 0.30045998181042216, 0.32028237650319114, 0.34110188913770617, 0.3629706045417424, 0.385944299359977, 0.4100827054993852, 0.4354497879153718, 0.46211403522409256, 0.49014876058334933, 0.5196324088559622, 0.550648864097444, 0.5832877487322476, 0.6176447021235878, 0.6538216212643707, 0.6919268395353497, 0.7320752102389373, 0.774388048993967, 0.8189928718121791, 0.8660228419690695, 0.9156158061267454, 0.9679127550084723, 1.023055481171308, 1.0811831188281376, 1.1424271277163445, 1.2069041094250783, 1.2747055980978956, 1.3458836151347084, 1.4204302708226728, 1.4982489623402468, 1.5791136491971676, 1.6626111222741642, 1.7480588801493748, 1.8343878308654888, 1.9199740368744058, 2.002396418502517, 2.078086896035037, 2.1418252717072375, 2.186014166482718, 2.199656359879381, 2.1669743266441976, 2.0657487375973633, 1.8660011072572438, 1.5315769559639296, 1.0338819786035256, 0.41112671841908016, 5.840254121154024E-5, 1.3752332576844561, 11.627827544223232, 67.2929805229619, 423.2788700748764, 4422.781229694036, 307413.5361982091, 2010533.638371578, 16497.192195530955, 2260.617918294027, 641.5074757714524, 253.09467388185504, 119.55011430555771, 62.75972611295566, 34.99636579636687, 20.04371062004188, 11.422663928092097, 6.2262152000439395, 3.039499801243124, 1.1436950447701502, 0.1858484575451087, 0.04375710545752627, 0.7939123978634597, 2.767525209687205, 6.745406640107101, 14.475017198114013, 30.100410786490666, 64.6390464448157, 152.8489144605108, 436.6928672087645, 1808.2955493641055, 18140.737278404515, 1.9854539306142636E7, 60431.77825806251, 1511.6514011929858, 48.783339274231324, 474053.01458212675, 103.95759964008045, 26.9537581208537, 9.674794875902831, 3.9353695741922046, 1.6729401891260818, 0.6926294724432064, 0.2484145949371982, 0.054677889619591996

])

print(len(y)) # 256

plt.scatter(freq,y[0:len(freq)])
plt.plot(freq,y[0:len(freq)])
plt.grid()
plt.show()


#
# clear all
# fs=100;%采样频率要大于等于原信号中最高频率的二倍
# N=128;%采样点数
# t=(0:N-1)/fs; # in matlab, left/right, all inclusive
# y=0.5*sin(2*pi*65*t)+0.8*cos(2*pi*40*t)+0.7*cos(2*pi*30*t);
# F=fft(y,N);
# freq=(0:N/2)*fs/N;%只画(0,fs/2)范围内的频率分量，起始坐标是0，因为只有(0,fs/2)范围内的频率才有意义
# stem(freq,abs(F(1:N/2+1)),'k');%依据频率坐标来绘制傅里叶变换后的信号的频率-幅度谱，注意F的起始坐标是1
# xlabel('频率(Hz)');
# ylabel('幅值');
# xlim([0 130]);
