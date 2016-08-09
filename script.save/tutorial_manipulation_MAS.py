
from hpp.corbaserver.manipulation import Client as ManipClient
from hpp.corbaserver.manipulation import Robot as ManipRobot

mcl = ManipClient()
mcl.problem.selectProblem("manip")


ManipRobot.packageName = "hpp_tutorial"
ManipRobot.meshPackageName = "pr2_description"
ManipRobot.rootJointType = "planar"
ManipRobot.urdfName = "pr2"
ManipRobot.urdfSuffix = ""
ManipRobot.srdfSuffix = ""



manipRobot = ManipRobot ("robot-name", "agent1")


