from  ..implementations import implem1

txt = """hey alors comment tu va salim , hey salim yeh cava ? 13 jours que je te cherche hoy""" 

assert(implem1.search("hey", txt, 101 ) == [0,32])


