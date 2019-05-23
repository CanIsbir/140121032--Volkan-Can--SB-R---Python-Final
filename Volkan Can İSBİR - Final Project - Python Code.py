# -*- coding: utf-8 -*-
"""
Created on Sunday 19/05/2019

@author: Can*/
"""
import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

df=pd.read_excel('Coordinates.xlsx','Sayfa1')
xy_coordinates=df.as_matrix()
Coordinates=xy_coordinates


df1=pd.read_excel('distancematrix.xls','Sayfa1')
distances1=df1.as_matrix()
distances=[]


n=len (xy_coordinates)-1

for i in range(len (distances1)-1):
    distances1[i+1][i+2]=0
for i in range (len (distances1)-1):
    distances.append(distances1[i+1][2:])
Distances=np.asanyarray(distances)


def route (n):
    
    cities = np.arange(n)
    
    np.random.shuffle(cities)
     
    cities = np.append(cities,cities[0])    
    
    return cities

def distance (aroute):
    
    totalroad = 0
    
    for i,j in zip(aroute[:-1],aroute[1:]):
        totalroad = totalroad + Distances[i][j]
    
    return totalroad


def drawn_route (aroute):
    
    #drawn path for first elementh
    
    for i,j in zip(aroute[:-1],aroute[1:]):
        plt.plot([Coordinates[i][1],Coordinates[j][1]],[Coordinates[i][0],Coordinates[j][0]],'-o')
    plt.show()
    

def creatingbetterpath(path1, path2,t):
    path1 = path1[:-1]
    path2 = path2[:-1]
    dist=[]
    
    for i,j in zip(path1[:-1],path1[1:]):
        dist.append( Distances[i][j])
    s     = np.random.randint(80)
    
    path31 = np.hstack((path1[:s], path2[s:]))
    unique, counts = np.unique(path31, return_counts=True)
    d = dict(zip(unique, counts))
   
    replacewith=[]
    for i in d:
        if d[i]==2:
            replacewith.append(i)
    
    if len(set(path31))!=len(set(path2)):
        missing = list(set(path1)-set(path31))
       
        for i,j in zip(replacewith,missing):
            
            index=np.where(path31==i)[0][0]
                                        
            path31[index]=j               
            
    path32 = np.hstack((path1[:s], path2[s:]))
    unique, counts = np.unique(path32, return_counts=True)
    d = dict(zip(unique, counts))
    replacewith=[]
    
    for i in d:
        if d[i]==2:
            replacewith.append(i)
    if len(set(path32))!=len(set(path2)):
        missing = list(set(path1)-set(path32))
       
        for i,j in zip(replacewith,missing):
            
            index=np.where(path32==i)[0][1]
                        
            path32[index]=j
                                   
    if distance(path31)   <    distance(path32):
        path3=path31
        
    else:
        path3=path32
                                   
    a,b,c,d= np.random.randint(0,n-t, 4)
    for i,j in zip (np.arange(a,c+t),np.arange(b,d+t)):
        path3[i],path3[j] = path3[j], path3[i]
                 
    path3 = np.append(path3,path3[0])
    return path3


def get_population_performance(population):
    # returns an array that stores the performance,ie total distances,
    # of each path of a population
    perf = []
    for i in population:
        perf.append(distance(i))
    return np.array(perf)


def sort_population(population):
    #sort the population according to totaldistances
    performance = get_population_performance(population)
    i = np.argsort(performance)
    return population[i]


def create_initial_population(n):
    #creates and sorts an initial population of size n.
    
    population = []
    l=81
    for i in range(n):
        p = route(l)
        population.append(p)
    population=np.array(population)
    population = sort_population(population)    
    return population

def geneticexchange(path1, path2):
    path1 = path1[:-1]
    path2 = path2[:-1]
    s     = np.random.randint(0,n)
    path3 = np.hstack((path1[:s], path2[s:]))
    unique, counts =np.unique(path3, return_counts=True)
    d = dict(zip(unique,counts))
    replacewith=[]
    for i in d:
        if d[i] == 2:
            replacewith.append(i)
    if len(set(path3)) != len(set(path2)):
        missing = list(set(path1)-set(path3))
        for i,j in zip(replacewith,missing):
            if np.random.rand()>.5:
                index = np.where(path3==i)[0][0]
            else:
                index = np.where(path3==i)[0][1]
            path3[index] = j
    chance = np.random.rand()
    if chance > 0.9:
        a,b = np.random.randint(0,n-2,2)
        for i,j in zip (np.arange(a,a+2), np.arange(b,b+2)):
            path3[i],path3[j] = path3[j], path3[i]
    elif chance > 0.8 and chance <= 0.9:
        a,b = np.random.randint(0,n-5,2)
        for i,j in zip (np.arange(a,a+5), np.arange(b,b+5)):
            path3[i],path3[j] = path3[j], path3[i]
    elif chance > 0.7 and chance <= 0.8:
        a,b = np.random.randint(0,n-8,2)
        for i,j in zip (np.arange(a,a+8), np.arange(b,b+8)):
            path3[i],path3[j] = path3[j], path3[i]    
    elif chance > 0.6 and chance <= 0.7:
        a,b = np.random.randint(0,n-15,2)
        for i,j in zip (np.arange(a,a+15), np.arange(b,b+15)):
            path3[i],path3[j] = path3[j], path3[i]        
    elif chance > 0.4 and chance <= 0.6:
        a,b = np.random.randint(0,n-25,2)
        for i,j in zip (np.arange(a,a+25), np.arange(b,b+25)):
            path3[i],path3[j] = path3[j], path3[i]    
    elif chance > 0.3 and chance <= 0.4:
        a,b = np.random.randint(0,n-30,2)
        for i,j in zip (np.arange(a,a+30), np.arange(b,b+30)):
            path3[i],path3[j] = path3[j], path3[i]
    elif chance > 0.2 and chance <= 0.3:
        a,b = np.random.randint(0,n-35,2)
        for i,j in zip (np.arange(a,a+35), np.arange(b,b+35)):
            path3[i],path3[j] = path3[j], path3[i]
    elif chance <= 0.2:
        a,b = np.random.randint(0,n-37,2)
        for i,j in zip (np.arange(a,a+37), np.arange(b,b+37)):
            path3[i],path3[j] = path3[j], path3[i]
    path3 = np.append(path3,path3[0])
    return path3

def cyclic_change(population,n,t):
    # reproduces the best n individuals of a population
    # to produce n*n new indivioduals and sorts the new population
    # return the sorted new population
    
    population=population[:n]
    newpop = []
    for i in population:
        for j in population:
            newpop.append(creatingbetterpath(i,j,t))
    newpop = np.array(newpop)
    newpop = sort_population(newpop)
    return newpop


n           = 81
population  = create_initial_population(500)
performance_list = []
population1=[]

for i in range(40):
   
    population = cyclic_change(population,25,1)
    performance_list.append(distance(population[0]))
    plt.plot(performance_list,'.-')
    plt.show()
    for t in range (10):
        population = cyclic_change(population,27,0)
        population = cyclic_change(population,27,1)
        population = cyclic_change(population,27,2)
        population = cyclic_change(population,27,3)
        population = cyclic_change(population,27,i+1)
        drawn_route(population[0])
        print('Trying ', (10)*i+t+1, 'best total distance %5.2f'% distance(population[0]),'km.')

goodroute= population[0]
goodroute = np.delete(goodroute,81)
for i,j in enumerate(goodroute):
    if j==5:
        locationofankara = i
        
firstpart = goodroute[locationofankara:]
secondpart = goodroute[:locationofankara]
goodroute = np.append(firstpart,secondpart)
goodroute= np.append(goodroute,5)    
print("The best route is ",goodroute+1)









