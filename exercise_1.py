MEMBER_1 = "Peiyan"
MEMBER_2 = "Jing"
MEMBER_3 = "Wan-Ting"
MEMBER_4="Michelle"

MEMBER_1_HOME = "China"
MEMBER_2_HOME = "Beijing, China"
MEMBER_3_HOME = "Taipei, Taiwan"
MEMBER_4_HOME = "Taipei, Taiwan"

MEMBERS = {
    MEMBER_1:MEMBER_1_HOME,
    MEMBER_2:MEMBER_2_HOME,
    MEMBER_3:MEMBER_3_HOME,
    MEMBER_4:MEMBER_4_HOME,
}

for k,v in MEMBERS.items():
    print(f"{k} is from {v}")
