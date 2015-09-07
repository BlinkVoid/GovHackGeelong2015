# -*- coding: utf-8 -*-
"""
Finding path for stormwater drain
"""
import math

class FindingPath:

    def __init__(self, pointFile, segmentFile):
        self.readPoints(pointFile)
        self.readSegments(segmentFile)
        self.createConnectionList()
        
    def readPoints(self, fileName):
        f = open(fileName, 'r')
        lines = f.readlines()
        self.points = []

        for line in lines:
            l = line.split(',');
            x = float(l[0])
            y = float(l[1])
            self.points.append([x,y])
                        
    def readSegments(self, fileName):
        f = open(fileName, 'r')
        lines = f.readlines()
        self.segments = []

        for line in lines:
            l = line.split(',');
            p1 = int(l[0])
            p2 = int(l[1])            
            self.segments.append([p1,p2])   
            
    def createConnectionList(self):
        self.connections = []
        for i in range(len(self.points)):
            self.connections.append([])
            
        for i in range(len(self.segments)):
            p1 = self.segments[i][0]
            p2 = self.segments[i][1]
            self.connections[p1].append(p2)              
            
    def findNearestPoint(self,x,y):
        pos = 0
        dx = self.points[pos][0] - x
        dy = self.points[pos][1] - y
        minDistance = math.sqrt(dx*dx + dy*dy)
        
        for i in range(1,len(self.points)):
            dx = self.points[i][0] - x
            dy = self.points[i][1] - y
            distance = math.sqrt(dx*dx + dy*dy)       
            if (distance < minDistance):
                pos = i
                minDistance = distance
                
        return pos
        
    def printPath(self, path):
        s = '';
        for i in range(len(path)):
            p = path[i]
            x = self.points[p][0]
            y = self.points[p][1]
            s = s + str(x) + ' ' + str(y) + ' ';
        
        return s.strip()

    def findingDownstream(self, x, y):
        p = self.findNearestPoint(x,y)
        path = [p]
        while (len(self.connections[p]) > 0):
            p = self.connections[p][0]
            path.append(p)
            
        return self.printPath(path)
    


