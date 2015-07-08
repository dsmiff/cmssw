#!/usr/bin/env python
#!/bin/sh
import os
import sys
import optparse
import subprocess
import logging
 
# Bristol SE: lcgse01.phy.bris.ac.uk/dpm/phy.bris.ac.uk/home/cms/store/user
# Imperial SE: gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms%s'
# CERN SE: eoscms.cern.ch//eos/cms

bristol = "soolin.phy.bris.ac.uk"
imperial = "ic.ac.uk"
cern = "cern.ch"

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
logging.basicConfig(filename='copyData.log',level=logging.INFO)

##__________________________________________________________
def parse_args():
    parser = optparse.OptionParser()
    parser.add_option("--dry_run", action = "store_true", default = False, help = "do not run any commands; only print them")
    parser.add_option("-H", "--HOST", help = "HOST")
    parser.add_option("--add_user", action="store_true",default=True, help="List contents for user")
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
def _listDir(SEdir):

    proc = subprocess.Popen(['gfal-ls',SEdir],stdout=subprocess.PIPE)
    tmp = proc.stdout.read()
#    print 'type ' ,tmp.split()
    ret = [ ]
    logging.info('Directory %s', tmp)
    for d in tmp.split():
        if d.endswith('.root'):
            ret.append(os.path.join(SEdir,d))
        else:
            ret.extend(_listDir(os.path.join(SEdir,d)))
    return ret

##_____________________________________________________________
def _listSamples(host, user, SEdir):

    options = parse_args()

    ReadFile_ = open("list.txt","r")

    if options.add_user:
        SEdir=SEdir+"user/"+user

    options = parse_args()

    cmd = ['gfal-ls']
    cmd.append(SEdir)
    cmd = ' '.join(cmd)
    
    if options.dry_run:
        print 'cmd ',cmd
    else:
        print "Host ", host
        print "-> " , cmd
        CompList = _listDir(SEdir)
        os.system(cmd)
        _Copy(CompList)

##____________________________________________________________
def _Copy(CompList):

    options = parse_args()

    file_ = open("fileList.sh","w")
    
    if options.TO_SITE == 'imperial':
        DestDir = 'srm://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/'
    elif options.TO_SITE == 'bristol':
        DestDir = 'gsiftp://lcgse01.phy.bris.ac.uk/dpm/phy.bris.ac.uk/home/cms/store/'
    elif options.TO_SITE == 'cern':
        DestDir = 'srm://srm-eoscms.cern.ch//eos/cms/store/'
    else:
        print "Need to specifiy destination site"

    for item in CompList:
        item = 'gfal-copy '+ item + ' ' + DestDir +"\n"
        file_.write(item)
    file_.close()
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
    logging.info('Host %s', host)
    logging.info('User %s', user)

##____________________________________________________________
if __name__ == '__main__':
    """
    Run main()
    """
    main()
