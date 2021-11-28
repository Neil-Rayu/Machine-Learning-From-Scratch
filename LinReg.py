import math
class ScatterPlot:
    def __init__(self, points):
        self.points = points
        self.pointsX = points[0]
        self.pointsY = points[1]
        self.meanX = self.mean(self.pointsX)
        self.meanY = self.mean(self.pointsY)
        self.SDx = self.standardDev(self.pointsX, self.meanX)
        self.SDy = self.standardDev(self.pointsY, self.meanY)
        self.r = self.correlation()
        self.info = self.scatterInfo()
        self.slope = self.r*(self.SDy/self.SDx)
        self.regression = self.LSRL()
        
    def mean(self, points):
        sum = 0
        for p in points:
            sum+=p
        return (sum/len(points))
    def standardDev(self, points, mean):
        sumOfSquares = 0
        for p in points:
            sumOfSquares+= ((p-mean) ** 2)
        return math.sqrt(sumOfSquares/len(points))
    def correlation(self):
        zSum = 0
        for i in range (len(self.pointsX)):
            zSum += (((self.points[0][i]-self.meanX)/self.SDx) * ((self.points[1][i]-self.meanY)/self.SDy))
        return zSum/(len(self.points))
    def scatterInfo(self):
        return "This Scatter plots has:\nMean(X): " + str(round(self.meanX, 3)) +"\nMean(Y): "+ str(round(self.meanY, 3)) + "\nStandard Deviation(X): "+ str(round(self.SDx, 3)) + "\nStandard Deviation(Y): "+ str(round(self.SDy, 3)) +"\nCorrelation: "+ str(round(self.r, 3))
    def LSRL(self):
        yInt = self.meanY-(self.slope*self.meanX)
        return "y = " + str(round(self.slope, 3)) + "x + " + str(round(yInt, 3))
    def perdictLSRL(self):
        predictions = []
        for x in self.points:
            predictions.append(self.slope*x + self.yInt)
        return predictions


scatter = ScatterPlot([[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4,5]])
print(scatter.SDx)
print(scatter.regression)
scatter2= ScatterPlot([[14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1,23.4,18.1,22.6,17.2], [215,325,185,332,406,522,412,614,544,421,445,408]])
print(scatter2.info)
print(scatter2.regression)

