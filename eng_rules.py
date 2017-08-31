# Encoding of rules from http://www.dtic.mil/get-tr-doc/pdf?AD=ADA021929
# Automatic Translation of English Text to Phonetics by Means of Letter-to-Sound Rules
# H. Elovitz, R. Johnson. A. McHugh, J. Shore
punct_rules = """
[ ]'=/ /;
[ - ]=/ /;
[ ]=/< >/;
[-]/<->;
. [' S]=/Z/;
#:.E [' S']=/Z/;
# [' S]=/Z/;
[' ]=/ /;
[,]=/<,>/;
[.]=/<.>;
[?]=/<?>/;
"""

a_rules = """
[A] =/AX/;
 [ARE] =/AA R/;
 [AR]O=/AX R/;
[AR]#=/EH R/;
 ^[AS]#=/EY S/;
[A]WA=/AX/;
[AW]=/AO/;
 :[ANY]=/EH N IY/;
[A]^+#=/EY/;
#:[ALLY]=/AX L IY/;
 [AL]#=/AX L/;
[AGAIN]=/AX G EH N/;
#:[AG]E=/IH JH/;
[A]^+:#=/AE/;
 :[A]^+ =/EY/;
[A]^:=/EY/;
 [ARR]=/AX R/;
[ARR]=/AE R/;
 :[AR] =/AA R/
[AR] =/ER/;
[AR]=/AA R/;
[AIR]=/EH R/;
[AI]=/EY/;
[AY]=/EY/;
[AU]=/AO/;
#:[AL] =/AX L/;
#:[ALS] =/AX L Z/;
[ALK]=/AO K/;
[AL]^=/AO L/;
 :[ABLE]=/EY B AX L/;
[ABLE]=/AX B AX L/;
[ANG]+=/EY N JH/;
[A]=/AE/;
"""

b_rules = """
 [BE]^#=/B IH/;
[BEING]=/B IY IH NX/;
 [BOTH] =/B OW TH/;
 [BUS]#=/B IH Z/;
[BUIL]=/B IH L/;
[B]=/B/;
"""

c_rules = """
 [CH]^=/K/;
^E[CH]=/K/;
[CH]=/CH/;
 S[CI]#=/S AY/;
[CI]A=/SH/;
[CI]O=/SH/;
[CI]EN=/SH/;
[C]+=/S/;
[CK]=/K/;
[COM]%=/K AH M/;
[C]=/K/;
"""

d_rules = """
#:[DED] =/D IH D/;
.E[D] =/D/;
#^:E[D] =/T/;
 [DE]^#=/D IH/;
 [DO] =/D UW/;
 [DOES]=/D AH Z/;
 [DOING]=/D UW IH NX/;
 [DOW]=/D AM/;
[DU]A=/JH UW/;
[D]=/D/;
"""

e_rules = """
#:[E] =/ /;
' ^:[E] =/ /;
 :[E] =/IY/;
#[ED] =/D/;
#:[E]D =/ /;
[EV]ER=/EH V/;
[E]^%=/IY/;
[ERI]#=/IY R IY/;
[ERI]=/EH R IH/;
#:[ER]#=/ER/;
[ER]#=/EH R/;
[ER]=/ER/;
 [EVEN]=/IY V EH N/;
#:[E]W=/ /;
@[EW]=/UW/;
[EW]=/Y UW/;
[E]O=/IY/;
#:&[ES] =/IH Z/;
#:[E]S =/ /;
#:[ELY] =/L IY/;
#:[EMENT]=/M EH N T/;
[EFUL]=/F UH L/;
[EE]=/IY/;
[EARN]=/ER N/;
 [EAR]^=/ER/;
[EAD]=/EH D/;
#:[EA] =/IY AX/;
[EA]SU=/EH/;
[EA]=/IY/;
[EIGH]=/EY/;
[EI]=/IY/;
 [EYE]=/AY/;
[EY]=/IY/;
[EU]=/Y UW/;
[E]=/EH/;
"""

f_rules = """
[FUL]=/F UH L/;
[F]=/F/;
"""

g_rules = """
[GIV]=/G IH V/;
 [G]I^=/G/;
[GE]T=/G EH/;
SU[GGES]=/G JH EH S/;
[GG]=/G/;
 B#[G]=/G/;
[G]+=/JH/;
[GREAT]=/G R EY T/;
#[GH]=/ /;
[G]=/G/;
"""

h_rules = """
 [HAV]=/HH AE V/;
 [HERE]=/HH IY R/;
 [HOUR]=/AW ER/;
[HOW]=/HH AW/;
[H]#=/HH/;
[H]=/ /;
"""

i_rules = """
 [IN]=/IH N/;
 [I] =/AY/;
[IN]D=/AY N/;
[IER]=/IY ER/;
#:R[IED] =/IY D/;
[IED] =/AY D/;
[IEN]=/IY EH N/;
[IE]T=/AY EH/;
 :[I]%=/AY/;
[I]%=/IY/;
[IE]=/IY/;
[I]^+:#=/IH/;
[IR]#=/AY R/;
[IZ]%=/AY Z/;
[IS]%=/AY Z/;
[I]D%=/AY/;
+^[I]^+=/IH/;
[I]T%=/AY/;
#^:[I]^+=/IH/;
[I]^+=/AY/;
[IR]=/ER/;
[IGH]=/AY/;
[ILD]=/AY L D/;
[IGN] =/AY N/;
[IGN]^=/AY N/;
[IGN]%=/AY N/;
[IQUE]=/IY K/;
[I]=/IH/;
"""

j_rules = """
[J]=/JH/;
"""

k_rules = """
 [K]N=/ /;
[K]=/K/;
"""

l_rules = """
[LO]C#=/L OW/;
L[L]=/ /;
#^:[L]%=/AX L/;
[LEAD]=/L IY D/;
[L]=/L/;
"""

m_rules = """
[MOV]=/M UW V/;
[M]=/M/;
"""

n_rules = """
E[NG]+=/N JH/;
[NG]R=/NX G/;
[NG]#=/NX G/;
[NGL]%=/NX G AX L/;
[NG]=/NX/;
[NK]=/NX K/;
 [NOW] =/N AW/;
[N]=/N/;
"""

o_rules = """
[OF] =/AX V/;
[OROUGH]=/ER OW/;
#:[OR] =/ER/;
#:[ORS] =/ER Z/;
[OR]=/AO R/;
 [ONE]=/W AH N/;
[OW]=/OW/;
 [OVER]=/OW V ER/;
[OV]=/AH V/;
[O]^%=/OW/;
[O]^EN=/OW/;
[O]^I#=/OW/;
[OL]D=/OW L/;
[OUGHT]=/AO T/;
[OUGH]=/AH F/;
 [OU]=/AW/;
H[OU]S#=/AW/;
[OUS]=/AX S/;
[OUR]=/AO R/;
[OULD]=/UH D/;
^[OU]^L=/AH/;
[OUP]=/UW P/;
[OU]=/AW/;
[OY]=/OY/;
[OING]=/OW IH NX/;
[OI]=/OY/;
[OOR]=/AO R/;
[OOK]=/UH K/;
[OOD]=/UH D/;
[OO]=/UW/;
[O]E=/OW/;
[O] =/IW/;
[OA]=/OW/;
 [ONLY]=/OW N L IY/;
 [ONCE]=/W AH N S/;
[ON ' T]=/OW N T/;
C[O]N=/AA/;
[O]NG=/AO/;
 ^:[O]N=/AH/;
I[ON]=/AX N/;
#:[ON] =/AX N/;
#^[ON]=/AX N/;
[O]ST =/OW/;
[OF]^=/AO F/;
[OTHER]=/AH DH ER/;
[OSS] =/AO S/;
#^:[OM]=/AH M/;
[O]=/AA/;
"""

p_rules = """
[PH]=/F/;
[PEOP]=/P IY P/;
[POW]=/P AW/;
[PUT] =/P UH T/;
[P]=/P/;
"""

q_rules = """
[QUAR]=/K W AO R/;
[QU]=/K W/;
[Q]=/K/;
"""

r_rules = """
 [RE]^#=/R IY/;
[R]=/R/;
"""

s_rules = """
[SH]=/SH/;
#[SION]=/ZH AX N/;
[SOME]=/S AH M/;
#[SUR]#=/ZH ER/;
[SUR]#=/SH ER/;
#[SU]#=/ZH UW/;
#[SSU]#=/SH UW/;
#[SED] =/Z D/;
#[S]#=/Z/;
[SAID]=/S EH D/;
^[SION]=/SH AX N/;
[S]S=/ /;
.[S] =/Z/;
#:.E[S] =/Z/;
#^:##[S] =/Z/;
#^:#[S] =/S/;
U[S] =/S/;
 :#[S] =/Z/;
 [SCH]=/S K/;
[S]C+=/ /;
#[SM]=/Z M/;
#[SN] '=/Z AX N/;
[S]=/S/;
"""

t_rules = """
 [THE] =/DH AX/;
[TO] =/T UW/;
[THAT] =/DH AE T/;
 [THIS] =/DH IH S/;
 [THEY]=/DH EY/;
 [THERE]=/DH EH R/;
[THER]=/DH ER/;
[THEIR]=/DH EH R/;
 [THAN] =/DH AE N/;
 [THEM] =/DH EH M/;
[THESE] =/DH IY Z/;
 [THEN]=/DH EH N/;
[THROUGH]=/TH R UW/;
[THOSE]=/DH OW Z/;
[THOUGH] =/DH OW/;
 [THUS]=/DH AH S/;
[TH]=/TH/;
#:[TED] =/T IH D/;
S[TI]#N=/CH/;
[TI]O=/SH/;
[TI]A=/SH/;
[TIEN]=/SH AX N/;
[TUR]#=/CH ER/;
[TU]A=/CH UW/;
 [TWO]=/T UW/;
[T]=/T/;
"""

u_rules = """
 [UN]I=/Y UW N/;
 [UN]=/AH N/;
 [UPON]=/AX P AO N/;
@[UR]#=/UH R/;
[UR]#=/Y UH R/;
[UR]=/ER/;
[U]^ =/AH/;
[U]^^=/AH/;
[UY]=/AY/;
 G[U]#=/ /;
G[U]%=/ /;
G[U]#=/W/;
#N[U]=/Y UW/;
@[U]=/UW/;
[U]=/Y UW/;
"""

v_rules = """
[VIEW]=/V Y UW/;
[V]=/V/;
"""

w_rules = """
 [WERE]=/W ER/;
[WA]S=/W AA/;
[WA]T=/W AA/;
[WHERE]=/WH EH R/;
[WHAT]=/WH AA T/;
[WHOL]=/HH UW L/;
[WHO]=/HH UW/;
[WH]=/WH/;
[WAR]=/W AO R/;
[WOR]^=/W ER/;
[WR]=/R/;
[W]=/W/;
"""

x_rules = """
[X]=/K S/;
"""

y_rules = """
[YOUNG]=/Y AH NX/;
 [YOU]=/Y UW/;
 [YES]=/Y EH S/;
 [Y]=/Y/;
#^:[Y] =/IY/;
#^:[Y]I=/IY/;
 :[Y] =/AY/;
 :[Y]#=/AY/;
 :[Y]^+:#=/IH/;
 :[Y]^#=/AY/;
[Y]=/IH/;
"""

z_rules = """
[Z]=/Z/;
"""

num_rules = """
[0]=/Z IH R OW/;
[1]=/W AH N/;
[2]=/T UW/;
[3]=/TH R IY/;
[4]=/F OW R/;
[5]=/F AY V/;
[6]=/S IH K S/;
[7]=/S EH V AX N/;
[8]=/EY T/;
[9]=/N AY N/;
"""

all_rules = punct_rules
all_rules += a_rules
all_rules += b_rules
all_rules += c_rules
all_rules += d_rules
all_rules += e_rules
all_rules += f_rules
all_rules += g_rules
all_rules += h_rules
all_rules += i_rules
all_rules += j_rules
all_rules += k_rules
all_rules += l_rules
all_rules += m_rules
all_rules += n_rules
all_rules += o_rules
all_rules += p_rules
all_rules += q_rules
all_rules += r_rules
all_rules += s_rules
all_rules += t_rules
all_rules += u_rules
all_rules += v_rules
all_rules += w_rules
all_rules += x_rules
all_rules += y_rules
all_rules += z_rules
all_rules += num_rules

vowels = "A E I O U Y"
consonants = "B C D F G H J K L M N P Q R S T V W X Z"
voiced_consonants = "B D V G J L M N R W Z"
suffixes = "ER E ES ED ING ELY"
sibilants = "S C G Z X J CH SH"
long_u_consonants = "T S R D L Z N J TH CH SH"
front_vowels = "E I Y"

# symbol meanings
# # = 1 or more vowels
# * = 1 or more consonants
# , = a voiced consonant
# $ = single consonant followed by I or E
# % = suffix
# & = a sibilant
# @ = a consonant after which a long U is pronounced, as in RULE not MULE
# ^ = a single consonant
# + = a front vowel
# : = 0 or more consonants
special = "# * , $ % & @ ^ + :"

sep_rules = [ar.strip() for ar in all_rules.split(";") if ar.strip() != ""]

def parse_and_build_rule_function(rule):
    lhs, rhs = rule.split("=")
    target = rhs.replace("/", "")
    prefix = lhs.split("[")[0]
    center = lhs.split("[")[1].split("]")[0]
    postfix = lhs.split("]")[-1]
    from IPython import embed; embed(); raise ValueError()

[parse_and_build_rule_function(sr) for sr in sep_rules]
