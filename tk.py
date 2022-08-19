import httpx

def get_url(url, page):
    headers = {'user-agent': 'My User Agent 1.0'}
    return httpx.get(url + f"{page}", headers=headers)

def find_tk(url):

    total_pages = get_url(url, 0).json()["pagination"]["numberOfPages"]
    print(f"Total pages: {total_pages}")
  
    reslist = []
    errs = 0

    for page in range(total_pages or total_pages-1): #sometimes cannot find "results" on the last page
        jsondata = get_url(url, page).json()
        print(f"current page: {page}")

        for i in range(len(jsondata["results"])): 
            res = {}
            try:
                res["Brand"] = jsondata["results"][i]["brandName"]
                # res["Label"] = jsondata["results"][i]["label"]
                res["Url"] = "https://www.tkmaxx.com" + jsondata["results"][i]["url"]
                res["Price"] = jsondata["results"][i]["price"]["formattedValue"]
                res["Image"] = jsondata["results"][i]["image"]["url"]
                # res["Stock value"] = jsondata["results"][i]["stockValue"]
                # res["RRP Price"] = jsondata["results"][i]["rrpPrice"]["formattedValue"]
                # res["Was Price"] = jsondata["results"][i]["wasPrice"]["formattedValue"]
                # res["Save"] = jsondata["results"][i]["savePrice"]["formattedValue"]
                # res["savePricePercentage"] = jsondata["results"][i]["savePricePercentage"]
            except:
                errs += 1
            finally:
                reslist.append(res)
    print(f"err: {errs}")
    return reslist

if __name__ == "__main__":
  find_tk()


