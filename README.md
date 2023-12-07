## Rylan Moore - Advanced Operating Systems Semester Project
# Running PySpark workloads on the Raspberry Pi 4
Low cost edge computing is made possible by the raspberry pi. This work looks at the feasibility of using containerized software on the Raspberry Pi to deploy such work. For testing a benchmark was created. Based on PySpark and adapted from CSCI 4253 Lab 4 of Datacenter Scale Computing from CU Boulder. The program timed_dataframe.py is the resulting benchmark program. This program does large data operations that result in a table of patents sorted by the number of times they are cited by other patents in the list. This program reports the time it takes for the entire program to run including loading the two large dataset files, joining and sorting data, and reporting results. 

## Hardware
Raspberry Pi 4B 4GB, 256GB SATA SSD connected over USB-3, Argon One case with Active Cooling Fan, Official RPI USB-C PSU, 32-bit Raspian Bullseye. 

Test of the SSD to confirm performance: 

Random write speed 13266 IOPS (target 500) - PASS 

Random read speed 13768 IOPS (target 1500) - PASS

CPU Frequency:
2.0 GHZ

## Container Configuration
There are many different container solutions available on Raspberry Pi. To start Docker will be used. To manage packages in a easier way than running containers on the command line Portainer will be run in Docker and used for container management. The command for running Portainer can be run with "make docker_manager". The image to run the benchmark is "rylanm14/spark-server:latest" which will run the python benchmark and report the time taken for the program in the logs. 

## Local Configuration
To run the python benchmark locally java and python3 need to be installed via apt, then pyspark can be installed with pip. 

## Images
![spark](https://github.com/rylan-moore/os_proj/assets/70982815/a89fdb61-c493-41d0-8f4f-5e96b3af4883)
Image of the spark webserver showing work running. 
![portainer](https://github.com/rylan-moore/os_proj/assets/70982815/32a100c6-613c-4795-af03-aa743008e844)
Image of the portainer webserver where the Docker container for benchmarking is run from. 



## Results
Below are the results from the benchmark. The CPU temperature was allowed to return to 50 Degrees Celcius beetween runs. RAM usage was collected from HTOP running concurrently with the benchmark. 
|         | Local (s) | Local RAM (MB)| Docker cold start (s) |Docker cold start RAM (MB)| Docker warm start (S) | Docker warm start RAM (MB) |
|:--------|:---------:|:----------:|:--------:|:-:|:-:|:-:|
| Run 1   | 290.41 | 1268 | 350.29 | 1330 | 331.59 | 1346 |
| Run 2   | 297.12 | 1271 | 340.66 | 1337 | 347.52 | 1350 |
| Run 3   | 302.56 | 1301 | 339.27 | 1329 | 333.42 | 1353 |
| Run 4   | 287.42 | 1289 | 336.43 | 1336 | 330.06 | 1347 |
| Run 5   | 308.00 | 1278 | 331.78 | 1345 | 329.31 | 1353 |
| Average | 297.10 | 1281.4 | 339.69 | 1335.4 | 334.38 | 1349.8 |

### Running two copies of the container at once

||Continer 1|Container 2|
|:-:|:-:|:-:|
|Time (s)| 510.31 | 523.86|
|RAM use (MB)| 1335 | 1329 | 

### Running four copies of the container at once results in the pi crashing once memory use starts to increase in the later half of the benchmark.

## Top 10 rows from Output Table - Count is what gets appended and sorted by
|PATENT|GYEAR|GDATE|APPYEAR|COUNTRY|POSTATE|ASSIGNEE|ASSCODE|CLAIMS|NCLASS|CAT|SUBCAT|CMADE|CRECEIVE|RATIOCIT|GENERAL|ORIGINAL|FWDAPLAG|BCKGTLAG|SELFCTUB|SELFCTLB|SECDUPBD|SECDLWBD|COUNT|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|--|--|--|--|--|--|--|--|--|
|5959466| 1999|14515|   1997|     US|     CA|    5310|      2|  NULL|   326|  4|    46|  159|       0|     1.0|   NULL|  0.6186|    NULL|  4.8868|  0.0455|   0.044|    NULL|    NULL|  125|
|5983822| 1999|14564|   1998|     US|     TX|  569900|      2|  NULL|   114|  5|    55|  200|       0|   0.995|   NULL|  0.7201|    NULL|   12.45|     0.0|     0.0|    NULL|    NULL|  103|
|6008204| 1999|14606|   1998|     US|     CA|  749584|      2|  NULL|   514|  3|    31|  121|       0|     1.0|   NULL|  0.7415|    NULL|     5.0|  0.0085|  0.0083|    NULL|    NULL|  100|
|5952345| 1999|14501|   1997|     US|     CA|  749584|      2|  NULL|   514|  3|    31|  118|       0|     1.0|   NULL|  0.7442|    NULL|  5.1102|     0.0|     0.0|    NULL|    NULL|   98|
|5958954| 1999|14515|   1997|     US|     CA|  749584|      2|  NULL|   514|  3|    31|  116|       0|     1.0|   NULL|  0.7397|    NULL|   5.181|     0.0|     0.0|    NULL|    NULL|   96|
|5998655| 1999|14585|   1998|     US|     CA|    NULL|      1|  NULL|   560|  1|    14|  114|       0|     1.0|   NULL|  0.7387|    NULL|  5.1667|    NULL|    NULL|    NULL|    NULL|   96|
|5936426| 1999|14466|   1997|     US|     CA|    5310|      2|  NULL|   326|  4|    46|  178|       0|     1.0|   NULL|    0.58|    NULL| 11.2303|  0.0765|   0.073|    NULL|    NULL|   94|
|5739256| 1998|13983|   1995|     US|     CA|   70060|      2|    15|   528|  1|    15|  453|       0|     1.0|   NULL|  0.8232|    NULL| 15.1104|  0.1124|  0.1082|    NULL|    NULL|   90|
|5978329| 1999|14550|   1995|     US|     CA|  148925|      2|  NULL|   369|  2|    24|  145|       0|     1.0|   NULL|  0.5449|    NULL| 12.9241|  0.4196|  0.4138|    NULL|    NULL|   90|
|5925042| 1999|14445|   1997|     US|     CA|  733846|      2|  NULL|   606|  3|    32|  242|       0|     1.0|   NULL|  0.7382|    NULL|  8.3471|     0.0|     0.0|    NULL|    NULL|   90|
