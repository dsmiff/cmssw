#include <FWCore/Framework/interface/MakerMacros.h>


#include "EventFilter/EcalRawToDigi/plugins/EcalRawToRecHitRoI.h"
DEFINE_FWK_MODULE(EcalRawToRecHitRoI);

#include "EventFilter/EcalRawToDigi/plugins/EcalRawToRecHitFacility.h"
DEFINE_FWK_MODULE(EcalRawToRecHitFacility);

#include "EventFilter/EcalRawToDigi/plugins/EcalRawToRecHitProducer.h"
DEFINE_FWK_MODULE(EcalRawToRecHitProducer);

#include "EventFilter/EcalRawToDigi/plugins/EcalRawToRecHitByproductProducer.h"
DEFINE_FWK_MODULE(EcalRawToRecHitByproductProducer);

#include "FWCore/Framework/interface/ModuleFactory.h"
#include "EventFilter/EcalRawToDigi/plugins/EcalRegionCablingESProducer.h"
DEFINE_FWK_EVENTSETUP_MODULE(EcalRegionCablingESProducer);

#include "EventFilter/EcalRawToDigi/plugins/EcalUnpackerWorkerESProducer.h"
DEFINE_FWK_EVENTSETUP_MODULE(EcalUnpackerWorkerESProducer);

#include "EventFilter/EcalRawToDigi/plugins/EcalRawToDigi.h"
DEFINE_FWK_MODULE(EcalRawToDigi);

#include "EventFilter/EcalRawToDigi/interface/MatacqProducer.h"
DEFINE_FWK_MODULE(MatacqProducer);

#include "EventFilter/EcalRawToDigi/interface/EcalDumpRaw.h"
DEFINE_FWK_MODULE(EcalDumpRaw);

