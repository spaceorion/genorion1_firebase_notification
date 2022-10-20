from django.db.models import fields
from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from drf_braces.serializers.form_serializer import FormSerializer
from myapp.forms import UserRegisterForm, SubUserRegisterForm
from myapp.models import SomeModel, oneyeardata,place,floor,flat,room,device,deviceStatus,pinschedule,emergencyNumber,sensors,ssidPassword,pinName, threeyears,userimages,deviceIpAddress,subuseraccess,subuserplace,tempuser,tempUserVerification,otptemplogin, energy, oneHourEnergy,FirebaseDetails,scene,scene_devices
import time
##
class Scenedevice_Serializer(serializers.ModelSerializer):
    starttime  = serializers.SerializerMethodField('epoch')

    def epoch(self, obj):
        """ Return epoch time for a datetime object or ``None``"""
        try:
            return int(time.mktime(obj.time.timetuple()))
        except (AttributeError, TypeError):
            return None

    class Meta:
        model = scene_devices
        fields =  ('starttime','scene_id','scenedevices_id','d_id','scene_device_type','status',)

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'

class userlogingetdataSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','first_name','last_name')

class emailSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)

class firstnameSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name',)

class subuseremailSerializers(serializers.ModelSerializer):
    class Meta:
        model = subuseraccess
        fields = ('emailtest',)

class user_register(FormSerializer):
    class Meta(object):
        form = UserRegisterForm

class subuser_register(FormSerializer):
    class Meta(object):
        form = SubUserRegisterForm

class placeSerializers(serializers.ModelSerializer):
    class Meta:
        model = place
        fields = '__all__'
        ##
class sceneSerializers(serializers.ModelSerializer):
    class Meta:
        model = scene
        fields = '__all__'

class placenameSerializers(serializers.ModelSerializer):
    class Meta:
        model = place
        fields = ('p_type','p_id')


class floorSerializers(serializers.ModelSerializer):
    class Meta:
        model = floor
        # fields = ('f_id', 'f_name')
        fields = '__all__'

class floornameSerializers(serializers.ModelSerializer):
    class Meta:
        model = floor
        fields = ('f_name','f_id')

class flatSerializers(serializers.ModelSerializer):
    class Meta:
        model = flat
        # fields = ('f_id', 'f_name')
        fields = '__all__'

class flatnameSerializers(serializers.ModelSerializer):
    class Meta:
        model = flat
        fields = ('flt_name','flt_id')


class roomSerializers(serializers.ModelSerializer):
    class Meta:
        model = room
        fields = '__all__'

class roomnameSerializers(serializers.ModelSerializer):
    class Meta:
        model = room
        fields = ('r_name','r_id')


class deviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = device
        fields = '__all__'



class deviceStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = deviceStatus
        fields = '__all__'

class pinnamesSerializers(serializers.ModelSerializer):
    class Meta:
        model = pinName
        fields = '__all__'

class pinscheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = pinschedule
        fields = '__all__'

class pinscheduleTimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = pinschedule
        fields = ('id','d_id','date1','timing1')

class emernumberSerializers(serializers.ModelSerializer):
    class Meta:
        model = emergencyNumber
        fields = '__all__'


class sensorSerializers(serializers.ModelSerializer):
    class Meta:
        model = sensors
        fields = '__all__'


class ssidPasswordSerializers(serializers.ModelSerializer):
    class Meta:
        model = ssidPassword
        fields = '__all__'

class userprofileimagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = userimages
        fields = '__all__'

class deviceipaddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = deviceIpAddress
        fields = '__all__'

class subuseraccessSerializers(serializers.ModelSerializer):
    class Meta:
        model = subuseraccess
        fields = '__all__'


class subuserplaceSerializers(serializers.ModelSerializer):
    class Meta:
        model = subuserplace
        fields = '__all__'

class subuserplacegetSerializers(serializers.ModelSerializer):
    class Meta:
        model = subuserplace
        fields = ('name','email', 'p_id',)

class otploginSerializers(serializers.ModelSerializer):
    class Meta:
        model = tempUserVerification
        fields = '__all__'


# class ValidatePhoneSendOTPSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = PhoneOTP
#         fields = '__all__'

class FirebaseSer(serializers.ModelSerializer):
    class Meta:
        model = FirebaseDetails
        fields = '__all__'
class tempuserregisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = tempuser
        fields= '__all__'

class dateasignSerializers(serializers.ModelSerializer):
    class Meta:
        model = tempuser
        fields= ('id','date','timing',)

class timeasignSerializers(serializers.ModelSerializer):
    class Meta:
        model = tempuser
        fields= ('timing',)


class otpfortampuserSerializers(serializers.ModelSerializer):
    class Meta:
        model = tempUserVerification
        fields = '__all__'

class otpuserloginSerializers(serializers.ModelSerializer):
    class Meta:
        model = otptemplogin
        fields = '__all__'

class testimageSerializers(serializers.ModelSerializer):
    class Meta:
        model = SomeModel
        fields = '__all__'


class energySerializers(serializers.ModelSerializer):
    class Meta:
        model = energy
        fields = '__all__'

class onehourenSerializers(serializers.ModelSerializer):
    class Meta:
        model = oneHourEnergy
        fields = '__all__'


class oneyearenSerializers(serializers.ModelSerializer):
    class Meta:
        model = oneyeardata
        fields = '__all__'    

class threeyearenSerializers(serializers.ModelSerializer):
    class Meta:
        model = threeyears
        fields = '__all__'     



# from .models import employees

# class employeesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = employees
#         fields = '__all__'
