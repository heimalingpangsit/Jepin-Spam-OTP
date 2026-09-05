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
        'name': 'Royal Canin',
        'post_type': 'royal_canin',
        'number_fmt': fmt_plus,
        'success_on': ['SUCCESS']
    },
    {
        'name': 'Beli Rumah',
        'post_type': 'belirumahco',
        'number_fmt': fmt_plus,
        'success_on': ['success', 'otp', 'code']
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
        'name': 'Auto2000',
        'post_type': 'get',
        'url': 'https://auto2000.co.id/api/saphybris-proxy/v1/saphybris/astrapay/check-loyalty-program?phone={number}',
        'referer': 'https://auto2000.co.id/verifikasi-otp?source=login',
        'headers': {
            'Accept': 'application/json',
            'Authorization': 'Bearer HcAvKMgGqYIVW0fSNuHHHTZX2Jw',
            'Origin': 'https://auto2000.co.id',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'number_fmt': fmt_08,
        'success_on': ['success', 'true', 'status']
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
        'name': 'Sidemang Palembang',
        'post_type': 'json',
        'url': 'https://sidemang.palembang.go.id/api/users/register/send-otp',
        'referer': 'https://sidemang.palembang.go.id/register-otp/verify',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Origin': 'https://sidemang.palembang.go.id',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"phoneNumber":"{number}","email":"mdjazarqy@gmail.com","recaptchaToken":""}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true']
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
        'name': 'Erafone / Eraspace',
        'post_type': 'json',
        'url': 'https://jeanne.eraspace.com/customers/v2.1/otp/request',
        'referer': 'https://erafone.com/register',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'source': 'erafone',
            'Sms-Client': 'erafone',
            'Otp-Client': 'erafone',
            'Authorization': 'Basic Y3VzdGJhc2ljOk9MV2llWlVvQlA=',
            'Signature': 'b5306fe4da91bbd4d4564e1613856b62ecf026ba806858c9ea99c798e4c69b99',
            'Otp-Provider': 'whatsapp',
            'device-id': '57c66344-5d6a-4265-8029-072ff88577b9',
            'Platform': 'erafone-web',
            'Origin': 'https://erafone.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"identifier":"{number}","type":"identifier_validation"}',
        'number_fmt': fmt_nocode,
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
        'name': 'Fastwork Indonesia',
        'post_type': 'json',
        'url': 'https://api.fastwork.id/auth/v2/signup.sendVerificationCode',
        'referer': 'https://auth2.fastwork.id/',
        'headers': {
            'Content-Type': 'application/json',
            'X-Device-ID': '3af3b305-659d-4fc5-9c86-a19e01aeb700',
            'Origin': 'https://auth2.fastwork.id',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"phone_number":"{number}"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true']
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
        'name': 'Astra Daihatsu',
        'post_type': 'json',
        'url': 'https://www.astra-daihatsu.id/otp/whatsapp/generate',
        'referer': 'https://www.astra-daihatsu.id/register',
        'headers': {
            'CSRFToken': 'beff18d4-f339-43aa-bb93-5e5d3d894420',
            'Content-Type': 'application/json; charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://www.astra-daihatsu.id',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"phoneNo":"{number}"}',
        'number_fmt': fmt_nocode,
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
        'name': 'Watsons Indonesia',
        'post_type': 'json',
        'url': 'https://api.watsons.co.id/api/v2/wtcid/otpToken?formId=registrationOTPForm_Web3&lang=id&curr=IDR',
        'referer': 'https://www.watsons.co.id/id/register',
        'headers': {
            'Content-Type': 'application/json',
            'queue-target': 'https://www.watsons.co.id/id/register',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://www.watsons.co.id',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"uid":"","action":"GENERAL","countryCode":"62","target":"{number}","type":"WHATSAPP"}',
        'number_fmt': lambda p: p[1:] if p.startswith('0') else (p[2:] if p.startswith('62') else p),
        'success_on': ['success', 'true', 'token']
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
        'name': 'Ruparupa',
        'post_type': 'json',
        'url': 'https://wapi.ruparupa.com/v3/otp/generate',
        'referer': 'https://www.ruparupa.com/auth/otp-verification',
        'headers': {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Company-Name': 'ruparupa',
            'X-Frontend-Type': 'mobile',
            'user-platform': 'mobile',
            'b2b-type': 'non-b2b',
            'rr-sid': '7uQqL17885769131pK1JGWaae',
            'Origin': 'https://www.ruparupa.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"session_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lcl9pZCI6MCwiaWF0IjoxNzg4NTc2OTMxLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.1KACmejFdrWHxJKRdrt_u9r5871uZ11U_YN0TjMuH4g","target":"{number}","send_to":"whatsapp","intent":"register","action":"verify_phone"}',
        'number_fmt': fmt_plus,
        'success_on': ['success', 'true']
    },
        {
        'name': '99.co',
        'post_type': 'json',
        'url': 'https://www.99.co/id/api/biz/messaging/otp-events',
        'referer': 'https://www.99.co/id/account',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJFUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJybzJ6ZThOYkFNUW1QTlVVZFcwTjItNnE5bWNleHJHcHdFNS0xd3hQQWJzIn0.eyJleHAiOjE3ODg1Nzg3NTUsImlhdCI6MTc4ODU3NTE1NSwianRpIjoiYzRkZmY1MDYtODlkMS00Y2Y0LTk2Y2YtNjEwYjFlNTZlOTdkIiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay1pZC45OS5jby9yZWFsbXMvOTlpZC1wcm9kIiwic3ViIjoiNDA0YmQ0NzItNjIzOS00YTRhLTlmZTctZDkxYWRhYjkyNjZlIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiZnJvbnRlbmQtYXBwIiwic2Vzc2lvbl9zdGF0ZSI6Ijk2YmYzODM5LTkxM2ItNDczNi05NWM2LTI2NGI4OWI0MjA4MyIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsic2VsbGVyIiwidW1hX2F1dGhvcml6YXRpb24iLCJkZWZhdWx0LXJvbGVzLTk5aWQtcHJvZCIsImJ1eWVyIl19LCJzY29wZSI6InByb2ZpbGUtbWluaW1pemUgY29yZS11dWlkIGVtYWlsIiwic2lkIjoiOTZiZjM4MzktOTEzYi00NzM2LTk1YzYtMjY0Yjg5YjQyMDgzIiwiY29yZV91dWlkIjoiMDRlOTNiMmQtNTdmYy00M2U0LWJiMTgtNjJmYTI4YjNhYjg1IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJjb3JlX2NvbnN1bWVyX3V1aWQiOiIwMzljYjczMi1jNGJjLTRhN2EtOGQ3ZS1kMWJjZTMxYTg5YzMiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJnYW50ZW5rIiwiY29yZV9jdXN0b21lcl91dWlkIjoiOWFiYjIwZWEtZTU4MC00MzJmLWE1MDQtODIwNDcyYjViMDk2IiwiZW1haWwiOiJtZGphemFycXlAZ21haWwuY29tIn0.ot312FIjGLVzPwi8BFTZ1f2QZw7vKY7W26C79oobQUiSU8Snmf8QCWcZUlGYLF8eIzOGoqvR0eKRh0QUY6Cr3g',
            'Origin': 'https://www.99.co',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"brand":"99id","destination_address":"{number}","type_id":0}',
        'number_fmt': fmt_plus,
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
        'name': 'Dekoruma / Blibli Tiket',
        'post_type': 'json',
        'url': 'https://account.bliblitiket.com/gateway/gks-unm-go-be/api/v1/otp/generate',
        'referer': 'https://account.bliblitiket.com/',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'X-Channel-Id': 'MWEB',
            'X-Client-Id': '3c90f67b0b7bad6d6e1d51fdd26f1d97',
            'X-Entity': 'DEKORUMA',
            'X-Lang': 'id',
            'Origin': 'https://account.bliblitiket.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"action":"REGISTER_OTP","channel":"WHATS_APP","recipient":"{number}","recaptchaToken":"","challengeToken":"1.S4iav-nDFTuvaZ_CuUGdCk8VuiAHwH78JUDaFXRxffdRxuqO7IGaXK2CW7AHOKXa0Skne5d6-_j4NVoWx8ksqgRDsMMr11f3tuJD_RODqW5KZmV5ReAKWr_j55T-tFGiTe734lEkpU956jIqqRzdUSMDX3lTH4VSO0MphYTnbamsXb1d3GjYL2WLy0QmdXjqvMj9XoEUChrNH-_1r6qfXnjvBkVz51OxmFdpnNsH2IsbQZyhrEHlRXdqnVU5lE3WBrl6KCG91rGsUvLUkXCpxPfSTJ1yl7XDKe1eIFG2dsybwlyhRbaExf-djQOX_tXqMTGF_FoH_nW021Ni_nwbfGWsl1TRZqrNipZq1tbEjawonIoQAPNFlXE70vD7XX-07vXSje7BvbGpRpGD_PbP5zLYtZejMpf1fHCEcrs2Dnf2pQGOL8PhADqCS70LbSYXM9jneryzOOdJ4va8AEpapFXSc4CSHBuu6Ii7wCy9YAQmrDEYMrN8eRXDBErO8rWsS4voyT7pHqna9oTTHv69Ht0SgZN48nfEvSKDaeOh6oEY9ciWxZJWQdRw1nPU47PKTmuzBtZPcaUQ9CLqTPJGuf5qnq4TXgaWhmfODlX3sxYcu5mfQT1rRYXvX_Zw9Ll3uq3I8xu3L4mY2vMSc-PkSmcdvsNrvUA9LKxcqxqzYsQ.RSirdkCWSG74KTYJ4-JfuA.3daf4b1e8825eaa66b5168e96f2ee8cf8b658feef60e4e784bf08e98ae6eece4"}',
        'number_fmt': fmt_plus,
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
        'name': 'Sejasa',
        'post_type': 'json',
        'url': 'https://www.sejasa.com/customer_api/v2/authentications/otp/send_otp',
        'referer': 'https://www.sejasa.com/otp#otp',
        'headers': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/json',
            'X-CSRF-Token': 'DYrdHiSKuIKyE7zs407fNaQx5K7RUhs9+hBUwBal9NHswrpBol2xjuhzvUHsRGruHX1VHC+a+r/UyaHqqfPTdw==',
            'X-Date': 'Sat, 05 Sep 2026 03:09:10 GMT',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://www.sejasa.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"otp_token":"eyJhbGciOiJIUzI1NiJ9.eyJsb2dpbl90b2tlbiI6IjNlMGQ4ODgxZWI0ZmY0NmE3MTFjMjMxZmUyNDZlMDg2IiwiaWQiOjE5NjA0OTYsIm90cF90b2tlbiI6IjEzYTVlMDk4OTUyNDkzNTc4MGM5MTAxZmI5ODY0ZjFiIiwib3RwX3JlcXVlc3RfZnJvbSI6InNpZ25faW4ifQ.NIYeX895BLTqY2SY3qYescbmf1YiB-rtQHEt9Ra3J4A","phone_number":"{number}","device_id":"13a5e0989524935780c9101fb9864f1b"}',
        'number_fmt': fmt_plus,
        'success_on': ['success', 'true']
    },
        {
        'name': 'OYO Rooms',
        'post_type': 'json',
        'url': 'https://www.oyorooms.com/api/pwa/generateByPhone?locale=id',
        'referer': 'https://www.oyorooms.com/login',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'access_token': 'SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=',
            'XSRF-TOKEN': 'HoIpzuwc-Nvw0drCNKTqe7Y4B97dEwhb9En8',
            'deviceid': '202dfcda2ea70eed9f9a8212a4f78312120061',
            'consumer_host': 'https://www.oyorooms.com',
            'Origin': 'https://www.oyorooms.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"phone":"{number}","country_code":"+62","country_iso_code":"ID","nod":4,"send_otp":true,"devise_role":"Consumer_Guest"}',
        'number_fmt': lambda p: p[1:] if p.startswith('0') else (p[2:] if p.startswith('62') else p),
        'success_on': ['success', 'true', 'status']
    },
        {
        'name': 'Pizza Hut Indonesia',
        'post_type': 'json',
        'url': 'https://api-prod.pizzahut.co.id/customer/v1/customer/send-otp',
        'referer': 'https://www.pizzahut.co.id/register',
        'headers': {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CLIENT-ID': 'b39773b0-435b-4f41-80e9-163eef20e0ab',
            'X-LANG': 'en',
            'X-DEVICE-TYPE': 'MOBILE',
            'X-PLATFORM': 'WEBMOBILE',
            'X-DEVICE-ID': 'web',
            'X-CHANNEL': '2',
            'Origin': 'https://www.pizzahut.co.id',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"key":"{number}","type":1}',  # Sesuaikan parameter key jika membutuhkan token sesi awal
        'number_fmt': fmt_nocode,
        'success_on': ['success', 'true', 'status']
    },
        {
        'name': 'Carsome Indonesia',
        'post_type': 'json',
        'url': 'https://www.carsome.id/website/login/sendSMSV2',
        'referer': 'https://www.carsome.id/jual-mobil-bekas',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'x-platform': 'web',
            'country': 'ID',
            'x-language': 'id',
            'Origin': 'https://www.carsome.id',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"username":"{number}","optType":1,"recaptchaToken":"","recaptchaSiteKey":"6LejduQhAAAAAJplB52IumC2_E5xKqqR2hZmeZPY","recaptchaExpectedAction":"Login"}',
        'number_fmt': lambda p: p[1:] if p.startswith('0') else (p[2:] if p.startswith('62') else p),
        'success_on': ['success', 'true', 'status']
    },
        {
        'name': 'Indodana Finance',
        'post_type': 'json',
        'url': 'https://api.indodanafinance.co.id/services/athena/download-app/sms',
        'referer': 'https://www.indodana.id/',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Origin': 'https://www.indodana.id',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"phoneNumber":"{number}"}',
        'number_fmt': lambda p: p[1:] if p.startswith('0') else (p[2:] if p.startswith('62') else p),
        'success_on': ['success', 'true', 'status']
    },
    {
        'name': 'Ginee',
        'post_type': 'json',
        'url': 'https://bizapi.ginee.com/infra/common/security/send-otp',
        'referer': 'https://accounts.ginee.com/profile/phone',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJnZW5pZS1pYW0tc2VydmljZSIsImFjY291bnRJZCI6IlUyMDk2MDc4ODkxNDQ0NTk2NzM2IiwicGhvbmUiOiIrNjI4NTE2NjEzOTA2NCIsImVtYWlsIjoibWRqYXphcnF5QGdtYWlsLmNvbSIsInBhcmVudElkIjpudWxsLCJhdWQiOiJXRUIiLCJpYXQiOjE3ODg1NzkxMjUsImV4cCI6MTc5MTE3MTEyNX0.i4eKFi7mO3gRgXltttzj89iLAoRX8By-PbntE6rB330owuxbBa9g04Iqw9soHVRim-sLe3j_Q-GSA1C1hOj1T-aoF2o2J_Voyjz94Gr5mI3Oit6NNxt8_XuJLuPLI4UNVSHG4iEm9jdeUkTwjXzY3kwdF0s3I2_n9LntyG_1HcYkcKJznsZZkaOQoj0daYdscb2JsqMi7uSOlraHRVdFVjWUMDjXpZGjNOe2yuVjyFT6GvWWmKvButHqVfdr9op6MopSQc4TuMp6J-zegltmKl0kgFAyeIxqH-pcV8rmx7DlQmy2XDvLvxLnSda2scBuuiWRJBhk71W31Yu-PQUMVg',
            'Accept-Language': 'en',
            'Origin': 'https://accounts.ginee.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"account":"{number}","phoneCountry":"ID","recaptchaToken":"","verificationPurpose":"USER_SUPPLEMENTARY_INFORMATION","verificationType":"PHONE"}',
        'number_fmt': lambda p: p[1:] if p.startswith('0') else (p[2:] if p.startswith('62') else p),
        'success_on': ['success', 'true', 'code']
    },
        {
        'name': 'Asani',
        'post_type': 'json',
        'url': 'https://api.asani.co.id/api/v2/sendOtp',
        'referer': 'https://my.asani.co.id/register/',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Origin': 'https://my.asani.co.id',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"email":"testing@gmail.com","phone":"{number}","token":""}',
        'number_fmt': lambda p: '62' + (p[1:] if p.startswith('0') else (p[2:] if p.startswith('62') else p)),
        'success_on': ['success', 'true', 'message']
    },
    {
        'name': 'Telkomsel FMC',
        'post_type': 'json',
        'url': 'https://www.telkomsel.com/landingpage/api/lp/fmc/v1/resend-otp',
        'referer': 'https://www.telkomsel.com/landingpage/regular/reg11/verifikasi-otp',
        'headers': {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'x-api-key': 'U2FsdGVkX1+4cu0+tCrz5JTWDtDiUD0Lsp+YQ8tqW7P+T/zGaeTbScSOjqDPUo90UA1K731jACNzmunLi2X+/g==',
            'Origin': 'https://www.telkomsel.com',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Mobile Safari/537.36'
        },
        'payload': '{"code":"0","token":"feK41oIHEz7d2v9DROpg","data":"{number}"}',
        'number_fmt': fmt_08,
        'success_on': ['success', 'true', 'status']
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
