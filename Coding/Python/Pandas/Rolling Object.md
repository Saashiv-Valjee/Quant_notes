Creates a rolling window using previous N entries, with the ability to not compute unless M entries are accessible within the window 

```
    rolling_mean = prices.rolling(window, min_periods=window).mean()
    rolling_std  = prices.rolling(window, min_periods=window).std()
```

input must be a dataframe, with an index and (probably) just 1 column of floats

very useful for computing the [[Rolling Z-Score]]

```
.rolling()
```

itself creates an object, which is required to be used alongside some combination function like mean or std to compute something. Alone it doesn't do much.