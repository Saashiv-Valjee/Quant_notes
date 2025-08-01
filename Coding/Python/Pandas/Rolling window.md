a rolling window for taking final - initial returns can be created using 
```
pct_change(periods=9) # 10 day rolling window
```

useful for when you don't want to aggregate the window like what [[Rolling Object]] does 

![[Pasted image 20250731232915.png]]

$$
\frac{series_N}{series_{N-periods}} 
$$
