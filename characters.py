from peewee import BigIntegerField
from peewee import CharField
from peewee import FloatField
from peewee import IntegerField
from peewee import Model
from peewee import MySQLDatabase
from peewee import PrimaryKeyField
from peewee import TextField


database = MySQLDatabase("characters", **{"password": "", "user": ""})


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Characters(BaseModel):
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


class Auctionhouse(BaseModel):
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


class ItemInstance(BaseModel):
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
