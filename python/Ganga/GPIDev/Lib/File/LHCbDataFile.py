################################################################################
# Ganga Project. http://cern.ch/ganga
#
# $Id: LHCbDataFile.py,v 0.1 2011-10-03 15:40:00 idzhunov Exp $
################################################################################

from Ganga.GPIDev.Schema import *

from OutputFile import OutputFile

class LHCbDataFile(OutputFile):
    """LHCbDataFile represents a class marking a file to be stored
       in Storage Element and registered in LHCb file catalogue
    """
    _schema = Schema(Version(1,1), {'name': SimpleItem(defvalue="",doc='name of the file')})
    _category = 'outputfiles'
    _name = "LHCbDataFile"

    def __init__(self,name='', **kwds):
        """ name is the name of the output file that has to be stored
            in Storage Element and registered in LHCb file catalogue 
        """
        super(LHCbDataFile, self).__init__(name, **kwds)


    def __construct__(self,args):
            super(LHCbDataFile,self).__construct__(args)

            
    def __repr__(self):
        """Get the representation of the file."""

        return "LHCbDataFile(name='%s')"% self.name


# add LHCbDataFile objects to the configuration scope (i.e. it will be possible to write instatiate LHCbDataFile() objects via config file)
import Ganga.Utility.Config
Ganga.Utility.Config.config_scope['LHCbDataFile'] = LHCbDataFile
