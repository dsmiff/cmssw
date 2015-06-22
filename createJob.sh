createBatchScript() {

echo "export CMSSW_PROJECT_SRC=\"CMGTools/CMSSW_7_4_3/src\" " > test.sh  
echo "export CFG_FILE=\"miniAOD-prod_BATCH.py\" " >> test.sh
echo "export OUTPUT_FILE=\"miniAOD-prod_PAT_BATCH.root\" " >> test.sh
echo "export TOP=\"\$PWD\" " >> test.sh
echo " " >> test.sh

echo "cd /afs/cern.ch/work/d/dosmith/\$CMSSW_PROJECT_SRC" >> test.sh
echo "eval \`scramv1 runtime -sh\` "  >> test.sh
echo "cd \$TOP" >> test.sh
echo "cmsRun /afs/cern.ch/work/d/dosmith/\$CMSSW_PROJECT_SRC/\$CFG_FILE" >> test.sh
echo "rfcp miniAOD-prod_PAT_BATCH.root /afs/cern.ch/work/d/dosmith/public/alphat/\$OUTPUT_FILE" >> test.sh
}

DATE=`date -I`
alias changeDir="cd $DATE"
mkdir $DATE
changeDir
wget https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-248005_13TeV_PromptReco_Collisions15_ZeroTesla_JSON_CaloOnly.txt
createBatchScript
echo "Certified runs:"
array=`grep -Po '".*?"' Cert_246908-248005_13TeV_PromptReco_Collisions15_ZeroTesla_JSON_CaloOnly.txt`