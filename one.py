import pulp

lp_prob = pulp.LpProblem("max",pulp.LpMaximize)

x=pulp.LpVariable('x',lowBound=0)
y=pulp.LpVariable('y',lowBound=0)

lp_prob += 3*x + 2*y ,"z"

lp_prob += 2*x + y <= 20
lp_prob += 4*x - 5*y >= -10

lp_prob.slove()

print("x =",x.varValue)
print("y =",y.varVariable)
print("max =",pulp.value(lp_prob.objective))



































