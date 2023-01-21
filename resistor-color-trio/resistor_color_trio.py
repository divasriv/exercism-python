color_list= ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
def label(colors):
    val=color_list.index(colors[0])*10 + color_list.index(colors[1]) 
    zeros= 10**color_list.index(colors[2])
    res=zeros*val
    if res>1000:
        return str(res//1000)+" kiloohms"
    return str(res)+" ohms"

# a=label(["yellow", "violet", "yellow"])
# print(a)
