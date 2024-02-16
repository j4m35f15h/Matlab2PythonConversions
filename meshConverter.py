# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:52:46 2024

@author: James
"""


import numpy as np
def meshConverterBasic(mesh_object):
    """
    Converts vectors describing faces of a mech into a vertex,face representation
    Basic form that allows vertex duplicates. For large meshes, duplicate
    vertices can be removed to improve computational load
    """
    #Each element of mesh_object.vectors represents a different face
    #Each element of the face is a separate vector
    
    vertices = list()
    faces = list()
    for faceInd in mesh_object.vectors: 
        temp = list()
        for faceVert in faceInd:#read through each face
            vertices.append(faceVert)#add each element to the vertices list
            temp.append(len(vertices)-1)
        faces.append(temp)#For meshes that contain duplicates, add the index to the face list
    return [vertices,faces]

