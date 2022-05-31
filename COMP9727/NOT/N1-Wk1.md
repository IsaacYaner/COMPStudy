# Wk1

## Userbased collaborate rating

### Similarity 

+ Jaccard 
  + $\frac{U_i \bigcap U_j}{U_i \bigcup U_j}$
+ Cosine 
  + $\frac{\Sigma U_iU_j}{\sqrt{\Sigma U^2}\sqrt{\Sigma U^2}}$
  + Works well for sparse dataset
+ Pearson correlation
  + $\frac{\Sigma(r-\overline r)(r-\overline{r})}{\sqrt{\Sigma(r-\overline r)^2}\sqrt{\Sigma(r-\overline r)^2}}$

### Predict

+ mean + weighted average of (similar(i,j))*(markj-meanj)

### Pick neighbours

+ Positive only
+ 50-200 ok

### Improvement

+ recount Valuable

## Item based

+ Flip
+ More static

## Cold start
