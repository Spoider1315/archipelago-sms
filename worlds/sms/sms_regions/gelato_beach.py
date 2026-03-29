from .sms_region_helper import *

GELATO_BEACH_ENTRANCE: SmsRegion = SmsRegion(
    SmsRegionName.GELATO_ENTRANCE,
    requirements=[
        Requirements(ANY_SPLASHER, shines=5),
        Requirements(skip_forward=True),
    ],
    shines=[
        Shine(
            "100 Coins",
            requirements=[
                Requirements(SPROCKET_OR_HOVER),
                Requirements(
                    SPRAY_OR_HOVER_OR_ROCKET,
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - It's Shadow Mario! After Him!",
                ),
            ],
            hard=[
                Requirements(SPRAY_OR_HOVER),
                Requirements(
                    manual_none=True,
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - It's Shadow Mario! After Him!",
                ),
            ],
            advanced=[Requirements(SPRAY_OR_HOVER_OR_ROCKET)],
            hundred=True,
            in_game_bit=102,
        ),
    ],
    ticketed="Gelato Beach Ticket",
    parent_region=SmsRegionName.PLAZA,
)

GELATO_BEACH_ONE: SmsRegion = SmsRegion(
    SmsRegionName.GELATO_ONE,
    shines=[
        Shine(
            "Dune Bud Sand Castle Secret",
            [Requirements(SPRAY_OR_HOVER_OR_TURBO)],
            in_game_bit=20,
        ),
        Shine(
            "Mirror Madness! Tilt, Slam, Bam!",
            requirements=[Requirements([[NozzleType.spray]])],
            hard=[Requirements(SPRAY_OR_HOVER)],
            advanced=[Requirements(SPRAY_OR_HOVER_OR_TURBO)],
            in_game_bit=21,
        ),
        Shine(
            "Wiggler Ahoy! Full Steam Ahead!",
            [
                Requirements(
                    SPRAY_OR_HOVER_OR_TURBO,
                    location=f"{SmsRegionName.GELATO_ONE} - Mirror Madness! Tilt, Slam, Bam!",
                )
            ],
            in_game_bit=22,
        ),
        Shine(
            "Red Coins in the Sand Castle",
            requirements=[
                Requirements(
                    [[NozzleType.hover]],
                    location=f"{SmsRegionName.GELATO_ONE} - Wiggler Ahoy! Full Steam Ahead!",
                )
            ],
            hard=[
                Requirements(
                    SPRAY_OR_HOVER_OR_TURBO,
                    location=f"{SmsRegionName.GELATO_ONE} - Wiggler Ahoy! Full Steam Ahead!",
                )
            ],
            in_game_bit=28,
        ),
        Shine(
            "Sandy Shine Sprite",
            requirements=[Requirements(SPRAY_OR_HOVER)],
            hard=[Requirements(SPRAY_OR_HOVER_OR_TURBO)],
            in_game_bit=29,
        ),
    ],
    blue_coins=[
        BlueCoin(
            "Juicer",
            [
                Requirements(SPRAY_OR_HOVER),
                Requirements(
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint"
                ),
            ],
            in_game_bit=275,
        ),
        BlueCoin(
            "Rocket M",
            requirements=[
                Requirements(SPRAY_OR_HOVER),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            advanced=[
                Requirements(SPRAY_OR_HOVER_OR_TURBO),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            in_game_bit=276,
        ),
        BlueCoin(
            "Spawn Triangle",
            requirements=[Requirements([[NozzleType.spray]])],
            hard=[
                Requirements(SPRAY_OR_HOVER_OR_TURBO),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            in_game_bit=277,
        ),
        BlueCoin(
            "Trees Triangle",
            requirements=[Requirements([[NozzleType.spray]])],
            hard=[
                Requirements(SPRAY_OR_HOVER),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            advanced=[
                Requirements(SPRAY_OR_HOVER_OR_TURBO),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            in_game_bit=278,
        ),
        BlueCoin(
            "Left Bird",
            requirements=[
                Requirements([[NozzleType.spray]]),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            tears=[
                Requirements(SPRAY_OR_HOVER_OR_TURBO),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            in_game_bit=280,
        ),
        BlueCoin(
            "Right Bird",
            requirements=[
                Requirements([[NozzleType.spray]]),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            tears=[
                Requirements(SPRAY_OR_HOVER_OR_TURBO),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            in_game_bit=281,
        ),
        BlueCoin(
            "Highest Rope",
            requirements=[Requirements(ROCKET_OR_HOVER)],
            hard=[Requirements(manual_none=True)],
            in_game_bit=282,
        ),
        BlueCoin(
            "Pole",
            requirements=[Requirements(ROCKET_OR_HOVER)],
            hard=[Requirements(manual_none=True)],
            in_game_bit=283,
        ),
        BlueCoin("Deck", in_game_bit=288),
        BlueCoin(
            "Swing",
            requirements=[Requirements(SPRAY_OR_HOVER)],
            hard=[Requirements(manual_none=True)],
            in_game_bit=289,
        ),
        BlueCoin("Big Tree", in_game_bit=290),
        BlueCoin("Crevice", in_game_bit=291),
        BlueCoin("Sand Cabana Roof", in_game_bit=293),
        BlueCoin(
            "Shack",
            requirements=[Requirements([[NozzleType.rocket]])],
            hard=[
                Requirements(ROCKET_OR_HOVER),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            advanced=[
                Requirements(SPRAY_OR_HOVER_OR_ROCKET),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            in_game_bit=294,
        ),
    ],
    parent_region=SmsRegionName.GELATO_ENTRANCE,
)

GELATO_BEACH_ONE_TWO_FOUR: SmsRegion = SmsRegion(
    SmsRegionName.GELATO_ONE_TWO_FOUR,
    blue_coins=[
        BlueCoin(
            "Red Cataquack",
            requirements=[Requirements(SPRAY_OR_HOVER_OR_TURBO)],
            hard=[Requirements(manual_none=True)],
            in_game_bit=270,
        )
    ],
    parent_region=SmsRegionName.GELATO_ENTRANCE,
)

GELATO_NOT_THREE: SmsRegion = SmsRegion(
    SmsRegionName.GELATO_NOT_THREE,
    blue_coins=[
        BlueCoin(
            "Sand Shine at Sand Cabana",
            requirements=[
                Requirements(SPRAY_OR_HOVER),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            hard=[
                Requirements(SPRAY_OR_HOVER_OR_TURBO),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            in_game_bit=271,
        ),
        BlueCoin(
            "Sand Shine at Surf Cabana",
            requirements=[
                Requirements(SPRAY_OR_HOVER),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            hard=[
                Requirements(SPRAY_OR_HOVER_OR_TURBO),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            in_game_bit=272,
        ),
        BlueCoin(
            "Middle Sand Shine",
            requirements=[
                Requirements(SPRAY_OR_HOVER),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            hard=[
                Requirements(SPRAY_OR_HOVER_OR_TURBO),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            in_game_bit=274,
        ),
        BlueCoin("Close Underwater", in_game_bit=284),
        BlueCoin("Far Underwater", in_game_bit=285),
        BlueCoin(
            "Blue Fish",
            requirements=[Requirements([[NozzleType.turbo]])],
            hard=[Requirements(manual_none=True)],
            in_game_bit=286,
        ),
        BlueCoin(
            "Red Fish",
            requirements=[Requirements([[NozzleType.turbo]])],
            hard=[Requirements(manual_none=True)],
            in_game_bit=287,
        ),
    ],
    parent_region=SmsRegionName.GELATO_ENTRANCE,
)

GELATO_BEACH_TWO_FOUR_THRU_EIGHT: SmsRegion = SmsRegion(
    SmsRegionName.GELATO_TWO_FOUR_THRU_EIGHT,
    requirements=[
        Requirements(
            location=f"{SmsRegionName.GELATO_ONE} - Dune Bud Sand Castle Secret"
        )
    ],
    blue_coins=[
        BlueCoin(
            "Big Sand Shine",
            requirements=[
                Requirements(SPRAY_OR_HOVER),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            hard=[
                Requirements(SPRAY_OR_HOVER_OR_TURBO),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            in_game_bit=292,
        )
    ],
    parent_region=SmsRegionName.GELATO_ENTRANCE,
)

GELATO_BEACH_FOUR_ONLY: SmsRegion = SmsRegion(
    SmsRegionName.GELATO_FOUR_ONLY,
    requirements=[
        Requirements(
            location=f"{SmsRegionName.GELATO_ONE} - Wiggler Ahoy! Full Steam Ahead!"
        )
    ],
    shines=[
        Shine(
            "The Sand Bird is Born",
            requirements=[Requirements([[NozzleType.hover]])],
            hard=[Requirements(manual_none=True)],
            in_game_bit=23,
        )
    ],
    blue_coins=[
        BlueCoin(
            "Sand Bird A",
            [Requirements([[NozzleType.hover]])],
            [Requirements(manual_none=True)],
            in_game_bit=296,
        ),
        BlueCoin(
            "Sand Bird B",
            [Requirements([[NozzleType.hover]])],
            [Requirements(manual_none=True)],
            in_game_bit=297,
        ),
        BlueCoin(
            "Sand Bird C",
            [Requirements([[NozzleType.hover]])],
            [Requirements(manual_none=True)],
            in_game_bit=298,
        ),
        BlueCoin(
            "Sand Bird D",
            [Requirements([[NozzleType.hover]])],
            [Requirements(manual_none=True)],
            in_game_bit=299,
        ),
    ],
    nozzle_boxes=[NozzleBox("Turbo Box", in_game_bit=877)],
    parent_region=SmsRegionName.GELATO_ENTRANCE,
)

GELATO_BEACH_FIVE_EIGHT: SmsRegion = SmsRegion(
    SmsRegionName.GELATO_FIVE_EIGHT,
    requirements=[
        Requirements(
            location=f"{SmsRegionName.GELATO_FOUR_ONLY} - The Sand Bird is Born"
        )
    ],
    shines=[
        Shine(
            "Il Piantissimo's Sand Sprint",
            requirements=[Requirements(ROCKET_OR_HOVER_OR_TURBO)],
            hard=[Requirements(manual_none=True)],
            in_game_bit=24,
        ),
        Shine("Red Coins in the Coral Reef", in_game_bit=25),
        Shine(
            "It's Shadow Mario! After Him!",
            requirements=[Requirements([[NozzleType.spray]])],
            hard=[Requirements(SPRAY_OR_HOVER)],
            in_game_bit=26,
        ),
        Shine(
            "The Watermelon Festival",
            requirements=[Requirements(SPRAY_OR_HOVER_OR_TURBO)],
            hard=[Requirements(manual_none=True)],
            in_game_bit=27,
        ),
    ],
    blue_coins=[
        BlueCoin(
            "Blue Cataquack",
            [
                Requirements(SPRAY_OR_HOVER_OR_TURBO),
                Requirements(
                    [[NozzleType.yoshi]],
                    location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint",
                ),
            ],
            [Requirements(manual_none=True)],
            in_game_bit=273,
        )
    ],
    nozzle_boxes=[
        NozzleBox("Rocket Box", [Requirements(ROCKET_OR_SPLASHER)], in_game_bit=876)
    ],
    parent_region=SmsRegionName.GELATO_ENTRANCE,
)

GELATO_BEACH_SIX: SmsRegion = SmsRegion(
    SmsRegionName.GELATO_SIX,
    requirements=[
        Requirements(
            location=f"{SmsRegionName.GELATO_FIVE_EIGHT} - Il Piantissimo's Sand Sprint"
        )
    ],
    blue_coins=[
        BlueCoin(
            "Yellow Goo Dune Bud", [Requirements([[NozzleType.yoshi]])], in_game_bit=279
        ),
        BlueCoin("Beehive", [Requirements([[NozzleType.yoshi]])], in_game_bit=295),
    ],
    parent_region=SmsRegionName.GELATO_ENTRANCE,
)
