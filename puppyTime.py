import datetime #, time

#Vars for easier calling and shorter programs
def timeUpdate():
    global UTCTime
    UTCTime = datetime.UTC

def testings():
    return("H-Hewwo! Dis is a fwuffy test of the package from an import~. If you see dis, it means my creator is at least slightly competent.")

def time(Timezone = "sys"):
    if Timezone.lower() == "sytem" or Timezone.lower() == "sys":
        return(datetime.datetime.now(tz=None))
    else:
        return(f'ERROR: \"{Timezone}\" not understood')