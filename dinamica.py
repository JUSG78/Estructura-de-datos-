class MemoriaDinamica:
    def main(self, args):
        
        frutas = []
        
        frutas.append("Mango")
        
        frutas.append("Manzana")
        
        frutas.append("Pera")
        
        frutas.append("Uvas")
        
        print(frutas)
        
        del frutas[0]
        del frutas[0]
        
        frutas.append("sandia")
        
        print(frutas)

if __name__ == "__main__":
    MemoriaDinamica().main([])
