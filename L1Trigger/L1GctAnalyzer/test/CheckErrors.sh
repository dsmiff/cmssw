INPUTFILE=$1
errorfile=${INPUTFILE%.*}


if [ $# -eq 0 ]
then
    echo "No input file"
    exit 1
fi  




echo "Input file is $INPUTFILE"

if grep -Fr "GCT fibre data error" $INPUTFILE -A 1 || grep -Fr "Gct fibre data error" $INPUTFILE -A 1  
then
echo "Found a Fibre Data Error"
grep -Fr "GCT fibre data error" $INPUTFILE -A 1 >> $errorfile.stderr
grep -Fr "Gct fibre data error" $INPUTFILE -A 1 >> $errorfile.stderr
else
echo "No Fibre Data Error Found"
fi
 
