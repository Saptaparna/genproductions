import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
	comEnergy = cms.double(13000.0),
	crossSection = cms.untracked.double(1.333),
	filterEfficiency = cms.untracked.double(1),
	maxEventsToPrint = cms.untracked.int32(0),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	pythiaPylistVerbosity = cms.untracked.int32(1),
	PythiaParameters = cms.PSet(
	        pythia8CommonSettingsBlock,
		pythia8CUEP8M1SettingsBlock,
		processParameters = cms.vstring(
                        'Main:numberOfEvents = 1000',         	# number of events to generate
                        'Init:showChangedSettings = on',        # list changed settings
                        'Init:showChangedParticleData = on',    # list changed particle data
                        'Next:showScaleAndVertex = on',
                        'Next:numberCount = 100',               # print message every n events
                        'Next:numberShowInfo = 10',             # print event information n times
                        'Next:numberShowProcess = 10',          # print process record n times
                        'Next:numberShowEvent = 10',            # print event record n times
                        'ParticleDecays:xyMax = 30000',         # in mm/c
                        'ParticleDecays:zMax = 30000',          # in mm/c
                        'ParticleDecays:limitCylinder = on',    # yes
                        'HiddenValley:gg2DvDvbar = on',         # gg fusion
                        'HiddenValley:qqbar2DvDvbar = on',      # qqbar fusion
                        'HiddenValley:alphaOrder = 1',          # Let it run
                        'HiddenValley:Ngauge = 3',              # Number of dark QCD colours
                        'HiddenValley:nFlav = 7',               # flavours used for the running
                        'HiddenValley:FSR = on',                
                        'HiddenValley:fragment = on',           
                        'HiddenValley:spinFv = 0',              # Spin of bi-fundamental res.
                        '4900001:m0 = 1000',                    # Mass of bi-fundamental resonance
                        '4900001:mWidth = 10',                  # Width of bi-fundamental resonance
                        '4900002:m0 = 50000',
                        '4900003:m0 = 50000',
                        '4900004:m0 = 50000',
                        '4900005:m0 = 50000',
                        '4900006:m0 = 50000',
                        'HiddenValley:Lambda=4.',
                        'HiddenValley:pTminFSR = 4.4',
                        '4900101:m0 = 4',		        # dark quark mass = LambdaHV
                        '4900111:m0 = 2',	                # dark scalar (pion) mass
			'4900211:m0 = 2', 
			'4900111:tau0 = 5',			# dark scalar (pion) lifetime (in mm)
			'4900211:tau0 = 5',
			'4900113:m0 = 8',			# dark vector (rho) mass
			'4900213:m0 = 8', 
                        '4900111:0:all =  1 1.0    91    1       -1',      	# dark pion decay to down quarks
 			'4900113:0:all =  1 0.999  91  4900111  4900111', 	# dark vector to dark pions 99.9%
			'4900113:addchannel = 1 0.001 91 1 -1', 	        # dark vector to down quarks 0.1%
			'4900211:oneChannel =  1 1.0    91    1       -1',      # dark pion decay to down quarks
			'4900213:oneChannel =  1 0.999  91  4900211  4900211',	# dark vector to dark pions 99.9%
			'4900213:addchannel = 1 0.001 91 1 -1',         	# dark vector to down quarks 0.1%                       
		),
		parameterSets = cms.vstring('pythia8CommonSettings',
		                            'pythia8CUEP8M1Settings',
		                            'processParameters')
	)
)

ProductionFilterSequence = cms.Sequence(generator)
