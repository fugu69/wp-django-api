# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class ArticleArticle(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    body = models.TextField()
    pinned = models.BooleanField()
    pin_order = models.IntegerField()
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'article_article'


class ArticleArticleViewers(models.Model):
    article = models.ForeignKey(ArticleArticle, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'article_article_viewers'
        unique_together = (('article', 'player'),)


class ArticleArticleVotesCon(models.Model):
    article = models.ForeignKey(ArticleArticle, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'article_article_votes_con'
        unique_together = (('article', 'player'),)


class ArticleArticleVotesPro(models.Model):
    article = models.ForeignKey(ArticleArticle, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'article_article_votes_pro'
        unique_together = (('article', 'player'),)


class ArticleCommentsblock(models.Model):
    date = models.DateTimeField()
    messages = models.TextField()
    article = models.ForeignKey(ArticleArticle, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'article_commentsblock'


class ArticleSubscription(models.Model):
    date = models.DateTimeField()
    author = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, related_name='articlesubscription_player_set')

    class Meta:
        managed = False
        db_table = 'article_subscription'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AvaBorderAvaborder(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    price = models.IntegerField()
    deleted = models.BooleanField()
    shape = models.TextField()
    box_x = models.DecimalField(max_digits=9, decimal_places=2)
    box_y = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ava_border_avaborder'


class AvaBorderAvaborderownership(models.Model):
    in_use = models.BooleanField()
    border = models.ForeignKey(AvaBorderAvaborder, models.DO_NOTHING)
    owner = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)
    png_use = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ava_border_avaborderownership'


class BillChangecoat(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_changecoat'


class BillChangecoatVotesCon(models.Model):
    changecoat = models.ForeignKey(BillChangecoat, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_changecoat_votes_con'
        unique_together = (('changecoat', 'player'),)


class BillChangecoatVotesPro(models.Model):
    changecoat = models.ForeignKey(BillChangecoat, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_changecoat_votes_pro'
        unique_together = (('changecoat', 'player'),)


class BillChangeform(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    form = models.CharField(max_length=15)
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_changeform'


class BillChangeformVotesCon(models.Model):
    changeform = models.ForeignKey(BillChangeform, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_changeform_votes_con'
        unique_together = (('changeform', 'player'),)


class BillChangeformVotesPro(models.Model):
    changeform = models.ForeignKey(BillChangeform, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_changeform_votes_pro'
        unique_together = (('changeform', 'player'),)


class BillChangeresidency(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    residency = models.CharField(max_length=5)
    rifle_cost = models.IntegerField()
    drone_cost = models.IntegerField()
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_changeresidency'


class BillChangeresidencyVotesCon(models.Model):
    changeresidency = models.ForeignKey(BillChangeresidency, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_changeresidency_votes_con'
        unique_together = (('changeresidency', 'player'),)


class BillChangeresidencyVotesPro(models.Model):
    changeresidency = models.ForeignKey(BillChangeresidency, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_changeresidency_votes_pro'
        unique_together = (('changeresidency', 'player'),)


class BillChangetaxes(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    destination = models.CharField(max_length=6, blank=True, null=True)
    tax_mod = models.CharField(max_length=6, blank=True, null=True)
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING, blank=True, null=True)
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)
    new_tax = models.DecimalField(max_digits=5, decimal_places=2)
    old_tax = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'bill_changetaxes'


class BillChangetaxesVotesCon(models.Model):
    changetaxes = models.ForeignKey(BillChangetaxes, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_changetaxes_votes_con'
        unique_together = (('changetaxes', 'player'),)


class BillChangetaxesVotesPro(models.Model):
    changetaxes = models.ForeignKey(BillChangetaxes, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_changetaxes_votes_pro'
        unique_together = (('changetaxes', 'player'),)


class BillChangetitle(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    new_title = models.CharField(max_length=50)
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_changetitle'


class BillChangetitleVotesCon(models.Model):
    changetitle = models.ForeignKey(BillChangetitle, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_changetitle_votes_con'
        unique_together = (('changetitle', 'player'),)


class BillChangetitleVotesPro(models.Model):
    changetitle = models.ForeignKey(BillChangetitle, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_changetitle_votes_pro'
        unique_together = (('changetitle', 'player'),)


class BillConstruction(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    building = models.CharField(max_length=20, blank=True, null=True)
    exp_value = models.IntegerField()
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_construction'


class BillConstructionVotesCon(models.Model):
    construction = models.ForeignKey(BillConstruction, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_construction_votes_con'
        unique_together = (('construction', 'player'),)


class BillConstructionVotesPro(models.Model):
    construction = models.ForeignKey(BillConstruction, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_construction_votes_pro'
        unique_together = (('construction', 'player'),)


class BillExploreall(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    resource = models.CharField(max_length=4, blank=True, null=True)
    exp_value = models.DecimalField(max_digits=5, decimal_places=2)
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_exploreall'


class BillExploreallVotesCon(models.Model):
    exploreall = models.ForeignKey(BillExploreall, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_exploreall_votes_con'
        unique_together = (('exploreall', 'player'),)


class BillExploreallVotesPro(models.Model):
    exploreall = models.ForeignKey(BillExploreall, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_exploreall_votes_pro'
        unique_together = (('exploreall', 'player'),)


class BillExploreallregion(models.Model):
    exp_value = models.DecimalField(max_digits=5, decimal_places=2)
    exp_bill = models.ForeignKey(BillExploreall, models.DO_NOTHING)
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_exploreallregion'


class BillExploreresources(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    resource = models.CharField(max_length=4, blank=True, null=True)
    exp_value = models.DecimalField(max_digits=5, decimal_places=2)
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_exploreresources'


class BillExploreresourcesVotesCon(models.Model):
    exploreresources = models.ForeignKey(BillExploreresources, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_exploreresources_votes_con'
        unique_together = (('exploreresources', 'player'),)


class BillExploreresourcesVotesPro(models.Model):
    exploreresources = models.ForeignKey(BillExploreresources, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_exploreresources_votes_pro'
        unique_together = (('exploreresources', 'player'),)


class BillIndependence(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_independence'


class BillIndependenceVotesCon(models.Model):
    independence = models.ForeignKey(BillIndependence, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_independence_votes_con'
        unique_together = (('independence', 'player'),)


class BillIndependenceVotesPro(models.Model):
    independence = models.ForeignKey(BillIndependence, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_independence_votes_pro'
        unique_together = (('independence', 'player'),)


class BillMartiallaw(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)
    mode = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'bill_martiallaw'


class BillMartiallawVotesCon(models.Model):
    martiallaw = models.ForeignKey(BillMartiallaw, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_martiallaw_votes_con'
        unique_together = (('martiallaw', 'player'),)


class BillMartiallawVotesPro(models.Model):
    martiallaw = models.ForeignKey(BillMartiallaw, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_martiallaw_votes_pro'
        unique_together = (('martiallaw', 'player'),)


class BillPurchaseauction(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    old_good = models.CharField(max_length=10)
    buy_value = models.BigIntegerField()
    lots_count = models.BigIntegerField()
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)
    good = models.ForeignKey('StorageGood', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_purchaseauction'


class BillPurchaseauctionVotesCon(models.Model):
    purchaseauction = models.ForeignKey(BillPurchaseauction, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_purchaseauction_votes_con'
        unique_together = (('purchaseauction', 'player'),)


class BillPurchaseauctionVotesPro(models.Model):
    purchaseauction = models.ForeignKey(BillPurchaseauction, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_purchaseauction_votes_pro'
        unique_together = (('purchaseauction', 'player'),)


class BillStartwar(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    war_type = models.CharField(max_length=20, blank=True, null=True)
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)
    region_to = models.ForeignKey('RegionRegion', models.DO_NOTHING, related_name='billstartwar_region_to_set')
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_startwar'


class BillStartwarVotesCon(models.Model):
    startwar = models.ForeignKey(BillStartwar, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_startwar_votes_con'
        unique_together = (('startwar', 'player'),)


class BillStartwarVotesPro(models.Model):
    startwar = models.ForeignKey(BillStartwar, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_startwar_votes_pro'
        unique_together = (('startwar', 'player'),)


class BillTransferaccept(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)
    state = models.ForeignKey('StateState', models.DO_NOTHING)
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_transferaccept'


class BillTransferacceptVotesCon(models.Model):
    transferaccept = models.ForeignKey(BillTransferaccept, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_transferaccept_votes_con'
        unique_together = (('transferaccept', 'player'),)


class BillTransferacceptVotesPro(models.Model):
    transferaccept = models.ForeignKey(BillTransferaccept, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_transferaccept_votes_pro'
        unique_together = (('transferaccept', 'player'),)


class BillTransferregion(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)
    state = models.ForeignKey('StateState', models.DO_NOTHING)
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_transferregion'


class BillTransferregionVotesCon(models.Model):
    transferregion = models.ForeignKey(BillTransferregion, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_transferregion_votes_con'
        unique_together = (('transferregion', 'player'),)


class BillTransferregionVotesPro(models.Model):
    transferregion = models.ForeignKey(BillTransferregion, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_transferregion_votes_pro'
        unique_together = (('transferregion', 'player'),)


class BillTransferresources(models.Model):
    running = models.BooleanField()
    type = models.CharField(max_length=2, blank=True, null=True)
    cash_cost = models.BigIntegerField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField(blank=True, null=True)
    send_cash = models.BooleanField()
    send_count = models.BigIntegerField()
    initiator = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    send_good = models.ForeignKey('StorageGood', models.DO_NOTHING, blank=True, null=True)
    send_treasury = models.ForeignKey('StateTreasury', models.DO_NOTHING)
    take_treasury = models.ForeignKey('StateTreasury', models.DO_NOTHING, related_name='billtransferresources_take_treasury_set')
    task = models.OneToOneField('DjangoCeleryBeatPeriodictask', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_transferresources'


class BillTransferresourcesVotesCon(models.Model):
    transferresources = models.ForeignKey(BillTransferresources, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_transferresources_votes_con'
        unique_together = (('transferresources', 'player'),)


class BillTransferresourcesVotesPro(models.Model):
    transferresources = models.ForeignKey(BillTransferresources, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bill_transferresources_votes_pro'
        unique_together = (('transferresources', 'player'),)


class ChatChat(models.Model):
    state = models.ForeignKey('StateState', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_chat'


class ChatChatmembers(models.Model):
    chat = models.ForeignKey(ChatChat, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chat_chatmembers'


class ChatMessageblock(models.Model):
    date = models.DateTimeField()
    messages = models.TextField()
    chat = models.ForeignKey(ChatChat, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chat_messageblock'


class ChatSticker(models.Model):
    description = models.CharField(max_length=20)
    image = models.CharField(max_length=100)
    deleted = models.BooleanField()
    pack = models.ForeignKey('ChatStickerpack', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chat_sticker'


class ChatStickerpack(models.Model):
    title = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    creator_link = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    deleted = models.BooleanField()
    price = models.IntegerField()
    owner = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    percent = models.IntegerField()
    creator_az = models.CharField(max_length=100, blank=True, null=True)
    creator_be = models.CharField(max_length=100, blank=True, null=True)
    creator_de = models.CharField(max_length=100, blank=True, null=True)
    creator_en = models.CharField(max_length=100, blank=True, null=True)
    creator_es = models.CharField(max_length=100, blank=True, null=True)
    creator_ind = models.CharField(max_length=100, blank=True, null=True)
    creator_lv = models.CharField(max_length=100, blank=True, null=True)
    creator_pl = models.CharField(max_length=100, blank=True, null=True)
    creator_pt_br = models.CharField(max_length=100, blank=True, null=True)
    creator_ru = models.CharField(max_length=100, blank=True, null=True)
    creator_tr = models.CharField(max_length=100, blank=True, null=True)
    creator_uk = models.CharField(max_length=100, blank=True, null=True)
    description_az = models.CharField(max_length=500, blank=True, null=True)
    description_be = models.CharField(max_length=500, blank=True, null=True)
    description_de = models.CharField(max_length=500, blank=True, null=True)
    description_en = models.CharField(max_length=500, blank=True, null=True)
    description_es = models.CharField(max_length=500, blank=True, null=True)
    description_ind = models.CharField(max_length=500, blank=True, null=True)
    description_lv = models.CharField(max_length=500, blank=True, null=True)
    description_pl = models.CharField(max_length=500, blank=True, null=True)
    description_pt_br = models.CharField(max_length=500, blank=True, null=True)
    description_ru = models.CharField(max_length=500, blank=True, null=True)
    description_tr = models.CharField(max_length=500, blank=True, null=True)
    description_uk = models.CharField(max_length=500, blank=True, null=True)
    title_az = models.CharField(max_length=100, blank=True, null=True)
    title_be = models.CharField(max_length=100, blank=True, null=True)
    title_de = models.CharField(max_length=100, blank=True, null=True)
    title_en = models.CharField(max_length=100, blank=True, null=True)
    title_es = models.CharField(max_length=100, blank=True, null=True)
    title_ind = models.CharField(max_length=100, blank=True, null=True)
    title_lv = models.CharField(max_length=100, blank=True, null=True)
    title_pl = models.CharField(max_length=100, blank=True, null=True)
    title_pt_br = models.CharField(max_length=100, blank=True, null=True)
    title_ru = models.CharField(max_length=100, blank=True, null=True)
    title_tr = models.CharField(max_length=100, blank=True, null=True)
    title_uk = models.CharField(max_length=100, blank=True, null=True)
    creator_fr = models.CharField(max_length=100, blank=True, null=True)
    creator_it = models.CharField(max_length=100, blank=True, null=True)
    creator_sr = models.CharField(max_length=100, blank=True, null=True)
    description_fr = models.CharField(max_length=500, blank=True, null=True)
    description_it = models.CharField(max_length=500, blank=True, null=True)
    description_sr = models.CharField(max_length=500, blank=True, null=True)
    title_fr = models.CharField(max_length=100, blank=True, null=True)
    title_it = models.CharField(max_length=100, blank=True, null=True)
    title_sr = models.CharField(max_length=100, blank=True, null=True)
    creator_hy = models.CharField(max_length=100, blank=True, null=True)
    description_hy = models.CharField(max_length=500, blank=True, null=True)
    title_hy = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_stickerpack'


class ChatStickersownership(models.Model):
    owner = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)
    pack = models.ForeignKey(ChatStickerpack, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chat_stickersownership'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCeleryBeatClockedschedule(models.Model):
    clocked_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_clockedschedule'


class DjangoCeleryBeatCrontabschedule(models.Model):
    minute = models.CharField(max_length=240)
    hour = models.CharField(max_length=96)
    day_of_week = models.CharField(max_length=64)
    day_of_month = models.CharField(max_length=124)
    month_of_year = models.CharField(max_length=64)
    timezone = models.CharField(max_length=63)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_crontabschedule'


class DjangoCeleryBeatIntervalschedule(models.Model):
    every = models.IntegerField()
    period = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_intervalschedule'


class DjangoCeleryBeatPeriodictask(models.Model):
    name = models.CharField(unique=True, max_length=200)
    task = models.CharField(max_length=200)
    args = models.TextField()
    kwargs = models.TextField()
    queue = models.CharField(max_length=200, blank=True, null=True)
    exchange = models.CharField(max_length=200, blank=True, null=True)
    routing_key = models.CharField(max_length=200, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    last_run_at = models.DateTimeField(blank=True, null=True)
    total_run_count = models.IntegerField()
    date_changed = models.DateTimeField()
    description = models.TextField()
    crontab = models.ForeignKey(DjangoCeleryBeatCrontabschedule, models.DO_NOTHING, blank=True, null=True)
    interval = models.ForeignKey(DjangoCeleryBeatIntervalschedule, models.DO_NOTHING, blank=True, null=True)
    solar = models.ForeignKey('DjangoCeleryBeatSolarschedule', models.DO_NOTHING, blank=True, null=True)
    one_off = models.BooleanField()
    start_time = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    headers = models.TextField()
    clocked = models.ForeignKey(DjangoCeleryBeatClockedschedule, models.DO_NOTHING, blank=True, null=True)
    expire_seconds = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictask'


class DjangoCeleryBeatPeriodictasks(models.Model):
    ident = models.SmallIntegerField(primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictasks'


class DjangoCeleryBeatSolarschedule(models.Model):
    event = models.CharField(max_length=24)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_solarschedule'
        unique_together = (('event', 'latitude', 'longitude'),)


class DjangoCeleryResultsChordcounter(models.Model):
    group_id = models.CharField(unique=True, max_length=255)
    sub_tasks = models.TextField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_celery_results_chordcounter'


class DjangoCeleryResultsGroupresult(models.Model):
    group_id = models.CharField(unique=True, max_length=255)
    date_created = models.DateTimeField()
    date_done = models.DateTimeField()
    content_type = models.CharField(max_length=128)
    content_encoding = models.CharField(max_length=64)
    result = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_results_groupresult'


class DjangoCeleryResultsTaskresult(models.Model):
    task_id = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=50)
    content_type = models.CharField(max_length=128)
    content_encoding = models.CharField(max_length=64)
    result = models.TextField(blank=True, null=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True, null=True)
    meta = models.TextField(blank=True, null=True)
    task_args = models.TextField(blank=True, null=True)
    task_kwargs = models.TextField(blank=True, null=True)
    task_name = models.CharField(max_length=255, blank=True, null=True)
    worker = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField()
    periodic_task_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_results_taskresult'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class DjangoSummernoteAttachment(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    file = models.CharField(max_length=100)
    uploaded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_summernote_attachment'


class EventActivityevent(models.Model):
    running = models.BooleanField()
    title = models.CharField(max_length=30)
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_activityevent'


class EventActivityeventpart(models.Model):
    points = models.IntegerField()
    paid_points = models.IntegerField()
    global_paid_points = models.IntegerField()
    event = models.ForeignKey(EventActivityevent, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)
    boost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_activityeventpart'


class EventActivityglobalpart(models.Model):
    points = models.IntegerField()
    event = models.ForeignKey(EventActivityevent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_activityglobalpart'


class EventCashevent(models.Model):
    running = models.BooleanField()
    title = models.CharField(max_length=30)
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_cashevent'


class EventInvite(models.Model):
    invited = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)
    sender = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, related_name='eventinvite_sender_set')
    exp = models.IntegerField()
    event = models.ForeignKey(EventCashevent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_invite'


class FactoryAutoproduce(models.Model):
    dtime = models.DateTimeField()
    old_good = models.CharField(max_length=10, blank=True, null=True)
    schema = models.IntegerField()
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    storage = models.ForeignKey('StorageStorage', models.DO_NOTHING)
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)
    good = models.ForeignKey('StorageGood', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factory_autoproduce'


class FactoryBlueprint(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    energy_cost = models.IntegerField()
    good = models.ForeignKey('StorageGood', models.DO_NOTHING)
    cash_cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'factory_blueprint'


class FactoryComponent(models.Model):
    count = models.IntegerField()
    blueprint = models.ForeignKey(FactoryBlueprint, models.DO_NOTHING)
    good = models.ForeignKey('StorageGood', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'factory_component'


class FactoryFactory(models.Model):
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=100, blank=True, null=True)
    level = models.IntegerField()
    deleted = models.BooleanField()
    owner = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factory_factory'


class FactoryProductionlog(models.Model):
    dtime = models.DateTimeField()
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    prod_storage = models.ForeignKey('StorageStorage', models.DO_NOTHING, blank=True, null=True)
    old_good = models.CharField(max_length=20, blank=True, null=True)
    good_move = models.CharField(max_length=5)
    prod_value = models.IntegerField()
    cash = models.BooleanField()
    good = models.ForeignKey('StorageGood', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factory_productionlog'


class FactoryWorkplace(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    worker = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'factory_workplace'


class FactoryWorkshop(models.Model):
    good = models.CharField(max_length=20)
    factory = models.ForeignKey(FactoryFactory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'factory_workshop'


class GovMinister(models.Model):
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)
    state = models.ForeignKey('StateState', models.DO_NOTHING)
    post_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'gov_minister'


class GovMinisterRights(models.Model):
    minister = models.ForeignKey(GovMinister, models.DO_NOTHING)
    ministerright = models.ForeignKey('GovMinisterright', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gov_minister_rights'
        unique_together = (('minister', 'ministerright'),)


class GovMinisterright(models.Model):
    right = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'gov_ministerright'


class GovPermitrequest(models.Model):
    deleted = models.BooleanField()
    char = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey('StateState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gov_permitrequest'


class GovPresident(models.Model):
    leader = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    state = models.OneToOneField('StateState', models.DO_NOTHING)
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)
    elections_day = models.IntegerField()
    foundation_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gov_president'


class GovPresidentialvoting(models.Model):
    running = models.BooleanField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField()
    president = models.ForeignKey(GovPresident, models.DO_NOTHING)
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gov_presidentialvoting'


class GovPresidentialvotingCandidates(models.Model):
    presidentialvoting = models.ForeignKey(GovPresidentialvoting, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gov_presidentialvoting_candidates'
        unique_together = (('presidentialvoting', 'player'),)


class GovResidencyrequest(models.Model):
    char = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey('StateState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gov_residencyrequest'


class GovVote(models.Model):
    challenger = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, related_name='govvote_player_set')
    voting = models.ForeignKey(GovPresidentialvoting, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gov_vote'


class GovWorkpermit(models.Model):
    dtime = models.DateTimeField()
    deleted = models.BooleanField()
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey('StateState', models.DO_NOTHING)
    until = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gov_workpermit'


class MetricsDailycash(models.Model):
    date = models.DateField()
    cash = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'metrics_dailycash'


class MetricsDailycashbystate(models.Model):
    date = models.DateField()
    cash = models.BigIntegerField()
    state = models.ForeignKey('StateState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'metrics_dailycashbystate'


class MetricsDailygold(models.Model):
    date = models.DateField()
    gold = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'metrics_dailygold'


class MetricsDailygoldbystate(models.Model):
    date = models.DateField()
    gold = models.BigIntegerField()
    state = models.ForeignKey('StateState', models.DO_NOTHING)
    daily_gold = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'metrics_dailygoldbystate'


class MetricsDailyoil(models.Model):
    date = models.DateField()
    oil = models.BigIntegerField()
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'metrics_dailyoil'


class MetricsDailyore(models.Model):
    date = models.DateField()
    ore = models.BigIntegerField()
    type = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'metrics_dailyore'


class PartyMembershiplog(models.Model):
    dtime = models.DateTimeField()
    exit_dtime = models.DateTimeField(blank=True, null=True)
    party = models.ForeignKey('PartyParty', models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_membershiplog'


class PartyParty(models.Model):
    title = models.CharField(max_length=30)
    type = models.CharField(max_length=2)
    foundation_date = models.DateTimeField()
    description = models.CharField(max_length=300, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    deleted = models.BooleanField()
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING, blank=True, null=True)
    members_image = models.CharField(max_length=100, blank=True, null=True)
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)
    color = models.CharField(max_length=6)
    primaries_day = models.IntegerField()
    gold = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'party_party'


class PartyPartyapply(models.Model):
    party = models.ForeignKey(PartyParty, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=2)
    dtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'party_partyapply'


class PartyPartygoldlog(models.Model):
    dtime = models.DateTimeField()
    gold = models.BigIntegerField()
    activity_txt = models.CharField(max_length=10, blank=True, null=True)
    party = models.ForeignKey(PartyParty, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'party_partygoldlog'


class PartyPartyposition(models.Model):
    title = models.CharField(max_length=30)
    based = models.BooleanField()
    party_lead = models.BooleanField()
    party_sec = models.BooleanField()
    party = models.ForeignKey(PartyParty, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'party_partyposition'


class PartyPrimaries(models.Model):
    running = models.BooleanField()
    prim_start = models.DateTimeField(blank=True, null=True)
    prim_end = models.DateTimeField(blank=True, null=True)
    party = models.ForeignKey(PartyParty, models.DO_NOTHING)
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_primaries'


class PartyPrimariesleader(models.Model):
    leader = models.OneToOneField('PlayerPlayer', models.DO_NOTHING)
    party = models.OneToOneField(PartyParty, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'party_primariesleader'


class PartyPrimbulletin(models.Model):
    candidate = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, related_name='partyprimbulletin_player_set')
    primaries = models.ForeignKey(PartyPrimaries, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'party_primbulletin'


class PlayerAutomining(models.Model):
    dtime = models.DateTimeField()
    resource = models.CharField(max_length=4, blank=True, null=True)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_automining'


class PlayerBonuscode(models.Model):
    code = models.CharField(max_length=30)
    reusable = models.BooleanField()
    date = models.DateTimeField()
    premium = models.IntegerField()
    gold = models.IntegerField()
    wild_pass = models.IntegerField()
    cash = models.IntegerField()
    color = models.CharField(max_length=20)
    invite = models.BooleanField()
    plane = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'player_bonuscode'


class PlayerCashlog(models.Model):
    dtime = models.DateTimeField()
    cash = models.BigIntegerField()
    object_id = models.IntegerField(blank=True, null=True)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    activity_txt = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_cashlog'


class PlayerCodeusage(models.Model):
    dtime = models.DateTimeField()
    code = models.ForeignKey(PlayerBonuscode, models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_codeusage'


class PlayerDonutlog(models.Model):
    dtime = models.DateTimeField()
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_donutlog'


class PlayerEnergyspent(models.Model):
    points = models.IntegerField()
    fin = models.BooleanField()
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'player_energyspent'


class PlayerEventpart(models.Model):
    points = models.IntegerField()
    event = models.ForeignKey('PlayerGameevent', models.DO_NOTHING)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)
    paid_points = models.IntegerField()
    global_paid_points = models.IntegerField()
    boost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_eventpart'


class PlayerFreebieusage(models.Model):
    dtime = models.DateTimeField()
    type = models.CharField(max_length=10)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_freebieusage'


class PlayerGameevent(models.Model):
    running = models.BooleanField()
    title = models.CharField(max_length=30)
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'player_gameevent'


class PlayerGlobalpart(models.Model):
    points = models.IntegerField()
    event = models.ForeignKey(PlayerGameevent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'player_globalpart'


class PlayerGoldlog(models.Model):
    dtime = models.DateTimeField()
    gold = models.BigIntegerField()
    object_id = models.IntegerField(blank=True, null=True)
    activity_txt = models.CharField(max_length=6, blank=True, null=True)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_goldlog'


class PlayerJackpot(models.Model):
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_jackpot'


class PlayerLootbox(models.Model):
    stock = models.IntegerField()
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING)
    garant_in = models.IntegerField()
    opened = models.IntegerField()
    dtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_lootbox'


class PlayerMedal(models.Model):
    count = models.IntegerField()
    type = models.CharField(max_length=10)
    player = models.ForeignKey('PlayerPlayer', models.DO_NOTHING, blank=True, null=True)
    dtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_medal'


class PlayerPlayer(models.Model):
    banned = models.BooleanField()
    user_ip = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30)
    image = models.CharField(max_length=100, blank=True, null=True)
    time_zone = models.CharField(max_length=50)
    residency_date = models.DateTimeField()
    level = models.IntegerField()
    exp = models.IntegerField()
    energy = models.IntegerField()
    last_refill = models.DateTimeField()
    cash = models.BigIntegerField()
    gold = models.BigIntegerField()
    prize_gold = models.BigIntegerField()
    bottles = models.BigIntegerField()
    account = models.OneToOneField(AuthUser, models.DO_NOTHING)
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING, blank=True, null=True)
    residency = models.ForeignKey('RegionRegion', models.DO_NOTHING, related_name='playerplayer_residency_set', blank=True, null=True)
    arrival = models.DateTimeField()
    destination = models.ForeignKey('RegionRegion', models.DO_NOTHING, related_name='playerplayer_destination_set', blank=True, null=True)
    party = models.ForeignKey(PartyParty, models.DO_NOTHING, blank=True, null=True)
    party_post = models.ForeignKey(PartyPartyposition, models.DO_NOTHING, blank=True, null=True)
    chat_ban = models.BooleanField()
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)
    last_top = models.IntegerField(blank=True, null=True)
    natural_refill = models.DateTimeField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    energy_consumption = models.IntegerField()
    paid_consumption = models.IntegerField()
    paid_sum = models.IntegerField()
    endurance = models.IntegerField()
    knowledge = models.IntegerField()
    power = models.IntegerField()
    premium = models.DateTimeField()
    cards_count = models.IntegerField()
    daily_fin = models.BooleanField()
    reason = models.TextField(blank=True, null=True)
    educated = models.BooleanField()
    articles_ban = models.BooleanField()
    fingerprint = models.CharField(max_length=50)
    utm_campaign = models.CharField(max_length=50)
    utm_content = models.CharField(max_length=50)
    utm_medium = models.CharField(max_length=50)
    utm_source = models.CharField(max_length=50)
    utm_term = models.CharField(max_length=50)
    image_33 = models.CharField(max_length=100, blank=True, null=True)
    image_75 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_player'


class PlayerPlayerregionalexpense(models.Model):
    energy_consumption = models.IntegerField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING)
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'player_playerregionalexpense'


class PlayerPlayersettings(models.Model):
    color_back = models.CharField(max_length=6)
    color_block = models.CharField(max_length=6)
    color_text = models.CharField(max_length=6)
    color_acct = models.CharField(max_length=6)
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING)
    language = models.CharField(max_length=7, blank=True, null=True)
    party_back = models.BooleanField()
    full_auto = models.BooleanField()
    wiki_hide = models.BooleanField()
    captcha_ans = models.IntegerField()
    captcha_date = models.DateTimeField()
    freeze_counts = models.IntegerField()
    last_checkin_date = models.DateField(blank=True, null=True)
    streak_days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_playersettings'


class PlayerPremlog(models.Model):
    dtime = models.DateTimeField()
    days = models.BigIntegerField()
    activity_txt = models.CharField(max_length=7, blank=True, null=True)
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_premlog'


class PlayerRatereward(models.Model):
    nickname = models.CharField(max_length=50)
    dtime = models.DateTimeField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_ratereward'


class PlayerSkilltraining(models.Model):
    dtime = models.DateTimeField()
    skill = models.CharField(max_length=20, blank=True, null=True)
    end_dtime = models.DateTimeField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)
    plan_dtime = models.DateTimeField()
    boosts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_skilltraining'


class PlayerTestlog(models.Model):
    dtime = models.DateTimeField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_testlog'


class PlayerTestpointusage(models.Model):
    dtime = models.DateTimeField()
    count = models.IntegerField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'player_testpointusage'


class PlayerWildpasslog(models.Model):
    dtime = models.DateTimeField()
    count = models.BigIntegerField()
    activity_txt = models.CharField(max_length=7, blank=True, null=True)
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_wildpasslog'


class PollsPoll(models.Model):
    header = models.CharField(max_length=100)
    poll_dtime = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'polls_poll'


class PollsVariant(models.Model):
    text = models.CharField(max_length=100)
    poll = models.ForeignKey(PollsPoll, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'polls_variant'


class PollsVariantVotesPro(models.Model):
    variant = models.ForeignKey(PollsVariant, models.DO_NOTHING)
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_variant_votes_pro'
        unique_together = (('variant', 'player'),)


class RegionDefences(models.Model):
    level = models.IntegerField()
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'region_defences'


class RegionFossils(models.Model):
    percent = models.IntegerField()
    good = models.ForeignKey('StorageGood', models.DO_NOTHING)
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'region_fossils'


class RegionHospital(models.Model):
    level = models.IntegerField()
    top = models.IntegerField()
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'region_hospital'


class RegionInfrastructure(models.Model):
    level = models.IntegerField()
    top = models.IntegerField()
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'region_infrastructure'


class RegionMapshape(models.Model):
    shape = models.TextField()
    zoom = models.IntegerField()
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'region_mapshape'


class RegionMovement(models.Model):
    dtime = models.DateTimeField()
    arrival = models.ForeignKey('RegionRegion', models.DO_NOTHING, blank=True, null=True)
    departure = models.ForeignKey('RegionRegion', models.DO_NOTHING, related_name='regionmovement_departure_set', blank=True, null=True)
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region_movement'


class RegionNeighbours(models.Model):
    region_1 = models.ForeignKey('RegionRegion', models.DO_NOTHING, blank=True, null=True)
    region_2 = models.ForeignKey('RegionRegion', models.DO_NOTHING, related_name='regionneighbours_region_2_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region_neighbours'


class RegionPlane(models.Model):
    in_use = models.BooleanField()
    plane = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)
    nickname = models.CharField(max_length=25)
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'region_plane'


class RegionPowerplant(models.Model):
    level = models.IntegerField()
    region = models.ForeignKey('RegionRegion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'region_powerplant'


class RegionRegion(models.Model):
    region_name = models.CharField(max_length=50, blank=True, null=True)
    coal_proc = models.IntegerField()
    iron_proc = models.IntegerField()
    bauxite_proc = models.IntegerField()
    ore_cap = models.DecimalField(max_digits=5, decimal_places=2)
    ore_has = models.DecimalField(max_digits=5, decimal_places=2)
    oil_cap = models.DecimalField(max_digits=5, decimal_places=2)
    oil_has = models.DecimalField(max_digits=5, decimal_places=2)
    oil_type = models.CharField(max_length=10)
    gold_cap = models.DecimalField(max_digits=5, decimal_places=2)
    gold_has = models.DecimalField(max_digits=5, decimal_places=2)
    east = models.DecimalField(max_digits=5, decimal_places=2)
    is_east = models.BooleanField()
    is_north = models.BooleanField()
    north = models.DecimalField(max_digits=5, decimal_places=2)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    state = models.ForeignKey('StateState', models.DO_NOTHING, blank=True, null=True)
    is_off = models.BooleanField()
    cash_tax = models.DecimalField(max_digits=5, decimal_places=2)
    oil_tax = models.DecimalField(max_digits=5, decimal_places=2)
    ore_tax = models.DecimalField(max_digits=5, decimal_places=2)
    trade_tax = models.DecimalField(max_digits=5, decimal_places=2)
    gold_depletion = models.DecimalField(max_digits=5, decimal_places=2)
    oil_depletion = models.DecimalField(max_digits=5, decimal_places=2)
    ore_depletion = models.DecimalField(max_digits=5, decimal_places=2)
    on_map_id = models.CharField(max_length=50)
    oil_mark = models.ForeignKey('StorageGood', models.DO_NOTHING, blank=True, null=True)
    peace_date = models.DateTimeField()
    limit_id = models.IntegerField()
    region_name_az = models.CharField(max_length=50, blank=True, null=True)
    region_name_be = models.CharField(max_length=50, blank=True, null=True)
    region_name_de = models.CharField(max_length=50, blank=True, null=True)
    region_name_en = models.CharField(max_length=50, blank=True, null=True)
    region_name_es = models.CharField(max_length=50, blank=True, null=True)
    region_name_ind = models.CharField(max_length=50, blank=True, null=True)
    region_name_lv = models.CharField(max_length=50, blank=True, null=True)
    region_name_pl = models.CharField(max_length=50, blank=True, null=True)
    region_name_pt_br = models.CharField(max_length=50, blank=True, null=True)
    region_name_ru = models.CharField(max_length=50, blank=True, null=True)
    region_name_tr = models.CharField(max_length=50, blank=True, null=True)
    region_name_uk = models.CharField(max_length=50, blank=True, null=True)
    joined_since = models.DateTimeField()
    region_name_fr = models.CharField(max_length=50, blank=True, null=True)
    region_name_it = models.CharField(max_length=50, blank=True, null=True)
    region_name_sr = models.CharField(max_length=50, blank=True, null=True)
    region_name_hy = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'region_region'


class RegionRegionTerrain(models.Model):
    region = models.ForeignKey(RegionRegion, models.DO_NOTHING)
    terrain = models.ForeignKey('RegionTerrain', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'region_region_terrain'
        unique_together = (('region', 'terrain'),)


class RegionSpawn(models.Model):
    code = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'region_spawn'


class RegionSpawnRegions(models.Model):
    spawn = models.ForeignKey(RegionSpawn, models.DO_NOTHING)
    region = models.ForeignKey(RegionRegion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'region_spawn_regions'
        unique_together = (('spawn', 'region'),)


class RegionTerrain(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region_terrain'


class RegionTerrainmodifier(models.Model):
    modifier = models.DecimalField(max_digits=5, decimal_places=2)
    terrain = models.ForeignKey(RegionTerrain, models.DO_NOTHING)
    unit = models.ForeignKey('WarUnit', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'region_terrainmodifier'


class Rewards(models.Model):
    provider = models.CharField(max_length=255, blank=True, null=True)
    uid = models.CharField(max_length=255, blank=True, null=True)
    premium = models.DateTimeField(blank=True, null=True)
    cards_count = models.IntegerField(blank=True, null=True)
    borders_id = models.CharField(max_length=255, blank=True, null=True)
    packs_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rewards'


class SilkProfile(models.Model):
    name = models.CharField(max_length=300)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    time_taken = models.FloatField(blank=True, null=True)
    file_path = models.CharField(max_length=300)
    line_num = models.IntegerField(blank=True, null=True)
    end_line_num = models.IntegerField(blank=True, null=True)
    func_name = models.CharField(max_length=300)
    exception_raised = models.BooleanField()
    dynamic = models.BooleanField()
    request = models.ForeignKey('SilkRequest', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'silk_profile'


class SilkProfileQueries(models.Model):
    profile = models.ForeignKey(SilkProfile, models.DO_NOTHING)
    sqlquery = models.ForeignKey('SilkSqlquery', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'silk_profile_queries'
        unique_together = (('profile', 'sqlquery'),)


class SilkRequest(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    path = models.CharField(max_length=190)
    query_params = models.TextField()
    raw_body = models.TextField()
    body = models.TextField()
    method = models.CharField(max_length=10)
    start_time = models.DateTimeField()
    view_name = models.CharField(max_length=190, blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    time_taken = models.FloatField(blank=True, null=True)
    encoded_headers = models.TextField()
    meta_time = models.FloatField(blank=True, null=True)
    meta_num_queries = models.IntegerField(blank=True, null=True)
    meta_time_spent_queries = models.FloatField(blank=True, null=True)
    pyprofile = models.TextField()
    num_sql_queries = models.IntegerField()
    prof_file = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'silk_request'


class SilkResponse(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    status_code = models.IntegerField()
    raw_body = models.TextField()
    body = models.TextField()
    encoded_headers = models.TextField()
    request = models.OneToOneField(SilkRequest, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'silk_response'


class SilkSqlquery(models.Model):
    query = models.TextField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    time_taken = models.FloatField(blank=True, null=True)
    traceback = models.TextField()
    request = models.ForeignKey(SilkRequest, models.DO_NOTHING, blank=True, null=True)
    identifier = models.IntegerField()
    analysis = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'silk_sqlquery'


class SkillBiochemistry(models.Model):
    level = models.IntegerField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill_biochemistry'


class SkillCoherence(models.Model):
    level = models.IntegerField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill_coherence'


class SkillExcavation(models.Model):
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skill_excavation'


class SkillFracturing(models.Model):
    level = models.IntegerField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill_fracturing'


class SkillMilitaryproduction(models.Model):
    level = models.IntegerField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill_militaryproduction'


class SkillScouting(models.Model):
    level = models.IntegerField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill_scouting'


class SkillStandardization(models.Model):
    level = models.IntegerField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill_standardization'


class SkillTrophyengineering(models.Model):
    level = models.IntegerField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill_trophyengineering'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.BooleanField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    token = models.CharField(max_length=32)
    next_step = models.SmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class StateBulletin(models.Model):
    party = models.ForeignKey(PartyParty, models.DO_NOTHING)
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING)
    voting = models.ForeignKey('StateParliamentvoting', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'state_bulletin'


class StateCapital(models.Model):
    region = models.ForeignKey(RegionRegion, models.DO_NOTHING, blank=True, null=True)
    state = models.OneToOneField('StateState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'state_capital'


class StateDeputymandate(models.Model):
    parliament = models.ForeignKey('StateParliament', models.DO_NOTHING)
    party = models.ForeignKey(PartyParty, models.DO_NOTHING, blank=True, null=True)
    player = models.OneToOneField(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)
    is_president = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'state_deputymandate'


class StateParliament(models.Model):
    size = models.IntegerField()
    state = models.OneToOneField('StateState', models.DO_NOTHING)
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)
    elections_day = models.IntegerField()
    foundation_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_parliament'


class StateParliamentparty(models.Model):
    seats = models.IntegerField()
    parliament = models.ForeignKey(StateParliament, models.DO_NOTHING)
    party = models.OneToOneField(PartyParty, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'state_parliamentparty'


class StateParliamentvoting(models.Model):
    running = models.BooleanField()
    voting_start = models.DateTimeField()
    voting_end = models.DateTimeField()
    parliament = models.ForeignKey(StateParliament, models.DO_NOTHING)
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_parliamentvoting'


class StateState(models.Model):
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=6)
    foundation_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=15)
    deleted = models.BooleanField()
    cash_tax = models.DecimalField(max_digits=5, decimal_places=2)
    oil_tax = models.DecimalField(max_digits=5, decimal_places=2)
    ore_tax = models.DecimalField(max_digits=5, decimal_places=2)
    trade_tax = models.DecimalField(max_digits=5, decimal_places=2)
    residency = models.CharField(max_length=5)
    message = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'state_state'


class StateTreasury(models.Model):
    steel = models.IntegerField()
    region = models.ForeignKey(RegionRegion, models.DO_NOTHING, blank=True, null=True)
    state = models.OneToOneField(StateState, models.DO_NOTHING)
    aluminium = models.IntegerField()
    antitank = models.IntegerField()
    bauxite = models.IntegerField()
    brent_oil = models.IntegerField()
    cash = models.BigIntegerField()
    coal = models.IntegerField()
    deleted = models.BooleanField()
    diesel = models.IntegerField()
    gas = models.IntegerField()
    iron = models.IntegerField()
    jet = models.IntegerField()
    pzrk = models.IntegerField()
    station = models.IntegerField()
    tank = models.IntegerField()
    urals_oil = models.IntegerField()
    wti_oil = models.IntegerField()
    rifle = models.IntegerField()
    ifv = models.IntegerField()
    medical = models.IntegerField()
    plastic = models.IntegerField()
    actualize_dtime = models.DateTimeField(blank=True, null=True)
    power_actualize = models.DateTimeField(blank=True, null=True)
    power_on = models.BooleanField()
    drone = models.IntegerField()
    drilling = models.IntegerField()
    residency_id = models.CharField(max_length=150, blank=True, null=True)
    mines = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'state_treasury'


class StateTreasurylock(models.Model):
    lock_good = models.ForeignKey('StorageGood', models.DO_NOTHING, blank=True, null=True)
    lock_count = models.BigIntegerField()
    deleted = models.BooleanField()
    lock_treasury = models.ForeignKey(StateTreasury, models.DO_NOTHING)
    cash = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'state_treasurylock'


class StateTreasurystock(models.Model):
    stock = models.IntegerField()
    good = models.ForeignKey('StorageGood', models.DO_NOTHING)
    treasury = models.ForeignKey(StateTreasury, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'state_treasurystock'


class StorageAuctionbet(models.Model):
    price = models.IntegerField()
    deleted = models.BooleanField()
    auction_lot = models.ForeignKey('StorageAuctionlot', models.DO_NOTHING)
    good_lock = models.ForeignKey('StorageGoodlock', models.DO_NOTHING)
    dtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'storage_auctionbet'


class StorageAuctionlot(models.Model):
    count = models.IntegerField()
    start_price = models.IntegerField()
    deleted = models.BooleanField()
    auction = models.ForeignKey('StorageBuyauction', models.DO_NOTHING)
    win_storage = models.ForeignKey('StorageStorage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_auctionlot'


class StorageBuyauction(models.Model):
    create_date = models.DateTimeField(blank=True, null=True)
    accept_date = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField()
    treasury_lock = models.ForeignKey(StateTreasurylock, models.DO_NOTHING)
    good = models.ForeignKey('StorageGood', models.DO_NOTHING, blank=True, null=True)
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)
    extensions = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'storage_buyauction'


class StorageCache(models.Model):
    deleted = models.BooleanField()
    owner = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)
    region = models.ForeignKey(RegionRegion, models.DO_NOTHING, blank=True, null=True)
    rebel = models.ForeignKey('WarRebel', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_cache'
        unique_together = (('owner', 'region'),)


class StorageCachestock(models.Model):
    stock = models.IntegerField()
    cache = models.ForeignKey(StorageCache, models.DO_NOTHING, blank=True, null=True)
    good = models.ForeignKey('StorageGood', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'storage_cachestock'


class StorageCashlock(models.Model):
    lock_cash = models.BigIntegerField()
    deleted = models.BooleanField()
    lock_player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING)
    lock_offer = models.ForeignKey('StorageTradeoffer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'storage_cashlock'


class StorageDestroy(models.Model):
    dtime = models.DateTimeField()
    coal = models.IntegerField()
    iron = models.IntegerField()
    bauxite = models.IntegerField()
    wti_oil = models.IntegerField()
    brent_oil = models.IntegerField()
    urals_oil = models.IntegerField()
    gas = models.IntegerField()
    diesel = models.IntegerField()
    steel = models.IntegerField()
    aluminium = models.IntegerField()
    tank = models.IntegerField()
    jet = models.IntegerField()
    station = models.IntegerField()
    pzrk = models.IntegerField()
    antitank = models.IntegerField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)
    storage_from = models.ForeignKey('StorageStorage', models.DO_NOTHING, blank=True, null=True)
    rifle = models.IntegerField()
    ifv = models.IntegerField()
    medical = models.IntegerField()
    plastic = models.IntegerField()
    drone = models.IntegerField()
    drilling = models.IntegerField()
    mines = models.IntegerField()
    count = models.IntegerField()
    good = models.ForeignKey('StorageGood', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_destroy'


class StorageGood(models.Model):
    name = models.CharField(max_length=30)
    name_ru = models.CharField(max_length=30, blank=True, null=True)
    name_en = models.CharField(max_length=30, blank=True, null=True)
    name_de = models.CharField(max_length=30, blank=True, null=True)
    name_be = models.CharField(max_length=30, blank=True, null=True)
    name_es = models.CharField(max_length=30, blank=True, null=True)
    name_pl = models.CharField(max_length=30, blank=True, null=True)
    name_uk = models.CharField(max_length=30, blank=True, null=True)
    name_tr = models.CharField(max_length=30, blank=True, null=True)
    name_ind = models.CharField(max_length=30, blank=True, null=True)
    name_lv = models.CharField(max_length=30, blank=True, null=True)
    name_pt_br = models.CharField(max_length=30, blank=True, null=True)
    size = models.CharField(max_length=6)
    volume = models.FloatField()
    name_az = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=10)
    name_fr = models.CharField(max_length=30, blank=True, null=True)
    name_it = models.CharField(max_length=30, blank=True, null=True)
    name_sr = models.CharField(max_length=30, blank=True, null=True)
    name_hy = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_good'


class StorageGoodlock(models.Model):
    lock_good = models.ForeignKey(StorageGood, models.DO_NOTHING)
    lock_count = models.BigIntegerField()
    deleted = models.BooleanField()
    lock_storage = models.ForeignKey('StorageStorage', models.DO_NOTHING)
    lock_offer = models.ForeignKey('StorageTradeoffer', models.DO_NOTHING, blank=True, null=True)
    old_good = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_goodlock'


class StorageLootboxcoauthor(models.Model):
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_lootboxcoauthor'


class StorageLootboxprize(models.Model):
    plane = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)
    deleted = models.BooleanField()
    replaced = models.BooleanField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'storage_lootboxprize'


class StorageStock(models.Model):
    stock = models.IntegerField()
    good = models.ForeignKey(StorageGood, models.DO_NOTHING)
    storage = models.ForeignKey('StorageStorage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_stock'


class StorageStorage(models.Model):
    cash = models.BigIntegerField()
    owner = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)
    region = models.ForeignKey(RegionRegion, models.DO_NOTHING, blank=True, null=True)
    deleted = models.BooleanField()
    was_moved = models.BooleanField()
    level = models.IntegerField()
    large_cap = models.IntegerField()
    medium_cap = models.IntegerField()
    small_cap = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'storage_storage'
        unique_together = (('owner', 'region'),)


class StorageTradeoffer(models.Model):
    initial_volume = models.BigIntegerField()
    count = models.BigIntegerField()
    price = models.BigIntegerField()
    cost = models.BigIntegerField()
    cost_count = models.BigIntegerField()
    type = models.CharField(max_length=4)
    view_type = models.CharField(max_length=6)
    old_good = models.CharField(max_length=10)
    create_date = models.DateTimeField(blank=True, null=True)
    accept_date = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField()
    owner_storage = models.ForeignKey(StorageStorage, models.DO_NOTHING, blank=True, null=True)
    offer_good = models.ForeignKey(StorageGood, models.DO_NOTHING, blank=True, null=True)
    wild_pass = models.BooleanField()
    tax = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'storage_tradeoffer'


class StorageTradeofferAccepters(models.Model):
    tradeoffer = models.ForeignKey(StorageTradeoffer, models.DO_NOTHING)
    tradinglog = models.ForeignKey('StorageTradinglog', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'storage_tradeoffer_accepters'
        unique_together = (('tradeoffer', 'tradinglog'),)


class StorageTradinglog(models.Model):
    dtime = models.DateTimeField()
    cash_value = models.BigIntegerField()
    good_value = models.BigIntegerField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)
    delivery_value = models.BigIntegerField()
    player_storage = models.ForeignKey(StorageStorage, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_tradinglog'


class StorageTransport(models.Model):
    dtime = models.DateTimeField()
    total_vol = models.IntegerField()
    coal = models.IntegerField()
    coal_vol = models.IntegerField()
    iron = models.IntegerField()
    iron_vol = models.IntegerField()
    bauxite = models.IntegerField()
    bauxite_vol = models.IntegerField()
    wti_oil = models.IntegerField()
    wti_oil_vol = models.IntegerField()
    brent_oil = models.IntegerField()
    brent_oil_vol = models.IntegerField()
    urals_oil = models.IntegerField()
    urals_oil_vol = models.IntegerField()
    gas = models.IntegerField()
    gas_vol = models.IntegerField()
    diesel = models.IntegerField()
    diesel_vol = models.IntegerField()
    steel = models.IntegerField()
    steel_vol = models.IntegerField()
    aluminium = models.IntegerField()
    aluminium_vol = models.IntegerField()
    tank = models.IntegerField()
    tank_vol = models.IntegerField()
    jet = models.IntegerField()
    jet_vol = models.IntegerField()
    station = models.IntegerField()
    station_vol = models.IntegerField()
    pzrk = models.IntegerField()
    pzrk_vol = models.IntegerField()
    antitank = models.IntegerField()
    antitank_vol = models.IntegerField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)
    storage_from = models.ForeignKey(StorageStorage, models.DO_NOTHING, blank=True, null=True)
    storage_to = models.ForeignKey(StorageStorage, models.DO_NOTHING, related_name='storagetransport_storage_to_set', blank=True, null=True)
    delivery_value = models.BigIntegerField()
    rifle = models.IntegerField()
    rifle_vol = models.IntegerField()
    ifv = models.IntegerField()
    ifv_vol = models.IntegerField()
    medical = models.IntegerField()
    medical_vol = models.IntegerField()
    plastic = models.IntegerField()
    plastic_vol = models.IntegerField()
    drone = models.IntegerField()
    drone_vol = models.IntegerField()
    mines = models.IntegerField()
    mines_vol = models.IntegerField()
    count = models.IntegerField()
    good = models.ForeignKey(StorageGood, models.DO_NOTHING, blank=True, null=True)
    cache_from = models.ForeignKey(StorageCache, models.DO_NOTHING, blank=True, null=True)
    cache_to = models.ForeignKey(StorageCache, models.DO_NOTHING, related_name='storagetransport_cache_to_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_transport'


class WarAutowar(models.Model):
    dtime = models.DateTimeField()
    object_id = models.IntegerField()
    war_side = models.CharField(max_length=3)
    dmg_balance = models.CharField(max_length=4)
    dmg_points = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING, blank=True, null=True)
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)
    source_ct = models.ForeignKey(DjangoContentType, models.DO_NOTHING, related_name='warautowar_source_ct_set')
    source_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'war_autowar'


class WarAutowarsquad(models.Model):
    count = models.IntegerField()
    auto_war = models.ForeignKey(WarAutowar, models.DO_NOTHING, blank=True, null=True)
    unit = models.ForeignKey('WarUnit', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'war_autowarsquad'


class WarEventwar(models.Model):
    running = models.BooleanField()
    start_time = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField()
    hq_points = models.BigIntegerField()
    agr_region = models.ForeignKey(RegionRegion, models.DO_NOTHING, blank=True, null=True)
    def_region = models.ForeignKey(RegionRegion, models.DO_NOTHING, related_name='wareventwar_def_region_set', blank=True, null=True)
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    round = models.IntegerField()
    graph = models.TextField(blank=True, null=True)
    end_task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, related_name='wareventwar_end_task_set', blank=True, null=True)
    defence_points = models.BigIntegerField()
    side_limit = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'war_eventwar'


class WarGroundwar(models.Model):
    running = models.BooleanField()
    round = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    graph = models.TextField(blank=True, null=True)
    deleted = models.BooleanField()
    hq_points = models.BigIntegerField()
    agr_region = models.ForeignKey(RegionRegion, models.DO_NOTHING, blank=True, null=True)
    def_region = models.ForeignKey(RegionRegion, models.DO_NOTHING, related_name='wargroundwar_def_region_set', blank=True, null=True)
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)
    end_task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, related_name='wargroundwar_end_task_set', blank=True, null=True)
    defence_points = models.BigIntegerField()
    side_limit = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'war_groundwar'


class WarMartial(models.Model):
    active = models.BooleanField()
    days_left = models.IntegerField()
    active_end = models.DateTimeField(blank=True, null=True)
    region = models.ForeignKey(RegionRegion, models.DO_NOTHING)
    state = models.ForeignKey(StateState, models.DO_NOTHING)
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'war_martial'


class WarPlayerdamage(models.Model):
    object_id = models.IntegerField()
    damage = models.IntegerField()
    energy = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING)
    side = models.CharField(max_length=3)
    hide = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'war_playerdamage'


class WarRebel(models.Model):
    resident = models.BooleanField()
    player = models.ForeignKey(PlayerPlayer, models.DO_NOTHING)
    region = models.ForeignKey(RegionRegion, models.DO_NOTHING)
    deleted = models.BooleanField()
    dtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'war_rebel'


class WarRevolution(models.Model):
    defence_points = models.BigIntegerField()
    running = models.BooleanField()
    round = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    graph = models.TextField(blank=True, null=True)
    deleted = models.BooleanField()
    hq_points = models.BigIntegerField()
    agr_region = models.ForeignKey(RegionRegion, models.DO_NOTHING, blank=True, null=True)
    def_region = models.ForeignKey(RegionRegion, models.DO_NOTHING, related_name='warrevolution_def_region_set', blank=True, null=True)
    end_task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, blank=True, null=True)
    task = models.OneToOneField(DjangoCeleryBeatPeriodictask, models.DO_NOTHING, related_name='warrevolution_task_set', blank=True, null=True)
    side_limit = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'war_revolution'


class WarTestResults(models.Model):
    player_id = models.IntegerField(blank=True, null=True)
    total_damage = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    nickname = models.CharField(blank=True, null=True)
    username = models.CharField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    reward = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    rewarded = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'war_test_results'


class WarUnit(models.Model):
    damage = models.IntegerField()
    energy = models.IntegerField()
    good = models.ForeignKey(StorageGood, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'war_unit'


class WarWarside(models.Model):
    object_id = models.IntegerField()
    side = models.CharField(max_length=3)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'war_warside'
