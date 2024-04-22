import unittest
from kwargs import search_data, database


class TestKwargs(unittest.TestCase):

    def test_picasso(self):
        result = search_data("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(result,{
            "persona1":{
                    "primer_nombre":"Pablo",
                    "segundo_nombre":"Diego",
                    "primer_apellido":"Ruiz",
                    "segundo_apellido":"Picasso"
                    }})

    def test_roman(self):
        result = search_data("Lionel", "Andres", "Messi", "Cuchitinni", **database)
        self.assertEqual(result,{
            "persona2":{
                    "primer_nombre":"Lionel",
                    "segundo_nombre":"Andres",
                    "primer_apellido":"Messi",
                    "segundo_apellido":"Cuchitinni"
                    }})
        
    def test_none(self):
        result = search_data("Dario", "Reynoso", "Riquelme", "Dionisio", **database)
        self.assertEqual(result,None)

    def test_none2(self):
        result = search_data("Jorge", "Roman", "Castro", "Gomez", **database)
        self.assertEqual(result,None)

    def test_osvaldo(self):
        result = search_data("Osvaldo", "Cerro", **database)
        self.assertEqual(result,{
            "persona3":{
                    "primer_nombre":"Osvaldo",
                    "primer_apellido":"Cerro",
                    }})
        
    def test_rodolfo(self):
        result = search_data("Luis", "Damian", "Rodolfo", "Lucero", "Perez", **database)
        self.assertEqual(result,{
            "persona4":{
                    "primer_nombre":"Luis",
                    "segundo_nombre":"Damian",
                    "tercer_nombre":"Rodolfo",
                    "primer_apellido":"Lucero",
                    "segundo_apellido":"Perez"
                    }})


if __name__ == "__main__":
    unittest.main()