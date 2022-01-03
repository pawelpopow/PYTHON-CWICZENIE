from object_oriented_programming.lister import Lister           # otrzymanie klasy narzędzi


class Super:

     def __init__(self):         # superklasa __init__
         self.data1 = "mielonka"

class Sub(Super, Lister):        # wmieszanie __repr__

     def __init__(self):         # Lister ma dostęp do self
         Super.__init__(self)
         self.data2 = "jajka"    # więcej attr przykładu
         self.data3 = 42

