## 📘 Bayes’ Theorem — Notes for Quant Interviews

Bayes’ Theorem allows us to reverse conditional probabilities when direct observation is difficult.

The formula is:

$$
P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}
$$

Where:
- $P(A)$ is the prior probability of $A$
- $P(B \mid A)$ is the likelihood of observing $B$ given $A$
- $P(B)$ is the total probability of observing $B$
- $P(A \mid B)$ is the posterior probability of $A$ after observing $B$

---

### 🔹 Law of Total Probability

Used to compute $P(B)$ when $B$ can occur under multiple mutually exclusive scenarios:

$$
P(B) = P(B \mid A) \cdot P(A) + P(B \mid \neg A) \cdot P(\neg A)
$$

---

### 🔹 Posterior Odds Form (Bayesian Updating)

Sometimes Bayes’ Theorem is written in odds form:

$$
\frac{P(A \mid B)}{P(\neg A \mid B)} = \frac{P(A)}{P(\neg A)} \cdot \frac{P(B \mid A)}{P(B \mid \neg A)}
$$

This shows how new evidence updates your belief via the likelihood ratio.

---

### 🔹 Continuous Version (Probability Density Functions)

In the continuous case, we use probability density functions instead of discrete probabilities:

$$
f_{X \mid Y}(x \mid y) = \frac{f_{Y \mid X}(y \mid x) \cdot f_X(x)}{f_Y(y)}
$$

---

### ✅ Summary Table

| Term          | Meaning                         |
| ------------- | ------------------------------- |
| $P(A)$        | Prior probability               |
| $P(B \mid A)$ | Likelihood                      |
| $P(B)$        | Marginal (evidence) probability |
| $P(A \mid B)$ | Posterior (updated) probability |

