# Programming Task

### The Task
The task is to parse a log file containing HTTP requests and to report on its contents.

For a given log file report:
* The number of unique IP addresses
* The top 3 most visited URLs
* The top 3 most active IP addresses

### Example Data
`177.71.128.21 - - [10/Jul/2018:22:21:28 +0200] "GET /intranet-analytics/ HTTP/1.1" 200 3574`

### Pre-requisites 
* [Python 3.6+ Installation](https://www.python.org/downloads/)

### Running the solution
`py -3 main.py <PATH_TO_INPUT_FILE>`

### Running the tests
`py -3 tests.py`
