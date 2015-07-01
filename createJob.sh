createBatchScript() {

echo "export CMSSW_PROJECT_SRC=\"CMGTools/CMSSW_7_4_3/src\" " > lxplusbatchscript.sh  
echo "export CFG_FILE=\"miniAOD-prod_BATCH.py\" " >> lxplusbatchscript.sh
echo "export OUTPUT_FILE=\"miniAOD-prod_PAT_BATCH.root\" " >> lxplusbatchscript.sh
echo "export TOP=\"\$PWD\" " >> lxplusbatchscript.sh
echo " " >> lxplusbatchscript.sh

echo "cd /afs/cern.ch/work/d/dosmith/$CMSSW_PROJECT_SRC" >> lxplusbatchscript.sh
echo "eval \`scramv1 runtime -sh\` "  >> lxplusbatchscript.sh
echo "cd $TOP" >> lxplusbatchscript.sh
echo "cmsRun /afs/cern.ch/work/d/dosmith/$CMSSW_PROJECT_SRC/$CFG_FILE" >> lxplusbatchscript.sh
echo "rfcp miniAOD-prod_PAT_BATCH.root /afs/cern.ch/work/d/dosmith/public/alphat/$OUTPUT_FILE" >> lxplusbatchscript.sh

chmod 777 lxplusbatchscript.sh
}

DATE=$(date +"%d_%b_%y_%H%M")
JOBDIR="jobs_${DESCRIPTION}_${DATE}"
alias changeDir="cd $JOBDIR"
if [ ! -d "$JOBDIR" ] ; then
    mkdir $JOBDIR
else
    echo "Directory already exists"
    exit 1
fi
changeDir
wget https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-248005_13TeV_PromptReco_Collisions15_ZeroTesla_JSON_CaloOnly.txt

# Copy relevant files to jobs directory
cp ../das_client.py .
cp ../miniAOD-PROD_CRAB.py .
cp ../CrabConfiguration.py .
sed -i 's@/src/@/src/'"$JOBDIR"'/@g' CrabConfiguration.py

ARRAY="$(grep -Po '".*?"' Cert_246908-248005_13TeV_PromptReco_Collisions15_ZeroTesla_JSON_CaloOnly.txt | tr -d '"')"
echo "Certified runs:"
echo $ARRAY
echo " "
echo "Find dataset with: "
for i in ${ARRAY};  do echo " " ./das_client.py --query=\"dataset dataset=/*/Run2015A-PromptReco-v1/AOD run="${i}"\" --limit 0; done

echo " " 
echo "Please edit the CrabConfiguration file to select your desired dataset and JSON file"
