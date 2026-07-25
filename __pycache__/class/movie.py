class movie:
    def __init__(self,name,directorname,rating):
        self.name = name 
        self.directorname = directorname
        self.rating = rating
    def display(self):
        print("name",self.name)
        print("directorname",self.directorname)
        print("rating",self.rating)
L1 = movie("fidaa","sri",100)
L1.display()
L2 = movie("mitra","aman",60)
L2.display()