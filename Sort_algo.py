#selection sort

def selection_sort(n):
    for i in range(len(n)):
        min_idex=i
        for j in range(i+1,len(n)):
            if n[j]<n[min_idex]:
                min_idex=j
                n[i],n[min_idex]=n[min_idex],n[i]
    return n
n=[5,7,10,2,8,1]
print(selection_sort(n))





#bubble sort
def bubble_sort(n):
    for i in range(len(n)-1):
        for j in range(len(n)-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n
n=[2,8,3,1,9,5]
print(bubble_sort(n))