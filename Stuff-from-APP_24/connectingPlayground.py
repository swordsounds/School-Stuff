from multiprocessing import Process
import playground as Graph
import dataGenerator as data

def process():
    data.main()

if __name__ == "__main__":
    Graph.main()
    p = Process(target=process)
    p.start()