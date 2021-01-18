import numpy as np

arr1 = np.array([[0.22927,0.0,6.91,0.0,0.448,6.03,85.5,5.6894,3.0,233.0,17.9,392.74,18.8]])
# numpy是行优先。而spark.Matrix shi列优先
pc0 = np.array([[
-0.030207238874172204,
0.0501830099189622,
-0.02861127367767564,
5.9372131130511546E-5,
-4.552794497627223E-4,
0.001373139463546815,
-0.08178591632005172,
0.006585743284361312,
-0.045684999171098854,
-0.9425888639299169,
-0.006017826894890262,
0.3127697279835974,
-0.024375731309160622,
-6.165691462730084E-4,
-0.008233382521712638,
0.004359001858899733,
3.7786528532853816E-5,
-1.0963588402364502E-5,
-5.519718174856994E-4,
0.015979821978806298,
-7.156274812693516E-4,
0.010790372438654853,
0.3127102682535292,
0.003826768928946668,
0.9495895766768271,
-0.00418389784625391,
0.010132775824737376,
-0.6664213593101804,
0.0860268024208513,
8.013600095825718E-4,
0.0018040405873372921,
-0.00433947336342097,
0.7274990781615227,
-0.047481072719487386,
-0.006202545339559497,
-0.09894127741906204,
0.010442165128367742,
0.014524207621661102,
0.08184961726883333,
-0.038701140639467106,
-0.7384171365975143,
0.01219120030502666,
-8.989024268910383E-4,
-9.281764521358324E-4,
-0.006947327955392623,
-0.6705718864961391,
9.895860122463886E-4,
0.016333097003798813,
0.019089601158585427,
0.034353227640579645,
-0.001986828342185375,
-0.039508036130044485,
-0.9591747496316944,
0.013422456145093478,
0.04121354987591742,
0.001740242402345059,
-7.22205739989249E-6,
0.008926950079226639,
0.051820378632934413,
0.007248079901810749,
-0.13516087259284515,
0.03443872851724117,
-0.01953906781531176,
-0.012319591122533335,
-0.23515195174770345
]])
pc1 = pc0.reshape(5,13);

pc = np.transpose(pc1) # pca matrix
# print(pc)
# print(pc.shape)

# print(pc)
# print(pc.shape)
#
# print(arr1)
# print(arr1.shape)

pcFeatures = np.matmul(arr1, pc)
print(pcFeatures)
print(pcFeatures.shape)
