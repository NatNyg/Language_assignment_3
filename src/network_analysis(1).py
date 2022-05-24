"""
First I'll import the packages I'll be using throughout the script 
"""
# System tools
import os
import argparse 

# Pandas
import pandas as pd

# Network analysis tools
import networkx as nx

# Matplotlib for plotting
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,20)


def directory(directory_name):
    """
This function takes a user-defined directory and loads the files into a filelist. It then does the following for each file:
- reads the data of the file using pandas
- creates a network using the extracted edgelist from that file (using the nx.from_pandas_edgelist)
- draws that network using the draw_networkx function
- saves the drawn network as an image to the "out" folder with the name of the file
- calculates degree, eigenvector centrality and betweenness centrality - all of which is then saved in a dataframe also containing the name of each node in the network. The dataframe is then saved to a .csv file to the "out" folder with the name of the file contained in the output filename.
    """
    
    directory_path = os.path.join("in",directory_name)
    file_list = []
    
    for filename in os.listdir(directory_path):
        path = os.path.join(directory_path, filename)
        file_list.append(path)
        
        for filepath in file_list:
            data = pd.read_csv(filepath, sep="\t") 
            G = nx.from_pandas_edgelist(data, "Source", "Target", ["Weight"])
            nx.draw_networkx(G, with_labels=True, node_size=20, font_size=10)
            nw_outpath = os.path.join("Out",f"network_{filename}.png")
            plt.savefig(nw_outpath, dpi=300, bbox_inches="tight")
            plt.clf()
            degrees = G.degree()
            degrees_df =pd.DataFrame(degrees, columns =["Name","Degree"])
            ev = nx.eigenvector_centrality(G)
            eigenvector_df = pd.DataFrame(ev.items(), columns = ["Name","Eigenvector"]).sort_values('Name', ascending=True)
            bc = nx.betweenness_centrality(G)
            betweenness_df = pd.DataFrame(bc.items(), columns = ["Name", "Centrality"])
            csv_outpath = os.path.join("out",f"Network_analysis_{filename}.csv")
        
            list_data = list(zip(eigenvector_df["Name"],degrees_df["Degree"], betweenness_df["Centrality"], eigenvector_df["Eigenvector"]))
        
            pd.DataFrame(list_data, columns = ["Name","Degree","Centrality","Eigenvector"]).to_csv(csv_outpath)
    

def single_file(directory_name, filename):
    """
This function basically does the exact same as the one above - but instead of looping over all files in a directory, this just performs the network analysis on a single user-defined file. That means that for a single file the function does the following:
- reads the data of the file using pandas
- creates a network using the extracted edgelist from that file (using the nx.from_pandas_edgelist)
- draws that network using the draw_networkx function
- saves the drawn network as an image to the "out" folder with the name of the file
- calculates degree, eigenvector centrality and betweenness centrality - all of which is then saved in a dataframe also containing the name of each node in the network. The dataframe is then saved to a .csv file to the "out" folder with the name of the file contained in the output filename.
    """
    filepath = os.path.join("in",directory_name,filename)
    data = pd.read_csv(filepath, sep="\t") 
    
    G = nx.from_pandas_edgelist(data, "Source", "Target", ["Weight"])
    nx.draw_networkx(G, with_labels=True, node_size=20, font_size=10)
    nw_outpath = os.path.join("out",f"network_{filename}.png")
    plt.savefig(nw_outpath, dpi=300, bbox_inches="tight")
    
    degrees = G.degree()
    degrees_df =pd.DataFrame(degrees, columns =["Name","Degree"])
    ev = nx.eigenvector_centrality(G)
    eigenvector_df = pd.DataFrame(ev.items(), columns = ["Name","Eigenvector"]).sort_values('Name', ascending=True)
    bc = nx.betweenness_centrality(G)
    betweenness_df = pd.DataFrame(bc.items(), columns = ["Name", "Centrality"])
    
    csv_outpath = os.path.join("out",f"Network_analysis_{filename}.csv")
    list_data = list(zip(eigenvector_df["Name"],degrees_df["Degree"],
                         betweenness_df["Centrality"], eigenvector_df["Eigenvector"]))
    
    pd.DataFrame(list_data, columns = ["Name","Degree","Centrality","Eigenvector"]).to_csv(csv_outpath)


    
def parse_args():
    """
This function intialises the argumentparser and defines the command line parameters
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("-dn","--directoryname",required=False, help = "The directory of files to make network analysis on")
    ap.add_argument("-fn","--filename",required=False, help = "The file to make network analysis on")
    args = vars(ap.parse_args())
    return args 

    
def main():
    """
This function defines which functions to run when the script is executed from the terminal. This main function includes two if-statements, defining to run the single_file function if a single filename and a directoryname is passed by the user, and to run the directory function if a directoryname is passed by the user. 
This allows for flexibility, as the script can then be run on any input data, as long as the input format is correct and the columnnames are the same. 
    """
    args = parse_args()
    if args["filename"] is not None and args["directoryname"] is not None:
        single_file(args["directoryname"], args["filename"])
        
            
    elif args["directoryname"] is not None and args["filename"] is None:
        directory(args["directoryname"])
     
    
if __name__== "__main__":
    main()