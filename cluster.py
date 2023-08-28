
from curvas import *
from collections import deque


class Cluster:

    curvas={}

    totalX = float(0)
    totalY= float(0)
    totalT= float(0)
    curvaModelo = None

    def __init__(curvaBase):

        self.curvas = {curvaBase}
        self.totalX = curvaBase.B.x
        self.totalY = curvaBase.B.y
        self.totalT = curvaBase.t
        self.curvaModelo = curvaBase 

    def combine(self , cluster2):
        self.curvas = curvas.union(cluster2.curva)
        self.totalX += cluster2.totalX
        self.totalY += cluster.totalY
        self.totalT += cluster.totalT

        n = len(self.curvas)
        self.curvaModelo.B = Point(self.totalX/n , self.totalY/n)
        self.curvaModelo.t = self.totalT/n

    def toList(self):
        cluster=deque()
        for curva in self.curvas:
            cluster.append((curva.id , self.curvaModelo.compare(curva)))
        return cluster

def merge(clusters1 , clusters2 , corte):

    newClusters = array.array()

    for i in range(len(clusters1)):
        maxIndex = int(-1)
        maxSimilitud =  float(0)
        modelo1 = clusters1[i].curvaModelo

        for j in range(len(clusters2)):

            modelo2 = clusters1[i].curvaModelo
            similitud = modelo1.compare(modelo2)

            if similitud > maxCoincidense:
                maxIndex = j
                maxSimilitud = similitud
        
        if (maxIndex > -1) and (maxSimilitud >= corte):
            clusters2[maxIndex].combine(clusters1[i])

        else:
            newClusters.append(clusters1[i])

    newClusters = newClusters + clusters2
    return newClusters



def clustering(  clusters  , corte ):

    if len(clusters) >1:

        q = math.floor((clusters.length)/2)
        clusters1 = clustering( clusters[0, q] , corte)
        clusters2 = clustering( clusters[q+1, len(clusters)-1] , corte)
        newCluster = merge(clusters1,clusters2 , corte)
        return newCluster
    
    return clusters


def solucion (curvas):

    clustersUnit = array.array()
    i = int(i)

    for curva in curvas:
        curva.normalize()
        curva.id = i
        clustersUnit.append(curva)
        i+=1
    
    clusters = clustering(clustersUnit , 0.5)
    similares = array.array()
    diferentes = array.array()

    for cluster in clusters:

        if len(cluster.curvas) > 1:
            clusterList = cluster.toList()
            similares.append(clusterList)
        
        else:
            curvaDif = cluster.curvas.popleft()
            diferentes.append(curvaDif.id)
    
    return (similares , diferentes)