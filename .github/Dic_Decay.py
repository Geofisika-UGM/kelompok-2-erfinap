# Tabel Periodik
nama= input("Nama unsur : ")

data= {
    'Uranium238'  : ['U', 92, 238],
    'Thorium234' : ['Th', 90, 234],
    'Protactinium234' : ['Pa', 91, 234],
    'Uranium234'  : ['U', 92, 234],
    'Thorium230' : ['Th', 90, 230],
    'Radium226' : ['Ra', 88, 226],
    'Radon222' : ['Rn', 86, 222],
    'Polonium218' : ['Po', 84, 218],
    'Plumbum214' : ['Pb', 82, 214],
    'Thalium214' : ['Tl', 83, 214],
    'Plumbum214' : ['Pb', 84, 214],
    'Bismuth210' : ['Bi', 81, 210],
    'Polonium210' : ['Po', 82, 210],
    'Bismuth210' : ['Bi', 83, 210],
    'Plumbum206' : ['Pl', 82, 206],

}

if nama in data.keys() :
    print("Simbol : ", data[nama][0], "\nNomor atom :",data[nama][1], "\nMassa atom : ",data[nama][2],)
else:
    print ('tidak ditemukan')