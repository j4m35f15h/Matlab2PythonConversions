# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 17:57:15 2024

@author: James
"""
import numpy as np

def evenOut(xInput,yInput,nSeg = 1000):
    """
    Takes two lists/numpy arrays containing coordinates decribing a path,
    and re-creates a new path made up of a different number of 
    coordinates
    """
    # Create the framework to assign the coordinates. First the input coordinates as well as the potential
    #  new coordinates are converted into relative positions, proportions along the original path with 
    # values between 0 and 1
    
    if type(xInput) == list:
        xInput = np.array(xInput)
    if type(yInput) == list:
        yInput = np.array(yInput)
    
    relMarker = np.cumsum(np.power(np.power(np.diff(xInput),2) + np.power(np.diff(yInput),2),0.5))
    
    distanceTotal = relMarker[-1]
    relMarker = relMarker/distanceTotal
    relMarker = np.append(0,relMarker)
    
    # Create a variable relPositions that stores between which of the original coordinates the new point lies between
    segmentPosition = np.array(range(nSeg))
    segmentPosition = segmentPosition/(nSeg-1)
    relPosition = [0 for _ in range(len(segmentPosition))]
    for i in range(len(segmentPosition)):
        for j in range(len(relMarker)):
            if segmentPosition[i] < relMarker[j]:
                relPosition[i] = j-1
                break
    relPosition[-1] = relPosition[-2]
    
    
    # Next subtract the "relPosition" index relative marker from the segmentPosition,
    # then find the difference in relPosition with the next marker. The new
    # coordinate is then the relPosition + the subtraction*the difference
    
    newXCoord = [0 for _ in range(nSeg)]
    newYCoord = [0 for _ in range(nSeg)]
    
    for i in range(len(newXCoord)):
        if relMarker[relPosition[i]]+1 > len(xInput):
            newXCoord[i] = xInput(relMarker[relPosition[i]])
            newYCoord[i] = yInput(relMarker[relPosition[i]])
            break
        relDiff = (segmentPosition[i] - relMarker[relPosition[i]])/(relMarker[relPosition[i]+1] - relMarker[relPosition[i]])
        newXCoord[i] = xInput[relPosition[i]] + relDiff*(xInput[relPosition[i]+1]-xInput[relPosition[i]])
        newYCoord[i] = yInput[relPosition[i]] + relDiff*(yInput[relPosition[i]+1]-yInput[relPosition[i]])
    
    return [newXCoord,newYCoord]
