import numpy as np
import random
                                  #mathplot library    
random.seed(1)

#class of the reinforcement model 
class PolyaUrnModel:
    def __init__(self, init_balls, reinforcement_matrix, num_paths):
        self.init_balls = init_balls   #a list of the intitialization: each ith element of the list is the number of balls for the ith type
        self.reinforcement_matrix = reinforcement_matrix
        self.num_paths = num_paths
        self.iterations =iterations
        self.n = len(init_balls) # number of types 
        self.count_object = {i : self.init_balls[i] for i in range((self.n))} #urn dictionary,starting from ball of type 0 to (number of types-1)

    def ratiox(first, *others): 
        'Calculate the ratio x_n'
        total = first + sum(others)
        return first / total
                     
    def simulate(self,iterations):
        "Runs one polya urn simulation for a fixed number of iterations"
        #itere=[[] for i in range(n+2)]#to disregard the zero i+1 bc of 0
        #itek=[[ratiox(init_list[i+1],)]]
        #itere[0]=[ratiox(t1_0,t2_0,t3_0)] #with only initial distribution
        #itere[1]=[x_n(t2_0,t1_0,t3_0)]
        #itere[2]=[x_n(t3_0,t1_0,t2_0)]
        
        for i in range(iterations):
            list_obj=[i for i in range(len(self.count_object))] #the list of types
            values=list(self.count_object.values())
            w=np.array(values) /sum(values) 
            rand=random.choices(list_obj,weights=w,k=1)[0]
            #count_object[rand]+=1
            for element in count_object:
                count_object[element] += self.reinforcement_matrix[rand][element]
                #itere[element].append(ratiox(count_object[element],count_object[]))
                        
            #itere[0].append(x_n(count_object[1],count_object[2],count_object[3]))
            #itere[1].append(x_n(count_object[2],count_object[1],count_object[3]))
            #itere[2].append(x_n(count_object[3],count_object[1],count_object[2]))
        
        values_f=list(self.count_object.values())
        wi=np.array(values_f) /sum(values_f) 
        
        return count_object,wi #,itere[0],itere[1],itere[2]


    

 

#there is a problem with this function
def unique_positive_left_eigenvector(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix.T)
    positive_eigenvalues = eigenvalues[np.where(eigenvalues > 0)]
    positive_left_eigenvector = eigenvectors[:, np.where(eigenvalues == positive_eigenvalues)]
    positive_left_eigenvector = positive_left_eigenvector[:, 0].real
    positive_left_eigenvector /= np.sum(positive_left_eigenvector)
    return positive_left_eigenvector

def multi_path(iterations):
        "runs simulation across multiple random paths"
        path_list=[]
        
        for _ in range(paths_no+1):  #multiple paths
            liste=polya_urn_model.simulate(iterations)
            path_list.append(liste[1])

            #at the end of the iterations number add the fraction xn along that path
        return path_list

def list_type(l):
    num=len(l[0])
    a=[]
    for i in range(len(l)):
        a.append([])
        for j in range(num):
            a[i].append(l[i][j])
    return a 


#[0.38379594 0.23240812 0.38379594]



iterations = 200000
num_paths=1000  #number of paths (states of the world)
init_balls=[1,1,1]
reinforcement_matrix=np.array([
                   [10,3,6],
                   [1,10,1],
                   [6,1,10]   
                   ])

polya_urn_model = PolyaUrnModel(init_balls, reinforcement_matrix, num_paths)
polya_urn_model.simulate(iterations)
li=polya_urn_model.simulate(iterations)
labels = 'Color 1', 'Color 2', 'Color 3'
sizes = [mean(li[i]) for i in range(len(li))]
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.4f%%')
#diagonal is the reinforcement of the one selected (not the one you return)

#default value of A
#A=np.ones((n, n*n))

#changing the initial allocation 
#Case 1: diago>off diagonal
#generate distributions for the non-deterministic
#Case 2 : alpha=1,beta=0 ->RV (distribution of Xn) dep on initial allocation
#reinforcement 2.1 : identity matrix 
#reinforcement 2.2 : scaled indentity matrix
#Case 3 : both 1,2 which one dominates , try different cases of reinforcement

#robustness 
#robustness 1: concentrated days/less concentrated days
