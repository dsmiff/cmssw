#!/usr/bin/env python
#!/bin/sh
import os
import sys
import optparse
import subprocess
from os import popen

# Bristol SE: lcgse01.phy.bris.ac.uk/dpm/phy.bris.ac.uk/home/cms/store/user
# Imperial SE: gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms%s'
# CERN SE: eoscms.cern.ch//eos/cms

bristol = "soolin.phy.bris.ac.uk"
imperial = "ic.ac.uk"
cern = "cern.ch"

#dir="/JetHT/JetHT_13TeV_Data/150629_160238/0000/"


##__________________________________________________________
def parse_args():
    parser = optparse.OptionParser()
    parser.add_option("--dry_run", action = "store_true", default = False, help = "do not run any commands; only print them")
    parser.add_option("-H", "--HOST", help = "HOST")
    parser.add_option("--add_user", action="store_true",default=False, help="List contents for user")
    parser.add_option("--from-site",action="store",dest="FROM_SITE",default="",help="SOURCE")
    parser.add_option("--to-site",action="store",dest="TO_SITE",default="",help="DESTINATION")
    (options,args) = parser.parse_args()
                
    return options

##__________________________________________________________
def _check_host(host, user):
    """
    List samples of SE of current HOST
    """
    
    options = parse_args()
    
    if options.HOST:
        HOST = options.HOST
        if 'imperial' in HOST:
            SEdir = 'srm://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/'
            _listSamples(host,user,SEdir)
        elif 'bristol' in HOST:
            SEdir = 'gsiftp://lcgse01.phy.bris.ac.uk/dpm/phy.bris.ac.uk/home/cms/store/'
            _listSamples(host,user,SEdir)
            _copySamples(host,user,SEdir)
        elif 'cern' in HOST:
            SEdir = 'srm://srm-eoscms.cern.ch//eos/cms/store/'
            _listSamples(host, user, SEdir)

    else:
        if cern in host:
            SEdir = 'srm://srm-eoscms.cern.ch//eos/cms/store/'
            _listSamples(host, user, SEdir)
        elif bristol in host:
            SEdir = 'gsiftp://lcgse01.phy.bris.ac.uk/dpm/phy.bris.ac.uk/home/cms/store/'
            _listSamples(host,user,SEdir)
        elif imperial in host:
            SEdir = 'srm://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/'
            _listSamples(host,user,SEdir)
        else:
            sys.exit("HOST not found")


##____________________________________________________________
def _listSamples(host, user, SEdir):

    options = parse_args()

    if options.add_user:
        SEdir=SEdir+"user/"+user
#    if  dir:
#       SEdir=SEdir+dir
#        print SEdir

    options = parse_args()

    cmd = ['gfal-ls']
    cmd.append(SEdir)
    cmd = ' '.join(cmd)
    
    if options.dry_run:
        print 'cmd ',cmd
    else:
        print "Host ", host
        print "-> " , cmd
        os.system(cmd)
        os.popen("sleep 1")
    
##____________________________________________________________
def _copySamples(host,user,SEdir):

    options = parse_args()
    cmd = ['gfal-ls']

    if options.add_user:
        SEdir=SEdir+"user/"+user

    cmd.append(SEdir)
    cmd.append('| xargs -iI echo gfal-copy ' + SEdir)

    # Copy output of command to script
    cmd.append(' > fileList.sh')
    cmd = ' '.join(cmd)

    if options.dry_run:
        print 'copy cmd ' , cmd
    else:
        print "-> " , cmd
        os.system(cmd)
    print "Output in fileList.sh"



##____________________________________________________________
def main():

    try:
        host = os.environ["HOSTNAME"]
        user = os.environ["USER"]
    except Exception, e:
        print >> sys.stderr, "HOST does not exist"
        print >> sys.stderr, "Exception: %s" % str(e)
        sys.exit(1)
        
    _check_host(host, user)



##____________________________________________________________
if __name__ == '__main__':
    """
    Run main()
    """
    main()
