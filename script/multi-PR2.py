# hpp-manipulation-server
# gepetto-viewer-server
from hpp.corbaserver.manipulation.pr2 import Robot
from hpp.corbaserver.manipulation import ProblemSolver, ConstraintGraph
from hpp.gepetto.manipulation import ViewerFactory
from hpp.gepetto import PathPlayer

# 2}}}
class PR2Robot (Robot):
  rootJointType = 'planar'
  packageName = 'pr2_description'
  meshPackageName = 'pr2_description'
  urdfName = 'pr2'
  urdfSuffix = ""
  srdfSuffix = ""


# Load PR2 and a box to be manipulated. {{{2
multiRobot = Robot ('multiRobot', 'r1')
multiRobot.setJointBounds ("r1/base_joint_xy", [-2,2,-2,2])

# ps = ProblemSolver (multiRobot )
# fk = ViewerFactory (ps)
# r = fk.createViewer ()
# graph = ConstraintGraph (multiRobot , 'graph')
# graph.createNode (['free'])
# graph.createEdge ('free', 'free', 'move_free', 1)
# pp = PathPlayer (ps.client.basic, r)
# pp(0)


ps = ProblemSolver (multiRobot )
fk = ViewerFactory (ps)

#Robot.rootJointType = "planar"
fk.loadObjectModel (Robot, 'r2')

multiRobot.setJointBounds ("r2/base_joint_xy", [-2,2,-2,2])

multiRobot.insertRobotModel ('r2', 'planar', "pr2_description", "pr2", "", "")

q0 = multiRobot.getCurrentConfig ()
q1 = q0[::]
q0 [0] = -1
q0 [1] = -1
q1 [0] = 1
q1 [1] = 1
q0 [40] = 1
q0 [41] = 1
q1 [40] = -1
q1 [41] = -1

r = fk.createViewer ()
graph = ConstraintGraph (multiRobot , 'graph')
graph.createNode (['free'])
graph.createEdge ('free', 'free', 'move_free', 1)
pp = PathPlayer (ps.client.basic, r)
pp(0)
res= ps.directPath (q0,q1,True)

pp = PathPlayer (ps.client.basic, r)

# robot.isConfigValid (q)
# returns: (False, 'Joint box/base_joint_xyz, rank: 0, value out of range: 1 not in [-5.1, -2]')

# robot.rootJointType
# returns: {'box': 'freeflyer', 'pr2': 'planar'}

pp(0)

