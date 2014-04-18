#ifndef CALO_TOPOLOGY_HCAL_TOPOLOGY_MODE_H
# define CALO_TOPOLOGY_HCAL_TOPOLOGY_MODE_H

#include "FWCore/Utilities/interface/Exception.h"
#include <map>
#include <string>
#include <algorithm>

template< typename T >
class StringToEnumParser
{
    std::map< std::string, T > enumMap;
public:
    
    StringToEnumParser( void );

    T parseString( const std::string &value )
	{ 
	    typename std::map<std::string, T>::const_iterator iValue = enumMap.find( value );
	    if( iValue  == enumMap.end())
                throw cms::Exception( "Configuration" )
		    << "the value " << value << " is not defined.";
	    
	    return iValue->second;
	}
};

namespace HcalTopologyMode {
    enum Mode {
	LHC=0, H2=1, SLHC=2, H2HE=3 };

    enum TriggerMode {
      tm_LHC_PreLS1=0, // HF is summed in 3x2 regions
      tm_LHC_PreLS1_and_1x1=1, // HF is summed in both 3x2 and 1x1 regions (simultaneously)
      tm_LHC_1x1=2  // HF is summed in 1x1 regions
    };
}


#endif // CALO_TOPOLOGY_HCAL_TOPOLOGY_MODE_H
