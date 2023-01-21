color_list= ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
def value(colors):
    return color_list.index(colors[0])*10 + color_list.index(colors[1]) 
    #since we have to return 2 digit num, we add face value of 10 to index 0 (5 becomes 50, so 5-1 becomes 50+1=51)
