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
        self.cohorts = []   # list of cohorts
        self.multiCohortOutcomes = MultiCohortOutcomes()

        # create cohorts
        for i in range(len(self.ids)):
            # create a cohort
            self.cohorts.append(
                Cohort(
                    id=self.ids[i],
                    pop_size=pop_sizes[i],
                    mortality_prob=mortality_probs[i]
                )
            )

    def simulate(self, n_time_steps):
        """ simulates all cohorts """

        # simulate all cohorts
        for cohort in self.cohorts:
            # simulate the cohort
            cohort.simulate(n_time_steps)

        # outcomes from simulating all cohorts
        self.multiCohortOutcomes.extract_outcomes(self.cohorts)


class MultiCohortOutcomes:
    def __init__(self):

        self.survivalTimes = []  # two dimensional list of patient survival times from all simulated cohort
        self.meanSurvivalTimes = []  # list of average patient survival time for all simulated cohort
        self.survivalCurves = []  # list of survival curves from all simulated cohorts
        self.sumStat_meanSurvivalTime = None  # summary statistics of mean survival time

    def extract_outcomes(self, simulated_cohorts):
        """ extracts outcomes of multiple simulated cohorts
        :param simulated_cohorts: multiple cohorts after being simulated"""

        # go over all simulation cohorts
        for cohort in simulated_cohorts:

            # store all patient survival times from this cohort
            self.survivalTimes.append(cohort.cohortOutcomes.survivalTimes)

            # append the survival curve of this cohort
            self.survivalCurves.append(cohort.cohortOutcomes.nLivingPatients)

        # calculate average patient survival time for all simulated cohorts
        for obs_set in self.survivalTimes:
            self.meanSurvivalTimes.append(sum(obs_set)/len(obs_set))

        # summary statistics of mean survival time
        self.sumStat_meanSurvivalTime = Stat.SummaryStat('Mean survival time', self.meanSurvivalTimes)

    def get_cohort_CI_mean_survival(self, cohort_index, alpha):
        """
        :returns: the confidence interval of the mean survival time for a specified cohort
        :param cohort_index: integer over [0, 1, ...] corresponding to the 1st, 2nd, ... simulated cohort
        :param alpha: significance level
        """

        stat = Stat.SummaryStat(name='Summary statistics',
                                data=self.survivalTimes[cohort_index])

        return stat.get_t_CI(alpha)

    def get_cohort_PI_survival(self, cohort_index, alpha):
        """ :returns: the prediction interval of the survival time for a specified cohort
        :param cohort_index: integer over [0, 1, ...] corresponding to the 1st, 2ndm ... simulated cohort
        :param alpha: significance level
        """

        stat = Stat.SummaryStat(name='Summary statistics',
                                data=self.survivalTimes[cohort_index])

        return stat.get_PI(alpha)
