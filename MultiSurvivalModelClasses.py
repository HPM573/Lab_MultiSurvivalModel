import deampy.statistics as stats

from SurvivalModelClasses import Cohort


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

    def simulate(self, n_time_steps, seeds):
        """ simulates all cohorts """

        # set the random seed
        # rng = RandomState(seed=seed)

        for i in range(len(self.ids)):

            # create a cohort
            cohort = Cohort(id=self.ids[i], pop_size=self.popSizes[i], mortality_prob=self.mortalityProbs[i])

            # simulate the cohort
            cohort.simulate(
                n_time_steps=n_time_steps,
                seed=seeds[i])

            # outcomes from simulating all cohorts
            self.multiCohortOutcomes.extract_outcomes(simulated_cohort=cohort)

        # calculate the summary statistics of from all cohorts
        self.multiCohortOutcomes.calculate_summary_stats()


class MultiCohortOutcomes:
    def __init__(self):

        self.survivalTimes = []  # two-dimensional list of patient survival times from all simulated cohort
        self.meanSurvivalTimes = []  # list of average patient survival time for all simulated cohort
        self.survivalCurves = []  # list of survival curves from all simulated cohorts
        self.statMeanSurvivalTime = None  # summary statistics of mean survival time

    def extract_outcomes(self, simulated_cohort):
        """ extracts outcomes of a simulated cohort
        :param simulated_cohort: a cohort after being simulated"""

        # store all patient survival times from this cohort
        self.survivalTimes.append(simulated_cohort.cohortOutcomes.survivalTimes)

        # append the survival curve of this cohort
        self.survivalCurves.append(simulated_cohort.cohortOutcomes.nLivingPatients)

    def calculate_summary_stats(self):
        """
        calculate the summary statistics
        """

        # calculate average patient survival time for all simulated cohorts
        for obs_set in self.survivalTimes:
            self.meanSurvivalTimes.append(sum(obs_set)/len(obs_set))

        # summary statistics of mean survival time
        self.statMeanSurvivalTime = stats.SummaryStat(name='Mean survival time',
                                                      data=self.meanSurvivalTimes)

    def get_cohort_CI_mean_survival(self, cohort_index, alpha):
        """
        :returns: the confidence interval of the mean survival time for a specified cohort
        :param cohort_index: integer over [0, 1, ...] corresponding to the 1st, 2nd, ... simulated cohort
        :param alpha: significance level
        """

        stat = stats.SummaryStat(name='Summary statistics',
                                 data=self.survivalTimes[cohort_index])

        return stat.get_t_CI(alpha=alpha)

    def get_cohort_PI_survival(self, cohort_index, alpha):
        """ :returns: the prediction interval of the survival time for a specified cohort
        :param cohort_index: integer over [0, 1, ...] corresponding to the 1st, 2ndm ... simulated cohort
        :param alpha: significance level
        """

        stat = stats.SummaryStat(name='Summary statistics',
                                 data=self.survivalTimes[cohort_index])

        return stat.get_PI(alpha=alpha)
