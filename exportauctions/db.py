from peewee import BigIntegerField
from peewee import CharField
from peewee import CompositeKey
from peewee import FloatField
from peewee import IntegerField
from peewee import Model
from peewee import MySQLDatabase
from peewee import PrimaryKeyField
from peewee import TextField


# http://docs.peewee-orm.com/en/latest/peewee/database.html#run-time-database-configuration  # noqa
characters_db = MySQLDatabase(None)
world_db = MySQLDatabase(None)


class CharactersBaseModel(Model):
    class Meta:
        database = characters_db


class WorldBaseModel(Model):
    class Meta:
        database = world_db


class Characters(CharactersBaseModel):
    account = IntegerField(index=True)
    actionbars = IntegerField(db_column="actionBars")
    activetalentgroup = IntegerField(db_column="activeTalentGroup")
    ammoid = IntegerField(db_column="ammoId")
    arenapoints = IntegerField(db_column="arenaPoints")
    at_login = IntegerField()
    bankslots = IntegerField(db_column="bankSlots")
    chosentitle = IntegerField(db_column="chosenTitle")
    cinematic = IntegerField()
    class_ = IntegerField(db_column="class")
    death_expire_time = IntegerField()
    deletedate = IntegerField(db_column="deleteDate", null=True)
    deleteinfos_account = IntegerField(db_column="deleteInfos_Account",
                                       null=True)
    deleteinfos_name = CharField(db_column="deleteInfos_Name", null=True)
    drunk = IntegerField()
    equipmentcache = TextField(db_column="equipmentCache", null=True)
    exploredzones = TextField(db_column="exploredZones", null=True)
    extra_flags = IntegerField()
    face = IntegerField()
    facialstyle = IntegerField(db_column="facialStyle")
    gender = IntegerField()
    grantablelevels = IntegerField(db_column="grantableLevels")
    guid = PrimaryKeyField()
    haircolor = IntegerField(db_column="hairColor")
    hairstyle = IntegerField(db_column="hairStyle")
    health = IntegerField()
    instance = IntegerField(db_column="instance_id")
    instance_mode_mask = IntegerField()
    is_logout_resting = IntegerField()
    knowncurrencies = BigIntegerField(db_column="knownCurrencies")
    knowntitles = TextField(db_column="knownTitles", null=True)
    latency = IntegerField()
    level = IntegerField()
    leveltime = IntegerField()
    logout_time = IntegerField()
    map = IntegerField()
    money = IntegerField()
    name = CharField(index=True)
    online = IntegerField(index=True)
    orientation = FloatField()
    playerflags = IntegerField(db_column="playerFlags")
    position_x = FloatField()
    position_y = FloatField()
    position_z = FloatField()
    power1 = IntegerField()
    power2 = IntegerField()
    power3 = IntegerField()
    power4 = IntegerField()
    power5 = IntegerField()
    power6 = IntegerField()
    power7 = IntegerField()
    race = IntegerField()
    resettalents_cost = IntegerField()
    resettalents_time = IntegerField()
    reststate = IntegerField(db_column="restState")
    rest_bonus = FloatField()
    skin = IntegerField()
    stable_slots = IntegerField()
    talentgroupscount = IntegerField(db_column="talentGroupsCount")
    taxi_path = TextField(null=True)
    taximask = TextField()
    todayhonorpoints = IntegerField(db_column="todayHonorPoints")
    todaykills = IntegerField(db_column="todayKills")
    totalhonorpoints = IntegerField(db_column="totalHonorPoints")
    totalkills = IntegerField(db_column="totalKills")
    totaltime = IntegerField()
    trans_o = FloatField()
    trans_x = FloatField()
    trans_y = FloatField()
    trans_z = FloatField()
    transguid = IntegerField()
    watchedfaction = IntegerField(db_column="watchedFaction")
    xp = IntegerField()
    yesterdayhonorpoints = IntegerField(db_column="yesterdayHonorPoints")
    yesterdaykills = IntegerField(db_column="yesterdayKills")
    zone = IntegerField()

    class Meta:
        db_table = "characters"


class Auctionhouse(CharactersBaseModel):
    buyguid = IntegerField()
    buyoutprice = IntegerField()
    deposit = IntegerField()
    houseid = IntegerField()
    itemguid = IntegerField(unique=True)
    itemowner = IntegerField()
    lastbid = IntegerField()
    startbid = IntegerField()
    time = IntegerField()

    class Meta:
        db_table = "auctionhouse"


class ItemInstance(CharactersBaseModel):
    charges = TextField(null=True)
    count = IntegerField()
    creatorguid = IntegerField(db_column="creatorGuid")
    durability = IntegerField()
    duration = IntegerField()
    enchantments = TextField()
    flags = IntegerField()
    giftcreatorguid = IntegerField(db_column="giftCreatorGuid")
    guid = PrimaryKeyField()
    itementry = IntegerField(db_column="itemEntry")
    owner_guid = IntegerField(index=True)
    playedtime = IntegerField(db_column="playedTime")
    randompropertyid = IntegerField(db_column="randomPropertyId")
    text = TextField(null=True)

    class Meta:
        db_table = "item_instance"


class ItemTemplate(WorldBaseModel):
    allowableclass = IntegerField(db_column="AllowableClass")
    allowablerace = IntegerField(db_column="AllowableRace")
    armordamagemodifier = FloatField(db_column="ArmorDamageModifier")
    bagfamily = IntegerField(db_column="BagFamily")
    buycount = IntegerField(db_column="BuyCount")
    buyprice = BigIntegerField(db_column="BuyPrice")
    containerslots = IntegerField(db_column="ContainerSlots")
    disenchantid = IntegerField(db_column="DisenchantID")
    flags = IntegerField(db_column="Flags")
    flagsextra = IntegerField(db_column="FlagsExtra")
    foodtype = IntegerField(db_column="FoodType")
    gemproperties = IntegerField(db_column="GemProperties")
    holidayid = IntegerField(db_column="HolidayId")
    inventorytype = IntegerField(db_column="InventoryType")
    itemlevel = IntegerField(db_column="ItemLevel")
    itemlimitcategory = IntegerField(db_column="ItemLimitCategory")
    languageid = IntegerField(db_column="LanguageID")
    map = IntegerField(db_column="Map")
    material = IntegerField(db_column="Material")
    maxdurability = IntegerField(db_column="MaxDurability")
    pagematerial = IntegerField(db_column="PageMaterial")
    pagetext = IntegerField(db_column="PageText")
    quality = IntegerField(db_column="Quality")
    randomproperty = IntegerField(db_column="RandomProperty")
    randomsuffix = IntegerField(db_column="RandomSuffix")
    rangedmodrange = FloatField(db_column="RangedModRange")
    requiredcityrank = IntegerField(db_column="RequiredCityRank")
    requireddisenchantskill = IntegerField(db_column="RequiredDisenchantSkill")
    requiredlevel = IntegerField(db_column="RequiredLevel")
    requiredreputationfaction = IntegerField(
        db_column="RequiredReputationFaction")
    requiredreputationrank = IntegerField(db_column="RequiredReputationRank")
    requiredskill = IntegerField(db_column="RequiredSkill")
    requiredskillrank = IntegerField(db_column="RequiredSkillRank")
    scalingstatdistribution = IntegerField(db_column="ScalingStatDistribution")
    scalingstatvalue = IntegerField(db_column="ScalingStatValue")
    scriptname = CharField(db_column="ScriptName")
    sellprice = IntegerField(db_column="SellPrice")
    soundoverridesubclass = IntegerField(db_column="SoundOverrideSubclass")
    statscount = IntegerField(db_column="StatsCount")
    totemcategory = IntegerField(db_column="TotemCategory")
    verifiedbuild = IntegerField(db_column="VerifiedBuild", null=True)
    ammo_type = IntegerField()
    arcane_res = IntegerField()
    area = IntegerField()
    armor = IntegerField()
    block = IntegerField()
    bonding = IntegerField()
    class_ = IntegerField(db_column="class", index=True)
    delay = IntegerField()
    description = CharField()
    displayid = IntegerField()
    dmg_max1 = FloatField()
    dmg_max2 = FloatField()
    dmg_min1 = FloatField()
    dmg_min2 = FloatField()
    dmg_type1 = IntegerField()
    dmg_type2 = IntegerField()
    duration = IntegerField()
    entry = PrimaryKeyField()
    fire_res = IntegerField()
    flagscustom = IntegerField(db_column="flagsCustom")
    frost_res = IntegerField()
    holy_res = IntegerField()
    itemset = IntegerField()
    lockid = IntegerField()
    maxmoneyloot = IntegerField(db_column="maxMoneyLoot")
    maxcount = IntegerField()
    minmoneyloot = IntegerField(db_column="minMoneyLoot")
    name = CharField(index=True)
    nature_res = IntegerField()
    requiredhonorrank = IntegerField()
    requiredspell = IntegerField()
    shadow_res = IntegerField()
    sheath = IntegerField()
    socketbonus = IntegerField(db_column="socketBonus")
    socketcolor_1 = IntegerField(db_column="socketColor_1")
    socketcolor_2 = IntegerField(db_column="socketColor_2")
    socketcolor_3 = IntegerField(db_column="socketColor_3")
    socketcontent_1 = IntegerField(db_column="socketContent_1")
    socketcontent_2 = IntegerField(db_column="socketContent_2")
    socketcontent_3 = IntegerField(db_column="socketContent_3")
    spellcategory_1 = IntegerField()
    spellcategory_2 = IntegerField()
    spellcategory_3 = IntegerField()
    spellcategory_4 = IntegerField()
    spellcategory_5 = IntegerField()
    spellcategorycooldown_1 = IntegerField()
    spellcategorycooldown_2 = IntegerField()
    spellcategorycooldown_3 = IntegerField()
    spellcategorycooldown_4 = IntegerField()
    spellcategorycooldown_5 = IntegerField()
    spellcharges_1 = IntegerField()
    spellcharges_2 = IntegerField()
    spellcharges_3 = IntegerField()
    spellcharges_4 = IntegerField()
    spellcharges_5 = IntegerField()
    spellcooldown_1 = IntegerField()
    spellcooldown_2 = IntegerField()
    spellcooldown_3 = IntegerField()
    spellcooldown_4 = IntegerField()
    spellcooldown_5 = IntegerField()
    spellid_1 = IntegerField()
    spellid_2 = IntegerField()
    spellid_3 = IntegerField()
    spellid_4 = IntegerField()
    spellid_5 = IntegerField()
    spellppmrate_1 = FloatField(db_column="spellppmRate_1")
    spellppmrate_2 = FloatField(db_column="spellppmRate_2")
    spellppmrate_3 = FloatField(db_column="spellppmRate_3")
    spellppmrate_4 = FloatField(db_column="spellppmRate_4")
    spellppmrate_5 = FloatField(db_column="spellppmRate_5")
    spelltrigger_1 = IntegerField()
    spelltrigger_2 = IntegerField()
    spelltrigger_3 = IntegerField()
    spelltrigger_4 = IntegerField()
    spelltrigger_5 = IntegerField()
    stackable = IntegerField(null=True)
    startquest = IntegerField()
    stat_type1 = IntegerField()
    stat_type10 = IntegerField()
    stat_type2 = IntegerField()
    stat_type3 = IntegerField()
    stat_type4 = IntegerField()
    stat_type5 = IntegerField()
    stat_type6 = IntegerField()
    stat_type7 = IntegerField()
    stat_type8 = IntegerField()
    stat_type9 = IntegerField()
    stat_value1 = IntegerField()
    stat_value10 = IntegerField()
    stat_value2 = IntegerField()
    stat_value3 = IntegerField()
    stat_value4 = IntegerField()
    stat_value5 = IntegerField()
    stat_value6 = IntegerField()
    stat_value7 = IntegerField()
    stat_value8 = IntegerField()
    stat_value9 = IntegerField()
    subclass = IntegerField()

    class Meta:
        db_table = "item_template"


class ItemTemplateLocale(WorldBaseModel):
    description = TextField(db_column="Description", null=True)
    id = IntegerField(db_column="ID")
    name = TextField(db_column="Name", null=True)
    verifiedbuild = IntegerField(db_column="VerifiedBuild", null=True)
    locale = CharField()

    class Meta:
        db_table = "item_template_locale"
        indexes = (
            (("id", "locale"), True),
        )
        primary_key = CompositeKey("id", "locale")
