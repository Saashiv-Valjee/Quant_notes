## 📘 Uniform Distribution Notes — Continuous Case

Let $X \sim \text{Uniform}(L, U)$ with $L < U$.

---

### 🔹 Probability Density Function (PDF)

$$
f_X(x) = 
\begin{cases}
\frac{1}{U - L} & \text{if } x \in [L, U] \\
0 & \text{otherwise}
\end{cases}
$$

---

### 🔹 Expectation (Mean)

$$
\mathbb{E}[X] = \frac{L + U}{2}
$$

---

### 🔹 Variance

$$
\text{Var}(X) = \frac{(U - L)^2}{12}
$$

---

### 🔹 Moment Generating Function (MGF)

$$
M_X(t) = 
\begin{cases}
\frac{e^{tU} - e^{tL}}{t(U - L)} & t \ne 0 \\
1 & t = 0
\end{cases}
$$

---

### 🔹 Cumulative Distribution Function (CDF)

$$
F_X(x) = 
\begin{cases}
0 & x < L \\
\frac{x - L}{U - L} & L \leq x \leq U \\
1 & x > U
\end{cases}
$$

---

## 🧠 Common Interview Questions & Examples

Q1: What is the mean and variance of $X \sim \text{Uniform}(2, 10)$?

**Solution**:

$$
\mathbb{E}[X] = \frac{2 + 10}{2} = 6
$$

$$
\text{Var}(X) = \frac{(10 - 2)^2}{12} = \frac{64}{12} = \frac{16}{3}
$$

---

Q2: Approximate the distribution of $S = X_1 + \dots + X_{12}$, where each $X_i \sim \text{Uniform}(0, 1)$.

**Solution**:

$$
\mathbb{E}[S] = 12 \cdot \frac{1}{2} = 6
$$

$$
\text{Var}(S) = 12 \cdot \frac{1}{12} = 1
$$

By the Central Limit Theorem:

$$
S \approx \mathcal{N}(6, 1)
$$

---

Q3: What is the probability that $X \sim \text{Uniform}(3, 9)$ lies between 4 and 7?

**Solution**:

$$
P(4 \leq X \leq 7) = \frac{7 - 4}{9 - 3} = \frac{3}{6} = 0.5
$$

---

Q4: What is the PDF and CDF of $X \sim \text{Uniform}(-1, 2)$?

**PDF**:

$$
f_X(x) = 
\begin{cases}
\frac{1}{3} & -1 \leq x \leq 2 \\
0 & \text{otherwise}
\end{cases}
$$

**CDF**:

$$
F_X(x) = 
\begin{cases}
0 & x < -1 \\
\frac{x + 1}{3} & -1 \leq x \leq 2 \\
1 & x > 2
\end{cases}
$$

---

## ✅ Summary Table

| Property  | Formula |
|-----------|---------|
| Mean      | $\frac{L + U}{2}$ |
| Variance  | $\frac{(U - L)^2}{12}$ |
| PDF       | $\frac{1}{U - L}$ on $[L, U]$ |
| CDF       | $\frac{x - L}{U - L}$ on $[L, U]$ |
| MGF       | $\frac{e^{tU} - e^{tL}}{t(U-L)}$ |

