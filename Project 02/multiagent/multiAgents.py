# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

#Question1: python autograder.py -q q1
class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        basicScore = successorGameState.getScore()
        foodLeft = float(newFood.count()) + 1
        basicScore = basicScore + (1/foodLeft)
        foodList = newFood.asList()
        nearestFood = float(minDistance(newPos,foodList)) + 1
        basicScore = basicScore +  (1/nearestFood)
        for eachGhost in newGhostStates:
            distance = float(manhattanDistance(newPos,eachGhost.getPosition())) + 1
            scaredTimer = eachGhost.scaredTimer
            if (distance < scaredTimer):
                basicScore = basicScore + (2.5/distance)
            else:
                basicScore = basicScore + (-2.5/distance)
        return basicScore
        #return successorGameState.getScore()

def minDistance(pos, locationList):
    minimumDist = float('inf')
    for each in locationList:
        distance = manhattanDistance(pos,each)
        if (distance <= minimumDist):
            minimumDist = distance
    return minimumDist

def maxDistance(pos, locationList):
    maximumDist = -float('inf')
    for each in locationList:
        distance = manhattanDistance(pos,each)
        if (maximumDist <= distance):
            maximumDist = distance
    return maximumDist

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

#Question2: python autograder.py -q q2 --no-graphics

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        pacmanindex = 0
        currentDepth = 1
        numberofAgents = gameState.getNumAgents()
        legalMoves = gameState.getLegalActions(pacmanindex)
        finalAction = None
        Score = -float('inf')
        for action in legalMoves:
            nextsuccessor = gameState.generateSuccessor(pacmanindex, action)
            bestScore = self.minmaxValue(nextsuccessor,pacmanindex,currentDepth,numberofAgents)
            if (bestScore >  Score):
                finalAction = action
                Score = bestScore
        return finalAction
        #util.raiseNotDefined()


    def minmaxValue(self,gameState,agentIndex,currentDepth,numberofAgents):
        newDepth = currentDepth
        if (agentIndex == numberofAgents - 1):
            if (currentDepth == self.depth):
                return self.evaluationFunction(gameState)
            else:
                newDepth = currentDepth + 1
        nextAgent = (agentIndex+1) % numberofAgents
        if (nextAgent == 0):
            return self.maxvalue(gameState,nextAgent,newDepth,numberofAgents)
        else:
            return self.minvalue(gameState,nextAgent,newDepth,numberofAgents)


    def maxvalue(self,gameState,agentIndex,currentDepth,numberofAgents):
        Score = -float('inf')
        actions = gameState.getLegalActions(agentIndex)
        if(len(actions) == 0):
            Score = self.evaluationFunction(gameState)
        for eachaction in actions:
            succ = gameState.generateSuccessor(agentIndex,eachaction)
            Score = max(Score,self.minmaxValue(succ,agentIndex,currentDepth,numberofAgents))
        return Score

    def minvalue(self,gameState,agentIndex,currentDepth,numberofAgents):
        Score = float('inf')
        actions = gameState.getLegalActions(agentIndex)
        if(len(actions) == 0):
            Score = self.evaluationFunction(gameState)
        for eachaction in actions:
            succ = gameState.generateSuccessor(agentIndex,eachaction)
            Score = min(Score,self.minmaxValue(succ,agentIndex,currentDepth,numberofAgents))
        return Score

#Question 3: python autograder.py -q q3 --no-graphics
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        pacmanindex = 0
        currentDepth = 1
        numberofAgents = gameState.getNumAgents()
        legalMoves = gameState.getLegalActions(pacmanindex)
        finalAction = None
        Score = -float('inf')
        alpha = -float('inf')
        beta = float('inf')
        for action in legalMoves:
          nextsuccessor = gameState.generateSuccessor(pacmanindex,action)
          bestScore,newalpha,newbeta = self.alphabetaValue(nextsuccessor,pacmanindex,currentDepth,numberofAgents,alpha,beta)
          if (bestScore > Score):
                finalAction = action
                Score = bestScore
          if bestScore > alpha :
                alpha = bestScore 
        return finalAction     
        #util.raiseNotDefined()

    def alphabetaValue(self,gameState,agentIndex,currentDepth,numofAgents,alpha,beta):
        newDepth = currentDepth
        if (agentIndex == numofAgents - 1):
          if (currentDepth == self.depth):
            return (self.evaluationFunction(gameState),alpha,beta)
          else:
            newDepth = currentDepth + 1
        nextAgent = (agentIndex + 1) % numofAgents
        if (nextAgent == 0):
            return self.alphaValue(gameState,nextAgent,newDepth,numofAgents,alpha,beta)
        else:
            return self.betaValue(gameState,nextAgent,newDepth,numofAgents,alpha,beta)
          
    def alphaValue(self,gameState,agentIndex,currentDepth,numofAgents,alpha,beta):
        Score = -float('inf')
        nextAlpha = alpha
        actions = gameState.getLegalActions(agentIndex)
        if (len(actions) == 0):
            Score = self.evaluationFunction(gameState)
        for eachAction in actions:
            succ = gameState.generateSuccessor(agentIndex,eachAction)
            Score = max((Score, self.alphabetaValue(succ,agentIndex,currentDepth,numofAgents,nextAlpha,beta)[0]))
            if (Score > beta):
                return (Score, nextAlpha, beta)
            nextAlpha = max(nextAlpha, Score)
        return (Score, nextAlpha, beta)

    def betaValue(self,gameState,agentIndex,currentDepth,numofAgents,alpha,beta):
        Score = float('inf')
        nextBeta = beta
        actions = gameState.getLegalActions(agentIndex)
        if (len(actions) == 0):
            Score = self.evaluationFunction(gameState)
        for eachAction in actions:
            succ = gameState.generateSuccessor(agentIndex,eachAction)
            Score = min((Score, self.alphabetaValue(succ,agentIndex,currentDepth,numofAgents,alpha,nextBeta)[0]))
            if (Score < alpha): 
                return (Score, alpha, nextBeta)
            nextBeta = min(nextBeta, Score)
        return (Score, alpha, nextBeta)       

#Question 4: python autograder.py -q q4 --no-graphics
class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        pacmanindex = 0
        currentDepth = 1
        numberofAgents = gameState.getNumAgents()
        legalMoves = gameState.getLegalActions(pacmanindex)
        finalAction = None
        Score = -float('inf')
        for action in legalMoves:
            nextSuccessor = gameState.generateSuccessor(pacmanindex,action)
            bestScore = self.expectimaxValue(nextSuccessor,pacmanindex,currentDepth,numberofAgents)
            if (bestScore > Score):
                finalAction = action
                Score = bestScore
        return finalAction
        #util.raiseNotDefined()

    def expectimaxValue(self,gameState,agentindex,currentDepth,numberofAgents):
        newDepth = currentDepth
        if (agentindex == numberofAgents - 1):
            if (currentDepth == self.depth):
                return self.evaluationFunction(gameState)
            else:
                newDepth = currentDepth + 1
        nextAgent = (agentindex + 1) % numberofAgents
        if (nextAgent == 0):
            return self.maxValue(gameState,nextAgent,newDepth,numberofAgents)
        else:
            return self.expValue(gameState,nextAgent,newDepth,numberofAgents)

    def maxValue(self,gameState,agentindex,currentDepth,numberofAgents):
        Score = -float('inf')
        actions = gameState.getLegalActions(agentindex)
        if (len(actions) == 0):
            Score = self.evaluationFunction(gameState)
        for eachaction in actions:
            succ = gameState.generateSuccessor(agentindex,eachaction)
            Score = max((Score,self.expectimaxValue(succ,agentindex,currentDepth,numberofAgents)))
        return Score

    def expValue(self,gameState,agentindex,currentDepth,numberofAgents):
        Score = 0
        actions = gameState.getLegalActions(agentindex)
        numActions = float(len(actions))
        if (numActions == 0):
            Score = self.evaluationFunction(gameState)
        else:
            probability = 1/numActions
        for eachAction in actions:
            succ = gameState.generateSuccessor(agentindex,eachAction)
            Score = Score + (probability * self.expectimaxValue(succ,agentindex,currentDepth,numberofAgents))
        return Score

#Question 5: python autograder.py -q q5 --no-graphics
def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    powerPellets = currentGameState.getCapsules()

    basicScore = currentGameState.getScore()
    numFood = float(newFood.count()) + 1
    basicScore += (1 / numFood)
    foodList = newFood.asList()
    
    # food with weight 1
    nearestFood = float(maxDistance(newPos, foodList)) + 1
    basicScore = basicScore + (1/nearestFood)

    # power pellet with weight 2
    nearestPowerpill = float(minDistance(newPos, powerPellets)) + 1
    basicScore = basicScore + (2/nearestPowerpill)

    # ghost with weight 4
    for eachGhost in newGhostStates:
        distance = float(manhattanDistance(newPos, eachGhost.getPosition())) + 1
        scaredTimer = eachGhost.scaredTimer
        if (distance < scaredTimer):
            basicScore = basicScore + (4/distance)
        else:
            basicScore = basicScore + (-4/distance)
    return basicScore
    #util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

