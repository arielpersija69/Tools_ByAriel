import os, sys

print ("\033[1;32mSilahkan Masukkan Nama Admin& Password Admin")

print ("\033[1;32atau silahkan Hubungi Ariel Sandy Permana ")

username = 'Ariel'      

password = 'Ganteng'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("Nama Admin : ")

	if uname == username:

		pwd = raw_input("Password admin : ")



		if pwd == password:

			print "\033[1;32mAlhmdllh sudah masuk juga..", 

			sys.exit()



		else:

			print "\033[1;32mMaaf Password Yang Anda Masukkan Salah... [?]\033[00m"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[1;32mMaaf Password Yang Anda Masukkan salah... [?]\033[00m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()

