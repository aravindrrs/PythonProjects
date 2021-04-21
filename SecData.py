from sec_edgar_downloader import Downloader
filelocation= Downloader("C:\\Users\\aravi8\\Documents\\PythonProjects\\SECFilings")
filelocation.get ('13F-HR' , 'Man Group', amount = 1)

