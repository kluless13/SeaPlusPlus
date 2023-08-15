# Statistical Tests in Python

Statistical tests are essential tools for making inferences based on data samples. Here, we'll explore some of the most commonly used tests, their syntax in Python using the `scipy.stats` module, and the reasons for using each test.

## 1. T-test (Independent Samples)

- **Syntax**:
  ```python
  from scipy.stats import ttest_ind
  t_stat, p_value = ttest_ind(sample1, sample2)
  ```

- **Why?**:
  Used to determine if there is a significant difference between the means of two independent groups. Assumes that the populations the samples come from are normally distributed.

## 2. Paired T-test

- **Syntax**:
  ```python
  from scipy.stats import ttest_rel
  t_stat, p_value = ttest_rel(sample1, sample2)
  ```

- **Why?**:
  Used when you have two related samples and you want to test if their means differ. Commonly used in before-and-after scenarios.

## 3. Chi-Squared Test

- **Syntax**:
  ```python
  from scipy.stats import chi2_contingency
  chi2, p_value, dof, expected = chi2_contingency(observed)
  ```

- **Why?**:
  Used to test the independence between two categorical variables. It compares the observed frequencies to the frequencies we would expect if the variables were independent.

## 4. One-way ANOVA

- **Syntax**:
  ```python
  from scipy.stats import f_oneway
  f_stat, p_value = f_oneway(group1, group2, group3)
  ```

- **Why?**:
  Used to compare the means of more than two independent groups. It checks if at least two groups are different from each other.

## 5. Pearson Correlation

- **Syntax**:
  ```python
  from scipy.stats import pearsonr
  corr_coeff, p_value = pearsonr(data1, data2)
  ```

- **Why?**:
  Measures the linear relationship between two datasets. Values range from -1 (perfect negative correlation) to 1 (perfect positive correlation).

## 6. Spearman Rank Correlation

- **Syntax**:
  ```python
  from scipy.stats import spearmanr
  corr_coeff, p_value = spearmanr(data1, data2)
  ```

- **Why?**:
  Measures the monotonic relationship between two datasets. Useful when the relationship between variables is not linear or when data doesn't meet the normality assumption.

## 7. Mann-Whitney U Test

- **Syntax**:
  ```python
  from scipy.stats import mannwhitneyu
  u_stat, p_value = mannwhitneyu(sample1, sample2)
  ```

- **Why?**:
  Non-parametric test used to compare two independent samples. Useful when data doesn't meet the assumptions of the t-test.

## 8. Kruskal-Wallis H-test

- **Syntax**:
  ```python
  from scipy.stats import kruskal
  h_stat, p_value = kruskal(group1, group2, group3)
  ```

- **Why?**:
  Non-parametric version of the one-way ANOVA. Used to compare more than two independent samples when data doesn't meet the assumptions of the ANOVA.

## 9. Shapiro-Wilk Test

- **Syntax**:
  ```python
  from scipy.stats import shapiro
  w_stat, p_value = shapiro(data)
  ```

- **Why?**:
  Tests if a sample is normally distributed. A significant p-value suggests that the data is not normally distributed.

## 10. Levene's Test

- **Syntax**:
  ```python
  from scipy.stats import levene
  w_stat, p_value = levene(sample1, sample2)
  ```

- **Why?**:
  Tests the equality of variances across different groups. Useful to check the assumption of equal variances before performing a t-test or ANOVA.

---

Of course! Here's a continuation of the statistical tests, diving deeper into more advanced tests and techniques. This is the "Stat Tests 2.0" markdown file:

---

# Advanced Statistical Tests in Python: Stat Tests 2.0

Building on our foundational statistical tests, this guide delves into more advanced techniques to help you make robust inferences from your data.

## 1. Two-way ANOVA

- **Syntax**:
  ```python
  import statsmodels.api as sm
  from statsmodels.formula.api import ols
  model = ols('response ~ C(factor1) + C(factor2) + C(factor1):C(factor2)', data=data).fit()
  anova_table = sm.stats.anova_lm(model, typ=2)
  ```

- **Why?**:
  Used to examine how two factors impact a continuous outcome. It assesses the individual and interactive effects of the factors.

## 2. Wilcoxon Signed-Rank Test

- **Syntax**:
  ```python
  from scipy.stats import wilcoxon
  w_stat, p_value = wilcoxon(data1, data2)
  ```

- **Why?**:
  Non-parametric test for comparing two related samples. Useful when the paired data does not meet the assumptions of the paired t-test.

## 3. Friedman Test

- **Syntax**:
  ```python
  from scipy.stats import friedmanchisquare
  chi2_stat, p_value = friedmanchisquare(group1, group2, group3)
  ```

- **Why?**:
  Non-parametric alternative to the repeated measures ANOVA. It tests for differences between groups when the dependent variable is ordinal.

## 4. Durbin-Watson Test

- **Syntax**:
  ```python
  from statsmodels.stats.stattools import durbin_watson
  dw_stat = durbin_watson(model.resid)
  ```

- **Why?**:
  Tests for the presence of autocorrelation in the residuals from a regression analysis.

## 5. Log-rank Test

- **Syntax**:
  ```python
  from lifelines.statistics import logrank_test
  results = logrank_test(time1, time2, event_observed_A=event1, event_observed_B=event2)
  ```

- **Why?**:
  Used to test the hypothesis that there is no difference between the survival curves of two groups.

## 6. Granger Causality Test

- **Syntax**:
  ```python
  from statsmodels.tsa.stattools import grangercausalitytests
  grangercausalitytests(data, maxlag=lag)
  ```

- **Why?**:
  Determines whether one time series can predict another time series.

## 7. Jarque-Bera Test

- **Syntax**:
  ```python
  from scipy.stats import jarque_bera
  jb_stat, p_value = jarque_bera(data)
  ```

- **Why?**:
  Tests if the data has the skewness and kurtosis of a normal distribution.

## 8. Breusch-Pagan Test

- **Syntax**:
  ```python
  from statsmodels.stats.diagnostic import het_breuschpagan
  bp_stat, p_value, fvalue, f_pvalue = het_breuschpagan(resid, exog_het)
  ```

- **Why?**:
  Tests for heteroscedasticity in a linear regression model.

## 9. Anderson-Darling Test

- **Syntax**:
  ```python
  from scipy.stats import anderson
  result = anderson(data)
  ```

- **Why?**:
  Tests if data comes from a particular distribution.

## 10. Ljung-Box Test

- **Syntax**:
  ```python
  from statsmodels.stats.diagnostic import acorr_ljungbox
  lb_stat, p_value = acorr_ljungbox(resids, lags=lags)
  ```

- **Why?**:
  Tests for autocorrelations in time series data.

---