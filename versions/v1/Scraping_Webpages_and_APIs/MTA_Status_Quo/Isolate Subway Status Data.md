# Isolate Subway Status Data

At this point you should have a dict that represents subways statuses for **all** the MTA's lines. But for this particular app we want only the subway lines.

Write a function that takes the response object dict from the last section as input and returns a dict with **only** the data relevant to our app as a response.

## Example

```python
data = get_subway_status({...}) # the input is the dict from URL request
print(data) # {'ACE': 'Delays', 'L': 'LOL fckked', ..., 'S': 'Service Change'}, etc
```
