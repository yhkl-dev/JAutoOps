import json
from pprint import pprint

from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from servers.models import ServerAliCloudInstanceModel
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.cvm.v20170312 import cvm_client, models

from .models import Resource


def create_client(access_key: str, access_secret: str, endpoint: str) -> Ecs20140526Client:
    config = open_api_models.Config(
        access_key_id=access_key,
        access_key_secret=access_secret
    )
    config.endpoint = endpoint
    return Ecs20140526Client(config)


def get_instance_list(access_key: str, access_secret: str, resource: str, endpoint='ecs-cn-hangzhou.aliyuncs.com'):
    client = create_client(access_key, access_secret, endpoint=endpoint)
    region_list = get_region_list(client)
    for r in region_list:
        if r.get('RegionId').startswith("cn"):
            get_aliyun_resource_instance_info(access_key, access_secret, resource, r.get('RegionId'),
                                              r.get('RegionEndpoint'))

    return True


def get_aliyun_resource_instance_info(access_key: str, access_secret: str, resource: str, region_id: str,
                                      region_endpoint: str) -> bool:
    client = create_client(access_key, access_secret, endpoint=region_endpoint)

    describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
        region_id=region_id
    )
    res = client.describe_instances(describe_instances_request)
    instance_list = res.body.to_map().get('Instances').get('Instance')

    if instance_list is not None:
        for i in instance_list:
            try:
                instance_to_server(i, resource)
            except Exception as e:
                print(e)
                continue
    return True


def get_region_list(client):
    describe_regions_request = ecs_20140526_models.DescribeRegionsRequest()
    res = client.describe_regions(describe_regions_request)
    region_list = res.body.to_map().get('Regions').get('Region')
    return region_list


def get_tencent_instance_info(access_key: str, access_secret: str, resource: str):
    try:
        cred = credential.Credential(access_key, access_secret)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cvm.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = cvm_client.CvmClient(cred, "ap-beijing", clientProfile)

        req = models.DescribeInstancesRequest()
        params = {

        }
        req.from_json_string(json.dumps(params))
        resp = client.DescribeInstances(req)
        x = json.loads(resp.to_json_string())
        for data in x.get("InstanceSet"):
            m = {
                'SerialNumber': data.get("Uuid"),
                'CreationTime': data.get("CreatedTime"),
                'ExpiredTime': data.get("ExpiredTime"),
                'OSNameEn': data.get("OsName"),
                'HostName': data.get("Uuid"),
                'OSType': 'linux' if data.get("OsName").startswith('Cen') else 'windows',
                'PublicIpAddress': {
                    'IpAddress': data.get("PublicIpAddresses"),
                },
                'Cpu': data.get("CPU"),
                'Memory': data.get("Memory"),
                'RegionId': data.get("Placement").get("Zone"),
                'Status': data.get("InstanceState"),
                'InstanceName': data.get("InstanceName")
            }
            instance_to_server(m, resource)

    except TencentCloudSDKException as err:
        print(err)




def instance_to_server(instance_info, resource):
    obj, created = ServerAliCloudInstanceModel.objects.update_or_create(SerialNumber=instance_info.get("SerialNumber"))
    if created:
        obj.InstanceName = instance_info.get("InstanceName")
        obj.CreationTime = instance_info.get("CreationTime")
        obj.Status = instance_info.get("Status")
        obj.HostName = instance_info.get("HostName")
        obj.IpAddress = '/'.join(instance_info.get("PublicIpAddress").get('IpAddress'))
        obj.OSNameEn = instance_info.get("OSNameEn")
        obj.OSType = instance_info.get("OSType")
        obj.InstanceNetworkType = instance_info.get("InstanceNetworkType")
        obj.Memory = instance_info.get("Memory")
        obj.Cpu = instance_info.get("Cpu")
        obj.ExpiredTime = instance_info.get("ExpiredTime")
        obj.StartTime = instance_info.get("StartTime")
        obj.RegionId = instance_info.get("RegionId")
        obj.resource_name = Resource.objects.get(id=resource)
        obj.save()
    else:
        obj.SerialNumber = instance_info.get("SerialNumber")
        obj.InstanceName = instance_info.get("InstanceName")
        obj.CreationTime = instance_info.get("CreationTime")
        obj.Status = instance_info.get("Status").lower() if instance_info.get("Status") is not None else None
        obj.HostName = instance_info.get("HostName")
        obj.IpAddress = '/'.join(instance_info.get("PublicIpAddress").get('IpAddress'))
        obj.OSNameEn = instance_info.get("OSNameEn")
        obj.OSType = instance_info.get("OSType")
        obj.InstanceNetworkType = instance_info.get("InstanceNetworkType")
        obj.Memory = instance_info.get("Memory")
        obj.Cpu = instance_info.get("Cpu")
        obj.ExpiredTime = instance_info.get("ExpiredTime")
        obj.StartTime = instance_info.get("StartTime")
        obj.RegionId = instance_info.get("RegionId")
        obj.resource_name = Resource.objects.get(id=resource)
        obj.save()
