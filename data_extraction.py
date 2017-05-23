
import os
from statistics import mean
from statistics import median
from tkinter import *
from tkinter import ttk

class Weather_Type:

    ### Sets up the GUI using a combo box so headers can be selected
    ### Calls the weather class with the selection and filename
    ### and returns median and mean which are displayed using text entry
    
    def __init__(self, master, filename):
        self._newfile = filename
        self._mean = 0
        self._median = 0
        new_header = Header(filename)
        self._headers = new_header.get_list()
        self._master = master
        self.create_labels()
        self.combo()
        
        
    def newselection(self, event):
        self.value_of_combo = self.box.get()
        print(self.value_of_combo)
        my_weather = Weather(self._newfile, self.value_of_combo)
        #self.display(my_weather.mean(), my_weather.median())
        self._mean = my_weather.mean()
        self._median = my_weather.median()
        self.display()

    def combo(self):
        self.box_value = StringVar()
        self.box = ttk.Combobox(self._master, textvariable=self.box_value, 
                                state='readonly')
        self.box['values'] = self._headers
        self.box.current(0)
        self.box.grid(column=0, row=0, columnspan=2)
        self.box.bind("<<ComboboxSelected>>", self.newselection)
    
    def create_labels(self):
        self.mean_lbl = ttk.Label(self._master, text = 'Mean')
        self.mean_lbl.grid(row=1, column=0)
        self.median_lbl = ttk.Label(self._master, text = 'Median')
        self.median_lbl.grid(row=1, column=1)
        self.mean_dis = ttk.Entry(self._master, width = 10 )
        self.mean_dis.grid(row=2, column=0)
        self.median_dis = ttk.Entry(self._master, width = 10)
        self.median_dis.grid(row=2, column=1)

    def display(self):
        self.mean_dis.delete(0, END)
        self.median_dis.delete(0, END)
        self.mean_dis.insert(0, '{:1.1f}'.format(self._mean))
        self.median_dis.insert(0, '{:1.1f}'.format(self._median))
        
        
class Weather:

    ### Take in the filename and info from the GUI
    ### Runs the Header to return the dictionary of header items
    ### which are indexed to put the specific item into an array
    ### mean and median are then calulated and returnd to the GUI
    
    def __init__(self, file_name, info = 'Wind_Speed'):
        self._infile = file_name
        self._info = info
        self._values = []
        
        self.new_header = Header(file_name)
        self._header_dic = self.new_header.get_dic()
        self._index = self._header_dic[self._info]
        self.get_values()

        
    def get_values(self):
        count = 0
        nodata_count = 0
        total = 0
        index = 0
        with open(self._infile, 'r') as f:
    
            for line in f:
                try:
                    bob = float(line.split('\t')[self._index])
                    count += 1
                except:
                    bob = 0
                    nodata_count += 1
                    print('No data')
                if nodata_count > 10:
                    print('Try a different parameter')
                    break
                self._values.append(bob)
                total += bob


    def mean(self):
        my_mean = mean(self._values)
        print('Mean {}: {:1.1f}'.format(self._info, my_mean))
        return my_mean

    def median(self):
        my_median = median(self._values)
        print('Median {}: {:1.1f}'.format(self._info, my_median))
        return my_median

class Header:
    ### takes the file name and returns the headers in a value list
    ### or in dictionary form for accessing the parameter
    

    def __init__(self, file_name):
        self._infile = file_name
        self.header = ()

        with open(self._infile, 'r') as f:
            count = 0
            for line in f:
                self.header = line.strip('\n')
                count +=1
                if count >0:
                    break
                
    def get_list(self):
        return self.header.split('\t')

    def get_dic(self):
        header_list = self.header.split('\t')
        dic_list = zip(header_list,range(len(header_list)))
        return dict(dic_list)

def main():

    
    newfile = '/home/ruppyrup/Documents/Python/Code Clinic/Ex_Files_FAQs/Ex_Files_CC_Python_01/Exercise Files/Problem 1/LPO_weatherdata-master/Environmental_Data_Deep_Moor_2015.txt'
    #newfile = 'newfile.txt'
    root = Tk()
    my_weather = Weather_Type(root, newfile)
    
    root.mainloop()
    

if __name__ == "__main__": main()

 

