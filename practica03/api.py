import json
import requests as req
import datetime
import pandas as pd
import time

def format_adrress(address):
    api_key = 'AxJQWEi8uOq9rfheazX7Ui0NXPTxzxMdBHOim7jW5QY'
    try:
        address_ = f"{'%20'.join(address)}%20RM%20Chile"
        address_to_geocode = f'https://geocoder.ls.hereapi.com/6.2/geocode.json?apiKey={api_key}&searchtext={address_}'
        res = req.get(address_to_geocode)
        if res.json()['Response']['View'][0]['Result'][0]['Relevance'] >= 0.9:
            latlon = res.json()['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']  # {'Latitude': 37.37634, 'Longitude': -122.03405}        
            ll = [latlon['Latitude'], latlon['Longitude']]      
            return ['Av.', address[1], address[-1], address[0], ll[0], ll[1]]
        else:
            return 'Por alguna razón no pudimos encontrar tu dirección.'                
    except Exception as e:
        print(e)
        return 'Por alguna razón no pudimos encontrar tu dirección.'           
    
    
    
def ubereats(calle_prefix, calle, numero, comuna, lat, lon, saving=False):
    pages = [81, 161, 241, 321, 401]
    categories = [
        'Bebidas alcohólicas',
        'Desayuno y brunch',
        'Pollo',
        'Postres',
        'Pizza',
        'Poke',
        'Árabe',
        'Hamburguesas',
        'Conveniencia',
        'Café y té'
    ]

    stamp = '{:%Y_%b_%d_%H_%M_%S}'.format(datetime.datetime.now())

    print('Processing...')

    list_of_items = []
    for j in pages:
        for k in categories:
            try:
                url = 'https://www.ubereats.com/api/getFeedV1?localeCode=cl'
                headers = {
                    "Host": "www.ubereats.com",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0",
                    "Accept": "*/*",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Content-Type": "application/json",
                    "x-uber-xps": "%7B%22eats_web_low_courier_supply_ux%22%3A%7B%22name%22%3A%22treatment%22%7D%2C%22eats_web_photo_forward_grid_view%22%3A%7B%22name%22%3A%22enabled%22%7D%2C%22eats_web_pm_checkout_message_banner%22%3A%7B%22name%22%3A%22treatment%22%7D%2C%22eats_web_westplan_migration_get_credit_balances_edge%22%3A%7B%22name%22%3A%22enabled%22%7D%2C%22eats_web_quick_add_to_cart%22%3A%7B%22name%22%3A%22enabled%22%7D%2C%22eats_web_coi_checkout_v2%22%3A%7B%22name%22%3A%22treatment%22%7D%2C%22eats_web_payments_switch_payment_enabled%22%3A%7B%22name%22%3A%22treatment%22%7D%2C%22eats_web_migrate_delivery_details_to_location_manager%22%3A%7B%22name%22%3A%22treatment%22%7D%2C%22eats_web_tipping_payment_info%22%3A%7B%22name%22%3A%22enabled%22%7D%2C%22eats_web_storefront_store_info%22%3A%7B%22name%22%3A%22treatment%22%7D%7D",
                    "x-csrf-token": "x",
                    "Content-Length": "983",
                    "Origin": "https://www.ubereats.com",
                    "Connection": "keep-alive",
                    "Referer": "https://www.ubereats.com/cl/feed?ps=1&sf=JTVCJTdCJTIydXVpZCUyMiUzQSUyMjFjN2NmN2VmLTczMGYtNDMxZi05MDcyLTI2YmMzOWY3YzAyMSUyMiUyQyUyMm9wdGlvbnMlMjIlM0ElNUIlN0IlMjJ1dWlkJTIyJTNBJTIyNGM3Y2Y3ZWYtNzMwZi00MzFmLTkwNzItMjZiYzM5ZjdjMDIzJTIyJTdEJTVEJTdEJTVE&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMkF2LiUyMENvbmRlbGwlMjA3MzglMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKNjRRY19JSEZZcFlSOWRqOGpDWGhIYUElMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBLTMzLjQ0MTcyMTclMkMlMjJsb25naXR1ZGUlMjIlM0EtNzAuNjI3MjMzOSU3RA%3D%3D",
                    "Cookie": f"uev2.id.xp=948c9109-c0eb-4b79-9180-b2bf712564c5; dId=5673ecf5-7b86-4dbe-8467-319308ed8245; uev2.id.session=2004152c-5489-4352-b94a-8504d0d5661b; uev2.ts.session=1635010372758; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2MzUwMTAzNzIsImV4cCI6MTYzNTA5Njc3Mn0.fR0VRjdvFBDVku743bOX3fbVvfGNn5zbLaCgsUhrX9A; marketing_vistor_id=57e7b24c-dbd3-42aa-92d0-dcdcf9f1271c; uev2.gg=true; utag_main=v_id:017cae3672360021b488a53fa70c00052001b00f00ac2$_sn:2$_se:4$_ss:0$_st:1635014778453$ses_id:1635012977906%3Bexp-session$_pn:1%3Bexp-session; _userUuid=fccc132f-7663-4b82-81db-df7a78ef4bff; utm_medium=undefined; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1635010376259%7Cconsent:true; _rdt_uuid=1635010376357.6e3d044a-7bb5-4f25-b43e-be5909232ed7; _scid=1d80677d-cad4-4b66-bd87-742b4d13a3ce; _gcl_au=1.1.578094346.1635010377; _sctr=1|1634958000000; _ts_yjad=1635010377247; _ga=GA1.2.503512902.1635010378; _gid=GA1.2.16842940.1635010378; _fbp=fb.1.1635010378056.368663011; sid=QA.CAESEIZ34RZ0iETaiMmuv0C66nkY6ajvjAYiATEqJGZjY2MxMzJmLTc2NjMtNGI4Mi04MWRiLWRmN2E3OGVmNGJmZjJAQ-K1QXKACW2K7867eugBr9tMNVkD-Qm08CbJLJ7ig1fnjwaJtRnqnbhJfH-yQEinsgRsdnlN4wgGsOBrmhGdkjoBMUINLnViZXJlYXRzLmNvbQ._Bb5VLf4-va_THnqJTfTMkPPy88MtPIHHP6iQDHeiEo; uev2.loc=%7B%22address%22%3A%7B%22address1%22%3A%22Av.%20{calle}%20{numero}%22%2C%22address2%22%3A%22{comuna}%2C%20Regi%C3%B3n%20Metropolitana%22%2C%22aptOrSuite%22%3A%22%22%2C%22eaterFormattedAddress%22%3A%22%22%2C%22subtitle%22%3A%22{comuna}%2C%20Regi%C3%B3n%20Metropolitana%22%2C%22title%22%3A%22{calle_prefix}%20{calle}%20{numero}%22%2C%22uuid%22%3A%22%22%7D%2C%22interactionType%22%3A%22door_to_door%22%2C%22latitude%22%3A{lat}%2C%22longitude%22%3A{lon}%2C%22reference%22%3A%22ChIJ64Qc_IHFYpYR9dj8jCXhHaA%22%2C%22referenceType%22%3A%22google_places%22%2C%22type%22%3A%22google_places%22%2C%22source%22%3A%22tagged_location%22%2C%22addressComponents%22%3A%7B%22countryCode%22%3A%22CL%22%2C%22firstLevelSubdivisionCode%22%3A%22Regi%C3%B3n%20Metropolitana%22%2C%22city%22%3A%22{comuna}%22%2C%22postalCode%22%3A%22%22%7D%2C%22originType%22%3A%22user_autocomplete%22%7D; _gat_tealium_0=1; _uetsid=42790210342711ec9c5dad915f993298; _uetvid=4278e550342711eca838a5976681c613",
                    "Sec-Fetch-Dest": 'empty',
                    "Sec-Fetch-Mode": 'cors',
                    "Sec-Fetch-Site": 'same-origin',
                    "Cache-Control": 'max-age=0',
                    "TE": 'trailers'
                }
                payload = {
                    "cacheKey": f"JTdCJTIyYWRkcmVzcyUyMiUzQSUyMkF2LiUyMFBkdGUuJTIwS2VubmVkeSUyMExhdGVyYWwlMjA5MDAxJTIyJTJDJTIycmVmZXJlbmNlJTIyJTNBJTIyQ2hJSmM5Y1lKTFRPWXBZUkdURUs0RmoxY0ZNJTIyJTJDJTIycmVmZXJlbmNlVHlwZSUyMiUzQSUyMmdvb2dsZV9wbGFjZXMlMjIlMkMlMjJsYXRpdHVkZSUyMiUzQS0zMy4zOTAzMTY3JTJDJTIybG9uZ2l0dWRlJTIyJTNBLTcwLjU0NDcyJTdE/DELIVERY/{k}//0/0//JTVCJTVE//////",
                    "feedSessionCount": {"announcementCount": 0, "announcementLabel": ""},
                    "showSearchNoAddress": "false", "userQuery": f"{k}", "date": "", "startTime": 0, "endTime": 0,
                    "carouselId": "", "sortAndFilters": [], "marketingFeedType": "", "billboardUuid": "",
                    "feedProvider": "", "promotionUuid": "", "targetingStoreTag": "", "venueUuid": "", "favorites": "",
                    "vertical": "", "pageInfo": {"offset": j, "pageSize": 80}}
                r = req.post(url, data=json.dumps(payload, indent=4), headers=headers)
                s = r.json()

                for i in s['data']['feedItems']:
                    if len(s['data']['feedItems']) > 0:
                        try:
                            uuid = i['uuid'].strip()
                            type_ = i['type'].lower().strip()
                            title = i['store']['title']['text'].lower().strip()
                            rating = float(i['store']['rating']['text'])
                            reviews = [int(s) for s in i['store']['rating']['accessibilityText'].split() if s.isdigit()][-1]
                            score = round((((rating*reviews)/100)/24.95),2)

                            o = {
                                'uuid': uuid,
                                'type': type_,
                                'title': title,
                                'rating': rating,
                                'reviews': reviews,
                                'score': score,
                                'timestamp': stamp
                            }                            
                            list_of_items.append(o)
                        except Exception as e:
                            print(e)                            
                            break
            except Exception as e:
                print(e)
                pass
            
    if len(list_of_items) > 0:
        df = pd.DataFrame(list_of_items)
        df.sort_values(by='score', ascending=False, inplace=True)
        df.drop_duplicates(subset=['title'], inplace=True)

        if saving:
            df.to_csv(f'data/{stamp}.csv', index=False)

        print(f'Done')
        time.sleep(5)
        return df
    
    
def check(d, s, n):
    q = format_adrress([d, s, n])
    r = ubereats(q[0], q[1], q[2], q[3], q[4], q[5], saving=True)
    res = r.iloc[:,[2,3,4,5]]
    return res.head(10)    

p1 = check('nunoa', 'montenegro', '1075')
print(p1)

# p2 = check('santiago', 'Catedral', '2227')
