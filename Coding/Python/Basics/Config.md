Config files that store variables are most of the time yaml,json or python files and can be used as such 

```
inside config.yaml

tickers:
  - NVDA
  - AMD
  - TSM
  - SMCI
  - SOXX
window_sizes:
  rsi: 20
  zscore: [5, 10, 21]

inside script.py
import yaml

with open("e:/QR_Proj/Phase_2/config.yaml", "r") as f:
    config = yaml.safe_load(f)

print(config["tickers"])
print(config["window_sizes"]["rsi"])
```

