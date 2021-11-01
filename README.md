
## Problem

### original data (shortened)
id   | remarks                                           |
:----| :-------------------------------------------------|
9613 | "Tablet Internet -phone , Free 1 GB Wi-FI Service"|
9601 | Free - Up to 25 mbs Wi-Fi Service                 |

### revised data after loading it using csv DictReader

id   | remarks                                           |                                |
:----| :-------------------------------------------------| :------------------------------|
9613 | Tablet Internet                                   |  -phone Free 1 GB Wi-FI Service|
9601 | Free - Up to 25 mbs Wi-Fi Service                 |                                |

Hi,  

I have been working on the data munging part of the practice exams and I am having troubles with properly saving my work as a csv file. Specifically, I am struggling with properly storing some the `remarks` values in the `wifi.csv` file. As shown above, some of the `remarks` values are multi-valued, where the value contains a comma inside and is delimited by a double quotation.  

I was originally trying to:
1. iterate through each row of the list of dictionaries, that I created in the first function
2. Then, storing the field values of each row as a list using `row.values()`
3. Combining the values delimited by a comma using `",".join(for val in row.values())`.   

This works when the `remarks` value doesn't contain a comma inside, as shown above in the second row (`id`=9601), However, if it does, the quotations are removed and treats the value as two separate value. So, instead of storing the value as `"Tablet Internet -phone , Free 1 GB Wi-FI Service"`, it stores the value as `Tablet Internet -phone, Free 1 GB Wi-FI Service`. This shifts all the remaining values to the right and messes up the csv file.  

My question is how do I retain the double quotations and treating this nested value as a single value, while still delimiting the rest by a comma. I am confused because in `row.values()`, the value still retains its quotation marks, but it disappears after using `",".joins()`. 

Inside this repository I attached:
- my code (`code.py`)
- the original data file (`wifi.csv`)
- the shortened data file, containing only the two rows shown above (`practice_data.csv`)
- the csv file, I generated using my code (`trial.csv`)