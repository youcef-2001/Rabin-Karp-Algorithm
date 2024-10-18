from  ..implementations.implem1 import search

txt = """hey alors comment tu va salim , hey salim yeh cava ? 13 jours que je te cherche hoy""" 

assert (search("hey", txt, 101 ) == [0,9])


