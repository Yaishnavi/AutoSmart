NUMERICAL_TYPE = "num"
NUMERICAL_PREFIX = "n_"

CATEGORY_TYPE = "cat"
CATEGORY_PREFIX = "c_"

TIME_TYPE = "time"
TIME_PREFIX = "t_"

MULTI_CAT_TYPE = "multi-cat"
MULTI_CAT_PREFIX = "m_"
MULTI_CAT_DELIMITER = ","

BINARY_TYPE = "binary"
BINARY_PREFIX = 'b_'

MAIN_TABLE_NAME = "main"
MAIN_TABLE_TEST_NAME = "main_test"
TABLE_PREFIX = "table_"

LABEL = "label"

type2prefix = {
    NUMERICAL_TYPE:NUMERICAL_PREFIX,
    CATEGORY_TYPE:CATEGORY_PREFIX,
    TIME_TYPE:TIME_PREFIX,
    MULTI_CAT_TYPE:MULTI_CAT_PREFIX,
    BINARY_TYPE: BINARY_PREFIX
}

THREAD_NUM = 4

SEED = 2222
JOBS = 7

CAT_SHIFT = 1

MAX_SAMPLE_NUM = 1000000

TIME_MIN_BINS = 1000
SEGMENTS = 100

LESS_LIMIT = 10
SMOOTH_SHIFT = 100
DEVIATION_SHIFT = 100

KEYWORDS = ["label",'index']

SPLIT = -1

round_opt = False

SAMPLE_NUM = 210000

USE_ENSEMBLE = 1
