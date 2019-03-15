# Exercise 4
# Kommentar: blablabla, Github ist sch...
# exercise: E4_Christina.py (-> wie man mit np.loadtxt files reinlädt...no paar Sachen in Klammern spezifizieren)...dann f.min(), f.max(),f.mean()

def precip_overview(my_file):

  #list my_file
  f = open(my_file,'r')
  mylist = list(f)
  mylist = mylist[1:]

  # initialize empty list
  precip = []

  # create new list
  for item in mylist:
    precip.append(float(item.split()[2]))

  # calculate max, min, mean
  max_precip = max(precip)
  min_precip = min(precip)
  mean_precip = round((sum(precip)/len(precip)),1)

  return [max_precip,min_precip,mean_precip]

# die Funktion precip_overview wird an einem spezifischen Input-File getestet:
path = r"C:\Users\david\Desktop\Studiordner\FS19\Geodata_Analysis\03\precip_data.txt"
results = precip_overview(path)
print("Maximum precipitation: {}\nMinimum Precipitation: {}\nMean Precipitation: {}".format(results[0],results[1],results[2]))



