$$
Z_t = \frac{X_t - \mu_t}{\sigma_t}, \quad
\mu_t = \frac{1}{N} \sum_{i=t-N+1}^{t} X_i, \quad
\sigma_t = \sqrt{\frac{1}{N} \sum_{i=t-N+1}^{t} (X_i - \mu_t)^2}
$$Where:
- $X_t$ is the value at time $t$  
- $\mu_t$ is the rolling mean over a fixed window of length $N$ ending at $t$  
- $\sigma_t$ is the rolling standard deviation over the same window

