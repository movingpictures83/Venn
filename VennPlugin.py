import seaborn as sns
import pandas as pd
from venn import venn
from matplotlib import pyplot as plt

# number of unique genes per sample


import PyPluMA
import PyIO

class VennPlugin:
    def input(self, inputfile):
        self.parameters = PyIO.readParameters(inputfile)
        df = pd.read_csv(PyPluMA.prefix()+"/"+self.parameters["csvfile"])
        groups = PyIO.readSequential(PyPluMA.prefix()+"/"+self.parameters["groupfile"])
        attribute = self.parameters["attribute"]
        self.genes = dict()
        for group in groups:
            self.genes[group+"_genes"] = set((df[df['Group']==group])[attribute].unique())

    def run(self):
        pass

    def output(self,outputfile):
        venn(self.genes)
        plt.savefig(outputfile)

