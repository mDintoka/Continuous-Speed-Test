import speedtest
import time
import datetime
import sys
import keyboard
import csv
viser=speedtest.Speedtest(secure=True)
time1=datetime.datetime.now()
min=time1.minute
hour=time1.hour
convert_hour_into_minute=((hour*60)+min)
date=time1.date()
# print(convert_hour_into_minute)
# help(viser.results)
# print(dir(viser))
# kp=viser.get_best_server
# print(viser.results.ping())
#TYPE OF OUTPUT USER WANT-----------
print(("viser".upper()).center(120))
print(f"DATE:{date}",f"TIME:{time.strftime("%I:%M")}".center(200))
while True: 
  answer=input("WANT ANSWER IN: \n1=kilobits\n2=Megabits\n")
  if answer in ("1","2"):
     break
  else:
     print("please select from menu".upper())
#SETTING THE SETTING OF CUSTIMIZE SPEEDTEST----------------
while True:
   input1=input("settings\n1=perform test one time\n2=custimize setting\n".upper())
   if input1 in ("1","2"):
      break
   else:
      print("'SELECT FROM ABOVE MENU'")
#1-TIME OUTPUT GENERATOR----------------
if input1 =="1":
   while True:
      try:
         print("GETTING SERVER......")
         obt_server=viser.get_servers()
         time.sleep(2.5)
         print("getting server near you".upper())
         get_server=viser.get_closest_servers()
         time.sleep(1.5)
# print(get_server)
         print("package obtain".upper())
         for i in range(len(get_server)): 
          time.sleep(1)
          print(f"PROVIDER:{get_server[i]["sponsor"]} IDs:{get_server[i]['id']}----------------------LOC:{get_server[i]['name']}".center(140))
         time.sleep(.5)

         print("catching server near you...".upper())
         time.sleep(2)
         print("optimizing".upper())


         print("GETTING BEST SERVER....")
         server=(viser.get_best_server())
# print(server)
#    ping=viser.results.ping() 
         print(f"FOUND BEST SERVER:{server["sponsor"]} LOCATED IN:{server["name"]}\nYOUR LOCATION:{server["country"]}")
         latency=server["latency"]
         print(f"LATENCY:{latency} ms")
         print("TESTING PLEASE WAIT\n")
         ping=None  #ping have some issue
         viser_download=viser.download()
         viser_upload=viser.upload()
         def speedtest_result(viser_download,viser_upload,ping):
              return{"vd":viser_download/1000,"vu":viser_upload/1000,"ping":ping} #speedtest gave the value in bits to convert bits to kilobits and then to megabits
         result=speedtest_result(viser_download,viser_upload,ping)
         
         if answer == "1":
             print(f"YOUR DOWNLOAD SPEED IS:{result["vd"]:.2f} Kbps",f"Real Time Down:{(result["vd"])/8:.2f} MBs".center(120))
             print(f"YOUR UPLOAD SPEED IS:{result["vu"]:.2f} Kbps",f"Real Time Up:{(result["vd"])/8:.2f} MBs".center(120))
            #  print(end=("\r"))
         #  print(f"YOUR PING:{ping}")
             break
            #  sys.exit()
         if answer=="2":
            print(f"YOUR DOWNLOAD SPEED IS:{(result["vd"]/1000):.2f} Mbps",f"Real Time Down:{(result["vd"]/1000)/8:.2f} MBs")
            # data3=(f"YOUR DOWNLOAD SPEED IS:{(result["vd"]/1000):.2f} Mbps",f"Real Time Down:{(result["vd"]/1000)/8:.2f} MBs")
            print(f"YOUR UPLOAD SPEED IS:{(result["vu"]/1000):.2f} Mbps",f"Real Time Up:{(result['vu']/1000)/8:.2f} MBs")
            # data4=(f"YOUR UPLOAD SPEED IS:{(result["vu"]/1000):.2f} Mbps",f"Real Time Up:{(result['vu']/1000)/8:.2f} MBs")
            
           #  print(f"Real Time Down:{(result["vd"]/1000)/8:.2f} Mbps Real Time Up{(result['vu']/1000)/8:.2f}".center(220))
            # print(end=("\r"))
            break
            # sys.exit()
         # print(f"YOUR PING:{ping}")
      except:
          print("UFFF!! SERVER IS Soo BUSY TRYING PLEASE WAIT")
          time.sleep(5)
          continue
       #  sys.exit()
   
#refresh these input after every 1 minute
if input1=="2":
   user99=int(input("ENTER THE MINUTE \nNOT GREATER THAN 60\n"))
   time1=time.time() #WE ARE USING TH EPOCH TIME WHICH IS EFFICIENT
   # print(time1)   
   how_long=(user99*60)+time1
   # print(how_long)
   print("HOLD S TO STOP")
#   time=int(input("SET YOUR MINUTES"))
#   stop_time=time+convert_hour_into_minute
   if user99>60:
     print("INPUT INVALID----TRY AGAIN".center(140))
     sys.exit()
   while (time.time())<how_long:
        if keyboard.is_pressed("S"):
         sys.exit()
        try:
            print("GETTING SERVER......")
            obt_server=viser.get_servers()
            time.sleep(.5)
            print("getting server near you".upper())
            get_server=viser.get_closest_servers()
            time.sleep(.5)
# print(get_server
            print("package obtain".upper())
            for i in range(len(get_server)): 
             time.sleep(.6)
             print(f"PROVIDER:{get_server[i]["sponsor"]} IDs:{get_server[i]['id']}----------------------LOC:{get_server[i]['name']}".center(140))
            time.sleep(1)

            print("catching server near you...".upper())
            time.sleep(1)
            print("optimizing".upper())


            print("GETTING BEST SERVER....")
            server=(viser.get_best_server())   
# print(server)
#    ping=viser.results.ping() 
            print(f"FOUND BEST SERVER:{server["sponsor"]} LOCATED IN:{server["name"]}\nYOUR LOCATION:{server["country"]}")
            serverdata=server["sponsor"],server["name"]
            # print(serverdata)
            latency=server["latency"]
            print(f"LATENCY:{latency} ms")
            print("TESTING PLEASE WAIT\n")
            ping=None  #ping have some issue
            viser_download=viser.download()
            viser_upload=viser.upload()
            def speedtest_result(viser_download,viser_upload,ping):
                 return{"vd":viser_download/1000,"vu":viser_upload/1000,"ping":ping} #speedtest gave the value in bits to convert bits to kilobits and then to megabits
            result=speedtest_result(viser_download,viser_upload,ping)
            # l=l+1
            if answer == "1":
              print(f"YOUR DOWNLOAD SPEED IS:{result["vd"]:.2f} Kbps",f"Real Time Down:{(result["vd"])/8:.2f} KBs".center(120))
              data1=(f"YOUR DOWNLOAD SPEED IS:{result["vd"]:.2f} Kbps",f"Real Time Down:{(result["vd"])/8:.2f} KBs")
              
              print(f"YOUR UPLOAD SPEED IS:{result["vu"]:.2f} Kbps",f"Real Time Up:{(result["vd"])/8:.2f} KBs".center(120))
              data2=(f"YOUR UPLOAD SPEED IS:{result["vu"]:.2f} Kbps",f"Real Time Up:{(result["vd"])/8:.2f} KBs")
            #   print(end=("\r"))
              output_time=time.strftime("%I:%M")
              head1=["DOWNLOAD-speed","UPLOAD-speed","time","RTD","RTU","server-used","server-loc"]
              outputdata=[{"DOWNLOAD-speed":data1[0],"UPLOAD-speed":data2[0],"time":output_time,"RTD":data1[1],"RTU":data2[1],"server-used":serverdata[0],"server-loc":serverdata[1]}]
              with open("speed_data in kbps.csv",mode="a",newline="")as file:
                writer=csv.DictWriter(file,fieldnames=head1,delimiter="-")
                if file.tell()==0:
                 writer.writeheader()
                writer.writerow(outputdata)
                print("DATA SAVED....")
        #  print(f"YOUR PING:{ping}")
           # sys.exit()
            if answer=="2":
               print(f"YOUR DOWNLOAD SPEED IS:{(result["vd"]/1000):.2f} Mbps",f"Real Time Down:{(result["vd"]/1000)/8:.2f} MBs".center(120))
               data3=(f"YOUR DOWNLOAD SPEED IS:{(result["vd"]/1000):.2f} Mbps",f"Real Time Down:{(result["vd"]/1000)/8:.2f} MBs")

               print(f"YOUR UPLOAD SPEED IS:{(result["vu"]/1000):.2f} Mbps",f"Real Time Up:{(result['vu']/1000)/8:.2f} MBs".center(120))
               data4=(f"YOUR UPLOAD SPEED IS:{(result["vu"]/1000):.2f} Mbps",f"Real Time Up:{(result['vu']/1000)/8:.2f} MBs")
               output_time=time.strftime("%I:%M:b")
               head2=["DOWNLOAD-speed","UPLOAD-speed","time","RTD","RTU","server-used","server-loc"]
               outputdata=[{"DOWNLOAD-speed":data3[0],"UPLOAD-speed":data4[0],"time":output_time,"RTD":data3[1],"RTU":data4[1],"server-used":serverdata[0],"server-loc":serverdata[1]}]
               with open("speed_data in Mbps.csv",mode="a",newline="")as file:
                 writer=csv.DictWriter(file,fieldnames=head2,delimiter="-")
                 if file.tell()==0:
                  writer.writeheader()
                 writer.writerows(outputdata)
                 print("DATA SAVED....")
            #  print(f"Real Time Down:{(result["vd"]/1000)/8:.2f} Mbps Real Time Up{(result['vu']/1000)/8:.2f}".center(220))
               # print(end=("\r"))

          # print(f"YOUR PING:{ping}")
          # sys.exit()
        except:
             print("UFFF!! SERVER IS Soo BUSY TRYING PLEASE WAIT")
      #  sys.exit()
             continue
# # while 
print("TIME END")


      
   

#make the server available list and location 
#best server will get their work by choosing server
#find your longitude and latitude 
#make the time for loop and make the 1 time seperate loop
# after gave the result in the exel list
#use of Gui after that

# time.sleep(1)
# keyfinder=list(get_server.keys())
# for i in range(len(keyfinder)):
#  print(keyfinder[i])
# key1=keyfinder[0]


#  key=list(get_server.keys())
#  k1=(key[0])
#  official=(get_server[k1][1])
#  name=(f"{official['name']},{official['sponsor']}")
#  print(name)
 # close=(get_server[340.4131659494677])