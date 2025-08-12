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

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getAvailableActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateNextState(agentIndex, action):
        Returns the nextState game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        def minimax(agentIndex, depth, state):
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state), None

            if agentIndex == 0:
                return max_value(agentIndex, depth, state)
            else:
                return min_value(agentIndex, depth, state)

        def max_value(agentIndex, depth, state):
            actions = state.getAvailableActions(agentIndex)
            if not actions:
                return self.evaluationFunction(state), None

            v = float('-inf') # negative infinity as start value
            best_action = None

            for action in actions:
                successor = state.generateNextState(agentIndex, action)
                nextAgent = (agentIndex + 1) % state.getNumAgents()
                nextDepth = depth + 1 if nextAgent == 0 else depth
                value, _ = minimax(nextAgent, nextDepth, successor)

                if value > v:
                    v = value
                    best_action = action

            return v, best_action

        def min_value(agentIndex, depth, state):
            actions = state.getAvailableActions(agentIndex)
            if not actions:
                return self.evaluationFunction(state), None

            v = float('inf')
            best_action = None

            for action in actions:
                successor = state.generateNextState(agentIndex, action)
                nextAgent = (agentIndex + 1) % state.getNumAgents()
                nextDepth = depth + 1 if nextAgent == 0 else depth
                value, _ = minimax(nextAgent, nextDepth, successor)

                if value < v:
                    v = value
                    best_action = action

            return v, best_action

        return minimax(0, 0, gameState)[1]
        #util.raiseNotDefined()


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        def minimax(agentIndex, depth, state, alpha, beta):
            if state.isWin() or state.isLose() or depth == self.depth:
                score = self.evaluationFunction(state)
                return score, None

            if agentIndex == 0:
                return max_value(agentIndex, depth, state, alpha, beta)
            else:
                return min_value(agentIndex, depth, state, alpha, beta)

        def max_value(agentIndex, depth, state, alpha, beta):
            max_score = float('-inf') # negative infinity as start value
            best_action = None
            actions = state.getAvailableActions(agentIndex)

            for action in actions:
                successor = state.generateNextState(agentIndex, action)
                nextAgent = (agentIndex + 1) % state.getNumAgents()
                nextDepth = depth + 1 if nextAgent == 0 else depth

                score, _action = minimax(nextAgent, nextDepth, successor, alpha, beta)

                if score > max_score:
                    max_score = score
                    best_action = action

                if max_score > beta: # prune
                    return max_score, best_action
                alpha = max(alpha, max_score)

            return max_score, best_action

        def min_value(agentIndex, depth, state, alpha, beta):
            min_score = float('inf') # positive infinity as start value
            best_action = None
            actions = state.getAvailableActions(agentIndex)

            for action in actions:
                successor = state.generateNextState(agentIndex, action)
                nextAgent = (agentIndex + 1) % state.getNumAgents()
                nextDepth = depth + 1 if nextAgent == 0 else depth

                score, _action = minimax(nextAgent, nextDepth, successor, alpha, beta)

                if score < min_score:
                    min_score = score
                    best_action = action

                if min_score < alpha: # prune
                    return min_score, best_action
                beta = min(beta, min_score)

            return min_score, best_action

        final_score, chosen_action = minimax(0, 0, gameState, float('-inf'), float('inf'))
        return chosen_action
        #util.raiseNotDefined()


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

        def expectimax(agentIndex, depth, state):
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state), None

            if agentIndex == 0: # pacman
                return max_value(agentIndex, depth, state)
            else: # ghosts
                return expect_value(agentIndex, depth, state)

        def max_value(agentIndex, depth, state):
            v = float('-inf') # negative infinity as start value
            best_action = None
            actions = state.getAvailableActions(agentIndex)

            for action in actions:
                successor = state.generateNextState(agentIndex, action)
                nextAgent = (agentIndex + 1) % state.getNumAgents()
                nextDepth = depth + 1 if nextAgent == 0 else depth

                value, best_action_for_value = expectimax(nextAgent, nextDepth, successor)

                if value > v:
                    v = value
                    best_action = action

            return v, best_action

        def expect_value(agentIndex, depth, state):
            v = 0
            actions = state.getAvailableActions(agentIndex)
            prob = 1.0 / len(actions) # uniform distribution

            for action in actions:
                successor = state.generateNextState(agentIndex, action)
                nextAgent = (agentIndex + 1) % state.getNumAgents()
                nextDepth = depth + 1 if nextAgent == 0 else depth

                value, best_action_for_expect = expectimax(nextAgent, nextDepth, successor)
                v += prob * value

            return v, None

        # agentIndex=0, depth=0
        expected_value, action = expectimax(0, 0, gameState)
        return action
        #util.raiseNotDefined()


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    Returns a score based on:
    - The distance to the nearest ghost, with a penalty for being close to a ghost (ghostPenalty)
    - The distance to the nearest food, with a reward for getting closer to food (foodReward)
    - The number of food pellets eaten so far (scoreReward)
    - The remaining food pellets on the board, which adds a penalty (foodPenalty) based on how much food is left
    """
    "*** YOUR CODE HERE ***"

    pacmanPos = currentGameState.getPacmanPosition()
    food = currentGameState.getFood()
    ghosts = currentGameState.getGhostStates()
    score = currentGameState.getScore()

    # calculates the distance to the closest ghost
    ghostDistances = [manhattanDistance(pacmanPos, ghost.getPosition()) for ghost in ghosts]
    closestGhostDist = min(ghostDistances) if ghostDistances else float('inf')

    # penalizes in the case that pacman is too close to a ghost (higher penalty for close ghosts)
    ghostPenalty = 5.0 / (closestGhostDist + 1)

    # calculates the distance to the nearest food
    foodList = food.asList()
    if foodList:
        foodDistances = [manhattanDistance(pacmanPos, foodPos) for foodPos in foodList]
        closestFoodDist = min(foodDistances)
        foodReward = 10.0 / (closestFoodDist + 1) # greater reward for approaching food
    else:
        foodReward = 0 # if no food is left, there is no further rewarding

    # calculates remaining food
    remainingFood = len(foodList)
    foodPenalty = remainingFood * 2 # penalty for more food left

    # uses the current score (number of food pellets eaten)
    scoreReward = score # the more food Pacman eats, the higher the reward (monotonous increase)

    # combines all factors into a better evaluation function
    evaluation = scoreReward + foodReward - ghostPenalty - foodPenalty

    return evaluation
    #util.raiseNotDefined()


# Abbreviation
better = betterEvaluationFunction
