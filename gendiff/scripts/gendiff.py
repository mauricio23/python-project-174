import argparse 
import json

def definir_rutas():
    ruta_1 = r'C:\Users\MAURICIO\Documents\GitHub\python-project-174\file1.json'
    data_1 = json.load(open(ruta_1))
    print (data_1)
    
    ruta_2 = r'C:\Users\MAURICIO\Documents\GitHub\python-project-174\file2.json'
    data_2 = json.load(open(ruta_2))
    print (data_2)

    return ruta_1, ruta_2


def main():
   parser = argparse.ArgumentParser(
     description="Compares two configuration files and shows a difference."
     )
   ruta_1, ruta_2 = definir_rutas
  

   parser.add_argument(ruta_1, help="First file to compare")
   parser.add_argument(ruta_2, help="Second file to compare")
   
   args = parser.parse_args()
   
   
if __name__ == "__main__":
    main()