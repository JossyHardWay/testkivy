from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

makanan = [
    {"nama": "Ayam Geprek", "harga": 15000},
    {"nama": "Ayam Cabe", "harga": 10000},
    {"nama": "Ayam Goreng", "harga": 13000},
    {"nama": "Ayam Bakar", "harga": 12000},
    {"nama": "Ayam Kecap", "harga": 17000},
    {"nama": "Ayam Suwir", "harga": 13000},
]

class PembelianMakananApp(App):
    def build(self):
        self.antrian = []
        
        layout = BoxLayout(orientation='vertical', padding=10)

        self.label_nomor = Label(text="Nomor Pembeli: ")
        layout.add_widget(self.label_nomor)
        
        self.input_nama = TextInput(multiline=False)
        layout.add_widget(self.input_nama)
        
        self.button_beli = Button(text="Beli", on_press=self.on_beli)
        layout.add_widget(self.button_beli)
        
        self.label_makanan = Label(text="Daftar Makanan:")
        layout.add_widget(self.label_makanan)

        self.buttons_makanan = []
        for mkn in makanan:
            btn = Button(text=mkn["nama"] + " - Rp " + str(mkn["harga"]), on_press=self.on_pilih_makanan)
            self.buttons_makanan.append(btn)
            layout.add_widget(btn)
        
        self.button_hapus = Button(text="Hapus Antrian", on_press=self.on_hapus_antrian)
        layout.add_widget(self.button_hapus)
        
        self.button_tampilkan_antrian = Button(text="Tampilkan Antrian", on_press=self.on_tampilkan_antrian)
        layout.add_widget(self.button_tampilkan_antrian)
        
        self.label_antrian = Label(text="Antrian:")
        layout.add_widget(self.label_antrian)
        
        return layout
    
    def on_beli(self, instance):
        nomor_pembeli = len(self.antrian) + 1
        nama_pembeli = self.input_nama.text
        makanan_dipilih = self.label_makanan.text
        total_harga = self.hitung_total_harga(makanan_dipilih)
        self.antrian.append({"nomor": nomor_pembeli, "nama": nama_pembeli, "makanan": makanan_dipilih, "total_harga": total_harga})
        self.label_nomor.text = "Nomor Pembeli: " + str(nomor_pembeli)
        self.input_nama.text = ""
        self.label_makanan.text = "Daftar Makanan:"

    def on_pilih_makanan(self, instance):
        makanan_dipilih = instance.text.split(" - ")[0]
        self.label_makanan.text += "\n- " + makanan_dipilih

    def on_hapus_antrian(self, instance):
        if len(self.antrian) > 0:
            self.antrian.pop(0)
            if len(self.antrian) > 0:
                self.label_nomor.text = "Nomor Pembeli: " + str(self.antrian[0]["nomor"])
            else:
                self.label_nomor.text = "Nomor Pembeli: "

    def on_tampilkan_antrian(self, instance):
        self.label_antrian.text = "Antrian:\n"
        for pesanan in self.antrian:
            self.label_antrian.text += "Nomor: " + str(pesanan["nomor"]) + " - Nama: " + pesanan["nama"] + "\n"
            self.label_antrian.text += "Makanan: " + pesanan["makanan"] + "\n"
            self.label_antrian.text += "Total Harga: Rp " + str(pesanan["total_harga"]) + "\n\n"

    def hitung_total_harga(self, makanan_dipilih):
        harga_total = 0
        makanan_list = makanan_dipilih.split("\n")
        for makanan_item in makanan_list:
            makanan_nama = makanan_item.strip("- ")
            for mkn in makanan:
                if mkn["nama"] == makanan_nama:
                    harga_total += mkn["harga"]
        return harga_total
    
PembelianMakananApp().run()
