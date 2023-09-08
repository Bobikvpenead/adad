class People():


    def __init__(self,name,phone,city,country):
        self.name = name
        self.phone = phone
        self.city = city
        self.country = country

    def show_info(self):
        print("name",self.name)
        print("phone",self.phone)
        print("city",self.city)
        print("country",self.country)


myClass = People("Грінченко Дмитро Дмитрович","066831327","Дніпро","Україна")
myCLass.show_info()