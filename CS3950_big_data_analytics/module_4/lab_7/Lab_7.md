```python
import pandas as pd
```


```python
import numpy as np
```


```python
df = pd.read_excel("/Users/lotfey/Desktop/Baker/github/CS3950_big_data_analytics/module_4/lab_7/Lab 7 - Cancer.xls")
```


```python
df.head()
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
      <th>patient_id</th>
      <th>clump_thickness</th>
      <th>cell_size_uniformity</th>
      <th>cell_shape_uniformity</th>
      <th>marginal_adhesion</th>
      <th>single_ep_cell_size</th>
      <th>bare_nuclei</th>
      <th>bland_chromatin</th>
      <th>normal_nucleoli</th>
      <th>mitoses</th>
      <th>class</th>
      <th>doctor_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000025</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Doe</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002945</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>4</td>
      <td>5</td>
      <td>7</td>
      <td>10</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Smith</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1015425</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Lee</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1016277</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>8</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Smith</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1017023</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Wong</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.dtypes
```




    patient_id                 int64
    clump_thickness          float64
    cell_size_uniformity     float64
    cell_shape_uniformity      int64
    marginal_adhesion          int64
    single_ep_cell_size        int64
    bare_nuclei               object
    bland_chromatin          float64
    normal_nucleoli          float64
    mitoses                    int64
    class                     object
    doctor_name               object
    dtype: object




```python
df.describe()
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
      <th>patient_id</th>
      <th>clump_thickness</th>
      <th>cell_size_uniformity</th>
      <th>cell_shape_uniformity</th>
      <th>marginal_adhesion</th>
      <th>single_ep_cell_size</th>
      <th>bland_chromatin</th>
      <th>normal_nucleoli</th>
      <th>mitoses</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>6.990000e+02</td>
      <td>698.000000</td>
      <td>698.000000</td>
      <td>699.000000</td>
      <td>699.000000</td>
      <td>699.000000</td>
      <td>695.000000</td>
      <td>698.000000</td>
      <td>699.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.071704e+06</td>
      <td>4.416905</td>
      <td>3.137536</td>
      <td>3.207439</td>
      <td>2.793991</td>
      <td>3.216023</td>
      <td>3.447482</td>
      <td>2.868195</td>
      <td>1.589413</td>
    </tr>
    <tr>
      <th>std</th>
      <td>6.170957e+05</td>
      <td>2.817673</td>
      <td>3.052575</td>
      <td>2.971913</td>
      <td>2.843163</td>
      <td>2.214300</td>
      <td>2.441191</td>
      <td>3.055647</td>
      <td>1.715078</td>
    </tr>
    <tr>
      <th>min</th>
      <td>6.163400e+04</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>8.706885e+05</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.171710e+06</td>
      <td>4.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.238298e+06</td>
      <td>6.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>3.500000</td>
      <td>4.000000</td>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.345435e+07</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_grb = df.groupby(['class', 'doctor_name'])
```


```python
df_grb["clump_thickness"].mean()
```




    class      doctor_name
    benign     Dr. Doe        2.637795
               Dr. Lee        2.983471
               Dr. Smith      3.098039
               Dr. Wong       3.166667
    malignant  Dr. Doe        7.586207
               Dr. Lee        6.600000
               Dr. Smith      7.356164
               Dr. Wong       7.265306
    Name: clump_thickness, dtype: float64




```python
missing_summary = df.isnull().sum()
```


```python
missing_summary[missing_summary > 0]
```




    clump_thickness         1
    cell_size_uniformity    1
    bare_nuclei             2
    bland_chromatin         4
    normal_nucleoli         1
    dtype: int64




```python
df_clean_rows = df.dropna()
```


```python
df.nunique()
```




    patient_id               645
    clump_thickness           10
    cell_size_uniformity      10
    cell_shape_uniformity     10
    marginal_adhesion         10
    single_ep_cell_size       10
    bare_nuclei               11
    bland_chromatin           10
    normal_nucleoli           10
    mitoses                    9
    class                      2
    doctor_name                4
    dtype: int64




```python
# The patient_id column contains 645 unique entries.
# The features such as clump_thickness, cell_size_uniformity, and related attributes each have between 9 and 11 unique values
# The class column has only 2 unique values.
```


```python
duplicate_ids = df[df.duplicated(subset='patient_id', keep=False)]
```


```python
duplicate_counts = duplicate_ids['patient_id'].value_counts()
```


```python
duplicate_counts
```




    patient_id
    1182404    6
    1276091    5
    1198641    3
    1017023    2
    798429     2
    493452     2
    1114570    2
    1293439    2
    734111     2
    1299596    2
    1238777    2
    1299924    2
    1320077    2
    769612     2
    1061990    2
    1240603    2
    1321942    2
    695091     2
    1277792    2
    1339781    2
    1354840    2
    466906     2
    654546     2
    822829     2
    704097     2
    733639     2
    1168736    2
    1070935    2
    1100524    2
    1105524    2
    1115293    2
    1116116    2
    1116192    2
    1143978    2
    1158247    2
    1171710    2
    1033078    2
    1173347    2
    1174057    2
    1212422    2
    1218860    2
    320675     2
    385103     2
    411453     2
    560680     2
    897471     2
    Name: count, dtype: int64




```python
# Identify the most frequently duplicated patient_id
most_frequent_id = duplicate_counts.idxmax()
most_frequent_count = duplicate_counts.max()

```


```python
most_frequent_count
```




    6




```python
# Remove the patients that show up more than two times
id_counts = df['patient_id'].value_counts()
valid_ids = id_counts[id_counts <= 2].index
df_filtered = df[df['patient_id'].isin(valid_ids)]
df_filtered
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
      <th>patient_id</th>
      <th>clump_thickness</th>
      <th>cell_size_uniformity</th>
      <th>cell_shape_uniformity</th>
      <th>marginal_adhesion</th>
      <th>single_ep_cell_size</th>
      <th>bare_nuclei</th>
      <th>bland_chromatin</th>
      <th>normal_nucleoli</th>
      <th>mitoses</th>
      <th>class</th>
      <th>doctor_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000025</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Doe</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002945</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>4</td>
      <td>5</td>
      <td>7</td>
      <td>10</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Smith</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1015425</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Lee</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1016277</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>8</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Smith</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1017023</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Wong</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>694</th>
      <td>776715</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Lee</td>
    </tr>
    <tr>
      <th>695</th>
      <td>841769</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Smith</td>
    </tr>
    <tr>
      <th>696</th>
      <td>888820</td>
      <td>5.0</td>
      <td>10.0</td>
      <td>10</td>
      <td>3</td>
      <td>7</td>
      <td>3</td>
      <td>8.0</td>
      <td>10.0</td>
      <td>2</td>
      <td>malignant</td>
      <td>Dr. Lee</td>
    </tr>
    <tr>
      <th>697</th>
      <td>897471</td>
      <td>4.0</td>
      <td>8.0</td>
      <td>6</td>
      <td>4</td>
      <td>3</td>
      <td>4</td>
      <td>10.0</td>
      <td>6.0</td>
      <td>1</td>
      <td>malignant</td>
      <td>Dr. Lee</td>
    </tr>
    <tr>
      <th>698</th>
      <td>897471</td>
      <td>4.0</td>
      <td>8.0</td>
      <td>8</td>
      <td>5</td>
      <td>4</td>
      <td>5</td>
      <td>10.0</td>
      <td>4.0</td>
      <td>1</td>
      <td>malignant</td>
      <td>Dr. Wong</td>
    </tr>
  </tbody>
</table>
<p>685 rows × 12 columns</p>
</div>




```python
categorical_df = df[['patient_id', 'doctor_name']].copy()
categorical_df['doctor_count'] = 1
one_hot_df = categorical_df.pivot_table( index='patient_id', columns='doctor_name', values='doctor_count', fill_value=0 ).reset_index()
```


```python
merged_df = pd.merge(df, one_hot_df, on='patient_id', how='left')
```


```python
merged_df.head(15)
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
      <th>patient_id</th>
      <th>clump_thickness</th>
      <th>cell_size_uniformity</th>
      <th>cell_shape_uniformity</th>
      <th>marginal_adhesion</th>
      <th>single_ep_cell_size</th>
      <th>bare_nuclei</th>
      <th>bland_chromatin</th>
      <th>normal_nucleoli</th>
      <th>mitoses</th>
      <th>class</th>
      <th>doctor_name</th>
      <th>Dr. Doe</th>
      <th>Dr. Lee</th>
      <th>Dr. Smith</th>
      <th>Dr. Wong</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000025</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Doe</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002945</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>4</td>
      <td>5</td>
      <td>7</td>
      <td>10</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Smith</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1015425</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Lee</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1016277</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>8</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Smith</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1017023</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Wong</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1017122</td>
      <td>8.0</td>
      <td>10.0</td>
      <td>10</td>
      <td>8</td>
      <td>7</td>
      <td>10</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>1</td>
      <td>malignant</td>
      <td>Dr. Smith</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1018099</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>10</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Doe</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1018561</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Smith</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1033078</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>5</td>
      <td>benign</td>
      <td>Dr. Smith</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1033078</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Doe</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1035283</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Doe</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1036172</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Smith</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1041801</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>1</td>
      <td>malignant</td>
      <td>Dr. Smith</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1043999</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Wong</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1044572</td>
      <td>8.0</td>
      <td>7.0</td>
      <td>5</td>
      <td>1</td>
      <td>7</td>
      <td>9</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>4</td>
      <td>malignant</td>
      <td>Dr. Doe</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
doctors_one_hot_encoded = pd.pivot_table( categorical_df, index=categorical_df.index, columns=['doctor_name'], values=['doctor_count'] )
```


```python
doctors_one_hot_encoded = doctors_one_hot_encoded.fillna(0)
```


```python
doctors_one_hot_encoded.columns = doctors_one_hot_encoded.columns.get_level_values(1)
```


```python
doctors_one_hot_encoded.head(15)
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
      <th>doctor_name</th>
      <th>Dr. Doe</th>
      <th>Dr. Lee</th>
      <th>Dr. Smith</th>
      <th>Dr. Wong</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
try:
    doctors_one_hot_encoded.columns = doctors_one_hot_encoded.columns.droplevel()
except ValueError:
    # Column index is not a MultiIndex, so no action is needed
    pass

```


```python
doctors_one_hot_encoded.head(15)
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
      <th>doctor_name</th>
      <th>Dr. Doe</th>
      <th>Dr. Lee</th>
      <th>Dr. Smith</th>
      <th>Dr. Wong</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
combined_df = pd.merge( df, doctors_one_hot_encoded, left_index=True, right_index=True, how='left' )
```


```python
combined_df.head()
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
      <th>patient_id</th>
      <th>clump_thickness</th>
      <th>cell_size_uniformity</th>
      <th>cell_shape_uniformity</th>
      <th>marginal_adhesion</th>
      <th>single_ep_cell_size</th>
      <th>bare_nuclei</th>
      <th>bland_chromatin</th>
      <th>normal_nucleoli</th>
      <th>mitoses</th>
      <th>class</th>
      <th>doctor_name</th>
      <th>Dr. Doe</th>
      <th>Dr. Lee</th>
      <th>Dr. Smith</th>
      <th>Dr. Wong</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000025</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Doe</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002945</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>4</td>
      <td>5</td>
      <td>7</td>
      <td>10</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Smith</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1015425</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Lee</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1016277</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>8</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Smith</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1017023</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>Dr. Wong</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
combined_df = combined_df.drop(columns=['doctor_name'])

```


```python
combined_df.head(15)
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
      <th>patient_id</th>
      <th>clump_thickness</th>
      <th>cell_size_uniformity</th>
      <th>cell_shape_uniformity</th>
      <th>marginal_adhesion</th>
      <th>single_ep_cell_size</th>
      <th>bare_nuclei</th>
      <th>bland_chromatin</th>
      <th>normal_nucleoli</th>
      <th>mitoses</th>
      <th>class</th>
      <th>Dr. Doe</th>
      <th>Dr. Lee</th>
      <th>Dr. Smith</th>
      <th>Dr. Wong</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1000025</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1002945</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>4</td>
      <td>5</td>
      <td>7</td>
      <td>10</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1</td>
      <td>benign</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1015425</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1016277</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>8</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>1</td>
      <td>benign</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1017023</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1017122</td>
      <td>8.0</td>
      <td>10.0</td>
      <td>10</td>
      <td>8</td>
      <td>7</td>
      <td>10</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>1</td>
      <td>malignant</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1018099</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>10</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1018561</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1033078</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>5</td>
      <td>benign</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1033078</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1035283</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1036172</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1041801</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>1</td>
      <td>malignant</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1043999</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>benign</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1044572</td>
      <td>8.0</td>
      <td>7.0</td>
      <td>5</td>
      <td>1</td>
      <td>7</td>
      <td>9</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>4</td>
      <td>malignant</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
def celltypelabel(x):
    if (x['cell_size_uniformity'] > 5) & (x['cell_shape_uniformity'] > 5):
        return 'normal'
    else:
        return 'abnormal'
```


```python
combined_df['cell_type'] = combined_df.apply(celltypelabel, axis=1)

```


```python
combined_df[['cell_size_uniformity', 'cell_shape_uniformity', 'cell_type']].head(15)
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
      <th>cell_size_uniformity</th>
      <th>cell_shape_uniformity</th>
      <th>cell_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.0</td>
      <td>4</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8.0</td>
      <td>8</td>
      <td>normal</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>5</th>
      <td>10.0</td>
      <td>10</td>
      <td>normal</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1.0</td>
      <td>2</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>12</th>
      <td>3.0</td>
      <td>3</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>14</th>
      <td>7.0</td>
      <td>5</td>
      <td>abnormal</td>
    </tr>
  </tbody>
</table>
</div>




```python
combined_df['cell_type_label'] = combined_df.apply(lambda x: celltypelabel(x), axis=1)
```


```python
combined_df[['cell_size_uniformity', 'cell_shape_uniformity', 'cell_type_label']].head(15)
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
      <th>cell_size_uniformity</th>
      <th>cell_shape_uniformity</th>
      <th>cell_type_label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.0</td>
      <td>4</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8.0</td>
      <td>8</td>
      <td>normal</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>5</th>
      <td>10.0</td>
      <td>10</td>
      <td>normal</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1.0</td>
      <td>2</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>12</th>
      <td>3.0</td>
      <td>3</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.0</td>
      <td>1</td>
      <td>abnormal</td>
    </tr>
    <tr>
      <th>14</th>
      <td>7.0</td>
      <td>5</td>
      <td>abnormal</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
