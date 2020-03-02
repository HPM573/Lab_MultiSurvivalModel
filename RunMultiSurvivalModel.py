import MultiSurvivalModelClasses as Cls
import SimPy.Plots.SamplePaths as Path
import SimPy.Plots.Histogram as Hist

MORTALITY_PROB = 0.1    # annual probability of death
TIME_STEPS = 100        # years
N_COHORTS = 500         # number of cohorts
COHORT_POP_SIZE = 1000   # size of each cohort

# create multiple cohorts

# simulate all cohorts

# plot the sample paths
Path.plot_sample_paths(
    sample_paths=multiCohort.multiCohortOutcomes.survivalCurves,
    title='Survival Curves',
    x_label='Time-Step (Year)',
    y_label='Number Survived',
    transparency=0.5)

# plot the histogram of average survival time
Hist.plot_histogram(
    data=multiCohort.multiCohortOutcomes.meanSurvivalTimes,
    title='Histogram of Mean Survival Time',
    x_label='Mean Survival Time (Year)',
    y_label='Count')

# print projected mean survival time (years)
print('Projected mean survival time (years)',

      )

# print projection interval
print('95% projection (prediction, percentile, or uncertainty) interval of average survival time (years)',

      )
