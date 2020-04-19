'''
Created on Apr 13, 2020

@author: sameeksha 
'''


class ModelBasedReflexAgent(object):
    def __init__(self, locA_st, locB_st, vaccumLocation):
        self.currentstate={'loc_A':locA_st,
                       'loc_B':locB_st,
                       'current_location':vaccumLocation}
        self.total_cost=0
        self.actions=[]
    def doAction(self):
        if self.currentstate['loc_A'] == self.currentstate['loc_B'] == 'clean':
            return 'no operation'
        elif self.currentstate['current_location'] == 0:
            if self.currentstate['loc_A']=='dirty':
                self.actions.append("suck")
                self.currentstate['loc_A']='clean'
                self.total_cost+=1
                # move to B
                self.total_cost+=1
                self.actions.append("right")
                # if B is Dirty
                if self.currentstate['loc_B'] == 'dirty':
                    self.actions.append("suck")
                    # suck and mark clean
                    self.currentstate['loc_B']='clean'
                    self.total_cost+=1
                    return self.total_cost, self.actions
                
            else:
                # move to B
                self.actions.append("right")
                self.total_cost+=1
                # if B is Dirty
                if self.currentstate['loc_B'] == 'dirty':
                    self.actions.append("suck")
                    # suck and mark clean
                    self.currentstate['loc_B']='clean'
                    self.total_cost+=1
                    return self.total_cost, self.actions
                
        elif self.currentstate['current_location'] == 1:
            if self.currentstate['loc_B']=='dirty':
                self.actions.append("suck")
                self.currentstate['loc_B']='clean'
                self.total_cost+=1
                # move to A
                self.total_cost+=1
                self.actions.append("left")
                # if A is Dirty
                if self.currentstate['loc_A'] == 'dirty':
                    self.actions.append("suck")
                    # suck and mark clean
                    self.currentstate['loc_A']='clean'
                    self.total_cost+=1
                    return self.total_cost, self.actions
                
            else:
                # move to A
                self.actions.append("left")
                self.total_cost+=1
                # if A is Dirty
                if self.currentstate['loc_A'] == 'dirty':
                    self.actions.append("suck")
                    # suck and mark clean
                    self.currentstate['loc_A']='clean'
                    self.total_cost+=1
                    return self.total_cost, self.actions
                
'''
test cases
'''
                
agent1=ModelBasedReflexAgent("clean","clean",0)
print(agent1.doAction())

agent2=ModelBasedReflexAgent("dirty","dirty",0)
agent2.doAction()
print('total cost:{}  actions:{}'.format(agent2.total_cost,agent2.actions))

                 
agent3=ModelBasedReflexAgent("clean","dirty",0)
agent3.doAction()
print('total cost:{}  actions:{}'.format(agent3.total_cost,agent3.actions))
                
agent4=ModelBasedReflexAgent("dirty","clean",0)
agent4.doAction()
print('total cost:{}  actions:{}'.format(agent4.total_cost,agent4.actions))         
            
agent5=ModelBasedReflexAgent("clean","clean",1)
print(agent5.doAction())

agent6=ModelBasedReflexAgent("dirty","dirty",1)
agent6.doAction()
print('total cost:{}  actions:{}'.format(agent6.total_cost,agent6.actions))

                 
agent7=ModelBasedReflexAgent("clean","dirty",1)
agent7.doAction()
print('total cost:{}  actions:{}'.format(agent7.total_cost,agent7.actions))
                
agent8=ModelBasedReflexAgent("dirty","clean",1)
agent8.doAction()
print('total cost:{}  actions:{}'.format(agent8.total_cost,agent8.actions))