#Robert White
#LAAS-CNRS
#gepetto-viewer-server
#hppcorbaserver

# from hpp.corbaserver import Client

# cl = Client ()



from hpp.corbaserver.pr2 import Robot
from hpp.corbaserver import ProblemSolver
from hpp.gepetto import ViewerFactory
from hpp.gepetto import PathPlayer

def all_in_one (index):
	robot = Robot ('pr2')
	robot.setJointBounds ("base_joint_xy", [-4, -3, -5, -3])
	ps = ProblemSolver (robot)
	vf = ViewerFactory (ps)
	#TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
	vf.loadObstacleModel ("iai_maps", "kitchen_area", "kitchen")
	vf.loadObstacleModel ("hpp_tutorial", "bigbox", "bb")
	vf.moveObstacle("bb/base_link_0",[-3.5, -5, 0.3, 1, 0, 0, 0])
	q_init = robot.getCurrentConfig ()
	q_goal = q_init [::]
	q_init [0:2] = [-3.2, -4]
	rank = robot.rankInConfiguration ['torso_lift_joint']
	q_init [rank] = 0.2
	vf (q_init) # What is this line about?
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
	if (index == 0):
		ps.setInitialConfig(q_init)
		ps.addGoalConfig (q_goal)
	else :
		ps.setInitialConfig (q_goal)
		ps.addGoalConfig(q_init)
	# vf.problemSolver.client.problem.selectProblem("1")
	ps.selectPathPlanner ("VisibilityPrmPlanner")
	ps.addPathOptimizer ("RandomShortcut")
	#if you can't find the name of your object
	#vf.problemSolver.client.obstacle.getObstacleNames(False, 1000)
	#boxconfig = vf.problemSolver.client.obstacle.getObstaclePosition("bb/base_link_0")
	r = vf.createViewer()
	# r.computeObjectPosition() 
	print ps.solve ()
	pp = PathPlayer (robot.client, r)
	pp (0)


robot_init = Robot ('pr2')
robot_init.client.problem.selectProblem('1')
all_in_one(0)
#TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
robot_init.client.problem.selectProblem("2")
robot_init.client.problem.getSelected('problem')
all_in_one(1)
