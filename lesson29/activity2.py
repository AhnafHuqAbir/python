class Bangladesh:
    def capital(self):
        print("Dhaka is the capital of Bangladesh")

    def language(self):
        print('Bangla is the offical language of Bangladesh')
    
    def type(self):
        print("Bangladesh is a developing country")

class China:
    def capital(self):
        print("Beijing is the capital of China")

    def language(self):
        print('Mandarin is the national language of China')

    def type(self):
        print("China is a highly advanced in tecnology country")

obj_bangladesh = Bangladesh()
obj_Chi = China()

for country in (obj_bangladesh, obj_Chi):
    country.capital()
    country.language()
    country.type()