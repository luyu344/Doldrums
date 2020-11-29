import Constants

from enum import Enum

class ClassId(Enum):
	def isTypedDataBaseClass(cid):
		return ClassId.TYPED_DATA_INT8_ARRAY.value <= cid < ClassId.BYTE_DATA_VIEW.value

	def isTypedDataClass(cid):
		return ClassId.isTypedDataBaseClass(cid) and (cid - ClassId.TYPED_DATA_INT8_ARRAY.value) % 3 == Constants.kTypedDataCidRemainderInternal

	ILLEGAL = 0
	FREE_LIST_ELEMENT = 1
	FORWARDING_CORPSE = 2
	OBJECT = 3
	CLASS = 4
	PATCH_CLASS = 5
	FUNCTION = 6
	CLOSURE_DATA = 7
	SIGNATURE_DATA = 8
	REDIRECTION_DATA = 9
	FFI_TRAMPOLINE_DATA = 10
	FIELD = 11
	SCRIPT = 12
	LIBRARY = 13
	NAMESPACE = 14
	KERNEL_PROGRAM_INFO = 15
	CODE = 16
	BYTECODE = 17
	INSTRUCTIONS = 18
	INSTRUCTIONS_SECTION = 19
	OBJECT_POOL = 20
	PC_DESCRIPTORS = 21
	CODE_SOURCE_MAP = 22
	COMPRESSED_STACK_MAPS = 23
	LOCAL_VAR_DESCRIPTORS = 24
	EXCEPTION_HANDLERS = 25
	CONTEXT = 26
	CONTEXT_SCOPE = 27
	PARAMTER_TYPE_CHECK = 28
	SINGLE_TARGET_CACHE = 29
	UNLINKED_CALL = 30
	MONOMORPHIC_SMIABLE = 31
	CALL_SITE_DATA = 32
	IC_DATA = 33
	MEGAMORPHIC_CACHE = 34
	SUBTYPE_TEST_CACHE = 35
	LOADING_UNIT = 36
	ERROR = 37
	API_ERROR = 38
	LANGUAGE_ERROR = 39
	UNHANDLED_EXCEPTION = 40
	UNWIND_ERROR = 41
	INSTANCE = 42
	LIBRARY_PREFIX = 43
	TYPE_ARGUMENTS = 44
	ABSTRACT_TYPE = 45
	TYPE = 46
	TYPE_REF = 47
	TYPE_PARAMETER = 48
	CLOSURE = 49
	NUMBER = 50
	INTEGER = 51
	SMI = 52
	MINT = 53
	DOUBLE = 54
	BOOL = 55
	GROWABLE_OBJECT_ARRAY = 56
	FLOAT_32X4 = 57
	INT_32X4 = 58
	FLOAT_64X2 = 59
	TYPED_DATA_BASE = 60
	TYPED_DATA = 61
	EXTERNAL_TYPED_DATA = 62
	TYPED_DATA_VIEW = 63
	POINTER = 64
	DYNAMIC_LIBRARY = 65
	CAPABILITY = 66
	RECEIVE_PORT = 67
	SEND_PORT = 68
	STACK_TRACE = 69
	REGEX = 70
	WEAK_PROPERTY = 71
	MIRROR_REFERENCE = 72
	LINKED_HASHMAP = 73
	FUTURE_OR = 74
	USER_TAG = 75
	TRANSFERABLE_TYPED_DATA = 76
	WEAK_SERIALIZATION_REFERENCE = 77
	ARRAY = 78
	IMMUTABLE_ARRAY = 79
	STRING = 80
	ONE_BYTE_STRING = 81
	TWO_BYTE_STRING = 82
	EXTERNAL_ONE_BYTE_STRING = 83
	EXTERNAL_TWO_BYTE_STRING = 84
	FFI_POINTER = 85
	FFI_NATIVE_FUNCTION = 86
	FFI_INT8 = 87
	FFI_INT16 = 88
	FFI_INT32 = 89
	FFI_INT64 = 90
	FFI_UINT8 = 91
	FFI_UINT16 = 92
	FFI_UINT32 = 93
	FFI_UINT64 = 94
	FFI_INT_PTR = 95
	FFI_FLOAT = 96
	FFI_DOUBLE = 97
	FFI_VOID = 98
	FFI_HANDLE = 99
	FFI_NATIVE_TYPE = 100
	FFI_DYNAMIC_LIBRARY = 101
	FFI_STRUCT = 102
	WASM_INT32 = 103
	WASM_INT64 = 104
	WASM_FLOAT = 105
	WASM_DOUBLE = 106
	WASM_VOID = 107
	TYPED_DATA_INT8_ARRAY = 108
	TYPED_DATA_INT8_ARRAY_VIEW = 109
	EXTERNAL_TYPED_DATA_INT8_ARRAY = 110
	TYPED_DATA_UINT8_ARRAY = 111
	TYPED_DATA_UINT8_ARRAY_VIEW = 112
	EXTERNAL_TYPED_DATA_UINT8_ARRAY = 113
	TYPED_DATA_UINT8_CLAMPED_ARRAY = 114
	TYPED_DATA_UINT8_CLAMPED_ARRAY_VIEW = 115
	EXTERNAL_TYPED_DATA_UINT8_CLAMPED_ARRAY = 116
	TYPED_DATA_INT16_ARRAY = 117
	TYPED_DATA_INT16_ARRAY_VIEW = 118
	EXTERNAL_TYPED_DATA_INT16_ARRAY = 119
	TYPED_DATA_UINT16_ARRAY = 120
	TYPED_DATA_UINT16_ARRAY_VIEW = 121
	EXTERNAL_TYPED_DATA_UINT16_ARRAY = 122
	TYPED_DATA_INT32_ARRAY = 123
	TYPED_DATA_INT32_ARRAY_VIEW = 124
	EXTERNAL_TYPED_INT32_ARRAY = 125
	TYPED_DATA_UINT32_ARRAY = 126
	TYPED_DATA_UINT32_ARRAY_VIEW = 127
	EXTERNAL_TYPED_DATA_UINT32_ARRAY = 128
	TYPED_DATA_INT64_ARRAY = 129
	TYPED_DATA_INT64_ARRAY_VIEW = 130
	EXTERNAL_TYPED_DATA_INT64_ARRAY = 131
	TYPED_DATA_UINT64_ARRAY = 132
	TYPED_DATA_UINT64_ARRAY_VIEW = 133
	EXTERNAL_TYPED_DATA_UINT64_ARRAY = 134
	TYPED_DATA_FLOAT32_ARRAY = 135
	TYPED_DATA_FLOAT32_ARRAY_VIEW = 136
	EXTERNAL_TYPED_DATA_FLOAT32_ARRAY = 137
	TYPED_DATA_FLOAT64_ARRAY = 138
	TYPED_DATA_FLOAT64_ARRAY_VIEW = 139
	EXTERNAL_TYPED_DATA_FLOAT64_ARRAY = 140
	TYPED_DATA_FLOAT32X4_ARRAY = 141
	TYPED_DATA_FLOAT32X4_ARRAY_VIEW = 142
	EXTERNAL_TYPED_DATA_FLOAT32X4_ARRAY = 143
	TYPED_DATA_INT32X4_ARRAY = 144
	TYPED_DATA_INT32X4_ARRAY_VIEW = 145
	EXTERNAL_TYPED_DATA_INT32X4_ARRAY = 146
	TYPED_DATA_FLOAT64X2_ARRAY = 147
	TYPED_DATA_FLOAT64X2_ARRAY_VIEW = 148
	EXTERNAL_TYPED_DATA_FLOAT64X2_ARRAY = 149
	BYTE_DATA_VIEW = 150
	BYTE_BUFFER = 151
	NULL = 152
	DYNAMIC = 153
	VOID = 154
	NEVER = 155
	NUM_PREDEFINED = 156