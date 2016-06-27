from django.db import models
import datetime


class AddressSet(models.Model):
    as_id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, max_length=100)
    fqdn = models.CharField(blank=True, max_length=256)
    IP = models.GenericIPAddressField(unique=True, null=False)
    mask = models.GenericIPAddressField(null=False)
    port = models.CharField(null=False, max_length=5)

    def __str__(self):
        return self.name


class AddressBook(models.Model):
    ab_id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, max_length=100)
    description = models.CharField(blank=True, max_length=100)
    AddressSet = models.ForeignKey(AddressSet)

    def __str__(self):
        return self.name


class LTMRequest(models.Model):
    ltm_id = models.AutoField(primary_key=True)
    placehold_ip = models.CharField(max_length=128, blank=False, unique=True)
    port = models.IntegerField(blank=False)
    oneconnect = models.BooleanField(default=False)
    http_compression = models.BooleanField(default=False)
    requestlog = models.CharField(blank=True, max_length=256)
    loadbalance = models.CharField(blank=False, max_length=100)
    healthmon = models.CharField(blank=False, max_length=100)
    AddressSet = models.ManyToManyField(AddressSet)

    def __str__(self):
        return self.placehold_ip


class SSLRequest(models.Model):
    ssl_id = models.AutoField(primary_key=True)
    ssl_fqdn = models.CharField(blank=True, max_length=256)
    ssl_req = models.BooleanField(default=False)
    ssl_cipher = models.CharField(blank=True, max_length=100)
    mutauth = models.BooleanField(default=False, blank=True)
    datagroup = models.CharField(blank=True, max_length=100)
    ma_client = models.CharField(blank=True, max_length=100)
    ma_srv = models.CharField(blank=True, max_length=100)
    ma_client_srv = models.CharField(blank=True, max_length=100)


    def __int__(self):
        return self.ssl_id


class GTMRequest(models.Model):
    gtm_id = models.AutoField(primary_key=True)
    wide_ip = models.CharField(blank=True, max_length=100)
    mastersite = models.CharField(blank=True, max_length=100)
    failoverstate = models.CharField(blank=True, max_length=100)
    preferedbalance = models.CharField(blank=True, max_length=100)
    altbalance = models.CharField(blank=True, max_length=100)
    fallback = models.CharField(blank=True, max_length=100)
    AddressSet = models.ManyToManyField(AddressSet)

    def __str__(self):
        return self.wide_ip


class FirewallRequest(models.Model):
    fw_id = models.AutoField(primary_key=True)
    AddressSet = models.ForeignKey(AddressSet)
    service = models.CharField(blank=True, max_length=100)
    protocol = models.GenericIPAddressField()
    action = models.BooleanField(default=True)
    log = models.BooleanField(default=True)
    scheduled = models.BooleanField(default=False)
    schedule_date = models.DateField(default=datetime.datetime.today)
    rule_desc = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return str(self.fw_id)


class ApplicationRequest(models.Model):
    app_id = models.AutoField(primary_key=True)
    pre = models.CharField(blank=False, unique=True, max_length=100)
    app_name = models.CharField(blank=False, max_length=100)
    app_env = models.CharField(blank=False, max_length=100)
    compartment = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.app_name

class PERRequest(models.Model):
    per_id = models.IntegerField(primary_key=True, unique=True, blank=False)
    LTMRequest = models.ForeignKey(LTMRequest)
    SSLRequest = models.ForeignKey(SSLRequest)
    GTMRequest = models.ForeignKey(GTMRequest)
    FirewallRequest = models.ForeignKey(FirewallRequest)
    ApplicationRequest = models.ForeignKey(ApplicationRequest)

    def __str__(self):
        return str(self.per_id)