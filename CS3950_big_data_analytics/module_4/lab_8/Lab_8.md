```python
import pandas as pd
```


```python
import numpy as np
```


```python
df = pd.read_excel("/Users/lotfey/Desktop/Baker/github/CS3950_big_data_analytics/module_4/lab_8/Lab 8 - Treatment.xls")
```


```python
grp_treatment = df.groupby("Treatment")
```


```python
group_summary = df.groupby("Group")["RelativeFitness"].describe()
```


```python
group_summary
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>BAC</th>
      <td>4.0</td>
      <td>1.218189</td>
      <td>0.479989</td>
      <td>0.795107</td>
      <td>0.806570</td>
      <td>1.212707</td>
      <td>1.624325</td>
      <td>1.652234</td>
    </tr>
    <tr>
      <th>BKB</th>
      <td>6.0</td>
      <td>1.133384</td>
      <td>0.233928</td>
      <td>0.869963</td>
      <td>0.987292</td>
      <td>1.076454</td>
      <td>1.253450</td>
      <td>1.507415</td>
    </tr>
    <tr>
      <th>DOS</th>
      <td>6.0</td>
      <td>1.266371</td>
      <td>0.351438</td>
      <td>0.939563</td>
      <td>0.947387</td>
      <td>1.266191</td>
      <td>1.584521</td>
      <td>1.594531</td>
    </tr>
    <tr>
      <th>ECO</th>
      <td>6.0</td>
      <td>1.266115</td>
      <td>0.333269</td>
      <td>0.939479</td>
      <td>0.981781</td>
      <td>1.226464</td>
      <td>1.510207</td>
      <td>1.699276</td>
    </tr>
    <tr>
      <th>ETH</th>
      <td>6.0</td>
      <td>1.208686</td>
      <td>0.310907</td>
      <td>0.914288</td>
      <td>0.937661</td>
      <td>1.161320</td>
      <td>1.444778</td>
      <td>1.612816</td>
    </tr>
    <tr>
      <th>FIT</th>
      <td>6.0</td>
      <td>0.979185</td>
      <td>0.043881</td>
      <td>0.926698</td>
      <td>0.945467</td>
      <td>0.977769</td>
      <td>1.011094</td>
      <td>1.035973</td>
    </tr>
    <tr>
      <th>H2W</th>
      <td>6.0</td>
      <td>1.213932</td>
      <td>0.342246</td>
      <td>0.853906</td>
      <td>0.921153</td>
      <td>1.225099</td>
      <td>1.521326</td>
      <td>1.539582</td>
    </tr>
    <tr>
      <th>HHE</th>
      <td>6.0</td>
      <td>1.182194</td>
      <td>0.271297</td>
      <td>0.922486</td>
      <td>0.946297</td>
      <td>1.140874</td>
      <td>1.420342</td>
      <td>1.493994</td>
    </tr>
    <tr>
      <th>JDK</th>
      <td>6.0</td>
      <td>1.218714</td>
      <td>0.360766</td>
      <td>0.849204</td>
      <td>0.908402</td>
      <td>1.213953</td>
      <td>1.537931</td>
      <td>1.582701</td>
    </tr>
    <tr>
      <th>PPP</th>
      <td>6.0</td>
      <td>1.259126</td>
      <td>0.317535</td>
      <td>0.948767</td>
      <td>0.976299</td>
      <td>1.249735</td>
      <td>1.542419</td>
      <td>1.581386</td>
    </tr>
    <tr>
      <th>SWI</th>
      <td>6.0</td>
      <td>1.185222</td>
      <td>0.296395</td>
      <td>0.909023</td>
      <td>0.920986</td>
      <td>1.145480</td>
      <td>1.448495</td>
      <td>1.515692</td>
    </tr>
  </tbody>
</table>
</div>




```python
!echo "By applying this code, we can observe the count, mean, standard deviation, and quartiles of Relative Fitness values for each group. The analysis shows variability among groups in both average performance and consistency. For instance, groups like ECO and DOS had higher maximum values and means, while BAC showed the greatest dispersion in fitness values, indicated by a higher standard deviation. This suggests that experimental outcomes differed meaningfully between groups, potentially due to differing responses to the treatment environments."
```

    By applying this code, we can observe the count, mean, standard deviation, and quartiles of Relative Fitness values for each group. The analysis shows variability among groups in both average performance and consistency. For instance, groups like ECO and DOS had higher maximum values and means, while BAC showed the greatest dispersion in fitness values, indicated by a higher standard deviation. This suggests that experimental outcomes differed meaningfully between groups, potentially due to differing responses to the treatment environments.



```python
grouped_stats = df.groupby(["Treatment", "Group"])["RelativeFitness"].describe()
```


```python
grouped_stats
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>Treatment</th>
      <th>Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="11" valign="top">Dish</th>
      <th>BAC</th>
      <td>2.0</td>
      <td>1.633628</td>
      <td>0.026313</td>
      <td>1.615022</td>
      <td>1.624325</td>
      <td>1.633628</td>
      <td>1.642931</td>
      <td>1.652234</td>
    </tr>
    <tr>
      <th>BKB</th>
      <td>3.0</td>
      <td>1.315682</td>
      <td>0.179156</td>
      <td>1.152544</td>
      <td>1.219815</td>
      <td>1.287085</td>
      <td>1.397250</td>
      <td>1.507415</td>
    </tr>
    <tr>
      <th>DOS</th>
      <td>3.0</td>
      <td>1.587148</td>
      <td>0.006740</td>
      <td>1.581325</td>
      <td>1.583456</td>
      <td>1.585587</td>
      <td>1.590059</td>
      <td>1.594531</td>
    </tr>
    <tr>
      <th>ECO</th>
      <td>3.0</td>
      <td>1.561197</td>
      <td>0.124910</td>
      <td>1.456057</td>
      <td>1.492157</td>
      <td>1.528258</td>
      <td>1.613767</td>
      <td>1.699276</td>
    </tr>
    <tr>
      <th>ETH</th>
      <td>3.0</td>
      <td>1.482941</td>
      <td>0.124571</td>
      <td>1.364456</td>
      <td>1.418004</td>
      <td>1.471552</td>
      <td>1.542184</td>
      <td>1.612816</td>
    </tr>
    <tr>
      <th>FIT</th>
      <td>3.0</td>
      <td>1.001960</td>
      <td>0.041853</td>
      <td>0.955221</td>
      <td>0.984953</td>
      <td>1.014686</td>
      <td>1.025329</td>
      <td>1.035973</td>
    </tr>
    <tr>
      <th>H2W</th>
      <td>3.0</td>
      <td>1.525228</td>
      <td>0.014052</td>
      <td>1.511499</td>
      <td>1.518050</td>
      <td>1.524601</td>
      <td>1.532092</td>
      <td>1.539582</td>
    </tr>
    <tr>
      <th>HHE</th>
      <td>3.0</td>
      <td>1.424773</td>
      <td>0.085070</td>
      <td>1.329803</td>
      <td>1.390162</td>
      <td>1.450522</td>
      <td>1.472258</td>
      <td>1.493994</td>
    </tr>
    <tr>
      <th>JDK</th>
      <td>3.0</td>
      <td>1.546707</td>
      <td>0.036218</td>
      <td>1.510268</td>
      <td>1.528710</td>
      <td>1.547152</td>
      <td>1.564926</td>
      <td>1.582701</td>
    </tr>
    <tr>
      <th>PPP</th>
      <td>3.0</td>
      <td>1.547974</td>
      <td>0.036531</td>
      <td>1.508969</td>
      <td>1.531269</td>
      <td>1.553568</td>
      <td>1.567477</td>
      <td>1.581386</td>
    </tr>
    <tr>
      <th>SWI</th>
      <td>3.0</td>
      <td>1.451796</td>
      <td>0.079652</td>
      <td>1.362556</td>
      <td>1.419848</td>
      <td>1.477141</td>
      <td>1.496417</td>
      <td>1.515692</td>
    </tr>
    <tr>
      <th rowspan="11" valign="top">Tube</th>
      <th>BAC</th>
      <td>2.0</td>
      <td>0.802749</td>
      <td>0.010808</td>
      <td>0.795107</td>
      <td>0.798928</td>
      <td>0.802749</td>
      <td>0.806570</td>
      <td>0.810392</td>
    </tr>
    <tr>
      <th>BKB</th>
      <td>3.0</td>
      <td>0.951087</td>
      <td>0.070794</td>
      <td>0.869963</td>
      <td>0.926449</td>
      <td>0.982935</td>
      <td>0.991649</td>
      <td>1.000363</td>
    </tr>
    <tr>
      <th>DOS</th>
      <td>3.0</td>
      <td>0.945595</td>
      <td>0.005768</td>
      <td>0.939563</td>
      <td>0.942864</td>
      <td>0.946164</td>
      <td>0.948610</td>
      <td>0.951057</td>
    </tr>
    <tr>
      <th>ECO</th>
      <td>3.0</td>
      <td>0.971033</td>
      <td>0.029120</td>
      <td>0.939479</td>
      <td>0.958115</td>
      <td>0.976750</td>
      <td>0.986811</td>
      <td>0.996871</td>
    </tr>
    <tr>
      <th>ETH</th>
      <td>3.0</td>
      <td>0.934431</td>
      <td>0.022169</td>
      <td>0.914288</td>
      <td>0.922555</td>
      <td>0.930821</td>
      <td>0.944502</td>
      <td>0.958183</td>
    </tr>
    <tr>
      <th>FIT</th>
      <td>3.0</td>
      <td>0.956410</td>
      <td>0.038808</td>
      <td>0.926698</td>
      <td>0.934457</td>
      <td>0.942216</td>
      <td>0.971267</td>
      <td>1.000318</td>
    </tr>
    <tr>
      <th>H2W</th>
      <td>3.0</td>
      <td>0.902636</td>
      <td>0.043792</td>
      <td>0.853906</td>
      <td>0.884605</td>
      <td>0.915304</td>
      <td>0.927001</td>
      <td>0.938698</td>
    </tr>
    <tr>
      <th>HHE</th>
      <td>3.0</td>
      <td>0.939615</td>
      <td>0.015305</td>
      <td>0.922486</td>
      <td>0.933450</td>
      <td>0.944414</td>
      <td>0.948180</td>
      <td>0.951946</td>
    </tr>
    <tr>
      <th>JDK</th>
      <td>3.0</td>
      <td>0.890721</td>
      <td>0.036479</td>
      <td>0.849204</td>
      <td>0.877263</td>
      <td>0.905323</td>
      <td>0.911480</td>
      <td>0.917637</td>
    </tr>
    <tr>
      <th>PPP</th>
      <td>3.0</td>
      <td>0.970277</td>
      <td>0.020897</td>
      <td>0.948767</td>
      <td>0.960166</td>
      <td>0.971565</td>
      <td>0.981033</td>
      <td>0.990500</td>
    </tr>
    <tr>
      <th>SWI</th>
      <td>3.0</td>
      <td>0.918647</td>
      <td>0.009692</td>
      <td>0.909023</td>
      <td>0.913768</td>
      <td>0.918514</td>
      <td>0.923459</td>
      <td>0.928405</td>
    </tr>
  </tbody>
</table>
</div>




```python
!echo "The two-level grouping by Treatment and Group revealed notable differences in Relative Fitness outcomes across conditions. For example, most groups displayed higher mean fitness values under the Dish treatment compared to the Tube treatment."
```

    The two-level grouping by Treatment and Group revealed notable differences in Relative Fitness outcomes across conditions. For example, most groups displayed higher mean fitness values under the Dish treatment compared to the Tube treatment.



```python
aggregated_data = df.groupby(["Treatment", "Group"])["RelativeFitness"].agg( ["mean", "max", "median", "sum", "std"] )
```


```python
aggregated_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>mean</th>
      <th>max</th>
      <th>median</th>
      <th>sum</th>
      <th>std</th>
    </tr>
    <tr>
      <th>Treatment</th>
      <th>Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="11" valign="top">Dish</th>
      <th>BAC</th>
      <td>1.633628</td>
      <td>1.652234</td>
      <td>1.633628</td>
      <td>3.267256</td>
      <td>0.026313</td>
    </tr>
    <tr>
      <th>BKB</th>
      <td>1.315682</td>
      <td>1.507415</td>
      <td>1.287085</td>
      <td>3.947045</td>
      <td>0.179156</td>
    </tr>
    <tr>
      <th>DOS</th>
      <td>1.587148</td>
      <td>1.594531</td>
      <td>1.585587</td>
      <td>4.761443</td>
      <td>0.006740</td>
    </tr>
    <tr>
      <th>ECO</th>
      <td>1.561197</td>
      <td>1.699276</td>
      <td>1.528258</td>
      <td>4.683590</td>
      <td>0.124910</td>
    </tr>
    <tr>
      <th>ETH</th>
      <td>1.482941</td>
      <td>1.612816</td>
      <td>1.471552</td>
      <td>4.448824</td>
      <td>0.124571</td>
    </tr>
    <tr>
      <th>FIT</th>
      <td>1.001960</td>
      <td>1.035973</td>
      <td>1.014686</td>
      <td>3.005880</td>
      <td>0.041853</td>
    </tr>
    <tr>
      <th>H2W</th>
      <td>1.525228</td>
      <td>1.539582</td>
      <td>1.524601</td>
      <td>4.575683</td>
      <td>0.014052</td>
    </tr>
    <tr>
      <th>HHE</th>
      <td>1.424773</td>
      <td>1.493994</td>
      <td>1.450522</td>
      <td>4.274319</td>
      <td>0.085070</td>
    </tr>
    <tr>
      <th>JDK</th>
      <td>1.546707</td>
      <td>1.582701</td>
      <td>1.547152</td>
      <td>4.640121</td>
      <td>0.036218</td>
    </tr>
    <tr>
      <th>PPP</th>
      <td>1.547974</td>
      <td>1.581386</td>
      <td>1.553568</td>
      <td>4.643923</td>
      <td>0.036531</td>
    </tr>
    <tr>
      <th>SWI</th>
      <td>1.451796</td>
      <td>1.515692</td>
      <td>1.477141</td>
      <td>4.355389</td>
      <td>0.079652</td>
    </tr>
    <tr>
      <th rowspan="11" valign="top">Tube</th>
      <th>BAC</th>
      <td>0.802749</td>
      <td>0.810392</td>
      <td>0.802749</td>
      <td>1.605498</td>
      <td>0.010808</td>
    </tr>
    <tr>
      <th>BKB</th>
      <td>0.951087</td>
      <td>1.000363</td>
      <td>0.982935</td>
      <td>2.853261</td>
      <td>0.070794</td>
    </tr>
    <tr>
      <th>DOS</th>
      <td>0.945595</td>
      <td>0.951057</td>
      <td>0.946164</td>
      <td>2.836784</td>
      <td>0.005768</td>
    </tr>
    <tr>
      <th>ECO</th>
      <td>0.971033</td>
      <td>0.996871</td>
      <td>0.976750</td>
      <td>2.913100</td>
      <td>0.029120</td>
    </tr>
    <tr>
      <th>ETH</th>
      <td>0.934431</td>
      <td>0.958183</td>
      <td>0.930821</td>
      <td>2.803292</td>
      <td>0.022169</td>
    </tr>
    <tr>
      <th>FIT</th>
      <td>0.956410</td>
      <td>1.000318</td>
      <td>0.942216</td>
      <td>2.869231</td>
      <td>0.038808</td>
    </tr>
    <tr>
      <th>H2W</th>
      <td>0.902636</td>
      <td>0.938698</td>
      <td>0.915304</td>
      <td>2.707909</td>
      <td>0.043792</td>
    </tr>
    <tr>
      <th>HHE</th>
      <td>0.939615</td>
      <td>0.951946</td>
      <td>0.944414</td>
      <td>2.818846</td>
      <td>0.015305</td>
    </tr>
    <tr>
      <th>JDK</th>
      <td>0.890721</td>
      <td>0.917637</td>
      <td>0.905323</td>
      <td>2.672164</td>
      <td>0.036479</td>
    </tr>
    <tr>
      <th>PPP</th>
      <td>0.970277</td>
      <td>0.990500</td>
      <td>0.971565</td>
      <td>2.910832</td>
      <td>0.020897</td>
    </tr>
    <tr>
      <th>SWI</th>
      <td>0.918647</td>
      <td>0.928405</td>
      <td>0.918514</td>
      <td>2.755942</td>
      <td>0.009692</td>
    </tr>
  </tbody>
</table>
</div>




```python
!echo "Share additional findings from the dataset"
```

    Share additional findings from the dataset



```python
!echo "Identify the group with the highest maximum fitness"
```

    Identify the group with the highest maximum fitness



```python
max_relative_fitness = df.groupby("Group")["RelativeFitness"].max()
```


```python
max_relative_fitness.idxmax()
```




    'ECO'




```python
!echo "Count of observations per Treatment and Group"
```

    Count of observations per Treatment and Group



```python
counts = df.groupby(["Treatment", "Group"]).size()
```


```python
counts
```




    Treatment  Group
    Dish       BAC      2
               BKB      3
               DOS      3
               ECO      3
               ETH      3
               FIT      3
               H2W      3
               HHE      3
               JDK      3
               PPP      3
               SWI      3
    Tube       BAC      2
               BKB      3
               DOS      3
               ECO      3
               ETH      3
               FIT      3
               H2W      3
               HHE      3
               JDK      3
               PPP      3
               SWI      3
    dtype: int64




```python

```
