import time
import random 

class Paper(object):
    # Creates stock attributes 
    Paper = 1000
    panic = False
    #def countdown(paper):

    #Data for the different variables that will be used.
    toilet_paper_stock = 3000
    toilet_paper_supply = 100
    toilet_paper_demand = 100
    panic_day_counter = 0
    day_counter = 0
    #Demo mode chooses if showing text or raw data if demo_mode = False data will be shown. If demo_mode = True text will be present
    demo_mode = 0
    print ("WELCOME TO THE TOILETPAPER HOARDING SIMULATOR BY LUKA!")
    print("Enter Usermode yes/no")
    x = input().lower()
    if x == ("yes"):
        demo_mode = True
    if x == ("no"):
        demo_mode = False
    else:
        demo_mode = True
    
    if demo_mode:
        print("Toilet paper left",toilet_paper_stock)
    while toilet_paper_stock > 0: 
        

      
        #Random counter for panic in toilet program for now p < 5 which activates pressmeeting
        p = random.randint(0,30)
        time.sleep(1)

        if p < 5:
            panic_day_counter = 0
            toilet_paper_demand += 150
            panic = True
            if panic == True: 
                if demo_mode:
                    print('PRESSMEETING')
            
            

                
        
            # input time in seconds for panic timer to end 
            t = 5
            
            # function call
            countdown(int(t),demo_mode)
        
        # create 10 variation
        v = random.randint(-10,10)

        #calculate factor
        f = 100/(100-v)
        #Calculating a random factor on the restock 
        toilet_paper_stock -= (toilet_paper_demand * f // 1)
        toilet_paper_stock += toilet_paper_supply
        #msg1 prints data if demo_mode is true and msg2 prints data for algebra programs where first number is days and second is the remaining stock
        msg1 = "Toiletpaper left",toilet_paper_stock
        msg2 = day_counter,toilet_paper_stock
        if demo_mode:
            print(msg1[0],msg1[1])
        else:
            print(msg2[0],",",msg2[1])

        #Debug info about counters that will show current value of the panic counter, toiletpaper demand and supply 
        #print(panic_day_counter,toilet_paper_demand,toilet_paper_supply)

        #starts day counter that counts days and displays end result at end
        day_counter +=1
        time.sleep(1)
        if toilet_paper_stock < 0:
            print ("Days until shortage",day_counter)
            break

            
        #Counter for when "Pressmeeting" startet that resets toilet_paper_demand
        if panic == True:
            panic_day_counter += 1
        #reseting to normal demand

        if panic_day_counter >= 3:
            toilet_paper_demand = 100
            panic_day_counter = 0
            panic = False
        
        #Increases supply if stock is lower than 2000
        if toilet_paper_stock < 2000:
            toilet_paper_supply = 150

        if toilet_paper_stock >= 3000:
            toilet_paper_supply = 100


    # define the countdown func.
    #Timer that will trigger if panic == True
        def countdown(t,demo_mode):
            
            while t:
                mins, secs = divmod(t, 60)
                timer2 = '{:02d}:{:02d}'.format(mins, secs)
                if demo_mode:
                    print(timer2, end="\r")
                time.sleep(1)
                t -= 1





