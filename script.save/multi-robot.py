# hpp-manipulation-server
# gepetto-viewer-server
from hpp.corbaserver.manipulation.pr2 import Robot
from hpp.corbaserver.manipulation import ProblemSolver, ConstraintGraph
from hpp.gepetto.manipulation import ViewerFactory
from hpp.gepetto import PathPlayer

# 2}}}

# Load PR2 and a box to be manipulated. {{{2
class Box (object):
  rootJointType = 'planar'
  packageName = 'hpp_tutorial'
  meshPackageName = 'hpp_tutorial'
  urdfName = 'box'
  urdfSuffix = ""
  srdfSuffix = ""

class Environment (object):
  packageName = 'iai_maps'
  meshPackageName = 'iai_maps'
  urdfName = 'kitchen_area'
  urdfSuffix = ""
  srdfSuffix = ""

robot = Robot ('pr2-box', 'pr2')
ps = ProblemSolver (robot)
## ViewerFactory is a class that generates Viewer on the go. It means you can
## restart the server and regenerate a new windows.
## To generate a window:
## fk.createRealClient ()
fk = ViewerFactory (ps)

fk.loadObjectModel (Box, 'box')

robot.setJointBounds ("pr2/base_joint_xy", [-2,2,-2,2])
robot.setJointBounds ("box/base_joint_xy", [-2,2,-2,2])

q0 = robot.getCurrentConfig ()
q1 = q0[::]
q0 [0] = -1
q0 [1] = -1
q0 [-4] = -1
q0 [-3] = 1
q1 [0] = 1
q1 [1] = 1
q1 [-4] = 1
q1 [-3] = -1
r = fk.createViewer ()
graph = ConstraintGraph (robot, 'graph')
graph.createNode (['free'])
graph.createEdge ('free', 'free', 'move_free', 1)

#ps.client.basic.problem.selectPathValidation ("Progressive", 0.02)
res= ps.directPath (q0,q1,True)

pp = PathPlayer (ps.client.basic, r)

# robot.isConfigValid (q)
# returns: (False, 'Joint box/base_joint_xyz, rank: 0, value out of range: 1 not in [-5.1, -2]')

# robot.rootJointType
# returns: {'box': 'freeflyer', 'pr2': 'planar'}

