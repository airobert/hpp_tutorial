#Robert White
#LAAS-CNRS
#gepetto-viewer-server
#hppcorbaserver

from hpp.corbaserver.pr2 import Robot
robot = Robot ('pr2')
robot.setJointBounds ("base_joint_xy", [-4, -3, -5, -3])

from hpp.corbaserver import ProblemSolver
ps = ProblemSolver (robot)

from hpp.gepetto import ViewerFactory
vf = ViewerFactory (ps)

q_init = robot.getCurrentConfig ()
q_goal = q_init [::]
q_init [0:2] = [-3.2, -4]
rank = robot.rankInConfiguration ['torso_lift_joint']
q_init [rank] = 0.2
vf (q_init)

q_goal [0:2] = [-3.2, -4]
rank = robot.rankInConfiguration ['l_shoulder_lift_joint']
q_goal [rank] = 0.5
rank = robot.rankInConfiguration ['l_elbow_flex_joint']
q_goal [rank] = -0.5
rank = robot.rankInConfiguration ['r_shoulder_lift_joint']
q_goal [rank] = 0.5
rank = robot.rankInConfiguration ['r_elbow_flex_joint']
q_goal [rank] = -0.5
vf (q_goal)

vf.loadObstacleModel ("iai_maps", "kitchen_area", "kitchen")
vf.loadObstacleModel ("hpp_tutorial", "bigbox", "bb")

ps.setInitialConfig (q_init)
ps.addGoalConfig (q_goal)

ps.selectPathPlanner ("VisibilityPrmPlanner")
ps.addPathOptimizer ("RandomShortcut")
#if you can't find the name of your object
#vf.problemSolver.client.obstacle.getObstacleNames(False, 1000)
boxconfig = vf.problemSolver.client.obstacle.getObstaclePosition("bb/base_link_0")


r = vf.createViewer()
vf.moveObstacle("bb/base_link_0",[-3.5, -3, 0.3, 1, 0, 0, 0])
r.computeObjectPosition() # this is to update the object's position in the viewer


# r.problemSolver.moveObstacle("bb", [0, 0, 0, 1])

# there is no direct path connecting them
#ps.directPath(q_init, q_goal, True)


print ps.solve ()
# ps.numberPaths()
# ps.pathLength(2)



from hpp.gepetto import PathPlayer
pp = PathPlayer (robot.client, r)
# r(q_init)
# r(q_goal)
pp (0)
# pp (1)

vf.moveObstacle("bb/base_link_0",[-3.5, -5, 0.3, 1, 0, 0, 0])
r.computeObjectPosition() 