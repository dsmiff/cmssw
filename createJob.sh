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
}

DATE=`date -I`
alias changeDir="cd $DATE"
mkdir $DATE
changeDir
wget https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-248005_13TeV_PromptReco_Collisions15_ZeroTesla_JSON_CaloOnly.txt
createBatchScript
cp ../das_client.py .
cp ../miniAOD-prod_BATCH.py .
ARRAY="$(grep -Po '".*?"' Cert_246908-248005_13TeV_PromptReco_Collisions15_ZeroTesla_JSON_CaloOnly.txt | tr -d '"')"
echo "Certified runs:"
echo $ARRAY
echo " "
echo "Find dataset with: "
for i in ${ARRAY};  do echo " " ./das_client.py --query=\"dataset dataset=/*/Run2015A-PromptReco-v1/AOD run="${i}"\" --limit 0; done