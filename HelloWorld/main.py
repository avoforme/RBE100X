from XRPLib.differential_drive import DifferentialDrive

drive: DifferentialDrive = DifferentialDrive.get_default_differential_drive()
drive.straight(20, 0.5)
