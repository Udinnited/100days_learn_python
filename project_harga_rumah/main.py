import requests
from contextlib import closing
import csv
# STEP 1: 
# Baca file "harga_rumah.txt"
url = "https://storage.googleapis.com/dqlab-dataset/harga_rumah.txt"
data_harga_rumah = []
with closing(requests.get(url, stream=True)) as r:
    f = (line.decode('utf-8') for line in r.iter_lines())
    data_harga_rumah = [row for row in csv.reader(f)]



# Buat list of dict dengan nama harga rumah
key_harga_rumah = data_harga_rumah[0]
harga_rumah = []
for baris_harga_rumah in harga_rumah[1:]:
	dict_harga_rumah = dict()
	for i in range(len(dict_harga_rumah)):
		dict_harga_rumah[key_harga_rumah[i]] = baris_harga_rumah[i]
	harga_rumah.append(i)
print(key_harga_rumah)
# # STEP 2:
# # Buat fungsi  get_all_specified_attribute yang menerima parameter list_of_dictionary 
# # (tipe data list yang berisikan sekumpulan tipe data dictionary) dan specified_key 
# # (tipe data string). Fungsi akan mengembalikan sebuah list yang berisikan seluruh 
# # atribut dengan kunci (key) specified_key. 
# def get_all_specified_attributes(___, ___):
# 	list_attributes = []
# 	for data in ___:
# 		attribute = data[___]
# 		list_attributes.append(___)
# 	return ___
# # STEP 3: 
# # Buat fungsi fungsi min_value yang menerima parameter list_attributes (berupa 
# # tipe data list) dan mengembalikan nilai terkecil dalam list_attributes 
# def min_value(___):
# 	min_attribute = 9999
# 	for attr in ___:
# 		if int(attr) < min_attribute:
# 			min_attribute = ___
# 	return ___
# # Buat fungsi dan max_value yang menerima parameter list_attribute dan 
# # mengembalikan nilai terbesar dalam list_attributes.	
# def max_value(___):
# 	max_attribute = -9999
# 	for attr in ___:
# 		if int(attr) > max_attribute:
# 			max_attribute = ___
# 	return ___
# # STEP 4: 
# # Buat fungsi transform_attribute yang menerima parameter attr (sebuah 
# # bilangan), max_attr (sebuah bilangan) dan min_attr (sebuah bilangan) 
# # yang mengembalikan nilai transformasi dari sebuah attribute.
# def transform_attribute(___, ___, ___):
# 	nilai_transformasi = (attr - min_attr) / (max_attr - min_attr)
# 	return ___
# # STEP 5:
# # Buat fungsi data_transformation yang menerima parameter list_of_dictionary 
# # (sebuah list yang berisikan tipe data dictionary) dan list_attribute_names 
# # (sebuah list yang berisikan tipe data string) mengembalikan hasil 
# # transformasi data dari list_of_dictionary berdasarkan list_attribute_names 
# # dan attr_info telah dispesifikasikan.
# def data_transformation(___, ___):
# 	attr_info = {}
# 	for attr_name in ___:
# 		specified_attributes = get_all_specified_attributes(___, ___)
# 		max_attr = max_value(___)
# 		min_attr = min_value(___)
# 		attr_info[attr_name] = {'max': ___, 'min': ___}
# 		data_idx = 0
# 		while(data_idx < len(___)):
# 			list_of_dictionary[data_idx][attr_name] = transform_attribute(int(list_of_dictionary[___][___]), ___, ___)
# 			data_idx += 1
# 	return list_of_dictionary, attr_info
# # STEP 6:
# # Berdasarkan data baru dan attr_info ini, buat fungsi transform_data yang
# # menerima parameter data dan attr_info dan mengembalikan nilai atribut 
# # dari data baru yang telah ditransformasikan.
# def transform_data(___, ___):
# 	for key_name in ___:
# 		data[key_name] = (data[key_name] - attr_info[key_name]['min']) / (
# 		                  attr_info[key_name]['max'] - attr_info[key_name]['min'])
# 	return ___
# # STEP 7:
# # Buat fungsi yang digunakan untuk sistem prediksi harga berdasarkan 
# # nilai kemiripan atribut, yaitu argument input data dan list_of_data!
# def abs_value(___):
# 	if value < 0:
# 		return -value
# 	else:
# 		return value
# def price_based_on_similarity(___, ___):
# 	prediksi_harga = 0
# 	perbedaan_terkecil = 999
# 	for data_point in list_of_data:
# 		perbedaan= abs_value(data['tanah'] - data_point['tanah'])
# 		perbedaan+= abs_value(data['bangunan'] - data_point['bangunan'])
# 		perbedaan+= abs_value(data['jarak_ke_pusat'] - data_point['jarak_ke_pusat'])
# 		if perbedaan < perbedaan_terkecil:
# 			prediksi_harga = data_point['harga']
# 			perbedaan_terkecil = perbedaan
# 	return ___
# # STEP 8:
# # Hitung harga rumah yang telah ditransformasikan ke dalam variabel 
# # harga_rumah berikut dengan atributnya attr_info
# harga_rumah, attr_info = data_transformation(___, ['tanah','bangunan','jarak_ke_pusat'])
# # Gunakan variabel data untuk memprediksi harga rumah
# data = {'tanah': 110, 'bangunan': 80, 'jarak_ke_pusat': 35}
# # Transformasikan data tersebut dengan dengan menggunakan attr_info yang telah 
# # diperoleh yang kembali disimpan ke variabel data.
# data = transform_data(___, ___)
# # Hitunglah prediksi harga dari variabel data tersebut.
# harga = price_based_on_similarity(___, ___)
# print("Prediksi harga rumah: ", harga)