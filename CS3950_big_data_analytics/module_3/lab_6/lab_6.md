```python
import pandas as pd
```


```python
df = pd.read_excel('~/Desktop/Baker/github/CS3950_big_data_analytics/module_3/lab_6/Lab 6 - Chipotle.xls', engine='xlrd')
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
      <th>Unnamed: 0</th>
      <th>order_id</th>
      <th>quantity</th>
      <th>item_name</th>
      <th>choice_description</th>
      <th>item_price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>Chips and Fresh Tomato Salsa</td>
      <td>NaN</td>
      <td>2.39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Izze</td>
      <td>[Clementine]</td>
      <td>3.39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Nantucket Nectar</td>
      <td>[Apple]</td>
      <td>3.39</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>Chips and Tomatillo-Green Chili Salsa</td>
      <td>NaN</td>
      <td>2.39</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>Chicken Bowl</td>
      <td>[Tomatillo-Red Chili Salsa (Hot), [Black Beans...</td>
      <td>16.98</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['item_price'] = df['item_price'].replace(r'[\$,]', '', regex=True).astype(float)
```


```python
chicken_items = df[df['item_name'].str.contains('chicken', case=False, na=False)]
```


```python
avg_chicken_price = chicken_items['item_price'].mean()
```


```python
print(f"Average price of an item with chicken: ${avg_chicken_price:.2f}")
```

    Average price of an item with chicken: $10.13



```python
steak_items = df[df['item_name'].str.contains('steak', case=False, na=False)]
```


```python
avg_steak_price = steak_items['item_price'].mean()
```


```python
print(f"Average price of an item with steak: ${avg_steak_price:.2f}")
```

    Average price of an item with steak: $10.52



```python
chicken_revenue = chicken_items['item_price'].sum()
```


```python
steak_revenue = steak_items['item_price'].sum()
```


```python
print(f"Total revenue from chicken: ${chicken_revenue:.2f}")
```

    Total revenue from chicken: $15808.61



```python
print(f"Total revenue from steak: ${steak_revenue:.2f}")
```

    Total revenue from steak: $7384.26



```python
if chicken_revenue > steak_revenue:
    print("Chicken produced more revenue.")
elif steak_revenue > chicken_revenue:
    print("Steak produced more revenue.")
else:
    print("Chicken and steak produced the same revenue.")
```

    Chicken produced more revenue.



```python
total_missing = df.isnull().sum().sum()
```


```python
print(total_missing)
```

    1246



```python
missing_per_column = df.isnull().sum()
```


```python
print(f"Total missing values in dataset: {total_missing}\n")
```

    Total missing values in dataset: 1246
    



```python
print(f'Missing values by column:\n{missing_per_column}')
```

    Missing values by column:
    Unnamed: 0               0
    order_id                 0
    quantity                 0
    item_name                0
    choice_description    1246
    item_price               0
    dtype: int64



```python

```
