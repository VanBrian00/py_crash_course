cars = ['audi', 'bmw', 'subaru', 'toyota']
#di atas adalah pembuatan sebuah list
#dan memberikan isi list

for car in cars:
    #untuk car di dalam cars,
    #untuk melakukan perulangan sesuai jumlah isi list
    if car == 'bmw':
        #jika car isinya bmw maka,
        #semua huruf dalam car dijadikan kapital
        print(car.upper())
    else:
        #jika bukan bmw maka,
        #hanya huruf pertama yang jadi kapital
        print(car.title())
        print(car.title())