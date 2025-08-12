# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getInitialState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getNextStates(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (nextState,
        action, stepCost), where 'nextState' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getInitialState())
    print("Is the start a goal?", problem.isGoalState(problem.getInitialState()))
    print("Start's nextStates:", problem.getNextStates(problem.getInitialState()))
    """
    "*** YOUR CODE HERE ***"

    # στοίβα με πλειάδες
    frontier = util.Stack() # χρησιμοποιώ στοίβα για bfs

    # αποθηκεύω tuples της μορφής: (τρέχουσα κατάσταση, μονοπάτι ενεργειών)
    start_state = problem.getInitialState()
    frontier.push((start_state, []))

    visited = set() # σύνολο καταστάσεων που έχει ήδη δει ο dfs

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        if state in visited:
            continue

        visited.add(state)

        # αν η κατάσταση είναι στόχος, επιστροφή της ακολουθίας ενεργειών
        if problem.isGoalState(state):
            return actions

        # δημιουργία νέων καταστάσεων
        for successor, action, cost in problem.getNextStates(state):
            if successor not in visited:
                frontier.push((successor, actions + [action]))

    return [] # περίπτωση που δε βρεθεί λύση
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # ουρά με πλειάδες
    frontier = util.Queue() # χρησιμοποιώ ουρά για bfs

    # αποθηκεύω tuples της μορφής: (τρέχουσα κατάσταση, μονοπάτι ενεργειών)
    start_state = problem.getInitialState()
    frontier.push((start_state, []))

    visited = set() # σύνολο καταστάσεων που έχει ήδη δει ο bfs

    while not frontier.isEmpty():
        state, actions = frontier.pop()

        if state in visited:
            continue

        visited.add(state)

        # αν η κατάσταση είναι στόχος, επιστροφή της ακολουθίας ενεργειών
        if problem.isGoalState(state):
            return actions

        # δημιουργία νέων καταστάσεων
        for successor, action, cost in problem.getNextStates(state):
            if successor not in visited:
                frontier.push((successor, actions + [action]))

    return [] # περίπτωση που δε βρεθεί λύση
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # ουρά προτεραιότητας για την αποθήκευση καταστάσεων με κόστος
    frontier = util.PriorityQueue()

    # αρχική κατάσταση με μηδενικό κόστος
    start_state = problem.getInitialState()
    frontier.push((start_state, [], 0), 0) # (state, actions, cost), priority

    visited = set() # σύνολο καταστάσεων που έχει ήδη δει ο ucs

    while not frontier.isEmpty():
        state, actions, cost = frontier.pop()

        if state in visited:
            continue

        visited.add(state)

        # αν η κατάσταση είναι στόχος, επιστροφή της ακολουθίας ενεργειών
        if problem.isGoalState(state):
            return actions

        # δημιουργία νέων καταστάσεων
        for successor, action, step_cost in problem.getNextStates(state):
            if successor not in visited:
                new_cost = cost + step_cost
                frontier.push((successor, actions + [action], new_cost), new_cost)

    return [] # περίπτωση που δε βρεθεί λύση
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # ουρά προτεραιότητας για την αποθήκευση καταστάσεων με κόστος
    frontier = util.PriorityQueue()

    # αρχική κατάσταση με μηδενικό κόστος
    start_state = problem.getInitialState()
    frontier.push((start_state, [], 0), heuristic(start_state, problem))  # (state, actions, cost)

    visited = {} # σύνολο καταστάσεων που έχει ήδη δει ο A*

    while not frontier.isEmpty():
        state, actions, cost_till_now = frontier.pop()

        # αν έχει ξαναδεί το state με μικρότερο κόστος, το αγνοεί
        if state in visited and visited[state] <= cost_till_now:
            continue

        visited[state] = cost_till_now

        # αν η κατάσταση είναι στόχος, επιστροφή της ακολουθίας ενεργειών
        if problem.isGoalState(state):
            return actions

        # δημιουργία νέων καταστάσεων
        for successor, action, step_cost in problem.getNextStates(state):
            new_cost = cost_till_now + step_cost
            priority = new_cost + heuristic(successor, problem) #priority=g(n)+h(n)
            frontier.push((successor, actions + [action], new_cost), priority)

    return [] # περίπτωση που δε βρεθεί λύση
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

