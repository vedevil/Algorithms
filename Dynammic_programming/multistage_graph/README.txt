Program is divided into 3 steps:
Step 1: Taking vertices stage-wise
Step 2:Taking edges of each vertices individually
Step 3: Main step of the algo
for each vertices, ceck all its edges
and min of edge+incient_vertex_cost
Do the above step in backward direction

Here DP works as we are uilding large solution by using values of small solutions.That is the reason we are performing in reverse order.

##Input format
Line 1 takes input of no of the stages(n)
Next n lines takes vertices stagewise

Let no of vertices=v
Next v line takes input as edges of each vertex.
