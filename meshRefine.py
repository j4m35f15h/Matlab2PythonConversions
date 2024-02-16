# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 18:04:42 2024

@author: James
"""
import copy
def meshRefine(vertices,faces):
    """
    takes in the vertices nad faces isolated from an stl file, and removes 
    duplicate vertices and alters the corresponding face indices
    """
    #Create a copy of the original vertices, populated with zeros
    #for each vertex, look at the previous entries to see if there is a match
    #find the earliest match
    #set the value in the copy to the earlies match. Move onto the next value
    
    #To remove duplicate vertices, for each vertex identify the first duplicate,
    #and store the index

    simArray = [0 for _ in range(len(vertices))]
    for index,vertex in enumerate(vertices):
        for compIndex,backCompare in enumerate(vertices[0:index]):
            if (vertex==backCompare).all(): #If a duplicate is found...
                simArray[index] = compIndex #... store the index
                break
            simArray[index] = index #If no duplicate is found, store original index

    
    #We want to create a new vertices array consisting of the non zero values
    #As well as looking through faces, 
    #finding values that are the indexes for non-zeros values
    #and changing those values into the value stored in simArray
    newVertices = list()
    newFaces = copy.deepcopy(faces)

    # for index,newIndex in enumerate(simArray):
    #     if not newIndex:
    #         #newVertices.append(vertices[newIndex])
    #     # else:
    #         newVertices.append(vertices[index])
    # for faceCount,faceVals in enumerate(faces):
    #     for j,faceVerts in enumerate(faceVals):
    #         if simArray[faceVerts]:
    #             newFaces[faceCount][j]=simArray[faceVerts]
                
    #Ok we have changed some things, each element of simArray contains the 
    #index of the first vertex that represents it. We need to find the unique 
    #values and append those vertices onto the newVertices list.
    #Then we need to take that unique list and look up the faces.
    #We can keep the current loop, then use that unique list as a key, with the
    #index of the same value in the unique as the new face value.
    
    #find unique values in simArray, and store in new list.
    uniqEle = list(set(simArray))

    #Convert the original face values using our key identifying unique vertices
    for faceCount,faceVals in enumerate(faces):
        for j,faceVerts in enumerate(faceVals):
            newFaces[faceCount][j]=simArray[faceVerts]
    
    #Create the new vertex list and use the unique values to simplify the face list 
    for iPos,i in enumerate(uniqEle):
        newVertices.append(vertices[i]) #New vertex list consists of unique vertices
        for j,_ in enumerate(newFaces):
            for k in range(len(newFaces[0])):
                if newFaces[j][k]==i:  
                    newFaces[j][k] = iPos

    return [newVertices,newFaces]

