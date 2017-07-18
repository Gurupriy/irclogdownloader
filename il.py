import requests,bs4,time,os
url="https://dgplug.org/irclogs/"
res=requests.get(url)
#res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"lxml")
element = soup.select('a')
os.makedirs("Misc")
def func(l,p):
    os.makedirs(p)
    os.chdir(p)
    for i in range(5,len(l)):

        time.sleep(0.3)
        newpage=l[i].get("href")
        print "---------------------------------------------------------"+newpage+"------------------------------------------------------"
        if(newpage[-1]=='/'):
            newpage=str(newpage).strip('/')
        File=open(newpage,'wb')
        get_content=requests.get(url+str(p)+str(newpage))

        for content in get_content.iter_content(len(get_content.text)):
            File.write(content)
            File.close()
            #print content
    os.chdir("../")
for i in range(5,len(element)):
    time.sleep(0.5)

    f=element[i].get("href")
    temp=requests.get(url+f)
    page=bs4.BeautifulSoup(temp.text,"lxml")
    a=page.select("a")
    if(len(a)>0):
        func(a,f)

    else:
        print "---------------------------------------------------------"+f+"------------------------------------------------------"
        for chunk in temp.iter_content(len(temp.text)):
            os.chdir("Misc")
            Filec=open(f,'wb')
            Filec.write(chunk)
            Filec.close()
            os.chdir("../")
print "***********************************DONE******************************************"
