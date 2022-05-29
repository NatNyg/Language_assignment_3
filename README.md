# Language_assignment_3 - Network Analysis

## This is the repository for assignment 3 in Language Analytics.

## Project Description
This project uses a script to perform network analysis. The script can take any input data as long as the input format (and same column names) as the dataset I have used for testing; "network_data". 
The script allows the user to input either a directory name or a filename, and based on either of the two, for each file:
- load the edgelist 
- perform network analysis on undirected, weighted edgelists using the networkx function 
- save a visualization of the network, and
- save a csv that contains name; degree; betweenness centrality and eigenvector_centrality for every node. 


## Repository Structure

The repository includes three folders:

    in: this folder should contain the data that the code is run on
    out: this folder will contain the results after the code has been run
    src: this folder contains the script of code that must be run to achieve the results

## Method
The script contains two functions (besides the main function and parse_args function); 
One that defines what to do if the user inputs the name of a directory, and one that defines what to do if the user inputs the name of directory and a single file. Both of the functions essentially does the same - the directory one just loops over each files in the directory and performs the previously mentioned steps on each file. 

The functions perform the following steps:
- loads the file using pandas read_csv function
- uses the networkx function on the edgelist (derived using from_pandas_edgelist) to create a network and draw it. The visualised network is then saved to the "out" folder 
- degree, eigenvector and betweenness centrality is then calculated (degree by using the degree function on the network, and eigenvector and betweenness by using the networkx functions). These values are then saved to a dataframe with the name of the file, transforms the dataframe to a .csv file which is then saved to the "out" folder. 


## Usage

In order to reproduce the results I have gotten (and which can be found in the "out" folder), a few steps has to be followed:

1) Install the relevant packages - relevant packages for the script can be found in the "requirements.txt" file.
2) Make sure to place the script in the "src" folder and the data in the "in" folder. Ross has the data used for this project, but the script can also run on any other file or dictionary, as long as it has the same format and column names. 
3) Run the script from the terminal and remember to pass the required arguments  - either -fn (filename) and -dn (directory_name) , if you want the script to run on only one file, or -dn (directory_name) if you want the script to run on the whole directory.
 -> Make sure to navigate to the main folder before executing the script - then you just have to type the following in the terminal: 

python src/network_analysis.py -fn {name of the desired filename} -dn {name of the desired directory} 

or,

python src/network_analysis.py -dn {name of the desired directory}
 

This should give you the same results as I have gotten in the "out" folder if you do it on the network data.

## Results

As addressed my results are placed in the "out" - I have made two subfolders in the out - one that contains a csv file for each of the files in the network_data, and one that contains a png file for each of the files that I have performed network analysis on. The .png is useful for a quick overview of the relation between different nodes in the network, making it easy to see which of the nodes are the most central ones. The .csv file provides more elaborate information on each of the nodes in the network, including the degree, centrality, and eigenvector values. This makes it possible for the user to understand the network in terms of the relations.   
