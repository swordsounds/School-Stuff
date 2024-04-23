from multiprocessing import Process
import dataGenerator as data
import playground as Graph

def function():
    data.main()
    
def main():
    p = Process(target=function)
    p.start()
    Graph.main()
    
if __name__ == "__main__":
     main()