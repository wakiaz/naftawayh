﻿from arabic_const import *
JOKER="*"
INFIX_LETTERS=u"اتوي"
#النون هل هي من حروف الحشو
MAX_PREFIX=5;
MAX_SUFFIX=6;



#------------------------------
# PREFIXES_LIST
#------------------------------
PREFIXES_LIST=[
u'ءأ',
u'ا',
u'ات',
u'است',
u'ال',
u'الا',
u'الاست',
u'الان',
u'الأ',
u'الإ',
u'الت',
u'اللا',
u'الم',
u'المت',
u'المتم',
u'المست',
u'المن',
u'ان',
u'اي',
u'أ',
u'أال',
u'أأ',
u'أب',
u'أبال',
u'لبال',
u'أت',
u'أف',
u'أفأ',
u'أفا',
u'أفال',
u'أفب',
u'أفبال',
u'أفت',
u'أفن',
u'أل',
u'ألل',
u'أو',
u'أن',
u'أوا',
u'أوال',
u'أولل',
u'أي',
u'إ',
u'است',
u'ب',
u'باست',
u'بال',
u'بالا',
u'بالاست',
u'بالان',
u'بالأ',
u'بالإ',
u'بالت',
u'بالم',
u'بالمت',
u'بالمست',
u'بان',
u'بأ',
u'بإ',
u'بت',
u'بم',
u'بمست',
u'ت',
u'تال',
u'تت',
u'تست',
u'تن',
##u'س',
u'سأ',
u'ست',
u'سن',
u'سنت',
u'سي',
u'سيت',
u'ف',
u'فا',
u'فاست',
u'فال',
u'فالا',
u'فالاست',
u'فالأ',
u'فالت',
u'فالم',
u'فالمست',
u'فان',
u'فأ',
u'فإ',
u'فب',
u'فبال',
u'فبالم',
u'فت',
u'فتست',
u'فس',
u'فسأ',
u'فست',
u'فسن',
u'فسي',
u'فك',
u'فل',
u'فلأ',
u'فلل',
u'فللم',
u'فلن',
u'فلي',
u'فليست',
u'فم',
u'فن',
u'فنت',
u'فو',
u'فوال',
u'في',
u'فيت',
u'فيست',
u'فين',
u'ك',
u'كاست',
u'كال',
u'كالا',
u'كالاست',
u'كالان',
u'كالت',
u'كالم',
u'كالمت',
u'كالمست',
u'كم',
u'كمست',
u'ل',
u'لا',
u'لاست',
u'لال',
u'لان',
u'لأ',
u'لأست',
u'لإ',
u'لت',
u'لل',
u'للا',
u'للاست',
u'للان',
u'للإ',
u'للاست',
u'للت',
u'للم',
u'للمت',
u'للمست',
u'لم',
u'لمست',
u'لن',
u'لي',
u'ليت',
u'ليست',
u'م',
u'مت',
u'مست',
u'من',
u'ن',
u'نت',
u'نست',
u'و',
u'وا',
u'وات',
u'واست',
u'وال',
u'والا',
u'والاست',
u'والان',
u'والأ',
u'والإ',
u'والت',
u'والم',
u'والمت',
u'والمست',
u'والمن',
u'وان',
u'وأ',
u'وأست',
u'وإ',
u'وب',
u'وبال',
u'وبالأ',
u'وبالت',
u'وبالم',
u'وبالمت',
u'وبإ',
u'وبت',
u'وبم',
u'وت',
u'وتت',
u'وسأ',
u'وست',
u'وسن',
u'وسي',
u'وك',
u'وكال',
u'ول',
u'ولأ',
u'ولت',
u'ولتست',
u'ولل',
u'وللا',
u'وللاست',
u'وللت',
u'وللم',
u'وللمت',
u'ولم',
u'ولن',
u'ولي',
u'وليت',
u'وم',
u'ومت',
u'ومست',
u'ومن',
u'ون',
u'وي',
u'ويت',
u'ويست',
u'وين',
u'ي',
u'يا',
u'يال',
u'يالل',
u'يت',
u'يست',
u'ين',
]

#------------------------------
#SUFFIXES_LIST
#------------------------------
SUFFIXES_LIST=[
u'ا',
u'اءك',
u'اءكم',
u'كموه',
u'كموها',
u'اءكما',
u'اءكن',
u'اءنا',
u'اءه',
u'اءها',
u'اءهم',
u'اءهما',
u'اءهن',
u'اءي',
u'ائك',
u'ائكم',
u'ائكما',
u'ائكن',
u'ائنا',
u'ائه',
u'ائها',
u'ائهم',
u'ائهما',
u'ائهن',
u'ائي',
u'ات',
u'اتك',
u'اتكم',
u'اتكما',
u'اتكن',
u'اتنا',
u'اته',
u'اتها',
u'اتهم',
u'اتهما',
u'اتهن',
u'اتي',
u'اتيات',
u'اتيان',
u'اتية',
u'اتيه',
u'اتيون',
u'اتيين',
u'اك',
u'اكما',
u'اكن',
u'ان',
u'انا',
u'انات',
u'اناتك',
u'اناتكم',
u'اناتكما',
u'اناتكن',
u'اناتنا',
u'اناته',
u'اناتها',
u'اناتهم',
u'اناتهما',
u'اناتهن',
u'اناتي',
u'انة',
u'انك',
u'انكم',
u'انكما',
u'انكن',
u'اننا',
u'انني',
u'انه',
u'انها',
u'انهم',
u'انهما',
u'انهن',
u'اني',
u'انيات',
u'انيان',
u'انية',
u'انيتك',
u'انيتكم',
u'انيتكما',
u'انيتكن',
u'انيتنا',
u'انيته',
u'انيتها',
u'انيتهم',
u'انيتهما',
u'انيتهن',
u'انيتي',
u'انيون',
u'انيين',
u'اها',
u'اهما',
u'اهن',
u'اوات',
u'اوي',
u'اوية',
u'اي',
u'ت',
u'ة',
u'تاك',
u'تاكم',
u'تاكما',
u'تاكن',
u'تان',
u'تانا',
u'تاني',
u'تاه',
u'تاها',
u'تاهم',
u'تاهما',
u'تاهن',
u'تاي',
u'تك',
u'تكم',
u'تكما',
u'تكن',
u'تم',
u'تما',
u'تمانا',
u'تماني',
u'تماه',
u'تماها',
u'تماهم',
u'تماهما',
u'تماهن',
u'تمونا',
u'تموني',
u'تموه',
u'تموها',
u'تموهم',
u'تموهما',
u'تموهن',
u'تن',
u'تنا',
u'تني',
u'ته',
u'تها',
u'تهم',
u'تهم',
u'تهما',
u'تهن',
u'تيَّ',
u'تي',
u'تيك',
u'تيكم',
u'تيكما',
u'تيكن',
u'تين',
u'تينا',
u'تيه',
u'تيها',
u'تيهم',
u'تيهما',
u'تيهن',
u'ك',
u'ك',
u'كم',
u'كم',
u'كما',
u'كن',
u'ن',
u'نا',
u'ناك',
u'ناكم',
u'ناكما',
u'ناكموه',
u'ناكن',
u'ناه',
u'ناها',
u'ناهم',
u'ناهما',
u'ناهن',
u'نك',
u'نكم',
u'نكما',
u'نكن',
u'ننا',
u'نني',
u'نه',
u'نها',
u'نهم',
u'نهما',
u'نهن',
u'ني',
u'نيها',
u'ه',
u'ه',
u'ها',
u'هم',
u'هما',
u'هن',
u'وا',
u'وات',
u'وانية',
u'وك',
u'وكم',
u'وكما',
u'وكن',
u'ون',
u'ونا',
u'ونك',
u'ونكم',
u'ونكما',
u'ونكن',
u'وننا',
u'ونني',
u'ونه',
u'ونها',
u'ونهم',
u'ونهما',
u'ونهن',
u'وني',
u'وه',
u'وها',
u'وهم',
u'وهما',
u'وهن',
u'ي',
u'يات',
u'ياتك',
u'ياتكم',
u'ياتكما',
u'ياتكن',
u'ياتنا',
u'ياته',
u'ياتها',
u'ياتهم',
u'ياتهن',
u'ياتهها',
u'ياتي',
u'يان',
u'ية',
u'يتان',
u'يتك',
u'يتكم',
u'يتكما',
u'يتكن',
u'يتنا',
u'يته',
u'يتها',
u'يتهم',
u'يتهما',
u'يتهن',
u'يتي',
u'يتيا',
u'يتيان',
u'يتين',
u'يك',
u'يكم',
u'يكم',
u'يكما',
u'يكن',
u'ين',
u'ينا',
u'يننا',
u'ينني',
u'ينه',
u'ينها',
u'ينهم',
u'ينهما',
u'ينهن',
u'يني',
u'يه',
u'يها',
u'يهم',
u'يهم',
u'يهما',
u'يهن',
u'يون',
u'يي',
u'يين',
]

#-------------------
#
#-------------------
VERBAL_PREFIX_LIST=([
u'ءأ',
u'ا',
#u'ات',
#u'است',
#u'ان',
#u'اي',
u'أ',
u'أأ',
u'أت',
u'أف',
u'أفأ',
u'أفا',
u'أفت',
u'أفن',
u'أل',
u'أو',
u'أن',
u'أوا',
u'أي',
u'إ',
#u'است',
u'ت',
#u'تت',
#u'تست',
#u'تن',
##u'س',
u'سأ',
u'ست',
u'سن',
#u'سنت',
u'سي',
#u'سيت',
u'ف',
u'فا',
#u'فاست',
#u'فان',
u'فأ',
#u'فإ',
u'فت',
#u'فتست',
u'فس',
u'فسأ',
u'فست',
u'فسن',
u'فسي',
u'فل',
u'فلأ',
u'فلن',
u'فلي',
#u'فليست',
u'فن',
#u'فنت',
u'فو',
u'في',
#u'فيت',
#u'فيست',
#u'فين',
u'ل',
u'لا',
#u'لاست',
#u'لان',
u'لأ',
#u'لأست',
u'لإ',
u'لت',
u'لن',
u'لي',
#u'ليت',
#u'ليست',
u'ن',
#u'نت',
#u'نست',
u'و',
u'وا',
#u'وات',
#u'واست',
#u'وان',
u'وأ',
#u'وأست',
u'وإ',
u'وت',
#u'وتت',
u'وسأ',
u'وست',
u'وسن',
u'وسي',
u'ول',
u'ولأ',
u'ولت',
#u'ولتست',
u'ولن',
u'ولي',
#u'وليت',
u'ون',
u'وي',
#u'ويت',
#u'ويست',
#u'وين',
u'ي',
#u'يا',
#u'يت',
#u'يست',
#u'ين',
]);
VERBAL_SUFFIX_LIST=set(["",
    YEH,
    NOON+YEH,
    NOON+ALEF,
    KAF,
    KAF+MEEM+ALEF,
    KAF+MEEM,
    KAF+NOON,
    HEH,
    HEH+ALEF,
    HEH+MEEM+ALEF,
    HEH+MEEM,
    HEH+NOON,
#CONJ_SUFFIX_LIST=("",
TEH,
TEH+ALEF,
TEH+MEEM,
TEH+MEEM+WAW,
TEH+MEEM+ALEF,
TEH+NOON,
ALEF,
NOON,
NOON+ALEF,
ALEF+NOON,
WAW+ALEF,
WAW+NOON,
WAW,
YEH,
YEH+NOON,
# to be cleaned
# conjugation with pronouns
u'انة',
u'انك',
u'انكم',
u'انكما',
u'انكن',
u'اننا',
u'انني',
u'انه',
u'انها',
u'انهم',
u'انهما',
u'انهن',
u'اني',
u'تاك',
u'تاكم',
u'تاكما',
u'تاكن',
u'تان',
u'تانا',
u'تاني',
u'تاه',
u'تاها',
u'تاهم',
u'تاهما',
u'تاهن',
u'تاي',
u'تك',
u'تكم',
u'تكما',
u'تكن',
u'تم',
u'تما',
u'تمانا',
u'تماني',
u'تماه',
u'تماها',
u'تماهم',
u'تماهما',
u'تماهن',
u'تمونا',
u'تموني',
u'تموه',
u'تموها',
u'تموهم',
u'تموهما',
u'تموهن',
u'تن',
u'تنا',
u'تني',
u'ته',
u'تها',
u'تهم',
u'تهم',
u'تهما',
u'تهن',
u'ك',
u'ك',
u'كم',
u'كم',
u'كما',
u'كن',
u'كك',
u'ككما',
u'ككم',
u'ككن',
u'كه',
u'كها',
u'كهما',
u'كهم',
u'كهن',
u'ن',
u'نا',
u'ناك',
u'ناكم',
u'ناكما',
u'ناكموه',
u'ناكن',
u'ناه',
u'ناها',
u'ناهم',
u'ناهما',
u'ناهن',
u'نك',
u'نكم',
u'نكما',
u'نكن',
u'ننا',
u'نني',
u'نه',
u'نها',
u'نهم',
u'نهما',
u'نهن',
u'ني',
u'نيها',
u'ه',
u'ه',
u'ها',
u'هم',
u'هما',
u'هن',
u'وا',
u'وات',
u'وانية',
u'وك',
u'وكم',
u'وكما',
u'وكن',
u'ون',
u'ونا',
u'ونك',
u'ونكم',
u'ونكما',
u'ونكن',
u'وننا',
u'ونني',
u'ونه',
u'ونها',
u'ونهم',
u'ونهما',
u'ونهن',
u'وني',
u'وه',
u'وها',
u'وهم',
u'وهما',
u'وهن',

# To double MAf3ool suffix
    u'يي',
    u'يني',
    u'ينا',
    u'يك',
    u'يكما',
    u'يكم',
    u'يكن',
    u'يه',
    u'يها',
    u'يهما',
    u'يهم',
    u'يهن',
    u'نيي',
    u'نيني',
    u'نينا',
    u'نيك',
    u'نيكما',
    u'نيكم',
    u'نيكن',
    u'نيه',
    u'نيها',
    u'نيهما',
    u'نيهم',
    u'نيهن',
    u'ناي',
    u'ناني',
    u'نانا',
    u'ناك',
    u'ناكما',
    u'ناكم',
    u'ناكن',
    u'ناه',
    u'ناها',
    u'ناهما',
    u'ناهم',
    u'ناهن',
    u'كي',
    u'كني',
    u'كنا',
    u'كك',
    u'ككما',
    u'ككم',
    u'ككن',
    u'كه',
    u'كها',
    u'كهما',
    u'كهم',
    u'كهن',
    u'كماي',
    u'كماني',
    u'كمانا',
    u'كماك',
    u'كماكما',
    u'كماكم',
    u'كماكن',
    u'كماه',
    u'كماها',
    u'كماهما',
    u'كماهم',
    u'كماهن',
    u'كموي',
    u'كموني',
    u'كمونا',
    u'كموك',
    u'كموكما',
    u'كموكم',
    u'كموكن',
    u'كموه',
    u'كموها',
    u'كموهما',
    u'كموهم',
    u'كموهن',
    u'كني',
    u'كنني',
    u'كننا',
    u'كنك',
    u'كنكما',
    u'كنكم',
    u'كنكن',
    u'كنه',
    u'كنها',
    u'كنهما',
    u'كنهم',
    u'كنهن',
    u'هي',
    u'هني',
    u'هنا',
    u'هك',
    u'هكما',
    u'هكم',
    u'هكن',
    u'هه',
    u'هها',
    u'ههما',
    u'ههم',
    u'ههن',
    u'هاي',
    u'هاني',
    u'هانا',
    u'هاك',
    u'هاكما',
    u'هاكم',
    u'هاكن',
    u'هاه',
    u'هاها',
    u'هاهما',
    u'هاهم',
    u'هاهن',
    u'هماي',
    u'هماني',
    u'همانا',
    u'هماك',
    u'هماكما',
    u'هماكم',
    u'هماكن',
    u'هماه',
    u'هماها',
    u'هماهما',
    u'هماهم',
    u'هماهن',
    u'هموي',
    u'هموني',
    u'همونا',
    u'هموك',
    u'هموكما',
    u'هموكم',
    u'هموكن',
    u'هموه',
    u'هموها',
    u'هموهما',
    u'هموهم',
    u'هموهن',
    u'هني',
    u'هنني',
    u'هننا',
    u'هنك',
    u'هنكما',
    u'هنكم',
    u'هنكن',
    u'هنه',
    u'هنها',
    u'هنهما',
    u'هنهم',
    u'هنهن',
    ]);

#------------------------------
# PREFIXES_LIST
#------------------------------
NOMINAL_GRAMMATICAL_PREFIXES_LIST=[
u'',
u'ب',
u'ك',
u'ل',
u'و',
u'ف',
u'وب',
u'فب',
u'وك',
u'فك',
u'ول',
u'فل',
u'أ',
u'أب',
u'أك',
u'أل',
u'أو',
u'أف',
u'أوب',
u'أفب',
u'أوك',
u'أفك',
u'أول',
u'أفل',
u'ال',
u'بال',
u'كال',
u'لل',
u'وال',
u'فال',
u'وبال',
u'فبال',
u'وكال',
u'فكال',
u'ولل',
u'فلل',
u'أال',
u'أبال',
u'أكال',
u'ألل',
u'أوال',
u'أفال',
u'أوبال',
u'أفبال',
u'أوكال',
u'أفكال',
u'أولل',
u'أفلل',

]
NOMINAL_PREFIXES_LIST=[
u'ءأ',
u'ا',
u'ات',
u'است',
u'ال',
u'الا',
u'الاست',
u'الان',
#u'الأ',
u'الإ',
u'الت',
u'اللا',
u'الم',
u'المت',
u'المتم',
u'المست',
u'المن',
u'ان',
u'أ',
u'أال',
u'أأ',
u'أب',
u'أبال',
u'لبال',
u'أت',
u'أف',
u'أفأ',
u'أفا',
u'أفال',
u'أفب',
u'أفبال',
u'أفت',
u'أل',
u'ألل',
u'أو',
u'أوا',
u'أوال',
u'أولل',
u'إ',
u'است',
u'ب',
u'باست',
u'بال',
u'بالا',
u'بالاست',
u'بالان',
u'بالأ',
u'بالإ',
u'بالت',
u'بالم',
u'بالمت',
u'بالمست',
u'بان',
u'بأ',
u'بإ',
u'بت',
u'بم',
u'بمست',
u'ت',
u'تال',
u'ف',
u'فا',
u'فاست',
u'فال',
u'فالا',
u'فالاست',
u'فالأ',
u'فالت',
u'فالم',
u'فالمست',
u'فان',
u'فأ',
u'فإ',
u'فب',
u'فبال',
u'فبالم',
u'فت',
u'فك',
u'فل',
u'فلأ',
u'فلل',
u'فللم',
u'فم',
u'فو',
u'فوال',
u'ك',
u'كاست',
u'كال',
u'كالا',
u'كالاست',
u'كالان',
u'كالت',
u'كالم',
u'كالمت',
u'كالمست',
u'كم',
u'كمست',
u'ل',
u'لا',
u'لاست',
u'لال',
u'لان',
u'لأ',
u'لإ',
u'لت',
u'لل',
u'للا',
u'للاست',
u'للان',
u'للإ',
u'للاست',
u'للت',
u'للم',
u'للمت',
u'للمست',
u'لم',
u'لمست',
u'م',
u'مت',
u'مست',
u'من',
u'و',
# u'وا',
# u'وات',
# u'واست',
u'وال',
# u'والا',
# u'والاست',
# u'والان',
# u'والأ',
# u'والإ',
# u'والت',
# u'والم',
# u'والمت',
# u'والمست',
# u'والمن',
# u'وان',
# u'وأ',
# u'وإ',
u'وب',
u'وبال',
# u'وبالأ',
# u'وبالت',
# u'وبالم',
# u'وبالمت',
# u'وبإ',
# u'وبت',
# u'وبم',
# u'وت',
u'وك',
u'وكال',
u'ول',
# u'ولأ',
# u'ولت',
u'ولل',
# u'وللا',
# u'وللاست',
# u'وللت',
# u'وللم',
# u'وللمت',
# u'ولم',
# u'وم',
# u'ومت',
# u'ومست',
# u'ومن',
]
