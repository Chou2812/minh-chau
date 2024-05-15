import requests
from bs4 import BeautifulSoup
import pandas as pd

#import URL cần lấy thông tin
url_str = 'https://p6-qa.samsung.com/vn/tvs/qled-tv/qe1d-50-inch-qled-4k-tizen-os-smart-tv-qa50qe1dakxxv/'

# Cookie variable defined
cookie = 'recent_list=[{"familyCode":"498821","modelCode":"QA50QE1DAKXXV","tellsomeYn":"N"}]; WMONID=s_LvOJAvPrx; device_type=pc; _ga_1Y8SWQHLVR=GS1.1.1715780754.2.1.1715782744.0.0.1155975874; bv_metrics=true; uat-cookie=si; s_fpid=72847943-a2d4-425e-8fbe-767a9167d41b; country_codes=vn; device_type=pc; visid_incap_2563519=B/7C72ZtTaqzCaRjQhS8HyPIRGYAAAAAQUIPAAAAAADwryHfsRZn63TWIzmfV9iH; incap_ses_282_2563519=dZlIfPlb4F7O5RHQkd3pAyPIRGYAAAAATnGtg24C10wJPmLO+nXtTQ==; wcms_enc_user=542b562a2e13ag155c636419601b3a29761e3b28742f7c2c; wcms_user=chau.mpham; login-token=06ed2b8a-768c-4d64-a78a-11cde16721bc%3a43f41f49-d161-4d0a-a9a3-86c6a69dc639_0e3d0cc99f38cbbc848718bd5613c648%3acrx.default; originalrequestUrl=/sites.html; country_region=CA-ON; AKA_A2=A; __COM_SPEED=H; nh=; pv=; cl=; wl=; ipv=; directCallFlAA=undefined; _gid=GA1.2.2004507476.1715783738; kndctr_C5D8694E5994D9EB0A495E34_AdobeOrg_cluster=sgp3; kndctr_C5D8694E5994D9EB0A495E34_AdobeOrg_identity=CiY1NzMyMTk1MDM1MDAxMzUwMDQ2MDIzMDYwNDUzNjU4MjY3NDg1NlIRCJnKuOX3MRgBKgRTR1AzMAKgAbfKuOX3MbABAPABmcq45fcx; AMCV_C5D8694E5994D9EB0A495E34%40AdobeOrg=MCMID|57321950350013500460230604536582674856; mboxEdgeCluster=38; _gcl_au=1.1.765457734.1715783739; da_sid=FD273F7A8F31AE96FEB4AA13BB2AD6342A.0|4|0|3; da_lid=8005B6EB989AEA14653DBB99F93FD347EB|0|0|0; da_intState=; FPAU=1.2.472755714.1715783740; FPGSID=1.1715783739.1715783739.G-K799WHEEMW.UfRF40nI5YsgGTzgCLQgpA; _vwo_uuid_v2=D4F6DC1DA8AE3F84EBF846245C9E11202|3676f829c558f172e66e7bb106f8830e; _vwo_uuid=D4F6DC1DA8AE3F84EBF846245C9E11202; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _ga_K799WHEEMW=GS1.1.1715783738.1.0.1715783740.0.0.724289425; spr-chat-token-60704a333f367d6e6cb54411_app_918889="eyJhbGciOiJSUzI1NiJ9.eyJ2aXNpdFNlc3Npb25JZCI6IjY2NDRjODNjMTQyNWQyNGQ2ZGUyYWM3OSIsInN1YiI6IkFjY2VzcyBUb2tlbiBHZW5lcmF0ZWQgQnkgU3ByaW5rbHIiLCJjaGF0TG9jYWxlIjoiZW4iLCJjaGF0VXNlckhhc0NvbnZlcnNhdGlvblN0YXJ0ZWQiOmZhbHNlLCJpc3MiOiJTUFJJTktMUiIsInZpc2l0U2Vzc2lvbklkRXhwaXJlQXQiOjE3MTU3ODU1NDA4OTEsInR5cCI6IkpXVCIsImlzRGVmbGVjdGlvblRva2VuIjpmYWxzZSwidXNlclNlc3Npb25Mb2dpbk1ldGhvZCI6IntcInR5cGVcIjpcIkFOT05ZTU9VU1wifSIsImNoYXRVc2VySWQiOiJBXzY2NDRjODNjMTQyNWQyNGQ2ZGUyYWM3OCIsImFwcElkIjoiYXBwXzkxODg4OSIsInNjb3BlIjpbIlJFQUQiLCJXUklURSJdLCJleHAiOjE3MTU3ODU1NDAsImF1dGhUeXBlIjoiU1BSX0tFWV9QQVNTX0xPR0lOIiwiaWF0IjoxNzE1NzgzNzQwLCJqdGkiOiJlMTRmYWNkMC02MzI5LTQxY2QtOTk2Zi1lMmZiNGRlZjZkNzIiLCJhbm9ueW1vdXNJZCI6IkFfNjY0NGM4M2MxNDI1ZDI0ZDZkZTJhYzc4IiwiY2xpZW50SWQiOjkyMTUsInN0cmljdFVzZXJBdXRoZW50aWNhdGlvbiI6ZmFsc2UsInVzZXJJZCI6MCwiYXVkIjoiU1BSSU5LTFIiLCJuYmYiOjE3MTU3ODI1NDAsInZpc2l0U2Vzc2lvblN0YXJ0VGltZSI6MTcxNTc4Mzc0MDg4NCwibXF0dEFjbCI6IntcInBcIjpbXCJwdWJsaXNoL0FfNjY0NGM4M2MxNDI1ZDI0ZDZkZTJhYzc4L3B0ci0xMjQtdG9waWNcIl0sXCJzXCI6W1wiYXBwXzkxODg4OV9pbmJveC9BXzY2NDRjODNjMTQyNWQyNGQ2ZGUyYWM3OFwiLFwiaW5ib3gvQV82NjQ0YzgzYzE0MjVkMjRkNmRlMmFjNzhcIl19IiwiY2hhdFVzZXJUeXBlIjoiQU5PTllNT1VTIiwicGFydG5lcklkIjoxMjQsInRva2VuVHlwZSI6IkFDQ0VTUyJ9.h-IwWQAePP2i9oB0ydHfqcLGoWSyEkPqKLBVEqqMLM0gBeDOImdscYj00lCasLVKv4mtjnQLPzezMUkgBKhIkcFTdR0lUttxGtGT2Ouwuwi6e17lv2rpzVnW2Mhuf1bOa3id63bX3JYxGBaeew2CEv0GQjJqgu_HHanX9vTurehGBcwzy3damxI794hrNa2NfyOW6N05owerKuuQ32V9BJMGi970kYkKTW9ZRg-8IA2TfT0XehFWKII4QnjwjCU153oannFT633UERZs8NnoOdO4Jdd8uo9_-JZk9L48AwdTmi88eNQp9Yqm3RQhJwb64HTg1QvC2vpXazXLVV8tcA"; cookie_country=vn; _tt_enable_cookie=1; _ttp=98NRxtbqWCjWUo18wgT5P7cImPD; spr-chat-token-60701e691263ec048095d2fd_app_918873=; _ga=GA1.1.1270944937.1715783738; BVBRANDID=537f8283-1284-4468-9365-7c0d04f68c40; BVBRANDSID=8b39fd74-6a87-402e-867c-bd815745ab28; vn_jwt_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJjYXJ0R3VpZCI6IjhhNWQ0Mzg2LTUyYmQtNDRjZi05OTc3LTZhNzAyM2VmN2ZiZiIsImprdSI6Imh0dHBzOi8vcDEtc21zLWFwaS1jZG4uc2hvcC5zYW1zdW5nLmNvbS90b2tvY29tbWVyY2V3ZWJzZXJ2aWNlcy92Mi92bi9qd3Qva2V5cyIsImlzcyI6InRva28iLCJpcEFkZHJlc3MiOiIxOTIuMTY4LjAuMCIsInVzZXJUeXBlIjoiQW5vbnltb3VzIiwiZXhwIjoxNzE1Nzg3MzY0LCJpYXQiOjE3MTU3ODM3NjR9.m2zoggACa73y4lYHalsFRqj6jt0pzq2nJebaJCnUsf1Ireb_4z7qNiES9yCq6j5kpS2l5WXFkOG6x-YR-8383oZVtHSbFejg4gp23I8NTKIK_RrCV5HZlF2DcK5TWYBrl_jZ57wMDW3d-k82YCYccyuBOlkQ-WZmZLaIheoKC4Yq-oueilhaqBEyTYRfKUkeK8RZsHqXa6jJLUwVZpEA27IHvj0jvBfFBL2xKzpLrWIIBI0sa03PVhTnwaBgvUTArHWCorZb2QNbQhKsJPYFLu3pRxNcCJDgXMbi-ibwPwmrVewMpjIlIqgL3owzJ3J4dYHdCzxDINrF0Ho_MmG48sC4qZVzPvidX30tEE-lWBDmIVF1kvFzH-Sa3_1_S5JISXHYTmdLNKh4QmafhFFxevXnQ1vGyKmsDwroT-nFfaioX9tUGj8PTvcGae6db0o1nsd1QlC_A7eM-QDnWtkemPViVvnWGD-Ej2GOECWiy6F6OZytn48tLNPjjIwA0jpiRoOmnLZeeVR4NzhqcYFT8T4yjrmekvndemX2Gz-6ZoQ1ftqpJxTjlUPlvbLFf3O7VI4STgujLd6QRps5ss2q31LzlY6gqVW8DEOhswnqX7FMqGFyH96C4cch_MtqXt_K-qxqOrjBdiD50uJfANhtO7uwfMzdUdULBX-9u9Mkx6g; jwt_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJjYXJ0R3VpZCI6IjhhNWQ0Mzg2LTUyYmQtNDRjZi05OTc3LTZhNzAyM2VmN2ZiZiIsImprdSI6Imh0dHBzOi8vcDEtc21zLWFwaS1jZG4uc2hvcC5zYW1zdW5nLmNvbS90b2tvY29tbWVyY2V3ZWJzZXJ2aWNlcy92Mi92bi9qd3Qva2V5cyIsImlzcyI6InRva28iLCJpcEFkZHJlc3MiOiIxOTIuMTY4LjAuMCIsInVzZXJUeXBlIjoiQW5vbnltb3VzIiwiZXhwIjoxNzE1Nzg3MzY0LCJpYXQiOjE3MTU3ODM3NjR9.m2zoggACa73y4lYHalsFRqj6jt0pzq2nJebaJCnUsf1Ireb_4z7qNiES9yCq6j5kpS2l5WXFkOG6x-YR-8383oZVtHSbFejg4gp23I8NTKIK_RrCV5HZlF2DcK5TWYBrl_jZ57wMDW3d-k82YCYccyuBOlkQ-WZmZLaIheoKC4Yq-oueilhaqBEyTYRfKUkeK8RZsHqXa6jJLUwVZpEA27IHvj0jvBfFBL2xKzpLrWIIBI0sa03PVhTnwaBgvUTArHWCorZb2QNbQhKsJPYFLu3pRxNcCJDgXMbi-ibwPwmrVewMpjIlIqgL3owzJ3J4dYHdCzxDINrF0Ho_MmG48sC4qZVzPvidX30tEE-lWBDmIVF1kvFzH-Sa3_1_S5JISXHYTmdLNKh4QmafhFFxevXnQ1vGyKmsDwroT-nFfaioX9tUGj8PTvcGae6db0o1nsd1QlC_A7eM-QDnWtkemPViVvnWGD-Ej2GOECWiy6F6OZytn48tLNPjjIwA0jpiRoOmnLZeeVR4NzhqcYFT8T4yjrmekvndemX2Gz-6ZoQ1ftqpJxTjlUPlvbLFf3O7VI4STgujLd6QRps5ss2q31LzlY6gqVW8DEOhswnqX7FMqGFyH96C4cch_MtqXt_K-qxqOrjBdiD50uJfANhtO7uwfMzdUdULBX-9u9Mkx6g; estoreSitecode=vn; estoreSitecode_cm=au2; _abck=7CCB46CE68D06598894CDD1318CD46F7~-1~YAAQfiZzaFAonXWPAQAAIImufAsEEw05QOwQ0Nq3QVE72pmtzK1cC0u5V3OeMujjH0fR0/+MuWcHRuc9BG4LTArtJXL0+yBsybkTLTQBejVgYhRdmWD9z2Q8ZMGaC6qxv7Exk2yRe++xweBvcpszDJJSFXaD+tS0zRRsJan6Jqv7Yo46jhuVLB3F9owRteaqHabbvHoBktS/ALm0FEtCFXzYEz3ZyTC2PdxsfZpigEstrNVgmkFdDDyOAYC7+Jq9gqiI7gexiq3+eDeDfY6XZ1huGVau/nyYWzw3sZhEI07rv7oXgHfs3FoMZxqSuCrBQAJy899IQ+Qsrdh8buasgSEalhWdkJd39z07uhkYax/AFgT5ejoPI6UFKxp0~-1~-1~-1; ak_bmsc=FB3B789A7FB83E8178C87F3454BD3C7F~000000000000000000000000000000~YAAQfiZzaFEonXWPAQAAIImufBeB3iVWdXBTGL26SCaaW5QIpy6JLO2ACGhqh7xOCKaGNkl9geRvUQw4JxaKn+pwW4ydteWsN1wwWeJNkpnorLJ0Z8mq3SCxWiL4+KRtL9u++fo6OLAatu7m2tXva2LwmzGZv52OdFNoz+FKz9wczhEZ7sEvPhCb5O1RS0OvOhtSG8nGuUPlhrNDXSN8TDWsyK2dOhXjypfuQXDRxta8HhxgRGXiGsx8p/gVmwk1vkMNd0DuYgSDZ0356EzszsWtWaXWjaFtnPSJkVPmTn9ayoTGScxSaQ69aMl/fv0MwmJCQ/Ynp5z6hDHdaynpK8gF/F9CTmcJbAKyte4uvu2rXchlEnHvBgdcAE/+sIAk69az5hC5Dt/1uA==; bm_sz=CCB300D49B7109EBBC01B3CD84610383~YAAQfiZzaFIonXWPAQAAIImufBdgbuRy8FjiBHBgqF6R58AGoGeUAUbof/xYEMP9wqNZuRO+ozm3wZKW/xQyAAl571BKUz5g70lzmpEQa+SIBHZsLn5Voqm7bTr0AKU8J52Inr+lKtDxyh1YV3+2XEV8gwqh5LhR1/IS5S/kLoCuJ/gPYffBKlaEA1x4T4arkUpzpaYYMRAcS7jK/X7EvJag40zX5yFyYRX419YxY2GyLJdIldiZsE7ynpPTGFcGirkfKoUTJcjvWp8Dm9PydnEUF+GRxbeahZCA0Q+Kq5h401YKLPhIfG1a9Mby4PZqRRFwt85mPb95GI4kQ5MeE3XqrW7WQOrrBTjQHOOR7Nl9YvBjTDggzyk=~4534327~3486257; _vwo_sn=0%3A4%3A%3A%3A1; _vwo_ds=3%3Aa_0%2Ct_0%3A0%241715783739%3A79.99862142%3A%3A4_0%3A47_0%2C45_0%2C31_0%2C29_0%2C4_0%2C3_0%3A1; _ga_TM7SH29VMQ=GS1.1.1715783741.1.1.1715783771.0.0.1767859843; RT="z=1&dm=samsung.com&si=2eb15663-7dd4-416d-9e98-a9a8c808fe72&ss=lw7xc415&sl=4&tt=615&bcn=%2F%2F684d0d4a.akstat.io%2F&ld=mpq&ul=q1j&hd=rd9"; s_pv=vn%3Atelevision%3Atvs%3Aqled%20tv%3Aqe1d-50-inch-qled-4k-tizen-os-smart-tv-qa50qe1dakxxv; _ga=GA1.3.1270944937.1715783738; _gid=GA1.3.2004507476.1715783738; mbox=session%2357321950350013500460230604536582674856%2DvBnEhY%231715785633; _ga_VRH3V7S3H8=GS1.1.1715783775.1.0.1715783775.0.0.62399353; BVImplvd_international=10676_2_0; mdLogger=false; kampyle_userid=617d-95b8-ef70-5962-f9ee-4bbc-b548-7a5b; kampyleUserSession=1715783780967; kampyleUserSessionsCount=1; kampyleSessionPageCounter=1; s_ppvl=sg%253Atelevision%253Atvs%253Aqled%2520tv%253Aqn87d-85-inch-neo-qled-4k-smart-tv-qa85qn87dakxxs%2C12%2C12%2C2549%2C521%2C703%2C1440%2C900%2C2%2CL; s_ppv=vn%253Atelevision%253Atvs%253Aqled%2520tv%253Aqe1d-50-inch-qled-4k-tizen-os-smart-tv-qa50qe1dakxxv%2C8%2C5%2C703%2C838%2C703%2C1440%2C900%2C2%2CP; AWSALB=WPnfz28ECEc0hrjbV4cdMQlRYuFuw+pn9WhkMZQZLrBbM0AgJiVV67ceP+YREZvhDXx4JXLqF+vdwANRRkNK/dhnYPlL+zQfHP1+s+O7qKfGiOppsjoPq8yBJm2a; RT="z=1&dm=p6-qa.samsung.com&si=2eb15663-7dd4-416d-9e98-a9a8c808fe72&ss=1715783770203&sl=0&tt=0&bcn=%2F%2F684d0d42.akstat.io%2F&ld=mpq&ul=1715783811076&hd=rd9&r=https%3A%2F%2Fp6-qa.samsung.com%2Fvn%2Ftvs%2Fqled-tv%2Fqe1d-50-inch-qled-4k-tizen-os-smart-tv-qa50qe1dakxxv%2F&obo=0&sh="'

# Header params variable define
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
  'cache-control': 'no-cache',
  'cookie': cookie,
  'pragma': 'no-cache',
  'priority': 'u=0, i',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

#  Create get_soup function to get page data - viết hàm để lấy data của page
def get_soup():
    response = requests.get(url=url_str, headers=headers)
    # Status code lớn hơn hoặc bằng 400 là bị lỗi, có thể do session hết hạn, đổi cookie mới
    if (response.status_code <= 200):
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        message = "UnAuthorized" if response.status_code == 401 else response.status_code
        print("Get data failed -", message)
        
soup = get_soup()

# Function find element with parent_class -> get section -> title_class -> get title
#  and get image alt
# Viết 1 hàm tìm và lấy những element từ block lớn đến chi tiết     
def getRawData(parent_class, title_class, all_titles, all_alt):
    
    if (soup is None):
        return
    # Kả triêm coi page data có giá trị hay không
    sections = soup.find_all(class_=parent_class)
    list_title = []
    list_alt = []
    for section in sections:
        title_element = section.find(class_=title_class)
        
        # Mặc định title là None, nếu tìm được title với class cho trước thì gán lại giá trị
        title = "None"
        if (title_element is not None):
            title = title_element.text
        
        image = section.find('img')
        alt = image.get('alt')
        if (alt is None):
            alt = image.get('data-desktop-alt')
            if (alt is None):
                alt = image.get('data-mobile-alt')
                
        # Thêm 1 phần từ mới vào danh sách
        all_titles.append(title)
        all_alt.append(alt)
        
        list_title.append(title)
        list_alt.append(alt)
    #In chơi để kiếm tra từng class có giá trị gồm title và Alt text hem thui    
    print(parent_class + " - " +title_class)
    print("List_Title: ", list_title)
    print("List_Alt: ", list_alt)
    print("-----------------------------------")

# Hàm viết riêng để lấy alt cho Gallery component (tương tự như bên trên)
# Nội dung hk thay đổi
def getGallery(parent_class, all_titles, all_alt):
    response = requests.get(url=url_str, headers=headers)
    # Status code lớn hơn hoặc bằng 400 là bị lỗi, có thể do session hết hạn, đổi cookie mới
    if (response.status_code >= 400):
        message = "UnAuthorized" if response.status_code == 401 else ""
        print("Get data failed - ", message)
        # Return khi gặp lỗi để dừng lại hàm và ko làm gì cả
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    sections = soup.find_all(class_=parent_class)
    for section in sections:
        images = section.find_all('img')
        for image in images:
            alt = image.get('alt')
            if (alt is None):
                alt = image.get('data-desktop-alt')
                if (alt is None):
                    alt = image.get('data-mobile-alt')
                    
            all_titles.append("None")
            all_alt.append(alt)
            
# getRawData("product-summary__list-item", "product-summary__list-item-text")
# getRawData("feature-benefit-full-bleed", "feature-benefit-full-bleed__title")
# getRawData("ftd14-key-feature-icon__column", "ftd14-key-feature-icon__sub-title")
# getRawData("feature-benefit", "feature-benefit__title")

# Khởi tạo list elements chứa parent_class và title_class
elements = [
    {
        "parent_class": "product-summary__list-item",
        "title_class": "product-summary__list-item-text"
    },
    {
        "parent_class": "feature-benefit-full-bleed",
        "title_class": "feature-benefit-full-bleed__title"
    },    
    {
        "parent_class": "ftd14-key-feature-icon__column",
        "title_class": "ftd14-key-feature-icon__sub-title"
    },
    {
        "parent_class": "feature-benefit",
        "title_class": "feature-benefit__title"
    },
    {
        "parent_class": "ftd16-interactive-multi-feature__swiper-item",
        "title_class": "ftd16-interactive-multi-feature__headline"
    },
    {
        "parent_class": "three-column-carousel__item",
        "title_class": "three-column-carousel__text__headline"
    },
    {
        "parent_class": "feature-benefit-tab-panel",
        "title_class": "feature-benefit-tab__title"
    }
]
#Hàm cuối cùng để lấy tổng hợp giá trị 2 hàm trên: Alt của hàm getRawData và hàm viết riêng cho Galerry component
def get_data(elements):
    all_titles = []
    all_alt = []

    # Lặp qua từng phần từ để lú va lây (lấy value: lấy giá trị)  của từng class
    for element in elements:
        parent_class = element['parent_class']
        title_class = element['title_class']
        
        # Lấy giá trị của getRawData
        getRawData(parent_class=parent_class, title_class=title_class, all_titles=all_titles, all_alt=all_alt)
    
    # Lấy data của class feature-benefit-gallery
    getGallery(parent_class="feature-benefit-gallery", all_titles=all_titles, all_alt=all_alt)
    
    # Trả về giá trị để export excel data
    return {
        "Title": all_titles,
        "Alt": all_alt
    }
    # print(parent_class, title_class + "- Success")
    

data = get_data(elements=elements)
# Export ra file excel
# Export data if Result not empty
if (len(data['Title']) > 0 or len(data['Alt']) > 0):
    df = pd.DataFrame(data)
    df.to_excel("List_Alt.xlsx", index=False)
    print("Export excel data successfully")