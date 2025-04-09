from cleanfid import fid 

# score_fid_11inputan = fid.compute_fid()
# score_kid_11inputan = fid.compute_kid()


# FID dan KID Untuk 2 Inputan
score_fid_2inputan = fid.compute_fid('/home/ta2122-s1si-106/Dataset_test_FID/2_inputan_sadumangkola', '/home/ta2122-s1si-106/FIDImage/2inputan/*')
score_kid_2inputan = fid.compute_kid('/home/ta2122-s1si-106/Dataset_test_FID/2_inputan_sadumangkola', '/home/ta2122-s1si-106/FIDImage/2inputan/*')

# FID dan KID untuk 11 inputan Random
# score_fid_11inputan = fid.compute_fid('/home/ta2122-s1si-106/Dataset_test_FID/11_inputan_random', '/home/ta2122-s1si-106/FIDImage/11inputan')
# score_kid_11inputan = fid.compute_kid('/home/ta2122-s1si-106/Dataset_test_FID/11_inputan_random', '/home/ta2122-s1si-106/FIDImage/11inputan')

# # FID dan KID untuk Sadumangkola part 1
# score_fid_sadumangkola1 = fid.compute_fid('/home/ta2122-s1si-106/Dataset_test_FID/Sadumangkola','/home/ta2122-s1si-106/FIDImage/sadumangkolapart1')
# score_kid_sadumangkola1 = fid.compute_kid('/home/ta2122-s1si-106/Dataset_test_FID/Sadumangkola','/home/ta2122-s1si-106/FIDImage/sadumangkolapart1')

# # FID dan KID untuk Sadumangkola part 2
# score_fid_sadumangkola2 = fid.compute_fid('/home/ta2122-s1si-106/Dataset_test_FID/Sadumangkola','/home/ta2122-s1si-106/FIDImage/sadumangkolapart2')
# score_kid_sadumangkola2 = fid.compute_kid('/home/ta2122-s1si-106/Dataset_test_FID/Sadumangkola','/home/ta2122-s1si-106/FIDImage/sadumangkolapart2')

# # FID dan KID untuk Batak Karo
# score_fid_karo = fid.compute_fid('/home/ta2122-s1si-106/Dataset_test_FID/BatakKaro','/home/ta2122-s1si-106/FIDImage/batakkaro')
# score_kid_karo = fid.compute_kid('/home/ta2122-s1si-106/Dataset_test_FID/BatakKaro','/home/ta2122-s1si-106/FIDImage/batakkaro')

# # FID dan KID untuk Batak simalungun
# score_fid_simalungun = fid.compute_fid('/home/ta2122-s1si-106/Dataset_test_FID/BatakSimalungun','/home/ta2122-s1si-106/Stylegannoprogrssive/StyleGAN-Tensorflow/results')
# score_kid_simalungun = fid.compute_kid('/home/ta2122-s1si-106/Dataset_test_FID/BatakSimalungun','/home/ta2122-s1si-106/Stylegannoprogrssive/StyleGAN-Tensorflow/results')

print('score_fid_2inputan:',score_fid_2inputan)
print('score_kid_2inputan:',score_kid_2inputan)
# print('score_fid_11inputan:',score_fid_11inputan)
# print('score_kid_11inputan:',score_kid_11inputan)
# print('score_fid_sadumangkola1:',score_fid_sadumangkola1)
# print('score_kid_sadumangkola1:',score_kid_sadumangkola1)
# print('score_fid_sadumangkola2:',score_fid_sadumangkola2)
# print('score_kid_sadumangkola2:',score_kid_sadumangkola2)
# print('score_fid_karo:',score_fid_karo)
# print('score_kid_karo:',score_kid_karo)
# print('score_fid_simalungun:',score_fid_simalungun)
# print('score_kid_simalungun:',score_kid_simalungun)