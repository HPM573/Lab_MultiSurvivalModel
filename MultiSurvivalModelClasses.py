from SurvivalModelClasses import Cohort
import SimPy.StatisticalClasses as Stat


class MultiCohort:
    """ simulates multiple cohorts with different parameters """

    def __init__(self, ids, pop_sizes, mortality_probs):
        """
        :param ids: (list) of ids for cohorts to simulate
        :param pop_sizes: (list) of population sizes of cohorts to simulate
        :param mortality_probs: (list) of the mortality probabilities
        """
        self.ids = ids
        self.popSizes = pop_sizes
        self.mortalityProbs = mortality_probs
        self.multiCohortOutcomes = MultiCohortOutcomes()

    def simulate(self, n_time_steps):
        """ simulates all cohorts """



class MultiCohortOutcomes:
    def __init__(self):

        self.survivalTimes = []  # two dimensional list of patient survival times from all simulated cohort
        self.meanSurvivalTimes = []  # list of average patient survival time for all simulated cohort
        self.survivalCurves = []  # list of survival curves from all simulated cohorts

    def extract_outcomes(self, simulated_cohort):
        """ extracts outcomes of a simulated cohort
        :param simulated_cohort: a cohort after being simulated"""

