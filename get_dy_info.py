import requests
import urllib.request

def get_url(url):
    """
    GET https://api3-normal-c-lf.amemv.com/aweme/v1/aweme/post/?source=0&max_cursor=0&sec_user_id=MS4wLjABAAAA8VRQ7AyGLXg6p841xpFHqoVMGQmlVrvPSQuYxX2VvoE&count=20&manifest_version_code=950&_rticket=1578902344152&app_type=normal&iid=98872770383&channel=huawei_1&device_type=LIO-AL00&language=zh&uuid=861118042473379&resolution=1176*2328&openudid=5c5d399b89ea47c9&update_version_code=9502&cdid=ba38f923-a708-4691-92a5-07f2ebd1ceed&os_api=29&dpi=480&oaid=ffaf56bb-ebbd-7b0c-33bf-ff5f79de7e0c&ac=wifi&device_id=69594287825&mcc_mnc=46000&os_version=10&version_code=950&app_name=aweme&version_name=9.5.0&device_brand=HUAWEI&ssmix=a&device_platform=android&aid=1128&ts=1578902341 HTTP/1.1
Host: api3-normal-c-lf.amemv.com
Connection: keep-alive
Cookie: odin_tt=82d0f74743ab0f5ef0d7b743ae9962eb677bd85571cdb9d4047be5d4031da7fe8498f55e835765b36373bae4f4a51cc3354052631b3d604d93d8bec0bc999ec1
X-SS-REQ-TICKET: 1578902344151
sdk-version: 1
X-SS-DP: 1128
x-tt-trace-id: 00-9de9d34a0a1034248ed1c59a15ff0468-9de9d34a0a103424-01
User-Agent: com.ss.android.ugc.aweme/950 (Linux; U; Android 10; zh_CN_#Hans; LIO-AL00; Build/HUAWEILIO-AL00; Cronet/77.0.3844.0)
Accept-Encoding: gzip, deflate
X-Khronos: 1578902344
X-Gorgon: 0401a0ca06048fda2aca18d258624fbb2e4bd81057d788be1ec6


HTTP/1.1 200 OK
Server: Tengine
Content-Type: application/json; charset=utf-8
Transfer-Encoding: chunked
Connection: keep-alive
Date: Mon, 13 Jan 2020 07:59:02 GMT
bd-tt-error-code: 0
status_code: 0
tt_stable: 1
x-tt-logid: 2020011315590101001203404922030A84
vary: Accept-Encoding
content-encoding: gzip
tt-idc-switch: 10000@20200112012
Access-Control-Expose-Headers: tt-idc-switch
server-timing: inner; dur=124
x-tt-trace-host: 01d7c7e87f4a795c92b162508f67f2f1ba611c412468b24f18c31575af4003f1b7e9f875f5954d656f2729a20555772313ddeddfa711b7f5b9517b4fc93ba7b76b2f9cd9a3a2e7aebf1a1b059ceadf4db8
x-tt-trace-tag: id=00;cdn-cache=miss
x-tt-trace-id: 00-9de9d34a0a1034248ed1c59a15ff0468-9de9d34a0a103424-01
Vary: Accept-Encoding
Via: cache13.cn927[143,0]
Timing-Allow-Origin: *
EagleId: 7b060cd515789023419232332e



    :param url:
    :return:
    """
    headers = {'user-agent': 'com.ss.android.ugc.aweme/950 (Linux; U; Android 10; zh_CN_#Hans; LIO-AL00; Build/HUAWEILIO-AL00; Cronet/77.0.3844.0)'}
    req = requests.get(url, headers=headers, verify=False)
    data = req.json()
    print(data)


if __name__ == "__main__":
    # get_url('https://api3-normal-c-lf.amemv.com/aweme/v1/user/following/list/?user_id=92619723838&sec_user_id=MS4wLjABAAAA7xdUo1GGP4UBfw9j0Hwwz32E_C3uc1YZKtVMLOLfruY&max_time=1578901650&count=20&offset=0&source_type=1&address_book_access=2&gps_access=1&manifest_version_code=950&_rticket=1578901653181&app_type=normal&iid=98872770383&channel=huawei_1&device_type=LIO-AL00&language=zh&uuid=861118042473379&resolution=1176*2328&openudid=5c5d399b89ea47c9&update_version_code=9502&cdid=ba38f923-a708-4691-92a5-07f2ebd1ceed&os_api=29&dpi=480&oaid=ffaf56bb-ebbd-7b0c-33bf-ff5f79de7e0c&ac=wifi&device_id=69594287825&mcc_mnc=46000&os_version=10&version_code=950&app_name=aweme&version_name=9.5.0&device_brand=HUAWEI&ssmix=a&device_platform=android&aid=1128&ts=1578901650')
    get_url("https://api3-normal-c-lf.amemv.com/aweme/v1/aweme/post/?source=0&max_cursor=0&sec_user_id=MS4wLjABAAAA8VRQ7AyGLXg6p841xpFHqoVMGQmlVrvPSQuYxX2VvoE&count=20&manifest_version_code=950&_rticket=1578902344152&app_type=normal&iid=98872770383&channel=huawei_1&device_type=LIO-AL00&language=zh&uuid=861118042473379&resolution=1176*2328&openudid=5c5d399b89ea47c9&update_version_code=9502&cdid=ba38f923-a708-4691-92a5-07f2ebd1ceed&os_api=29&dpi=480&oaid=ffaf56bb-ebbd-7b0c-33bf-ff5f79de7e0c&ac=wifi&device_id=69594287825&mcc_mnc=46000&os_version=10&version_code=950&app_name=aweme&version_name=9.5.0&device_brand=HUAWEI&ssmix=a&device_platform=android&aid=1128&ts=1578902341")
