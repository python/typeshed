import _win32typing

def CTL_CODE(DeviceType: int, Function: int, Method: int, Access: int) -> int: ...
def DEVICE_TYPE_FROM_CTL_CODE(ctrlCode: int) -> int: ...

FILE_DEVICE_BEEP: int
FILE_DEVICE_CD_ROM: int
FILE_DEVICE_CD_ROM_FILE_SYSTEM: int
FILE_DEVICE_CONTROLLER: int
FILE_DEVICE_DATALINK: int
FILE_DEVICE_DFS: int
FILE_DEVICE_DISK: int
FILE_DEVICE_DISK_FILE_SYSTEM: int
FILE_DEVICE_FILE_SYSTEM: int
FILE_DEVICE_INPORT_PORT: int
FILE_DEVICE_KEYBOARD: int
FILE_DEVICE_MAILSLOT: int
FILE_DEVICE_MIDI_IN: int
FILE_DEVICE_MIDI_OUT: int
FILE_DEVICE_MOUSE: int
FILE_DEVICE_MULTI_UNC_PROVIDER: int
FILE_DEVICE_NAMED_PIPE: int
FILE_DEVICE_NETWORK: int
FILE_DEVICE_NETWORK_BROWSER: int
FILE_DEVICE_NETWORK_FILE_SYSTEM: int
FILE_DEVICE_NULL: int
FILE_DEVICE_PARALLEL_PORT: int
FILE_DEVICE_PHYSICAL_NETCARD: int
FILE_DEVICE_PRINTER: int
FILE_DEVICE_SCANNER: int
FILE_DEVICE_SERIAL_MOUSE_PORT: int
FILE_DEVICE_SERIAL_PORT: int
FILE_DEVICE_SCREEN: int
FILE_DEVICE_SOUND: int
FILE_DEVICE_STREAMS: int
FILE_DEVICE_TAPE: int
FILE_DEVICE_TAPE_FILE_SYSTEM: int
FILE_DEVICE_TRANSPORT: int
FILE_DEVICE_UNKNOWN: int
FILE_DEVICE_VIDEO: int
FILE_DEVICE_VIRTUAL_DISK: int
FILE_DEVICE_WAVE_IN: int
FILE_DEVICE_WAVE_OUT: int
FILE_DEVICE_8042_PORT: int
FILE_DEVICE_NETWORK_REDIRECTOR: int
FILE_DEVICE_BATTERY: int
FILE_DEVICE_BUS_EXTENDER: int
FILE_DEVICE_MODEM: int
FILE_DEVICE_VDM: int
FILE_DEVICE_MASS_STORAGE: int
FILE_DEVICE_SMB: int
FILE_DEVICE_KS: int
FILE_DEVICE_CHANGER: int
FILE_DEVICE_SMARTCARD: int
FILE_DEVICE_ACPI: int
FILE_DEVICE_DVD: int
FILE_DEVICE_FULLSCREEN_VIDEO: int
FILE_DEVICE_DFS_FILE_SYSTEM: int
FILE_DEVICE_DFS_VOLUME: int
FILE_DEVICE_SERENUM: int
FILE_DEVICE_TERMSRV: int
FILE_DEVICE_KSEC: int
FILE_DEVICE_FIPS: int
FILE_DEVICE_INFINIBAND: int
METHOD_BUFFERED: int
METHOD_IN_DIRECT: int
METHOD_OUT_DIRECT: int
METHOD_NEITHER: int
METHOD_DIRECT_TO_HARDWARE: int
METHOD_DIRECT_FROM_HARDWARE: int
FILE_ANY_ACCESS: int
FILE_SPECIAL_ACCESS: int
FILE_READ_ACCESS: int
FILE_WRITE_ACCESS: int
IOCTL_STORAGE_BASE: int
RECOVERED_WRITES_VALID: int
UNRECOVERED_WRITES_VALID: int
RECOVERED_READS_VALID: int
UNRECOVERED_READS_VALID: int
WRITE_COMPRESSION_INFO_VALID: int
READ_COMPRESSION_INFO_VALID: int
TAPE_RETURN_STATISTICS: int
TAPE_RETURN_ENV_INFO: int
TAPE_RESET_STATISTICS: int
MEDIA_ERASEABLE: int
MEDIA_WRITE_ONCE: int
MEDIA_READ_ONLY: int
MEDIA_READ_WRITE: int
MEDIA_WRITE_PROTECTED: int
MEDIA_CURRENTLY_MOUNTED: int
IOCTL_DISK_BASE: int
PARTITION_ENTRY_UNUSED: int
PARTITION_FAT_12: int
PARTITION_XENIX_1: int
PARTITION_XENIX_2: int
PARTITION_FAT_16: int
PARTITION_EXTENDED: int
PARTITION_HUGE: int
PARTITION_IFS: int
PARTITION_OS2BOOTMGR: int
PARTITION_FAT32: int
PARTITION_FAT32_XINT13: int
PARTITION_XINT13: int
PARTITION_XINT13_EXTENDED: int
PARTITION_PREP: int
PARTITION_LDM: int
PARTITION_UNIX: int
VALID_NTFT: int
PARTITION_NTFT: int
GPT_ATTRIBUTE_PLATFORM_REQUIRED: int
GPT_BASIC_DATA_ATTRIBUTE_NO_DRIVE_LETTER: int
GPT_BASIC_DATA_ATTRIBUTE_HIDDEN: int
GPT_BASIC_DATA_ATTRIBUTE_SHADOW_COPY: int
GPT_BASIC_DATA_ATTRIBUTE_READ_ONLY: int
HIST_NO_OF_BUCKETS: int
DISK_LOGGING_START: int
DISK_LOGGING_STOP: int
DISK_LOGGING_DUMP: int
DISK_BINNING: int
CAP_ATA_ID_CMD: int
CAP_ATAPI_ID_CMD: int
CAP_SMART_CMD: int
ATAPI_ID_CMD: int
ID_CMD: int
SMART_CMD: int
SMART_CYL_LOW: int
SMART_CYL_HI: int
SMART_NO_ERROR: int
SMART_IDE_ERROR: int
SMART_INVALID_FLAG: int
SMART_INVALID_COMMAND: int
SMART_INVALID_BUFFER: int
SMART_INVALID_DRIVE: int
SMART_INVALID_IOCTL: int
SMART_ERROR_NO_MEM: int
SMART_INVALID_REGISTER: int
SMART_NOT_SUPPORTED: int
SMART_NO_IDE_DEVICE: int
SMART_OFFLINE_ROUTINE_OFFLINE: int
SMART_SHORT_SELFTEST_OFFLINE: int
SMART_EXTENDED_SELFTEST_OFFLINE: int
SMART_ABORT_OFFLINE_SELFTEST: int
SMART_SHORT_SELFTEST_CAPTIVE: int
SMART_EXTENDED_SELFTEST_CAPTIVE: int
READ_ATTRIBUTE_BUFFER_SIZE: int
IDENTIFY_BUFFER_SIZE: int
READ_THRESHOLD_BUFFER_SIZE: int
SMART_LOG_SECTOR_SIZE: int
READ_ATTRIBUTES: int
READ_THRESHOLDS: int
ENABLE_DISABLE_AUTOSAVE: int
SAVE_ATTRIBUTE_VALUES: int
EXECUTE_OFFLINE_DIAGS: int
SMART_READ_LOG: int
SMART_WRITE_LOG: int
ENABLE_SMART: int
DISABLE_SMART: int
RETURN_SMART_STATUS: int
ENABLE_DISABLE_AUTO_OFFLINE: int
IOCTL_CHANGER_BASE: int
MAX_VOLUME_ID_SIZE: int
MAX_VOLUME_TEMPLATE_SIZE: int
VENDOR_ID_LENGTH: int
PRODUCT_ID_LENGTH: int
REVISION_LENGTH: int
SERIAL_NUMBER_LENGTH: int
CHANGER_BAR_CODE_SCANNER_INSTALLED: int
CHANGER_INIT_ELEM_STAT_WITH_RANGE: int
CHANGER_CLOSE_IEPORT: int
CHANGER_OPEN_IEPORT: int
CHANGER_STATUS_NON_VOLATILE: int
CHANGER_EXCHANGE_MEDIA: int
CHANGER_CLEANER_SLOT: int
CHANGER_LOCK_UNLOCK: int
CHANGER_CARTRIDGE_MAGAZINE: int
CHANGER_MEDIUM_FLIP: int
CHANGER_POSITION_TO_ELEMENT: int
CHANGER_REPORT_IEPORT_STATE: int
CHANGER_STORAGE_DRIVE: int
CHANGER_STORAGE_IEPORT: int
CHANGER_STORAGE_SLOT: int
CHANGER_STORAGE_TRANSPORT: int
CHANGER_DRIVE_CLEANING_REQUIRED: int
CHANGER_PREDISMOUNT_EJECT_REQUIRED: int
CHANGER_CLEANER_ACCESS_NOT_VALID: int
CHANGER_PREMOUNT_EJECT_REQUIRED: int
CHANGER_VOLUME_IDENTIFICATION: int
CHANGER_VOLUME_SEARCH: int
CHANGER_VOLUME_ASSERT: int
CHANGER_VOLUME_REPLACE: int
CHANGER_VOLUME_UNDEFINE: int
CHANGER_SERIAL_NUMBER_VALID: int
CHANGER_DEVICE_REINITIALIZE_CAPABLE: int
CHANGER_KEYPAD_ENABLE_DISABLE: int
CHANGER_DRIVE_EMPTY_ON_DOOR_ACCESS: int
CHANGER_RESERVED_BIT: int
CHANGER_PREDISMOUNT_ALIGN_TO_SLOT: int
CHANGER_PREDISMOUNT_ALIGN_TO_DRIVE: int
CHANGER_CLEANER_AUTODISMOUNT: int
CHANGER_TRUE_EXCHANGE_CAPABLE: int
CHANGER_SLOTS_USE_TRAYS: int
CHANGER_RTN_MEDIA_TO_ORIGINAL_ADDR: int
CHANGER_CLEANER_OPS_NOT_SUPPORTED: int
CHANGER_IEPORT_USER_CONTROL_OPEN: int
CHANGER_IEPORT_USER_CONTROL_CLOSE: int
CHANGER_MOVE_EXTENDS_IEPORT: int
CHANGER_MOVE_RETRACTS_IEPORT: int
CHANGER_TO_TRANSPORT: int
CHANGER_TO_SLOT: int
CHANGER_TO_IEPORT: int
CHANGER_TO_DRIVE: int
LOCK_UNLOCK_IEPORT: int
LOCK_UNLOCK_DOOR: int
LOCK_UNLOCK_KEYPAD: int
LOCK_ELEMENT: int
UNLOCK_ELEMENT: int
EXTEND_IEPORT: int
RETRACT_IEPORT: int
ELEMENT_STATUS_FULL: int
ELEMENT_STATUS_IMPEXP: int
ELEMENT_STATUS_EXCEPT: int
ELEMENT_STATUS_ACCESS: int
ELEMENT_STATUS_EXENAB: int
ELEMENT_STATUS_INENAB: int
ELEMENT_STATUS_PRODUCT_DATA: int
ELEMENT_STATUS_LUN_VALID: int
ELEMENT_STATUS_ID_VALID: int
ELEMENT_STATUS_NOT_BUS: int
ELEMENT_STATUS_INVERT: int
ELEMENT_STATUS_SVALID: int
ELEMENT_STATUS_PVOLTAG: int
ELEMENT_STATUS_AVOLTAG: int
ERROR_LABEL_UNREADABLE: int
ERROR_LABEL_QUESTIONABLE: int
ERROR_SLOT_NOT_PRESENT: int
ERROR_DRIVE_NOT_INSTALLED: int
ERROR_TRAY_MALFUNCTION: int
ERROR_INIT_STATUS_NEEDED: int
ERROR_UNHANDLED_ERROR: int
SEARCH_ALL: int
SEARCH_PRIMARY: int
SEARCH_ALTERNATE: int
SEARCH_ALL_NO_SEQ: int
SEARCH_PRI_NO_SEQ: int
SEARCH_ALT_NO_SEQ: int
ASSERT_PRIMARY: int
ASSERT_ALTERNATE: int
REPLACE_PRIMARY: int
REPLACE_ALTERNATE: int
UNDEFINE_PRIMARY: int
UNDEFINE_ALTERNATE: int
USN_PAGE_SIZE: int
USN_REASON_DATA_OVERWRITE: int
USN_REASON_DATA_EXTEND: int
USN_REASON_DATA_TRUNCATION: int
USN_REASON_NAMED_DATA_OVERWRITE: int
USN_REASON_NAMED_DATA_EXTEND: int
USN_REASON_NAMED_DATA_TRUNCATION: int
USN_REASON_FILE_CREATE: int
USN_REASON_FILE_DELETE: int
USN_REASON_EA_CHANGE: int
USN_REASON_SECURITY_CHANGE: int
USN_REASON_RENAME_OLD_NAME: int
USN_REASON_RENAME_NEW_NAME: int
USN_REASON_INDEXABLE_CHANGE: int
USN_REASON_BASIC_INFO_CHANGE: int
USN_REASON_HARD_LINK_CHANGE: int
USN_REASON_COMPRESSION_CHANGE: int
USN_REASON_ENCRYPTION_CHANGE: int
USN_REASON_OBJECT_ID_CHANGE: int
USN_REASON_REPARSE_POINT_CHANGE: int
USN_REASON_STREAM_CHANGE: int
USN_REASON_TRANSACTED_CHANGE: int
USN_REASON_CLOSE: int
USN_DELETE_FLAG_DELETE: int
USN_DELETE_FLAG_NOTIFY: int
USN_DELETE_VALID_FLAGS: int
USN_SOURCE_DATA_MANAGEMENT: int
USN_SOURCE_AUXILIARY_DATA: int
USN_SOURCE_REPLICATION_MANAGEMENT: int
MARK_HANDLE_PROTECT_CLUSTERS: int
MARK_HANDLE_TXF_SYSTEM_LOG: int
MARK_HANDLE_NOT_TXF_SYSTEM_LOG: int
VOLUME_IS_DIRTY: int
VOLUME_UPGRADE_SCHEDULED: int
VOLUME_SESSION_OPEN: int
FILE_PREFETCH_TYPE_FOR_CREATE: int
FILE_PREFETCH_TYPE_FOR_DIRENUM: int
FILE_PREFETCH_TYPE_FOR_CREATE_EX: int
FILE_PREFETCH_TYPE_FOR_DIRENUM_EX: int
FILE_PREFETCH_TYPE_MAX: int
FILESYSTEM_STATISTICS_TYPE_NTFS: int
FILESYSTEM_STATISTICS_TYPE_FAT: int
FILE_SET_ENCRYPTION: int
FILE_CLEAR_ENCRYPTION: int
STREAM_SET_ENCRYPTION: int
STREAM_CLEAR_ENCRYPTION: int
MAXIMUM_ENCRYPTION_VALUE: int
ENCRYPTION_FORMAT_DEFAULT: int
COMPRESSION_FORMAT_SPARSE: int
COPYFILE_SIS_LINK: int
COPYFILE_SIS_REPLACE: int
COPYFILE_SIS_FLAGS: int
WMI_DISK_GEOMETRY_GUID: _win32typing.PyIID
GUID_DEVINTERFACE_CDROM: _win32typing.PyIID
GUID_DEVINTERFACE_FLOPPY: _win32typing.PyIID
GUID_DEVINTERFACE_SERENUM_BUS_ENUMERATOR: _win32typing.PyIID
GUID_DEVINTERFACE_COMPORT: _win32typing.PyIID
GUID_DEVINTERFACE_DISK: _win32typing.PyIID
GUID_DEVINTERFACE_STORAGEPORT: _win32typing.PyIID
GUID_DEVINTERFACE_CDCHANGER: _win32typing.PyIID
GUID_DEVINTERFACE_PARTITION: _win32typing.PyIID
GUID_DEVINTERFACE_VOLUME: _win32typing.PyIID
GUID_DEVINTERFACE_WRITEONCEDISK: _win32typing.PyIID
GUID_DEVINTERFACE_TAPE: _win32typing.PyIID
GUID_DEVINTERFACE_MEDIUMCHANGER: _win32typing.PyIID
GUID_SERENUM_BUS_ENUMERATOR: int
GUID_CLASS_COMPORT: int
DiskClassGuid: int
CdRomClassGuid: int
PartitionClassGuid: int
TapeClassGuid: int
WriteOnceDiskClassGuid: int
VolumeClassGuid: int
MediumChangerClassGuid: int
FloppyClassGuid: int
CdChangerClassGuid: int
StoragePortClassGuid: int
IOCTL_STORAGE_CHECK_VERIFY: int
IOCTL_STORAGE_CHECK_VERIFY2: int
IOCTL_STORAGE_MEDIA_REMOVAL: int
IOCTL_STORAGE_EJECT_MEDIA: int
IOCTL_STORAGE_LOAD_MEDIA: int
IOCTL_STORAGE_LOAD_MEDIA2: int
IOCTL_STORAGE_RESERVE: int
IOCTL_STORAGE_RELEASE: int
IOCTL_STORAGE_FIND_NEW_DEVICES: int
IOCTL_STORAGE_EJECTION_CONTROL: int
IOCTL_STORAGE_MCN_CONTROL: int
IOCTL_STORAGE_GET_MEDIA_TYPES: int
IOCTL_STORAGE_GET_MEDIA_TYPES_EX: int
IOCTL_STORAGE_GET_MEDIA_SERIAL_NUMBER: int
IOCTL_STORAGE_GET_HOTPLUG_INFO: int
IOCTL_STORAGE_SET_HOTPLUG_INFO: int
IOCTL_STORAGE_RESET_BUS: int
IOCTL_STORAGE_RESET_DEVICE: int
IOCTL_STORAGE_BREAK_RESERVATION: int
IOCTL_STORAGE_GET_DEVICE_NUMBER: int
IOCTL_STORAGE_PREDICT_FAILURE: int
IOCTL_DISK_GET_DRIVE_GEOMETRY: int
IOCTL_DISK_GET_PARTITION_INFO: int
IOCTL_DISK_SET_PARTITION_INFO: int
IOCTL_DISK_GET_DRIVE_LAYOUT: int
IOCTL_DISK_SET_DRIVE_LAYOUT: int
IOCTL_DISK_VERIFY: int
IOCTL_DISK_FORMAT_TRACKS: int
IOCTL_DISK_REASSIGN_BLOCKS: int
IOCTL_DISK_PERFORMANCE: int
IOCTL_DISK_IS_WRITABLE: int
IOCTL_DISK_LOGGING: int
IOCTL_DISK_FORMAT_TRACKS_EX: int
IOCTL_DISK_HISTOGRAM_STRUCTURE: int
IOCTL_DISK_HISTOGRAM_DATA: int
IOCTL_DISK_HISTOGRAM_RESET: int
IOCTL_DISK_REQUEST_STRUCTURE: int
IOCTL_DISK_REQUEST_DATA: int
IOCTL_DISK_PERFORMANCE_OFF: int
IOCTL_DISK_CONTROLLER_NUMBER: int
SMART_GET_VERSION: int
SMART_SEND_DRIVE_COMMAND: int
SMART_RCV_DRIVE_DATA: int
IOCTL_DISK_GET_PARTITION_INFO_EX: int
IOCTL_DISK_SET_PARTITION_INFO_EX: int
IOCTL_DISK_GET_DRIVE_LAYOUT_EX: int
IOCTL_DISK_SET_DRIVE_LAYOUT_EX: int
IOCTL_DISK_CREATE_DISK: int
IOCTL_DISK_GET_LENGTH_INFO: int
IOCTL_DISK_GET_DRIVE_GEOMETRY_EX: int
IOCTL_DISK_REASSIGN_BLOCKS_EX: int
IOCTL_DISK_UPDATE_DRIVE_SIZE: int
IOCTL_DISK_GROW_PARTITION: int
IOCTL_DISK_GET_CACHE_INFORMATION: int
IOCTL_DISK_SET_CACHE_INFORMATION: int
OBSOLETE_IOCTL_STORAGE_RESET_BUS: int
OBSOLETE_IOCTL_STORAGE_RESET_DEVICE: int
OBSOLETE_DISK_GET_WRITE_CACHE_STATE: int
IOCTL_DISK_GET_WRITE_CACHE_STATE: int
IOCTL_DISK_DELETE_DRIVE_LAYOUT: int
IOCTL_DISK_UPDATE_PROPERTIES: int
IOCTL_DISK_FORMAT_DRIVE: int
IOCTL_DISK_SENSE_DEVICE: int
IOCTL_DISK_CHECK_VERIFY: int
IOCTL_DISK_MEDIA_REMOVAL: int
IOCTL_DISK_EJECT_MEDIA: int
IOCTL_DISK_LOAD_MEDIA: int
IOCTL_DISK_RESERVE: int
IOCTL_DISK_RELEASE: int
IOCTL_DISK_FIND_NEW_DEVICES: int
IOCTL_DISK_GET_MEDIA_TYPES: int
DISK_HISTOGRAM_SIZE: int
HISTOGRAM_BUCKET_SIZE: int
IOCTL_CHANGER_GET_PARAMETERS: int
IOCTL_CHANGER_GET_STATUS: int
IOCTL_CHANGER_GET_PRODUCT_DATA: int
IOCTL_CHANGER_SET_ACCESS: int
IOCTL_CHANGER_GET_ELEMENT_STATUS: int
IOCTL_CHANGER_INITIALIZE_ELEMENT_STATUS: int
IOCTL_CHANGER_SET_POSITION: int
IOCTL_CHANGER_EXCHANGE_MEDIUM: int
IOCTL_CHANGER_MOVE_MEDIUM: int
IOCTL_CHANGER_REINITIALIZE_TRANSPORT: int
IOCTL_CHANGER_QUERY_VOLUME_TAGS: int
IOCTL_SERIAL_LSRMST_INSERT: int
IOCTL_SERENUM_EXPOSE_HARDWARE: int
IOCTL_SERENUM_REMOVE_HARDWARE: int
IOCTL_SERENUM_PORT_DESC: int
IOCTL_SERENUM_GET_PORT_NAME: int
SERIAL_LSRMST_ESCAPE: int
SERIAL_LSRMST_LSR_DATA: int
SERIAL_LSRMST_LSR_NODATA: int
SERIAL_LSRMST_MST: int
SERIAL_IOC_FCR_FIFO_ENABLE: int
SERIAL_IOC_FCR_RCVR_RESET: int
SERIAL_IOC_FCR_XMIT_RESET: int
SERIAL_IOC_FCR_DMA_MODE: int
SERIAL_IOC_FCR_RES1: int
SERIAL_IOC_FCR_RES2: int
SERIAL_IOC_FCR_RCVR_TRIGGER_LSB: int
SERIAL_IOC_FCR_RCVR_TRIGGER_MSB: int
SERIAL_IOC_MCR_DTR: int
SERIAL_IOC_MCR_RTS: int
SERIAL_IOC_MCR_OUT1: int
SERIAL_IOC_MCR_OUT2: int
SERIAL_IOC_MCR_LOOP: int
FSCTL_REQUEST_OPLOCK_LEVEL_1: int
FSCTL_REQUEST_OPLOCK_LEVEL_2: int
FSCTL_REQUEST_BATCH_OPLOCK: int
FSCTL_OPLOCK_BREAK_ACKNOWLEDGE: int
FSCTL_OPBATCH_ACK_CLOSE_PENDING: int
FSCTL_OPLOCK_BREAK_NOTIFY: int
FSCTL_LOCK_VOLUME: int
FSCTL_UNLOCK_VOLUME: int
FSCTL_DISMOUNT_VOLUME: int
FSCTL_IS_VOLUME_MOUNTED: int
FSCTL_IS_PATHNAME_VALID: int
FSCTL_MARK_VOLUME_DIRTY: int
FSCTL_QUERY_RETRIEVAL_POINTERS: int
FSCTL_GET_COMPRESSION: int
FSCTL_SET_COMPRESSION: int
FSCTL_MARK_AS_SYSTEM_HIVE: int
FSCTL_OPLOCK_BREAK_ACK_NO_2: int
FSCTL_INVALIDATE_VOLUMES: int
FSCTL_QUERY_FAT_BPB: int
FSCTL_REQUEST_FILTER_OPLOCK: int
FSCTL_FILESYSTEM_GET_STATISTICS: int
FSCTL_GET_NTFS_VOLUME_DATA: int
FSCTL_GET_NTFS_FILE_RECORD: int
FSCTL_GET_VOLUME_BITMAP: int
FSCTL_GET_RETRIEVAL_POINTERS: int
FSCTL_MOVE_FILE: int
FSCTL_IS_VOLUME_DIRTY: int
FSCTL_ALLOW_EXTENDED_DASD_IO: int
FSCTL_FIND_FILES_BY_SID: int
FSCTL_SET_OBJECT_ID: int
FSCTL_GET_OBJECT_ID: int
FSCTL_DELETE_OBJECT_ID: int
FSCTL_SET_REPARSE_POINT: int
FSCTL_GET_REPARSE_POINT: int
FSCTL_DELETE_REPARSE_POINT: int
FSCTL_ENUM_USN_DATA: int
FSCTL_SECURITY_ID_CHECK: int
FSCTL_READ_USN_JOURNAL: int
FSCTL_SET_OBJECT_ID_EXTENDED: int
FSCTL_CREATE_OR_GET_OBJECT_ID: int
FSCTL_SET_SPARSE: int
FSCTL_SET_ZERO_DATA: int
FSCTL_QUERY_ALLOCATED_RANGES: int
FSCTL_SET_ENCRYPTION: int
FSCTL_ENCRYPTION_FSCTL_IO: int
FSCTL_WRITE_RAW_ENCRYPTED: int
FSCTL_READ_RAW_ENCRYPTED: int
FSCTL_CREATE_USN_JOURNAL: int
FSCTL_READ_FILE_USN_DATA: int
FSCTL_WRITE_USN_CLOSE_RECORD: int
FSCTL_EXTEND_VOLUME: int
FSCTL_QUERY_USN_JOURNAL: int
FSCTL_DELETE_USN_JOURNAL: int
FSCTL_MARK_HANDLE: int
FSCTL_SIS_COPYFILE: int
FSCTL_SIS_LINK_FILES: int
FSCTL_HSM_MSG: int
FSCTL_HSM_DATA: int
FSCTL_RECALL_FILE: int
FSCTL_READ_FROM_PLEX: int
FSCTL_FILE_PREFETCH: int
FSCTL_MAKE_MEDIA_COMPATIBLE: int
FSCTL_SET_DEFECT_MANAGEMENT: int
FSCTL_QUERY_SPARING_INFO: int
FSCTL_QUERY_ON_DISK_VOLUME_INFO: int
FSCTL_SET_VOLUME_COMPRESSION_STATE: int
FSCTL_TXFS_MODIFY_RM: int
FSCTL_TXFS_QUERY_RM_INFORMATION: int
FSCTL_TXFS_ROLLFORWARD_REDO: int
FSCTL_TXFS_ROLLFORWARD_UNDO: int
FSCTL_TXFS_START_RM: int
FSCTL_TXFS_SHUTDOWN_RM: int
FSCTL_TXFS_READ_BACKUP_INFORMATION: int
FSCTL_TXFS_WRITE_BACKUP_INFORMATION: int
FSCTL_TXFS_CREATE_SECONDARY_RM: int
FSCTL_TXFS_GET_METADATA_INFO: int
FSCTL_TXFS_GET_TRANSACTED_VERSION: int
FSCTL_TXFS_CREATE_MINIVERSION: int
FSCTL_TXFS_TRANSACTION_ACTIVE: int
FSCTL_SET_ZERO_ON_DEALLOCATION: int
FSCTL_SET_REPAIR: int
FSCTL_GET_REPAIR: int
FSCTL_WAIT_FOR_REPAIR: int
FSCTL_INITIATE_REPAIR: int
FSCTL_CSC_INTERNAL: int
FSCTL_SHRINK_VOLUME: int
FSCTL_SET_SHORT_NAME_BEHAVIOR: int
FSCTL_DFSR_SET_GHOST_HANDLE_STATE: int
FSCTL_QUERY_PAGEFILE_ENCRYPTION: int
IOCTL_VOLUME_BASE: int
IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS: int
IOCTL_VOLUME_ONLINE: int
IOCTL_VOLUME_OFFLINE: int
IOCTL_VOLUME_IS_CLUSTERED: int
IOCTL_VOLUME_GET_GPT_ATTRIBUTES: int
DDS_4mm: int
MiniQic: int
Travan: int
QIC: int
MP_8mm: int
AME_8mm: int
AIT1_8mm: int
DLT: int
NCTP: int
IBM_3480: int
IBM_3490E: int
IBM_Magstar_3590: int
IBM_Magstar_MP: int
STK_DATA_D3: int
SONY_DTF: int
DV_6mm: int
DMI: int
SONY_D2: int
CLEANER_CARTRIDGE: int
CD_ROM: int
CD_R: int
CD_RW: int
DVD_ROM: int
DVD_R: int
DVD_RW: int
MO_3_RW: int
MO_5_WO: int
MO_5_RW: int
MO_5_LIMDOW: int
PC_5_WO: int
PC_5_RW: int
PD_5_RW: int
ABL_5_WO: int
PINNACLE_APEX_5_RW: int
SONY_12_WO: int
PHILIPS_12_WO: int
HITACHI_12_WO: int
CYGNET_12_WO: int
KODAK_14_WO: int
MO_NFR_525: int
NIKON_12_RW: int
IOMEGA_ZIP: int
IOMEGA_JAZ: int
SYQUEST_EZ135: int
SYQUEST_EZFLYER: int
SYQUEST_SYJET: int
AVATAR_F2: int
MP2_8mm: int
DST_S: int
DST_M: int
DST_L: int
VXATape_1: int
VXATape_2: int
STK_9840: int
LTO_Ultrium: int
LTO_Accelis: int
DVD_RAM: int
AIT_8mm: int
ADR_1: int
ADR_2: int
STK_9940: int
BusTypeUnknown: int
BusTypeScsi: int
BusTypeAtapi: int
BusTypeAta: int
BusType1394: int
BusTypeSsa: int
BusTypeFibre: int
BusTypeUsb: int
BusTypeRAID: int
BusTypeiScsi: int
BusTypeSas: int
BusTypeSata: int
BusTypeMaxReserved: int
Unknown: int
F5_1Pt2_512: int
F3_1Pt44_512: int
F3_2Pt88_512: int
F3_20Pt8_512: int
F3_720_512: int
F5_360_512: int
F5_320_512: int
F5_320_1024: int
F5_180_512: int
F5_160_512: int
RemovableMedia: int
FixedMedia: int
F3_120M_512: int
F3_640_512: int
F5_640_512: int
F5_720_512: int
F3_1Pt2_512: int
F3_1Pt23_1024: int
F5_1Pt23_1024: int
F3_128Mb_512: int
F3_230Mb_512: int
F8_256_128: int
F3_200Mb_512: int
F3_240M_512: int
F3_32M_512: int
PARTITION_STYLE_MBR: int
PARTITION_STYLE_GPT: int
PARTITION_STYLE_RAW: int
DetectNone: int
DetectInt13: int
DetectExInt13: int
EqualPriority: int
KeepPrefetchedData: int
KeepReadData: int
DiskWriteCacheNormal: int
DiskWriteCacheForceDisable: int
DiskWriteCacheDisableNotSupported: int
RequestSize: int
RequestLocation: int
DeviceProblemNone: int
DeviceProblemHardware: int
DeviceProblemCHMError: int
DeviceProblemDoorOpen: int
DeviceProblemCalibrationError: int
DeviceProblemTargetFailure: int
DeviceProblemCHMMoveError: int
DeviceProblemCHMZeroError: int
DeviceProblemCartridgeInsertError: int
DeviceProblemPositionError: int
DeviceProblemSensorError: int
DeviceProblemCartridgeEjectError: int
DeviceProblemGripperError: int
DeviceProblemDriveError: int
FILE_READ_DATA: int
FILE_WRITE_DATA: int
FSCTL_TXFS_LIST_TRANSACTIONS: int
FSCTL_TXFS_LIST_TRANSACTION_LOCKED_FILES: int
