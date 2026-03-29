from .sms_region_helper import *

GELATO_BEACH_ENTRANCE: SmsRegion = SmsRegion(SmsRegionName.GELATO_ENTRANCE,
    requirements=[Requirements(SPRAY_OR_HOVER, shines=5), Requirements(skip_forward=True)],
    ticketed="Gelato Beach Ticket", parent_region=SmsRegionName.PLAZA)

GELATO_BEACH_ONE: SmsRegion = SmsRegion(SmsRegionName.GELATO_ONE,
    shines=[Shine("Dune Bud Sand Castle Secret", [Requirements(SPRAY_OR_HOVER)], in_game_bit=20),
        Shine("Red Coins in the Sand Castle", [Requirements([[NozzleType.hover]])],in_game_bit=28),
        Shine("Sandy Shine Sprite", [Requirements(SPRAY_OR_HOVER)], in_game_bit=29)],
    blue_coins=[BlueCoin("Red Cataquack", [Requirements(SPRAY_OR_HOVER)], in_game_bit=270),
        BlueCoin("Juicer", in_game_bit=275),
        BlueCoin("Rocket M", [Requirements(SPRAY_OR_HOVER)], in_game_bit=276),
        BlueCoin("Spawn Triangle", [Requirements([[NozzleType.spray]])], in_game_bit=277),
        BlueCoin("Trees Triangle", [Requirements([[NozzleType.spray]])], in_game_bit=278),
        BlueCoin("Left Bird", [Requirements([[NozzleType.spray]])], in_game_bit=280),
        BlueCoin("Right Bird", [Requirements([[NozzleType.spray]])], in_game_bit=281),
        BlueCoin("Highest Rope", [Requirements(ROCKET_OR_HOVER)], in_game_bit=282),
        BlueCoin("Pole", [Requirements(ROCKET_OR_HOVER)], in_game_bit=283),
        BlueCoin("Deck", in_game_bit=288),
        BlueCoin("Swing", [Requirements(SPRAY_OR_HOVER)], in_game_bit=289),
        BlueCoin("Big Tree", in_game_bit=290),
        BlueCoin("Crevice", in_game_bit=291),
        BlueCoin("Sand Cabana Roof", in_game_bit=293),
        BlueCoin("Shack", [Requirements([[NozzleType.rocket]])], in_game_bit=294),
        BlueCoin("Sand Shine at Sand Cabana", [Requirements(SPRAY_OR_HOVER)], in_game_bit=271),
        BlueCoin("Sand Shine at Surf Cabana", [Requirements(SPRAY_OR_HOVER)], in_game_bit=272),
        BlueCoin("Middle Sand Shine", [Requirements(SPRAY_OR_HOVER)], in_game_bit=274),
        BlueCoin("Close Underwater", in_game_bit=284),
        BlueCoin("Far Underwater", in_game_bit=285),
        BlueCoin("Blue Fish", [Requirements([[NozzleType.turbo]])], in_game_bit=286),
        BlueCoin("Red Fish", [Requirements([[NozzleType.turbo]])], in_game_bit=287)],
    parent_region=SmsRegionName.GELATO_ENTRANCE
)

GELATO_BEACH_TWO: SmsRegion = SmsRegion(SmsRegionName.GELATO_TWO,
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_ONE} - Dune Bud Sand Castle Secret")],
    shines=[Shine("Mirror Madness! Tilt, Slam, Bam!", [Requirements([[NozzleType.spray]])], in_game_bit=21),],
    blue_coins=[BlueCoin("Big Sand Shine", [Requirements(SPRAY_OR_HOVER)], in_game_bit=292)],
    parent_region=SmsRegionName.GELATO_ENTRANCE
)

GELATO_BEACH_THREE: SmsRegion = SmsRegion(SmsRegionName.GELATO_THREE,
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_TWO} - Mirror Madness! Tilt, Slam, Bam!")],
    shines=[Shine("Wiggler Ahoy! Full Steam Ahead!", [Requirements(SPRAY_OR_HOVER)], in_game_bit=22),],
    blue_coins=[],
    parent_region=SmsRegionName.GELATO_ENTRANCE
)

GELATO_BEACH_FOUR: SmsRegion = SmsRegion(SmsRegionName.GELATO_FOUR,
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_THREE} - Wiggler Ahoy! Full Steam Ahead!")],
    shines=[Shine("The Sand Bird is Born", [Requirements([[NozzleType.hover]])], in_game_bit=23)],
    blue_coins=[BlueCoin("Sand Bird A", [Requirements([[NozzleType.hover]])], in_game_bit=296),
        BlueCoin("Sand Bird B", [Requirements([[NozzleType.hover]])], in_game_bit=297),
        BlueCoin("Sand Bird C", [Requirements([[NozzleType.hover]])], in_game_bit=298),
        BlueCoin("Sand Bird D", [Requirements([[NozzleType.hover]])], in_game_bit=299)],
    nozzle_boxes=[NozzleBox("Turbo Box", in_game_bit=877)],
    parent_region=SmsRegionName.GELATO_ENTRANCE
)

GELATO_BEACH_FIVE: SmsRegion = SmsRegion(SmsRegionName.GELATO_FIVE,
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_FOUR} - The Sand Bird is Born")],
    shines=[Shine("Il Piantissimo's Sand Sprint", [Requirements(TURBO_OR_HOVER)], in_game_bit=24),],
    blue_coins=[BlueCoin("Blue Cataquack", [Requirements([[NozzleType.spray]])], in_game_bit=273)],
    nozzle_boxes=[NozzleBox("Rocket Box", [Requirements(ROCKET_OR_SPLASHER)], in_game_bit=876)],
    parent_region=SmsRegionName.GELATO_ENTRANCE
)

GELATO_BEACH_SIX: SmsRegion = SmsRegion(SmsRegionName.GELATO_SIX,
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_FIVE} - Il Piantissimo's Sand Sprint")],
    shines=[Shine("Red Coins in the Coral Reef", in_game_bit=25),],
    blue_coins=[BlueCoin("Yellow Goo Dune Bud", [Requirements([[NozzleType.yoshi]])], in_game_bit=279),
        BlueCoin("Beehive", [Requirements([[NozzleType.yoshi]])], in_game_bit=295)],
    parent_region=SmsRegionName.GELATO_ENTRANCE
)

GELATO_BEACH_SEVEN: SmsRegion = SmsRegion(SmsRegionName.GELATO_SEVEN,
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_SIX} - Red Coins in the Coral Reef")],
    shines=[Shine("It's Shadow Mario! After Him!", [Requirements([[NozzleType.spray]])], in_game_bit=26),],
    blue_coins=[],
    parent_region=SmsRegionName.GELATO_ENTRANCE
)

GELATO_BEACH_EIGHT: SmsRegion = SmsRegion(SmsRegionName.GELATO_EIGHT,
    requirements=[Requirements(location=f"{SmsRegionName.GELATO_SEVEN} - It's Shadow Mario! After Him!")],
    shines=[Shine("The Watermelon Festival", [Requirements(TURBO_OR_SPLASHER)], in_game_bit=27),
        Shine("100 Coins", [Requirements(YOSHI_AND_SPRAY_OR_YOSHI_AND_HOVER)], hundred=True, in_game_bit=102)],
    blue_coins=[],
    parent_region=SmsRegionName.GELATO_ENTRANCE
)