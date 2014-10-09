INPUTFILE=$1

echo "Input file is $INPUTFILE"

if grep -Fr "GCT fibre data error" $INPUTFILE || grep -Fr "Gct fibre data error" $INPUTFILE
then
echo "Found a Fibre Data Error"
else
echo "No Fibre Data Error Found"
fi
 
